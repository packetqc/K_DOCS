---
layout: publication
title: "Diagrammes d'architecture de Knowledge 2.0 — Documentation complète"
description: "Architecture visuelle complète : 14 diagrammes Mermaid couvrant vue d'ensemble multi-module, architecture mémoire mind-first, structure des modules K_, cycle de vie des sessions, flux inter-modules, pipeline de publication, limites de sécurité, architecture web, dépendances des qualités, chemins de récupération et intégration GitHub."
pub_id: "Publication #15 — Complete"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/architecture-diagrams/full/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "architecture, diagrammes, mermaid, knowledge 2.0, multi-module, mind-first, sécurité"
---

# Diagrammes d'architecture de Knowledge 2.0 — Documentation complète
{: #pub-title}

**Table des matières**

| | |
|---|---|
| [Auteurs](#auteurs) | Auteurs de la publication |
| [Résumé](#resume) | Companion visuel de l'architecture Knowledge 2.0 |
| [Conventions des diagrammes](#conventions-des-diagrammes) | Codage couleur, notation, syntaxe Mermaid |
| [1. Vue d'ensemble](#1-vue-densemble--contexte-c4) | Contexte C4 — Système multi-module au centre |
| [2. Architecture mémoire Mind-First](#2-architecture-memoire-mind-first) | Mémoire à 4 niveaux : Mindmap → JSONs → Near → Far |
| [3. Architecture multi-module](#3-architecture-multi-module) | 5 modules K_, scripts et relations |
| [4. Cycle de vie de session](#4-cycle-de-vie-de-session) | session_init → /mind-context → memory_append → archive |
| [5. Flux d'interaction des modules](#5-flux-dinteraction-des-modules) | K_MIND hub central, pipelines de compilation, invocations de skills |
| [6. Pipeline de publication](#6-pipeline-de-publication) | Source → viewer statique → EN/FR × résumé/complet × 4 thèmes |
| [7. Limites de sécurité](#7-limites-de-securite) | Modèle proxy — opérations autorisées vs bloquées |
| [8. Architecture web](#8-architecture-web) | Viewer JS statique, 4 thèmes, 5 interfaces, .nojekyll |
| [9. Dépendances des qualités](#9-graphe-de-dependance-des-qualites) | Graphe de dépendance des 13 qualités |
| [10. Chemins de récupération](#10-chemins-de-recuperation) | Récupération K_MIND : compaction, rappel, session init |
| [11. Intégration GitHub](#11-integration-github) | Module K_GITHUB, scripts de sync, cycle de vie boards |
| [Publications liées](#publications-liees) | Publications parentes et liées |

## Auteurs

**Martin Paquet** — Analyste et programmeur sécurité réseau, administrateur de sécurité des réseaux et des systèmes, et analyste programmeur et concepteur logiciels embarqués. Architecte du système Knowledge — une intelligence d'ingénierie IA auto-évolutive construite sur 30 ans d'expérience en systèmes embarqués, sécurité réseau et développement logiciel. A conçu l'architecture multi-module documentée dans ces diagrammes.

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. A co-créé les diagrammes architecturaux, rendant la structure du système en notation Mermaid pour une visualisation web interactive. Opère au sein du système que ces diagrammes décrivent.

---

## Résumé

Knowledge 2.0 est un **système d'intelligence d'ingénierie IA multi-module** structuré autour d'une grille mémoire centrale (K_MIND) avec des modules satellites spécialisés (K_DOCS, K_GITHUB, K_PROJECTS, K_VALIDATION). Cette publication est le **companion visuel** — 14 diagrammes Mermaid qui rendent la structure, les flux, les limites et les dépendances du système en visualisations interactives.

Ces diagrammes couvrent toute la surface architecturale : du contexte C4 de haut niveau (5 modules K_ au centre, plateforme GitHub, viewer web statique) jusqu'aux limites de sécurité granulaires (couches proxy, canaux API) et l'architecture mémoire mind-first (mindmap → JSONs de domaine → mémoire near/far → archives).

Tous les diagrammes utilisent la syntaxe [Mermaid](https://mermaid.js.org/), rendue côté client par le viewer JS statique via CDN.

---

## Audience ciblée

| Audience | Quoi privilégier |
|----------|-----------------|
| **Administrateurs réseau** | Interaction modules (#5), limites de sécurité (#7), architecture web (#8) |
| **Administrateurs système** | Architecture web (#8), intégration GitHub (#11), pipeline de publication (#6) |
| **Programmeurs et programmeuses** | Architecture multi-module (#3), cycle de vie de session (#4), chemins de récupération (#10) |
| **Gestionnaires** | Vue d'ensemble (#1), mémoire mind-first (#2), dépendances des qualités (#9) |

## Conventions des diagrammes

Tous les diagrammes utilisent la notation **Mermaid** — un langage de diagrammes basé sur le markdown, rendu côté client par le viewer JS statique.

**Codage couleur** :

| Couleur | Signification | Utilisé pour |
|---------|---------------|--------------|
| Sarcelle / Vert | Core / Stable / Obligatoire | K_MIND, mind_memory, conventions stables |
| Bleu | Actif / En cours | Sessions, flux actifs, opérations en cours |
| Orange / Ambre | Avertissement / Dérive | Dérive de version, contenu périmé, problèmes mineurs |
| Rouge | Critique / Bloqué | Limites de sécurité, blocages proxy |
| Violet | Externe / Plateforme | GitHub, GitHub Pages, services externes |
| Gris | Inactif / En attente | Chemins inutilisés, éléments en attente |

**Notation** :

| Symbole | Signification |
|---------|---------------|
| Flèche pleine (`-->`) | Flux de données direct ou dépendance |
| Flèche tiretée (`-.->`) | Flux indirect ou périodique |
| Flèche épaisse (`==>`) | Chemin principal / critique |
| Sous-graphe | Groupement logique ou limite |

---

## 1. Vue d'ensemble — Contexte C4

Le système Knowledge 2.0 se situe au centre d'une constellation d'acteurs : 5 modules K_ internes, services de la plateforme GitHub, GitHub Pages pour l'hébergement web statique, Claude Code comme moteur de session IA, et le développeur humain.

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


**Légende** : Le système est organisé en 5 modules K_ sous un répertoire `Knowledge/`. K_MIND est le core obligatoire — toujours chargé, toujours maintenu. Les autres modules (K_DOCS, K_GITHUB, K_PROJECTS, K_VALIDATION) fournissent des capacités spécialisées. Claude Code est l'environnement d'exécution, lisant la mindmap à chaque début de session et maintenant la mémoire via des scripts à chaque tour. GitHub Pages sert le viewer web statique avec rendu côté client du markdown et mermaid.

---

## 2. Architecture mémoire Mind-First

Le système organise les connaissances en 4 niveaux de stabilité décroissante et de granularité croissante. La mindmap est la grille de directives opérationnelles — toujours chargée en premier. Les JSONs de domaine fournissent des références structurées. La near memory suit la session en temps réel. La far memory préserve l'historique verbatim complet.

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


**Légende** : Les connaissances remontent (far memory → near memory → JSONs de domaine → mindmap) par le pipeline de staging. Elles descendent (mindmap → comportement session) comme directives opérationnelles. L'ordre de chargement suit la stabilité : le plus stable d'abord (mindmap), le plus granulaire en dernier (far memory archivée). Toutes les opérations mécaniques utilisent des scripts Python déterministes — Claude fournit l'intelligence (résumés, noms de sujets) comme arguments.

---

## 3. Architecture multi-module

Les 5 modules K_, leur structure interne, scripts et relations au sein du dépôt Knowledge 2.0.

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


**Légende** : Le dépôt est organisé en 5 modules K_ sous `Knowledge/`. Chaque module possède ses propres conventions, état de travail et scripts. K_MIND est obligatoire (toujours chargé). Les autres modules sont déclarés dans `modules.json` et chargés à la demande. Le répertoire `docs/` est la sortie web — servi par GitHub Pages avec .nojekyll (aucune étape de build). Les scripts de compilation dans K_VALIDATION et K_PROJECTS produisent des données JSON consommées par les interfaces du viewer statique.

---

## 4. Cycle de vie de session

Chaque session Claude Code suit un cycle de vie déterministe géré par les scripts K_MIND. La mindmap est chargée en premier, la mémoire est maintenue à chaque tour, et les sujets sont archivés une fois terminés.

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


**Légende** : Le cycle de vie de session a trois phases : démarrage (/mind-context), travail (memory_append à chaque tour) et récupération (gestion de compaction). Le principe mind-first signifie que la mindmap est toujours chargée en premier — elle contient toutes les directives comportementales. La far memory stocke la conversation verbatim complète ; la near memory stocke des résumés en une ligne avec des pointeurs. L'archivage par sujet maintient far_memory.json gérable. La récupération de compaction relit la mindmap et la near memory, avec rappel optionnel approfondi depuis les archives.

---

## 5. Flux d'interaction des modules

Comment les 5 modules K_ interagissent : K_MIND comme hub central, pipelines de compilation alimentant le viewer web, et invocations de skills inter-modules.

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


**Légende** : K_MIND est le hub — sa mindmap fournit des directives à tous les modules, et gh_helper.py est le wrapper API GitHub partagé. K_PROJECTS et K_VALIDATION compilent des données structurées dans les fichiers JSON de `docs/data/` consommés par les 5 interfaces web. K_GITHUB synchronise l'état GitHub externe. K_DOCS possède la méthodologie et les conventions du pipeline web. La live mindmap (I5) lit directement depuis mind_memory.md.

---

## 6. Pipeline de publication

Chaque publication existe à deux niveaux web (résumé + complet), en deux langues (EN + FR), rendue par le viewer JS statique avec 4 variantes de thème.

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


**Légende** : Les publications suivent la méthodologie K_DOCS. Les pages EN et FR partagent des corps `{::nomarkdown}` identiques — la langue est un paramètre runtime via JS `translateStatic()` (convention conv-020 : jamais de duplication de templates). Le viewer statique rend le markdown + mermaid côté client avec 4 variantes de thème. L'export PDF utilise CSS @page media ; le DOCX utilise des éléments MSO. Les skills de validation assurent la concordance EN/FR et l'intégrité structurelle.

---

## 7. Limites de sécurité

Le modèle proxy régissant ce que les sessions Claude Code peuvent et ne peuvent pas faire. Le proxy du conteneur médiatise toutes les opérations git tandis que Python urllib le contourne pour l'accès API.

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


**Légende** : Le proxy du conteneur est la limite de sécurité principale. Les opérations git sont restreintes à la branche de tâche assignée. `gh_helper.py` (situé dans K_MIND/scripts/) contourne le proxy via Python `urllib`, permettant un accès complet à l'API GitHub avec un token valide. `curl` est intercepté et les headers d'authentification sont supprimés. Le modèle à deux canaux : proxy git (restreint) + urllib (sans restriction avec token). Le token n'est jamais exposé dans les commandes ou URLs — gh_helper.py gère la récupération du token en interne.

---

## 8. Architecture web

L'architecture du viewer web statique : GitHub Pages .nojekyll, rendu côté client, système à 4 thèmes, 5 interfaces interactives et synchronisation de thème via BroadcastChannel.

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


**Légende** : La présence web utilise GitHub Pages .nojekyll — aucun build côté serveur. Le viewer JS statique (2065 lignes) gère le parsing markdown, le rendu mermaid, la réécriture de liens, le changement de thème et l'export. Le système à 4 thèmes utilise des propriétés CSS personnalisées injectées par un moteur de thème. Les interfaces s'exécutent comme iframes dans le navigateur principal, recevant les diffusions de thème via BroadcastChannel. Les données JSON compilées par K_VALIDATION et K_PROJECTS alimentent les interfaces. MindElixir v5.9.3 alimente la live mindmap avec les mêmes 4 thèmes.

---

## 9. Graphe de dépendance des qualités

Les 13 qualités core et comment elles dépendent les unes des autres. Autosuffisant est la fondation — si le système dépend de services externes, rien d'autre ne fonctionne.

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


**Légende** : Le graphe de dépendance coule de la fondation (autosuffisant — texte brut dans Git) à travers les qualités habilitantes vers les qualités organisationnelles. Mis à jour pour Knowledge 2.0 : Interactif référence les 5 interfaces web, Distribué référence le flux multi-module, Résilient référence la récupération K_MIND, et Structuré référence la hiérarchie des modules K_.

---

## 10. Chemins de récupération

Les mécanismes de récupération K_MIND, du plus léger au plus lourd. Chaque chemin répond à un mode de panne différent.

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


**Légende** : K_MIND fournit 4 chemins de récupération. **Compaction** (le plus courant) : `/mind-context` recharge la mindmap et la near memory — suffisant dans la plupart des cas. **Rappel profond** : `memory_recall.py` recherche dans les sujets archivés quand des détails spécifiques sont nécessaires. **Récupération de crash** : `session_init.py --preserve-active` préserve les messages existants. **Démarrage frais** : nouvelle session hérite des résumés last_session pour la continuité.

**Résumé de récupération** :

| Récupération | Déclencheur | Vitesse | Ce qui est restauré |
|--------------|------------|---------|---------------------|
| `/mind-context` | Compaction de contexte | ~5s | Directives mindmap + résumés récents |
| `memory_recall.py` | Besoin de détails archivés | ~10s | Sujet spécifique depuis les archives |
| `session_init --preserve-active` | Crash avec messages | ~10s | Continuité complète de session |
| `session_init` (frais) | Nouvelle session | ~15s | Démarrage propre + contexte last_session |
| Vérification near memory | Contexte périmé | ~3s | Résumés d'activité récente |

---

## 11. Intégration GitHub

Le module K_GITHUB gère la synchronisation des entités GitHub. `gh_helper.py` (dans K_MIND/scripts/) est le wrapper API partagé utilisé par tous les modules.

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


**Légende** : Trois flux de travail clés. **Cycle de vie des tâches** : évaluation par skill → travail avec mémoire en temps réel → push vers main → auto-déploiement. **Compilation de données** : les scripts K_VALIDATION et K_PROJECTS compilent des JSON consommés par les interfaces web. **Synchronisation GitHub** : les scripts K_GITHUB récupèrent l'état externe dans des fichiers de données locaux. Tous les appels API passent par `gh_helper.py` (Python urllib, contourne le proxy du conteneur).

---

## 12. Carte mentale de l'architecture système

Carte de navigation de haut niveau du système Knowledge 2.0 avec ses piliers architecturaux.

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


**Les piliers architecturaux** :

| # | Pilier | Essence | Éléments clés |
|---|--------|---------|---------------|
| 1 | **Core multi-module** | L'organisation K_ | 5 modules + registre, chacun avec ses conventions/travail/scripts |
| 2 | **Mémoire mind-first** | La mémoire opérationnelle | Mindmap → JSONs domaine → near/far → archives |
| 3 | **Système de session** | Le rythme de travail | init → append → split → recover |
| 4 | **Présence web** | La face publique | Viewer statique, .nojekyll, 4 thèmes, 25+ pubs |
| 5 | **5 interfaces** | La couche interactive | Navigateur, session, tâche, projet, mindmap |
| 6 | **Système de skills** | La surface de commande | Skills spécifiques par module invoqués par Claude |
| 7 | **Sécurité** | Confiance par conception | Modèle proxy, gestion de tokens, fork-safe |
| 8 | **Cadre qualité** | Le contrat qualité | 13 qualités, graphe de dépendance, 30 ans distillés |

---

## 13. Carte mentale de la structure des modules

La structure au niveau fichier de Knowledge 2.0 — chaque module et ses composants.

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


**Rôles des modules** :

| Module | Fichiers | Rôle principal |
|--------|----------|---------------|
| **K_MIND** | 38 | Mémoire core : mindmap, sessions, JSONs domaine, 10 scripts |
| **K_DOCS** | 4 374 | Pipeline documentation : viewer web, publications, interfaces |
| **K_PROJECTS** | 13 | Gestion de projet : registre P#, compilation, skills |
| **K_VALIDATION** | 19 | QA : workflow tâches, protocole session, vérifications d'intégrité |
| **K_GITHUB** | 9 | Synchronisation GitHub : issues, PRs, boards, enrichissement |
| **docs/** | 100+ | Sortie web : viewer statique, 25+ pubs, 5 interfaces |

---

## 14. Carte mentale de la structure Publication

L'anatomie d'une publication Knowledge 2.0 — composants, niveaux, assets et intégration.

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


**Cycle de vie d'une publication** :

```
/docs-create → Pages EN/FR scaffoldées → Webcards générées
    → Contenu écrit (corps EN/FR identique)
    → /normalize → Concordance EN/FR vérifiée
    → /integrity-check → Structure validée
    → Push → .nojekyll deploy → En ligne sur GitHub Pages
```

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
