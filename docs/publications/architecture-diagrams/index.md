---
layout: publication
title: "Knowledge Architecture Diagrams"
description: "Visual architecture diagrams of the Knowledge system (P0): system overview, knowledge layers, component architecture, session lifecycle, distributed flow, publication pipeline, security boundaries, and deployment tiers. Companion to Publication #14."
pub_id: "Publication #15"
version: "v1"
date: "2026-02-26"
permalink: /publications/architecture-diagrams/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "architecture, diagrams, mermaid, knowledge, distributed, security"
---

# Knowledge Architecture Diagrams
{: #pub-title}

> **Parent publication**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | **Analysis companion**: [#14 — Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Visual companion to the architecture analysis |
| [System Overview](#1-system-overview--c4-context) | C4 context diagram — Knowledge at center |
| [Knowledge Layers](#2-knowledge-layers) | 4-layer stack: Core → Proven → Harvested → Session |
| [Session Lifecycle](#4-session-lifecycle) | Wakeup → work → checkpoint → save → PR → merge |
| [Distributed Flow](#5-distributed-flow--push-and-pull) | Push (wakeup) and pull (harvest) with promotion pipeline |
| [Full Documentation](#full-documentation) | All 14 diagrams with complete explanations |

## Target Audience

| Audience | Focus |
|----------|-------|
| **Network Administrators** | Distributed flow (#5), security boundaries (#7), deployment tiers (#8) |
| **System Administrators** | Deployment tiers (#8), GitHub integration (#11), publication pipeline (#6) |
| **Programmers** | Component architecture (#3), session lifecycle (#4), recovery ladder (#10) |
| **Managers** | System overview (#1), knowledge layers (#2), quality dependencies (#9) |

## Abstract

Publication #14 (Architecture Analysis) examines the system through analytical narrative. This publication is the **visual companion** — 14 Mermaid diagrams that render the Knowledge system's structure, flows, boundaries, and dependencies into interactive visualizations.

This summary presents the 4 key diagrams. The [complete documentation]({{ '/publications/architecture-diagrams/full/' | relative_url }}) includes all 14 diagrams covering security boundaries, deployment tiers, quality dependencies, recovery paths, and GitHub integration.

Closes #317

## 1. System Overview — C4 Context

The Knowledge system (P0) at the center of its constellation: satellite projects, GitHub platform, GitHub Pages, Claude Code sessions, and the developer.

```mermaid
graph TB
    subgraph External["External Actors"]
        User["👤 Martin Paquet<br/>Developer & Architect"]
        GitHub["🐙 GitHub Platform<br/>Repos, Issues, PRs, Projects v2"]
        Pages["📄 GitHub Pages<br/>packetqc.github.io/*"]
        ClaudeCode["🤖 Claude Code<br/>AI Session Container"]
    end

    subgraph Core["Knowledge System (P0)"]
        CLAUDE["CLAUDE.md<br/>3000+ lines<br/>Core methodology"]
        Patterns["patterns/<br/>Proven approaches"]
        Lessons["lessons/<br/>Known pitfalls"]
        Methodology["methodology/<br/>How we work"]
        Minds["minds/<br/>Harvested intel"]
        Notes["notes/<br/>Session memory"]
        Pubs["publications/<br/>13 publications"]
        Scripts["scripts/<br/>gh_helper, generate_og"]
        Docs["docs/<br/>GitHub Pages source"]
    end

    subgraph Satellites["Satellite Projects"]
        P1["P1 — MPLIB<br/>Storage Pipeline"]
        P2["P2 — STM32 PoC<br/>Embedded System"]
        P3["P3 — knowledge-live<br/>Live Streaming"]
        P4["P4 — MPLIB Dev<br/>Staging"]
        P5["P5 — PQC<br/>Post-Quantum Crypto"]
    end

    User -->|"commands<br/>wakeup, save, harvest"| ClaudeCode
    ClaudeCode -->|"reads on wakeup"| CLAUDE
    ClaudeCode -->|"push to task branch"| GitHub
    ClaudeCode -->|"API via gh_helper.py"| GitHub
    GitHub -->|"PR merge → deploy"| Pages
    CLAUDE -.->|"push methodology<br/>(wakeup)"| Satellites
    Satellites -.->|"pull insights<br/>(harvest)"| Minds
    Docs -->|"Jekyll build"| Pages
    Notes -->|"session persistence"| ClaudeCode
    Minds -->|"promote"| Patterns
    Minds -->|"promote"| Lessons
```


The core repo contains all methodology, publications, and tooling. Satellites inherit on `wakeup` (push) and contribute back via `harvest` (pull). GitHub Pages publishes the web presence.

## 2. Knowledge Layers

Four layers of decreasing stability and increasing currency — from DNA (core) to heartbeat (session).

```mermaid
graph TB
    subgraph Layer1["Layer 1 — Core (Stable)"]
        style Layer1 fill:#ecfdf5,stroke:#0f766e
        CM["CLAUDE.md<br/>Identity, methodology,<br/>evolution log<br/>3000+ lines"]
    end

    subgraph Layer2["Layer 2 — Proven (Validated)"]
        style Layer2 fill:#dbeafe,stroke:#2563eb
        PAT["patterns/<br/>Battle-tested<br/>approaches"]
        LES["lessons/<br/>Known pitfalls<br/>(20 entries)"]
        MET["methodology/<br/>Workflow specs<br/>& templates"]
    end

    subgraph Layer3["Layer 3 — Harvested (Evolving)"]
        style Layer3 fill:#fef3c7,stroke:#d97706
        MIN["minds/<br/>Fresh insights<br/>from satellites"]
    end

    subgraph Layer4["Layer 4 — Session (Ephemeral)"]
        style Layer4 fill:#fce7f3,stroke:#db2777
        NOT["notes/<br/>Per-session<br/>working memory"]
    end

    NOT -->|"remember harvest:"| MIN
    MIN -->|"harvest --promote"| PAT
    MIN -->|"harvest --promote"| LES
    MIN -->|"harvest --stage evolution"| CM
    PAT -->|"inherited on wakeup"| NOT
    CM -->|"read on wakeup<br/>(step 0)"| NOT

    subgraph ReadOrder["Reading Order"]
        R1["1. CLAUDE.md"] --> R2["2. methodology/"]
        R2 --> R3["3. patterns/"]
        R3 --> R4["4. lessons/"]
        R4 --> R5["5. minds/"]
    end
```


Knowledge flows upward through the promotion pipeline and downward through the wakeup protocol.

## 4. Session Lifecycle

Every Claude Code session follows a deterministic path from auto-wakeup to save.

```mermaid
flowchart TD
    Start([Session Start]) ==> AutoWakeup["Auto-wakeup<br/>⏳ Wakeup starting..."]
    AutoWakeup --> CheckSkip{{"User says<br/>skip?"}}
    CheckSkip -->|"Yes"| RawSession["Raw Session<br/>(no sunglasses — NPC)"]
    CheckSkip -->|"No"| Step0

    Step0["Step 0: Read knowledge<br/>git clone packetqc/knowledge"] --> Step03["Step 0.3: Token detection<br/>GH_TOKEN env? /tmp/.gh_token?"]
    Step03 --> Step05["Step 0.5: Bootstrap scaffold<br/>Create missing files"]
    Step05 --> Step055["Step 0.55: Self-heal<br/>Update stale CLAUDE.md"]
    Step055 --> Step056["Step 0.56: Merge self-heal PR<br/>(if elevated)"]
    Step056 --> Step07["Step 0.7: Sync upstream<br/>git fetch + merge default"]
    Step07 --> Step09{{"Checkpoint<br/>detected?"}}
    Step09 -->|"Yes"| Resume["resume<br/>Restart from checkpoint"]
    Step09 -->|"No"| Steps1to8["Steps 1-8: Read evolution,<br/>minds/, notes/, plan,<br/>sync assets, git log,<br/>branches, summarize"]
    Resume --> Work
    Steps1to8 --> Step9["Step 9: Print help table"]
    Step9 --> Step10{{"Core repo +<br/>healthcheck > 24h?"}}
    Step10 -->|"Yes"| HarvestPrompt["Prompt: Run<br/>harvest --healthcheck?"]
    Step10 -->|"No"| AddressMsg["Step 11: Address<br/>user's entry message"]
    HarvestPrompt --> AddressMsg
    AddressMsg --> Work

    Work(["💻 Work Phase"]) --> Save

    Save["save protocol"] --> WriteNotes["1. Write session notes"]
    WriteNotes --> Commit["2. Commit on task branch"]
    Commit --> Push["3. Push to origin"]
    Push --> CreatePR["4. Create PR → default branch"]
    CreatePR --> CheckElevated{{"Elevated?"}}
    CheckElevated -->|"Yes"| AutoMerge["5. Auto-merge via API"]
    CheckElevated -->|"No"| ManualMerge["5. ⏸ User merges PR"]
    AutoMerge --> SyncBack["6. Sync default branch"]
    ManualMerge --> SyncBack
    SyncBack --> Done([Session End])

    Work -->|"Crash!"| Checkpoint["Auto-checkpoint<br/>notes/checkpoint.json"]
    Checkpoint -->|"Next session"| Start

    Work -->|"Compaction"| Refresh["refresh<br/>Re-read CLAUDE.md<br/>+ git status + help"]
    Refresh --> Work
```


Three phases: boot (wakeup), work, and delivery (save). Crash recovery via checkpoints. Context loss via `refresh`.

## 5. Distributed Flow — Push and Pull

Bidirectional knowledge flow with the promotion pipeline.

```mermaid
flowchart TB
    subgraph Master["Master Mind (P0 — Knowledge)"]
        direction TB
        CoreCM["CLAUDE.md<br/>v48"]
        CorePat["patterns/"]
        CoreLes["lessons/"]
        CoreMet["methodology/"]
        CoreMinds["minds/"]
        Dashboard["Dashboard<br/>(Publication #4a)"]
    end

    subgraph SatA["P1 — MPLIB"]
        SatA_CM["CLAUDE.md<br/>← knowledge-version: vN →"]
        SatA_Notes["notes/"]
        SatA_Pubs["publications/"]
    end

    subgraph SatB["P2 — STM32 PoC"]
        SatB_CM["CLAUDE.md"]
        SatB_Notes["notes/"]
    end

    subgraph SatC["P3 — knowledge-live"]
        SatC_CM["CLAUDE.md"]
        SatC_Notes["notes/"]
        SatC_Pubs["publications/"]
    end

    CoreCM ==>|"Push on wakeup<br/>(methodology, commands)"| SatA_CM
    CoreCM ==>|"Push"| SatB_CM
    CoreCM ==>|"Push"| SatC_CM

    SatA_Notes -.->|"harvest MPLIB<br/>(pull insights)"| CoreMinds
    SatA_Pubs -.->|"publication<br/>detection"| CoreMinds
    SatB_Notes -.->|"harvest STM32"| CoreMinds
    SatC_Notes -.->|"harvest knowledge-live"| CoreMinds
    SatC_Pubs -.->|"publication<br/>detection"| CoreMinds

    subgraph Promotion["Promotion Pipeline"]
        direction LR
        Review["🔍 Review"] --> Stage["📦 Stage"]
        Stage --> Promote["✅ Promote"]
        Promote --> Auto["🔄 Auto"]
    end

    CoreMinds --> Review
    Promote -->|"lesson"| CoreLes
    Promote -->|"pattern"| CorePat
    Promote -->|"methodology"| CoreMet
    Promote -->|"evolution"| CoreCM

    CoreMinds -->|"healthcheck"| Dashboard
```


Push delivers methodology outward on wakeup. Harvest pulls insights inward. The promotion pipeline advances insights from raw to core.

## Full Documentation

The [complete documentation]({{ '/publications/architecture-diagrams/full/' | relative_url }}) includes all 14 diagrams:

| # | Diagram | What it shows |
|---|---------|---------------|
| 1 | System Overview | C4 context — Knowledge at center |
| 2 | Knowledge Layers | 4-layer stack with promotion flow |
| 3 | Component Architecture | All folders, scripts, relationships |
| 4 | Session Lifecycle | Wakeup → work → save flowchart |
| 5 | Distributed Flow | Push/pull with promotion pipeline |
| 6 | Publication Pipeline | Source → EN/FR summary/complete |
| 7 | Security Boundaries | Proxy model, allowed/blocked ops |
| 8 | Deployment Tiers | Production/development dual-role |
| 9 | Quality Dependencies | 13 qualities dependency graph |
| 10 | Recovery Ladder | 5 recovery paths by failure mode |
| 11 | GitHub Integration | Issues, PRs, boards lifecycle |
| 12 | System Architecture Mindmap | 9-pillar bird's-eye navigation map |
| 13 | Core Nucleus Mindmap | File-level structure with weight analysis |
| 14 | Publication Structure Mindmap | 9-branch publication anatomy |

**Source**: [Issue #317](https://github.com/packetqc/knowledge/issues/317), [Issue #318](https://github.com/packetqc/knowledge/issues/318) — Architecture exploration sessions.

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
