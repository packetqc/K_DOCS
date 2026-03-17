---
layout: publication
title: "MPLIB Storage — High-Throughput SQLite Log Ingestion on Cortex-M55"
description: "5-stage pipeline achieving ~2,650 logs/sec sustained on bare-metal ARM Cortex-M55 (STM32N6570-DK). PSRAM dual buffers, WAL-mode SQLite, zero-SQL GUI frontend, ThreadX RTOS."
pub_id: "Publication #1"
version: "v1"
date: "2026-02-19"
permalink: /publications/mplib-storage-pipeline/
og_image: /assets/og/mplib-pipeline-en-cayman.gif
keywords: "embedded, SQLite, RTOS, ThreadX, pipeline, dual-buffer, PSRAM"
---

# MPLIB Storage — High-Throughput SQLite Log Ingestion on Cortex-M55
{: #pub-title}

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | System overview and pipeline summary |
| [Key Metrics](#key-metrics) | Throughput, memory, and cache figures |
| [Architecture](#architecture) | 5-stage pipeline and frontend/backend separation |
| [Technology Stack](#technology-stack) | MCU, RTOS, database, and storage components |

## Abstract

MPLIB Storage is a high-throughput SQLite log ingestion pipeline designed for bare-metal ARM Cortex-M55 systems. Running on the STM32N6570-DK (800 MHz), it achieves **~2,650 logs/sec sustained** across 400K+ rows using a 5-stage pipeline architecture with PSRAM-backed dual buffers, WAL-mode SQLite, and a zero-SQL GUI frontend.

## Key Metrics

| Metric | Value |
|--------|-------|
| Sustained write rate | ~2,650 logs/sec |
| Total rows tested | 400,000+ |
| Log struct size | 224 bytes, 32-byte aligned |
| Buffer pair memory | 7.2 MB (PSRAM) |
| SQLite heap | 512 KB (memsys5) |
| Page cache | 4 MB (~965 pages) |

## Architecture

**5-stage pipeline**: Generate → DualBuffer (PSRAM) → Ingest (SQLite) → WAL Engine → SD Card

**Frontend/backend separation**: GUI thread never executes SQL — reads from PSRAM buffer populated by backend thread. Prefetch cache with 4 slots (next/prev/first/last) hides query latency.

## Technology Stack

| Component | Technology |
|-----------|-----------|
| MCU | STM32N6570-DK (Cortex-M55 @ 800 MHz) |
| RTOS | ThreadX |
| UI | TouchGFX |
| Database | SQLite 3 (WAL mode, memsys5 allocator) |
| Storage | SD Card via SDMMC2 / FileX |

---

[**Read the full documentation →**]({{ '/publications/mplib-storage-pipeline/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
