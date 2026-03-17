# Embedded Debugging Patterns

Proven debugging techniques for bare-metal and RTOS-based embedded systems.

## Printf Diagnostics

The fastest debug loop on embedded targets. Add UART trace output to understand runtime behavior without altering module logic.

### Rules
- **Never remove printf after debugging** — wrap in `#if DEBUG` or leave as-is
- **Keep the infrastructure** — once a trace point works, it's permanent instrumentation
- **Don't change logic to add printf** — insert trace lines between existing statements
- **Include context in output**: function name, variable values, state transitions

### Patterns
```c
// State transition trace
printf("[STORAGE] State: %s -> %s\n", state_name(old), state_name(new));

// Performance measurement
uint32_t t0 = HAL_GetTick();
sqlite3_step(stmt);
printf("[SQL] INSERT took %lu ms\n", HAL_GetTick() - t0);

// Buffer swap trace
printf("[DUAL_BUF] Swap: buf_%c full (%lu entries), switching to buf_%c\n",
       active == 0 ? 'A' : 'B', count, active == 0 ? 'B' : 'A');

// Thread lifecycle trace
printf("[THREAD:%s] Started, stack=%lu, priority=%u\n", name, stack_size, priority);
```

### Stack Warning
Printf with float formatting (`%f`, `%e`) needs 2 KB+ thread stack. Set ThreadX thread stacks accordingly or use integer-scaled output:
```c
// Instead of: printf("Rate: %.2f logs/sec\n", rate);
printf("Rate: %lu.%02lu logs/sec\n", (uint32_t)rate, (uint32_t)(rate * 100) % 100);
```

## Screenshots as Data

Screen captures from the running device are primary data sources, not supplementary.

### What to Extract
- **UART terminal output**: every line, every value, every timestamp
- **UI state**: active tab, page number, entry range, button states
- **Timing values**: ms counters, rate displays, elapsed time
- **Error indicators**: red text, error codes, fault icons
- **State consistency**: does the UI match the UART output?

### Analysis Flow
1. Read the image at full resolution
2. Extract ALL text visible (UART logs, UI labels, status bars)
3. Compare extracted values against expected behavior
4. Flag inconsistencies between UI state and serial output
5. Note any visual artifacts (rendering glitches, partial updates)

## UART Log Analysis

When UART output is captured (screenshot or video):

### Key Things to Watch
- **Boot sequence**: init order, timing between stages, any stalls
- **Error messages**: any line containing "Error", "Fault", "FAIL", "assert"
- **Performance counters**: logs/sec, ms per operation, queue depths
- **State machines**: transitions that don't follow expected sequence
- **Memory reports**: heap usage, stack high-water marks, PSRAM allocation
