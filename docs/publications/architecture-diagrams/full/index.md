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


**Legend**: The core knowledge repo contains all methodology, publications, and tooling. Satellites inherit methodology on `wakeup` (push) and contribute insights back via `harvest` (pull). GitHub acts as the persistence and collaboration layer. GitHub Pages publishes the web presence. Claude Code is the execution environment — ephemeral containers that become aware via the `wakeup` protocol.

---

## 2. Knowledge Layers

The system organizes knowledge into 4 layers of decreasing stability and increasing currency. Core is the DNA — rarely changing, maximum authority. Session is the heartbeat — ephemeral, maximum currency.

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


**Legend**: Knowledge flows upward (session → harvested → proven → core) through the promotion pipeline. It flows downward (core → session) through the wakeup protocol. The reading order for new Claude instances follows the stability gradient: most stable first, most current last.

---

## 3. Component Architecture

The major folders, scripts, and their relationships within the knowledge repository.

```mermaid
graph LR
    subgraph Root["Repository Root"]
        CM["CLAUDE.md<br/>Core brain"]
        PLAN["PLAN.md<br/>Roadmap"]
        NEWS["NEWS.md<br/>Changelog"]
        LINKS["LINKS.md<br/>URL directory"]
    end

    subgraph Knowledge["Knowledge Folders"]
        patterns["patterns/<br/>Proven patterns"]
        lessons["lessons/<br/>Pitfalls"]
        methodology["methodology/<br/>Specifications"]
        minds["minds/<br/>Harvested"]
        notes["notes/<br/>Sessions"]
        projects["projects/<br/>P# registry"]
    end

    subgraph Content["Content Folders"]
        pubs["publications/<br/>Source docs"]
        docs["docs/<br/>Web pages"]
        assets["docs/assets/<br/>OG images"]
        layouts["docs/_layouts/<br/>HTML layouts"]
        refs["references/<br/>Source assets"]
    end

    subgraph Tooling["Scripts & Tools"]
        gh["scripts/<br/>gh_helper.py"]
        og["scripts/<br/>generate_og_gifs.py"]
        pqc["scripts/<br/>pqc_envelope.py"]
        sync["scripts/<br/>sync_roadmap.py"]
    end

    subgraph Live["Live Infrastructure"]
        beacon["live/<br/>knowledge_beacon.py"]
        scanner["live/<br/>knowledge_scanner.py"]
        capture["live/<br/>stream_capture.py"]
    end

    CM -->|"references"| Knowledge
    CM -->|"documents"| Content
    pubs -->|"pub sync"| docs
    docs -->|"Jekyll build"| assets
    og -->|"generates"| assets
    gh -->|"API calls"| GitHub["GitHub API"]
    refs -->|"source images"| og
    minds -->|"harvest --promote"| patterns
    minds -->|"harvest --promote"| lessons
    beacon -->|"port 21337"| scanner
```


**Legend**: The repository is organized into five major groups: root files (entry points), knowledge folders (the intelligence layers), content folders (publications and web pages), scripts (automation tooling), and live infrastructure (inter-instance communication). Arrows show data flow between components.

---

## 4. Session Lifecycle

Every Claude Code session follows a deterministic lifecycle. This flowchart shows the complete path from session start to session end, including crash recovery and context loss paths.

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


**Legend**: The session lifecycle has three phases: boot (wakeup), work, and delivery (save). Crash recovery uses checkpoints. Context loss recovery uses `refresh`. The elevated path (with token) is fully autonomous; the semi-automatic path requires one user click to merge the PR.

---

## 5. Distributed Flow — Push and Pull

The bidirectional knowledge flow between the master mind (P0) and satellite projects. Push delivers methodology outward; harvest pulls insights inward. The promotion pipeline advances insights from raw to core.

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


**Legend**: Thick solid arrows represent the push flow (wakeup). Dashed arrows represent the pull flow (harvest). The promotion pipeline advances insights through four stages: review (human validated), stage (typed and targeted), promote (written to core), auto (queued for next healthcheck). The dashboard is updated on every harvest.

