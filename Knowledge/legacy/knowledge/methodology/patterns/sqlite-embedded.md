# SQLite on Embedded Systems

Proven configuration and patterns for SQLite on resource-constrained RTOS targets with SD card storage.

## Configuration

### WAL Mode (Mandatory)
Write-Ahead Logging is required for concurrent read/write on SD card:

```sql
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;     -- FULL is too slow for SD card
PRAGMA locking_mode=NORMAL;    -- Allow concurrent readers
```

### Memory Allocator — memsys5
No malloc in embedded. Use SQLite's static allocator:

```c
// 512 KB static heap for SQLite
static uint8_t sqlite_heap[512 * 1024] __attribute__((section(".psram_buffers")));

sqlite3_config(SQLITE_CONFIG_HEAP, sqlite_heap, sizeof(sqlite_heap), 64);
```

### Page Cache in PSRAM
Dramatically reduces SD card I/O:

```c
// 4 MB page cache
static uint8_t page_cache[4 * 1024 * 1024] __attribute__((section(".psram_buffers")));

sqlite3_config(SQLITE_CONFIG_PAGECACHE, page_cache, 4096,
               sizeof(page_cache) / 4096);
```

## Prepared Statements

**Rule**: Prepare once at init, bind+step+reset in loop. Never re-prepare.

```c
// At init (once)
sqlite3_prepare_v2(db, "INSERT INTO logs VALUES(?,?,?)", -1, &insert_stmt, NULL);

// In hot loop (thousands of times)
sqlite3_bind_int(insert_stmt, 1, id);
sqlite3_bind_text(insert_stmt, 2, data, -1, SQLITE_STATIC);
sqlite3_step(insert_stmt);
sqlite3_reset(insert_stmt);    // CRITICAL: always reset after step
sqlite3_clear_bindings(insert_stmt);
```

### Reset Is Mandatory
Always `sqlite3_reset()` after `sqlite3_step()` returns `SQLITE_DONE`. Without reset:
- The statement holds a read/write lock on the database
- Subsequent statements may get `SQLITE_BUSY`
- WAL checkpoint will stall

## Transaction Batching

For high-throughput ingestion, batch inserts in transactions:

```c
sqlite3_exec(db, "BEGIN IMMEDIATE", NULL, NULL, NULL);  // IMMEDIATE for writes
for (int i = 0; i < batch_size; i++) {
    sqlite3_bind_...(...);
    sqlite3_step(insert_stmt);
    sqlite3_reset(insert_stmt);
}
sqlite3_exec(db, "COMMIT", NULL, NULL, NULL);
```

- **BEGIN IMMEDIATE**: acquires write lock upfront, prevents deadlocks
- **BEGIN DEFERRED**: for read-only queries, allows concurrent writers
- **Batch size**: 250-500 rows per transaction is the sweet spot on SD card

## WAL Checkpoint

```c
// Manual checkpoint — call during idle window (between buffer swaps)
sqlite3_wal_checkpoint_v2(db, NULL, SQLITE_CHECKPOINT_PASSIVE, &nLog, &nCkpt);
```

### Checkpoint Rules
- **Don't checkpoint during burst ingestion** — wait for buffer swap idle
- **PASSIVE mode**: doesn't block writers, may not fully checkpoint (acceptable)
- **After checkpoint**: call `fx_media_flush()` (FileX) to ensure SD card write-through
- **Auto-checkpoint**: set WAL size threshold, not time interval

## FileX VFS Integration

SQLite on STM32 uses a custom VFS that maps to FileX (ThreadX file system):

- `xOpen` → `fx_file_open`
- `xRead` → `fx_file_read`
- `xWrite` → `fx_file_write`
- `xSync` → `fx_media_flush` (critical for data persistence)
- `xFileSize` → `fx_file_seek` to end + `fx_file_tell`

**Critical**: `fx_media_flush()` after checkpoint is mandatory. Without it, data lives in FileX cache only and is lost on power cycle.

## Performance Reference

On STM32N6570-DK (Cortex-M55 @ 800 MHz), PSRAM cache, Class 10 SD:
- **Ingestion**: ~2,650 logs/sec sustained (224-byte records)
- **Batch read**: 50 records in < 5 ms from PSRAM cache
- **WAL checkpoint**: ~200 ms for 10,000 pending records
- **Total capacity tested**: 400,000+ rows without degradation
