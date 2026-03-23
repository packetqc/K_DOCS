# Publication K2.0 Deep Review — Specifications

## Context

Phase 1 (mermaid diagram updates) completed 2026-03-16. Phase 2 is the full text content review: every publication must reflect K2.0 reality in all text, tables, descriptions, and references.

All 25 publications in `docs/publications/` are production K2.0 documentation. Only `legacy/knowledge/data/publications/knowledge-system/v1` is legacy.

## Review Principle

Each publication must answer for the audience: **What** (capability, how it works in K2.0), **Why** (problem solved, design decision), **Who** (which K2.0 module owns it), **Where** (scripts, skills, files), **When** (lifecycle: session start, every turn, on command, on save).

## K1.0 → K2.0 Reference Mapping

### Architecture

| K1.0 | K2.0 |
|------|------|
| Monolithic `CLAUDE.md` (3000+ lines) | `mind_memory.md` (264-node directive grid) + domain JSONs per module |
| `patterns/`, `lessons/` | `conventions.json`, `work.json` per module |
| `minds/` (harvested from satellites) | `far_memory archives/` (topic-split) |
| `notes/` (session memory) | `sessions/` — `near_memory.json` + `far_memory.json` + `archives/` |
| `live/`, `scripts/` (monolith) | `K_DOCS/scripts/` + `K_MIND/scripts/` (per module) |
| `NEWS.md`, `PLAN.md`, `LINKS.md`, `STORIES.md` | K_MIND memory files (mind_memory.md nodes, domain JSONs) |
| `publications/README.md` | `K_DOCS/` publication pipeline |
| `projects/` | `K_PROJECTS/data/projects/` |

### Commands & Lifecycle

| K1.0 Command | K2.0 Equivalent |
|-------------|----------------|
| `wakeup` | `session_init.py` + `/mind-context` skill |
| `save` | `far_memory_split.py` + git commit/push |
| `remember ...` | `memory_append.py --content "..."` |
| `resume` / `recover` | `session_init.py --preserve-active` + `memory_recall.py` |
| `recall` | `memory_recall.py --subject "..."` |
| `refresh` | `/mind-context` (reload mindmap + near_memory) |
| `status` | `/mind-stats` + `/mind-context` |
| `help` / `aide` / `?` | `.claude/skills/` SKILL.md system (Claude Code native) |
| `elevate` | GH_TOKEN detection via `gh_helper.py` |
| `checkpoint` | Near/far memory auto-persistence (every turn) |

### Harvest & Distribution

| K1.0 Command | K2.0 Equivalent |
|-------------|----------------|
| `harvest <project>` | K_GITHUB `sync_github.py` |
| `harvest --healthcheck` | K_GITHUB + K_VALIDATION `/integrity-check` |
| `harvest --promote N` | Manual: update `conventions.json` or `work.json` |
| `harvest --fix <project>` | K_GITHUB sync to satellite |
| Push CLAUDE.md to satellites | K_MIND module pushed via git |

### Publications & Documentation

| K1.0 Command | K2.0 Equivalent |
|-------------|----------------|
| `pub new <slug>` | `/docs-create <slug>` skill |
| `pub check` / `pub sync` | K_DOCS validation scripts |
| `pub export --pdf/--docx` | K_DOCS export pipeline (browser CSS Paged Media) |
| `doc review` | K_DOCS `/pub` skill |
| `webcard <target>` | K_DOCS `generate_mindmap_webcard.py` + `stitch_webcard.py` |
| `weblinks` / `weblinks --admin` | K_DOCS webcard skill |
| `profile update` | K_DOCS profile-update skill |

### Projects

| K1.0 Command | K2.0 Equivalent |
|-------------|----------------|
| `project create <name>` | K_PROJECTS `/project-create` skill |
| `project list/info/review` | K_PROJECTS `/project-manage` skill |
| `project register` | K_PROJECTS `compile_projects.py` |

### Live Session & Visual

| K1.0 Command | K2.0 Equivalent |
|-------------|----------------|
| `I'm live` | K_DOCS live-session skill (same concept) |
| `multi-live` | K_DOCS live-session skill |
| `recipe` | K_DOCS live-session skill |
| `visual <path>` | K_DOCS visual skill (OpenCV + Pillow) |
| `deep <description>` | K_DOCS visual skill (deep analysis mode) |
| `analyze <path>` | K_DOCS visual skill (static analysis) |

### Scoped Input & Boards

| K1.0 Command | K2.0 Equivalent |
|-------------|----------------|
| `#N: <content>` | K_GITHUB tagged-input skill |
| `#N:methodology:<topic>` | K_GITHUB tagged-input skill |
| `#N:info` / `#N:done` | K_GITHUB tagged-input skill |
| `g:<board>:<item>` | K_GITHUB board-item-alias methodology |
| `g:<board>:<item>:done/progress/info` | K_GITHUB board operations |

### Structure & Integrity

