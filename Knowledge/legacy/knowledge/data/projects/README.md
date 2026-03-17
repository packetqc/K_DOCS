# Projects — First-Class Entities in Knowledge

<!-- project-index-version: v1 -->
<!-- knowledge-version: v47 -->

---

## What Is a Project

A **project** is a concrete entity that exists simultaneously at three levels:

| Level | What it means | Example |
|-------|--------------|---------|
| **Logical** | An organized body of work with publications, documentation, evolution, stories | Knowledge System (P0) |
| **Physical** | One or more Git repositories (satellites) that implement the project — or **none** for managed projects | `packetqc/knowledge`, `packetqc/MPLIB`, or core-only |
| **Platform** | A GitHub Project board for tracking issues, milestones, and progress | GitHub Project entity (created with `project create` when elevated) |

A project is **not** a repository. A project **has** repositories — or has **none**. The core project (P0) has 1 repository. A child project may have 1 or more satellite repositories. A **managed** project has no repository — it exists entirely within knowledge core for documentation and management. The project entity ties them all together.

### Project Types

| Type | Has repos? | Where it lives | Use case |
|------|-----------|----------------|---------|
| **core** | Yes (knowledge) | Self | Knowledge itself (P0) |
| **child** | Yes (satellites) | Own repos + metadata in core | Software projects with code repositories |
| **managed** | Optional (host repo) | Core metadata + optional host repo | Documentation, processes, cross-cutting concerns — board always links to a repo |

**Managed projects** — exist for documentation and management without a dedicated repository. They get a P# ID, a `projects/<slug>.md` metadata file, publications, documentation, and a GitHub Project board. The board always links to a repo: either the current/host repo (e.g., P6 links to knowledge-live) or the core repo as fallback. Managed projects may live as subfolders in a host repo (`managed-in-repo` marker) or purely in core. Every project links to a repo — no exceptions.

---

## Project Hierarchy

```
P0: Knowledge (core)
├── P1: MPLIB (child)
│   └── S: packetqc/MPLIB
│   └── S: packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE
├── P2: STM32 PoC (child)
│   └── S: packetqc/STM32N6570-DK_SQLITE
├── P3: knowledge-live (child)
│   └── S: packetqc/knowledge-live
├── P5: PQC (child — pre-bootstrap)
│   └── S: packetqc/PQC
```

**Core vs child**: Knowledge (P0) is the core project — it owns the methodology, the publications system, and the distributed network. All other projects are **children** that use Knowledge. They are independent projects that benefit from the core's methodology, not sub-components of the core.

**MPLIB relationship**: MPLIB (P1) is a **child project** — the original proof-of-concept that proved Knowledge works. It has its own publications, its own satellites, its own evolution. It is not a core asset; it is a core success story.

---

## Indexing Scheme

Hierarchical indexing with 3 levels: project / satellite / document.

### Project Index (Level 1)

Every project gets a unique identifier: `P<n>`.

