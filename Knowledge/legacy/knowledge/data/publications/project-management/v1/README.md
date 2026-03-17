# Publication #12 — Project Management

**First-Class Project Entities, Hierarchical Indexing, and Satellite Lifecycle**

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*v1 — February 2026*
*Knowledge version: v36*

---

## Abstract

Knowledge manages a growing network of repositories, publications, and AI sessions. As this network expanded from a single repo to 6+ projects with multiple satellites each, a structural gap emerged: **projects had no formal identity**. Repositories existed, publications existed, satellites existed — but the entity that ties them together (the project) was implicit. Publication #12 documents the v35 project entity model that makes projects explicit: hierarchical indexing (P#/S#/D#), three-level entity model (logical, physical, platform), dual-origin publishing, satellite lifecycle management, and the commands that operate on them.

This publication consolidates four methodology documents into a single reference:
- **Project Management** — entity model, indexing, commands, integration
- **Satellite Bootstrap** — single-session iterative staging protocol
- **Project Create** — web presence scaffolding for satellites
- **Tagged Input** — `#` call alias for scoped project knowledge

---

## Related Publications

| # | Publication | Relationship |
|---|------------|--------------|
| 0 | Knowledge | Parent — project management extends the core system |
| 4 | Distributed Minds | Architecture — projects organize the distributed network |
| 4a | Knowledge Dashboard | Dashboard — project status displayed in network view |
| 7 | Harvest Protocol | Collection — harvest operates on project-indexed content |
| 8 | Session Management | Lifecycle — sessions operate within project context |
| 11 | Success Stories | Validation — project milestones become stories |

---

## 1. Project Entity Model

A **project** is a first-class entity that exists at three levels:

| Level | What it means | Example |
|-------|--------------|---------|
| **Logical** | An organized body of work with publications, documentation, evolution, stories | Knowledge System (P0) |
| **Physical** | One or more Git repositories — or **none** for managed projects | `packetqc/knowledge`, `packetqc/MPLIB`, or core-only |
| **Platform** | A GitHub Project board for tracking issues, milestones, and progress | GitHub Project entity (when elevated) |

A project is **not** a repository — it **has** repositories, or has **none**. A project is **not** a publication — it **has** publications. The project entity ties everything together: identity, documentation, publications, evolution, stories, and platform presence.

### Project Relationships

| Relationship | Meaning | Example |
|-------------|---------|---------|
| **owns** | The project's primary repository | P0 owns `packetqc/knowledge` |
| **child-of** | A sub-project of a parent project | P1 (MPLIB) is child-of P0 |
| **managed** | No dedicated repository — lives in a host repo or core only | Documentation, processes, cross-cutting initiatives — board always links to a repo |

**Managed projects** have no dedicated code repository. They may live as subfolders in a host repo or purely in knowledge core. All content — publications, documentation, evolution, stories — is authored in the host or core repo. Their GitHub Project board always links to a repo: child projects link to their own repo, managed projects link to the host repo (or core repo as fallback). Every project links to a repo — no exceptions.

### Current Registry

| ID | Project | Type | Status |
|----|---------|------|--------|
| P0 | Knowledge System | core | active |
| P1 | MPLIB | child | active |
| P2 | STM32 PoC | child | active |
| P3 | knowledge-live | child | active |
| P4 | MPLIB Dev Staging | child (of P1) | active |
| P5 | PQC | child | pre-bootstrap |

### MPLIB Decoupling

MPLIB (P1) is reclassified from core asset to child project. The publications index title changed from "MPLIB Knowledge" to "Knowledge System". Publication #1 carries `P0/#1 ->P1` cross-ref. MPLIB is the original proof-of-concept — a core success story, not a core asset.

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

In all inventories and dashboards, the index appears **left of the status tag**:

```
P0/#0    Knowledge
P0/#1    MPLIB Storage Pipeline           ->P1
P0/#10   Live Knowledge Network           ->P3
P1/S1    MPLIB (v31)
P5/S1    PQC (v0, pre-bootstrap)
```

