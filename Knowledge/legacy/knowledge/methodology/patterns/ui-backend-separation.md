# UI / Backend Separation Pattern

The absolute rule: **GUI thread NEVER executes SQL.** This pattern ensures responsive UI on RTOS targets.

## Architecture

```
┌─────────────────┐    PSRAM Buffer    ┌──────────────────┐
│   GUI Thread     │◄──────────────────│  Backend Thread   │
│  (TouchGFX)      │  viewable_buffer  │  (SQLite + WAL)   │
│                  │     [50 rows]     │                    │
│  Reads buffer    │                   │  Writes buffer     │
│  Renders list    │                   │  Manages cache     │
│  Handles touch   │                   │  Checkpoints WAL   │
└─────────────────┘                    └──────────────────┘
         │                                      │
         │          Event Flags                  │
         └──────────────────────────────────────┘
              PAGE_NEXT / PAGE_PREV / REFRESH
```

## Mediator Pattern

A parent container (CC_MPLIB_STORAGE) owns the data flow between UI widgets and backend:

```
CC_MPLIB_STORAGE (mediator)
  ├── ListViewLogsStored (UI widget — renders PSRAM data, zero SQL)
  ├── LogItem (single row renderer)
  └── LogDBUpdaterThread (backend — PSRAM sync + prefetch)
```

### Data Flow
1. User taps "Next Page" → UI sends event to mediator
2. Mediator sets `FLAG_PAGE_NEXT` on backend event flags
3. Backend reads next 50 rows from SQLite into `viewable_buffer[]`
4. Backend sets `FLAG_DATA_READY` on UI event flags
5. Mediator tells ListViewLogsStored to re-render from `viewable_buffer[]`
6. ListViewLogsStored reads PSRAM directly — no SQL, no mutex, no blocking

### Why This Works
- GUI thread never blocks on SD card I/O
- Touch events are always responsive (< 16 ms frame budget)
- Backend can do expensive operations (checkpoint, batch read) without UI stutter
- PSRAM access is fast enough for direct rendering (< 1 μs per read)

## Prefetch Cache

4-slot PSRAM neighbor page cache for instant page turns:

```
┌──────────┬──────────┬──────────┬──────────┐
│ slot[0]  │ slot[1]  │ slot[2]  │ slot[3]  │
│ FIRST    │ PREV     │ NEXT     │ LAST     │
│ page     │ page     │ page     │ page     │
└──────────┴──────────┴──────────┴──────────┘
```

- When current page is displayed, backend pre-loads adjacent pages
- On page turn, swap cache slot → viewable_buffer, start pre-loading new neighbors
- Result: page turns appear instant (PSRAM copy vs SD card read)

## Thread Safety Rules

1. **Never call `invalidate()` from non-GUI thread** — use `OSWrappers::signalVSync()` to request redraw
2. **Never access UI widgets from backend thread** — only write to shared PSRAM buffers
3. **PSRAM buffers are the contract** — backend writes, frontend reads, event flags synchronize
4. **No mutex on viewable_buffer** — backend writes complete buffer before signaling ready, frontend reads only after signal. Double-buffering avoids torn reads.
