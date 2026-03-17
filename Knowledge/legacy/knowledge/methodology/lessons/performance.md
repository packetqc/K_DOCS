# Performance — What We Measured, What Worked

Real measurements from STM32N6570-DK (Cortex-M55 @ 800 MHz), ThreadX, SD card Class 10, PSRAM.

## Ingestion Pipeline

### Sustained Throughput
- **2,650 logs/sec** sustained across 400,000+ rows
- Record size: 224 bytes (DS_LOG_STRUCT, 32-byte aligned)
- Batch size: 250 records per transaction
- WAL mode, synchronous=NORMAL

### What Made It Fast
1. **Prepared statements** — prepare once, bind+step+reset in loop. Re-preparing drops to ~400 logs/sec.
2. **Transaction batching** — 250 rows per BEGIN/COMMIT. Without batching: ~50 logs/sec (SD card sync per row).
3. **PSRAM page cache** — 4 MB page cache in PSRAM. Without it: ~800 logs/sec (cache misses hit SD card).
4. **Dual-buffer architecture** — producer never waits for consumer. No pipeline stalls.
5. **WAL mode** — readers don't block writers. Without WAL: UI queries stall ingestion.

### What Didn't Help
- Increasing batch size beyond 500 — diminishing returns, higher latency
- `synchronous=OFF` — marginal speed gain, unacceptable data loss risk
- Multiple insert threads — SD card is the bottleneck, more threads = more contention

## Read Performance

### Batch Read (Backend → PSRAM)
- **50 records in < 5 ms** from PSRAM page cache (cache hit)
- **50 records in ~25 ms** from SD card (cache miss, first page load)
- Prefetch cache eliminates visible latency on sequential page turns

### UI Rendering (PSRAM → Screen)
- **< 1 ms** to render 10 visible rows from PSRAM viewable buffer
- Zero SQL in render path — PSRAM memcpy only
- 60 FPS maintained during active scrolling

## WAL Checkpoint

- **~200 ms** for 10,000 pending records (PASSIVE mode)
- **~500 ms** for 25,000 pending records
- Checkpoint during buffer swap idle window — no visible impact on ingestion
- `fx_media_flush()` adds ~50 ms (SD card write-through)

## Memory Budget

| Resource | Size | Location |
|----------|------|----------|
| SQLite heap (memsys5) | 512 KB | PSRAM |
| Page cache | 4 MB | PSRAM |
| Dual buffers (A+B) | 2 × 56 KB | PSRAM |
| Viewable buffer | 11.2 KB | PSRAM |
| Prefetch cache (4 slots) | 44.8 KB | PSRAM |
| Thread stacks (all) | ~32 KB | DTCM |
| **Total PSRAM** | **~4.7 MB** | — |

## Scaling Observations

- **Linear ingestion**: rate stays constant from 0 to 400K+ rows (B-tree insertion is O(log n), but SD card I/O dominates)
- **Read scales with cache**: first read of a page range is slow (SD), subsequent reads are fast (PSRAM cache)
- **WAL file growth**: checkpointing at 10K intervals keeps WAL file manageable (~2-3 MB peak)
- **SD card wear**: WAL + checkpoint pattern concentrates writes to WAL region. Consider wear leveling for production.
