---
layout: publication
title: "Knowledge 2.0 Architecture Diagrams — Complete Documentation"
description: "Complete visual architecture: 14 Mermaid diagrams covering multi-module system overview, mind-first memory architecture, K_ module structure, session lifecycle, module interaction flow, publication pipeline, security boundaries, web architecture, quality dependencies, recovery paths, and GitHub integration."
pub_id: "Publication #15 — Full"
version: "v2"
date: "2026-03-16"
permalink: /publications/architecture-diagrams/full/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "architecture, diagrams, mermaid, knowledge 2.0, multi-module, mind-first, security"
---

# Knowledge 2.0 Architecture Diagrams — Complete Documentation
{: #pub-title}

**Contents**

| | |
|---|---|
| [Authors](#authors) | Publication authors |
| [Abstract](#abstract) | Visual companion to the Knowledge 2.0 architecture |
| [Diagram Conventions](#diagram-conventions) | Color coding, notation, Mermaid syntax |
| [1. System Overview](#1-system-overview--c4-context) | C4 context — Multi-module system at center |
| [2. Mind-First Memory Architecture](#2-mind-first-memory-architecture) | 4-tier memory: Mindmap → Domain JSONs → Near → Far |
| [3. Multi-Module Architecture](#3-multi-module-architecture) | 5 K_ modules, scripts, and relationships |
| [4. Session Lifecycle](#4-session-lifecycle) | session_init → /mind-context → memory_append → archive |
| [5. Module Interaction Flow](#5-module-interaction-flow) | K_MIND central hub, compilation pipelines, skill invocations |
| [6. Publication Pipeline](#6-publication-pipeline) | Source → static viewer → EN/FR × summary/full × 4 themes |
| [7. Security Boundaries](#7-security-boundaries) | Proxy model — allowed vs blocked operations |
| [8. Web Architecture](#8-web-architecture) | Static JS viewer, 4 themes, 5 interfaces, .nojekyll |
| [9. Quality Dependencies](#9-quality-dependency-graph) | 13 qualities dependency graph |
| [10. Recovery Paths](#10-recovery-paths) | K_MIND recovery: compaction, recall, session init |
| [11. GitHub Integration](#11-github-integration) | K_GITHUB module, sync scripts, board lifecycle |
| [Related Publications](#related-publications) | Sibling and parent publications |

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Architect of the Knowledge system — a self-evolving AI engineering intelligence built on 30 years of embedded systems, network security, and software development experience. Designed the multi-module architecture documented in these diagrams.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Co-created the architectural diagrams, rendering system structure into Mermaid notation for interactive web visualization. Operates within the system these diagrams describe.

---

## Abstract

Knowledge 2.0 is a **multi-module AI engineering intelligence system** structured around a central memory grid (K_MIND) with specialized satellite modules (K_DOCS, K_GITHUB, K_PROJECTS, K_VALIDATION). This publication is the **visual companion** — 14 Mermaid diagrams that render the system's structure, flows, boundaries, and dependencies into interactive visualizations.

These diagrams cover the full architectural surface: from the high-level C4 context (5 K_ modules at center, GitHub platform, static web viewer) down to the granular security boundaries (proxy layers, API channels) and the mind-first memory architecture (mindmap → domain JSONs → near/far memory → archives).

All diagrams use [Mermaid](https://mermaid.js.org/) syntax, rendered client-side by the static JS viewer via CDN.

---

## Target Audience

| Audience | What to focus on |
|----------|-----------------|
| **Network Administrators** | Module interaction (#5), security boundaries (#7), web architecture (#8) |
| **System Administrators** | Web architecture (#8), GitHub integration (#11), publication pipeline (#6) |
| **Programmers** | Multi-module architecture (#3), session lifecycle (#4), recovery paths (#10) |
| **Managers** | System overview (#1), mind-first memory (#2), quality dependencies (#9) |

## Diagram Conventions

All diagrams use **Mermaid** notation — a markdown-based diagramming language rendered client-side by the static JS viewer.

**Color coding**:

| Color | Meaning | Used for |
|-------|---------|----------|
| Teal / Green | Core / Stable / Mandatory | K_MIND, mind_memory, stable conventions |
| Blue | Active / In-progress | Sessions, active flows, current operations |
| Orange / Amber | Warning / Drift | Version drift, stale content, minor issues |
| Red | Critical / Blocked | Security boundaries, proxy blocks |
| Purple | External / Platform | GitHub, GitHub Pages, external services |
| Gray | Inactive / Pending | Unused paths, pending items |

**Notation**:

| Symbol | Meaning |
|--------|---------|
| Solid arrow (`-->`) | Direct data flow or dependency |
| Dashed arrow (`-.->`) | Indirect or periodic flow |
| Thick arrow (`==>`) | Primary / critical path |
| Subgraph | Logical grouping or boundary |

---

## 1. System Overview — C4 Context

The Knowledge 2.0 system sits at the center of a constellation of actors: 5 internal K_ modules, GitHub platform services, GitHub Pages for static web publishing, Claude Code as the AI session engine, and the human developer.

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


**Legend**: The system is organized as 5 K_ modules under a `Knowledge/` directory. K_MIND is the mandatory core — always loaded, always maintained. Other modules (K_DOCS, K_GITHUB, K_PROJECTS, K_VALIDATION) provide specialized capabilities. Claude Code is the execution environment, reading the mindmap on every session start and maintaining memory via scripts every turn. GitHub Pages serves the static web viewer with client-side markdown and mermaid rendering.

---

## 2. Mind-First Memory Architecture

The system organizes knowledge into 4 tiers of decreasing stability and increasing granularity. The mindmap is the operating directive grid — always loaded first. Domain JSONs provide structured references. Near memory tracks the session in real time. Far memory preserves full verbatim history.

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


**Legend**: Knowledge flows upward (far memory → near memory → domain JSONs → mindmap) through the staging pipeline. It flows downward (mindmap → session behavior) as operational directives. The loading order follows stability: most stable first (mindmap), most granular last (archived far memory). All mechanical operations use deterministic Python scripts — Claude provides intelligence (summaries, topic names) as arguments.

---

## 3. Multi-Module Architecture

The 5 K_ modules, their internal structure, scripts, and relationships within the Knowledge 2.0 repository.

```mermaid
graph LR
    subgraph Root["Repository Root"]
        CLAUDE["CLAUDE.md<br/>K_MIND instructions"]
        ModJSON["modules.json<br/>Module registry"]
        Skills[".claude/skills/<br/>5 root skills"]
    end

    subgraph KMIND["K_MIND — Core Memory (mandatory)"]
        mind["mind/<br/>mind_memory.md"]
        sessions["sessions/<br/>near + far + archives"]
        km_conv["conventions/<br/>conventions.json<br/>depth_config.json"]
        km_work["work/<br/>work.json"]
        km_arch["architecture/<br/>architecture.json"]
        km_const["constraints/<br/>constraints.json"]
        km_scripts["scripts/ (10)<br/>memory_append, recall,<br/>session_init, gh_helper,<br/>mindmap_filter, set_depth,<br/>memory_stats, install"]
    end

    subgraph KDOCS["K_DOCS — Documentation Pipeline"]
        kd_scripts["scripts/ (7)<br/>capture_mindmap.js,<br/>stitch_webcard.py,<br/>generate_webcard.py"]
        kd_method["methodology/ (7)<br/>web-production-pipeline,<br/>documentation-generation,<br/>webcard-generation"]
        kd_conv["conventions/<br/>sessions/ + web/"]
        kd_work["work/<br/>work.json"]
    end

    subgraph KGITHUB["K_GITHUB — GitHub Integration"]
        kg_scripts["scripts/ (3)<br/>sync_github.py,<br/>sync_roadmap.py,<br/>enrich_from_github.py"]
        kg_method["methodology/<br/>github-project-integration"]
    end

    subgraph KPROJECTS["K_PROJECTS — Project Management"]
        kp_data["data/<br/>projects.json<br/>+ project files"]
        kp_scripts["scripts/ (2)<br/>compile_projects.py"]
        kp_skills["skills/ (2)<br/>project-create,<br/>project-manage"]
    end

    subgraph KVALIDATION["K_VALIDATION — QA & Validation"]
        kv_scripts["scripts/ (5)<br/>compile_tasks.py,<br/>compile_sessions.py,<br/>documentation_validation.py"]
        kv_skills["skills/ (5)<br/>task-received, work-cycle,<br/>integrity-check, normalize,<br/>knowledge-validation"]
        kv_method["methodology/ (4)<br/>task-workflow,<br/>session-protocol,<br/>checkpoint-resume"]
    end

    subgraph WebOutput["docs/ — Web Presence"]
        viewer["index.html<br/>Static JS viewer"]
        interfaces["interfaces/ (5)<br/>navigator, session,<br/>task, project, mindmap"]
        pubs["publications/ (25+)<br/>EN + FR mirrors"]
        data["data/<br/>projects.json,<br/>sessions.json,<br/>tasks.json"]
        assets["assets/og/<br/>Webcard GIFs"]
    end

    CLAUDE -->|"loads"| KMIND
    ModJSON -->|"declares"| KDOCS
    ModJSON -->|"declares"| KGITHUB
    ModJSON -->|"declares"| KPROJECTS
    ModJSON -->|"declares"| KVALIDATION
    km_scripts -->|"gh_helper.py<br/>shared API"| KGITHUB
    kv_scripts -->|"compile →"| data
    kp_scripts -->|"compile →"| data
    kd_scripts -->|"capture →"| assets
    pubs -->|"rendered by"| viewer
```


**Legend**: The repository is organized into 5 K_ modules under `Knowledge/`. Each module owns its conventions, work state, and scripts. K_MIND is mandatory (always loaded). Other modules are declared in `modules.json` and loaded on demand. The `docs/` directory is the web output — served by GitHub Pages with .nojekyll (no build step). Compilation scripts in K_VALIDATION and K_PROJECTS produce JSON data consumed by the static viewer's interfaces.

---

## 4. Session Lifecycle

Every Claude Code session follows a deterministic lifecycle managed by K_MIND scripts. The mindmap is loaded first, memory is maintained every turn, and topics are archived when complete.

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


**Legend**: The session lifecycle has three phases: boot (/mind-context), work (memory_append every turn), and recovery (compaction handling). The mind-first principle means the mindmap is always loaded first — it contains all behavioral directives. Far memory stores full verbatim conversation; near memory stores one-line summaries with pointers. Topic archiving keeps far_memory.json manageable. Compaction recovery re-reads the mindmap and near memory, with optional deep recall from archives.

---

## 5. Module Interaction Flow

How the 5 K_ modules interact: K_MIND as central hub, compilation pipelines feeding the web viewer, and skill invocations across modules.

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


**Legend**: K_MIND is the hub — its mindmap provides directives to all modules, and gh_helper.py is the shared GitHub API wrapper. K_PROJECTS and K_VALIDATION compile structured data into `docs/data/` JSON files consumed by the 5 web interfaces. K_GITHUB syncs external GitHub state. K_DOCS owns the web pipeline methodology and conventions. The live mindmap (I5) reads directly from mind_memory.md.

---

## 6. Publication Pipeline

Each publication exists at two web tiers (summary + full), in two languages (EN + FR), rendered by the static JS viewer with 4 theme variants.

```mermaid
flowchart LR
    subgraph Source["Source (K_DOCS methodology)"]
        Method["methodology/<br/>documentation-generation.md"]
        Audience["methodology/<br/>documentation-audience.md<br/>19 segments"]
    end

    subgraph EN_Web["EN Web Pages"]
        EN_Sum["docs/publications/slug/<br/>index.md<br/>(Summary)"]
        EN_Full["docs/publications/slug/full/<br/>index.md<br/>(Complete)"]
    end

    subgraph FR_Web["FR Web Pages"]
        FR_Sum["docs/fr/publications/slug/<br/>index.md<br/>(Résumé)"]
        FR_Full["docs/fr/publications/slug/full/<br/>index.md<br/>(Complet)"]
    end

    subgraph Viewer["Static JS Viewer"]
        ViewerHTML["docs/index.html<br/>2065 lines<br/>Client-side render"]
        Mermaid["Mermaid CDN<br/>Diagram rendering"]
        Themes["4 Themes<br/>cayman, midnight,<br/>daltonism-light,<br/>daltonism-dark"]
    end

    subgraph Validation["Validation Skills"]
        Normalize["/normalize<br/>EN/FR concordance"]
        IntCheck["/integrity-check<br/>Structure validation"]
    end

    subgraph Social["Social & Export"]
        OG["assets/og/<br/>Animated GIFs<br/>4 per publication"]
        PDF["CSS @page<br/>PDF export"]
        DOCX["MSO elements<br/>DOCX export"]
    end

    Method -->|"/docs-create"| EN_Sum
    Method -->|"/docs-create"| EN_Full
    EN_Sum -->|"identical body<br/>JS translateStatic()"| FR_Sum
    EN_Full -->|"identical body<br/>JS translateStatic()"| FR_Full
    EN_Sum -->|"link to full"| EN_Full
    FR_Sum -->|"link to full"| FR_Full

    EN_Web -->|"rendered by"| ViewerHTML
    FR_Web -->|"rendered by"| ViewerHTML
    ViewerHTML --> Mermaid
    ViewerHTML --> Themes

    Normalize -->|"validates"| EN_Web
    Normalize -->|"validates"| FR_Web
    IntCheck -->|"validates"| EN_Web

    EN_Sum --- OG
    ViewerHTML --> PDF
    ViewerHTML --> DOCX
```


**Legend**: Publications follow K_DOCS methodology. EN and FR pages share identical `{::nomarkdown}` bodies — language is a runtime parameter via JS `translateStatic()` (convention conv-020: never duplicate templates). The static viewer renders markdown + mermaid client-side with 4 theme variants. Export to PDF uses CSS @page media; DOCX uses MSO elements. Validation skills ensure EN/FR concordance and structural integrity.

---

## 7. Security Boundaries

The proxy model governing what Claude Code sessions can and cannot do. The container proxy mediates all git operations while Python urllib bypasses it for API access.

```mermaid
flowchart TB
    subgraph Container["Claude Code Container"]
        Session["Claude Session<br/>claude/task-id-xxx"]
        GHHelper["K_MIND/scripts/<br/>gh_helper.py<br/>(Python urllib)"]
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


**Legend**: The container proxy is the primary security boundary. Git operations are restricted to the assigned task branch. `gh_helper.py` (located in K_MIND/scripts/) bypasses the proxy via Python `urllib`, enabling full GitHub API access with a valid token. `curl` is intercepted and auth headers stripped. The two-channel model: git proxy (restricted) + urllib (unrestricted with token). Token is never exposed in commands or URLs — gh_helper.py manages token retrieval internally.

---

## 8. Web Architecture

The static web viewer architecture: .nojekyll GitHub Pages, client-side rendering, 4-theme system, 5 interactive interfaces, and the BroadcastChannel theme sync.

```mermaid
graph TB
    subgraph GitHubPages["GitHub Pages — .nojekyll"]
        direction TB
        NoJekyll[".nojekyll<br/>No build step<br/>Raw file serving"]
    end

    subgraph Viewer["Static JS Viewer (index.html)"]
        direction TB
        Parser["Markdown parser<br/>+ Liquid resolver"]
        MermaidCDN["Mermaid CDN<br/>Diagram rendering"]
        ThemeEngine["Theme engine<br/>CSS custom properties"]
        LinkInterceptor["Link interceptor<br/>viewer URL rewriting"]
        DocHeader["Doc header<br/>nav-back, link, version,<br/>collapsible metadata"]
        TOC["TOC generator<br/>Two-column 8+ items"]
        Export["Export engine<br/>PDF (@page) + DOCX (MSO)"]
    end

    subgraph Themes["4-Theme System"]
        T1["☀️ Cayman<br/>Blue accent, light bg"]
        T2["🌙 Midnight<br/>Soft blue, dark bg"]
        T3["♿ Daltonism Light<br/>Color-blind safe, light"]
        T4["♿ Daltonism Dark<br/>Color-blind safe, dark"]
    end

    subgraph Interfaces["5 Interactive Interfaces"]
        I1["I1: Main Navigator<br/>3-panel layout<br/>draggable dividers"]
        I2["I2: Session Review<br/>Timeline, metrics,<br/>task breakdown"]
        I3["I3: Task Workflow<br/>8-stage progress<br/>related issues"]
        I4["I4: Project Viewer<br/>Board display<br/>issue tracking"]
        I5["I5: Live Mindmap<br/>MindElixir v5.9.3<br/>4 themes synced"]
    end

    subgraph DataLayer["Compiled Data (docs/data/)"]
        DJ1["projects.json"]
        DJ2["sessions.json"]
        DJ3["tasks.json"]
        DJ4["board-N.json"]
    end

    NoJekyll --> Viewer
    Viewer --> Themes
    ThemeEngine -->|"BroadcastChannel<br/>kdocs-theme-sync"| Interfaces
    I1 -->|"iframe src"| I2
    I1 -->|"iframe src"| I3
    I1 -->|"iframe src"| I4
    I1 -->|"iframe src"| I5
    DataLayer -->|"fetch()"| Interfaces

    subgraph Social["Social Preview"]
        WebcardGIF["Animated GIF webcards<br/>1200×630, 4 themes<br/>MindElixir capture pipeline"]
        OGTags["og:image meta injection<br/>per-document"]
    end

    Viewer --> OGTags
    WebcardGIF --> OGTags
```


**Legend**: The web presence uses .nojekyll GitHub Pages — no server-side build. The static JS viewer (2065 lines) handles markdown parsing, mermaid rendering, link rewriting, theme switching, and export. The 4-theme system uses CSS custom properties injected via a theme engine. Interfaces run as iframes within the main navigator, receiving theme broadcasts via BroadcastChannel. Compiled JSON data from K_VALIDATION and K_PROJECTS feeds the interfaces. MindElixir v5.9.3 powers the live mindmap with the same 4 themes.

---

## 9. Quality Dependency Graph

The 13 core qualities and how they depend on each other. Autosuffisant is the foundation — if the system depends on external services, nothing else works.

```mermaid
graph TB
    Auto["1. Autosuffisant<br/>(Self-sufficient)<br/>Plain text + Git"]

    Auto --> Autonome["2. Autonome<br/>(Self-propagating)"]
    Auto --> Concordant["3. Concordant<br/>(Structural integrity)"]
    Auto --> Concis["4. Concis<br/>(Critical-subset)"]

    Autonome --> Distribue["7. Distribué<br/>(Multi-module flow)"]
    Autonome --> Persistant["8. Persistant<br/>(Session → permanent)"]

    Concordant --> Interactif["5. Interactif<br/>(5 web interfaces)"]
    Concis --> Evolutif["6. Évolutif<br/>(Self-growing)"]

    Interactif --> Recursif["9. Récursif<br/>(Self-documenting)"]
    Evolutif --> Recursif

    Distribue --> Securitaire["10. Sécuritaire<br/>(Security by architecture)"]
    Persistant --> Resilient["11. Résilient<br/>(K_MIND recovery)"]

    Securitaire --> Structure["12. Structuré<br/>(K_ module hierarchy)"]
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


**Legend**: The dependency graph flows from foundation (autosuffisant — plain text in Git) through enabling qualities to operational qualities to organizational qualities. Updated for Knowledge 2.0: Interactif now references 5 web interfaces, Distribué references multi-module flow, Résilient references K_MIND recovery, and Structuré references the K_ module hierarchy.

---

## 10. Recovery Paths

The K_MIND recovery mechanisms, ordered from lightest to heaviest. Each path addresses a different failure mode.

```mermaid
stateDiagram-v2
    [*] --> Working: Session active

    Working --> Compacted: Context compaction
    Working --> Crashed: Container restart / API error
    Working --> StaleContext: Long gap between turns
    Working --> NewSession: Fresh start needed

    Compacted --> MindContext: /mind-context
    MindContext --> ReadMindmap: Re-read mindmap + near_memory
    ReadMindmap --> NeedDetails: Need specific details?
    NeedDetails --> MemoryRecall: memory_recall.py --subject "topic"
    NeedDetails --> Working: No — resume with mindmap context
    MemoryRecall --> Working: Archived topic loaded

    Crashed --> CheckFar: Check far_memory.json
    CheckFar --> HasMessages: Messages preserved?
    HasMessages --> SessionInit: session_init.py --preserve-active
    CheckFar --> NoMessages: Messages lost
    NoMessages --> FreshInit: session_init.py (fresh)
    SessionInit --> MindContext
    FreshInit --> MindContext

    StaleContext --> NearCheck: Read near_memory summaries
    NearCheck --> Working: Context restored from summaries

    NewSession --> FreshInit
```


**Legend**: K_MIND provides 4 recovery paths. **Compaction** (most common): `/mind-context` reloads the mindmap and near memory — sufficient for most cases. **Deep recall**: `memory_recall.py` searches archived topics when specific details are needed. **Crash recovery**: `session_init.py --preserve-active` preserves existing messages. **Fresh start**: new session inherits last_session summaries for continuity.

**Recovery summary**:

| Recovery | Trigger | Speed | What it restores |
|----------|---------|-------|------------------|
| `/mind-context` | Context compaction | ~5s | Mindmap directives + recent summaries |
| `memory_recall.py` | Need archived details | ~10s | Specific topic from archives |
| `session_init --preserve-active` | Crash with messages | ~10s | Full session continuity |
| `session_init` (fresh) | New session | ~15s | Clean start + last_session context |
| Near memory check | Stale context | ~3s | Recent activity summaries |

---

## 11. GitHub Integration

The K_GITHUB module manages GitHub entity synchronization. `gh_helper.py` (in K_MIND/scripts/) is the shared API wrapper used across modules.

```mermaid
sequenceDiagram
    participant User as 👤 Developer
    participant Claude as 🤖 Claude Code
    participant GH as 🐙 GitHub API
    participant Board as 📋 Project Board
    participant Viewer as 📄 Static Viewer

    Note over User,Viewer: Task Lifecycle (K_VALIDATION)
    User->>Claude: /task-received (skill)
    Claude->>Claude: 9-step initial assessment
    Claude->>GH: Comment via gh_helper.py
    Claude->>Board: Update status field
    Claude->>Claude: Work (memory_append every turn)
    Claude->>GH: git push main
    GH->>Viewer: Auto-deploy (.nojekyll)

    Note over User,Viewer: Data Compilation
    Claude->>Claude: compile_tasks.py → tasks.json
    Claude->>Claude: compile_sessions.py → sessions.json
    Claude->>Claude: compile_projects.py → projects.json
    Claude->>GH: Push compiled data
    GH->>Viewer: Deploy → interfaces consume JSON

    Note over User,Viewer: GitHub Sync (K_GITHUB)
    Claude->>GH: sync_github.py (fetch issues/PRs)
    Claude->>Claude: enrich_from_github.py (add fields)
    Claude->>Claude: Store in docs/data/board-N.json
    Claude->>GH: Push synced data
    GH->>Viewer: Interfaces display board data

    Note over User,Viewer: Project Creation (K_PROJECTS)
    User->>Claude: /project-create "Name"
    Claude->>GH: createProjectV2 (GraphQL)
    Claude->>GH: linkProjectV2ToRepository
    Claude->>Claude: Register P# in projects.json
    Claude->>GH: Push + deploy
```


**Legend**: Three key workflows. **Task lifecycle**: skill-driven assessment → work with real-time memory → push to main → auto-deploy. **Data compilation**: K_VALIDATION and K_PROJECTS scripts compile JSON consumed by web interfaces. **GitHub sync**: K_GITHUB scripts fetch external state into local data files. All API calls go through `gh_helper.py` (Python urllib, bypasses container proxy).

---

## 12. System Architecture Mindmap

High-level navigation map of the Knowledge 2.0 system with its architectural pillars.

```mermaid
mindmap
  root((Knowledge 2.0))
    Multi-Module Core
      K_MIND mandatory
      K_DOCS documentation
      K_GITHUB integration
      K_PROJECTS management
      K_VALIDATION QA
      modules.json registry
    Mind-First Memory
      mind_memory.md grid
      264 nodes 7 groups
      Domain JSONs per module
      Near + far memory
      16 topic archives
      Deterministic scripts
    Session System
      session_init.py
      memory_append every turn
      far_memory_split by topic
      Compaction recovery
      memory_recall archives
    Web Presence
      Static JS viewer
      .nojekyll Pages
      4 themes system
      25+ publications
      EN/FR bilingual
      Animated webcards
    5 Interfaces
      Main navigator
      Session review
      Task workflow
      Project viewer
      Live mindmap MindElixir
    Skills System
      /mind-context
      /docs-create
      /github
      /project-create
      /task-received
      /work-cycle
    Security
      Container proxy
      gh_helper.py bypass
      Token management
      Fork-safe
    Quality Framework
      13 qualities
      Autosuffisant foundation
      Self-documenting
      30 years distilled
```


**The architectural pillars**:

| # | Pillar | Essence | Key elements |
|---|--------|---------|--------------|
| 1 | **Multi-module core** | The K_ organization | 5 modules + registry, each with own conventions/work/scripts |
| 2 | **Mind-first memory** | The operating memory | Mindmap → domain JSONs → near/far → archives |
| 3 | **Session system** | The work rhythm | init → append → split → recover |
| 4 | **Web presence** | The public face | Static viewer, .nojekyll, 4 themes, 25+ pubs |
| 5 | **5 interfaces** | The interactive layer | Navigator, session, task, project, mindmap |
| 6 | **Skills system** | The command surface | Module-specific skills invoked by Claude |
| 7 | **Security** | Trust by design | Proxy model, token management, fork-safe |
| 8 | **Quality framework** | The quality contract | 13 qualities, dependency graph, 30 years distilled |

---

## 13. Module Structure Mindmap

The Knowledge 2.0 file-level structure — every module and its components.

```mermaid
mindmap
  root((Knowledge 2.0<br/>Repository))
    Knowledge/K_MIND
      mind/mind_memory.md
      sessions/near+far+archives
      conventions/depth_config
      architecture.json
      constraints.json
      work.json
      scripts 10 programs
    Knowledge/K_DOCS
      scripts 7 programs
      methodology 7 files
      conventions sessions+web
      work.json
    Knowledge/K_GITHUB
      scripts 3 sync programs
      methodology
      conventions.json
    Knowledge/K_PROJECTS
      data/projects.json
      scripts 2 compilers
      skills 2
      methodology 2 files
    Knowledge/K_VALIDATION
      scripts 5 compilers
      skills 5
      methodology 4 files
    docs Web Output
      index.html viewer
      interfaces 5 panels
      publications 25+
      data compiled JSON
      assets/og webcards
      fr/ bilingual mirror
    .claude
      skills 5 root
      settings.json
      launch.json
    CLAUDE.md
      K_MIND instructions
      Mind-first principle
```


**Module roles**:

| Module | Files | Primary Role |
|--------|-------|-------------|
| **K_MIND** | 38 | Core memory: mindmap, sessions, domain JSONs, 10 scripts |
| **K_DOCS** | 4,374 | Documentation pipeline: web viewer, publications, interfaces |
| **K_PROJECTS** | 13 | Project management: P# registry, compilation, skills |
| **K_VALIDATION** | 19 | QA: task workflow, session protocol, integrity checks |
| **K_GITHUB** | 9 | GitHub sync: issues, PRs, boards, enrichment |
| **docs/** | 100+ | Web output: static viewer, 25+ pubs, 5 interfaces |

---

## 14. Publication Structure Mindmap

The anatomy of a single Knowledge 2.0 publication — components, tiers, assets, and integration.

```mermaid
mindmap
  root((Publication))
    Web Pages EN
      Summary index.md
      Complete full/index.md
    Web Pages FR
      Résumé index.md
      Complet full/index.md
    Front Matter
      8 required fields
      Static viewer metadata
    Webcards OG
      2 languages
      4 themes
      Animated GIFs 1200x630
    Static Viewer Rendering
      Client-side markdown
      Mermaid CDN diagrams
      4 theme variants
      PDF + DOCX export
    Bilingual Convention
      Identical body conv-020
      JS translateStatic
      Runtime language detection
    System Integration
      Publication indexes
      Profile pages
      docs/data/ compiled
      Webcard pipeline
    Identifiers
      Pub number
      Slug
      2 tiers summary+full
      EN/FR mirrors
    Validation
      /normalize concordance
      /integrity-check structure
      /docs-create lifecycle
```


**Publication lifecycle**:

```
/docs-create → EN/FR pages scaffolded → Webcards generated
    → Content written (identical EN/FR body)
    → /normalize → EN/FR concordance verified
    → /integrity-check → Structure validated
    → Push → .nojekyll deploy → Live on GitHub Pages
```

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
