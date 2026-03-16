---
layout: publication
title: "Harvest Protocol — Practical Guide to Distributed Knowledge Collection"
description: "Practical how-to guide for the harvest commands: pulling knowledge from satellite projects, the promotion pipeline (review → stage → promote), network healthcheck, satellite remediation, and common daily workflows."
pub_id: "Publication #7"
version: "v1"
date: "2026-02-19"
permalink: /publications/harvest-protocol/
og_image: /assets/og/harvest-protocol-en-cayman.gif
keywords: "harvest, promotion, healthcheck, satellites, insights, version drift"
---

# Harvest Protocol — Practical Guide
{: #pub-title}

> **Parent publication**: [#0 — Knowledge]({{ '/publications/knowledge-system/' | relative_url }}) | **Architecture**: [#4 — Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }})

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

Publication #4 (Distributed Minds) documents the **architecture** of bidirectional knowledge flow. This publication is the **practical guide** — how to actually use `harvest` day-to-day: pulling knowledge from satellites, reviewing insights, promoting to core, running network sweeps, and fixing version drift.

## Quick Reference

| Command | Action |
|---------|--------|
| `harvest <project>` | Pull knowledge from a satellite into `minds/` |
| `harvest --list` | List all projects with version + drift status |
| `harvest --procedure` | Guided promotion walkthrough |
| `harvest --healthcheck` | Full network sweep + auto-promote |
| `harvest --review <N>` | Mark insight as human-reviewed |
| `harvest --stage <N> <type>` | Stage for integration (lesson, pattern, methodology, evolution, docs) |
| `harvest --promote <N>` | Promote to core knowledge now |
| `harvest --auto <N>` | Queue for auto-promote on next healthcheck |
| `harvest --fix <project>` | Update satellite CLAUDE.md to latest version |

## Core Concept

**Push** (outbound): On `wakeup`, satellites read the master mind. **Harvest** (inbound): The master crawls satellites, extracts evolved knowledge, stages it in `minds/` for review.

**Access scope**: Harvest only operates on repositories that the user owns and that Claude Code has been granted access to via its GitHub application configuration. No external or third-party repos are ever crawled.

All satellite access uses public HTTPS: `https://github.com/packetqc/<project>`, targeting the default branch (`main` or `master`).

## The Promotion Pipeline

```
harvested → 🔍 review → 📦 stage → ✅ promote (or 🔄 auto)
```

| Stage | Action |
|-------|--------|
| **Harvest** | `harvest <project>` pulls insights into `minds/` |
| **Review** | `harvest --review N` marks as human-validated (quality gate) |
| **Stage** | `harvest --stage N lesson` assigns target type (lesson, pattern, methodology, evolution, docs) |
| **Promote** | `harvest --promote N` writes to core now, or `harvest --auto N` queues for next healthcheck |

## Network Healthcheck

`harvest --healthcheck` sweeps all known satellites, updates severity icons (🟢🟡🟠🔴⚪), processes auto-promote queue, and regenerates dashboard webcards.

## Satellite Remediation

`harvest --fix <project>` prepares a version update locally. The satellite self-heals on next `wakeup` by reading the updated core — pull-based, not push-based (Claude Code cannot push cross-repo).

## Common Workflows

**Daily check**: `harvest --list` → `harvest --healthcheck`

**New insight**: `harvest <project>` → `harvest --review N` → `harvest --stage N lesson` → `harvest --promote N`

**Guided**: `harvest --procedure` for step-by-step walkthrough with current state.

---

[**Read the full documentation →**]({{ '/publications/harvest-protocol/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