---

## 6. Publication Pipeline

Each publication exists at three tiers: source (canonical), summary (web), and complete (web). Each tier is bilingual (EN + FR). This diagram shows the sync and review flows.

```mermaid
flowchart LR
    subgraph Source["Source (Canonical)"]
        SRC["publications/<slug>/v1/<br/>README.md"]
        SRC_Assets["assets/"]
        SRC_Media["media/"]
    end

    subgraph EN_Web["EN Web Pages"]
        EN_Sum["docs/publications/<slug>/<br/>index.md<br/>(Summary)"]
        EN_Full["docs/publications/<slug>/full/<br/>index.md<br/>(Complete)"]
    end

    subgraph FR_Web["FR Web Pages"]
        FR_Sum["docs/fr/publications/<slug>/<br/>index.md<br/>(Résumé)"]
        FR_Full["docs/fr/publications/<slug>/full/<br/>index.md<br/>(Complet)"]
    end

    subgraph Validation["Validation & Review"]
        PubCheck["pub check #N<br/>Structure validation"]
        PubSync["pub sync #N<br/>Source → docs sync"]
        DocReview["doc review #N<br/>Freshness check"]
        DocsCheck["docs check<br/>Page validation"]
    end

    subgraph Assets_Web["Web Assets"]
        OG_EN["assets/og/<br/><card>-en-cayman.gif"]
        OG_FR["assets/og/<br/><card>-fr-cayman.gif"]
    end

    SRC ==>|"pub sync"| EN_Sum
    SRC ==>|"pub sync"| EN_Full
    EN_Sum -->|"translate"| FR_Sum
    EN_Full -->|"translate"| FR_Full
    EN_Sum <-->|"language bar"| FR_Sum
    EN_Full <-->|"language bar"| FR_Full
    EN_Sum -->|"link to full"| EN_Full
    FR_Sum -->|"link to full"| FR_Full
    SRC_Assets -->|"copy"| EN_Full
    SRC_Media -->|"copy"| EN_Full

    PubCheck -->|"validates"| SRC
    PubCheck -->|"validates"| EN_Web
    PubCheck -->|"validates"| FR_Web
    PubSync -->|"compares"| SRC
    PubSync -->|"syncs to"| EN_Web
    DocReview -->|"freshness"| SRC
    DocsCheck -->|"pages"| EN_Web
    DocsCheck -->|"pages"| FR_Web

    EN_Sum --- OG_EN
    FR_Sum --- OG_FR
```


**Legend**: The source README.md is the single source of truth. `pub sync` propagates changes from source to EN web pages. Translation produces FR mirrors. Each web page links to its language mirror (EN ↔ FR) and to its depth variant (summary ↔ complete). Four validation commands ensure structural integrity, source-docs concordance, content freshness, and page-level correctness.

---

## 7. Security Boundaries

The proxy model governing what Claude Code sessions can and cannot do. The container proxy mediates all git operations while Python urllib bypasses it for API access.

