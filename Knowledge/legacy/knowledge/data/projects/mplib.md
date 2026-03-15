# Project: MPLIB

<!-- project-id: P1 -->
<!-- project-type: child -->
<!-- project-status: active -->
<!-- github-project: X -->
<!-- parent-project: P0 -->

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | P1 |
| **Name** | MPLIB |
| **Type** | child of P0 |
| **Repositories** | [packetqc/MPLIB](https://github.com/packetqc/MPLIB), [packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE](https://github.com/packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE) |
| **GitHub Project** | X |
| **Status** | 🟢 active |
| **Created** | X |
| **Knowledge Version** | v31 |
| **Parent Index** | P0/S1 |
| **Description** | High-throughput embedded systems library — SQLite log ingestion on ARM Cortex-M55, ThreadX RTOS, TouchGFX UI, PSRAM-backed dual buffers |

**Role in ecosystem**: MPLIB is the **original proof-of-concept** that validated Knowledge. The methodology, patterns, and pitfalls in P0 were largely discovered while building MPLIB. It is a child project — not a core asset.

---

## Publications

### In core (P0) — about this project

| Index | # | Title | Status |
|-------|---|-------|--------|
| P0/#1 | 1 | MPLIB Storage Pipeline | 🟢 published |

### Local publications

| Index | Title | Status |
|-------|-------|--------|
| P1/D1 | X | X |

---

## Satellites

| Index | Name | Repository | Version | Drift | Health |
|-------|------|------------|---------|-------|--------|
| P1/S1 | MPLIB main | [packetqc/MPLIB](https://github.com/packetqc/MPLIB) | v31 | 🟢 0 | 🟢 healthy |
| P1/S2 | MPLIB dev staging | [packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE](https://github.com/packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE) | v31 | 🟢 0 | 🟢 healthy |

---

## Evolution

| Date | Entry |
|------|-------|
| X | Project inception — MPLIB library for embedded systems |
| 2026-02-16 | First session with knowledge persistence (v1) |
| 2026-02-17 | Publication #1 — MPLIB Storage Pipeline documented |
| 2026-02-20 | MPLIB_DEV_STAGING satellite bootstrapped with iterative staging (v25) |
| 2026-02-21 | First successful cross-repo API bypass from knowledge session |
| 2026-02-22 | Decoupled from core — registered as child project P1 |

---

## Stories

| Date | Story |
|------|-------|
| X | 5-stage pipeline achieving ~2,650 logs/sec sustained across 400K+ rows |
| X | PSRAM dual-buffer architecture eliminating SD card I/O bottleneck |
| 2026-02-20 | MPLIB_DEV_STAGING: first satellite bootstrapped with v25 iterative staging |

---

## Technical Profile

| Property | Value |
|----------|-------|
| **Platform** | STM32N6570-DK (Cortex-M55 @ 800 MHz) |
| **RTOS** | ThreadX |
| **UI** | TouchGFX |
| **Database** | SQLite 3 (WAL mode, memsys5) |
| **Memory** | PSRAM (4 MB page cache) |
| **Performance** | ~2,650 logs/sec sustained |

---

## Required Assets Status

| Asset | Status | Notes |
|-------|--------|-------|
| CLAUDE.md | 🟢 active | Critical-subset, v31 |
| notes/ | 🟢 present | Session persistence active |
| live/ | 🟢 deployed | Knowledge assets synced |
| publications/ | X | Scaffold ready, no local pubs yet |
| docs/ | X | Web presence not yet created |
| GitHub Project | X | — |
