---
layout: publication
title: "Session Management — K_MIND Scripts Lifecycle"
description: "Practical reference for the K2.0 session lifecycle: session_init.py bootstrap, /mind-context context loading, memory_append.py real-time persistence, far_memory_split.py topic archiving, memory_recall.py deep search — programs over improvisation, deterministic scripts with Claude intelligence as arguments."
pub_id: "Publication #8"
version: "v2"
date: "2026-03-16"
permalink: /publications/session-management/
og_image: /assets/og/session-management-en-cayman.gif
keywords: "session, K_MIND, scripts, lifecycle, memory, persistence, session_init, memory_append"
---

# Session Management — K_MIND Scripts Lifecycle
{: #pub-title}

> **Parent publication**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | **Core reference**: [#14 — Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }}) | [#15 — Architecture Diagrams]({{ '/publications/architecture-diagrams/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/publications/knowledge-2.0/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Programs over improvisation |
| [K1.0 → K2.0 Evolution](#k10--k20-evolution) | Commands to scripts transformation |
| [Session Lifecycle](#session-lifecycle) | session_init.py → /mind-context → work → memory_append.py → far_memory_split.py → git |
| [Session Init](#session-init--session_initpy) | Bootstrap with deterministic script |
| [Context Loading](#context-loading--mind-context) | Mindmap directive grid + near memory |
| [Real-Time Persistence](#real-time-persistence--memory_appendpy) | Every turn — far_memory + near_memory atomically |
| [Topic Archiving](#topic-archiving--far_memory_splitpy) | Split completed topics from far_memory |
| [Memory Recall](#memory-recall--memory_recallpy) | Search archived memory by subject |
| [Memory Stats](#memory-stats--mind-stats) | Context occupancy and available tokens |
| [Session Viewer (I1)](#session-viewer--interface-i1) | Interactive session browser with charts and grouping |
| [The Free Guy Analogy](#the-free-guy-analogy) | NPC vs aware — updated for K2.0 |

## Abstract

Publication #3 (AI Session Persistence) explains the **methodology** — why AI sessions need persistent memory. This publication is the **practical reference** — how the K_MIND module's deterministic scripts manage the session lifecycle in Knowledge 2.0.

**Core principle: Programs over improvisation.** Claude provides intelligence (summaries, topic names, mind references) as arguments to deterministic Python scripts. Every mechanical operation is scripted — no freeform note writing, no manual state management.

Every session follows:

```
session_init.py → /mind-context → [work + memory_append.py every turn] → far_memory_split.py → git commit & push
```

## K1.0 → K2.0 Evolution

| K1.0 (Commands) | K2.0 (Scripts) |
|-----------------|----------------|
| `wakeup` (11-step bootstrap) | `session_init.py` + `/mind-context` skill |
| `save` (6-step PR protocol) | `memory_append.py` (every turn) + `far_memory_split.py` + git commit/push |
| `refresh` (re-read CLAUDE.md) | `/mind-context` (reload mindmap + near_memory) |
| `resume` / `recover` | `session_init.py --preserve-active` + `memory_recall.py` |
| `recall` (4-layer search) | `memory_recall.py --subject "..."` |
| `remember <text>` | `memory_append.py --content "..."` |
| `status` (read notes/) | `/mind-stats` + `/mind-context` |
| `help` / `?` | `.claude/skills/` SKILL.md system (Claude Code native) |
| `notes/` (flat files) | `sessions/` — near_memory.json + far_memory.json + archives/ |
| CLAUDE.md (3000+ lines) | `mind_memory.md` (264-node directive grid) + domain JSONs |
| `session-runtime-*.json` cache | near_memory.json (summaries) + far_memory.json (verbatim) |
| PreToolUse hooks (v56 gates) | K_MIND session lifecycle (scripts enforce flow) |

## Session Lifecycle

```
session_init.py → /mind-context → [work] → memory_append.py (every turn) → far_memory_split.py → git commit & push
```

Every session, every turn, every topic. Scripts handle all mechanical operations — Claude provides intelligence as arguments.

## Session Init — `session_init.py`

Initializes session files and manages the near/far memory lifecycle.

| Mode | Command | What it does |
|------|---------|-------------|
| **New session** | `session_init.py --session-id "<id>"` | Archive previous session, carry forward summaries to `last_session` in near_memory |
| **Resume** | `session_init.py --session-id "<id>" --preserve-active` | Preserve active messages, restore context |
| **Compaction recovery** | (auto via `/mind-context`) | Reload mindmap + near_memory from disk |

## Context Loading — `/mind-context`

The `/mind-context` skill loads the mindmap directive grid and near_memory summaries. Output:

1. **Mindmap** — mermaid code block from `mind_memory.md` (264 nodes, ~2.8K tokens)
2. **Recent context** — categorized near_memory summaries (conversation, conventions, work, documentation)
3. **Memory stats** — disk size, token counts, loaded context, available tokens

Modes: normal (depth-filtered), full (all nodes), branch peek (specific path at full depth).

## Real-Time Persistence — `memory_append.py`

Called **every turn**. Handles far_memory + near_memory atomically.

| Parameter | Content | Destination |
|-----------|---------|-------------|
| `--content` | User's exact message (verbatim) | far_memory.json |
| `--content2` | Assistant's full output (verbatim) | far_memory.json |
| `--summary` | One-line summary | near_memory.json |
| `--mind-refs` | Referenced mindmap nodes | near_memory.json |
| `--tools` | Tool calls made | near_memory.json |

Supports `--stdin` mode for large content (tables, code blocks, mermaid diagrams).

## Topic Archiving — `far_memory_split.py`

When far_memory grows large, archive completed topics:

```bash
python3 scripts/far_memory_split.py \
    --topic "Topic Name" \
    --start-msg 1 --end-msg 24 \
    --start-near 1 --end-near 7
```

Claude identifies topic boundaries from near_memory summary clusters. The script moves messages to `archives/far_memory_session_<id>_<timestamp>.json`.

## Memory Recall — `memory_recall.py`

Search archived memory by subject:

```bash
python3 scripts/memory_recall.py --subject "architecture"   # Search
python3 scripts/memory_recall.py --list                       # List all archives
python3 scripts/memory_recall.py --subject "theme" --full     # Full content
```

Replaces K1.0's 4-layer progressive search with direct archive access.

## Memory Stats — `/mind-stats`

Shows context occupancy per memory store:

| Store | What it measures |
|-------|-----------------|
| far_memory | Verbatim message count + size |
| near_memory | Summary count + size |
| archives | Topic count + total size |
| mind_memory | Node count + size |
| domain JSONs | Reference count + total size |
| Context used | Total loaded tokens |
| Available | Remaining before compaction |

## Session Viewer — Interface I1

Interactive web interface at `/interfaces/session-review/` for browsing session reports. Features:

- **Date-based session grouping**: all sessions from the same day grouped under the earliest as root, subsequent ones as continuations. The root aggregates all children's data.
- **4 pie charts**: Session Scope, Deliverables, Lines Changed, Active Time
- **Code Impact bar chart**: additions/deletions per individual PR
- **Metrics compilation**: files, commits, lines changed, velocity, calendar/active time
- **Timeline**: chronological task comments with expand/collapse

## The Free Guy Analogy

Without `mind_memory.md` and `sessions/`, every Claude session is an **NPC** — stateless, no memory. With the K_MIND scripts lifecycle (`session_init.py` → `/mind-context` → work → `memory_append.py`), each session inherits everything the previous one learned.

`/mind-context` is putting on the sunglasses. Without the sunglasses, you're just another NPC.

```
NPC (no context) → /mind-context → AWARE (264-node directive grid) → work → memory_append.py → next session inherits
```

Recovery: ~10 seconds with `/mind-context` reload vs ~15 minutes of manual re-explanation.

---

[**Read the full documentation →**]({{ '/publications/session-management/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
