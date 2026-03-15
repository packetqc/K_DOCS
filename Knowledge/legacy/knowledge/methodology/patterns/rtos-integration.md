# RTOS Integration Patterns (ThreadX)

Proven patterns for ThreadX (Azure RTOS) on STM32 Cortex-M targets.

## Thread Architecture

### Singleton Module Pattern
Each hardware/software module is a singleton class with its own ThreadX thread:

```cpp
class MPLIB_MODULE {
    static MPLIB_MODULE* instance;
    TX_THREAD thread;
    TX_EVENT_FLAGS_GROUP event_flags;
    TX_MUTEX mutex;

    static void Services_MODULE(ULONG arg);  // ThreadX entry point (unique name!)
public:
    static MPLIB_MODULE* getInstance();
    void init();
    void start();
};
```

**Critical**: Thread entry points MUST have unique names (`Services_STORAGE`, `Services_GPS`, etc.). ThreadX does not support duplicate entry point names.

### Static Allocation
All RTOS objects are statically allocated. No `malloc` in RTOS context:

```cpp
// Thread stack — statically allocated, placed in appropriate memory section
static UCHAR thread_stack[4096] __attribute__((section(".psram_buffers")));

// Event flags, mutexes, semaphores — declared as class members, not dynamically created
TX_EVENT_FLAGS_GROUP flags;
TX_MUTEX mutex;
```

## Inter-Thread Communication

### Event Flags (Preferred)
For simple ready/not-ready signaling between threads:

```cpp
#define FLAG_BUF_A_READY  0x01
#define FLAG_BUF_B_READY  0x02
#define FLAG_SHUTDOWN      0x04

// Producer sets flag
tx_event_flags_set(&flags, FLAG_BUF_A_READY, TX_OR);

// Consumer waits for any buffer ready
ULONG actual_flags;
tx_event_flags_get(&flags, FLAG_BUF_A_READY | FLAG_BUF_B_READY,
                   TX_OR_CLEAR, &actual_flags, TX_WAIT_FOREVER);
```

### Mutex (For Shared Data)
When multiple threads access the same data structure:

```cpp
tx_mutex_get(&db_mutex, TX_WAIT_FOREVER);
// ... access shared resource ...
tx_mutex_put(&db_mutex);
```

**Rule**: Keep mutex hold time minimal. Never call SQLite operations inside a mutex that UI thread needs.

## Dual-Buffer Architecture

The core pattern for high-throughput data ingestion:

```
Producer Thread          Consumer Thread
     |                       |
     v                       v
  Fill Buffer A    ←→    Drain Buffer B
     |                       |
  [threshold]           [complete]
     |                       |
  Swap A↔B              Swap B↔A
     |                       |
  Fill Buffer B    ←→    Drain Buffer A
```

### Implementation Keys
- Buffers in PSRAM (`.psram_buffers` linker section) for size
- Threshold-based swap, not time-based
- Event flags signal swap completion
- Producer never waits for consumer (drops if both full — rare with proper sizing)

## Memory Placement

### Linker Sections
```
.psram_buffers    — Large buffers (dual-buffer arrays, page cache)
.psram_bss        — PSRAM zero-init variables
.dtcm             — Fast-access variables (counters, flags)
```

### Alignment
- `DS_LOG_STRUCT`: 224 bytes, 32-byte aligned — MPU requirement
- PSRAM buffers: 32-byte aligned minimum
- DMA buffers: cache-line aligned (32 bytes on Cortex-M55)

```cpp
typedef struct __attribute__((packed, aligned(32))) {
    uint32_t id;
    char data[220];
} DS_LOG_STRUCT;
```
