---
layout: publication
title: "CLAUDE.md Bootstrap Optimization — Condensation Strategy & Section Map"
description: "Annex documenting the 81% reduction of CLAUDE.md from 3872 to 714 lines: condensation strategy, full section map, before/after metrics, and best practices for maintaining compact AI bootstrap files."
pub_id: "Publication #0"
version: "v1"
date: "2026-03-02"
permalink: /publications/knowledge-system/bootstrap-optimization/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "CLAUDE.md, bootstrap, condensation, optimization, section map, compaction survival, best practices"
---

# CLAUDE.md Bootstrap Optimization — Condensation Strategy & Section Map

> **Parent publication**: [#0 — The Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | **Complete**: [Full documentation]({{ '/publications/knowledge-system/full/' | relative_url }})

**Contents**

| | |
|---|---|
| [Context](#context) | Why the reduction was necessary |
| [Strategy](#strategy) | The condensation approach |
| [Section Map — Before & After](#section-map--before--after) | Full map of every section transformation |
| [Metrics](#metrics) | Quantitative results |
| [Best Practices](#best-practices) | Principles for maintaining compact bootstrap files |
| [Archive Reference](#archive-reference) | Where the removed content lives |

---

## Authors

**Martin Paquet** — Network security analyst programmer, architect of Knowledge. Identified the bootstrap optimization need after observing compaction behavior across hundreds of sessions.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Executed the condensation across 3 sessions, applying the methodology file pointer pattern to reduce CLAUDE.md by 81%.

---

## Context

CLAUDE.md is the bootstrap file — the "sunglasses" that transform a stateless AI session into a knowledge-aware one. It is read at the start of every session (wakeup step 0) and loaded as system-level project instructions.

**The problem**: Over 54 knowledge versions, CLAUDE.md grew from a focused bootstrap to 3872 lines (~68KB). The Quick Commands section alone was 2370 lines — 62% of the file — duplicating content already documented in 25 methodology files (7239 total lines). This created three issues:

1. **Token budget pressure** — At ~50K tokens, CLAUDE.md consumed 25% of the 200K context window before any work began
2. **Compaction fragility** — Larger files lose more content when the context compresses
3. **Redundancy** — Command implementations existed in both CLAUDE.md and methodology/ files, creating maintenance drift

**The constraint**: CLAUDE.md must contain enough behavioral DNA to survive compaction. After compaction, only what's in CLAUDE.md (system-level) persists — methodology files (conversation-level) are lost. The critical-subset principle applies: keep the *what* and *when*, point to the *how*.

---

## Strategy

The condensation follows one principle: **tables + pointers replace prose**.

| Pattern | Before | After |
|---------|--------|-------|
| Command implementations | Full protocol with all steps, edge cases, error handling | Command table + `**Full specification**: methodology/xxx.md` pointer |
| Section introductions | Multi-paragraph context | Single sentence + key constraint |
| Behavioral rules | Embedded in command descriptions | Extracted to dedicated subsection (kept in full) |
| Edge cases & pitfalls | Inline in every section | Consolidated in `lessons/pitfalls.md` with 5-line reference |
| Evolution history | 49 entries in-file | Archive file + last 5 entries retained |

**What stays in CLAUDE.md** (behavioral DNA — survives compaction):
- Core Methodology (6 items including strategic remote check)
- Core Qualities (13 qualities table)
- Session Lifecycle (auto-wakeup, elevate, two-gate flow)
- Autonomous Execution Principle
- Command tables (user-facing — what to type, what happens)
- Key constraints (never use curl, proxy reality, token safety)
- Proven Patterns (validated across real projects)
- Publications table
- How To Use This File (bootstrap instructions)

**What moves to methodology/** (on-demand — loaded when command is invoked):
- Step-by-step protocol implementations
- Checkpoint/resume details
- Dashboard update procedures
- Webcard generation internals
- Publication management internals
- Harvest protocol internals

---

## Section Map — Before & After

The complete transformation of CLAUDE.md from 3872 to 714 lines:

### Retained Sections (Behavioral DNA)

| Section | Lines (before) | Lines (after) | Action |
|---------|---------------|--------------|--------|
| Title + Who Is Martin | 1–27 | 1–27 | **Kept as-is** — identity and contact |
| How We Work Together | 29–168 | 29–168 | **Kept as-is** — Core Methodology (6 items), Core Qualities (13), Session Lifecycle, Autonomous Execution |
| Proven Patterns | 3310–3353 | 457–501 | **Kept as-is** — validated debugging, RTOS, SQLite, UI patterns |
| Knowledge Evolution (v50–v54) | 3385–3407 | 508–530 | **Kept as-is** — recent evolution + archive pointer |
| Publications table | 3736–3810 | 580–643 | **Kept as-is** — 22 publications + interfaces |
| How To Use This File | 3811–3860 | 644–709 | **Kept as-is** — bootstrap instructions |
| Authors | 3861–3872 | 711–714 | **Kept as-is** |

### Condensed Sections

| Section | Lines (before) | Lines (after) | Reduction | Strategy |
|---------|---------------|--------------|-----------|----------|
| On Task Received | 169–535 (367 lines) | 169–200 (33 lines) | **91%** | Five-channel table + protocol summary + cache API reference + pointers |
| Human Bridge + Principles | 536–831 (296 lines) | 201–230 (30 lines) | **90%** | Key rules as bullets + convention summaries + recovery ladder |
| Knowledge Assets + Distributed Minds | 832–938 (107 lines) | 232–246 (19 lines) | **82%** | Asset list + sync rule + gh_helper summary + knowledge layers |
| Quick Commands (ALL) | 939–3308 (2370 lines) | 248–455 (209 lines) | **91%** | Command tables + key rules + `Full specification` pointers |
| Known Pitfalls | 3354–3382 (27 entries) | 501–507 (7 lines) | **74%** | Category summary + pointer to `lessons/pitfalls.md` |
| Knowledge Base / Repo / Token | 3436–3735 (300 lines) | 531–577 (47 lines) | **84%** | Versioning paragraph + proxy table + two-channel model + token modes |

### Removed Content (Archived)

| Content | Original location | New location |
|---------|-------------------|--------------|
| Knowledge Evolution v1–v49 | CLAUDE.md lines 3409–3435 | `knowledge-evolution-archive.md` (86 lines) |

### Quick Commands — Subsection Detail

The largest condensation (2370 → 209 lines) broken down by subsection:

| Subsection | Before (lines) | After (lines) | Methodology file |
|-----------|----------------|---------------|------------------|
| Session Management | ~80 | 18 | `session-protocol.md` |
| GitHub Item Lifecycle | ~120 | 6 | `github-project-integration.md` |
| `save` protocol | ~180 | 23 | `session-protocol.md`, `metrics-compilation.md` |
| Harvest commands | ~350 | 24 | `production-development-minds.md` |
| Content Management | ~280 | 25 | `documentation-generation.md`, `web-production-pipeline.md` |
| `normalize` | ~150 | 6 | Publication #6 |
| `webcard` | ~120 | 6 | Publication #5 |
| Project Management | ~180 | 18 | `project-management.md`, `project-create.md` |
| Project Knowledge (`#`) | ~140 | 15 | `tagged-input.md`, `github-board-item-alias.md` |
| Live Session Analysis | ~200 | 16 | `interactive-diagnostic.md` |
| `help` / `aide` | ~80 | 8 | `commands.md` |
| `refresh` | ~40 | 4 | — (inline) |
| `resume` | ~60 | 8 | `checkpoint-resume.md` |
| `recall` | ~30 | 4 | — (inline) |
| `wakeup` | ~280 | 22 | `session-protocol.md`, `satellite-bootstrap.md` |

---

## Metrics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| **Total lines** | 3,872 | 714 | **−81.6%** |
| **Words** | ~38,000 | ~8,989 | **−76.3%** |
| **Characters** | ~275,000 | ~67,861 | **−75.3%** |
| **Estimated tokens** | ~50,000 | ~12,000 | **−76%** |
| **Context budget usage** | ~25% of 200K | ~6% of 200K | **−19 percentage points** |
| **Major `##` sections** | 12 | 12 | No change |
| **Command tables** | All present | All present | No change |
| **Methodology pointers** | Scattered | 15 explicit | Standardized |

### Token Budget Impact

```
Before (3872 lines):
  CLAUDE.md system load:     ~50,000 tokens (25% of budget)
  Remaining for work:        ~150,000 tokens
  Compaction risk:           HIGH — large system prompt

After (714 lines):
  CLAUDE.md system load:     ~12,000 tokens (6% of budget)
  Remaining for work:        ~188,000 tokens
  Compaction risk:           LOW — compact system prompt
  Net gain:                  +38,000 tokens for actual work
```

---

## Best Practices

Principles derived from this condensation, applicable to any CLAUDE.md or AI bootstrap file:

### 1. Tables Over Prose

Command documentation belongs in tables. A command table row (command | action) survives compaction better than a 20-line protocol description. The table gives the *what*; the methodology file gives the *how*.

### 2. Pointer Architecture

Every condensed section ends with `**Full specification**: methodology/xxx.md`. This creates a two-layer system:
- **Layer 1** (CLAUDE.md): What commands exist, when to use them, key constraints
- **Layer 2** (methodology/): How to execute them, edge cases, error handling

Layer 1 is always present (system-level). Layer 2 is loaded on-demand (wakeup step 0.1 or when the command is invoked).

### 3. Behavioral DNA First

Sections that control session *behavior* (Core Methodology, Session Lifecycle, Autonomous Execution, Branch Protocol) stay in full. Sections that describe *implementation details* (how harvest internally updates dashboards, how webcards render animations) get condensed. The test: "If this section is lost to compaction, does the session still follow the correct protocol?" If yes, it can be condensed.

### 4. Evolution History Archival

The knowledge evolution table grew linearly (one entry per version). At v54, entries v1–v49 were moved to `knowledge-evolution-archive.md` with only the last 5 entries (v50–v54) retained in CLAUDE.md. The archive is referenced but not loaded at wakeup — recent evolution is sufficient for operational context.

### 5. Critical-Subset Principle

The same principle used for satellite CLAUDE.md files (~180 lines) applies to the core: carry enough DNA to drive correct behavior post-compaction. Deep implementations are inherited on demand. The minimum viable bootstrap is:
- Identity (who the user is)
- Methodology (how we work)
- Commands (what's available)
- Constraints (what to never do)
- Pointers (where to find more)

### 6. Maintain the Section Contract

All 12 major `##` sections were preserved in the same order. No sections were removed — only condensed. This preserves the navigability contract: anyone reading CLAUDE.md finds the same structure, just more compact.

### 7. Consolidate Scattered Content

Pitfalls were scattered across command descriptions ("watch out for X when doing Y"). The condensation moved all pitfalls to `lessons/pitfalls.md` with a 7-line reference in CLAUDE.md. One source of truth, one place to update.

---

## Archive Reference

| Content | Location | Size |
|---------|----------|------|
| Knowledge Evolution v1–v49 | [`knowledge-evolution-archive.md`]({{ site.github.repository_url }}/blob/main/knowledge-evolution-archive.md) | 86 lines |
| 25 methodology files | [`methodology/`]({{ site.github.repository_url }}/tree/main/methodology) | 7,239 lines total |
| Pitfalls (full list) | [`lessons/pitfalls.md`]({{ site.github.repository_url }}/blob/main/lessons/pitfalls.md) | 22 entries |
| Proven patterns (full) | [`patterns/`]({{ site.github.repository_url }}/tree/main/patterns) | Multiple files |

---

*Authors: Martin Paquet (packetqcca@gmail.com) & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
