---
layout: publication
title: "Diagrammes d'architecture de Knowledge"
description: "Diagrammes visuels de l'architecture du systeme Knowledge (P0) : vue d'ensemble, couches de connaissances, architecture des composants, cycle de vie des sessions, flux distribue, pipeline de publication, limites de securite et niveaux de deploiement. Companion de la Publication #14."
pub_id: "Publication #15"
version: "v1"
date: "2026-02-26"
permalink: /fr/publications/architecture-diagrams/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "architecture, diagrammes, mermaid, connaissances, distribue, securite"
---

# Diagrammes d'architecture de Knowledge
{: #pub-title}

> **Publication parente** : [#0 — Systeme de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Analyse companion** : [#14 — Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }})

**Table des matieres**

| | |
|---|---|
| [Resume](#resume) | Companion visuel de l'analyse d'architecture |
| [Vue d'ensemble](#1-vue-densemble--contexte-c4) | Diagramme de contexte C4 — Knowledge au centre |
| [Couches de connaissances](#2-couches-de-connaissances) | Pile a 4 couches : Core → Prouve → Recolte → Session |
| [Cycle de vie de session](#4-cycle-de-vie-de-session) | Wakeup → travail → checkpoint → save → PR → merge |
| [Flux distribue](#5-flux-distribue--push-et-pull) | Push (wakeup) et pull (harvest) avec pipeline de promotion |
| [Documentation complete](#documentation-complete) | Les 14 diagrammes avec explications completes |

## Audience ciblee

| Audience | Quoi privilegier |
|----------|-----------------|
| **Administrateurs reseau** | Flux distribue (#5), limites de securite (#7), niveaux de deploiement (#8) |
| **Administrateurs systeme** | Niveaux de deploiement (#8), integration GitHub (#11), pipeline de publication (#6) |
| **Programmeurs et programmeuses** | Architecture des composants (#3), cycle de vie de session (#4), echelle de recuperation (#10) |
| **Gestionnaires** | Vue d'ensemble (#1), couches de connaissances (#2), dependances des qualites (#9) |

## Resume

La publication #14 (Analyse d'architecture) examine le systeme a travers un recit analytique. Cette publication est le **companion visuel** — 14 diagrammes Mermaid qui rendent la structure, les flux, les limites et les dependances du systeme Knowledge en visualisations interactives.

Ce resume presente les 4 diagrammes cles. La [documentation complete]({{ '/fr/publications/architecture-diagrams/full/' | relative_url }}) inclut les 14 diagrammes couvrant les limites de securite, les niveaux de deploiement, les dependances des qualites, les chemins de recuperation et l'integration GitHub.

Closes #317

## 1. Vue d'ensemble — Contexte C4

Le systeme Knowledge (P0) au centre de sa constellation : projets satellites, plateforme GitHub, GitHub Pages, sessions Claude Code et le developpeur.

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


Le depot core contient toute la methodologie, les publications et l'outillage. Les satellites heritent au `wakeup` (push) et contribuent via `harvest` (pull). GitHub Pages publie la presence web.

## 2. Couches de connaissances

Quatre couches de stabilite decroissante et de pertinence croissante — de l'ADN (core) au battement de coeur (session).

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


Les connaissances remontent par le pipeline de promotion et descendent par le protocole wakeup.

## 4. Cycle de vie de session

Chaque session Claude Code suit un chemin deterministe de l'auto-wakeup au save.

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


Trois phases : demarrage (wakeup), travail et livraison (save). Recuperation de crash via checkpoints. Perte de contexte via `refresh`.

## 5. Flux distribue — Push et Pull

Flux bidirectionnel de connaissances avec le pipeline de promotion.

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


Le push livre la methodologie vers l'exterieur au wakeup. Le harvest tire les decouvertes vers l'interieur. Le pipeline de promotion fait avancer les decouvertes du brut vers le core.

## Documentation complete

La [documentation complete]({{ '/fr/publications/architecture-diagrams/full/' | relative_url }}) inclut les 14 diagrammes :

| # | Diagramme | Ce qu'il montre |
|---|-----------|-----------------|
| 1 | Vue d'ensemble | Contexte C4 — Knowledge au centre |
| 2 | Couches de connaissances | Pile a 4 couches avec flux de promotion |
| 3 | Architecture des composants | Tous les dossiers, scripts, relations |
| 4 | Cycle de vie de session | Flowchart wakeup → travail → save |
| 5 | Flux distribue | Push/pull avec pipeline de promotion |
| 6 | Pipeline de publication | Source → EN/FR resume/complet |
| 7 | Limites de securite | Modele proxy, operations autorisees/bloquees |
| 8 | Niveaux de deploiement | Double role production/developpement |
| 9 | Dependances des qualites | Graphe de dependance des 13 qualites |
| 10 | Echelle de recuperation | 5 chemins de recuperation par type de panne |
| 11 | Integration GitHub | Cycle de vie Issues, PRs, boards |
| 12 | Carte mentale architecture systeme | Carte de navigation 9 piliers |
| 13 | Carte mentale noyau core | Structure au niveau fichier avec analyse de poids |
| 14 | Carte mentale structure Publication | Anatomie a 9 branches d'une publication |

**Source** : [Issue #317](https://github.com/packetqc/knowledge/issues/317), [Issue #318](https://github.com/packetqc/knowledge/issues/318) — Sessions d'exploration architecturale.

---

## Publications liees

| # | Publication | Relation |
|---|-------------|---------|
| 0 | [Systeme de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — le systeme que ces diagrammes visualisent |
| 4 | [Connaissances distribuees]({{ '/fr/publications/distributed-minds/' | relative_url }}) | Architecture — flux push/pull (Diagramme 5) |
| 7 | [Protocole Harvest]({{ '/fr/publications/harvest-protocol/' | relative_url }}) | Protocole — flux harvest (Diagrammes 5, 11) |
| 8 | [Gestion de session]({{ '/fr/publications/session-management/' | relative_url }}) | Cycle de vie — flux session (Diagramme 4) |
| 9 | [Securite par conception]({{ '/fr/publications/security-by-design/' | relative_url }}) | Securite — limites proxy (Diagramme 7) |
| 12 | [Gestion de projet]({{ '/fr/publications/project-management/' | relative_url }}) | Projets — hierarchie P# (Diagrammes 1, 8) |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
