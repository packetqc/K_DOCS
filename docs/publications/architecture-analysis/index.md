---
layout: publication
title: "Knowledge Architecture Analysis"
description: "Comprehensive architecture analysis of the Knowledge 2.0 system: five-module design (K_MIND, K_DOCS, K_GITHUB, K_PROJECTS, K_VALIDATION), mind-first memory, skill-based routing, static JS web viewer, security model, and deployment architecture."
pub_id: "Publication #14"
version: "v2"
date: "2026-03-16"
permalink: /publications/architecture-analysis/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "architecture, knowledge, K_MIND, modules, memory, skills, security"
---

# Knowledge Architecture Analysis
{: #pub-title}

> **Parent publication**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | **Core reference**: [#15 — Architecture Diagrams]({{ '/publications/architecture-diagrams/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/publications/knowledge-2.0/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | System architecture overview |
| [System Overview](#system-overview) | Multi-module AI engineering intelligence |
| [Module Architecture](#module-architecture) | Five specialized modules |
| [Memory Architecture](#memory-architecture) | Mind-first tiered memory |
| [Skill Architecture](#skill-architecture) | Claude Code native skill routing |
| [Quality Architecture](#quality-architecture) | 13 core qualities and K2.0 enforcement |
| [Session Lifecycle](#session-lifecycle) | K_MIND scripts persistence mechanism |
| [Distributed Architecture](#distributed-architecture) | Multi-repo knowledge network |
| [Security Architecture](#security-architecture) | Proxy model, ephemeral tokens, owner-scoped access |
| [Web Architecture](#web-architecture) | Static JS viewer, 5 interfaces + live mindmap |
| [Deployment Model](#deployment-model) | Dual remote strategy, network topology |

## Target Audience

| Audience | Focus |
|----------|-------|
| **Network Administrators** | Distributed architecture, security model, proxy boundaries |
| **System Administrators** | Deployment model, GitHub Pages, module structure |
| **Programmers** | Module architecture, memory system, session lifecycle, skill routing |
| **Managers** | System overview, core qualities, deployment model |

## Abstract

The Knowledge system is a self-evolving AI engineering intelligence that transforms stateless AI coding sessions into a persistent, distributed, self-healing network of awareness. Built on Markdown files, JSON domain files, and Python scripts in Git repositories — no external services, no databases, no cloud infrastructure.

This publication provides a comprehensive architecture analysis of the **Knowledge 2.0 multi-module design**: five specialized modules, mind-first memory with a 264-node directive grid, tiered session memory, Claude Code native skill routing, a static JavaScript web viewer, and the security and deployment architecture.

## System Overview

The system solves a fundamental problem: AI coding sessions are stateless. The K2.0 architecture addresses this through three mechanisms:

1. **Persistence**: A 264-node mindmap directive grid (`mind_memory.md`) + tiered session memory (`near_memory.json` / `far_memory.json` / `archives/`) + K_MIND scripts transform ephemeral sessions into continuous collaboration
2. **Modularity**: Five specialized modules (K_MIND, K_DOCS, K_GITHUB, K_PROJECTS, K_VALIDATION) each own their domain with own scripts, skills, conventions, and work tracking
3. **Self-documentation**: The system records its evolution in domain JSONs, publishes documentation via K_DOCS, and grows by consuming its own output

### K1.0 → K2.0 Evolution

| Aspect | K1.0 (Monolithic) | K2.0 (Multi-Module) |
|--------|-------------------|---------------------|
| **Brain** | `CLAUDE.md` (3000+ lines) | `mind_memory.md` (264-node grid) + domain JSONs |
| **Knowledge** | `patterns/`, `lessons/` | `conventions.json`, `work.json` per module |
| **Session memory** | `notes/` (flat files) | `sessions/` — near + far + archives |
| **Command routing** | `routes.json` + `SkillRegistry` | `.claude/skills/` SKILL.md (Claude Code native) |
| **Web** | Jekyll with `_config.yml` | `.nojekyll` static JS viewer |

## Module Architecture

Five specialized modules under `Knowledge/`:

| Module | Role | Key Components |
|--------|------|----------------|
| **K_MIND** | Core memory — mindmap, sessions, scripts | `mind_memory.md`, `session_init.py`, `memory_append.py`, `far_memory_split.py`, `memory_recall.py` |
| **K_DOCS** | Documentation — publications, webcards, web viewer | `capture_mindmap.js`, `generate_mindmap_webcard.py`, conventions, methodology |
| **K_GITHUB** | GitHub integration — sync, boards, tagged input | `sync_github.py`, board aliases, tagged-input skill |
| **K_PROJECTS** | Project management — registry, compilation | `compile_projects.py`, project data, create/manage skills |
| **K_VALIDATION** | Quality assurance — integrity, normalize, workflow | `documentation_validation.py`, 29 checkpoints, task workflow |

Each module owns its own `conventions.json`, `work.json`, and `documentation.json` — no single file is a bottleneck.

## Memory Architecture

Mind-first: always read `mind_memory.md` first (hive view), then domain JSONs (structured detail), then session files (history).

| Tier | Storage | Content | Loaded at start? |
|------|---------|---------|-------------------|
| **Mindmap** | `mind_memory.md` | 264-node directive grid | Yes (~2.8K tokens) |
| **Domain JSONs** | Per-module `.json` | 163 references, ~1.8 MB | Subset (~4.5K tokens) |
| **Near memory** | `near_memory.json` | Real-time summaries with pointers | Yes (~8.5K tokens) |
| **Far memory** | `far_memory.json` | Full verbatim history | Minimal |
| **Archives** | `archives/` | Topic-split far_memory | On demand |

## Skill Architecture

K2.0 replaces `routes.json` / `SkillRegistry` with Claude Code native `.claude/skills/` SKILL.md files. 20+ skills across 5 modules — each self-contained with its own methodology chain.

## Quality Architecture

13 core qualities with K2.0 enforcement:

| # | Quality | K2.0 Enforcement |
|---|---------|-------------------|
| 1 | **Autosuffisant** | Plain Markdown + JSON in Git, pure Python scripts |
| 2 | **Autonome** | `session_init.py` auto-runs, `/normalize` self-heals |
| 3 | **Concordant** | `/normalize`, `/integrity-check` (29 checkpoints) |
| 4 | **Concis** | 264-node mindmap as hive view, depth filtering |
| 5 | **Interactif** | 5 interfaces + live MindElixir mindmap |
| 6 | **Evolutif** | near_memory grows every turn, work.json accumulates |
| 7 | **Distribue** | K_MIND pushed via git, K_GITHUB sync |
| 8 | **Persistant** | Tiered memory (near/far/archives) |
| 9 | **Recursif** | K_DOCS publications describe K_MIND architecture |
| 10 | **Securitaire** | Proxy scoping, ephemeral tokens, gh_helper.py |
| 11 | **Resilient** | `/mind-context` reload, `memory_recall.py`, archives |
| 12 | **Structure** | 5 modules with own domain files, K_PROJECTS registry |
| 13 | **Integre** | K_GITHUB gh_helper.py, Projects v2, board aliases |

## Session Lifecycle

Every session: `session_init.py → /mind-context → [work] → memory_append.py (every turn) → far_memory_split.py → git commit & push`. Programs over improvisation — Claude provides intelligence as arguments to deterministic scripts.

## Distributed Architecture

Hub-and-spoke with bidirectional flow. K_MIND is pushed to satellites via git. K_GITHUB `sync_github.py` handles bidirectional sync (replaces K1.0 `harvest`).

## Security Architecture

- **Proxy model**: Git operations proxy-restricted per-repo/per-branch; Python `urllib` bypasses to API
- **Ephemeral tokens**: Classic PAT via `GH_TOKEN` env var — dies with session, zero stored at rest
- **Owner-scoped**: Only user-owned repos with Claude Code access
- **Fork-safe**: Public and safe to clone — forkers get methodology, not credentials

## Web Architecture

Static JS viewer (`.nojekyll`) with client-side Markdown + mermaid rendering. 4 themes via CSS media queries. 5 interfaces (navigator, project viewer, session review, task workflow, publication index) + live MindElixir mindmap. Unified EN/FR templates with `translateStatic()` for i18n (conv-020).

## Deployment Model

Dual remote strategy: `knowledge` (packetqc/knowledge) + `origin` (packetqc/K_DOCS). Both receive pushes on every completed unit of work.

---

[**Read the full documentation →**]({{ '/publications/architecture-analysis/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