```mermaid
flowchart TB
    subgraph Container["Claude Code Container"]
        Session["Claude Session<br/>claude/task-id-xxx"]
        GHHelper["gh_helper.py<br/>(Python urllib)"]
        GitCLI["git CLI"]
        CurlCLI["curl"]
    end

    subgraph Proxy["Container Proxy"]
        GitProxy["Git Proxy<br/>http://local_proxy@127.0.0.1:PORT"]
        HTTPProxy["HTTP Proxy<br/>(intercepts curl)"]
    end

    subgraph GitHub_API["GitHub Platform"]
        REST["REST API<br/>api.github.com"]
        GraphQL["GraphQL API<br/>api.github.com/graphql"]
        GitRemote["Git Remote<br/>github.com/packetqc/*"]
    end

    Session --> GitCLI
    Session --> GHHelper
    Session --> CurlCLI

    GitCLI -->|"push (assigned branch only)"| GitProxy
    GitCLI -->|"clone (public, initial only)"| GitProxy
    GitProxy -->|"✅ Authorized repo+branch"| GitRemote
    GitProxy -->|"❌ 403 other branches"| GitRemote
    GitProxy -->|"❌ 403 other repos"| GitRemote

    CurlCLI -->|"all requests"| HTTPProxy
    HTTPProxy -->|"❌ 401 (strips auth)"| REST

    GHHelper -->|"✅ Direct socket<br/>(bypasses proxy)"| REST
    GHHelper -->|"✅ Direct socket<br/>(bypasses proxy)"| GraphQL

    subgraph Allowed["✅ Allowed Operations"]
        A1["Push to assigned claude/* branch"]
        A2["Clone public repos (initial)"]
        A3["API: PR create/merge (urllib)"]
        A4["API: Projects v2 (urllib)"]
        A5["API: Issues/comments (urllib)"]
    end

    subgraph Blocked["❌ Blocked Operations"]
        B1["Push to default branch"]
        B2["Push to other claude/* branches"]
        B3["Push to other repos"]
        B4["Re-fetch after initial clone"]
        B5["curl with auth headers"]
        B6["Commit signing (foreign repo)"]
    end
```


**Legend**: The container proxy is the primary security boundary. Git operations are restricted to the assigned task branch of the current repo. Python `urllib` (used by `gh_helper.py`) bypasses the proxy entirely, enabling full GitHub API access with a valid token. `curl` is intercepted by the proxy and auth headers are stripped. The two-channel model: git proxy (restricted) + urllib (unrestricted with token).

---

## 8. Deployment Tiers

The multi-tier deployment model where each satellite is simultaneously development (relative to core) and production (at its own level). Every node publishes independently via GitHub Pages.

```mermaid
graph TB
    subgraph Production["SYSTEM PRODUCTION — Core"]
        Core["P0 — Knowledge<br/>packetqc.github.io/knowledge/<br/>Canonical methodology<br/>13 publications"]
    end

    subgraph PreProd["DEV/PRE-PROD relative to Core<br/>PRODUCTION at repo level"]
        S1["P1 — MPLIB<br/>packetqc.github.io/MPLIB/<br/>Own publications<br/>Own project board (#5)"]
        S2["P2 — STM32 PoC<br/>packetqc.github.io/STM32.../<br/>Own publications<br/>Own project board (#6)"]
        S3["P3 — knowledge-live<br/>packetqc.github.io/knowledge-live/<br/>Own publications<br/>Own project board (#7)"]
        S4["P4 — MPLIB Dev<br/>packetqc.github.io/MPLIB_DEV.../<br/>Staging environment<br/>Own project board (#8)"]
    end

    Core ==>|"wakeup push<br/>(methodology)"| S1
    Core ==>|"wakeup push"| S2
    Core ==>|"wakeup push"| S3
    Core ==>|"wakeup push"| S4

    S1 -.->|"harvest pull<br/>(insights)"| Core
    S2 -.->|"harvest pull"| Core
    S3 -.->|"harvest pull"| Core
    S4 -.->|"harvest pull"| Core

    subgraph Lifecycle["Lifecycle"]
        direction LR
        Idea["💡 Idea"] --> SatTest["Satellite testing<br/>(dev)"]
        SatTest --> SatPages["Satellite Pages<br/>(repo-production)"]
        SatPages --> Harvest["harvest to core"]
        Harvest --> CorePromo["Core promotion<br/>(system-production)"]
        CorePromo --> Inherit["All satellites<br/>inherit on wakeup"]
    end

    subgraph DualOrigin["Dual-Origin Links"]
        CoreLink["**core** badge<br/>knowledge/publications/.../<br/>Canonical / approved"]
        SatLink["*satellite* badge<br/><repo>/publications/.../<br/>Development / staging"]
    end
```


