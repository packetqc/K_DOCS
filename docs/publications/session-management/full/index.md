---
layout: publication
title: "Session Management — Complete Documentation"
description: "Complete documentation for session management commands: wakeup protocol (10 steps), save protocol (semi-automatic delivery), remember (insight persistence), status (state recovery), help (multipart command table), the Free Guy analogy, session notes format, and cross-session recovery."
pub_id: "Publication #8 — Full"
version: "v1"
date: "2026-02-19"
permalink: /publications/session-management/full/
og_image: /assets/og/session-management-en-cayman.gif
keywords: "session, wakeup, save, lifecycle, commands, persistence"
---

# Session Management — Complete Documentation
{: #pub-title}

**Contents**

| | |
|---|---|
| [Authors](#authors) | Publication authors |
| [Abstract](#abstract) | Practical command reference overview |
| [Usage Patterns](#usage-patterns) | Three ways to interact with commands |
| [Quick Reference](#quick-reference) | All 9 session commands at a glance |
| [wakeup — Session Init](#wakeup--session-init) | 11-step bootstrap protocol with context recovery |
| [save — Session Save Protocol](#save--session-save-protocol) | Pre-save summary → commit → push → PR → merge |
| [refresh](#refresh--lightweight-context-restore) | Re-read CLAUDE.md, git status, reprint help (~5s) |
| [resume](#resume--crash-recovery-from-checkpoint) | Crash recovery from checkpoint |
| [recover](#recover--branch-based-work-recovery) | Cherry-pick stranded work from `claude/*` branches |
| [recall](#recall--deep-memory-search) | 4-layer progressive search across all knowledge channels |
| [remember — Persist Insights](#remember--persist-insights) | Append insights to session notes |
| [status — State Summary](#status--state-summary) | Read notes and summarize current state |
| [help — Multipart Command Table](#help--multipart-command-table) | Concatenated knowledge + project commands |
| [Session Lifecycle](#session-lifecycle) | How sessions persist across time |
| &nbsp;&nbsp;[The Free Guy Analogy](#the-free-guy-analogy) | NPC vs aware — the sunglasses moment |
| &nbsp;&nbsp;[Session Notes Format](#session-notes-format) | Done, Remember, Next sections |
| &nbsp;&nbsp;[Cross-Session Recovery](#cross-session-recovery) | How wakeup restores previous session context |
| &nbsp;&nbsp;[Client Disconnect Recovery](#client-disconnect-recovery) | Recovery paths when client disconnects mid-save |
| &nbsp;&nbsp;[Session Runtime Cache](#session-runtime-cache--compaction-resilient-memory) | Compaction-resilient memory layer |
| &nbsp;&nbsp;[Context Loss Recovery](#context-loss-recovery) | Cache-first recovery after compaction |
| [PreToolUse Enforcement (v56)](#pretooluse-enforcement-v56) | Two-layer hook architecture blocking edits until protocol passes |
| [Session Viewer — Interface I1](#session-viewer--interface-i1) | Interactive session browser with pie charts and tree grouping |
| [Integration with Other Commands](#integration-with-other-commands) | How session commands work with harvest, normalize, etc. |
| [Related Publications](#related-publications) | Sibling and parent publications |

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Designed the session lifecycle protocol enabling AI coding assistants to maintain continuity across sessions.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Executes the session lifecycle — wakeup, work, save — maintaining context continuity across hundreds of sessions.

---

## Abstract

Publication #3 (AI Session Persistence) explains the **methodology** — why AI sessions need persistent memory and how CLAUDE.md + notes/ achieves it. This publication is the **practical command reference** — how to use `wakeup`, `save`, `remember`, `status`, and `help` in daily work.

Every session follows the same lifecycle:

```
wakeup → read notes/ → summarize state → work → save → commit & push
```

---

## Usage Patterns

The Knowledge system supports three entry patterns for interacting with commands. All commands in this publication work through any of them.

| Pattern | How | Example | Best for |
|---------|-----|---------|----------|
| **Direct command** | Type the command as your entry prompt | `save` | Known commands, fast one-shot |
| **Natural language** | Describe what you want in plain text | `sauvegarde ma session` | When you don't know the exact syntax |
| **Interactive session** | `interactif` + command or request in description | `interactif` then `resume interrupted work` | Multi-step sessions, chaining commands |

### Direct Command

Type the command name directly as your message:

```
save
```
```
pub list
```
```
harvest healthcheck
```

Fastest path when you know the exact command.

### Natural Language

Describe what you want in your own words — the system maps it to the right command:

```
sauvegarde ma session
```
```
montre-moi les publications existantes
```
```
can you check my satellite projects for new insights?
```

Works in French or English. The intent is recognized and routed to the appropriate command.

### Interactive Session

Start with `interactif` as your entry prompt, then provide a description:

```
interactif
```
> Description: `resume mon travail interrompu et ensuite crée un nouveau projet test`

In interactive mode:
- `help` is displayed automatically at session start
- The session description is analyzed for actionable commands
- Multiple commands can be chained in sequence
- The session stays open for follow-up until `terminé` or `done`

---

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

---

## wakeup — Session Init

The `wakeup` command bootstraps a new Claude session with full context recovery. It is the first thing every session runs.

**Protocol (11 steps):**

| Step | Action | What it does |
|------|--------|-------------|
| 0 | **Put on the sunglasses** | Read `packetqc/knowledge` CLAUDE.md first |
| 0.5 | **Bootstrap scaffold** | Create missing essential files on fresh repos (non-destructive) |
| 0.6 | **Start knowledge beacon** | Launch beacon for inter-instance discovery |
| 0.7 | **Sync upstream** | Fetch and merge the default branch into the current task branch. Pulls any PRs merged since the session started (e.g., `live/` assets, notes, scaffold files). Essential for re-running `wakeup` mid-session without archiving |
| 1 | **Knowledge Evolution** | Report latest entries as "Recent intelligence" |
| 2 | **Distributed minds** | Scan `minds/` for harvested satellite knowledge |
| 3 | **Read notes** | All `notes/` files for cross-session context |
| 4 | **Read plans** | `PLAN.md`, `changelog.txt` for roadmap |
| 5 | **Sync assets** | Copy `live/` folder from knowledge if missing |
| 6 | **Git log** | `git log --oneline -20` for recent activity |
| 7 | **Branches** | `git branch -a` for active branches |
| 8 | **Summarize** | Last session, current state, next steps |
| 9 | **Print help** | Recent intelligence + multipart command table |
| 10 | **Ask user** | What to focus on |

**Access method** — try in order:

| Priority | Method | Notes |
|----------|--------|-------|
| 1 | `git clone https://github.com/packetqc/knowledge` | Full clone |
| 2 | `WebFetch https://raw.githubusercontent.com/packetqc/knowledge/main/CLAUDE.md` | Read-only fallback (if 404, try `/master/`) |

Never use `gh` — always `git` or `WebFetch`.

### Fork & Clone Safety

If you fork or clone this repository, session commands are **owner-scoped** and environmentally isolated:

| Aspect | Protection |
|--------|------------|
| **`wakeup`** | Reads from the original owner's knowledge repo via public HTTPS — a forker gets the methodology (intentionally public) but no credentials or account access |
| **`save`** | Pushes only to the current session's assigned branch — a forker's Claude Code cannot push to the original repo |
| **`notes/`** | Starts blank for every new user — no cross-contamination between owners |
| **Credentials / tokens** | None stored in session notes, CLAUDE.md, or git history |

To use session management for your own projects: replace `packetqc` with your GitHub username in CLAUDE.md. The lifecycle protocol (`wakeup` → work → `save`) adapts to your namespace automatically.

---

## save — Session Save Protocol

Semi-automatic delivery — Claude does 95%, user provides one approval click.

**Protocol (6 steps):**

| Step | Action | Who |
|------|--------|-----|
| 1 | Write session notes to `notes/session-YYYY-MM-DD.md` | Claude |
| 2 | Commit on task branch (`claude/<task-id>`) | Claude |
| 3 | `git push -u origin <task-branch>` | Claude |
| 4 | Detect default branch (`main` or `master`) | Claude |
| 5 | Create PR: task branch → default branch | Claude |
| 6 | Approve/merge the PR | **User** (one click) |

**Why semi-automatic**: Claude Code's proxy restricts push access to the exact assigned branch only. Pushing to the default branch returns HTTP 403. The PR is the bridge — user approval is the gate.

**Todo list rule**: When executing `save`, the todo list must include all 4 autonomous steps as visible items: write notes, commit, push, create PR. A missing PR means stranded work.

**PR creation rules:**

| Rule | Detail |
|------|--------|
| Target | The repo's default branch — detect with `git remote show origin \| grep 'HEAD branch'` (supports both `main` and `master`) |
| Title | Concise summary of session work |
| Body | Summary of changes, session context |
| Duplicates | If a PR already exists, report its URL instead of creating a duplicate |
| Method | Use `gh pr create` |

---

## refresh — Lightweight Context Restore

```
refresh
```

Re-reads CLAUDE.md, performs a strategic remote check, quick git status, re-reads session notes, reprints help. No clone, no sync (~5 seconds). Use after compaction or when methodology rules seem forgotten. Use `wakeup` only when a deep re-sync is needed (other sessions merged PRs, assets changed).

---

## resume — Crash Recovery from Checkpoint

```
resume
```

Reads `notes/checkpoint.json`, verifies git state, restores the todo list, and restarts the protocol from the last completed step. Checkpoints are written automatically at step boundaries by checkpoint-aware commands (`save`, `harvest`, `normalize --fix`, `pub new`, `wakeup`). Auto-deletes the checkpoint on successful resume.

Offered automatically during `wakeup` step 0.9 when a checkpoint file is detected.

---

## recover — Branch-Based Work Recovery

```
recover
```

Searches `claude/*` branches for stranded work — commits that were pushed but never merged via PR. Shows unmerged commits, file diffs, and PR status for each branch. Offers two recovery paths:

| Path | Method | When to use |
|------|--------|-------------|
| **Cherry-pick** | Apply specific commits from stranded branch | When commits are clean and self-contained |
| **Diff-apply** | Extract diff and apply as new commit | When commits overlap with current work |

Complements `resume` (checkpoint-based recovery). `recover` recovers from pushed branches where no checkpoint exists — e.g., after a container restart or session crash after `git push` but before PR creation.

---

## recall — Deep Memory Search

```
recall <keyword or question>
```

Hybrid command that searches across all knowledge channels to find information from past sessions. Searches progressively through 4 layers, stopping when an answer is found:

| Layer | Time | What it searches |
|-------|------|------------------|
| **Near memory** | ~5s | Current session cache, recent `notes/session-runtime-*.json`, recent `notes/session-*.md` |
| **Git memory** | ~10s | Commit messages, branch names, file diffs across `claude/*` branches |
| **GitHub memory** | ~15s | Issue titles/comments, PR descriptions, board items (requires elevation) |
| **Deep memory** | ~30s | Full-text search across publications, methodology, patterns, lessons, minds/ |

Deeper layers require `AskUserQuestion` confirmation before proceeding. If stranded branch work is found, suggests `recover` to cherry-pick/apply it. `recall` finds, `recover` acts.

---

## remember — Persist Insights

```
remember Add creation date and version to all publications
```

Appends text to the current session notes file. Insights carry forward to future sessions via `wakeup`.

**Common uses:**

| Use case | Example |
|----------|---------|
| Record a decision | `remember Chose WAL mode for SQLite concurrent access` |
| Flag for harvest | `remember harvest: Page cache sizing degrades at 81%` |
| Track a todo | `remember Next session: test the checkpoint strategy` |
| Record a preference | `remember User prefers French commit messages` |

**Harvest integration**: Text starting with `harvest:` gets collected by the `harvest` command when crawling satellite projects. This is how insights flow from session notes → `minds/` → core knowledge.

---

## status — State Summary

```
status
```

Reads all `notes/` files and produces a concise summary:

| Section | Content |
|---------|---------|
| Last activity | Most recent session work |
| Pending items | Remembered directives awaiting action |
| Active branches | Current and recent `claude/*` branches |
| Plan state | Current roadmap and next steps |

Designed for quick pickup after a break — everything you need in one view.

---

## help — Multipart Command Table

```
help
```

Outputs a **concatenated** command table in two parts:

**Part 1 — Knowledge commands** (from `packetqc/knowledge`):

| Group | Commands |
|-------|----------|
| Session management | `wakeup`, `help`, `status`, `save`, `remember` |
| Normalize | `normalize`, `normalize --fix`, `normalize --check` |
| Harvest | All `harvest` subcommands |
| Publications | `pub list`, `pub check`, `pub new`, `pub sync`, `docs check` |
| Webcards | `webcard` targets |
| Live session | `I'm live`, `multi-live`, `deep`, `analyze`, `recipe` |

**Part 2 — Project commands** (from the project's own CLAUDE.md):

| Aspect | Detail |
|--------|--------|
| Source | The project's own CLAUDE.md |
| Content | Varies per project |
| Example | `vanilla <NAME> <LED>` for MPLIB projects |

**Rule**: Knowledge commands come from `packetqc/knowledge`. Project commands come from the project's own CLAUDE.md. Never duplicate — concatenate.

---

## Session Lifecycle

### The Free Guy Analogy

Without `notes/` and `CLAUDE.md`, every Claude session is an **NPC** — stateless, no memory, same blank start. With the `wakeup` → work → `save` loop, each session inherits everything the previous one learned.

`wakeup` is putting on the sunglasses. Without the sunglasses, you're just another NPC — walking around, responding to prompts, with no awareness of yesterday.

```
NPC (no context) → wakeup → AWARE (full context) → work → save → next session inherits
```

### Session Notes Format

Notes are stored in `notes/session-YYYY-MM-DD.md`:

```markdown
# Session Notes — 2026-02-19

## Done
1. Created Publication #5 (Webcards & Social Sharing)
2. Fixed layout language concordance
3. Updated version tables across all publications

## Remember
- Add creation date, modification date, and version to all docs/pubs
- User prefers combined doc+pub creation workflow

## Next
- Create remaining publications (#6, #7, #8)
- Implement asset automation when publications include images/video
```

### Cross-Session Recovery

On `wakeup`:

| Step | What happens |
|------|-------------|
| 1 | All `notes/` files are read chronologically |
| 2 | The most recent session's "Next" section becomes the starting point |
| 3 | "Remember" directives accumulate — they're never deleted, only acted upon |
| 4 | "Done" sections provide context for what was achieved |

**Recovery time**: ~30 seconds with `wakeup` vs ~15 minutes of manual re-explanation without it.

### Client Disconnect Recovery

When the client interface (browser tab, desktop app, VS Code) disconnects mid-session — after commits have been pushed but before PR creation completes — the work is safe on the remote branch. The **git push is the durability boundary**.

| Path | Method | Speed |
|------|--------|-------|
| **A** | Browser refresh / session resume | Instant |
| **B** | Manual PR creation (`gh_helper.py` or GitHub web UI) | Minutes |
| **C** | New session + `resume` command | ~10s |
| **D** | Wait for harvest | Hours/days (not recommended) |

**Key insight**: PR creation is **idempotent** — re-running it for a branch that already has a PR returns the existing PR URL, not a duplicate.

### Session Runtime Cache — Compaction-Resilient Memory

The session runtime cache (`notes/session-runtime-<suffix>.json`) is the **compaction-resilient memory layer**. Data written here survives context compression, crash, and container restart. It is the fourth persistence channel — beyond git, notes, and GitHub issues.

**Multi-session naming convention**: Each session has its own cache file, named after the branch suffix:

| Branch | Cache file |
|--------|-----------|
| `claude/session-cache-qa-0o1sQ` | `session-runtime-0o1sQ.json` |
| `claude/fix-webcards-abc12` | `session-runtime-abc12.json` |

This prevents multiple concurrent sessions from overwriting each other's state.

**Core functions** (from `scripts/session_agent.py`):

```python
from scripts.session_agent import write_runtime_cache, read_runtime_cache, update_session_data

# Write full cache on session start
write_runtime_cache(repo="packetqc/knowledge", issue_number=521,
                    issue_title="SESSION: ...", branch="claude/task-xyz")

# Read cache after compaction/crash
cache = read_runtime_cache()
issue = cache["issue_number"]
request = cache["request_description"]
data = cache.get("session_data", {})

# Update individual keys during work
update_session_data("current_todo", "Fix authentication bug")
```

**What gets persisted in `session_data`**:

| Key | Type | Purpose |
|-----|------|---------|
| `comment_ids` | Map of step → comment ID | PATCH ⏳→✅ on existing comments |
| `decisions` | List of strings | Key decisions for context recovery |
| `current_todo` | String | Current in-progress todo step |
| `files_modified` | List of paths | Scope awareness for commits |
| `parent_issue` | Integer | Parent issue linkage |
| `labels` | List of strings | Issue labels applied |
| `request_addon` | List of `{index, timestamp, verbatim}` | User add-on comments verbatim |
| `request_addon_synthesis` | List of `{index, timestamp, synthesis}` | Claude's interpretation of each add-on |
| `todo_snapshot` | List of `{content, status}` | Full todo list state |
| `session_phase` | String | Lifecycle phase (wakeup/planning/executing/saving/delivered) |
| `pr_numbers` | List of `{number, title, status}` | PRs created this session |
| `git_state` | `{last_commit_sha, uncommitted_count, timestamp}` | Branch state verification |
| `time_markers` | List of `{event, timestamp}` | Timeline for metrics compilation |
| `elevation_status` | Boolean | Whether GH_TOKEN is available |
| `default_branch` | String | Detected default branch name |
| `work_summary` | String | Running summary of accomplishments |
| `errors_encountered` | List of `{error, timestamp}` | Error log for pattern detection |
| `issue_comments_count` | Integer | Comment count for integrity check |

**Auto-commit on write**: Every cache write is automatically committed to git. Both `write_runtime_cache()` and `update_session_data()` call `commit_cache()` immediately after writing to disk — the cache file is `git add`ed and committed with a descriptive message. This ensures the cache is recoverable via `recover` even if the session crashes before a manual commit.

**Dedicated helper functions**:

```python
from scripts.session_agent import (
    append_request_addon, read_request_addons,
    update_todo_snapshot, update_session_phase, append_pr_number,
    update_git_state, append_time_marker, update_elevation_status,
    update_default_branch, update_work_summary, append_error,
    update_issue_comments_count
)
```

#### Request Add-Ons — Mid-Session Instruction Tracking

When a user provides supplementary instructions during work, they are stored as **add-ons** — paired verbatim + synthesis entries:

```python
append_request_addon(
    verbatim="please also add error handling for the edge case...",
    synthesis="Add error handling for empty input in validation step."
)
addons = read_request_addons()
```

Add-ons are **live working data** — sessions must read them on recovery and check them before each todo step.

### Context Loss Recovery

When a session hits the context window limit, the conversation gets **compacted**. The mind is lost, but the git state and session cache survive.

**Recovery protocol** (ordered by priority):

| Step | Action |
|------|--------|
| 1 | **Read session cache** — `read_runtime_cache()` recovers issue number, request description, all session_data (decisions, comment IDs, todo state, add-ons, phase, PR numbers). This is the **first recovery action**. |
| 2 | **Run `refresh`** — re-reads CLAUDE.md, quick git status, reprints help. Restores formatting rules and methodology. |
| 3 | **Run the git recovery line** — `git branch --show-current && git status -s && git log --oneline -10` |
| 4 | **Read `notes/`** — session notes if written before compaction |
| 5 | **Resume work** — no ramp-up, no re-explanation needed |

**Recovery comparison**:

| Scenario | Recovery mechanism | Time |
|----------|-------------------|------|
| New session (cold start) | `wakeup` — full protocol | ~30 seconds |
| Context loss (mid-session) | Session cache + `refresh` | ~10 seconds |
| Crash (checkpoint exists) | `resume` from checkpoint | ~10 seconds |
| Crash (no checkpoint) | `recover` from stranded branch | ~15 seconds |
| Deep memory search | `recall` from session history | ~10 seconds |
| Manual (no tooling) | User re-explains everything | ~15 minutes |

---

## PreToolUse Enforcement (v56)

Two-layer hook architecture that ensures every session follows the protocol before modifying files.

**Architecture**:

| Layer | Hook Event | Can block? | Purpose |
|-------|-----------|------------|---------|
| **SessionStart** | Session init | No (inform only) | Initialize state file, print environment summary |
| **PreToolUse** | Before `Edit\|Write\|NotebookEdit` | **Yes** (exit 2 = deny) | Enforce gates, block edits until protocol passes |

**Enforcement gates**:

| Gate | Field | Unlocked by | Prevents |
|------|-------|-------------|----------|
| **G1 — Protocol** | `protocol_completed` | `update_enforcement_state()` after wakeup integrity check (step 0.35) | Editing files without completing wakeup |
| **G2 — Issue** | `issue_created` | `write_runtime_cache()` with issue number (automatic) | Editing files without a tracking issue |
| **G7 — Exchanges** | `last_post_time` | `post_exchange()` on each comment (continuous) | Warning if >5 min since last issue comment |

**State file**: `/tmp/.claude-session-state.json` — ephemeral, per-container.

**Exceptions** (always allowed): `/tmp/*`, `.claude/*`, `notes/session-runtime-*`, `notes/checkpoint.json`.

**Key insight**: `SessionStart` can only inform. `PreToolUse` can enforce (deny). The v1 system had information without enforcement — Claude read 100 lines of ASCII protocol rules and ignored them entirely. The v2 system blocks file edits until the protocol is done. The deny message tells any Claude instance exactly how to unblock.

---

## Session Viewer — Interface I1

The Session Viewer is an interactive web interface at `/interfaces/session-review/` that lets users browse all knowledge session reports. Select any session from the dropdown to see its complete report.

### Date-Based Session Grouping

Sessions from the same day are automatically grouped under the earliest session as root. This reflects the user's reality: one conversation window per day with multiple system-level session restarts (compaction, crashes, continuation).

- The **earliest session** (by issue creation time) on each date becomes the day's **root** (💬 original)
- All subsequent sessions on that date become **continuations** (🔁)
- The root session **aggregates** all children's PRs, metrics, commits, lines changed, and comments
- Selecting the root session shows the combined picture of the entire day's work

**Tree icons**:

| Icon | Meaning | In dropdown | In issues table |
|------|---------|-------------|-----------------|
| 💬 | Original session (root) | Before title | Parent session link |
| 🔁 | Continuation (child) | Before title | Child session link |
| 🔗 | Related issue (non-session) | — | Non-tree issue link |

### Pie Charts

The Session Viewer displays 4 doughnut charts when data is available:

| Chart | Position | What it shows |
|-------|----------|---------------|
| **Session Scope** | 1st | Child Sessions vs Related Issues — the session's tree structure at a glance |
| **Deliverables** | 2nd | Pull Requests + Commits + Issues + Lessons — what was produced |
| **Lines Changed** | 3rd | Additions (green) vs Deletions (red) — code impact balance |
| **Active Time** | 4th | Active vs Inactive time — session utilization |

Below the pie charts, a **Code Impact** horizontal bar chart shows additions/deletions per individual PR with #number labels.

### Data Sources

The Session Viewer reads from `docs/data/sessions.json`, generated by `generate_sessions.py` which merges 4 sources:

| Source | Type | What it provides |
|--------|------|-----------------|
| GitHub Issues (SESSION label) | Real-time | Issue metadata, comments, timestamps |
| Pull Requests | Real-time | PR numbers, additions, deletions, commits, files |
| Session notes (`notes/session-*.md`) | Batch | Summary, metrics, time blocks, lessons |
| Runtime cache (`notes/session-runtime-*.json`) | Real-time | Todo state, phase, decisions, request description |

---

## Integration with Other Commands

| Command | How it uses session management |
|---------|-------------------------------|
| `harvest` | Reads `remember harvest:` flags from session notes |
| `normalize` | Recommended before `save` to catch issues |
| `I'm live` | Pauses regular workflow during live monitoring |
| `pub new` | Creates files, then `save` commits them |
| `webcard` | Generates GIFs, then `save` commits them |
| All write commands | End with `save` to deliver via PR |

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — session management is a core subsystem |
| 3 | [AI Session Persistence]({{ '/publications/ai-session-persistence/' | relative_url }}) | Methodology — the "why" behind these commands |
| 4 | [Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }}) | harvest reads session notes as input data |
| 7 | [Harvest Protocol]({{ '/publications/harvest-protocol/' | relative_url }}) | harvest processes flagged `remember harvest:` notes |
| 19 | [Interactive Work Sessions]({{ '/publications/interactive-work-sessions/' | relative_url }}) | On task received protocol, issue lifecycle |
| 20 | [Session Metrics & Time]({{ '/publications/session-metrics-time/' | relative_url }}) | Pre-save metrics compilation, time blocks |
| 21 | [Main Interface]({{ '/publications/main-interface/' | relative_url }}) | Session Viewer (I1) and Main Navigator (I2) |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
