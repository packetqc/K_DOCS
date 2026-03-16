---
layout: publication
title: "Knowledge Architecture Analysis"
description: "Comprehensive architecture analysis of the Knowledge system (P0): knowledge layers, component architecture, 13 core qualities, session lifecycle, distributed topology, security model, web architecture, and deployment tiers."
pub_id: "Publication #14"
version: "v1"
date: "2026-02-26"
permalink: /publications/architecture-analysis/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "architecture, knowledge, distributed, security, quality, session, harvest"
---

# Knowledge Architecture Analysis
{: #pub-title}

> **Parent publication**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | **Closes**: [#316](https://github.com/packetqc/knowledge/issues/316)

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | System architecture overview |
| [System Overview](#system-overview) | Self-evolving AI engineering intelligence |
| [Knowledge Layers](#knowledge-layers) | Core, Proven, Harvested, Session |
| [Component Architecture](#component-architecture) | 13 major components |
| [Quality Architecture](#quality-architecture) | 13 core qualities and their interactions |
| [Session Lifecycle](#session-lifecycle-architecture) | Wakeup, work, save, checkpoint, resume |
| [Distributed Architecture](#distributed-architecture) | Master-satellite topology |
| [Security Architecture](#security-architecture) | Proxy model, ephemeral tokens, owner-scoped access |
| [Web Architecture](#web-architecture) | GitHub Pages, dual-theme, publication pipeline |
| [Deployment Model](#deployment-model) | Production/development tiers |

## Target Audience

| Audience | Focus |
|----------|-------|
| **Network Administrators** | Distributed architecture, security model, proxy boundaries |
| **System Administrators** | Deployment model, GitHub Pages, asset management |
| **Programmers** | Component architecture, session lifecycle, knowledge layers |
| **Managers** | System overview, core qualities, deployment tiers |

## Abstract

The Knowledge system (P0) is a self-evolving AI engineering intelligence that transforms stateless AI coding sessions into a persistent, distributed, self-healing network of awareness. Built entirely on plain Markdown files in Git repositories, it requires no external services, no databases, and no cloud infrastructure. One `git clone` bootstraps everything.

This publication provides a comprehensive architecture analysis: four knowledge layers, 13+ major components, 13 core qualities, session lifecycle, distributed master-satellite topology, security model, web publishing architecture, and production/development deployment tiers.

## System Overview

The system solves a fundamental problem: AI coding sessions are stateless. Without external structure, every new session starts blank — an NPC with no memory. The architecture addresses this through three mechanisms:

1. **Persistence**: CLAUDE.md + notes/ + wakeup/save lifecycle transform ephemeral sessions into continuous collaboration
2. **Distribution**: A master mind pushes methodology to satellites and harvests insights back — bidirectional intelligence flow
3. **Self-documentation**: The system records its own evolution, publishes its own docs, and grows by consuming its own output

## Knowledge Layers

Four layers, ordered by stability:

| Layer | Location | Stability | Content |
|-------|----------|-----------|---------|
| **Core** | `CLAUDE.md` | Highest | Identity, methodology, commands, evolution log |
| **Proven** | `patterns/`, `lessons/`, `methodology/` | High | Battle-tested patterns and pitfalls |
| **Harvested** | `minds/` | Medium | Fresh insights from satellite projects |
| **Session** | `notes/` | Lowest | Per-session working memory |

The layers form a lifecycle: sessions generate insights, harvest collects them, promotion validates them, and the core absorbs them. The next session inherits the enriched core.

## Component Architecture

13 major components with distinct roles:

| Component | Role |
|-----------|------|
| `CLAUDE.md` | System configuration + methodology documentation (3000+ lines in core) |
| `scripts/gh_helper.py` | GitHub API gateway — pure Python `urllib`, bypasses container proxy |
| `scripts/generate_og_gifs.py` | Visual identity — 40+ animated dual-theme webcards |
| `scripts/sync_roadmap.py` | Board synchronization — Project board items to static JSON |
| `publications/` | Source documents — canonical versioned content |
| `docs/` | Web publishing — GitHub Pages, bilingual EN/FR |
| `minds/` | Harvested intelligence — satellite insights incubator |
| `methodology/` | Process knowledge — detailed operational procedures |
| `patterns/` + `lessons/` | Validated knowledge — proven across 2+ projects |
| `notes/` | Session memory — ephemeral working data |
| `live/` | Real-time tooling — capture, beacon, scanner |
| `projects/` | Project registry — hierarchical P# indexing |

## Quality Architecture

13 core qualities form a dependency hierarchy:

| # | Quality | Essence | Enforcement |
|---|---------|---------|-------------|
| 1 | **Autosuffisant** | No external services | Pure Python, plain Markdown |
| 2 | **Autonome** | Self-propagating | Auto-wakeup, auto-bootstrap |
| 3 | **Concordant** | Structural integrity | `normalize`, `pub check` |
| 4 | **Concis** | Critical-subset, not copies | ~180-line satellite template |
| 5 | **Interactif** | Operable, not just readable | Click-to-copy dashboard |
| 6 | **Evolutif** | Grows as it works | 48 evolution entries |
| 7 | **Distribue** | Bidirectional flow | `harvest` + `wakeup` |
| 8 | **Persistant** | Knowledge survives sessions | `notes/` + `save` |
| 9 | **Recursif** | Self-documenting | Harvest feeds publications |
| 10 | **Securitaire** | Security by architecture | Owner-scoped, proxy-bounded |
| 11 | **Resilient** | Every failure has recovery | `resume`, `recall`, `refresh` |
| 12 | **Structure** | Organized around projects | P# indexing, project registry |
| 13 | **Integre** | Extends to platforms | GitHub Projects, Issues, PRs |

## Session Lifecycle Architecture

Every session follows: `wakeup → work → save`. Wakeup is the "sunglasses moment" — 12 steps from NPC to AWARE. Save delivers work via PR. Crash recovery uses checkpoints (`resume`), branch scanning (`recall`), and context restore (`refresh`).

## Distributed Architecture

Hub-and-spoke topology with bidirectional flow:

- **Push (wakeup)**: Satellites read core CLAUDE.md, inherit methodology and tooling
- **Pull (harvest)**: Core crawls satellites, extracts insights into `minds/`, promotes to core

Self-healing: bootstrap scaffold on fresh repos, automatic CLAUDE.md drift remediation, pull-based version synchronization.

## Security Architecture

- **Proxy model**: Git operations proxy-restricted per-repo/per-branch; Python `urllib` bypasses to API
- **Ephemeral tokens**: Classic PAT via `GH_TOKEN` env var — dies with session, zero stored at rest
- **Owner-scoped**: Only user-owned repos with Claude Code access. No third-party access ever
- **Fork-safe**: Public and safe to clone. Forkers get methodology, not credentials

## Web Architecture

GitHub Pages from `docs/`, Jekyll with custom layouts (no remote theme). Dual-theme (Cayman light / Midnight dark) via CSS media queries. Three-tier publications: source → summary → complete. Full bilingual EN/FR mirror system enforced by `normalize`.

## Deployment Model

Multi-tier: core = system-production, satellites = dev relative to core AND production at their own repo level. A constellation of independent web presences, not a single central site. Each node publishes independently via its own GitHub Pages.

## Structural Analysis — Core Nucleus

The entire system fits in < 1 MB. CLAUDE.md alone (293 KB, 31%) is the brain. The authority gap insight: CLAUDE.md has **system authority** (survives compaction), while everything else (~640 KB) has **conversation authority** (lost on first compaction). This drives the critical-subset architecture (v31).

## Publication Structure Analysis

Every publication follows a 9-branch anatomy: Source, Web EN, Web FR, Front matter, Webcards OG, Layout, System integration, Identifiers, and Validation. Five quality commands (`pub check`, `pub sync`, `doc review`, `docs check`, `normalize`) form a complete quality loop.

**Source**: [Issue #317](https://github.com/packetqc/knowledge/issues/317), [Issue #318](https://github.com/packetqc/knowledge/issues/318) — Architecture exploration sessions.

---

[**Read the full documentation →**]({{ '/publications/architecture-analysis/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