**Legend**: The deployment model is multi-tier. Core is system-production — the canonical brain. Each satellite is simultaneously development relative to core (testing ground for new capabilities) and production at its own level (independent GitHub Pages, project boards, publications). Ideas flow: satellite testing → satellite pages → harvest → core promotion → all satellites inherit.

---

## 9. Quality Dependency Graph

The 13 core qualities and how they depend on each other. Autosuffisant is the foundation — if the system depends on external services, nothing else works.

```mermaid
graph TB
    Auto["1. Autosuffisant<br/>(Self-sufficient)<br/>Plain text + Git"]

    Auto --> Autonome["2. Autonome<br/>(Self-propagating)"]
    Auto --> Concordant["3. Concordant<br/>(Structural integrity)"]
    Auto --> Concis["4. Concis<br/>(Critical-subset)"]

    Autonome --> Distribue["7. Distribué<br/>(Bidirectional flow)"]
    Autonome --> Persistant["8. Persistant<br/>(Session → permanent)"]

    Concordant --> Interactif["5. Interactif<br/>(Operable dashboard)"]
    Concis --> Evolutif["6. Évolutif<br/>(Self-growing)"]

    Interactif --> Recursif["9. Récursif<br/>(Self-documenting)"]
    Evolutif --> Recursif

    Distribue --> Securitaire["10. Sécuritaire<br/>(Security by architecture)"]
    Persistant --> Resilient["11. Résilient<br/>(Crash recovery)"]

    Securitaire --> Structure["12. Structuré<br/>(Project hierarchy)"]
    Resilient --> Structure

    Structure --> Integre["13. Intégré<br/>(GitHub platform)"]

    style Auto fill:#ecfdf5,stroke:#0f766e,stroke-width:3px
    style Autonome fill:#dbeafe,stroke:#2563eb
    style Concordant fill:#dbeafe,stroke:#2563eb
    style Concis fill:#dbeafe,stroke:#2563eb
    style Interactif fill:#e0e7ff,stroke:#4f46e5
    style Evolutif fill:#e0e7ff,stroke:#4f46e5
    style Distribue fill:#fef3c7,stroke:#d97706
    style Persistant fill:#fef3c7,stroke:#d97706
    style Recursif fill:#fce7f3,stroke:#db2777
    style Securitaire fill:#fee2e2,stroke:#dc2626
    style Resilient fill:#fee2e2,stroke:#dc2626
    style Structure fill:#f3e8ff,stroke:#7c3aed
    style Integre fill:#f3e8ff,stroke:#7c3aed
```


**Legend**: The dependency graph flows from foundation (autosuffisant — plain text in Git) through enabling qualities (autonome, concordant, concis) to operational qualities (interactif, evolutif) to network qualities (distribue, persistant) to meta-qualities (recursif, securitaire, resilient) to organizational qualities (structure, integre). Each quality reinforces the ones that depend on it.

---

## 10. Recovery Ladder

The five recovery paths, ordered from lightest to heaviest. Each path addresses a different failure mode.

```mermaid
stateDiagram-v2
    [*] --> Working: Session active

    Working --> Disconnected: Client disconnect
    Working --> Compacted: Context window limit
    Working --> Crashed: API 400/500 / container restart
    Working --> StaleUpstream: Other sessions merged PRs

    Disconnected --> BrowserRefresh: Path A — Instant
    BrowserRefresh --> Working: Session may still be alive

    Disconnected --> ManualPR: Path B — Minutes
    ManualPR --> Working: Work was pushed, create PR manually

    Crashed --> ResumeCheck: Check checkpoint
    ResumeCheck --> Resume: notes/checkpoint.json exists
    ResumeCheck --> RecallCheck: No checkpoint
    Resume --> Working: ~10s — restart from last step

    RecallCheck --> Recall: Commits on dead branch
    RecallCheck --> NewSession: No commits found
    Recall --> Working: ~15s — cherry-pick stranded work

    Compacted --> Refresh: Re-read CLAUDE.md + git status
    Refresh --> Working: ~5s — formatting restored

    StaleUpstream --> Wakeup: Full protocol re-run
    Wakeup --> Working: ~30-60s — deep re-sync

    NewSession --> Wakeup: Start fresh
```


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

