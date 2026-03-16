---
layout: publication
title: "Diagrammes d'architecture de Knowledge 2.0"
description: "Diagrammes visuels de l'architecture du système multi-module Knowledge 2.0 : vue d'ensemble, architecture mémoire mind-first, cycle de vie des sessions, flux d'interaction des modules. Companion de la Publication #14."
pub_id: "Publication #15"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/architecture-diagrams/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "architecture, diagrammes, mermaid, knowledge 2.0, multi-module, mind-first"
---

# Diagrammes d'architecture de Knowledge 2.0
{: #pub-title}

> **Publication parente** : [#0 — Système de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Analyse companion** : [#14 — Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Résumé](#resume) | Companion visuel de l'architecture Knowledge 2.0 |
| [Vue d'ensemble](#1-vue-densemble--contexte-c4) | Contexte C4 — Système multi-module au centre |
| [Mémoire Mind-First](#2-architecture-memoire-mind-first) | Mémoire à 4 niveaux : Mindmap → JSONs → Near → Far |
| [Cycle de vie de session](#4-cycle-de-vie-de-session) | session_init → /mind-context → memory_append → archive |
| [Interaction des modules](#5-flux-dinteraction-des-modules) | K_MIND hub central, pipelines de compilation, invocations de skills |
| [Documentation complète](#documentation-complete) | Les 14 diagrammes avec explications complètes |

## Audience ciblée

| Audience | Quoi privilégier |
|----------|-----------------|
| **Administrateurs réseau** | Interaction modules (#5), limites de sécurité (#7), architecture web (#8) |
| **Administrateurs système** | Architecture web (#8), intégration GitHub (#11), pipeline de publication (#6) |
| **Programmeurs et programmeuses** | Architecture multi-module (#3), cycle de vie de session (#4), chemins de récupération (#10) |
| **Gestionnaires** | Vue d'ensemble (#1), mémoire mind-first (#2), dépendances des qualités (#9) |

## Résumé

La publication #14 (Analyse d'architecture) examine le système à travers un récit analytique. Cette publication est le **companion visuel** — 14 diagrammes Mermaid qui rendent la structure, les flux, les limites et les dépendances du système multi-module Knowledge 2.0 en visualisations interactives.

Ce résumé présente les 4 diagrammes clés. La [documentation complète]({{ '/fr/publications/architecture-diagrams/full/' | relative_url }}) inclut les 14 diagrammes couvrant les limites de sécurité, l'architecture web, les dépendances des qualités, les chemins de récupération et l'intégration GitHub.

## 1. Vue d'ensemble — Contexte C4

Le système Knowledge 2.0 au centre de sa constellation : 5 modules K_, plateforme GitHub, GitHub Pages (.nojekyll hébergement statique), sessions Claude Code et le développeur.

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


Le système est organisé en 5 modules K_ sous `Knowledge/`. K_MIND est le core obligatoire. Les autres modules fournissent des capacités spécialisées. GitHub Pages sert le viewer web statique avec rendu côté client.

## 2. Architecture mémoire Mind-First

Quatre niveaux de stabilité décroissante et de granularité croissante — de la grille de directives (mindmap) à l'archive verbatim complète.

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


Les connaissances remontent par le pipeline de staging et descendent comme directives opérationnelles. Toutes les opérations mécaniques utilisent des scripts Python déterministes.

## 4. Cycle de vie de session

Chaque session Claude Code suit un cycle de vie déterministe géré par les scripts K_MIND.

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


Trois phases : démarrage (/mind-context), travail (memory_append à chaque tour) et récupération (gestion de compaction). La mindmap est toujours chargée en premier car elle contient toutes les directives comportementales.

## 5. Flux d'interaction des modules

Comment les 5 modules K_ interagissent : K_MIND comme hub central, pipelines de compilation alimentant le viewer web.

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


K_MIND est le hub — sa mindmap fournit des directives à tous les modules, et gh_helper.py est le wrapper API GitHub partagé. Les scripts de compilation produisent des données JSON consommées par les 5 interfaces web.

## Documentation complète

La [documentation complète]({{ '/fr/publications/architecture-diagrams/full/' | relative_url }}) inclut les 14 diagrammes :

| # | Diagramme | Ce qu'il montre |
|---|-----------|-----------------|
| 1 | Vue d'ensemble | Contexte C4 — Système multi-module au centre |
| 2 | Mémoire Mind-First | Architecture mémoire à 4 niveaux avec scripts |
| 3 | Architecture multi-module | 5 modules K_, scripts, relations |
| 4 | Cycle de vie de session | session_init → travail → archive flowchart |
| 5 | Interaction des modules | K_MIND hub, pipelines de compilation |
| 6 | Pipeline de publication | Source → viewer statique → EN/FR × 4 thèmes |
| 7 | Limites de sécurité | Modèle proxy, opérations autorisées/bloquées |
| 8 | Architecture web | Viewer statique, 4 thèmes, 5 interfaces |
| 9 | Dépendances des qualités | Graphe de dépendance des 13 qualités |
| 10 | Chemins de récupération | Récupération K_MIND : compaction, rappel, init |
| 11 | Intégration GitHub | Sync K_GITHUB, compilation, cycle boards |
| 12 | Carte mentale architecture | Piliers architecturaux K2.0 |
| 13 | Carte mentale structure modules | Structure multi-module au niveau fichier |
| 14 | Carte mentale structure publication | Anatomie publication avec viewer statique |

---

## Publications liées

| # | Publication | Relation |
|---|-------------|---------|
| 0 | [Système de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — le système que ces diagrammes visualisent |
| 4 | [Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) | Architecture — flux multi-module (Diagramme 5) |
| 7 | [Protocole Harvest]({{ '/fr/publications/harvest-protocol/' | relative_url }}) | Protocole — flux de données (Diagrammes 5, 11) |
| 8 | [Gestion de session]({{ '/fr/publications/session-management/' | relative_url }}) | Cycle de vie — système de session K_MIND (Diagramme 4) |
| 9 | [Sécurité par conception]({{ '/fr/publications/security-by-design/' | relative_url }}) | Sécurité — limites proxy (Diagramme 7) |
| 12 | [Gestion de projet]({{ '/fr/publications/project-management/' | relative_url }}) | Projets — module K_PROJECTS (Diagrammes 1, 8) |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge 2.0 : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
