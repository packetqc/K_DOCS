# STM32N6570-DK_SQLITE

## Harvest Metadata
| Field | Value |
|-------|-------|
| Repo | [packetqc/STM32N6570-DK_SQLITE](https://github.com/packetqc/STM32N6570-DK_SQLITE) |
| Last harvest | 2026-02-22 |
| Branches scanned | main |

### Branch Cursors
| Branch | Last harvested SHA | Date |
|--------|-------------------|------|
| main | 5a0840d63911d62a614c146ebfa83f06ce297f30 | 2026-02-21 |

---

## Knowledge Version
| Field | Value |
|-------|-------|
| Satellite version | **v31** |
| Core version | v35 |
| Drift | 4 🟠 |
| Missing features | v32 recall + contextual help, v33 PAT access levels, v34 secure textarea delivery, v35 project entity model |
| Last remediated | 2026-02-21 (harvest --fix via API — critical-subset deployed) |

---

## Knowledge Status
| Check | Status | Detail |
|-------|--------|--------|
| Bootstrap | 🟢 **active** | CLAUDE.md references packetqc/knowledge with `<!-- knowledge-version: v31 -->` — critical-subset (~240 lines) |
| Session persistence | 🟢 **active** | notes/ with 3 session files (2026-02-19 bootstrap, 2026-02-19-v22 update, 2026-02-21-v31 upgrade) |
| Live tooling | 🟢 **deployed** | live/ fully synced — beacon (`knowledge_beacon.py`), scanner (`knowledge_scanner.py`), capture (`stream_capture.py`), `dynamic/`, `static/` |
| Own knowledge | **rich** | doc/readme.md (15,666 bytes) has complete architecture docs, runtime data, degradation analysis |
| Publications | **detected** | doc/readme.md = source material for Publication #1 (already published) |
| Health | **healthy** | Repo reachable, all branches scanned, PR #1 merged |

---

## Bootstrap Event — 2026-02-19

PR #1 (`claude/read-packetqc-knowledge-E50zO` → main) merged 2026-02-19T04:58:37Z:
- Created CLAUDE.md with v11 bootstrap tag, project overview, architecture decisions, 4 project-specific pitfalls
- Created notes/session-2026-02-19.md (bootstrap session — sunglasses on)
- Satellite is now self-sustaining — next wakeup inherits methodology, commands, session persistence
- Session link: [redacted — session expired]

---

## Project Overview

**High-throughput SQLite logging on STM32N6570-DK** — 2,800 logs/sec sustained into SQLite on SD card from bare-metal Cortex-M55 @ 800 MHz with zero data loss and bounded memory. The entire pipeline — from log generation through SQLite insertion to SD card persistence — runs on a single board.

### Key Metrics
| Metric | Value |
|--------|-------|
| Sustained ingestion rate | ~2,600-2,800 logs/sec |
| Peak rate (cold cache) | 3,272 logs/sec |
| Log struct size | 224 bytes (cache-aligned) |
| Effective throughput | ~600 KB/s structured data into SQLite |
| Data loss | 0 (backpressure-guaranteed) |
| SQLite heap usage | ~15-27 KB / 1 MB (< 3%) |
| PSRAM used | ~12.2 MB / 32 MB available |
| Total capacity tested | 400,000+ rows without degradation (with 4 MB cache fix) |

### Hardware
- MCU: STM32N657X0H3QU — Cortex-M55 @ 800 MHz
- PSRAM: APS256XX — 32 MB XSPI @ 200 MHz
- SD Card: SDMMC2 — 4-bit @ 50 MHz (Class 10 U1)
- RTOS: ThreadX (Azure RTOS)
- Filesystem: FileX

---

## Claude Instructions

CLAUDE.md exists (100 lines, v22). Key sections:
- Knowledge Base bootstrap referencing packetqc/knowledge
- Project overview with hardware specs
- Architecture decisions (5 key decisions)
- Thread priority scheme (3 threads)
- PSRAM memory layout (4 sections starting 0x90000000)
- 4 project-specific pitfalls
- Quick Commands placeholder (none yet)

---

## Evolved Patterns

### 1. PSRAM Double-Buffer with 4-Flag ThreadX Protocol
**Status**: Already captured in core `patterns/rtos-integration.md`

4-flag protocol (READY_A `0x01`, READY_B `0x02`, FREE_A `0x04`, FREE_B `0x08`) for zero-loss backpressure between producer and consumer threads. Producer blocks on `TX_WAIT_FOREVER` when both buffers full. Consumer clears READY bit and sets FREE bit atomically after COMMIT. The `__DSB()` barrier before signaling ensures all PSRAM writes are visible before the consumer reads.

Key implementation detail from `captureLog()`:
```cpp
// 1. SYNC: Finalize PSRAM writes before signaling
__DSB();
// 2. SIGNAL: Tell ingestor this buffer is full
tx_event_flags_set(&staging_events, ready_flag, TX_OR);
// 3. BACKPRESSURE: Block until OTHER buffer is free
tx_event_flags_get(&staging_events, next_free, TX_AND_CLEAR, &actual_f, TX_WAIT_FOREVER);
// 4. SWAP: Switch to the now-free standby buffer
active_fill_buffer = (active_fill_buffer == psram_buffer_A) ? psram_buffer_B : psram_buffer_A;
```

### 2. Page Cache Sizing to Prevent B-Tree Degradation
**Status**: PROMOTION CANDIDATE — not yet in core lessons

96-page (393 KB) cache caused **81% throughput collapse** at 4M rows (3,272 -> 533 l/s). Root cause: B-tree at 5-6 levels, interior pages evicted, every insert triggers SD random reads (0.5-2 ms each). Fix: scale cache to ~965 pages (4 MB) keeping ALL interior pages hot.

Formula: `cache_slots = total_psram_budget / (page_size + pcache_header_overhead)`
Where `pcache_header_overhead` is ~256 bytes on STM32 (this is the slot size mismatch pitfall below).

### 3. memsys5 + PSRAM Page Cache Separation
**Status**: Already captured in core `patterns/sqlite-embedded.md`

Two distinct PSRAM pools: 1 MB heap (memsys5, 64-byte granularity) and 4 MB page cache (4,352-byte slots). Heap stays under 3% utilization when page cache absorbs all B-tree page management. Must be configured pre-`sqlite3_initialize()`:
```c
sqlite3_config(SQLITE_CONFIG_PAGECACHE, sqlite_pcache, PCACHE_SLOT_SIZE, slot_count);
sqlite3_config(SQLITE_CONFIG_HEAP, sqlite_heap, sizeof(sqlite_heap), 64);
sqlite3_config(SQLITE_CONFIG_MEMSTATUS, 1);  // Enable runtime stats
sqlite3_initialize();  // Locks config
```

### 4. Cache-Aligned 224-Byte Log Struct
**Status**: Already captured in core `lessons/pitfalls.md` (#1)

`DS_LOG_STRUCT` at exactly 224 bytes = 7 x 32-byte cache lines on Cortex-M55. `__attribute__((packed, aligned(32)))`. Includes 16-byte reserved field for future expansion while maintaining exact cache-line alignment.

### 5. Passive WAL Checkpoint on Buffer Drain Cadence
**Status**: Already captured in core `patterns/sqlite-embedded.md`

`wal_autocheckpoint = 0` (disabled). Manual `SQLITE_CHECKPOINT_PASSIVE` every 5 buffer drains. Aligned with buffer swap idle windows. The idle window between buffer COMMIT and next buffer READY is the natural checkpoint slot.

### 6. Direct PSRAM-to-SQLite Ingestor (Bypass Raw Files)
**Status**: New pattern — not yet in core

Two ingestion strategies implemented:
- **Raw file path**: PSRAM -> DMA -> SRAM landing zone -> raw file on SD -> read back -> SQLite insert. More resilient to crashes but slower.
- **Direct path** (`ingestor_direct()`): PSRAM -> DCache invalidate -> SQLite bind/step directly from PSRAM buffer. No intermediate files. Single `BEGIN TRANSACTION` per 16,384-row buffer, single `COMMIT`. Faster, simpler, fewer failure modes.

The direct path won. Key insight: `SQLITE_STATIC` binding tells SQLite not to copy the data — it reads directly from the PSRAM buffer pointer. This eliminates one entire memcpy layer.

### 7. DMA with Polling Fallback for PSRAM-to-SRAM Transfers
**Status**: New pattern — not yet in core

For the raw-file path, GPDMA1 Channel 0 performs mem-to-mem transfers from PSRAM to AXI SRAM landing zone. If DMA fails (start error or poll timeout), falls back to `memcpy()`. Production code should not need this fallback, but having it prevents hard failures during development.

### 8. Database Recovery Protocol
**Status**: New pattern — not yet in core

When `SQLITE_CORRUPT` or `SQLITE_NOTADB` detected during ingestion:
1. Finalize prepared statement
2. Close database handle (with `sqlite3_interrupt()` + retry on SQLITE_BUSY)
3. Flush FileX media
4. Delete corrupted database + WAL + SHM files
5. Recreate database, apply pragmas, recreate table
6. Close database (let ingestor thread reopen on next iteration)
7. Reset state without resetting counters (pipeline continues from where it left off)

The recovery is designed to be non-fatal — pipeline pauses, recovers, and resumes. No reboot needed.

---

## New Pitfalls

### 1. Printf Latency in Hot Path — PROMOTION CANDIDATE
**Impact**: 1-5 ms per `printf()` call at 2,800 logs/sec (115200 baud UART)
**Context**: Debug output in the ingestion loop (`bindAndStep`) and transaction commit. Each call blocks the ingestion thread for UART transmission time.
**Distinct from**: Pitfall #2 in core (stack overflow in printf). This is about latency, not stack.
**Fix**: Remove from production, or gate with `#if DEBUG_INGESTION`. Keep the `STATS BLOCK` prints (every 5 seconds) — those are valuable diagnostics.
**Candidate for**: `lessons/pitfalls.md` as new entry #13

### 2. Page Cache Slot Size Mismatch — PROMOTION CANDIDATE
**Impact**: memsys5 malloc failures, SQLite falls back to heap for every page operation
**Context**: Setting `SQLITE_CONFIG_PAGECACHE` with `slot_size = page_size (4096)` is wrong. SQLite adds a per-slot header (~256 bytes). Correct slot size: `page_size + 256 = 4352`.
**Evidence**: With 4096-byte slots, SQLite silently rejected the PSRAM page cache and used the 1 MB heap instead. Heap utilization was anomalously high until the slot size was corrected.
**Candidate for**: `lessons/pitfalls.md` as new entry #14

### 3. SD Card Class 10 U1 as Throughput Ceiling
**Impact**: Theoretical sequential 15 MB/s, but random read latency (0.5-2 ms) during WAL checkpoint or cache miss is the real limiter
**Context**: The 2,800 l/s ceiling at 224 bytes/log (~628 KB/s) is CPU-bound early, then SD-bound late. At scale, random reads for B-tree page fetches dominate.
**Status**: Informational — not a bug, just a hardware constraint to document

### 4. SQLITE_CONFIG Before sqlite3_initialize() Is Mandatory
**Impact**: Configuration silently ignored if called after initialization
**Context**: `sqlite3_shutdown()` must be called first to allow reconfiguration, then `SQLITE_CONFIG_PAGECACHE`, `SQLITE_CONFIG_HEAP`, `SQLITE_CONFIG_MEMSTATUS`, then `sqlite3_initialize()` to lock the config.
**Status**: Informational — already implicit in core patterns, but worth making explicit

---

## Methodology Progress

### MPLIB-CODE Singleton Module Pattern
Self-contained `MPLIB_STORAGE.cpp/.h` with `CreateInstance()` static factory. Thread entry points as C-linkage `extern "C"` functions delegating to instance methods:
```cpp
extern "C" void ingestion_direct_thread_entry(unsigned long thread_input) {
    STORAGE->ingestor_direct(0);
}
```

### Thread Priority Scheme
| Thread | Priority | Stack | Role |
|--------|----------|-------|------|
| Ingestor Direct | 5 (highest) | 80 KB | PSRAM -> SQLite critical path |
| Storage Worker | 8 (mid) | 12 KB | Service loop (dormant in direct mode) |
| Simulator | 15 (lowest) | 4 KB | Log generation, yields to ingestor |

Higher priority = lower number = more CPU time. The ingestor gets the CPU whenever it needs it because it's the bottleneck.

### Linker Section Architecture for PSRAM
Four distinct PSRAM sections, each 32-byte aligned:
```
0x90000000  .psram_cache    - 4 MB SQLite page cache (965 x 4352-byte slots)
            .psram_buffers  - Custom buffers section
            .psram_logs     - 7.2 MB double buffers (2 x 16384 x 224 bytes)
            .psram_data     - 1 MB SQLite memsys5 heap
```
Plus `.SqlPoolSection` in AXI SRAM for thread stacks and DMA landing zone (128 KB).

### SQLite PRAGMA Tuning for Maximum Throughput
```sql
PRAGMA page_size          = 4096       -- Match SD sector / pcache slot
PRAGMA journal_mode       = WAL        -- Write-Ahead Logging
PRAGMA synchronous        = OFF        -- No fsyncs (data loss on power-fail OK)
PRAGMA cache_size         = -4096      -- 4 MB PSRAM page cache
PRAGMA locking_mode       = EXCLUSIVE  -- Single-writer, no contention
PRAGMA temp_store         = MEMORY     -- Temp in PSRAM, not SD
PRAGMA journal_size_limit = 4194304    -- 4 MB WAL cap
PRAGMA wal_autocheckpoint = 0          -- Manual PASSIVE every 5 buffers
PRAGMA auto_vacuum        = NONE       -- No fragmentation overhead
```

### SQLite Azure RTOS Integration Layer
`sqlite3_azure.c/h` provides the FileX VFS bridge. `sqlite3_azure_fx_user.h` extends `FX_FILE` with locking fields for thread safety:
```c
#define FX_FILE_MODULE_EXTENSION unsigned open_count;         \
                                 int delete_on_close;         \
                                 unsigned shared_locks_count; \
                                 int lock_type;               \
                                 TX_THREAD* lock_task;        \
                                 TX_MUTEX mutex;
```

---

## Publications Detected
| Title | Path (in satellite) | Status |
|-------|---------------------|--------|
| Architecture doc (source for Publication #1) | doc/readme.md | **published** — already in core as publications/mplib-storage-pipeline/v1/ |
| Mermaid pipeline diagram | doc/architecture.mmd | **referenced** — 5-stage pipeline diagram with color-coded subgraphs |
| Video demo | doc/2026 N6 TESTS SQLITE POC.mp4 | reference only (752 KB) |
| Mermaid degradation diagram | doc/readme.md (inline) | **referenced** — B-tree growth -> cache eviction -> SD random reads |

---

## Promotion Candidates

| # | Insight | Target | Status |
|---|---------|--------|--------|
| 1 | **Page cache sizing degradation** — 81% throughput collapse when B-tree interior pages evicted at 4M rows. Scale cache to hold all interior pages. | `lessons/pitfalls.md` | Ready for review |
| 2 | **Printf latency in hot path** — 1-5 ms per call at 2,800 l/s on 115200 baud UART. Gate with `#if DEBUG`. | `lessons/pitfalls.md` | Ready for review |
| 3 | **Slot size mismatch** — pcache slot must be `page_size + 256`, not just `page_size`. Silent fallback to heap. | `lessons/pitfalls.md` | Ready for review |
| 4 | **Direct PSRAM-to-SQLite bypass** — skip raw file intermediate step, use `SQLITE_STATIC` binding to read directly from PSRAM. | `patterns/sqlite-embedded.md` | Ready for review |
| 5 | **Database recovery protocol** — non-fatal recovery from corruption: finalize, close, flush, delete, recreate, resume. | `patterns/sqlite-embedded.md` | Ready for review |
| 6 | **sqlite3_shutdown() before reconfiguration** — must shutdown, reconfigure, then re-initialize. Config calls are ignored after init. | `lessons/pitfalls.md` | Ready for review |
