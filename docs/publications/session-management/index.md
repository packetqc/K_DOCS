---
layout: publication
title: "Session Management — Practical Guide to AI Session Lifecycle Commands"
description: "Practical command reference for wakeup, save, remember, status, and help — the five commands that manage the AI session lifecycle. Every session follows: wakeup → work → save. This guide documents each command with usage, behavior, and examples."
pub_id: "Publication #8"
version: "v1"
date: "2026-02-19"
permalink: /publications/session-management/
og_image: /assets/og/session-management-en-cayman.gif
keywords: "session, wakeup, save, lifecycle, commands, persistence"
---

# Session Management — Commands Reference
{: #pub-title}

> **Parent publication**: [#0 — Knowledge]({{ '/publications/knowledge-system/' | relative_url }}) | **Methodology**: [#3 — AI Session Persistence]({{ '/publications/ai-session-persistence/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Practical command reference overview |
| [Usage Patterns](#usage-patterns) | Three ways to interact with commands |
| [Quick Reference](#quick-reference) | All 9 session commands at a glance |
| [wakeup](#wakeup--session-init) | 11-step bootstrap with context recovery |
| [save](#save--session-save-protocol) | Pre-save summary → commit → push → PR → merge |
| [refresh](#refresh--lightweight-context-restore) | Re-read CLAUDE.md, git status, reprint help (~5s) |
| [resume](#resume--crash-recovery) | Crash recovery from checkpoint |
| [recover](#recover--branch-based-work-recovery) | Cherry-pick stranded work from `claude/*` branches |
| [recall](#recall--deep-memory-search) | 4-layer progressive search across all knowledge channels |
| [remember](#remember--persist-insights) | Append insights to session notes |
| [status / help](#status--state-summary) | State summary and multipart command table |
| [PreToolUse Enforcement](#pretooluse-enforcement-v56) | Two-layer hook architecture blocking edits until protocol passes |
| [Session Viewer (I1)](#session-viewer--interface-i1) | Interactive session browser with pie charts and tree grouping |
| [The Free Guy Analogy](#the-free-guy-analogy) | NPC vs aware — the sunglasses moment |

## Abstract

Publication #3 explains the **methodology** — why AI sessions need persistent memory. This publication is the **practical command reference** — how to use `wakeup`, `save`, `remember`, `status`, and `help` in daily work.

Every session follows: `wakeup → work → save`. These commands manage that lifecycle.

## Usage Patterns

The Knowledge system supports three entry patterns for interacting with commands. All commands work through any of them.

| Pattern | How | Example | Best for |
|---------|-----|---------|----------|
| **Direct command** | Type the command as your entry prompt | `save` | Known commands, fast one-shot |
| **Natural language** | Describe what you want in plain text | `sauvegarde ma session` | When you don't know the exact syntax |
| **Interactive session** | `interactif` + command or request in description | `interactif` then `resume interrupted work` | Multi-step sessions, chaining commands |

In interactive mode, `help` is displayed automatically at session start — showing all available commands. The session stays open for follow-up commands until `terminé` or `done`.

## Quick Reference

| Command | Action |
|---------|--------|
| `wakeup` | Session init — read knowledge, notes, sync assets, print commands |
| `save` | Pre-save summary → commit → push → PR → merge (elevated) or guide |
| `refresh` | Lightweight context restore — re-read CLAUDE.md, git status (~5s) |
| `resume` | Crash recovery from `notes/checkpoint.json` |
| `recover` | Search `claude/*` branches for stranded work, cherry-pick/apply |
| `recall <keyword>` | Deep memory search across all knowledge channels |
| `remember ...` | Append text to current session notes |
| `status` | Read `notes/` and summarize current state |
| `help` / `?` | Print multipart command table |

## wakeup — Session Init

Bootstraps a new session with full context recovery in 11 steps: read knowledge, check evolution, scan `minds/`, read `notes/`, read plans, sync assets, sync upstream (fetch and merge default branch into task branch), check git log, check branches, summarize state, print commands. The "sunglasses moment" — without it, you're an NPC.

## save — Session Save Protocol

Pre-save summary (metrics, time blocks, self-assessment) → generate session notes → post notes on issue → finalize runtime cache → commit → push → create PR → merge (elevated) or guide (semi-auto) → closing report → post-close comment. Dual file output: both `session-YYYY-MM-DD-*.md` and `session-runtime-*.json` must be in the commit.

## refresh — Lightweight Context Restore

Re-reads CLAUDE.md, strategic remote check, git status, reprints help (~5s). Use after compaction. Use `wakeup` only for deep re-sync.

## resume — Crash Recovery

Reads `notes/checkpoint.json`, restores todo list, restarts from last completed step. Auto-offered at wakeup step 0.9.

## recover — Branch-Based Work Recovery

Searches `claude/*` branches for stranded commits (pushed but never merged). Offers cherry-pick or diff-apply recovery. Complements `resume` (checkpoint-based).

## recall — Deep Memory Search

4-layer progressive search: near memory (~5s) → git memory (~10s) → GitHub memory (~15s) → deep memory (~30s). Stops when found. If stranded branch detected, suggests `recover`.

## remember — Persist Insights

`remember <text>` appends to session notes. Use for decisions, harvest flags (`remember harvest: <insight>`), and directives for future sessions.

## status — State Summary

Reads all `notes/` files and summarizes: last activity, pending items, active branches, remembered directives. Quick pickup after a break.

## help — Multipart Command Table

Part 1 (knowledge commands) + Part 2 (project commands). Concatenated, never duplicated. Part 1 from `packetqc/knowledge`, Part 2 from the project's own CLAUDE.md.

## The Free Guy Analogy

Without notes and CLAUDE.md, every session is an NPC. `wakeup` is putting on the sunglasses. Recovery: ~30 seconds vs ~15 minutes manual.

## Context Loss Recovery

When a session hits the context window limit, the conversation gets compacted. The mind is lost, but git and the session cache survive. Recovery protocol:

1. **Read session cache** — `read_runtime_cache()` recovers issue number, request description, all session_data (decisions, comment IDs, todo state, add-ons, phase, PR numbers). This is the **first recovery action**.
2. **Run `refresh`** — re-reads CLAUDE.md, quick git status, reprints help.
3. **Run the git recovery line**:

```bash
git branch --show-current && git status -s && git log --oneline -10
```

Cache + branch + uncommitted work + recent commits = complete state recovery in ~10 seconds.

**Auto-commit on write**: Every cache write (`write_runtime_cache()`, `update_session_data()`) auto-commits to git via `commit_cache()` — the cache is always recoverable, even after a crash.

## PreToolUse Enforcement (v56)

Two-layer hook architecture: `SessionStart` initializes state, `PreToolUse` enforces it by blocking `Edit|Write|NotebookEdit` until Gate 1 (wakeup protocol completed) and Gate 2 (GitHub issue created) pass. Gate 7 warns if >5 min since last issue comment. The deny message tells any Claude instance exactly how to unblock.

## Session Viewer — Interface I1

Interactive web interface at `/interfaces/session-review/` for browsing session reports. Features:

- **Date-based session grouping**: all sessions from the same day grouped under the earliest as root (💬 original), subsequent ones as continuations (🔁). The root aggregates all children's data.
- **4 pie charts**: Session Scope (children vs related issues), Deliverables (PRs + Commits + Issues + Lessons), Lines Changed (additions vs deletions), Active Time
- **Code Impact bar chart**: additions/deletions per individual PR
- **Metrics compilation**: files, commits, lines changed, velocity, calendar/active time
- **Timeline**: chronological issue comments with expand/collapse, PR delivery markers

---

[**Read the full documentation →**]({{ '/publications/session-management/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
