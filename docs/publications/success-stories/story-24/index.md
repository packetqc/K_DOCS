---
layout: publication
title: "Story #24 — The Toggle: Restructuring Knowledge with a Safety Net"
description: "How a satellite-first migration strategy turned a risky repo restructure into a validated, reversible operation — 852 files moved, 158 paths remapped, zero breakage."
pub_id: "Publication #11 — Story #24"
version: "v1"
date: "2026-03-10"
permalink: /publications/success-stories/story-24/
keywords: "success story, knowledge restructure, migration, toggle, satellite, dry-run"
---

# Story #24 — The Toggle: Restructuring Knowledge with a Safety Net

> **Parent publication**: [#11 — Success Stories]({{ '/publications/success-stories/' | relative_url }})

---

<div class="story-section">

## The Problem

The knowledge repo had grown organically — `scripts/`, `methodology/`, `notes/`, `publications/`, `docs/`, `live/`, `evidence/`, `patterns/`, `lessons/`, `minds/`, `projects/`, `profile/`, `assets/` — all at root level. Fifteen directories competing for attention. Satellites bootstrapping from this structure inherited the sprawl.

The core/satellite version juggling (`<!-- knowledge-version: v47 -->`) added friction without value. Every satellite needed to know what version it was at, what it was missing, what had drifted. Manual bookkeeping disguised as automation.

The goal: one `knowledge/` directory with clear subdivisions. Engine separate from data. Methodology separate from presentation. Runtime state separate from everything.

## The Approach — Toggle

Instead of restructuring the core live and hoping nothing breaks, use a **toggle strategy**:

1. Build the migration script on the core branch
2. **Merge to main** before sharing (pitfall #25 — learned the hard way, got a 404)
3. Drop the script on a satellite, run it, validate
4. If the satellite works → apply to core with confidence

The migration script (`knowledge_migrate.py`) is self-contained. One file. Download, `chmod +x`, run. Four steps:

- **Detect** legacy indicators (version tags, flat structure, scripts at root)
- **Restructure** into `knowledge/` (engine, methodology, data, web, state)
- **Remap** 158+ path references in CLAUDE.md and all skills
- **Commit & push**

## The Numbers

| Metric | Value |
|--------|-------|
| Files moved | 852 |
| Path references remapped | 158 (skills + CLAUDE.md) |
| GitHub URLs updated | 44 (EN + FR publications) |
| Root directories eliminated | 15 → 1 (`knowledge/`) |
| Files staying at root | 4 (CLAUDE.md, README.md, LICENSE, .gitignore) |
| Runtime JSONs separated | 43 (notes/ → knowledge/state/sessions/) |
| Satellite migration time | Single command, one commit |
| Breakage | Zero |

## The Result

```
repo/
├── CLAUDE.md
├── README.md
├── LICENSE
├── .claude/skills/
└── knowledge/
    ├── engine/        # scripts, live, config
    ├── methodology/   # 40+ docs, lessons, patterns
    ├── data/          # notes, projects, minds, publications
    ├── web/           # docs, assets, profile
    └── state/         # runtime sessions
```

## What Made It Work

**Safe-boot mode** — The restructure script has a `--safe-boot` flag that moves everything *except* CLAUDE.md and `.claude/`. The boot files that Claude Code depends on stay untouched during the first pass. Path remapping happens as a separate step. Two-phase migration, each independently verifiable.

**The toggle** — Satellite validates before core commits. If the satellite breaks, the core is untouched. If it works, you know the migration is safe. The satellite is the canary.

**Pitfall #25** — We published the download URL before merging to main. The satellite got a 404. Now documented: always PR+merge before sharing raw GitHub URLs. Sequencing constraint, not optional.

**Mechanical remapping** — No manual find-and-replace across 28 files. The `remap_paths.py` script has deterministic rules: `scripts/` → `knowledge/engine/scripts/`, `methodology/` → `knowledge/methodology/`, etc. Run it twice, get the same result. Idempotent.

</div>

---

> *The best migration is the one where you can prove it works before you commit to it.*
