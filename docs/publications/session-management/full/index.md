---
layout: publication
title: "Session Management — Complete Documentation"
description: "Complete documentation for the K2.0 session lifecycle: session_init.py bootstrap, /mind-context context loading, memory_append.py real-time persistence (every turn), far_memory_split.py topic archiving, memory_recall.py deep search, tiered memory architecture (near/far/archives), the Free Guy analogy updated for K2.0, and the Session Viewer interface."
pub_id: "Publication #8 — Full"
version: "v2"
date: "2026-03-16"
permalink: /publications/session-management/full/
og_image: /assets/og/session-management-en-cayman.gif
keywords: "session, K_MIND, scripts, lifecycle, memory, persistence, session_init, memory_append, far_memory_split"
---

# Session Management — Complete Documentation
{: #pub-title}

**Contents**

| | |
|---|---|
| [Authors](#authors) | Publication authors |
| [Abstract](#abstract) | Programs over improvisation |
| [K1.0 → K2.0 Evolution](#k10--k20-evolution) | Commands to scripts transformation |
| [Session Lifecycle](#session-lifecycle) | The complete lifecycle flow |
| [Session Init — session_init.py](#session-init--session_initpy) | Bootstrap new/resume/compaction sessions |
| [Context Loading — /mind-context](#context-loading--mind-context) | Mindmap directive grid + near memory + stats |
| [Real-Time Persistence — memory_append.py](#real-time-persistence--memory_appendpy) | Every turn — far_memory + near_memory atomically |
| [Topic Archiving — far_memory_split.py](#topic-archiving--far_memory_splitpy) | Archive completed topics from far_memory |
| [Memory Recall — memory_recall.py](#memory-recall--memory_recallpy) | Search archived memory by subject |
| [Mindmap Management](#mindmap-management) | mindmap_filter.py, set_depth.py, memory_stats.py |
| [Tiered Memory Architecture](#tiered-memory-architecture) | Near, far, archives — how data flows |
| [Session Lifecycle Events](#session-lifecycle-events) | New session, resume, compaction recovery |
| [The Free Guy Analogy](#the-free-guy-analogy) | NPC vs aware — updated for K2.0 |
| [Recovery Comparison](#recovery-comparison) | Recovery times across scenarios |
| [Fork & Clone Safety](#fork--clone-safety) | Owner-scoped, environmentally isolated |
| [Session Viewer — Interface I1](#session-viewer--interface-i1) | Interactive session browser with charts |
| [Integration with Other Skills](#integration-with-other-skills) | How session scripts work with K2.0 skills |
| [Related Publications](#related-publications) | Sibling and parent publications |

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Designed the session lifecycle protocol enabling AI coding assistants to maintain continuity across sessions.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Executes the session lifecycle — `session_init.py` → `/mind-context` → work → `memory_append.py` — maintaining context continuity across hundreds of sessions.

---

## Abstract

Publication #3 (AI Session Persistence) explains the **methodology** — why AI sessions need persistent memory and the theoretical framework behind it. This publication is the **practical reference** — how the K_MIND module's deterministic scripts manage the session lifecycle in Knowledge 2.0.

**Core principle: Programs over improvisation.** Claude-as-engine is ONLY the bootstrap (new session, resume, compaction recovery). All mechanical operations use scripts. Claude provides intelligence (summaries, topic names, mind references) as arguments to deterministic Python programs.

Every session follows the same lifecycle:

```
session_init.py → /mind-context → [work + memory_append.py every turn] → far_memory_split.py → git commit & push
```

---

## K1.0 → K2.0 Evolution

The K2.0 architecture replaces K1.0's command-based session management with a scripts-based lifecycle. The fundamental shift: from ad-hoc commands that Claude interprets and executes, to deterministic scripts that Claude feeds with intelligent arguments.

| Aspect | K1.0 | K2.0 |
|--------|------|------|
| **Session start** | `wakeup` (11-step protocol: clone repo, read CLAUDE.md, scan minds/, read notes/, sync assets...) | `session_init.py` + `/mind-context` (2 steps: init files, load directive grid) |
| **Session save** | `save` (6-step PR protocol: write notes, commit, push, create PR, user merges) | `memory_append.py` (every turn, automatic) + `far_memory_split.py` + git commit/push |
| **Context restore** | `refresh` (re-read CLAUDE.md, ~5s) | `/mind-context` (reload mindmap + near_memory, ~3s) |
| **Crash recovery** | `resume` (from checkpoint.json) / `recover` (from claude/* branches) | `session_init.py --preserve-active` + `memory_recall.py` |
| **Deep search** | `recall` (4-layer progressive: near → git → GitHub → deep) | `memory_recall.py --subject "..."` (direct archive access) |
| **Persist insight** | `remember <text>` (append to notes/) | `memory_append.py --content "..."` (goes to far_memory.json) |
| **State summary** | `status` (read notes/) | `/mind-stats` + `/mind-context` (live stats + recent context) |
| **Command routing** | `help` / `routes.json` / SkillRegistry | `.claude/skills/` SKILL.md (Claude Code native routing) |
| **Memory storage** | `notes/` (flat Markdown files) | `sessions/` — near_memory.json + far_memory.json + archives/ |
| **Brain** | CLAUDE.md (3000+ lines, monolithic) | `mind_memory.md` (264-node directive grid) + domain JSONs per module |
| **Session cache** | `session-runtime-*.json` (per-branch) | near_memory.json (summaries with pointers) + far_memory.json (verbatim) |
| **Enforcement** | PreToolUse hooks (v56 gates: G1 protocol, G2 issue, G7 exchanges) | K_MIND scripts lifecycle (scripts enforce flow naturally) |
| **Recovery store** | `notes/checkpoint.json` + `claude/*` branches | near_memory.json survives compaction + far_memory archives |

**Key insight**: K1.0 relied on Claude correctly executing multi-step protocols (11 steps for wakeup, 6 steps for save). K2.0 reduces human-interpretable protocols to script calls — Claude decides WHAT (topic name, summary text), the script handles HOW (file I/O, JSON updates, archiving).

---

## Session Lifecycle

### The Complete Flow

```
1. session_init.py         → Initialize session files (new or resume)
2. /mind-context           → Load mindmap directive grid + near_memory context
3. [Work]                  → User requests, Claude executes
4. memory_append.py        → Every turn: persist user message + assistant output + summary
5. (repeat 3-4)            → Continue working
6. far_memory_split.py     → Archive completed topics when far_memory grows
7. git commit & push       → Persist to remote (both remotes)
```

**Versus K1.0**:
- K1.0: Start → 11-step wakeup → work (no per-turn persistence) → 6-step save → end
- K2.0: Start → 2-step init → work (every turn persisted) → archive when needed → commit

The fundamental difference: K1.0 persisted at session END (save). K2.0 persists every TURN (memory_append.py). If a session crashes at turn 50, K1.0 loses everything since the last save. K2.0 has 50 turns of verbatim history in far_memory.json.

---

## Session Init — `session_init.py`

The session initialization script manages the near/far memory lifecycle across session boundaries.

### New Session

```bash
python3 scripts/session_init.py --session-id "<uuid>"
```

| Step | What it does |
|------|-------------|
| 1 | Archive previous session's active messages to `last_session` in near_memory |
| 2 | Clear active messages in far_memory and near_memory |
| 3 | Preserve archives (never deleted) |
| 4 | Write session ID to both memory files |

The previous session's summaries are carried forward as `last_session` context — visible in `/mind-context` output as "Last Session Context".

### Resume / Continue

```bash
python3 scripts/session_init.py --session-id "<uuid>" --preserve-active
```

Preserves all active messages in far_memory and near_memory. Used when:
- Resuming after a crash or disconnect
- Continuing a compacted session
- Re-entering an interrupted session

### Compaction Recovery

When context is compacted, `/mind-context` is invoked automatically. It reloads:
1. The mindmap directive grid from `mind_memory.md`
2. Recent summaries from `near_memory.json`
3. Memory stats from `memory_stats.py`

No data is lost — far_memory.json retains all verbatim messages, near_memory.json retains all summaries.

---

## Context Loading — `/mind-context`

The `/mind-context` skill is the K2.0 equivalent of "putting on the sunglasses." It loads the mindmap directive grid and recent context into the conversation.

### What It Loads

| Component | Source | Size |
|-----------|--------|------|
| Mindmap directive grid | `mind_memory.md` | ~2.8K tokens (264 nodes) |
| Depth config | `depth_config.json` | Controls which branches are shown |
| Near memory summaries | `near_memory.json` | ~8.5K tokens (categorized) |
| Memory stats | `memory_stats.py` output | Context occupancy table |

### Output Format

1. **Mindmap** — mermaid code block, depth-filtered per config
2. **Recent context** — categorized summaries under 4 groups:
   - **conversation** — recent discussions and decisions
   - **conventions** — patterns and standards discovered
   - **work** — tasks accomplished and in progress
   - **documentation** — docs created or updated
3. **Memory stats** — table showing disk size, token counts, loaded context, available tokens

### Modes

| Mode | Command | What it shows |
|------|---------|---------------|
| **Normal** | `/mind-context` | Depth-filtered mindmap (default depth 3, architecture/constraints omitted) |
| **Full** | `/mind-context full` | All nodes at maximum depth |
| **Branch peek** | `/mind-context <path>` | Specific branch at full depth (temporary) |
| **Branch override** | `/mind-context <path> <depth>` | Set depth for a branch (persisted to config) |

### The Mindmap Is Your Memory Grid

The mindmap is not decoration — it is the operating memory. Every node is a directive:

| Node group | Behavioral mapping |
|------------|-------------------|
| **architecture** | HOW you work — system design rules, follow as implementation constraints |
| **constraints** | BOUNDARIES — hard limits, never violate |
| **conventions** | HOW you execute — patterns and standards, apply consistently |
| **work** | STATE — accomplished/staged results, continuity anchor |
| **session** | CONTEXT — brainstorming record, references work for concordance |
| **documentation** | STRUCTURE — documentation references |

---

## Real-Time Persistence — `memory_append.py`

Called **every turn** of every session. This is the heartbeat of K2.0 session management — it handles both far_memory (verbatim) and near_memory (summaries) atomically in a single script call.

### Arguments Mode (short turns)

```bash
python3 scripts/memory_append.py \
    --role user --content "exact user message" \
    --role2 assistant --content2 "full assistant output text" \
    --summary "one-line summary" \
    --mind-refs "knowledge::node1,knowledge::node2"
```

### Stdin Mode (long turns with tables/code)

```bash
python3 scripts/memory_append.py --stdin << 'ENDJSON'
{"role":"user","content":"exact user message","role2":"assistant","content2":"full output with tables, code blocks, etc","summary":"one-line summary","mind_refs":"node1,node2","tools":[{"tool":"Edit","file":"path","action":"desc"}]}
ENDJSON
```

### What Gets Persisted

| Parameter | Content | Destination | Purpose |
|-----------|---------|-------------|---------|
| `--content` | User's exact message (verbatim) | far_memory.json | Full conversation record |
| `--content2` | Assistant's complete visible output | far_memory.json | Full conversation record |
| `--summary` | One-line summary of the turn | near_memory.json | Quick-access context |
| `--mind-refs` | Referenced mindmap nodes | near_memory.json | Concordance tracking |
| `--tools` | JSON array of tool calls made | near_memory.json | Action audit trail |

### Critical Rules

1. **far_memory stores FULL VERBATIM content, NEVER summaries** — the `--content` and `--content2` values are the exact messages, word for word
2. **Called every turn, no exceptions** — even during fast coding sessions, memory_append.py must run
3. **Atomic operation** — both far_memory and near_memory are updated in a single script call, preventing inconsistency

### Versus K1.0

K1.0's `remember <text>` appended a single line to `notes/session-*.md`. K2.0's `memory_append.py` captures the **entire conversation** — every user message, every assistant response, every summary — in structured JSON with cross-references to the mindmap.

---

## Topic Archiving — `far_memory_split.py`

When `far_memory.json` grows large (many turns of verbatim conversation), completed topics are archived to individual files.

### Usage

```bash
python3 scripts/far_memory_split.py \
    --topic "Topic Name" \
    --start-msg 1 --end-msg 24 \
    --start-near 1 --end-near 7
```

### How It Works

| Step | What happens |
|------|-------------|
| 1 | Claude identifies topic boundaries from near_memory summary clusters |
| 2 | Claude provides the topic name, message range, and summary range |
| 3 | The script moves messages from far_memory.json to `archives/far_memory_session_<id>_<timestamp>.json` |
| 4 | Corresponding near_memory summaries are marked as archived |
| 5 | The original far_memory.json shrinks, freeing context space |

### Versus K1.0

K1.0's `save` wrote a Done/Remember/Next Markdown file at session end. K2.0's `far_memory_split.py` archives **by topic**, not by time — a session that covers 3 topics produces 3 archive files, each self-contained and searchable.

---

## Memory Recall — `memory_recall.py`

Searches archived memory by subject keyword.

### Usage

```bash
# Search archives by subject
python3 scripts/memory_recall.py --subject "architecture"

# List all archived topics
python3 scripts/memory_recall.py --list

# Get full content (not just summaries)
python3 scripts/memory_recall.py --subject "theme" --full
```

### Versus K1.0

K1.0's `recall` was a 4-layer progressive search (near memory → git memory → GitHub memory → deep memory), each layer slower and requiring confirmation. K2.0's `memory_recall.py` directly searches the topic-indexed archives — faster, deterministic, no API calls needed.

| K1.0 Layer | Time | K2.0 Equivalent |
|------------|------|-----------------|
| Near memory (~5s) | Session cache, recent notes | near_memory.json (always loaded) |
| Git memory (~10s) | Commit messages, branch diffs | Not needed — far_memory has full verbatim |
| GitHub memory (~15s) | Issue titles, PR descriptions | Not needed — no issue-per-session in K2.0 |
| Deep memory (~30s) | Full-text across publications | `memory_recall.py --subject --full` (~3s) |

---

## Mindmap Management

Three utility scripts support the mindmap directive grid:

### mindmap_filter.py

Renders the mindmap with depth filtering from `depth_config.json`:

```bash
python3 scripts/mindmap_filter.py            # Normal mode (depth-filtered)
python3 scripts/mindmap_filter.py --full      # Full mode (all nodes)
python3 scripts/mindmap_filter.py --path "work" --depth 4  # Branch peek
```

### set_depth.py

Manages depth configuration for mindmap branches:

```bash
python3 scripts/set_depth.py --path "session/near memory" --depth 4
python3 scripts/set_depth.py --path "conventions" --depth 3
```

Persists to `depth_config.json` — human-editable, version-controlled.

### memory_stats.py

Outputs memory statistics table:

| Store | What it measures |
|-------|-----------------|
| far_memory | Message count, size, ~tokens |
| near_memory | Summary count, size, ~tokens |
| archives | Topic count, total size, ~tokens |
| mind_memory | Node count, size, ~tokens |
| domain JSONs | Reference count across all modules, total size |
| CLAUDE.md | File size |
| Context used | Total tokens currently loaded |
| Usable limit | 200K minus buffer |
| Available | Remaining tokens before compaction |

---

## Tiered Memory Architecture

K2.0 uses a tiered memory system managed by K_MIND scripts:

| Tier | File | Content | Loaded at start? |
|------|------|---------|-------------------|
| **Mindmap** | `mind_memory.md` | 264-node directive grid | Yes (~2.8K tokens) |
| **Domain JSONs** | Per-module `.json` | 163 references, ~1.8 MB | Subset (~4.5K tokens) |
| **Near memory** | `near_memory.json` | Real-time summaries with pointers | Yes (~8.5K tokens) |
| **Far memory** | `far_memory.json` | Full verbatim conversation | Minimal |
| **Archives** | `archives/*.json` | Topic-split far_memory | On demand |

### Data Flow

```
User message → memory_append.py → far_memory.json (verbatim)
                                → near_memory.json (summary)

far_memory.json → far_memory_split.py → archives/ (by topic)

archives/ → memory_recall.py → conversation context (on demand)
```

### Near Memory Structure

Near memory summaries are categorized into 4 groups matching the mindmap top-level branches:

- **conversation** — recent discussions, decisions, user feedback
- **conventions** — patterns, standards, rules discovered
- **work** — tasks accomplished, in progress, blocked
- **documentation** — publications, interfaces, docs updated

Each summary includes: message index pointer to far_memory, one-line summary text, mind-refs (mindmap nodes referenced), timestamp.

### Versus K1.0

| Aspect | K1.0 | K2.0 |
|--------|------|------|
| **Storage** | `notes/session-YYYY-MM-DD.md` (flat Markdown) | `sessions/` tiered JSON (near + far + archives) |
| **Granularity** | Per-session (one file per day) | Per-turn (every message persisted) |
| **Format** | Freeform Done/Remember/Next sections | Structured JSON with cross-references |
| **Search** | `recall` (4-layer, slow) | `memory_recall.py` (indexed, fast) |
| **Archiving** | Manual (user decides when to save) | Automatic (memory_append.py every turn) + topic-split (far_memory_split.py) |
| **Recovery** | `checkpoint.json` + `session-runtime-*.json` | near_memory.json (always current) + far_memory.json (always complete) |

---

## Session Lifecycle Events

### New Session Start

1. Run: `python3 scripts/session_init.py --session-id "<uuid>"`
   - Previous session archived, summaries carried forward as `last_session`
2. Run `/mind-context` — output mindmap + recent context + stats
   - Last session summaries visible as "Last Session Context"
3. Begin work — `memory_append.py` called every turn

### Resume

1. Run: `python3 scripts/session_init.py --session-id "<uuid>" --preserve-active`
2. Run `/mind-context` — output mindmap + context
3. Continue work from where it was interrupted

### Compaction Recovery

1. Run `/mind-context` — reload mindmap + near_memory (survives compaction)
2. Use `memory_recall.py --subject "..."` if specific details needed
3. Continue work — no data lost

---

## The Free Guy Analogy

Without `mind_memory.md` and `sessions/`, every Claude session is an **NPC** — stateless, no memory, same blank start. With the K_MIND scripts lifecycle, each session inherits everything the previous one learned.

`/mind-context` is putting on the sunglasses. Without the sunglasses, you're just another NPC — walking around, responding to prompts, with no awareness of yesterday.

```
NPC (no context) → /mind-context → AWARE (264-node directive grid) → work → memory_append.py → next session inherits
```

**K1.0 update**: The analogy was originally built around `wakeup` and `notes/`. In K2.0:
- `wakeup` → `session_init.py` + `/mind-context` (the sunglasses are now a 264-node directive grid instead of a 3000-line CLAUDE.md)
- `notes/` → `sessions/` (the memory is now tiered JSON with per-turn granularity instead of per-session Markdown)
- `save` → no longer needed as a discrete command — `memory_append.py` persists every turn automatically

The NPC/aware duality remains. The implementation moved from commands to scripts.

---

## Recovery Comparison

| Scenario | K1.0 Mechanism | K2.0 Mechanism | Time |
|----------|---------------|----------------|------|
| New session (cold start) | `wakeup` — 11-step protocol | `session_init.py` + `/mind-context` | ~10s |
| Context loss (mid-session) | Session cache + `refresh` | `/mind-context` (near_memory survives) | ~3s |
| Crash (state exists) | `resume` from checkpoint.json | `session_init.py --preserve-active` | ~5s |
| Crash (no state) | `recover` from claude/* branches | `memory_recall.py` from archives | ~5s |
| Deep memory search | `recall` (4-layer, ~30s per layer) | `memory_recall.py --subject` | ~3s |
| Manual (no tooling) | User re-explains everything | User re-explains everything | ~15 min |

---

## Fork & Clone Safety

The K2.0 session lifecycle inherits the same security properties as K1.0:

| Aspect | Protection |
|--------|------------|
| **Session init** | `session_init.py` operates on local files only — no network access |
| **Memory files** | `sessions/` starts empty for every new clone — no cross-contamination |
| **Scripts** | Pure Python with no external dependencies — no supply chain risk |
| **Credentials** | GH_TOKEN is an environment variable, never stored in session files or git history |
| **Mindmap** | `mind_memory.md` is methodology (public) — no secrets in the directive grid |

---

## Session Viewer — Interface I1

The Session Viewer is an interactive web interface at `/interfaces/session-review/` that lets users browse all knowledge session reports.

### Date-Based Session Grouping

Sessions from the same day are automatically grouped under the earliest session as root. This reflects the user's reality: one conversation window per day with multiple system-level session restarts (compaction, crashes, continuation).

- The **earliest session** on each date becomes the day's **root**
- All subsequent sessions on that date become **continuations**
- The root session **aggregates** all children's PRs, metrics, commits, and lines changed

**Tree icons**:

| Icon | Meaning |
|------|---------|
| 💬 | Original session (root of the day) |
| 🔁 | Continuation (child session, same day) |
| 🔗 | Related task (non-session) |

### Pie Charts

4 doughnut charts when data is available:

| Chart | What it shows |
|-------|---------------|
| **Session Scope** | Child Sessions vs Related Tasks — the session's tree structure |
| **Deliverables** | Pull Requests + Commits + Tasks + Lessons — what was produced |
| **Lines Changed** | Additions (green) vs Deletions (red) — code impact balance |
| **Active Time** | Active vs Inactive time — session utilization |

Below the pie charts, a **Code Impact** horizontal bar chart shows additions/deletions per individual PR.

### Data Sources

The Session Viewer reads from `docs/data/sessions.json`, which merges multiple sources:

| Source | What it provides |
|--------|-----------------|
| GitHub Tasks (SESSION label) | Task metadata, comments, timestamps |
| Pull Requests | PR numbers, additions, deletions, commits, files |
| Session notes | Summary, metrics, time blocks, lessons |

---

## Integration with Other Skills

| K2.0 Skill | How it uses session management |
|------------|-------------------------------|
| `/mind-context` | Loads session context (mindmap + near_memory) |
| `/mind-stats` | Reports session memory occupancy |
| `/mind-depth` | Configures mindmap depth for session display |
| `/normalize` | Validates session file structure |
| `/integrity-check` | Checks session memory consistency |
| `/docs-create` | Creates publications, then git commit/push |
| K_GITHUB `sync_github.py` | Syncs session-relevant data with GitHub |

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — session management is a core subsystem |
| 0v2 | [Knowledge 2.0]({{ '/publications/knowledge-2.0/' | relative_url }}) | Architecture — the multi-module design that session scripts implement |
| 3 | [AI Session Persistence]({{ '/publications/ai-session-persistence/' | relative_url }}) | Methodology — the "why" behind session persistence |
| 14 | [Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }}) | Core reference — K_MIND module, memory architecture, script inventory |
| 15 | [Architecture Diagrams]({{ '/publications/architecture-diagrams/' | relative_url }}) | Visual reference — session lifecycle flow, memory tiers |
| 4 | [Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }}) | K_GITHUB sync reads session context as input |
| 19 | [Interactive Work Sessions]({{ '/publications/interactive-work-sessions/' | relative_url }}) | Task received protocol, work cycle |
| 20 | [Session Metrics & Time]({{ '/publications/session-metrics-time/' | relative_url }}) | Metrics compilation from session data |
| 21 | [Main Interface]({{ '/publications/main-interface/' | relative_url }}) | Session Viewer (I1) and Main Navigator (I2) |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
