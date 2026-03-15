---
layout: publication
title: "Project Management — Complete Documentation"
description: "Complete documentation for project management in Knowledge: entity model, hierarchical indexing (P#/S#/D#), project commands, satellite bootstrap protocol, web presence scaffolding, tagged input for scoped knowledge, dual-origin publishing, GitHub Project integration, and multi-instance convergence."
pub_id: "Publication #12 — Full"
version: "v1"
date: "2026-02-22"
permalink: /publications/project-management/full/
og_image: /assets/og/project-management-en-cayman.gif
keywords: "project, management, indexing, satellite, bootstrap, hierarchy"
---

# Project Management — Complete Documentation
{: #pub-title}

**Contents**

| | |
|---|---|
| [Authors](#authors) | Publication authors |
| [Abstract](#abstract) | Project management system overview |
| [Related Publications](#related-publications) | Parent and sibling publications |
| [Project Entity Model](#1-project-entity-model) | Three-level entity: logical, physical, platform |
| &nbsp;&nbsp;[Project Relationships](#project-relationships) | Owns, child-of, and managed relationship types |
| &nbsp;&nbsp;[Current Registry](#current-registry) | Active project index P0 through P9 |
| &nbsp;&nbsp;[MPLIB Decoupling](#mplib-decoupling) | MPLIB reclassified as child project P1 |
| [Hierarchical Indexing](#2-hierarchical-indexing-psd) | P#/S#/D# hierarchical identifier scheme |
| &nbsp;&nbsp;[Display Convention](#display-convention) | How index tags appear in inventories |
| &nbsp;&nbsp;[Machine-Parseable Markers](#machine-parseable-markers) | Structured markers for automated processing |
| [Project Commands](#3-project-commands) | CLI commands for project management |
| [Satellite Bootstrap Protocol](#4-satellite-bootstrap-protocol) | Multi-round satellite installation |
| &nbsp;&nbsp;[Console Guidance](#console-guidance-human-bridge) | Human bridge UX for bootstrap steps |
| &nbsp;&nbsp;[Round 1 — Bootstrap](#round-1--bootstrap) | Essential files and CLAUDE.md scaffold |
| &nbsp;&nbsp;[Round 2 — Normalize](#round-2--normalize) | Structure concordance enforcement |
| &nbsp;&nbsp;[Round 3 — Project Create](#round-3--project-create-optional) | Web presence and GitHub board setup |
| &nbsp;&nbsp;[Critical-Subset Principle](#critical-subset-principle) | Behavioral DNA that survives compaction |
| [Web Presence Scaffolding](#5-web-presence-scaffolding) | GitHub Pages docs structure creation |
| &nbsp;&nbsp;[File Specifications](#file-specifications) | 12 files and 7 directories created |
| &nbsp;&nbsp;[Layout Adaptation](#layout-adaptation-rules) | Layout customization for satellite projects |
| &nbsp;&nbsp;[Post-Create Checklist](#post-create-checklist) | Verification steps after scaffolding |
| [Tagged Input](#6-tagged-input--call-alias) | `#N:` scoped knowledge input system |
| &nbsp;&nbsp;[Implicit Main Project](#implicit-main-project) | Default routing when no `#N:` prefix |
| &nbsp;&nbsp;[Raw Dump Mode](#raw-dump-mode) | Unstructured input classification |
| &nbsp;&nbsp;[Multi-Satellite Convergence](#multi-satellite-convergence) | Same project documented from multiple repos |
| &nbsp;&nbsp;[Subconscious Detection](#subconscious-detection) | Automatic insight-to-publication matching |
| [Dual-Origin Link System](#7-dual-origin-link-system) | Core vs satellite origin badges |
| [GitHub Project Integration](#8-github-project-integration) | Projects v2 board creation and linking |
| [Integration with Existing Commands](#9-integration-with-existing-commands) | How project commands extend harvest, normalize, pub |
| [URL Preservation](#10-url-preservation) | Backward-compatible URL scheme |
| [Multi-Instance Concurrent Updates](#11-multi-instance-concurrent-updates) | Append-only concurrent project editing |
| [Project Required Assets](#12-project-required-assets) | Mandatory files and assets per project |
| [Project Lifecycle](#13-project-lifecycle) | Register to create to publish to harvest to evolve |

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Designed the project entity model that gives formal identity to the distributed knowledge network.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Implements project commands, satellite bootstrap, and web presence scaffolding across the knowledge network.

---

## Abstract

As the knowledge network grew from a single repository to 6+ projects with multiple satellites each, a structural gap emerged: **projects had no formal identity**. Repositories existed, publications existed, satellites existed — but the entity that ties them together (the project) was implicit.

Publication #12 documents the v35 project entity model that makes projects explicit: hierarchical indexing (P#/S#/D#), three-level entity model (logical, physical, platform), dual-origin publishing, satellite lifecycle management, and the commands that operate on them.

This publication consolidates four methodology documents into a single reference:

| Document | Scope |
|----------|-------|
| **Project Management** | Entity model, indexing, commands, integration |
| **Satellite Bootstrap** | Single-session iterative staging protocol |
| **Project Create** | Web presence scaffolding for satellites |
| **Tagged Input** | `#` call alias for scoped project knowledge |

---

## Related Publications

| # | Publication | Relationship |
|---|------------|--------------|
| 0 | [Knowledge]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — project management extends the core system |
| 4 | [Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }}) | Architecture — projects organize the distributed network |
| 4a | [Knowledge Dashboard]({{ '/publications/distributed-knowledge-dashboard/' | relative_url }}) | Dashboard — project status displayed in network view |
| 7 | [Harvest Protocol]({{ '/publications/harvest-protocol/' | relative_url }}) | Collection — harvest operates on project-indexed content |
| 8 | [Session Management]({{ '/publications/session-management/' | relative_url }}) | Lifecycle — sessions operate within project context |
| 11 | [Success Stories]({{ '/publications/success-stories/' | relative_url }}) | Validation — project milestones become stories |

---

## 1. Project Entity Model

A **project** is a first-class entity that exists at three levels:

| Level | What it means | Example |
|-------|--------------|---------|
| **Logical** | An organized body of work with publications, documentation, evolution, stories | Knowledge (P0) |
| **Physical** | One or more Git repositories (satellites) that implement the project, or **none** for managed projects | `packetqc/knowledge`, `packetqc/MPLIB` |
| **Platform** | A GitHub Project board for tracking issues, milestones, and progress | GitHub Project entity (when elevated) |

A project is **not** a repository — it **has** repositories. A project is **not** a publication — it **has** publications. The project entity ties everything together.

### Project Relationships

Projects have four relationship types to repositories:

| Relationship | Meaning | Example |
|-------------|---------|---------|
| **owns** | The project's primary repository | P0 owns `packetqc/knowledge` |
| **child-of** | A sub-project of a parent project | P1 (MPLIB) is child-of P0 |
| **managed** | No dedicated repository — lives in host repo or core | Documentation, processes, cross-cutting initiatives — board always links to a repo |

**Managed projects** may live as subfolders in a host repo or purely in knowledge core. They get their own P# ID. On `harvest`, their content is routed to the correct project, not the host's. Their GitHub Project board always links to a repo: child projects link to their own repo, managed projects link to the host repo (or core repo as fallback). Every project links to a repo — no exceptions.

### Promotion-Based Import

When a managed project or new asset matures, the **promotion cycle** handles import and normalization:

| Phase | Action |
|-------|--------|
| **Discover** | `harvest` detects content belonging to a different project |
| **Route** | Content routed to the correct project's `minds/` entry |
| **Register** | If the project doesn't exist, `project register` assigns a P# ID |
| **Review** | `harvest --review` validates the content |
| **Stage** | `harvest --stage N <type>` prepares for integration (type: lesson, pattern, methodology, evolution, docs, project) |
| **Promote** | `harvest --promote N` writes to project's core assets |
| **Normalize** | `normalize` ensures promoted content follows conventions |

### Current Registry

| ID | Project | Type | Status |
|----|---------|------|--------|
| P0 | Knowledge | core | active |
| P1 | MPLIB | child | active |
| P2 | STM32 PoC | child | active |
| P3 | knowledge-live | child | active |
| P4 | MPLIB Dev Staging | child (of P1) | active |
| P5 | PQC | child | pre-bootstrap |

### MPLIB Decoupling

MPLIB is reclassified from core asset to child project (P1):

| Before (v34) | After (v35) |
|--------------|-------------|
| Publications index titled "MPLIB Knowledge" | Titled "Knowledge" |
| MPLIB patterns in core | Stay in core — tagged as originating from P1 |
| Publication #1 = core publication | P0/#1 with cross-ref `->P1` |

What doesn't change: Publication #1 stays at its URL. MPLIB patterns stay in core (they generalize). What changes: identity — MPLIB is a successful child, not part of the core's name.

---

## 2. Hierarchical Indexing (P#/S#/D#)

Three levels of indexing:

```
Level 1: P<n>                    <- Project identifier
Level 2: P<n>/S<m>              <- Satellite (repository instance)
Level 3: P<n>/#<pub>            <- Publication
         P<n>/S<m>/D<k>         <- Satellite-local document
```

### Display Convention

In all inventories, dashboards, and command output, the index appears **left of the status tag**:

```
P0/#0    Knowledge
P0/#1    MPLIB Storage Pipeline           ->P1
P0/#2    Live Session Analysis
P0/#4    Distributed Minds
P0/#10   Live Knowledge Network           ->P3
P1/S1    MPLIB (v31)
P5/S1    PQC (v0, pre-bootstrap)
```

The `->P<n>` cross-reference marker indicates a publication that documents a different project.

### Machine-Parseable Markers

Every project metadata file carries markers:

```markdown
<!-- project-id: P<n> -->
<!-- project-type: core|child|managed -->
<!-- project-status: active|pre-bootstrap|archived -->
<!-- github-project: <url or X> -->
<!-- parent-project: P<n> -->
```

Every document can carry provenance markers:

```markdown
<!-- project-index: P0/#7 -->
<!-- last-updated-by: knowledge/claude/<task-id> -->
<!-- last-updated: YYYY-MM-DD -->
```

---

## 3. Project Commands

| Command | Action |
|---------|--------|
| `project list` | List all projects with P# index, type, status, satellite count |
| `project info <P#>` | Show project details — identity, publications, satellites, evolution, stories, assets |
| `project create <name>` | Full creation: register P# + GitHub Project board (elevated, linked to repo) + web presence |
| `project register <name>` | Register a new project with P# ID — creates `projects/<slug>.md` in core |
| `project review <P#>` | Review project state — documentation, publications, required assets, freshness |
| `project review --all` | Review all projects |

### `project list` Output

```
=== Projects ===

  ID   Name                    Type     Status           Sats  Pubs  Health
  P0   Knowledge               core     active            5     14    healthy
  P1   MPLIB                   child    active            2     1     healthy
  P2   STM32 PoC              child    active            1     1     healthy
  P3   knowledge-live          child    active            1     1     healthy
  P4   MPLIB Dev Staging       child    active            1     0     healthy
  P5   PQC                     child    pre-bootstrap     1     0     pending

  Total: 6 projects (5 active, 1 pre-bootstrap)
```

### `project review` Output

Audits a project against the required assets checklist:

```
=== Project Review: P1 (MPLIB) ===

  Identity:      registered (projects/mplib.md)
  CLAUDE.md:     active (v31, critical-subset)
  notes/:        present (2 sessions in P1/S1, 5 sessions in P1/S2)
  live/:         deployed
  Publications:  1 in core (P0/#1), 0 local
  Docs:          web presence not created
  GitHub Project: not created
  Evolution:     6 entries (last: 2026-02-22)
  Stories:       3 entries (2 undated)
```

### `project create` — Enhanced Protocol

```
1. Register project:      Assign P# ID, create projects/<slug>.md
2. Create GitHub Project:  If elevated, create board via API (gh_helper.py / urllib)
3. Link project to repo:  If elevated, link board to repository via API
4. Bootstrap satellite:   wakeup step 0.5
5. Scaffold web presence: docs/, layouts, hubs, publications/
6. Register in core:     Update projects/README.md
7. Update dashboard:     Add satellite to harvest dashboard
8. Commit & deliver:     Commit, push, PR
```

### `project register` — Lightweight

Just creates the project metadata file. Used when the repo already exists or when registering a discovered project from harvest. Auto-populates from `minds/<slug>.md` and git history if available.

---

## 4. Satellite Bootstrap Protocol

Single-session iterative staging — one session does everything, user merges between rounds, no restarts.

```
Round 1: wakeup -> bootstrap scaffold -> commit -> push -> PR
         user merges -> refresh -> verify stage 1

Round 2: normalize -> trim to critical-subset -> commit -> push -> PR
         user merges -> refresh -> verify stage 2

Round 3: project create (optional) -> commit -> push -> PR
         user merges -> refresh -> verify stage 3

Final:   "Installation complete. Any new session will auto-wakeup."
```

### Console Guidance (Human Bridge)

The session actively guides the user through every manual step. Never go silent between rounds. After each commit+push+PR, print: what was pushed, the PR URL (or manual creation URL), and a clear pause instruction.

After commit + push:

```
=== Stage N — PR Created ===

  PR: https://github.com/packetqc/<repo>/pull/<N>
  Branch: claude/<task-id> -> <default-branch>

  Please merge the PR to continue staging.
  Say "merged" when done.
```

After user says "merged":

```
=== Stage N Verified ===

  <checklist results>

  Proceeding to Stage N+1...
```

### Round 1 — Bootstrap

Wakeup step 0.5 creates missing essential files (non-destructive):

| File | Content |
|------|---------|
| `CLAUDE.md` | Critical-subset (~180 lines): knowledge pointer + behavioral DNA + commands |
| `README.md` | Repo name, description, link to knowledge |
| `LICENSE` | MIT with current year |
| `.gitignore` | Standard ignores (`.env`, `*.pem`, `node_modules/`, `__pycache__/`, `.mp4`) |
| `notes/.gitkeep` | Session persistence folder |

Autonomous change detection triggers the staging flow automatically — no need for the user to type `save`.

### Round 2 — Normalize

Trim the satellite CLAUDE.md to critical-subset form (~180 lines). Remove deep implementation content that was over-synced in Round 1. Keep: knowledge pointer, session protocol, save protocol, branch protocol, human bridge, full 7-group commands reference, project overview.

### Round 3 — Project Create (Optional)

Scaffold web presence with `project create <name>`. Only needed if the satellite will produce documentation or publications. Creates 10 files, 6 directories (see section 5).

### Critical-Subset Principle

The satellite CLAUDE.md carries enough DNA to drive correct behavior even after context compaction:

```
Core CLAUDE.md (2600+ lines)    Full methodology, implementations    <- source of truth
         |
         | read on wakeup (Step 0)
         |
Satellite CLAUDE.md (~180 lines) Knowledge pointer                   <- critical-subset
                                  Session + save + branch protocol       (survives compaction)
                                  Full 7-group commands reference
                                  Project overview + commands
```

**Why not thin-wrapper (~30 lines)**: After compaction, satellites lost all behavioral rules. The critical-subset includes essential operational rules that survive.

**Why not full mirror (2600+ lines)**: Duplicating core creates massive version drift. The critical-subset carries behavioral rules (stable) but NOT implementation details (evolve frequently).

### Final Confirmation

```
=== Installation Complete ===

  Satellite: <repo-name>
  Knowledge version: v36
  CLAUDE.md: critical-subset (~200 lines)
  Default branch: <main|master>

  Any new Claude Code session on this repo will:
  1. Auto-wakeup (step 0: read packetqc/knowledge)
  2. Inherit all methodology, commands, patterns
  3. Have session persistence (notes/)
  4. Be discoverable by harvest --healthcheck
```

---

## 5. Web Presence Scaffolding

`project create <name>` scaffolds a complete GitHub Pages + publication structure:

```
<satellite-repo>/
  docs/
    _config.yml                    <- Jekyll config for GitHub Pages
    _layouts/
      default.html                 <- Copied from knowledge (Cayman/Midnight themes)
      publication.html             <- Copied from knowledge (banner, keywords, cross-refs)
    index.md                       <- Project landing page (EN)
    publications/
      index.md                     <- Publications hub (EN)
    fr/
      index.md                     <- Project landing page (FR)
      publications/
        index.md                   <- Publications hub (FR)
    assets/
      og/.gitkeep                  <- Webcard GIFs placeholder
  publications/
    .gitkeep                       <- Source publications folder
```

**10 files, 6 directories.** Everything for a bilingual GitHub Pages site with publication support.

### File Specifications

**`_config.yml`**: Project-specific title, baseurl `/<repo-name>`, no remote theme. Layouts are self-contained.

**Layouts**: Copied from knowledge with one change — `og:site_name` replaced with project name. Everything else identical: Cayman/Midnight CSS, webcard header, mermaid support, cache-bust JS.

**Landing pages**: EN + FR with project name, links to knowledge and publications.

**Publications hubs**: EN + FR — empty, ready for `pub new`.

### Layout Adaptation Rules

| Rule | Detail |
|------|--------|
| Replace `og:site_name` | Use the project name instead of the knowledge site name |
| Keep everything else | CSS, JS, webcard header, mermaid — identical to knowledge |
| Keyword map | Leave as-is (points to knowledge publications) |
| Version banner | Works automatically from front matter |
| Theme detection | Automatic (Cayman/Midnight via `prefers-color-scheme`) |

### Post-Create Checklist

| Step | Who | Action |
|------|-----|--------|
| 1 | Claude | Commit all created files to task branch |
| 2 | Claude | Push to task branch, create PR |
| 3 | User | Enable GitHub Pages: Settings > Pages > Source: default branch, `/docs` |
| 4 | User | Approve PR to merge docs structure |
| 5 | User | Visit `https://packetqc.github.io/<repo-name>/` to verify |

---

## 6. Tagged Input (`#` Call Alias)

The `#` prefix at the beginning of a prompt triggers scoped knowledge input mode. Claude routes, classifies, and stores the content.

| Command | Action |
|---------|--------|
| `#N: <content>` | Scoped note for publication/project #N |
| `#N:methodology:<topic> <content>` | Methodology insight — flagged for doc harvesting |
| `#N:principle:<topic> <content>` | Design principle — flagged for doc harvesting |
| `#N:info` | Show all accumulated knowledge for #N |
| `#N:info:<topic>` | Show specific topic within #N |
| `#N:done` | End documentation focus, compile summary |

### Implicit Main Project

Every repo has a main project. When the user feeds information without `#N:` prefix, Claude assumes it's for the repo's main project:

| Repo | Main project | `#` equivalent |
|------|-------------|----------------|
| `packetqc/knowledge` | #0 Knowledge | `#0:` |
| `packetqc/STM32N6570-DK_SQLITE` | #1 MPLIB Storage Pipeline | `#1:` |

Use `#N:` explicitly only when the content is for a *different* project.

### Raw Dump Mode

`#N:` accepts unstructured raw input. Claude uses acquired knowledge (CLAUDE.md, publications, methodology) + universal knowledge to classify, route, and store. The user says whatever they have; Claude organizes it.

### Multi-Satellite Convergence

The same project can be documented from multiple satellites. `#N:` is the routing key, not the repo — the insight goes where it belongs regardless of where it was discovered.

```
Satellite A --> harvest --> minds/ --> promotion --> core knowledge
Satellite B --> harvest --/
Satellite C --> harvest --/
Core direct ---------------------------------> notes/ --> core knowledge
```

### Subconscious Detection

During normal conversation, Claude monitors for content that naturally relates to a publication's domain. When obvious, Claude suggests capture:

> *This looks relevant to #7 (Harvest Protocol). Capture it? (`#7:methodology:incremental-cursors` to confirm)*

Light touch — only when obvious, not on every message.

### `#N:info` Output

```
=== #7 Harvest Protocol — Accumulated Knowledge ===

  Methodology (3 notes)
  - incremental-cursors: only scan commits after cursor
  - branch-crawling: enumerate all remote branches via ls-remote
  - cleanup: rm -rf temporary clones after extraction

  Principles (1 note)
  - pull-based: satellites self-heal by reading core

  General (2 notes)
  - dashboard should update all 5 files on every harvest
  - healthcheck should report unreachable satellites

  Sources: knowledge (2), STM32N6570-DK_SQLITE (3), MPLIB (1)
```

---

## 7. Dual-Origin Link System

Publications exist across repos with independent GitHub Pages:

| Origin | Badge | Base URL | Meaning |
|--------|-------|----------|---------|
| **Core** | **core** | `packetqc.github.io/K_DOCS/` | Reviewed, published, canonical |
| **Satellite** | *satellite* | `packetqc.github.io/<repo>/` | Development, staging, local |

Both are valid — same GitHub Pages technology, different review stage. Core links are stable and safe to share externally. Satellite links are evolving and may change.

Cross-referencing: core publications reference satellite docs for "latest development" state. Satellite docs reference core for "official" state.

---

## 8. GitHub Project Integration

When elevated (PAT with project scope), `project create` creates a GitHub Project board — the **human interface layer**. Two entry points: `project create` (new project scaffolding) and `harvest --promote` (promoted insights create or update board items).

| Knowledge system (AI-native) | GitHub Project (human-native) |
|------------------------------|-------------------------------|
| `projects/<slug>.md` metadata | Project board with cards |
| Evolution entries (v#) | Milestones |
| Harvest insights | Issues (auto-created from promotion candidates) |
| Project stories | Discussion threads |
| `project review` findings | Issue labels (stale, missing, drift) |
| Session notes | Activity timeline |

**Why this matters**: Knowledge is powerful but opaque to non-AI participants. A GitHub Project board with labeled issues, milestones, and assignees is immediately comprehensible. The board is the **human-readable projection** of the AI-native project state.

**Automation potential** (when elevated):

| Command | Board effect |
|---------|-------------|
| `harvest --healthcheck` | Creates issues for critical findings |
| `project review` | Creates issues for missing assets |
| `doc review --apply` | Updates milestone progress |
| `harvest --promote` | Moves board cards from "Backlog" to "Done" |

---

## 9. Integration with Existing Commands

| Command | What project management adds |
|---------|------------------------------|
| `harvest --healthcheck` | Project status table — counts, satellite health, publication distribution |
| `normalize` | Project concordance — registry consistency, unique P# assignments, valid cross-refs |
| `pub list` | Project index column — `P0/#1` with `->P1` cross-references |
| `doc review --list` | Project index in freshness inventory |

---

## 10. URL Preservation

The project restructure is **additive** — no existing URLs change:

| Existing (unchanged) | New (additive) |
|---------------------|----------------|
| `/publications/<slug>/` | `/projects/` (EN project hub) |
| `/publications/<slug>/full/` | `/fr/projects/` (FR project hub) |
| `/fr/publications/<slug>/` | |
| `/profile/`, `/profile/resume/`, `/profile/full/` | |
| `/assets/og/<card>.gif` | |

The project hub pages link to existing publication URLs, organized by project. Two navigation paths to the same content: by publication number (existing) and by project (new).

---

## 11. Multi-Instance Concurrent Updates

Multiple Claude Code instances can update the same project's content:

| Mechanism | Detail |
|-----------|--------|
| **Append-only indexing** | Each instance appends, never overwrites |
| **Provenance tracking** | `<!-- last-updated-by -->` marker on each document |
| **Harvest concatenation** | `harvest --healthcheck` merges indexes from all satellites |
| **Conflict resolution** | Most recent `last-updated` timestamp wins |

---

## 12. Project Required Assets

| Asset | Core (P0) | Child (P1+) | Purpose |
|-------|-----------|-------------|---------|
| `CLAUDE.md` | Full (~2600 lines) | Critical-subset (~180 lines) | Behavioral DNA |
| `notes/` | Session notes | Session notes | Ephemeral memory |
| `projects/<name>.md` | In core repo | Registered in core | Project metadata |
| Publications source | `publications/<slug>/v1/` | Optional | Canonical content |
| Docs web pages | `docs/publications/<slug>/` | Optional | GitHub Pages |
| GitHub Project | Not yet created | Not yet created | Platform tracking |
| `minds/<name>.md` | N/A (self) | In core repo | Harvested knowledge |
| `live/` | Knowledge assets | Synced from core | Tooling |

---

## 13. Project Lifecycle

```
discover -> register -> bootstrap -> create (platform) -> publish -> harvest -> evolve
```

| Phase | What happens | Command |
|-------|-------------|---------|
| **Discover** | New satellite or project conceived | Manual or `harvest --healthcheck` |
| **Register** | P# ID assigned, `projects/<name>.md` created | `project register <name>` |
| **Bootstrap** | CLAUDE.md, notes/, live/, knowledge pointer | `wakeup` step 0.5 |
| **Create** | GitHub Project board + web presence | `project create <name>` |
| **Publish** | Publications created and indexed | `pub new <slug>` |
| **Harvest** | Knowledge flows back to core | `harvest <project>` |
| **Evolve** | Evolution log grows, stories accumulate | Continuous |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-02-22 | Initial publication — project entity model, indexing, commands, bootstrap, web presence, tagged input |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