The `->P<n>` cross-reference marker indicates a publication that documents a different project than where it's published.

### Machine-Parseable Markers

```markdown
<!-- project-id: P<n> -->
<!-- project-type: core|child|managed -->
<!-- project-status: active|pre-bootstrap|archived -->
<!-- github-project: <url or X> -->
<!-- parent-project: P<n> -->
```

---

## 3. Project Commands

| Command | Action |
|---------|--------|
| `project list` | List all projects with P# index, type, status, satellite count |
| `project info <P#>` | Show project details — identity, publications, satellites, evolution, stories |
| `project create <name>` | Full creation: register P# + GitHub Project board (elevated, linked to repo) + web presence |
| `project register <name>` | Register a new project with P# ID — creates `projects/<slug>.md` |
| `project review <P#>` | Review project state — documentation, publications, required assets, freshness |
| `project review --all` | Review all projects |

### `project list` Output

```
=== Projects ===

  ID   Name                    Type     Status           Sats  Pubs  Health
  P0   Knowledge System        core      active            5     14    healthy
  P1   MPLIB                   child     active            2     1     healthy
  P2   STM32 PoC              child     active            1     1     healthy
  P3   knowledge-live          child     active            1     1     healthy
  P4   MPLIB Dev Staging       child     active            1     0     healthy
  P5   PQC                     child     pre-bootstrap     1     0     pending

  Total: 6 projects (5 active, 1 pre-bootstrap)
```

**Managed projects** show `—` in the Sats column (no satellites). Their health is determined by documentation completeness and management status:

```
  P6   (example)               managed   active            —     2     healthy
```

### `project review` Output

Audits a project against the required assets checklist: identity, CLAUDE.md, notes/, live/, publications, docs, GitHub Project, evolution, stories.

---

## 4. Satellite Bootstrap Protocol

Single-session iterative staging — one session does everything, user merges between rounds.

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

The session actively guides the user through every manual step. Never go silent between rounds — always print what happened, what the user needs to do, and what happens after.

### Round 1 — Bootstrap

Wakeup step 0.5 creates missing essential files (non-destructive, skip-if-exists):

| File | Content |
|------|---------|
| `CLAUDE.md` | Critical-subset (~180 lines): knowledge pointer + behavioral DNA + commands |
| `README.md` | Repo name, description, link to knowledge |
| `LICENSE` | MIT with current year |
| `.gitignore` | Standard ignores |
| `notes/.gitkeep` | Session persistence folder |

### Round 2 — Normalize

Trim the satellite CLAUDE.md to critical-subset form. Remove over-synced deep implementation content, keeping behavioral DNA: auto-wakeup protocol, session lifecycle, save protocol, branch protocol, human bridge, full 7-group commands reference.

### Round 3 — Project Create (Optional)

Scaffold web presence (docs/, layouts, hubs). Only needed if the satellite will produce documentation or publications.

### Critical-Subset Principle

The satellite CLAUDE.md carries enough DNA to drive correct behavior even after context compaction:

```
Core CLAUDE.md (2600+)     Full methodology, all implementations     <- source of truth
         |
         | read on wakeup (Step 0)
         |
Satellite CLAUDE.md (~180) Knowledge pointer + behavioral DNA        <- critical-subset
                           Session + save + branch protocol              (survives compaction)
                           Full 7-group commands reference
                           Project overview + commands
```

---

## 5. Web Presence Scaffolding (`project create`)

Creates a complete GitHub Pages + publication structure on a satellite:

```
<satellite-repo>/
  docs/
    _config.yml                    <- Jekyll config
    _layouts/
      default.html                 <- Copied from knowledge (Cayman/Midnight)
      publication.html             <- Copied from knowledge (version banner, keywords)
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

**10 files, 6 directories.** Everything needed for a bilingual GitHub Pages site with publication support. Layouts are copied (not referenced) — fully self-contained, no external theme dependency.

---

## 6. Tagged Input (`#` Call Alias)

