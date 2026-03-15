---
layout: publication
title: "Knowledge Architecture Diagrams — Complete Documentation"
description: "Complete visual architecture: 14 Mermaid diagrams covering system overview, knowledge layers, components, session lifecycle, distributed flow, publication pipeline, security boundaries, deployment tiers, quality dependencies, recovery ladder, and GitHub integration."
pub_id: "Publication #15 — Full"
version: "v1"
date: "2026-02-26"
permalink: /publications/architecture-diagrams/full/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "architecture, diagrams, mermaid, knowledge, distributed, security"
---

# Knowledge Architecture Diagrams — Complete Documentation
{: #pub-title}

**Contents**

| | |
|---|---|
| [Authors](#authors) | Publication authors |
| [Abstract](#abstract) | Visual companion to the architecture analysis |
| [Diagram Conventions](#diagram-conventions) | Color coding, notation, Mermaid syntax |
| [1. System Overview](#1-system-overview--c4-context) | C4 context — Knowledge at center |
| [2. Knowledge Layers](#2-knowledge-layers) | 4-layer stack: Core → Proven → Harvested → Session |
| [3. Component Architecture](#3-component-architecture) | All folders, scripts, and relationships |
| [4. Session Lifecycle](#4-session-lifecycle) | Wakeup → work → checkpoint → save → PR → merge |
| [5. Distributed Flow](#5-distributed-flow--push-and-pull) | Push (wakeup) and pull (harvest) with promotion |
| [6. Publication Pipeline](#6-publication-pipeline) | Source → EN/FR summary/complete with sync flows |
| [7. Security Boundaries](#7-security-boundaries) | Proxy model — allowed vs blocked operations |
| [8. Deployment Tiers](#8-deployment-tiers) | Production/development dual-role of satellites |
| [9. Quality Dependencies](#9-quality-dependency-graph) | 13 qualities dependency graph |
| [10. Recovery Ladder](#10-recovery-ladder) | 5 recovery paths by failure mode |
| [11. GitHub Integration](#11-github-integration) | Issues, PRs, Project boards lifecycle |
| [Related Publications](#related-publications) | Sibling and parent publications |

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Architect of the Knowledge system — a self-evolving AI engineering intelligence built on 30 years of embedded systems, network security, and software development experience. Designed the visual architecture documented in these diagrams.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Co-created the architectural diagrams, rendering system structure into Mermaid notation for interactive web visualization. Operates within the system these diagrams describe.

---

## Abstract

Publication #14 (Architecture Analysis) examines the system's architecture through analytical narrative. This publication is the **visual companion** — 14 Mermaid diagrams that render the Knowledge system's structure, flows, boundaries, and dependencies into interactive, browsable visualizations.

These diagrams cover the full architectural surface: from the high-level C4 context (Knowledge at center, surrounded by satellites, GitHub, and users) down to the granular security boundaries (proxy layers, API channels, branch scoping). Each diagram is self-contained but cross-referenced — together they form a complete visual map of the system.

All diagrams use [Mermaid](https://mermaid.js.org/) syntax, rendered natively by GitHub Pages via CDN.

Closes #317

---

## Target Audience

This publication is intended for work teams involved in the Knowledge system's ecosystem:

| Audience | What to focus on |
|----------|-----------------|
| **Network Administrators** | Distributed flow (#5), security boundaries (#7), deployment tiers (#8) |
| **System Administrators** | Deployment tiers (#8), GitHub integration (#11), publication pipeline (#6) |
| **Programmers** | Component architecture (#3), session lifecycle (#4), recovery ladder (#10) |
| **Managers** | System overview (#1), knowledge layers (#2), quality dependencies (#9) |

Each diagram is self-contained with annotations. Start with the System Overview (#1) for high-level context, then navigate to domain-specific diagrams. The companion publication #14 (Architecture Analysis) provides the written analysis for each diagram's domain.

## Diagram Conventions

All diagrams use **Mermaid** notation — a markdown-based diagramming language rendered client-side by the GitHub Pages layout.

**Color coding**:

| Color | Meaning | Used for |
|-------|---------|----------|
| Teal / Green | Core / Stable / Healthy | Core knowledge, proven patterns, healthy status |
| Blue | Active / In-progress | Sessions, active flows, current operations |
| Orange / Amber | Warning / Drift | Version drift, stale content, minor issues |
| Red | Critical / Blocked | Security boundaries, proxy blocks, critical drift |
| Purple | External / Platform | GitHub, GitHub Pages, external services |
| Gray | Inactive / Pending | Unused paths, pending items |

**Notation**:

| Symbol | Meaning |
|--------|---------|
| Solid arrow (`-->`) | Direct data flow or dependency |
| Dashed arrow (`-.->`) | Indirect or periodic flow |
| Thick arrow (`-->`) | Primary / critical path |
| Subgraph | Logical grouping or boundary |

---

## 1. System Overview — C4 Context

The Knowledge system (P0) sits at the center of a constellation of actors: satellite projects, GitHub platform services, GitHub Pages for publishing, Claude Code for AI sessions, and the human developer.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-01-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-01-en-cayman.png' | relative_url }}" alt="Diagram 1" style="max-width:100%;height:auto;">
</picture>


**Legend**: The core knowledge repo contains all methodology, publications, and tooling. Satellites inherit methodology on `wakeup` (push) and contribute insights back via `harvest` (pull). GitHub acts as the persistence and collaboration layer. GitHub Pages publishes the web presence. Claude Code is the execution environment — ephemeral containers that become aware via the `wakeup` protocol.

---

## 2. Knowledge Layers

The system organizes knowledge into 4 layers of decreasing stability and increasing currency. Core is the DNA — rarely changing, maximum authority. Session is the heartbeat — ephemeral, maximum currency.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-02-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-02-en-cayman.png' | relative_url }}" alt="Diagram 2" style="max-width:100%;height:auto;">
</picture>


**Legend**: Knowledge flows upward (session → harvested → proven → core) through the promotion pipeline. It flows downward (core → session) through the wakeup protocol. The reading order for new Claude instances follows the stability gradient: most stable first, most current last.

---

## 3. Component Architecture

The major folders, scripts, and their relationships within the knowledge repository.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-03-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-03-en-cayman.png' | relative_url }}" alt="Diagram 3" style="max-width:100%;height:auto;">
</picture>


**Legend**: The repository is organized into five major groups: root files (entry points), knowledge folders (the intelligence layers), content folders (publications and web pages), scripts (automation tooling), and live infrastructure (inter-instance communication). Arrows show data flow between components.

---

## 4. Session Lifecycle

Every Claude Code session follows a deterministic lifecycle. This flowchart shows the complete path from session start to session end, including crash recovery and context loss paths.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-04-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-04-en-cayman.png' | relative_url }}" alt="Diagram 4" style="max-width:100%;height:auto;">
</picture>


**Legend**: The session lifecycle has three phases: boot (wakeup), work, and delivery (save). Crash recovery uses checkpoints. Context loss recovery uses `refresh`. The elevated path (with token) is fully autonomous; the semi-automatic path requires one user click to merge the PR.

---

## 5. Distributed Flow — Push and Pull

The bidirectional knowledge flow between the master mind (P0) and satellite projects. Push delivers methodology outward; harvest pulls insights inward. The promotion pipeline advances insights from raw to core.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-05-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-05-en-cayman.png' | relative_url }}" alt="Diagram 5" style="max-width:100%;height:auto;">
</picture>


**Legend**: Thick solid arrows represent the push flow (wakeup). Dashed arrows represent the pull flow (harvest). The promotion pipeline advances insights through four stages: review (human validated), stage (typed and targeted), promote (written to core), auto (queued for next healthcheck). The dashboard is updated on every harvest.

---

## 6. Publication Pipeline

Each publication exists at three tiers: source (canonical), summary (web), and complete (web). Each tier is bilingual (EN + FR). This diagram shows the sync and review flows.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-06-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-06-en-cayman.png' | relative_url }}" alt="Diagram 6" style="max-width:100%;height:auto;">
</picture>


**Legend**: The source README.md is the single source of truth. `pub sync` propagates changes from source to EN web pages. Translation produces FR mirrors. Each web page links to its language mirror (EN ↔ FR) and to its depth variant (summary ↔ complete). Four validation commands ensure structural integrity, source-docs concordance, content freshness, and page-level correctness.

---

## 7. Security Boundaries

The proxy model governing what Claude Code sessions can and cannot do. The container proxy mediates all git operations while Python urllib bypasses it for API access.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-07-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-07-en-cayman.png' | relative_url }}" alt="Diagram 7" style="max-width:100%;height:auto;">
</picture>


**Legend**: The container proxy is the primary security boundary. Git operations are restricted to the assigned task branch of the current repo. Python `urllib` (used by `gh_helper.py`) bypasses the proxy entirely, enabling full GitHub API access with a valid token. `curl` is intercepted by the proxy and auth headers are stripped. The two-channel model: git proxy (restricted) + urllib (unrestricted with token).

---

## 8. Deployment Tiers

The multi-tier deployment model where each satellite is simultaneously development (relative to core) and production (at its own level). Every node publishes independently via GitHub Pages.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-08-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-08-en-cayman.png' | relative_url }}" alt="Diagram 8" style="max-width:100%;height:auto;">
</picture>


**Legend**: The deployment model is multi-tier. Core is system-production — the canonical brain. Each satellite is simultaneously development relative to core (testing ground for new capabilities) and production at its own level (independent GitHub Pages, project boards, publications). Ideas flow: satellite testing → satellite pages → harvest → core promotion → all satellites inherit.

---

## 9. Quality Dependency Graph

The 13 core qualities and how they depend on each other. Autosuffisant is the foundation — if the system depends on external services, nothing else works.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-09-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-09-en-cayman.png' | relative_url }}" alt="Diagram 9" style="max-width:100%;height:auto;">
</picture>


**Legend**: The dependency graph flows from foundation (autosuffisant — plain text in Git) through enabling qualities (autonome, concordant, concis) to operational qualities (interactif, evolutif) to network qualities (distribue, persistant) to meta-qualities (recursif, securitaire, resilient) to organizational qualities (structure, integre). Each quality reinforces the ones that depend on it.

---

## 10. Recovery Ladder

The five recovery paths, ordered from lightest to heaviest. Each path addresses a different failure mode.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-10-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-10-en-cayman.png' | relative_url }}" alt="Diagram 10" style="max-width:100%;height:auto;">
</picture>


**Legend**: The recovery ladder matches failure modes to recovery paths. Client disconnect: browser refresh (instant) or manual PR (minutes). Crash with checkpoint: `resume` (~10s). Crash without checkpoint: `recover` (~15s). Context compaction: `refresh` (~5s). Stale upstream: `wakeup` (~30-60s). Each path is the lightest possible response to its failure mode.

**Recovery summary**:

| Recovery | Trigger | Speed | What it restores |
|----------|---------|-------|------------------|
| Browser refresh | Client disconnect | Instant | Session may still be alive server-side |
| Manual PR | Push succeeded, PR interrupted | Minutes | Work on remote branch gets a PR |
| `resume` | Crash with checkpoint | ~10s | Protocol progress + todo state |
| `recover` | Crash, no checkpoint | ~15s | Committed code from dead branch |
| `recall` | Deep memory search | ~10s | Session history and past decisions |
| `refresh` | Context compaction | ~5s | CLAUDE.md formatting + rules |
| `wakeup` | Stale upstream | ~30-60s | Full deep re-sync |
| New session | Severe compaction | ~60s | Complete fresh start |

---

## 11. GitHub Integration

The lifecycle of GitHub entities (Issues, PRs, Project board items) within the Knowledge system. Each entity type has a well-defined lifecycle managed by `gh_helper.py`.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-11-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-11-en-cayman.png' | relative_url }}" alt="Diagram 11" style="max-width:100%;height:auto;">
</picture>


**Legend**: Three key workflows. **Issue lifecycle**: issue created → linked to board → work (In Progress) → PR with "Closes #N" → merge → auto-close → auto-Done. **Harvest cycle**: clone satellite → extract → update dashboard → push → deploy. **Project creation**: create board → link to repo → scaffold web presence → deploy. All API calls go through `gh_helper.py` (Python urllib).

**GitHub entity lifecycle summary**:

| Entity | Created by | Managed by | Closed by |
|--------|-----------|------------|-----------|
| Issue | User (GitHub UI) | Claude (comments, labels) | Auto-close on PR merge (`Closes #N`) |
| PR | Claude (`gh_helper.py`) | Claude (push, create) | Claude merge (elevated) or user (semi-auto) |
| Board item | User or Claude (draft/linked) | Claude (`project_item_update`) | Auto-Done on issue close |
| Project board | Claude (`createProjectV2`) | Claude (fields, items) | Never (persistent) |

---

## 12. System Architecture Mindmap

High-level navigation map of the Knowledge system with its 9 architectural pillars. This mindmap provides a bird's-eye view complementing the detailed flowcharts above.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-12-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-12-en-cayman.png' | relative_url }}" alt="Diagram 12" style="max-width:100%;height:auto;">
</picture>


**The 9 architectural pillars**:

| # | Pillar | Essence | Key elements |
|---|--------|---------|--------------|
| 1 | **Identity** | The system's DNA | 13 qualities, Free Guy analogy, 48 evolutions, Martin 30 years XP |
| 2 | **Distributed architecture** | The living network | Bidirectional flow, 4 layers, satellites, proxy protocol |
| 3 | **Session lifecycle** | The work rhythm | wakeup → work → save → recovery |
| 4 | **Projects** | The P0-P9 entities | 3 core/child, 3 managed, 1 pre-bootstrap |
| 5 | **Publications** | The public face | 15 pubs × 3 tiers × 2 languages |
| 6 | **Security** | Trust by design | Ephemeral tokens, proxy-aware, fork-safe |
| 7 | **Web presence** | The constellation of sites | GitHub Pages, dual-theme, 40 webcards |
| 8 | **Tools** | The toolbox | 7 Python scripts deployed everywhere |
| 9 | **Proven knowledge** | The long memory | 4 patterns + 20 pitfalls = 30 years distilled |

**Source**: [Issue #317](https://github.com/packetqc/knowledge/issues/317) — Interactive voice-to-text architecture exploration session.

---

## 13. Core Nucleus Mindmap

The Knowledge system's file-level structure — every folder and its weight, role, and contents. The entire system fits in < 1 MB of Markdown + Python.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-13-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-13-en-cayman.png' | relative_url }}" alt="Diagram 13" style="max-width:100%;height:auto;">
</picture>


**Nucleus weight by role**:

| Role | Components | Weight | Proportion |
|------|-----------|--------|------------|
| **Brain** | CLAUDE.md | 293 KB | 31% |
| **Knowledge** | methodology + patterns + lessons | 218 KB | 23% |
| **Intelligence** | minds + projects | 121 KB | 13% |
| **Tools** | scripts | 242 KB | 26% |
| **Infrastructure** | live | 53 KB | 6% |
| **Ephemeral** | docs + notes + publications | Variable | — |
| **Total nucleus** | **~930 KB** | **100%** | |

**Reading priority for Claude instances**:

| Priority | Folder / File | Size | Authority | Survives compaction? | Role |
|----------|---------------|------|----------|---------------------|------|
| **P0** | `CLAUDE.md` | 293 KB | System (project instructions) | Yes | **The nucleus** — identity, methodology, commands, evolution, pitfalls |
| **P1** | `methodology/` | 194 KB | Conversation (read at wakeup) | No | Implementation blueprints — bootstrap, checkpoint, projects, export |
| **P2** | `patterns/` | 14 KB | Conversation | No | Proven knowledge — embedded debugging, RTOS, SQLite, UI/backend |
| **P3** | `lessons/` | 10 KB | Conversation | No | Mistakes to avoid — 20 documented pitfalls |
| **P4** | `minds/` | 71 KB | Conversation | No | Harvested intelligence from satellites — newest, least validated |
| **P5** | `notes/` | 80 KB (latest 3) | Conversation | No | Ephemeral memory — previous session context |
| **P6** | `projects/` | 50 KB | Conversation | No | Entity registry P0-P9 with metadata |
| **P7** | `scripts/` | 242 KB | Executable | N/A | Deployed tools — not read, executed (gh_helper, webcards, beacon) |
| **P8** | `publications/` | Variable | Conversation | No | Source for 15 publications — read on demand, not at wakeup |
| **P9** | `docs/` | 100+ pages | Web | N/A | Web presence — GitHub Pages, not read by Claude |
| **P10** | `live/` | 53 KB | Executable | N/A | Live infrastructure — beacon, scanner, capture |

**Key insight — The authority gap**: CLAUDE.md (293 KB) has **system authority** — survives compaction, loaded as "project instructions". Everything else (~640 KB) has **conversation authority** — read at wakeup step 0, lost on first compaction. This is why the **critical-subset** (v31) is vital: the satellite CLAUDE.md (~180 lines) carries enough behavioral DNA to survive post-compaction.

**Source**: [Issue #317](https://github.com/packetqc/knowledge/issues/317) — Detailed architecture exploration.

---

## 14. Publication Structure Mindmap

The anatomy of a single Publication — all its components, tiers, assets, metadata, and integration points.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{{ '/assets/diagrams/architecture-diagrams/diagram-14-en-midnight.png' | relative_url }}">
  <img src="{{ '/assets/diagrams/architecture-diagrams/diagram-14-en-cayman.png' | relative_url }}" alt="Diagram 14" style="max-width:100%;height:auto;">
</picture>


**Publication lifecycle**:

```
pub new → Source created → EN/FR pages scaffolded → Webcards generated
    → Content written in Source
    → pub sync → Web pages updated
    → doc review → Freshness verified
    → pub check → Structure validated
    → normalize → Global concordance
```

**Publication branches**:

| Branch | Role | Files |
|--------|------|-------|
| **Source** | Canonical truth, versioned | `publications/<slug>/v1/README.md` + `assets/` + `media/` |
| **Web pages EN** | English web presence, 2 tiers | Summary (`index.md`) + Complete (`full/index.md`) |
| **Web pages FR** | French mirror | Same structure under `docs/fr/` |
| **Front matter** | Jekyll metadata | 8 required fields per page |
| **Webcards OG** | Animated social preview | 4 GIFs per publication (2 languages × 2 themes) |
| **Layout** | Rendering engine | Version banner, language bar, export, printing, cross-refs |
| **System integration** | Connection points | Indexes, profiles, CLAUDE.md, dashboard |
| **Identifiers** | Naming system | #N, slug, tiers, origin, cross-project |
| **Validation** | Quality control | 5 verification commands |

**Source**: [Issue #318](https://github.com/packetqc/knowledge/issues/318) — Publication structure exploration.

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — the system these diagrams visualize |
| 4 | [Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }}) | Architecture — push/pull flow (Diagram 5) |
| 7 | [Harvest Protocol]({{ '/publications/harvest-protocol/' | relative_url }}) | Protocol — harvest flow (Diagrams 5, 11) |
| 8 | [Session Management]({{ '/publications/session-management/' | relative_url }}) | Lifecycle — session flow (Diagram 4) |
| 9 | [Security by Design]({{ '/publications/security-by-design/' | relative_url }}) | Security — proxy boundaries (Diagram 7) |
| 12 | [Project Management]({{ '/publications/project-management/' | relative_url }}) | Projects — P# hierarchy (Diagrams 1, 8) |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
