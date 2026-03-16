---
layout: publication
title: "Distributed Knowledge Dashboard — Master Mind and Satellite Network Status"
description: "Living dashboard tracking the distributed knowledge network: master mind version, satellite project status, version drift, harvested insights, and discovered publications. Updated on every K_GITHUB sync."
pub_id: "Publication #4a"
version: "v3"
date: "2026-03-16"
permalink: /publications/distributed-knowledge-dashboard/
og_image: /assets/og/knowledge-dashboard-en-cayman.gif
keywords: "dashboard, satellites, healthcheck, drift, severity, network status"
---

# Distributed Knowledge Dashboard — Master Mind and Satellite Network Status
{: #pub-title}

> **Parent publication**: [#4 — Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }}) — the architecture this dashboard visualizes | **Core reference**: [#14 — Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/publications/knowledge-2.0/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Living dashboard concept and purpose |
| [Satellite Network](#satellite-network) | Real-time satellite inventory with severity icons |
| [Acquired Knowledge](#acquired-knowledge) | Harvested insights with promotion workflow |
| [Discovered Publications](#discovered-publications) | Technical content found in satellite repos |
| [Master Mind Status](#master-mind-status) | Core repository version and statistics |
| [The Network](#the-network) | Components and their roles |
| [Knowledge Layers](#knowledge-layers) | Core, proven, harvested, session hierarchy |
| [Lifecycle of an Insight](#lifecycle-of-an-insight) | From session note to core knowledge |

## Abstract

AI coding assistants gain persistent memory through `mind_memory.md` and `sessions/` — but each project evolves independently. The **distributed knowledge system** connects them: a master mind pushes the K_MIND module to satellites on session start, and K_GITHUB `sync_github.py` syncs evolved knowledge back.

This publication is a **living dashboard** — updated on every K_GITHUB sync. It is the network's self-awareness.

## Satellite Network

> Updated on every K_GITHUB sync. Only includes repositories that the user owns and that Claude Code has been granted access to — no external or third-party repos.

<div class="table-wrap" markdown="1">

| Satellite | Version | Drift | Bootstrap | Sessions | Assets | Live | Pubs | Health | Last Harvest |
|-----------|---------|-------|-----------|----------|--------|------|------|--------|--------------|
|[knowledge](https://github.com/packetqc/knowledge) (self)|v47|🟢 0|🟢 **core**|🟢 16|🟢 core|🟢 1| healthy | 2026-03-03 |2026-02-23|
|[MPLIB](https://github.com/packetqc/MPLIB)|v31|🔴 16|🟢 active|🟢 2|🟢 deployed|⚪ 0| healthy | 2026-03-03 |2026-02-22|
| [knowledge-live](https://github.com/packetqc/knowledge-live) | v39 | 🔴 8 | 🟢 active | 🟢 7 | 🟢 deployed | ⚪ 0 | 1 | 🟢 healthy | 2026-02-24 |
|[STM32N6570-DK_SQLITE](https://github.com/packetqc/STM32N6570-DK_SQLITE)|v31|🔴 16|🟢 active|🟢 3|🟢 deployed|⚪ 0| healthy | 2026-03-03 |2026-02-22|
| [MPLIB_DEV_STAGING](https://github.com/packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE) | v31 | 🔴 16 | 🟢 active | 🟢 5 | 🟢 deployed | ⚪ 0 | 0 | 🔴 unreachable | 2026-02-22 |
|[PQC](https://github.com/packetqc/PQC)|v0|🔴 47|🔴 missing|⚪ 0|🔴 missing|⚪ 0| healthy | 2026-03-03 |2026-02-22|

</div>

> **Icons**: 🟢 current/healthy — 🟡 minor drift — 🟠 moderate drift — 🔴 critical/missing — ⚪ inactive

## Acquired Knowledge

> Click any command to copy it — paste into Claude Code to advance the insight.
>
> **Workflow**: `synced` → 🔍 review in `far_memory archives/` → 📦 assign type → ✅ promote to `conventions.json` or `work.json`

| # | Insight | Source | Status | Actions |
|---|---------|--------|--------|---------|
| 1 | Page cache sizing degradation (81%) | STM32N6570-DK_SQLITE | harvested | 🔍 `harvest --review 1` 📦 `harvest --stage 1 lesson` ✅ `harvest --promote 1` 🔄 `harvest --auto 1` |
| 2 | Printf latency in hot path (1-5 ms) | STM32N6570-DK_SQLITE | harvested | 🔍 `harvest --review 2` 📦 `harvest --stage 2 lesson` ✅ `harvest --promote 2` 🔄 `harvest --auto 2` |
| 3 | Slot vs page size mismatch (memsys5) | STM32N6570-DK_SQLITE | harvested | 🔍 `harvest --review 3` 📦 `harvest --stage 3 lesson` ✅ `harvest --promote 3` 🔄 `harvest --auto 3` |
| 4 | Multi-RTOS abstraction (FreeRTOS/ThreadX) | MPLIB | harvested | 🔍 `harvest --review 4` 📦 `harvest --stage 4 pattern` ✅ `harvest --promote 4` 🔄 `harvest --auto 4` |
| 5 | CubeMX N6570-DK limitation | MPLIB | harvested | 🔍 `harvest --review 5` 📦 `harvest --stage 5 lesson` ✅ `harvest --promote 5` 🔄 `harvest --auto 5` |
| 6 | TouchGFX MVP with backend services | MPLIB | harvested | 🔍 `harvest --review 6` 📦 `harvest --stage 6 pattern` ✅ `harvest --promote 6` 🔄 `harvest --auto 6` |
| 7 | ML-KEM/ML-DSA sizing for embedded | PQC | harvested | 🔍 `harvest --review 7` 📦 `harvest --stage 7 pattern` ✅ `harvest --promote 7` 🔄 `harvest --auto 7` |
| 8 | PQC library compliance (WolfSSL=prod) | PQC | harvested | 🔍 `harvest --review 8` 📦 `harvest --stage 8 pattern` ✅ `harvest --promote 8` 🔄 `harvest --auto 8` |
| 9 | Flash certificate storage pattern | PQC | harvested | 🔍 `harvest --review 9` 📦 `harvest --stage 9 pattern` ✅ `harvest --promote 9` 🔄 `harvest --auto 9` |
| 10 | AI-assisted module staging methodology | MPLIB_DEV_STAGING_WITH_CLAUDE | harvested | 🔍 `harvest --review 10` 📦 `harvest --stage 10 methodology` ✅ `harvest --promote 10` 🔄 `harvest --auto 10` |
| 11 | Parallel instance operations (core + satellite) | MPLIB_DEV_STAGING_WITH_CLAUDE | harvested | 🔍 `harvest --review 11` 📦 `harvest --stage 11 methodology` ✅ `harvest --promote 11` 🔄 `harvest --auto 11` |
| 12 | Two-merge bootstrap lifecycle (bootstrap → normalize → healthcheck) | MPLIB_DEV_STAGING_WITH_CLAUDE | harvested | 🔍 `harvest --review 12` 📦 `harvest --stage 12 methodology` ✅ `harvest --promote 12` 🔄 `harvest --auto 12` |
| 13 | Satellite thin-wrapper principle (~30 lines, not ~120) | MPLIB_DEV_STAGING_WITH_CLAUDE | harvested | 🔍 `harvest --review 13` 📦 `harvest --stage 13 methodology` ✅ `harvest --promote 13` 🔄 `harvest --auto 13` |
| 14 | Evolution relay methodology — new `evolution` stage type | knowledge-live | **promoted** | ✅ Promoted as v39 evolution entry |
| 15 | Managed projects — subfolder scaffold, harvest routing | knowledge-live | **promoted** | ✅ Promoted as P6 + methodology update |
| 16 | Autonomous convergence — elevated sessions converge | knowledge-live | harvested | 🔍 `harvest --review 16` 📦 `harvest --stage 16 pattern` ✅ `harvest --promote 16` 🔄 `harvest --auto 16` |
| 17 | Beacon PQC integration — protocol v0→v1, --secure flag | knowledge-live | harvested | 🔍 `harvest --review 17` 📦 `harvest --stage 17 docs` ✅ `harvest --promote 17` 🔄 `harvest --auto 17` |
| 18 | GitHub Project bidirectional integration | knowledge-live | **promoted** | ✅ Promoted to methodology/github-project-integration.md |
| 19 | TAG: convention — knowledge structure mirroring | knowledge-live | **promoted** | ✅ Promoted to methodology/github-project-integration.md |
| 20 | Entity convention — #N:story/#N:task/#N:bug | knowledge-live | **promoted** | ✅ Promoted to methodology/github-project-integration.md |
| 21 | Quality candidate "Intégré" — platform integration | knowledge-live | **promoted** | ✅ Promoted as core quality #13 in CLAUDE.md |
| 22 | gh_helper.py board reader + bidirectional reconciliation | knowledge-live | **promoted** | ✅ Promoted to core scripts/gh_helper.py (836→1494 lines) |
| 23 | Dynamic roadmap — board-driven web publication pipeline | knowledge-live | **promoted** | ✅ Promoted to core scripts/sync_roadmap.py + methodology |
| 24 | Autonomous proof — zero-manual GitHub UI cycle | knowledge-live | **promoted** | ✅ Promoted to methodology/github-project-integration.md |

## Discovered Publications

Publications detected in satellite repos:

| Title | Satellite | Status | Actions |
|-------|-----------|--------|---------|
| Architecture doc (SQLite pipeline) | STM32N6570-DK_SQLITE | **published** — core Publication #1 | 🔍 `harvest --review pub:stm32` |
| #1 GitHub Project Integration | knowledge-live | harvested — three-tier bilingual | 🔍 `harvest --review pub:kl1` |

## Master Mind Status

| Field | Value |
|-------|-------|
| Current version | **v47** |
| Evolution entries | 47 |
| Publications | 14 (#0–#12 + #4a dashboard + #9a compliance) |
| Patterns | 4 |
| Pitfalls | 17 |

## The Network

| Component | Role |
|-----------|------|
| **Master mind** (`packetqc/knowledge`) | Central repository: K_MIND module, domain JSONs, publications |
| **Satellites** (project repos) | Independent projects that inherit and evolve knowledge |
| **Push** (session start) | Satellites load K_MIND module on session start — "put on the sunglasses" |
| **Sync** (inbound) | K_GITHUB `sync_github.py` syncs satellite knowledge bidirectionally |
| **Versioning** (v1–v47) | Each evolution entry is a version. Drift = satellite behind core. |

## Knowledge Layers

| Layer | Stability | Content |
|-------|-----------|---------|
| **Core** (mind_memory.md) | Stable | 264-node directive grid — identity, methodology |
| **Proven** (conventions.json, work.json) | Validated | Battle-tested across projects, per module |
| **Harvested** (far_memory archives/) | Evolving | Fresh from satellite experiments |
| **Session** (sessions/) | Ephemeral | near_memory + far_memory per session |

## Lifecycle of an Insight

```
Session note → K_GITHUB sync → far_memory archives/ → validated across projects → conventions.json/work.json → mind_memory.md
```

Insights migrate upward through the layers as they prove their worth across multiple projects. The dashboard tracks this progression — updated on every K_GITHUB sync.

---

[**Read the full documentation →**]({{ '/publications/distributed-knowledge-dashboard/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
*This is a living document — updated on every K_GITHUB sync.*