The `#` prefix triggers scoped knowledge input mode. Claude routes, classifies, and stores the content.

| Command | Action |
|---------|--------|
| `#N: <content>` | Scoped note for publication/project #N |
| `#N:methodology:<topic>` | Methodology insight — flagged for harvesting |
| `#N:principle:<topic>` | Design principle — flagged for harvesting |
| `#N:info` | Show accumulated knowledge for #N |
| `#N:info:<topic>` | Show specific topic within #N |
| `#N:done` | End documentation focus, compile summary |

### Implicit Main Project

Every repo has a main project. When the user feeds information without `#N:` prefix, Claude assumes it's for the repo's main project. In `packetqc/knowledge`, the main project is `#0`.

### Raw Dump Mode

`#N:` accepts unstructured raw input. Claude uses acquired knowledge + universal knowledge to classify and route. Lowest-friction entry point.

### Multi-Satellite Convergence

The same project can be documented from multiple satellites. `#N:` is the routing key, not the repo — the insight goes where it belongs regardless of where it was discovered. Harvest pulls all distributed notes into `minds/`, promotion converges them into core.

---

## 7. Dual-Origin Link System

Publications exist across repos with independent GitHub Pages. The link origin indicates provenance:

| Origin | Badge | Base URL | Meaning |
|--------|-------|----------|---------|
| **Core** | **core** | `packetqc.github.io/knowledge/` | Reviewed, published, canonical |
| **Satellite** | *satellite* | `packetqc.github.io/<repo>/` | Development, staging, local |

Both are valid — same GitHub Pages technology, different review stage. Core links are stable. Satellite links are evolving.

---

## 8. GitHub Project Integration

When elevated (PAT with project scope), GitHub Project boards are created through two paths:

1. **`project create <name>`** — direct creation, immediate
2. **`harvest --promote N`** — when `project`-staged intel is promoted, auto-creates the board

Both paths create the GitHub Project board — the **human interface layer** where the AI-native knowledge system meets human-native project management.

| Knowledge system (AI-native) | GitHub Project (human-native) |
|------------------------------|-------------------------------|
| `projects/<slug>.md` metadata | Project board with cards |
| Evolution entries (v#) | Milestones |
| Harvest insights | Issues (auto-created from promotion candidates) |
| Session notes | Activity timeline |

---

## 9. Integration with Existing Commands

### harvest Integration

`harvest --healthcheck` includes project status. The dashboard shows project counts, satellite health, and publication distribution.

**Harvest-driven project creation**: The `project` stage type enables harvest to create managed projects when intel matures through the promotion pipeline:

```
harvest <satellite>                    # Discover intel
harvest --review N                     # Validate
harvest --stage N project              # Stage as project-grade
harvest --promote N                    # Auto-registers P# + creates GitHub Project (if elevated)
```

Two entry points for GitHub Project creation: `project create` (direct) and `harvest --promote` (when intel has been promoted through the full review → stage → promote pipeline). The promotion pipeline is the quality gate — only human-validated, explicitly staged intel triggers project creation.

### normalize Integration

`normalize` checks project concordance: registry consistency, unique P# assignments, valid cross-references, required assets, GitHub Project linkage.

### pub list Integration

`pub list` shows project index alongside publications — `P0/#1` with `->P1` cross-references.

### doc review Integration

`doc review --list` includes project index in freshness inventory.

---

## 10. URL Preservation

The project restructure is **additive** — no existing URLs change.

| What stays | What's new |
|-----------|------------|
| All publication permalinks | `/projects/` (EN project hub) |
| All profile page URLs | `/fr/projects/` (FR project hub) |
| All webcard URLs | |
| Landing page | |

The project hub provides a **navigation overlay** that links to existing URLs, organized by project. Two paths to the same content: by number (publications/) and by project (projects/).

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-02-22 | Initial publication — project entity model, indexing, commands, bootstrap, web presence, tagged input |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