| ID | Project | Type | Repository | Board |
|----|---------|------|------------|-------|
| P0 | Knowledge System | core | packetqc/knowledge | [#4](https://github.com/users/packetqc/projects/4) |
| P1 | MPLIB | child | packetqc/MPLIB | [#5](https://github.com/users/packetqc/projects/5) |
| P2 | STM32 PoC | child | packetqc/STM32N6570-DK_SQLITE | [#6](https://github.com/users/packetqc/projects/6) |
| P3 | knowledge-live | child | packetqc/knowledge-live | [#7](https://github.com/users/packetqc/projects/7) |
| P4 | MPLIB Dev Staging | child | packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE | [#8](https://github.com/users/packetqc/projects/8) |
| P5 | PQC | child | packetqc/PQC | [#9](https://github.com/users/packetqc/projects/9) |

**Managed projects** link to a host repo (or core repo as fallback):

| ID | Project | Type | Repository (linked) | Board |
|----|---------|------|---------------------|-------|
| P6 | Export Documentation | managed | packetqc/knowledge-live (`projects/export-documentation/`) | [#10](https://github.com/users/packetqc/projects/10) |
| P8 | Documentation System | managed | packetqc/knowledge | [#38](https://github.com/users/packetqc/projects/38) |
| P9 | Knowledge Compliancy Report | managed | packetqc/knowledge | [#43](https://github.com/users/packetqc/projects/43) |
| P10 | Test spontaneous | managed | packetqc/knowledge | [#47](https://github.com/users/packetqc/projects/47) |
| P11 | Test project 3454 | managed | packetqc/knowledge | [#48](https://github.com/users/packetqc/projects/48) |
| P12 | 9876 | managed | packetqc/knowledge | [#49](https://github.com/users/packetqc/projects/49) |
| P13 | Studio 54 | managed | packetqc/knowledge | [#50](https://github.com/users/packetqc/projects/50) |
| P14 | Project version code order 66 | managed | packetqc/knowledge | X |
| P15 | Project skills loaded at start | managed | packetqc/knowledge | X |
| P16 | Level Up v100 | managed | packetqc/knowledge | [#53](https://github.com/users/packetqc/projects/53) |

### Satellite Index (Level 2)

When a project has multiple repositories: `P<n>/S<m>`.

| Index | Satellite | Repository |
|-------|-----------|------------|
| P1/S1 | MPLIB main | packetqc/MPLIB |
| P1/S2 | MPLIB dev staging | packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE |

### Document Index (Level 3)

Publications and documents within a project: `P<n>/#<pub>` or `P<n>/S<m>/D<k>`.

| Index | Document | Location |
|-------|----------|----------|
| P0/#0 | Knowledge | core |
| P0/#1 | MPLIB Storage Pipeline | core (→P1) |
| P0/#2 | Live Session Analysis | core |
| P0/#3 | AI Session Persistence | core |
| P0/#4 | Distributed Minds | core |
| P0/#4a | Knowledge Dashboard | core |
| P0/#5 | Webcards & Social Sharing | core |
| P0/#6 | Normalize | core |
| P0/#7 | Harvest Protocol | core |
| P0/#8 | Session Management | core |
| P0/#9 | Security by Design | core |
| P0/#10 | Live Knowledge Network | core (→P3) |
| P0/#11 | Success Stories | core |

**Cross-project marker** `→P<n>`: When a publication in one project documents another project, the cross-reference is shown. `P0/#1 →P1` means publication #1 lives in P0 (core) but documents P1 (MPLIB). `P0/#10 →P3` means #10 documents P3 (knowledge-live).

### Display Convention

In inventories, the project index appears **left of the status tag**:

```
P0/#0    🟢  Knowledge
P0/#1    🟢  MPLIB Storage Pipeline           →P1
P0/#2    🟢  Live Session Analysis
P0/#3    🟢  AI Session Persistence
P0/#4    🟢  Distributed Minds
P0/#4a   🟢  Knowledge Dashboard
P0/#5    🟢  Webcards & Social Sharing
P0/#6    🟢  Normalize & Structure Concordance
P0/#7    🟢  Harvest Protocol
P0/#8    🟢  Session Management
P0/#9    🟢  Security by Design
P0/#10   🟢  Live Knowledge Network           →P3
P0/#11   🟢  Success Stories
```

---

## Multi-Instance Updates

Multiple Claude Code instances can update the same project's content concurrently. The convergence protocol:

1. **Each instance** works on its own `claude/<task-id>` branch
2. **Each instance** commits and pushes to its task branch
3. **PRs** deliver work to the project's default branch
4. **Merge order** resolves conflicts (PR-by-PR)
5. **Next harvest** aggregates all merged content

Indexation from multiple instances is **combined/concatenated** — not overwritten. If satellite S1 contributes document D1 and satellite S2 contributes document D2, both appear in the project index after harvest.

### Concurrent Index Markers

Each document carries a provenance marker showing where it was last updated:

```markdown
<!-- project-index: P0/#7 -->
<!-- last-updated-by: knowledge/claude/fix-harvest-xyz -->
<!-- last-updated: 2026-02-22 -->
```

On harvest, these markers are read to build the combined index. If two instances update the same document, the more recent `last-updated` wins. Conflicts are flagged for review.

---

## Project Required Assets

Every project, whether core or child, must have these assets **by design**:

| Asset | Core (P0) | Child (P1+) | Managed | Purpose |
|-------|-----------|-------------|---------|---------|
| `CLAUDE.md` | Full (~2600 lines) | Critical-subset (~180 lines) | N/A (no dedicated repo) | Behavioral DNA |
| `notes/` | Session notes | Session notes | N/A (no dedicated repo) | Ephemeral memory |
| `projects/<name>.md` | In core repo | X (registered in core) | In core repo | Project metadata |
| Publications source | `publications/<slug>/v1/` | Optional | Optional | Canonical content |
| Docs web pages | `docs/publications/<slug>/` | Optional | Optional | GitHub Pages |
| GitHub Project | [#4](https://github.com/users/packetqc/projects/4) | Created per project | Created per project | Platform tracking |
| `minds/<name>.md` | N/A (self) | In core repo | N/A (no dedicated satellite) | Harvested knowledge |
| `live/` | Knowledge assets | Synced from core | N/A (no dedicated repo) | Tooling |
| Evolution log | In CLAUDE.md | In project.md | In project.md | History |
| Stories | In #11 + project.md | In project.md | In project.md | Validation |

**Managed projects** have no dedicated repo-level assets (`CLAUDE.md`, `notes/`, `live/`, `minds/`). Their identity exists in `projects/<slug>.md` and their content in publications and docs — all within knowledge core. Their GitHub Project board always links to a repo (host repo or core repo).

**X = not yet defined/created** — placeholder until harvesting and normalization sync this evolution.

---

## Project Lifecycle

**Child projects** (repo-backed):
```
discover → register → bootstrap → create (platform) → publish → harvest → evolve
```

**Managed projects** (core-only):
```
conceive → register → create (platform) → publish → evolve
```

| Phase | Child | Managed | Command |
|-------|-------|---------|---------|
| **Discover** | Satellite detected by harvest | — | `harvest --healthcheck` |
| **Conceive** | — | Project need identified | Manual |
| **Register** | P# ID + `projects/<name>.md` | P# ID + `projects/<name>.md` | `project register <name>` |
| **Bootstrap** | CLAUDE.md, notes/, live/ on satellite | N/A (no dedicated repo) | `wakeup` step 0.5 |
| **Create** | GitHub Project (linked to repo) + web presence | GitHub Project (linked to host/core repo) + web presence | `project create <name>` |
| **Publish** | Publications in core and/or satellite | Publications in core | `pub new <slug>` |
| **Harvest** | Knowledge flows back to core | N/A (already in core) | `harvest <project>` |
| **Evolve** | Evolution log grows | Evolution log grows | Continuous |

Managed projects skip bootstrap and harvest — there's no dedicated satellite to bootstrap and no external repo to harvest from. All content is authored directly in knowledge core. Their GitHub Project board links to the host repo (or core repo as fallback).

---

## File Per Project

Each project has a metadata file: `projects/<slug>.md`. Format:

```markdown
# Project: <Name>
<!-- project-id: P<n> -->
<!-- project-type: core|child|managed -->
<!-- project-status: active|pre-bootstrap|archived -->
<!-- github-project: X -->

## Identity
| Field | Value |
|-------|-------|
| **ID** | P<n> |
| **Name** | <Name> |
| **Type** | core / child |
| **Repositories** | <repo links> |
| **GitHub Project** | X |
| **Status** | active / pre-bootstrap |
| **Created** | YYYY-MM-DD |

## Publications
| Index | Title | Status |
|-------|-------|--------|

## Satellites
| Index | Name | Repository |
|-------|------|------------|

## Evolution
| Date | Entry |
|------|-------|

## Stories
| Date | Story |
|------|-------|
```

---

## URL Preservation

The project tree is **additive** — it adds `projects/` and `docs/projects/` without moving or renaming any existing file. All existing URLs are preserved:

| Existing URL | Status |
|-------------|--------|
| `/publications/<slug>/` | **Unchanged** — publications stay at their current permalinks |
| `/publications/<slug>/full/` | **Unchanged** |
| `/fr/publications/<slug>/` | **Unchanged** |
| `/profile/`, `/profile/resume/`, `/profile/full/` | **Unchanged** |
| `/assets/og/<card>.gif` | **Unchanged** |

**New URLs** (additive):

| New URL | Content |
|---------|---------|
| `/projects/` | EN project hub — project-centric navigation |
| `/fr/projects/` | FR project hub |

The project hub pages **link to** existing publication URLs — they don't replace them. This is a navigation layer on top of the existing structure.

---

## Deployment to Satellites

Satellites receive project management awareness on their **next wakeup** via the standard push mechanism:

1. Core evolves to v35 (this version) — adds project entity model
2. On satellite wakeup, step 0 reads core CLAUDE.md → gains project awareness
3. Step 0.5 checks for `projects/` structure → creates if missing (future)
4. Satellite's project.md is registered in core on next `harvest`

**Manual deployment** for satellites not yet restructured:

```
1. Open a Claude Code session in the satellite
2. Type: wakeup
3. The session reads v35 core → gains project awareness
4. Type: project register
5. The session creates the satellite's project entry
```

See `methodology/project-management.md` for the full deployment procedure.
