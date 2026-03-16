---
layout: publication
title: "Knowledge 2.0 Architecture Diagrams"
description: "Visual architecture diagrams of the Knowledge 2.0 multi-module system: system overview, mind-first memory architecture, session lifecycle, module interaction flow. Companion to Publication #14."
pub_id: "Publication #15"
version: "v2"
date: "2026-03-16"
permalink: /publications/architecture-diagrams/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "architecture, diagrams, mermaid, knowledge 2.0, multi-module, mind-first"
---

# Knowledge 2.0 Architecture Diagrams
{: #pub-title}

> **Parent publication**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | **Analysis companion**: [#14 — Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Visual companion to the Knowledge 2.0 architecture |
| [System Overview](#1-system-overview--c4-context) | C4 context — Multi-module system at center |
| [Mind-First Memory](#2-mind-first-memory-architecture) | 4-tier memory: Mindmap → Domain JSONs → Near → Far |
| [Session Lifecycle](#4-session-lifecycle) | session_init → /mind-context → memory_append → archive |
| [Module Interaction](#5-module-interaction-flow) | K_MIND central hub, compilation pipelines, skill invocations |
| [Full Documentation](#full-documentation) | All 14 diagrams with complete explanations |

## Target Audience

| Audience | Focus |
|----------|-------|
| **Network Administrators** | Module interaction (#5), security boundaries (#7), web architecture (#8) |
| **System Administrators** | Web architecture (#8), GitHub integration (#11), publication pipeline (#6) |
| **Programmers** | Multi-module architecture (#3), session lifecycle (#4), recovery paths (#10) |
| **Managers** | System overview (#1), mind-first memory (#2), quality dependencies (#9) |

## Abstract

Publication #14 (Architecture Analysis) examines the system through analytical narrative. This publication is the **visual companion** — 14 Mermaid diagrams that render the Knowledge 2.0 multi-module system's structure, flows, boundaries, and dependencies into interactive visualizations.

This summary presents the 4 key diagrams. The [complete documentation]({{ '/publications/architecture-diagrams/full/' | relative_url }}) includes all 14 diagrams covering security boundaries, web architecture, quality dependencies, recovery paths, and GitHub integration.

## 1. System Overview — C4 Context

The Knowledge 2.0 system at the center of its constellation: 5 K_ modules, GitHub platform, GitHub Pages (.nojekyll static hosting), Claude Code sessions, and the developer.

```mermaid
graph TB
    subgraph External["External Actors"]
        User["👤 Martin Paquet<br/>Developer & Architect"]
        GitHub["🐙 GitHub Platform<br/>Repos, Issues, PRs, Projects v2"]
        Pages["📄 GitHub Pages<br/>.nojekyll static hosting"]
        ClaudeCode["🤖 Claude Code<br/>AI Session Engine"]
    end

    subgraph System["Knowledge 2.0 — Multi-Module System"]
        subgraph KMIND["K_MIND — Core Memory"]
            MindMap["mind_memory.md<br/>Mermaid mindmap<br/>Operating directive grid"]
            Sessions["sessions/<br/>near_memory + far_memory<br/>+ 16 topic archives"]
            DomainJSON["Domain JSONs<br/>conventions, work,<br/>architecture, constraints"]
            ScriptsM["10 Python scripts<br/>memory_append, recall,<br/>gh_helper, mindmap_filter"]
        end

        subgraph KDOCS["K_DOCS — Documentation Pipeline"]
            Viewer["docs/index.html<br/>Static JS viewer<br/>4 themes"]
            Interfaces["5 Interfaces<br/>navigator, session, task,<br/>project, live-mindmap"]
            Pubs["25+ Publications<br/>EN/FR × summary/full"]
            ScriptsD["7 scripts<br/>capture, stitch,<br/>webcard pipeline"]
        end

        subgraph KGITHUB["K_GITHUB — GitHub Integration"]
            SyncGH["sync_github.py<br/>Issue/PR sync + enrich"]
        end

        subgraph KPROJECTS["K_PROJECTS — Project Management"]
            ProjReg["projects.json<br/>P# registry + 2 skills"]
        end

        subgraph KVALIDATION["K_VALIDATION — QA"]
            TaskWF["8-stage task workflow<br/>5 QA skills + 5 scripts"]
        end
    end

    User -->|"skill invocations<br/>/mind-context, /docs-create"| ClaudeCode
    ClaudeCode -->|"reads mindmap<br/>+ domain JSONs"| KMIND
    ClaudeCode -->|"memory_append.py<br/>every turn"| Sessions
    ClaudeCode -->|"git push main"| GitHub
    ClaudeCode -->|"API via gh_helper.py"| GitHub
    GitHub -->|"push → deploy"| Pages
    Viewer -->|"client-side render<br/>markdown + mermaid"| Pages
    SyncGH -.->|"fetch issues/PRs"| GitHub
    KVALIDATION -.->|"compile tasks/sessions<br/>→ docs/data/"| Viewer
    KPROJECTS -.->|"compile projects<br/>→ docs/data/"| Viewer
```


The system is organized as 5 K_ modules under `Knowledge/`. K_MIND is the mandatory core. Other modules provide specialized capabilities. GitHub Pages serves the static web viewer with client-side rendering.

## 2. Mind-First Memory Architecture

Four tiers of decreasing stability and increasing granularity — from the directive grid (mindmap) to the full verbatim archive.

```mermaid
graph TB
    subgraph Tier1["Tier 1 — Mind Memory (Directive Grid)"]
        style Tier1 fill:#ecfdf5,stroke:#0f766e
        MM["mind_memory.md<br/>Mermaid mindmap<br/>264 nodes, 7 groups<br/>Always loaded first"]
    end

    subgraph Tier2["Tier 2 — Domain JSONs (Structured References)"]
        style Tier2 fill:#dbeafe,stroke:#2563eb
        CONV["conventions.json<br/>Reusable patterns<br/>(per module)"]
        WORK["work.json<br/>Accomplished/staged<br/>results (per module)"]
        ARCH["architecture.json<br/>System design<br/>references"]
        CONST["constraints.json<br/>Known limitations<br/>& boundaries"]
    end

    subgraph Tier3["Tier 3 — Near Memory (Session Summaries)"]
        style Tier3 fill:#fef3c7,stroke:#d97706
        NEAR["near_memory.json<br/>One-line summaries<br/>+ far_memory pointers<br/>+ mind_memory refs"]
    end

    subgraph Tier4["Tier 4 — Far Memory (Verbatim + Archives)"]
        style Tier4 fill:#fce7f3,stroke:#db2777
        FAR["far_memory.json<br/>Full verbatim<br/>conversation history"]
        ARCHIVES["archives/<br/>16 topic-based<br/>archived sessions"]
    end

    MM -->|"directives govern<br/>all behavior"| CONV
    MM -->|"work nodes track<br/>accomplished state"| WORK
    NEAR -->|"pointers to<br/>message indices"| FAR
    FAR -->|"far_memory_split.py<br/>by subject"| ARCHIVES
    CONV -->|"staged conventions<br/>from session"| NEAR
    WORK -->|"staged results<br/>from session"| NEAR

    subgraph ReadOrder["Loading Order (session start)"]
        R1["1. mind_memory.md"] --> R2["2. depth_config.json"]
        R2 --> R3["3. near_memory.json"]
        R3 --> R4["4. Domain JSONs<br/>(on demand)"]
        R4 --> R5["5. memory_recall.py<br/>(archived topics)"]
    end

    subgraph Scripts["Deterministic Scripts"]
        S1["memory_append.py<br/>Every turn"]
        S2["far_memory_split.py<br/>Archive by topic"]
        S3["memory_recall.py<br/>Search archives"]
        S4["mindmap_filter.py<br/>Depth-filtered render"]
        S5["memory_stats.py<br/>Context occupancy"]
    end
```


Knowledge flows upward through the staging pipeline and downward as operational directives. All mechanical operations use deterministic Python scripts.

## 4. Session Lifecycle

Every Claude Code session follows a deterministic lifecycle managed by K_MIND scripts.

```mermaid
flowchart TD
    Start([Session Start]) ==> Init["session_init.py<br/>--session-id UUID"]
    Init --> CheckResume{{"--preserve-active<br/>flag?"}}
    CheckResume -->|"Yes (resume)"| LoadContext
    CheckResume -->|"No (fresh)"| ArchivePrev["Archive previous session<br/>carry forward last_session"]
    ArchivePrev --> LoadContext

    LoadContext["/mind-context skill"] --> ReadMind["1. mindmap_filter.py<br/>Render depth-filtered mindmap"]
    ReadMind --> ReadStats["2. memory_stats.py<br/>Context occupancy table"]
    ReadStats --> ReadNear["3. Display near_memory<br/>Last 5 summaries"]
    ReadNear --> DisplayAll["Output mindmap +<br/>context + stats<br/>to conversation"]
    DisplayAll --> Ready(["✅ Session Ready"])

    Ready --> Work

    subgraph Work["💻 Work Phase — Every Turn"]
        direction TB
        UserMsg["User message"] --> DoWork["Claude processes task"]
        DoWork --> Append["memory_append.py<br/>--role user --content ...<br/>--role2 assistant --content2 ...<br/>--summary ... --mind-refs ..."]
        Append --> UpdateMind["Update mind_memory.md<br/>nodes if needed"]
        UpdateMind --> UpdateJSON["Update domain JSONs<br/>if relevant"]
    end

    Work --> TopicDone{{"Topic<br/>complete?"}}
    TopicDone -->|"Yes"| Split["far_memory_split.py<br/>--topic 'Name'<br/>--start-msg N --end-msg N"]
    TopicDone -->|"No"| Work
    Split --> Work

    Work -->|"Compaction!"| Recovery["Compaction Recovery"]
    Recovery --> ReloadContext["/mind-context<br/>Re-read mindmap + near_memory"]
    ReloadContext --> NeedRecall{{"Need details?"}}
    NeedRecall -->|"Yes"| Recall["memory_recall.py<br/>--subject 'topic'"]
    NeedRecall -->|"No"| Work
    Recall --> Work

    Work --> SessionEnd(["Session End"])
```


Three phases: boot (/mind-context), work (memory_append every turn), and recovery (compaction handling). The mindmap is always loaded first as it contains all behavioral directives.

## 5. Module Interaction Flow

How the 5 K_ modules interact: K_MIND as central hub, compilation pipelines feeding the web viewer.

```mermaid
flowchart TB
    subgraph KMIND["K_MIND — Central Hub"]
        direction TB
        MindMap["mind_memory.md<br/>264 nodes"]
        GHHelper["gh_helper.py<br/>GitHub API wrapper"]
        MemScripts["Memory scripts<br/>append, recall, split"]
        DomainJSONs["Domain JSONs<br/>per module"]
    end

    subgraph KDOCS["K_DOCS — Documentation"]
        direction TB
        Methodology["7 methodologies<br/>web pipeline, audience,<br/>webcard generation"]
        WebConv["Web conventions<br/>diagram, CSS theme,<br/>render, OG images"]
        DocScripts["7 scripts<br/>capture, stitch, webcard"]
    end

    subgraph KGITHUB["K_GITHUB"]
        direction TB
        SyncScripts["3 sync scripts<br/>issues, roadmap, enrich"]
    end

    subgraph KPROJECTS["K_PROJECTS"]
        direction TB
        CompileP["compile_projects.py<br/>+ compile_from_mind.py"]
        ProjSkills["Skills:<br/>project-create,<br/>project-manage"]
    end

    subgraph KVALIDATION["K_VALIDATION"]
        direction TB
        CompileV["compile_tasks.py<br/>+ compile_sessions.py"]
        ValSkills["Skills:<br/>task-received, work-cycle,<br/>integrity-check, normalize"]
    end

    subgraph WebViewer["docs/ — Static Web Viewer"]
        direction TB
        DataJSON["data/<br/>projects.json<br/>sessions.json<br/>tasks.json"]
        I1["I1: Main Navigator"]
        I2["I2: Session Review"]
        I3["I3: Task Workflow"]
        I4["I4: Project Viewer"]
        I5["I5: Live Mindmap"]
    end

    MindMap ==>|"directives"| KDOCS
    MindMap ==>|"directives"| KGITHUB
    MindMap ==>|"directives"| KPROJECTS
    MindMap ==>|"directives"| KVALIDATION

    GHHelper -->|"shared API"| SyncScripts
    GHHelper -->|"shared API"| ProjSkills

    CompileP -->|"projects.json"| DataJSON
    CompileV -->|"tasks.json<br/>sessions.json"| DataJSON

    SyncScripts -.->|"fetch from<br/>GitHub API"| GHHelper

    DataJSON -->|"consumed by"| I1
    DataJSON -->|"consumed by"| I2
    DataJSON -->|"consumed by"| I3
    DataJSON -->|"consumed by"| I4
    MindMap -->|"mermaid source"| I5
```


K_MIND is the hub — its mindmap provides directives to all modules, and gh_helper.py is the shared GitHub API wrapper. Compilation scripts produce JSON data consumed by the 5 web interfaces.

## Full Documentation

The [complete documentation]({{ '/publications/architecture-diagrams/full/' | relative_url }}) includes all 14 diagrams:

| # | Diagram | What it shows |
|---|---------|---------------|
| 1 | System Overview | C4 context — Multi-module system at center |
| 2 | Mind-First Memory | 4-tier memory architecture with scripts |
| 3 | Multi-Module Architecture | 5 K_ modules, scripts, relationships |
| 4 | Session Lifecycle | session_init → work → archive flowchart |
| 5 | Module Interaction | K_MIND hub, compilation pipelines |
| 6 | Publication Pipeline | Source → static viewer → EN/FR × 4 themes |
| 7 | Security Boundaries | Proxy model, allowed/blocked ops |
| 8 | Web Architecture | Static viewer, 4 themes, 5 interfaces |
| 9 | Quality Dependencies | 13 qualities dependency graph |
| 10 | Recovery Paths | K_MIND recovery: compaction, recall, init |
| 11 | GitHub Integration | K_GITHUB sync, compilation, board lifecycle |
| 12 | System Architecture Mindmap | K2.0 architectural pillars |
| 13 | Module Structure Mindmap | File-level multi-module structure |
| 14 | Publication Structure Mindmap | Publication anatomy with static viewer |

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — the system these diagrams visualize |
| 4 | [Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }}) | Architecture — multi-module flow (Diagram 5) |
| 7 | [Harvest Protocol]({{ '/publications/harvest-protocol/' | relative_url }}) | Protocol — data flow (Diagrams 5, 11) |
| 8 | [Session Management]({{ '/publications/session-management/' | relative_url }}) | Lifecycle — K_MIND session system (Diagram 4) |
| 9 | [Security by Design]({{ '/publications/security-by-design/' | relative_url }}) | Security — proxy boundaries (Diagram 7) |
| 12 | [Project Management]({{ '/publications/project-management/' | relative_url }}) | Projects — K_PROJECTS module (Diagrams 1, 8) |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge 2.0: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
