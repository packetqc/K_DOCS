---
layout: publication
title: "Harvest Protocol — Practical Guide to Distributed Knowledge Collection"
description: "Practical how-to guide for the harvest commands: pulling knowledge from satellite projects, the promotion pipeline (review → stage → promote), network healthcheck, satellite remediation, and common daily workflows."
pub_id: "Publication #7"
version: "v2"
date: "2026-03-16"
permalink: /publications/harvest-protocol/
og_image: /assets/og/harvest-protocol-en-cayman.gif
keywords: "harvest, promotion, healthcheck, satellites, insights, version drift"
---

# Harvest Protocol — Practical Guide
{: #pub-title}

> **Parent publication**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | **Core reference**: [#14 — Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/publications/knowledge-2.0/' | relative_url }}) | **Architecture**: [#4 — Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Practical guide overview |
| [Quick Reference](#quick-reference) | All harvest commands at a glance |
| [Core Concept](#core-concept) | Bidirectional knowledge flow and access scope |
| [The Promotion Pipeline](#the-promotion-pipeline) | Review, stage, promote workflow |
| [Network Healthcheck](#network-healthcheck) | Full network sweep with severity icons |
| [Satellite Remediation](#satellite-remediation) | Pull-based version drift fix |
| [Common Workflows](#common-workflows) | Daily check, new insight, guided procedures |

## Abstract

Publication #4 (Distributed Minds) documents the **architecture** of bidirectional knowledge flow. This publication is the **practical guide** — how K_GITHUB `sync_github.py` replaces K1.0's `harvest` commands: syncing knowledge from satellites, managing the promotion pipeline, and tracking version drift.

## Quick Reference

| Command | Action |
|---------|--------|
| K_GITHUB `sync_github.py <project>` | Sync knowledge from satellite |
| K_GITHUB project inventory | List satellites with version + drift |
| K_GITHUB + K_VALIDATION `/integrity-check` | Full network sweep |
| Manual: update `conventions.json` or `work.json` | Promote to domain files |
| K_GITHUB sync to satellite | Push updates to satellite |

## Core Concept

**Push** (outbound): On session start, satellites load the K_MIND module (`mind_memory.md` + domain JSONs). **Sync** (inbound): K_GITHUB `sync_github.py` syncs bidirectionally — extracting evolved knowledge and staging it in `far_memory archives/` for review.

**Access scope**: Harvest only operates on repositories that the user owns and that Claude Code has been granted access to via its GitHub application configuration. No external or third-party repos are ever crawled.

All satellite access uses public HTTPS: `https://github.com/packetqc/<project>`, targeting the default branch (`main` or `master`).

## The Promotion Pipeline

```
harvested → 🔍 review → 📦 stage → ✅ promote (or 🔄 auto)
```

| Stage | Action |
|-------|--------|
| **Sync** | K_GITHUB `sync_github.py` pulls insights from satellite |
| **Review** | Human review of staged content in `far_memory archives/` (quality gate) |
| **Stage** | Assign target type (lesson, pattern, methodology, evolution, docs) |
| **Promote** | Manual: update `conventions.json` or `work.json` with promoted knowledge |

## Network Healthcheck

K_GITHUB + K_VALIDATION `/integrity-check` sweeps all known satellites, updates severity icons (🟢🟡🟠🔴⚪), and regenerates dashboard webcards.

## Satellite Remediation

K_GITHUB `sync_github.py` prepares a version update locally. The satellite self-heals on next session start by loading the updated K_MIND module — pull-based, not push-based (Claude Code cannot push cross-repo).

## Common Workflows

**Daily check**: K_GITHUB project inventory → K_GITHUB + K_VALIDATION `/integrity-check`

**New insight**: K_GITHUB `sync_github.py <project>` → human review of `far_memory archives/` → assign type → promote to `conventions.json` or `work.json`

**Guided**: K_VALIDATION `/work-cycle` for step-by-step walkthrough with current state.

---

[**Read the full documentation →**]({{ '/publications/harvest-protocol/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
