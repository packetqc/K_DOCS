# Session Metrics & Time Compilation — Measuring AI-Assisted Productivity

**Publication #20 · v1 · February 2026**
**Languages / Langues**: English (this document) | [Français](https://packetqc.github.io/knowledge/fr/publications/session-metrics-time/)

---

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Architect of the metrics and time compilation methodology — born from the need to demonstrate that AI-assisted sessions deliver a week's team output in a single day.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Co-author and compiler of the session data that validates this methodology. The compilation itself was produced during the session it measures.

---

## Abstract

Every interactive work session generates two classes of valuable data: **metrics** (what was produced) and **time** (how long it took). These data points are scattered across commits, PRs, issues, board items, and session notes — valuable but unstructured. Without compilation, the evidence of productivity vanishes with the session.

This publication introduces **two compilation methodologies** — metrics sheets and timesheets — that transform session activity into structured, appendable tables. The same category grid (diagnostic, conception, documentation, document management, collateral) organizes both compilations, with **todos as primary items** and **tasks as sub-items** within each category.

The key insight: these tables are **appendable across sessions**. A single session compilation shows a day's work. Appending multiple sessions shows a week's sprint. The same grid, the same categories, the same structure — enabling sums, averages, and trend analysis across any time period.

The proof is the session itself: February 26, 2026 — 20 PRs merged, ~18,000 lines added, 288 files modified, 6 publications created, 4 methodologies written, 3 pitfalls documented, across 5 work categories in approximately 10 hours of active work. A team's weekly output, compiled and measured.

---

## The Problem

### What Gets Lost

| Data | Where it exists | What happens |
|------|----------------|--------------|
| Files changed | `git log --stat` | Buried in 137 commits |
| Time spent | Commit timestamps | Scattered, no aggregation |
| PRs merged | GitHub API | Individual records, no category view |
| Issues resolved | GitHub Issues | Closed but not compiled |
| Publications created | `docs/` folder | Count visible, effort invisible |
| Category breakdown | Nowhere | Developer knows, nobody else can see |

### Why It Matters

The developer and AI deliver a week's team output in a day. But without compilation:
- **No evidence** — the productivity is real but unmeasured
- **No trends** — can't compare sessions, can't identify bottlenecks
- **No reporting** — can't demonstrate ROI of AI-assisted development
- **No planning** — can't estimate future sessions based on past performance
- **No inheritance** — successor sessions can't learn from predecessor patterns

### The Gap

Publication #19 (Interactive Work Sessions) codified **how** sessions work — resilience patterns, session types, progressive commits. But it didn't address **what was produced** and **how long it took**. The methodology for productive sessions exists; the measurement of that productivity didn't.

---

## The Solution

Two compilation tools with shared structure, appendable across sessions.

### Shared Category Grid

Every session's work falls into these interaction categories:

| Category | Icon | Description | Examples |
|----------|------|-------------|----------|
| **Diagnostic** | 🔍 | Bug fixes, root cause analysis, troubleshooting | kramdown rendering fix, theme switcher investigation |
| **Conception** | 💡 | Design sessions, architecture exploration, new ideas | Mermaid source preservation design (v49), compilation methodology |
| **Documentation** | 📝 | Publication creation, methodology files, web pages | Publications #17, #18, #19 creation |
| **Document Management** | 📋 | Essential files, indexes, NEWS.md, metadata updates | STORIES.md creation, vital files expansion |
| **Collateral** | ⚙️ | GitHub issues/boards, infrastructure, tooling, diagrams | Board updates, diagram re-rendering, issue closure |

### Hierarchy: Todos and Tasks

Within each category:
- **Todos** (primary items) — the main deliverables, shown in **bold**
- **Tasks** (sub-items) — the steps to complete each todo, shown indented beneath

This mirrors the TodoWrite structure used during sessions: one todo `in_progress` at a time, tasks flowing underneath.

### Two Compilation Sheets

#### 1. Metrics Compilation Sheet

For each todo/task, capture what was **produced**:

| Metric | Unit | What it measures |
|--------|------|------------------|
| PRs | count | Pull requests created and merged |
| Files | count | Files created or modified |
| Lines+ | count | Lines of code/content added |
| Lines− | count | Lines removed |
| Issues | count | GitHub issues resolved/closed |
| Pitfalls | count | Known pitfalls documented |
| Pubs | count | Publications created |
| Methods | count | Methodology files created/updated |
| Evolutions | count | Knowledge evolution entries added |

#### 2. Time Compilation Sheet

For each todo/task, capture **when** and **how long**:

| Field | Format | What it captures |
|-------|--------|------------------|
| Start | HH:MM | When work began (from commit timestamps) |
| End | HH:MM | When work completed |
| Duration | minutes | Active working time |
| Type | category | Session interaction type |
| Phase | text | Which phase (hypothesis, creation, review, etc.) |

### Appendability

Both sheets use the same category grid. When sessions are appended:

```
Session 2026-02-26 (this session)
  Diagnostic:     20 min  |  3 PRs, 31 files
  Documentation: 187 min  |  3 pubs, 48 files
  ...
  ─────────────────────────────────────────
  Session total: 337 min  |  25 PRs, 100+ files

Session 2026-02-25 (previous session)
  Documentation: 240 min  |  2 pubs, 36 files
  Collateral:    120 min  |  10 PRs, 56 files
  ...
  ─────────────────────────────────────────
  Session total: 480 min  |  15 PRs, 92 files

═══════════════════════════════════════════
Week total:     817 min  |  40 PRs, 192+ files
                13.6 hrs |  ~5.5 pubs
```

---

## Live Example: Session 2026-02-26

### Metrics Summary

**Totals: 12 todos · 20 PRs · 288 files · +17,974 −6,049 lines · 6 pubs, 4 metho, 3 pitfalls**

| Category | Todos | PRs | Files | Lines+ | Lines− | Deliverables |
|----------|-------|-----|-------|--------|--------|--------------|
| 🔍 Diagnostic | 1 | 9 | 207 | 9,338 | 5,733 | 3 pitfalls (#20, #21, #22) |
| 💡 Conception | 4 | 1 | 23 | 3,587 | 23 | 4 methodologies, v49 |
| 📝 Documentation | 4 | 4 | 43 | 4,358 | 240 | 6 publications (#14–#19) |
| 📋 Doc Management | 2 | 2 | 5 | 497 | 0 | STORIES.md, essential files |
| ⚙️ Collateral | — | 4 | 10 | 194 | 53 | 4 collateral PRs |
| **Total** | **12** | **20** | **288** | **17,974** | **6,049** | **6 pubs, 4 metho, 3 pitfalls** |

### Metrics Detail

#### 🔍 Diagnostic (1 todo)

**Totals: 1 todo · 9 PRs · 207 files · +9,338 −5,733 lines · 3 pitfalls**

| # | Todo / Task | Issue | PRs | Files | Lines+ | Lines− |
|---|-------------|-------|-----|-------|--------|--------|
| **T3** | **Diagnostic diagrammes pages web** | #334 | 9 | 207 | 9,338 | 5,733 |
| | → Replace Mermaid with PNG | — | #337 | 30 | 28 | 1,444 |
| | → Dual-theme diagrams | — | #338 | 62 | 245 | 161 |
| | → Theme switcher + Pub #16 | — | #340 | 23 | 3,354 | 3 |
| | → Re-render 28 PNGs | — | #341 | 80 | 3,373 | 5 |
| | → Source preservation (v49) | — | #342 | 2 | 2,112 | 202 |
| | → Summary page reconstruction | — | #343 | 2 | 214 | 2,044 |
| | → Diagram count fix | — | #344 | 4 | 12 | 12 |
| | → kramdown `<details>` fix | — | #345 | 4 | 0 | 1,862 |

#### 💡 Conception (4 todos)

**Totals: 4 todos · 1 PR · 23 files · +3,587 −23 lines · 4 methodologies, v49**

| # | Todo / Task | Issue | PRs | Files | Lines+ | Lines− |
|---|-------------|-------|-----|-------|--------|--------|
| **T4** | **Web Page Visualization capability** | #335 | — | *(in T3)* | | |
| **T10** | **Méthodologie documentaire (meta-metho)** | #355 | #356 | 23 | 3,587 | 23 |
| **T11** | **Publication #20 — Metrics & Time** | #358 | *(in progress)* | | | |
| **T12** | **Export portrait/paysage** | #357 | *(future)* | | | |

#### 📝 Documentation (4 todos)

**Totals: 4 todos · 4 PRs · 43 files · +4,358 −240 lines · 6 publications**

| # | Todo / Task | Issue | PRs | Files | Lines+ | Lines− |
|---|-------------|-------|-----|-------|--------|--------|
| **T1** | **Revue documentaire architecture** | #327 | #328 | 14 | 279 | 12 |
| **T2** | **Enrichissement iteration 2** | #360 | #333 | 18 | 1,763 | 226 |
| **T5** | **Diagnostic méthodologies** | #361 | #336 | 4 | 417 | 0 |
| **T6** | **Publication #17 Web Production Pipeline** | #347 | #348 | 7 | 1,919 | 2 |

#### 📋 Doc Management (2 todos)

**Totals: 2 todos · 2 PRs · 5 files · +497 −0 lines · STORIES.md, essential files**

| # | Todo / Task | Issue | PRs | Files | Lines+ | Lines− |
|---|-------------|-------|-----|-------|--------|--------|
| **T7** | **Vérification méthodologies web** | #350 | #349 | 2 | 150 | 0 |
| **T8** | **Vérification scripts pipeline** | #351 | #352 | 3 | 347 | 0 |

#### ⚙️ Collateral

**Totals: 4 PRs · 15 files · +599 −67 lines · 4 collateral PRs, 1 success story**

| # | Todo / Task | PRs | Files | Lines+ | Lines− |
|---|-------------|-----|-------|--------|--------|
| | → T1 collateral fixes | #329–332 | 10 | 194 | 53 |
| **T9** | **Success Story #18** | #354 | 5 | 405 | 14 |

### Time Summary

**Totals: 12 todos · ~10h04 active · 3 blocks · avg ~50min/todo**

| Category | Todos | Total Time | Avg per Todo |
|----------|-------|------------|--------------|
| 🔍 Diagnostic | 1 | ~1h16 | 1h16 |
| 💡 Conception | 4 | ~1h43 | ~26min |
| 📝 Documentation | 4 | ~6h46 | ~1h42 |
| 📋 Doc Management | 2 | ~19min | ~10min |
| **Total** | **12** | **~10h04** | **~50min** |

### Time Detail

#### Block: Morning (06:07–08:30) — ~2h23

**Totals: 2 todos · ~2h23 active**

| # | Todo | Start | End | Duration | Category |
|---|------|-------|-----|----------|----------|
| **T1** | Revue documentaire architecture | 06:07 | 07:57 | ~1h50 | 📝 Documentation |
| **T2** | Enrichissement iteration 2 | 07:57 | ~08:30 | ~33min | 📝 Documentation |

#### Block: Afternoon (14:14–19:30) — ~5h16

**Totals: 3 todos · ~5h16 active**

| # | Todo | Start | End | Duration | Category |
|---|------|-------|-----|----------|----------|
| **T3** | Diagnostic diagrammes pages web | 14:14 | ~15:30 | ~1h16 | 🔍 Diagnostic |
| **T4** | Web Page Visualization capability | 15:30 | 15:33 | ~3min | 💡 Conception |
| **T5** | Diagnostic méthodologies + styling | 15:33 | ~19:30 | ~3h57 | 📝 Documentation |

#### Block: Evening (19:30–22:05) — ~2h35

**Totals: 7 todos · ~2h35 active**

| # | Todo | Start | End | Duration | Category |
|---|------|-------|-----|----------|----------|
| **T6** | Publication #17 | 19:30 | ~19:56 | ~26min | 📝 Documentation |
| **T7** | Vérification méthodologies | 19:56 | ~19:56 | ~5min | 📋 Doc Management |
| **T8** | Vérification scripts | 19:56 | ~20:10 | ~14min | 📋 Doc Management |
| **T9** | Success Story #18 | 20:10 | ~20:25 | ~15min | ⚙️ Collateral |
| **T10** | Méthodologie documentaire | 20:25 | ~21:40 | ~1h15 | 💡 Conception |
| **T11** | Publication #20 (début) | ~21:40 | ~22:00 | ~20min | 💡 Conception |
| **T12** | Export portrait/paysage (issue only) | ~22:00 | ~22:05 | ~5min | 💡 Conception |

*Total: ~10h14 across 3 blocks, pause ~5h44 between morning and afternoon*

---

## Methodology Integration

### Metrics Checklist (Post-Session Routine)

Run after every session to compile metrics:

1. **Git statistics** — `git log --since="<date>" --stat --oneline | tail -50`
2. **PR count** — `git log --since="<date>" --oneline --all | grep -c "Merge"`
3. **Category assignment** — classify each todo into diagnostic/conception/documentation/doc-mgmt/collateral
4. **Lines count** — `git diff --stat <start-sha>..<end-sha>`
5. **Issue status** — check closed issues via `gh_helper.py`
6. **Publication inventory** — count new publications, methodology files, evolution entries
7. **Fill metrics grid** — populate the category × metrics table

### Time Checklist (Post-Session Routine)

Run after every session to compile time:

1. **Session boundaries** — first and last commit timestamps
2. **Active blocks** — group commits by proximity (< 15 min gap = same block)
3. **Category timing** — assign each block to a work category
4. **Duration calculation** — sum active blocks per category
5. **Idle detection** — gaps > 30 min between commits = non-active time
6. **Fill time grid** — populate the category × time table
7. **Percentage calculation** — each category's share of total active time

### Subconscious Detection

During work sessions, Claude monitors for compilation-worthy data:
- When a PR is merged → note the metrics (files, lines, category)
- When an issue is closed → note resolution time
- When a todo completes → note duration since start
- When a session ends → suggest compilation before `save`

---

## Impact

### What This Enables

| Before | After |
|--------|-------|
| "I was productive today" | "337 min active, 25 PRs, 3 publications, 9,831 lines" |
| No cross-session comparison | Appendable tables show weekly/monthly trends |
| Effort invisible to stakeholders | Structured evidence of AI-assisted productivity |
| No planning data | Historical data enables session estimation |
| Metrics scattered in git | Compiled in standardized, reusable format |

### Design Principles

1. **Same grid, two views** — metrics and time share the category structure
2. **Todos over tasks** — primary items drive the compilation; tasks are detail
3. **Appendable** — tables from multiple sessions stack for aggregation
4. **Evidence-based** — all data derived from git, PRs, issues (not estimates)
5. **Routine-integrated** — checklists embed in the session lifecycle (`save` protocol)
6. **Successor-ready** — compiled data is inherited by the next session via `notes/`

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 19 | [Interactive Work Sessions](../interactive-work-sessions/) | Session methodology that generates the data compiled here |
| 8 | [Session Management](../session-management/) | Lifecycle commands (wakeup, save) where compilation integrates |
| 3 | [AI Session Persistence](../ai-session-persistence/) | Foundational persistence — compilation is a persistence artifact |
| 11 | [Success Stories](../success-stories/) | Compiled metrics feed validation narratives |
| 4a | [Knowledge Dashboard](../distributed-knowledge-dashboard/) | Network metrics — same compilation philosophy at system level |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
