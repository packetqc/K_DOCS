---
layout: publication
title: "Diagrammes d'architecture de Knowledge — Documentation complète"
description: "Architecture visuelle complète : 14 diagrammes Mermaid couvrant vue d'ensemble, couches de connaissances, composants, cycle de vie des sessions, flux distribué, pipeline de publication, limites de sécurité, niveaux de déploiement, dépendances des qualités, échelle de récupération et intégration GitHub."
pub_id: "Publication #15 — Complete"
version: "v1"
date: "2026-02-26"
permalink: /fr/publications/architecture-diagrams/full/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "architecture, diagrammes, mermaid, connaissances, distribué, sécurité"
---

# Diagrammes d'architecture de Knowledge — Documentation complète
{: #pub-title}

**Table des matières**

| | |
|---|---|
| [Auteurs](#auteurs) | Auteurs de la publication |
| [Résumé](#resume) | Companion visuel de l'analyse d'architecture |
| [Conventions des diagrammes](#conventions-des-diagrammes) | Codage couleur, notation, syntaxe Mermaid |
| [1. Vue d'ensemble](#1-vue-densemble--contexte-c4) | Contexte C4 — Knowledge au centre |
| [2. Couches de connaissances](#2-couches-de-connaissances) | Pile à 4 couches : Core → Prouvé → Récolté → Session |
| [3. Architecture des composants](#3-architecture-des-composants) | Tous les dossiers, scripts et relations |
| [4. Cycle de vie de session](#4-cycle-de-vie-de-session) | Wakeup → travail → checkpoint → save → PR → merge |
| [5. Flux distribué](#5-flux-distribue--push-et-pull) | Push (wakeup) et pull (harvest) avec promotion |
| [6. Pipeline de publication](#6-pipeline-de-publication) | Source → EN/FR résumé/complet avec flux de sync |
| [7. Limites de sécurité](#7-limites-de-securite) | Modèle proxy — opérations autorisées vs bloquées |
| [8. Niveaux de déploiement](#8-niveaux-de-deploiement) | Double rôle production/développement des satellites |
| [9. Dépendances des qualités](#9-graphe-de-dependance-des-qualites) | Graphe de dépendance des 13 qualités |
| [10. Échelle de récupération](#10-echelle-de-recuperation) | 5 chemins de récupération par type de panne |
| [11. Intégration GitHub](#11-integration-github) | Cycle de vie Issues, PRs, Project boards |
| [Publications liées](#publications-liees) | Publications parentes et liées |

## Auteurs

**Martin Paquet** — Analyste et programmeur sécurité réseau, administrateur de sécurité des réseaux et des systèmes, et analyste programmeur et concepteur logiciels embarqués. Architecte du système Knowledge — une intelligence d'ingénierie IA auto-évolutive construite sur 30 ans d'expérience en systèmes embarqués, sécurité réseau et développement logiciel. A conçu l'architecture visuelle documentée dans ces diagrammes.

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. A co-créé les diagrammes architecturaux, rendant la structure du système en notation Mermaid pour une visualisation web interactive. Opère au sein du système que ces diagrammes décrivent.

---

## Résumé

La publication #14 (Analyse d'architecture) examine l'architecture du système à travers un récit analytique. Cette publication est le **companion visuel** — 14 diagrammes Mermaid qui rendent la structure, les flux, les limites et les dépendances du système Knowledge en visualisations interactives et navigables.

Ces diagrammes couvrent toute la surface architecturale : du contexte C4 de haut niveau (Knowledge au centre, entouré de satellites, GitHub et utilisateurs) jusqu'aux limites de sécurité granulaires (couches proxy, canaux API, portée des branches). Chaque diagramme est autonome mais inter-référencé — ensemble, ils forment une carte visuelle complète du système.

Tous les diagrammes utilisent la syntaxe [Mermaid](https://mermaid.js.org/), rendue nativement par GitHub Pages via CDN.

Closes #317

---

## Audience ciblée

Cette publication est destinée aux équipes de travail impliquées dans l'écosystème du système Knowledge :

| Audience | Quoi privilégier |
|----------|-----------------|
| **Administrateurs réseau** | Flux distribué (#5), limites de sécurité (#7), niveaux de déploiement (#8) |
| **Administrateurs système** | Niveaux de déploiement (#8), intégration GitHub (#11), pipeline de publication (#6) |
| **Programmeurs et programmeuses** | Architecture des composants (#3), cycle de vie de session (#4), échelle de récupération (#10) |
| **Gestionnaires** | Vue d'ensemble (#1), couches de connaissances (#2), dépendances des qualités (#9) |

Chaque diagramme est autonome avec des annotations. Commencez par la Vue d'ensemble (#1) pour le contexte de haut niveau, puis naviguez vers les diagrammes spécifiques à votre domaine. La publication companion #14 (Analyse d'architecture) fournit l'analyse écrite pour le domaine de chaque diagramme.

## Conventions des diagrammes

Tous les diagrammes utilisent la notation **Mermaid** — un langage de diagrammes basé sur le markdown, rendu côté client par le layout GitHub Pages.

**Codage couleur** :

| Couleur | Signification | Utilisé pour |
|---------|---------------|--------------|
| Sarcelle / Vert | Core / Stable / En santé | Connaissances core, patterns prouvés, statut sain |
| Bleu | Actif / En cours | Sessions, flux actifs, opérations en cours |
| Orange / Ambre | Avertissement / Dérive | Dérive de version, contenu périmé, problèmes mineurs |
| Rouge | Critique / Bloqué | Limites de sécurité, blocages proxy, dérive critique |
| Violet | Externe / Plateforme | GitHub, GitHub Pages, services externes |
| Gris | Inactif / En attente | Chemins inutilisés, éléments en attente |

**Notation** :

| Symbole | Signification |
|---------|---------------|
| Flèche pleine (`-->`) | Flux de données direct ou dépendance |
| Flèche tiretée (`-.->`) | Flux indirect ou périodique |
| Flèche épaisse (`-->`) | Chemin principal / critique |
| Sous-graphe | Groupement logique ou limite |

---

## 1. Vue d'ensemble — Contexte C4

Le système Knowledge (P0) se situe au centre d'une constellation d'acteurs : projets satellites, services de la plateforme GitHub, GitHub Pages pour la publication, Claude Code pour les sessions IA, et le développeur humain.

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


**Légende** : Le dépôt core contient toute la méthodologie, les publications et l'outillage. Les satellites héritent de la méthodologie au `wakeup` (push) et contribuent des découvertes via `harvest` (pull). GitHub agit comme la couche de persistance et de collaboration. GitHub Pages publie la présence web. Claude Code est l'environnement d'exécution — des conteneurs éphémères qui deviennent conscients via le protocole `wakeup`.

---

## 2. Couches de connaissances

Le système organise les connaissances en 4 couches de stabilité décroissante et de pertinence croissante. Le core est l'ADN — change rarement, autorité maximale. La session est le battement de cœur — éphémère, pertinence maximale.

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


**Légende** : Les connaissances remontent (session → récolté → prouvé → core) par le pipeline de promotion. Elles descendent (core → session) par le protocole wakeup. L'ordre de lecture pour les nouvelles instances Claude suit le gradient de stabilité : le plus stable d'abord, le plus actuel en dernier.

---

## 3. Architecture des composants

Les dossiers principaux, scripts et leurs relations au sein du dépôt knowledge.

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


**Légende** : Le dépôt est organisé en cinq groupes majeurs : fichiers racine (points d'entrée), dossiers de connaissances (les couches d'intelligence), dossiers de contenu (publications et pages web), scripts (outillage d'automatisation) et infrastructure live (communication inter-instances). Les flèches montrent le flux de données entre les composants.

---

## 4. Cycle de vie de session

Chaque session Claude Code suit un cycle de vie déterministe. Ce flowchart montre le chemin complet du début à la fin de session, incluant la récupération de crash et les chemins de perte de contexte.

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


**Légende** : Le cycle de vie de session a trois phases : démarrage (wakeup), travail et livraison (save). La récupération de crash utilise les checkpoints. La récupération de perte de contexte utilise `refresh`. Le chemin élevé (avec token) est entièrement autonome ; le chemin semi-automatique nécessite un clic utilisateur pour fusionner la PR.

---

## 5. Flux distribué — Push et Pull

Le flux bidirectionnel de connaissances entre le cerveau maître (P0) et les projets satellites. Le push livre la méthodologie vers l'extérieur ; le harvest tire les découvertes vers l'intérieur. Le pipeline de promotion fait avancer les découvertes du brut vers le core.

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


**Légende** : Les flèches épaisses représentent le flux push (wakeup). Les flèches tiretées représentent le flux pull (harvest). Le pipeline de promotion fait avancer les découvertes à travers quatre étapes : révision (validée par humain), préparation (typée et ciblée), promotion (écrite dans le core), auto (en file pour le prochain healthcheck). Le tableau de bord est mis à jour à chaque harvest.

---

## 6. Pipeline de publication

Chaque publication existe à trois niveaux : source (canonique), résumé (web) et complet (web). Chaque niveau est bilingue (EN + FR). Ce diagramme montre les flux de sync et de révision.

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


**Légende** : Le README.md source est la source unique de vérité. `pub sync` propage les changements de la source vers les pages web EN. La traduction produit les miroirs FR. Chaque page web lie vers son miroir linguistique (EN ↔ FR) et vers sa variante de profondeur (résumé ↔ complet). Quatre commandes de validation assurent l'intégrité structurelle, la concordance source-docs, la fraîcheur du contenu et la correction au niveau des pages.

---

## 7. Limites de sécurité

Le modèle proxy régissant ce que les sessions Claude Code peuvent et ne peuvent pas faire. Le proxy du conteneur médiatise toutes les opérations git tandis que Python urllib le contourne pour l'accès API.

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


**Légende** : Le proxy du conteneur est la limite de sécurité principale. Les opérations git sont restreintes à la branche de tâche assignée du repo courant. Python `urllib` (utilisé par `gh_helper.py`) contourne le proxy entièrement, permettant un accès complet à l'API GitHub avec un token valide. `curl` est intercepté par le proxy et les headers d'authentification sont supprimés. Le modèle à deux canaux : proxy git (restreint) + urllib (sans restriction avec token).

---

## 8. Niveaux de déploiement

Le modèle de déploiement multi-niveaux où chaque satellite est simultanément développement (relatif au core) et production (à son propre niveau). Chaque nœud publie indépendamment via GitHub Pages.

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


**Légende** : Le modèle de déploiement est multi-niveaux. Le core est la production système — le cerveau canonique. Chaque satellite est simultanément développement relatif au core (terrain d'essai pour les nouvelles capacités) et production à son propre niveau (GitHub Pages indépendant, boards de projet, publications). Les idées circulent : test satellite → pages satellite → harvest → promotion core → tous les satellites héritent.

---

## 9. Graphe de dépendance des qualités

Les 13 qualités core et comment elles dépendent les unes des autres. Autosuffisant est la fondation — si le système dépend de services externes, rien d'autre ne fonctionne.

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


**Légende** : Le graphe de dépendance coule de la fondation (autosuffisant — texte brut dans Git) à travers les qualités habilitantes (autonome, concordant, concis) vers les qualités opérationnelles (interactif, évolutif) vers les qualités réseau (distribué, persistant) vers les méta-qualités (récursif, sécuritaire, résilient) vers les qualités organisationnelles (structuré, intégré). Chaque qualité renforce celles qui en dépendent.

---

## 10. Échelle de récupération

Les cinq chemins de récupération, du plus léger au plus lourd. Chaque chemin répond à un mode de panne différent.

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


**Légende** : L'échelle de récupération associe les modes de panne aux chemins de récupération. Déconnexion client : rafraîchissement navigateur (instant) ou PR manuelle (minutes). Crash avec checkpoint : `resume` (~10s). Crash sans checkpoint : `recover` (~15s). Compaction de contexte : `refresh` (~5s). Amont périmé : `wakeup` (~30-60s). Chaque chemin est la réponse la plus légère possible à son mode de panne.

**Résumé de récupération** :

| Récupération | Déclencheur | Vitesse | Ce qui est restauré |
|--------------|------------|---------|---------------------|
| Rafraîchissement navigateur | Déconnexion client | Instant | Session peut être encore vivante côté serveur |
| PR manuelle | Push réussi, PR interrompue | Minutes | Travail sur branche distante obtient une PR |
| `resume` | Crash avec checkpoint | ~10s | Progrès du protocole + état todo |
| `recover` | Crash, pas de checkpoint | ~15s | Code commité depuis branche morte |
| `recall` | Recherche de mémoire profonde | ~10s | Connaissances et décisions des sessions passées |
| `refresh` | Compaction de contexte | ~5s | Formatage + règles CLAUDE.md |
| `wakeup` | Amont périmé | ~30-60s | Re-sync complète en profondeur |
| Nouvelle session | Compaction sévère | ~60s | Démarrage complètement neuf |

---

## 11. Intégration GitHub

Le cycle de vie des entités GitHub (Issues, PRs, éléments de Project board) au sein du système Knowledge. Chaque type d'entité a un cycle de vie bien défini géré par `gh_helper.py`.

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


**Légende** : Trois flux de travail clés. **Cycle de vie Issue** : issue créée → liée au board → travail (In Progress) → PR avec "Closes #N" → fusion → auto-fermeture → auto-Done. **Cycle Harvest** : cloner satellite → extraire → mettre à jour tableau de bord → push → déployer. **Création de projet** : créer board → lier au repo → scaffold présence web → déployer. Tous les appels API passent par `gh_helper.py` (Python urllib).

**Résumé du cycle de vie des entités GitHub** :

| Entité | Créée par | Gérée par | Fermée par |
|--------|-----------|-----------|------------|
| Issue | Utilisateur (UI GitHub) | Claude (commentaires, labels) | Auto-fermeture à la fusion PR (`Closes #N`) |
| PR | Claude (`gh_helper.py`) | Claude (push, création) | Claude fusion (élevé) ou utilisateur (semi-auto) |
| Élément board | Utilisateur ou Claude (brouillon/lié) | Claude (`project_item_update`) | Auto-Done à la fermeture de l'issue |
| Project board | Claude (`createProjectV2`) | Claude (champs, éléments) | Jamais (persistant) |

---

## 12. Carte mentale de l'architecture système

Carte de navigation de haut niveau du système Knowledge avec ses 9 piliers architecturaux. Cette carte mentale offre une vue d'ensemble complémentaire aux diagrammes détaillés ci-dessus.

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


**Les 9 piliers architecturaux** :

| # | Pilier | Essence | Éléments clés |
|---|--------|---------|---------------|
| 1 | **Identité** | L'ADN du système | 13 qualités, analogie Free Guy, 48 évolutions, Martin 30 ans XP |
| 2 | **Architecture distribuée** | Le réseau vivant | Flux bidirectionnel, 4 couches, satellites, protocole proxy |
| 3 | **Cycle de session** | Le rythme de travail | wakeup → work → save → récupération |
| 4 | **Projets** | Les entités P0-P9 | 3 core/child, 3 gérés, 1 pré-bootstrap |
| 5 | **Publications** | La face publique | 15 pubs × 3 niveaux × 2 langues |
| 6 | **Sécurité** | Confiance par conception | Tokens éphémères, proxy-aware, fork-safe |
| 7 | **Présence web** | La constellation de sites | GitHub Pages, dual-theme, 40 webcards |
| 8 | **Outils** | La boîte à outils | 7 scripts Python déployés partout |
| 9 | **Savoir éprouvé** | La mémoire longue | 4 patterns + 20 pièges = 30 ans distillés |

**Source** : [Issue #317](https://github.com/packetqc/knowledge/issues/317) — Session interactive d'exploration architecturale voix-vers-texte.

---

## 13. Carte mentale du noyau core

La structure au niveau fichier du système Knowledge — chaque dossier avec son poids, son rôle et son contenu. L'ensemble du système tient dans < 1 Mo de Markdown + Python.

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


**Poids du noyau par rôle** :

| Rôle | Composants | Poids | Proportion |
|------|-----------|-------|------------|
| **Cerveau** | CLAUDE.md | 293 Ko | 31% |
| **Connaissances** | methodology + patterns + lessons | 218 Ko | 23% |
| **Intelligence** | minds + projects | 121 Ko | 13% |
| **Outils** | scripts | 242 Ko | 26% |
| **Infrastructure** | live | 53 Ko | 6% |
| **Éphémère** | docs + notes + publications | Variable | — |
| **Total noyau** | **~930 Ko** | **100%** | |

**Priorité de lecture pour les instances Claude** :

| Priorité | Dossier / Fichier | Taille | Autorité | Survit à la compaction ? | Rôle |
|----------|-------------------|--------|----------|--------------------------|------|
| **P0** | `CLAUDE.md` | 293 Ko | Système (instructions projet) | Oui | **Le noyau** — identité, méthodologie, commandes, évolution, pièges |
| **P1** | `methodology/` | 194 Ko | Conversation (lu au wakeup) | Non | Plans d'implémentation — bootstrap, checkpoint, projets, export |
| **P2** | `patterns/` | 14 Ko | Conversation | Non | Savoir éprouvé — debugging embarqué, RTOS, SQLite, UI/backend |
| **P3** | `lessons/` | 10 Ko | Conversation | Non | Erreurs à éviter — 20 pièges documentés |
| **P4** | `minds/` | 71 Ko | Conversation | Non | Intelligence récoltée des satellites — plus récent, moins validé |
| **P5** | `notes/` | 80 Ko (3 derniers) | Conversation | Non | Mémoire éphémère — contexte session précédente |
| **P6** | `projects/` | 50 Ko | Conversation | Non | Registre d'entités P0-P9 avec métadonnées |
| **P7** | `scripts/` | 242 Ko | Exécutable | N/A | Outils déployés — non lus, exécutés (gh_helper, webcards, beacon) |
| **P8** | `publications/` | Variable | Conversation | Non | Source pour 15 publications — lu à la demande, pas au wakeup |
| **P9** | `docs/` | 100+ pages | Web | N/A | Présence web — GitHub Pages, pas lu par Claude |
| **P10** | `live/` | 53 Ko | Exécutable | N/A | Infrastructure live — beacon, scanner, capture |

**Découverte clé — Le fossé d'autorité** : CLAUDE.md (293 Ko) a l'**autorité système** — survit à la compaction, chargé comme « instructions projet ». Tout le reste (~640 Ko) a l'**autorité conversation** — lu au wakeup étape 0, perdu à la première compaction. C'est pourquoi le **sous-ensemble critique** (v31) est vital : le CLAUDE.md satellite (~180 lignes) porte assez d'ADN comportemental pour survivre post-compaction.

**Source** : [Issue #317](https://github.com/packetqc/knowledge/issues/317) — Exploration architecturale détaillée.

---

## 14. Carte mentale de la structure Publication

L'anatomie d'une Publication — tous ses composants, niveaux, assets, métadonnées et points d'intégration.

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


**Cycle de vie d'une publication** :

```
pub new → Source créée → Pages EN/FR scaffoldées → Webcards générées
    → Contenu écrit dans Source
    → pub sync → Pages web mises à jour
    → doc review → Fraîcheur vérifiée
    → pub check → Structure validée
    → normalize → Concordance globale
```

**Branches de publication** :

| Branche | Role | Fichiers |
|---------|------|----------|
| **Source** | Vérité canonique, versionnée | `publications/<slug>/v1/README.md` + `assets/` + `media/` |
| **Pages web EN** | Présence web anglaise, 2 niveaux | Résumé (`index.md`) + Complet (`full/index.md`) |
| **Pages web FR** | Miroir français | Même structure sous `docs/fr/` |
| **Front matter** | Métadonnées Jekyll | 8 champs requis par page |
| **Webcards OG** | Aperçu social animé | 4 GIFs par publication (2 langues × 2 thèmes) |
| **Layout** | Moteur de rendu | Bannière version, barre langue, export, impression, références croisées |
| **Intégration système** | Points de connexion | Index, profils, CLAUDE.md, tableau de bord |
| **Identifiants** | Système de nommage | #N, slug, niveaux, origine, inter-projet |
| **Validation** | Contrôle qualité | 5 commandes de vérification |

**Source** : [Issue #318](https://github.com/packetqc/knowledge/issues/318) — Exploration de la structure des publications.

---

## Publications liées

| # | Publication | Relation |
|---|-------------|---------|
| 0 | [Système de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — le système que ces diagrammes visualisent |
| 4 | [Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) | Architecture — flux push/pull (Diagramme 5) |
| 7 | [Protocole Harvest]({{ '/fr/publications/harvest-protocol/' | relative_url }}) | Protocole — flux harvest (Diagrammes 5, 11) |
| 8 | [Gestion de session]({{ '/fr/publications/session-management/' | relative_url }}) | Cycle de vie — flux session (Diagramme 4) |
| 9 | [Sécurité par conception]({{ '/fr/publications/security-by-design/' | relative_url }}) | Sécurité — limites proxy (Diagramme 7) |
| 12 | [Gestion de projet]({{ '/fr/publications/project-management/' | relative_url }}) | Projets — hiérarchie P# (Diagrammes 1, 8) |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