| K1.0 Command | K2.0 Equivalent |
|-------------|----------------|
| `normalize` / `normalize --fix` | K_VALIDATION `/normalize` skill |
| `/healthcheck` | K_VALIDATION `/healthcheck` skill (engineering + task workflow scopes) |
| `/integrity` | K_VALIDATION `/integrity-check` skill (29 checkpoints) |

### Task Workflow

| K1.0 | K2.0 |
|------|------|
| 8-stage SDLC (INITIAL → COMPLETION) | K_VALIDATION `/task-received` + `/work-cycle` skills |
| Work cycle (8 steps per todo) | K_VALIDATION `/work-cycle` skill |
| Engineering cycle (10-stage parallel) | K_VALIDATION methodology |
| Save protocol (7-section summary) | K_VALIDATION `/save-protocol` equivalent |

### Interactive Modes

| K1.0 Mode | K2.0 Equivalent |
|-----------|----------------|
| Conception (design new capabilities) | K_DOCS conventions `interactive-conception.md` |
| Documentation (create publications) | K_DOCS conventions `interactive-work-sessions.md` |
| Diagnostic (live debugging) | K_DOCS conventions `interactive-diagnostic.md` |
| `interactif` / `interactive` | Natural language + skill routing |

### Skills System

| K1.0 | K2.0 |
|------|------|
| `routes.json` (keyword → program) | `.claude/skills/` SKILL.md files (Claude Code native) |
| `SkillRegistry` (LireChoix, Fonction, Programme) | SKILL.md invocation by Claude Code |
| `resolve_methodologies()` (family-based) | Each skill reads its own `methodology/` chain |
| `filter_unread()` / `mark_read()` (dedup) | Claude Code native skill loading (no dedup needed) |
| `knowledge_resultats.json` (quiz results) | Removed — skills are on-demand |
| `executer_demande.py` (command router) | Claude Code interprets + routes to skills |

### Infrastructure

| K1.0 | K2.0 |
|------|------|
| Jekyll build (`_config.yml`, `_layouts/`) | `.nojekyll` static JS viewer (`docs/index.html`) |
| 6 interfaces (session, project, task, navigator, pub index, profile) | 5 interfaces + live mindmap (I1-I5 + mindmap) |
| `generate_sessions.py` | K_DOCS compilation scripts |
| `compile_tasks.py` | K_DOCS compilation scripts |
| `gh_helper.py` (GitHub API) | K_MIND `gh_helper.py` (same, relocated) |

## Publications Needing Deep Text Review

### Priority 1 — Core Architecture (K1.0 refs throughout)
- **#14 Architecture Analysis** — Full K2.0 rewrite needed (4-layer → 5-module)
- **#3 AI Session Persistence** — Diagrams done, text still refs CLAUDE.md/notes/wakeup/save
- **#8 Session Management** — All commands ref K1.0 lifecycle
- **#4 Distributed Minds** — Text refs CLAUDE.md push, patterns/lessons/minds layers

### Priority 2 — Feature Documentation
- **#7 Harvest Protocol** — 4-stage promotion, minds/ refs
- **#4a Knowledge Dashboard** — Network monitoring with K1.0 refs
- **#9 Security by Design** — Principles valid, architecture refs need K2.0
- **#10 Live Knowledge Network** — TCP discovery + K1.0 evolution refs
- **#19 Interactive Work Sessions** — Diagrams done, text has K1.0 channel refs
- **#20 Session Metrics & Time** — Compilation workflow tied to K1.0

### Priority 3 — Moderate Updates
- **#6 Normalize** — Concept valid, some CLAUDE.md refs
- **#12 Project Management** — Concept valid (K_PROJECTS), satellite refs
- **#18 Documentation Generation** — Diagrams done, some heritage refs

### Already Current (No Text Review Needed)
- #0 Knowledge System (diagrams updated)
- #0v2 Knowledge 2.0 (legacy notice + sections 1&8 current)
- #1 MPLIB Storage Pipeline (domain-specific)
- #2 Live Session Analysis (domain-specific)
- #5 Webcards & Social Sharing (K_DOCS pipeline, current)
- #11 Success Stories (historical narratives)
- #13 Web Pagination & Export (K_DOCS, current)
- #15 Architecture Diagrams (fully rewritten K2.0)
- #16 Web Page Visualization (K_DOCS, current)
- #17 Web Production Pipeline (K_DOCS, current)
- #21 Main Interface (current)
- #22 Session Review / Visual Documentation (current)
- #23 Web Documentation Viewer (current)
- #24 Live Mindmap (current)

## Review Method Per Publication

1. Read full EN content (summary + full)
2. Compare every reference against K1.0 → K2.0 mapping above
3. Update text, tables, descriptions to K2.0 equivalents
4. Verify mermaid diagrams still accurate (phase 1 should have caught these)
5. Update FR mirror with same changes
6. Commit + push to both remotes
7. Mark as reviewed
