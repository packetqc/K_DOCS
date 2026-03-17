# knowledge-live — Harvested Knowledge

> Last harvest: 2026-02-24
> Source: [packetqc/knowledge-live](https://github.com/packetqc/knowledge-live)
> Default branch: master

## Satellite Status

| Field | Value |
|-------|-------|
| Knowledge version | v39 |
| Core version | v47 |
| Drift | 8 🔴 |
| Bootstrap | Active (CLAUDE.md references packetqc/knowledge) — critical-subset (~230 lines) |
| Sessions | 7 (session-2026-02-20, session-2026-02-22, session-2026-02-23, session-2026-02-23-b, session-2026-02-23-c, session-2026-02-24, v39-hosted-project-design) |
| Assets | Deployed (live/ fully synced — beacon w/ PQC integration, scanner, stream_capture + scripts/ — gh_helper 1494 lines, pqc_envelope, sync_roadmap) |
| Live instances | 0 |
| Publications | 1 (#1 GitHub Project Integration — three-tier bilingual, source + EN/FR summary + complete) |
| Health | Healthy |
| Docs | Full web presence (layouts, landing pages EN/FR, publications hub, plan pages EN/FR, publication #1 pages) |
| Managed projects | 11 (P6 Export Documentation, P7-P9 test child, P10-P15 test managed, P16 Project documentation) |
| GitHub Project board | #37 (P3 Knowledge Live — 19 items, 16 Done / 1 In Progress / 1 Todo) |
| Missing features | v40–v47: proxy deep mapping v2, gh_helper sole API method, wakeup dedup, interactive input convention, token zero-display, environment-only delivery, production/development tiers |

## Bootstrap Event

- **Date**: 2026-02-20
- **Branch**: `claude/wakeup-functionality-ZBS4k` (initial), `claude/wakeup-functionality-f4qEi` (follow-up), `claude/wakeup-functionality-32xlp` (critical-subset upgrade)
- **Method**: Autonomous wakeup scaffold (step 0.5) — CLAUDE.md, README, LICENSE, .gitignore, notes/, live/ all created automatically
- **PR**: #1 (web presence scaffold), #2 (live assets sync), #3 (critical-subset upgrade) — all merged to master
- **Observation**: First satellite bootstrapped after v25 autonomous change detection fix. CLAUDE.md upgraded from thin-wrapper to critical-subset (v31) via PR #3.

## Self-Heal History

- **2026-02-22**: v31 → v36 (PR #4 — self-heal commands section via satellite-commands.md template)
- **2026-02-22**: v36 → v37 (PR #6 — full-read instruction for core CLAUDE.md added)
- **2026-02-22**: v37 → v39 (PR #7 — evolution stage type added to commands)

## Normalize History

- **2026-02-23**: `normalize --fix` applied — created PLAN.md, LINKS.md, NEWS.md (PR #15 merged). Flagged `projects/export-documentation/` subfolder for manual migration to flat `.md`.

## P6 Managed Project — Export Documentation

- **Created**: 2026-02-22 (PR #8 — `b5c2e4c`)
- **Type**: managed (in P3/knowledge-live)
- **Path**: `projects/export-documentation/`
- **Scaffold**: README.md, docs/.gitkeep, notes/.gitkeep, assets/.gitkeep
- **Host CLAUDE.md**: Updated with "Managed Projects" section listing P6
- **Design spec**: `notes/v39-hosted-project-design.md` — complete operationalization design
- **First instance**: The first managed project in the knowledge network
- **Success story**: Validates the managed project architecture (v35 concept → v39 operationalization)

## P16 Managed Project — Project Documentation (NEW)

- **Created**: 2026-02-23 (session C, branch `claude/create-project-docs-tJACS`)
- **Type**: managed (in P3/knowledge-live)
- **Path**: `projects/project-documentation.md`
- **Content**: Consolidates GitHub Project integration methodology knowledge from branch `claude/create-new-project-kXoLe`
- **Covers**: TAG: convention, entity convention, bidirectional bridge, item model, engineering requirements, quality candidate Intégré
- **PR**: #35 merged to master

## Test Projects (P7–P15)

Extensive `project create` testing across sessions 2026-02-23 and 2026-02-23-b:

| ID | Name | Type | Board | PR |
|----|------|------|-------|----|
| P7 | Test project 3 | child | #26 | #12 merged |
| P8 | Test project 4 | child | #27 | #16 merged |
| P9 | Test project 5 | child | #28 | #17 merged |
| P10 | Project test 101 | managed | #30 | #19 merged |
| P11 | Project test 102 | managed | #31 | #20 merged |
| P12 | Project test 200 | managed | — | #21 merged |
| P13 | Project test 201 | managed | — | #22 merged |
| P14 | Project test 300 | managed | #34 | #23 merged |
| P15 | Project test 500 | managed | #36 | #24 merged |

**Observation**: These are test projects validating the `project create` pipeline. P7-P9 are child projects with GitHub repos. P10-P15 are managed projects in knowledge-live. All boards linked to repos via `linkProjectV2ToRepository`.

## Publication #1 — GitHub Project Integration (NEW)

- **Created**: 2026-02-23 (session B, branch `claude/create-new-project-kXoLe`)
- **Three-tier bilingual**: Source + EN/FR summary + EN/FR complete
- **Source**: `publications/github-project-integration/v1/README.md` (311 lines)
- **EN docs**: `docs/publications/github-project-integration/index.md` + `full/index.md`
- **FR docs**: `docs/fr/publications/github-project-integration/index.md` + `full/index.md`
- **Content**: TAG: convention, bidirectional flow, entity convention, engineering requirements, quality candidate Intégré, gh_helper.py command spec
- **Cross-references**: All 4 pages link to board #37, methodology spec, repo issue #30
- **PRs**: #28 (docs), #33 (cross-references)

## GitHub Project Board #37 — P3 Knowledge Live (NEW)

- **Created**: 2026-02-23 (session B, PR #29)
- **Linked**: to knowledge-live repo via `linkProjectV2ToRepository`
- **Items**: 19 total (16 Done, 1 In Progress, 1 Todo)
- **TAG: labels deployed**: 9 types on knowledge-live repo
- **Item types**: METHODOLOGY: (3), PATTERN: (2), LESSON: (2), EVOLUTION: (1), STORY: (3), TASK: (4), PUB: (1), HARVEST: (2)

### Board Items (key items)

| TAG: | Title | Status |
|------|-------|--------|
| STORY: | Build gh_helper.py project item commands | Done |
| STORY: | Implement harvest from GitHub Project boards | In Progress |
| STORY: | Autonomous documentation authorship — Claude as sole author | Todo |
| METHODOLOGY: | GitHub Project bidirectional integration | Done |
| METHODOLOGY: | TAG: convention for knowledge structure mirroring | Done |
| METHODOLOGY: | Date-based bidirectional state sync | Done |

## gh_helper.py Evolution (NEW — session 2026-02-23-b + 2026-02-24)

The satellite's `gh_helper.py` has grown from the core version (~800 lines) to **1494 lines** with significant new capabilities:

### New Commands (session 2026-02-23-b)

| Command | Type | Description |
|---------|------|-------------|
| `labels setup --repo` | REST | Creates all 9 TAG: labels (idempotent) |
| `labels list --repo` | REST | Lists repo labels |
| `labels setup-all --repos` | REST | Batch setup of 9 TAG: labels across multiple repos |
| `issue create --repo --title --labels` | REST | Creates repo issue with TAG: prefix + label |
| `project item-add --project-id --title` | GraphQL | Adds draft items to board (`addProjectV2DraftIssue`) |
| `project get-id --owner --number` | GraphQL | Retrieves board node ID |
| `project item-update --item-id --status` | GraphQL | Updates board item status field (Todo/In Progress/Done) |
| `project fields --project-id` | GraphQL | Lists board fields and their option values |

### New Commands (session 2026-02-24)

| Command | Type | Description |
|---------|------|-------------|
| `project items-list` | GraphQL | Paginated board reader with TAG: parsing, timestamps, summary by status and tag |
| `project sync` | GraphQL + local | Bidirectional reconciliation: fetch board state, compare with local JSON, produce diff report |
| `labels setup-all` | REST | Batch TAG: label deployment across comma-separated repo list |

### TAG: Labels Deployment

32 labels created across 4 repositories (session 2026-02-24):
- packetqc/test-project-3: 8 new + 1 existed
- packetqc/test-project-4: 8 new + 1 existed
- packetqc/test-project-5: 8 new + 1 existed
- packetqc/knowledge: 8 new + 1 existed
- packetqc/knowledge-live: all 9 existed (from prior session)

## New Scripts (NEW)

### sync_roadmap.py

- **Path**: `scripts/sync_roadmap.py` (183 lines)
- **Purpose**: Syncs GitHub Project board → Jekyll `_data/roadmap.json`
- **Mechanism**: Pulls all items from Projects v2 board, categorizes into Ongoing/Planned/Forecast tiers, writes JSON data file for Liquid templates
- **Trigger**: Manual run or GitHub Actions (`.github/workflows/sync-roadmap.yml`)
- **Design**: Board is single source of truth → script is bridge → static docs site

### GitHub Actions Workflow

- **Path**: `.github/workflows/sync-roadmap.yml` (35 lines)
- **Purpose**: Automated roadmap sync from board to docs
- **Trigger**: Schedule or manual

## Dynamic Roadmap Web Pages (NEW)

- **EN**: `docs/plan/index.md` — board-driven publication pipeline
- **FR**: `docs/fr/plan/index.md` — same, French
- **Data**: `docs/_data/roadmap.json` (427 items)
- **Purpose**: Live roadmap published on GitHub Pages, fed from board #37

## Stranded Branches

5 branches with unmerged work:

| Branch | Content | Status |
|--------|---------|--------|
| `claude/create-new-project-ovT9p` | P12 attempt (no PAT) | Superseded |
| `claude/create-new-project-qg1xY` | P10 attempt (early version) | Superseded |
| `claude/create-new-project-uehkE` | P12 attempt (child registration) | Superseded |
| `claude/create-test-project-QAoMw` | P7 attempt (early version) | Superseded |
| `claude/create-new-project-kXoLe` | 2 unmerged commits (success story + issue tracking) | Active work |

## Knowledge Inventory

| Check | Status |
|-------|--------|
| CLAUDE.md references packetqc/knowledge | Yes |
| notes/ exists with session files | Yes (7 sessions + 1 design spec + board-state.json) |
| live/ synced from knowledge | Yes (beacon w/ PQC, scanner, stream_capture, dynamic/, static/) |
| scripts/ synced from knowledge | Yes (gh_helper.py 1494 lines, pqc_envelope.py, sync_roadmap.py) |
| Own patterns/ or methodology/ | No (methodology knowledge embedded in P16 metadata + publication #1) |
| publications/ with content | Yes (#1 GitHub Project Integration — source + docs EN/FR) |
| docs/ web presence | Yes (full — layouts, landing pages, publications hub + #1, plan pages, projects hub) |
| projects/ with managed guests | Yes (P6 + P10-P16 managed + P7-P9 child refs) |
| Essential files | Yes (PLAN.md, LINKS.md, NEWS.md) |
| GitHub Actions | Yes (.github/workflows/sync-roadmap.yml) |

## Branch Cursors

| Branch | HEAD | Date |
|--------|------|------|
| master | c0c8453a52e724c3f6207e8808393def55603610 | 2026-02-24 |
| claude/create-new-project-kXoLe | 7823f54177242e9f22cf978d759f4c1938b5271b | 2026-02-24 (2 unmerged) |

## Evolved Patterns

### 1. Evolution relay methodology (#0:methodology:evolution-relay)
**Origin**: Session 2026-02-22, branch `claude/wakeup-functionality-hNWiF`
**Status**: ✅ **promoted** (v39 — evolution stage type added to harvest pipeline)

Satellite sessions discover evolution-worthy insights but have no formal path to deliver them to core. The existing `harvest --stage` pipeline accepts `lesson | pattern | methodology | docs` — no `evolution` type. Proposed design:
- New harvest stage type: `evolution` — `harvest --stage N evolution`
- Evolution relay document convention: `notes/evolution-v<NN>-<slug>.md` pattern
- New flag: `remember evolution:` alongside existing `remember harvest:`
- Autonomous cross-monitoring between elevated sessions (core + satellite)
- Both sessions must be elevated for autonomous flow; non-elevated falls back to Human Bridge

### 2. Managed projects design (#0:principle:managed-projects)
**Origin**: Session 2026-02-22, file `notes/v39-hosted-project-design.md`
**Status**: ✅ **promoted** — P6 created on satellite, core registry updated

Complete design spec for operationalizing the managed project type:
- Managed type marker: `<!-- project-type: managed -->`
- Managed projects always link their board to a repo (host repo or core repo)
- Harvest routing: content from managed projects routes to correct P#, not host's
- First instance: P6 "Export Documentation" managed in P3 (knowledge-live)
- Decision matrix: managed vs child guided by AskUserQuestion
- Normalize integration: managed project consistency checks

### 3. Autonomous convergence principle (#0:principle:autonomous-convergence)
**Origin**: Session 2026-02-22, scoped note
**Status**: 🔍 harvested

Elevated sessions (core + satellite) should converge evolution autonomously without human relay. When both sessions have L2 tokens, the pipeline completes: satellite discovers → saves → PR merges → core harvests → stages → promotes → satellite wakeup sees the update. The Human Bridge remains for non-elevated sessions.

### 4. Beacon PQC integration (asset sync)
**Origin**: Session 2026-02-22, PR #9
**Status**: 🔍 harvested

Satellite synced updated `live/knowledge_beacon.py` from core: 10,779 → 12,182 bytes. PQC auto-detection, crypto identity payload, `--secure` CLI flag. Protocol v0 → v1. All other assets current.

### 5. GitHub Project bidirectional integration methodology
**Origin**: Session 2026-02-23-b, branch `claude/create-new-project-kXoLe`
**Status**: 🔍 harvested

Major architectural insight: GitHub Projects have **two primitive item types** — Issues and Pull Requests. Three touch points for knowledge integration:
1. **Board issues** — planning layer (Claude creates via `addProjectV2DraftIssue`)
2. **Repo issues** — tracking layer (linked to board via `addProjectV2Item`)
3. **Repo PRs** — delivery layer (auto-linked when session `save` creates PR)

The knowledge system becomes the **bridge** between GitHub's native tracking (issues/PRs) and rich technical documentation:
- **GitHub** = collaboration layer (human decisions, reviews, tracking)
- **Knowledge** = intelligence layer (methodology, patterns, documentation)

### 6. TAG: convention for knowledge structure mirroring
**Origin**: Session 2026-02-23-b, branch `claude/create-new-project-kXoLe`
**Status**: 🔍 harvested

Replicate knowledge's project structure into GitHub using **issues with labels + TAG: title prefix**:

| TAG: prefix | Knowledge origin | GitHub label |
|-------------|-----------------|--------------|
| `METHODOLOGY:` | `#N:methodology:` | `methodology` |
| `PATTERN:` | `patterns/` | `pattern` |
| `LESSON:` | `lessons/` | `lesson` |
| `EVOLUTION:` | CLAUDE.md evolution table | `evolution` |
| `STORY:` | `#N:story:` | `story` |
| `TASK:` | `#N:task:` | `task` |
| `BUG:` | `#N:bug:` | `bug` |
| `PUB:` | `publications/` | `publication` |
| `HARVEST:` | `minds/` harvest flag | `harvest` |

Bidirectional: Knowledge → GitHub (auto-create issues) and GitHub → Knowledge (harvest reads issues).

### 7. Entity convention for typed project items
**Origin**: Session 2026-02-23-b, branch `claude/create-new-project-kXoLe`
**Status**: 🔍 harvested

New scoped note types: `#N:story:<title>`, `#N:task:<title>`, `#N:bug:<title>` — auto-create GitHub issue + board item. Maps 1:1 with TAG: convention labels.

### 8. Quality candidate "Intégré" (#13)
**Origin**: Session 2026-02-23-b, branch `claude/create-new-project-kXoLe`
**Status**: 🔍 harvested

The system integrates with external platforms (GitHub Projects, Issues, PRs) rather than replacing them. GitHub is the collaboration layer, knowledge is the intelligence layer. Proposed as the 13th core quality.

### 9. gh_helper.py board reader + bidirectional reconciliation (NEW)
**Origin**: Session 2026-02-24, branch `claude/create-new-project-kXoLe`
**Status**: 🔍 harvested

Three new commands implementing the read phase of bidirectional sync:
- `project items-list` — paginated GraphQL query, TAG: parsing, status+tag summary
- `project sync` — date-based reconciliation (new/updated/removed/in_sync detection)
- `labels setup-all` — batch TAG: label deployment across multiple repos

First `project sync` baseline: 17 items captured, second sync correctly detected 2 new + 2 updated + 15 in sync. Local state in `notes/board-state.json`.

### 10. Dynamic roadmap — board-driven web publication (NEW)
**Origin**: Session 2026-02-23-b + 2026-02-24, branches `claude/create-new-project-kXoLe` + `claude/create-new-project-sZaSZ`
**Status**: 🔍 harvested

`sync_roadmap.py` pulls board items → writes `docs/_data/roadmap.json` → Jekyll Liquid templates render a live roadmap page. GitHub Actions workflow automates the sync. Board is single source of truth for project planning → docs site reflects live state.

### 11. Autonomous proof — zero-manual GitHub UI (NEW)
**Origin**: Session 2026-02-23-b, cumulative evidence across PRs #24-#36
**Status**: 🔍 harvested

Complete autonomous cycle proved: 9 TAG: labels created, 19 board items populated, 1 repo issue (#30), Publication #1 created (6 pages), 13 PRs merged, status field updates, board reader + sync — all without manual GitHub UI intervention. Foundation for autonomous documentation authorship.

## New Pitfalls

### 1. `addProjectV2Item` vs `addProjectV2DraftIssue` confusion
**Origin**: Session 2026-02-23-b
`addProjectV2Item` requires linking an **existing** issue or PR (by content node ID). `addProjectV2DraftIssue` creates a **new** board-level draft item. Using the wrong one causes confusing errors.

### 2. HTTP response handling in gh_helper.py
**Origin**: Session 2026-02-23-b
Always check status codes from GitHub API. Gateway errors (502/503) need retry with backoff. Token errors (401) need user guidance. Validation errors (422) need field-level parsing.

## Promotion Candidates

| # | Insight | Origin | Type | Status |
|---|---------|--------|------|--------|
| 1 | Evolution relay methodology — new `evolution` stage type for harvest | Session 2026-02-22 | evolution | ✅ **promoted** (v39) |
| 2 | Managed projects — subfolder scaffold, harvest routing, board always linked to repo | Session 2026-02-22 | methodology | ✅ **promoted** (P6 created, core updated) |
| 3 | Autonomous convergence — elevated sessions converge without human relay | Session 2026-02-22 | pattern | 🔍 harvested |
| 4 | Beacon PQC integration — protocol v0→v1, --secure flag, crypto identity | Session 2026-02-22 | docs | 🔍 harvested |
| 5 | GitHub Project bidirectional integration — issues/PRs as bridge between collaboration and intelligence | Session 2026-02-23-b | methodology | ✅ **promoted** (methodology/github-project-integration.md) |
| 6 | TAG: convention — prefix issue titles with knowledge structure type + matching GitHub labels | Session 2026-02-23-b | methodology | ✅ **promoted** (methodology/github-project-integration.md) |
| 7 | Entity convention — #N:story/#N:task/#N:bug for typed project items with GitHub sync | Session 2026-02-23-b | methodology | ✅ **promoted** (methodology/github-project-integration.md) |
| 8 | Quality candidate "Intégré" — external platform integration as 13th core quality | Session 2026-02-23-b | evolution | ✅ **promoted** (CLAUDE.md quality #13) |
| 9 | gh_helper.py board reader + bidirectional reconciliation | Session 2026-02-24 | methodology | ✅ **promoted** (scripts/gh_helper.py 836→1494 lines) |
| 10 | Dynamic roadmap — board-driven web publication pipeline | Session 2026-02-24 | methodology | ✅ **promoted** (scripts/sync_roadmap.py + methodology/) |
| 11 | Autonomous proof — zero-manual GitHub UI intervention cycle | Session 2026-02-23-b | pattern | ✅ **promoted** (methodology/github-project-integration.md) |

## Harvest Flags

- `remember harvest: Cross-repo evolution delivery gap discovered — harvest --stage has no 'evolution' type. Satellites cannot formally propose CLAUDE.md evolution entries through the pipeline. Proposed: evolution-relay methodology with notes/evolution-*.md convention, remember evolution: flag, and autonomous cross-monitoring between elevated sessions.`
- `remember evolution: v40 — Evolution relay pipeline. New harvest stage type 'evolution' for satellite→core CLAUDE.md delivery. Autonomous convergence when both sessions elevated. Pull-based architecture preserved.`
- `harvest: GitHub Project bidirectional integration methodology — issues and PRs as two primitive item types bridging human and machine work`
- `harvest: TAG: convention — prefix issue titles with knowledge structure type (METHODOLOGY:, PATTERN:, LESSON:, etc.) + matching GitHub labels for taxonomy mirroring`
- `harvest: GitHub Project item model — board issues (planning) vs repo items (issues + PRs) as three touch points for knowledge integration`
- `harvest: Entity convention #N:story/#N:task/#N:bug for typed project items with GitHub sync`
- `harvest: New quality candidate "Intégré" — external platform integration as a core quality`
- `harvest: project items-list — paginated GraphQL board reader with TAG: parsing`
- `harvest: project sync — date-based bidirectional reconciliation (read phase)`
- `harvest: labels setup-all — batch TAG: label deployment across satellite network`
- `harvest: Dynamic roadmap — board-driven web publication via sync_roadmap.py + GitHub Actions`
- `harvest: Autonomous proof — 19 board items, 9 labels, 13 PRs, 6 doc pages, zero manual UI`
- `evolution: GitHub Project integration as bidirectional bridge between collaboration (GitHub) and intelligence (knowledge)`
- **Delivery status**: Flags #1-2 processed (promoted). Flags #3-11 harvested — pending review/promotion. User requested fast promotion to core.
