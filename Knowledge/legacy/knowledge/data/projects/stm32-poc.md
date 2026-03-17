# Project: STM32 PoC

<!-- project-id: P2 -->
<!-- project-type: child -->
<!-- project-status: active -->
<!-- github-project: https://github.com/users/packetqc/projects/6 -->
<!-- parent-project: P0 -->

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | P2 |
| **Name** | STM32 PoC |
| **Type** | child of P0 |
| **Repository** | [packetqc/STM32N6570-DK_SQLITE](https://github.com/packetqc/STM32N6570-DK_SQLITE) |
| **GitHub Project** | [#6](https://github.com/users/packetqc/projects/6) |
| **Status** | 🟢 active |
| **Created** | X |
| **Knowledge Version** | v31 |
| **Parent Index** | P0/S2 |
| **Description** | STM32N6570-DK proof-of-concept — SQLite integration, ThreadX RTOS, embedded database on Cortex-M55 |

**Role in ecosystem**: Hardware proof-of-concept for the MPLIB library. Tests SQLite, PSRAM, TouchGFX, and ThreadX integration on real hardware. Source of Publication #1 data.

---

## Publications

### In core (P0) — about this project

| Index | # | Title | Status |
|-------|---|-------|--------|
| P0/#1 | 1 | MPLIB Storage Pipeline | 🟢 published (shared with P1) |

### Local publications

| Index | Title | Status |
|-------|-------|--------|
| P2/D1 | doc/readme.md | X (detected by harvest, not yet promoted) |

---

## Satellites

| Index | Name | Repository | Version | Drift | Health |
|-------|------|------------|---------|-------|--------|
| P2/S1 | STM32N6570-DK_SQLITE | [packetqc/STM32N6570-DK_SQLITE](https://github.com/packetqc/STM32N6570-DK_SQLITE) | v31 | 🟢 0 | 🟢 healthy |

---

## Evolution

| Date | Entry |
|------|-------|
| X | Project inception — STM32N6570-DK hardware PoC |
| 2026-02-18 | First harvest — patterns and pitfalls extracted to core |
| 2026-02-22 | Registered as child project P2 |

---

## Stories

| Date | Story |
|------|-------|
| X | SQLite WAL mode validated on SD card via ThreadX FileX |
| X | PSRAM memsys5 allocator — bounded memory, no malloc |

---

## Required Assets Status

| Asset | Status | Notes |
|-------|--------|-------|
| CLAUDE.md | 🟢 active | Critical-subset, v31 |
| notes/ | 🟢 present | 3 session files |
| live/ | 🟢 deployed | Knowledge assets synced |
| publications/ | X | 1 detected (doc/), not promoted |
| docs/ | X | Web presence not yet created |
| GitHub Project | 🟢 [#6](https://github.com/users/packetqc/projects/6) | Created 2026-02-22 |