```mermaid
sequenceDiagram
    participant User as 👤 Developer
    participant Claude as 🤖 Claude Code
    participant GH as 🐙 GitHub API
    participant Board as 📋 Project Board
    participant Pages as 📄 GitHub Pages

    Note over User,Pages: Issue Lifecycle
    User->>GH: Create issue (#N)
    GH->>Board: Link to project board (Todo)
    Claude->>GH: Comment with branch reference
    Claude->>Board: Move to In Progress
    Claude->>Claude: Work on claude/task-branch
    Claude->>GH: Push + Create PR (Closes #N)
    Claude->>GH: Merge PR (if elevated)
    GH->>GH: Auto-close issue #N
    GH->>Board: Auto-move to Done
    GH->>Pages: Deploy from default branch

    Note over User,Pages: Harvest Cycle
    Claude->>GH: Clone satellite (HTTPS)
    Claude->>Claude: Extract insights → minds/
    Claude->>Claude: Update dashboard files
    Claude->>GH: Push + PR + Merge
    GH->>Pages: Deploy updated dashboard

    Note over User,Pages: Project Creation
    User->>Claude: project create "Name"
    Claude->>GH: createProjectV2 (GraphQL)
    Claude->>GH: linkProjectV2ToRepository
    Claude->>Claude: Register P# + scaffold docs/
    Claude->>GH: Push + PR + Merge
    GH->>Pages: Deploy project pages
```


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

```mermaid
mindmap
  root((Knowledge System))
    Identity
      13 qualities
      Free Guy analogy
      48 evolutions
      Martin 30 years XP
    Distributed Architecture
      Bidirectional flow
      4 knowledge layers
      Satellites P1-P5
      Proxy protocol
    Session Lifecycle
      wakeup
      work
      save
      recovery
    Projects
      3 core/child
      3 managed
      1 pre-bootstrap
    Publications
      15 pubs
      3 tiers
      2 languages
    Security
      Ephemeral tokens
      Proxy-aware
      Fork-safe
    Web Presence
      GitHub Pages
      Dual-theme
      40 webcards
    Tools
      7 Python scripts
      Deployed everywhere
    Proven Knowledge
      4 patterns
      20 pitfalls
      30 years distilled
```


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

```mermaid
mindmap
  root((Core Nucleus<br/>~930 KB))
    Brain — 31%
      CLAUDE.md 293 KB
      Identity + methodology
      Evolution log
    Knowledge — 23%
      methodology/ 194 KB
      patterns/ 14 KB
      lessons/ 10 KB
    Intelligence — 13%
      minds/ 71 KB
      projects/ 50 KB
    Tools — 26%
      scripts/ 242 KB
      gh_helper.py
      generate_og_gifs.py
    Infrastructure — 6%
      live/ 53 KB
      beacon + scanner
    Ephemeral
      docs/ 100+ pages
      notes/ 80 KB
      publications/ variable
```


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

```mermaid
mindmap
  root((Publication))
    Source
      publications/slug/v1/README.md
      assets/
      media/
    Web Pages EN
      Summary index.md
      Complete full/index.md
    Web Pages FR
      Résumé index.md
      Complet full/index.md
    Front Matter
      8 required fields
      Jekyll metadata
    Webcards OG
      2 languages
      2 themes
      4 GIFs per pub
    Layout
      Version banner
      Language bar
      Export + printing
      Cross-refs
    System Integration
      Indexes
      Profiles
      CLAUDE.md
      Dashboard
    Identifiers
      Pub number
      Slug
      Tiers
      Origin
    Validation
      pub check
      pub sync
      doc review
      docs check
      normalize
```


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
