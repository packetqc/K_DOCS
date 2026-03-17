# packetqc/knowledge — Knowledge 2.0

**Interactive Intelligence Framework** for AI-augmented software engineering.

Knowledge 2.0 solves **session initialization chaos** — structured questionnaire, deterministic command routing, composable skills, family-based methodology resolution, and deduplication. Every session *understands what it's about to do* before doing it.

---

## What's Inside

| Component | Count | Description |
|-----------|-------|-------------|
| **Methodologies** | 30 | Operational standards in `methodology/` — documentation, interactive modes, system, satellite, project, compilation |
| **Skills** | 26 | Composable units in `.claude/skills/` — from `knowledge-validation` to `webcard` |
| **Scripts** | 22 | Python programs in `scripts/` — knowledge engine, OG GIF generator, visual CLI, project scaffolding |
| **Publications** | 1 | `publications/knowledge-2.0/` — master publication |
| **Interfaces** | 3 | Session Review (I1), Main Navigator (I2), Task Workflow (I3) — landscape-native |
| **Web Pages** | 4+ | EN+FR summary + complete in `docs/` with dual-theme webcards |
| **Success Stories** | 23 | `docs/publications/success-stories/` — validated capabilities |

## Key Features

- **Session Questionnaire** — A1-E4 validation grid, persistent state in `.claude/knowledge_resultats.json`
- **Command Router** — `routes.json` maps keywords to programs deterministically
- **GitHub Project Integration** — `project_ensure()` + `project_item_add()` as non-blocking preconditions
- **Non-Blocking Persistence** — All GitHub operations persist locally when unavailable, sync at next opportunity
- **Task Progression** — Persistent 8-stage progression bar in Task Workflow viewer
- **Session Identity** — `user_session_id` aggregates N system sessions into 1 user session
- **Skill Architecture** — `SkillRegistry` with `LireChoixSkill`, `FonctionSkill`, `ProgrammeSkill`
- **Methodology Resolution** — `resolve_methodologies(family)` scans by prefix, 6 families, 30 files
- **Deduplication Engine** — `filter_unread` / `mark_read` — 66% reduction in multi-command sessions
- **Interactive Modes** — Conception, Documentation, Diagnostic — each with its own phase pattern
- **Dual-Theme Webcards** — 1200x630 animated GIFs, Cayman (light) + Midnight (dark)

## Structure

```
CC/
├── CLAUDE.md                    # System instructions (compaction-resilient)
├── methodology/                 # 30 operational methodologies
├── .claude/skills/              # 26 composable skills
├── scripts/                     # 22 Python programs
├── publications/knowledge-2.0/  # Source (README.md)
└── docs/                        # Web pages + OG assets
    ├── publications/            # EN (summary + complete)
    ├── fr/publications/         # FR mirror
    └── assets/og/               # Animated GIF webcards
```

## Legacy

This repo evolves from [packetqc/knowledge](https://github.com/packetqc/knowledge) — the v1 system with 12 publications, 26 knowledge versions, and a distributed satellite network. Knowledge 2.0 serves as the integration test for the planned migration.

---

**Authors**: Martin Paquet & Claude (Anthropic, Opus 4.6)
