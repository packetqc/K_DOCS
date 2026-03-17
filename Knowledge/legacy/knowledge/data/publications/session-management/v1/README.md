# Session Management — Commands Reference

**Publication #8 — Practical Guide to AI Session Lifecycle**

*By Martin Paquet & Claude (Anthropic, Opus 4.6)*
*v1 — February 2026*

---

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

These commands manage that lifecycle. This guide documents each one with usage, behavior, examples, and integration with the rest of Knowledge.

---

## Table of Contents

- [Quick Reference](#quick-reference)
- [wakeup — Session Init](#wakeup--session-init)
- [save — Session Save Protocol](#save--session-save-protocol)
- [refresh — Lightweight Context Restore](#refresh--lightweight-context-restore)
- [resume — Crash Recovery from Checkpoint](#resume--crash-recovery-from-checkpoint)
- [recover — Branch-Based Work Recovery](#recover--branch-based-work-recovery)
- [recall — Deep Memory Search](#recall--deep-memory-search)
- [remember — Persist Insights](#remember--persist-insights)
- [status — State Summary](#status--state-summary)
- [help — Multipart Command Table](#help--multipart-command-table)
- [Session Lifecycle](#session-lifecycle)
  - [The Free Guy Analogy](#the-free-guy-analogy)
  - [Session Notes Format](#session-notes-format)
  - [Cross-Session Recovery](#cross-session-recovery)
- [PreToolUse Enforcement (v56)](#pretooluse-enforcement-v56)
- [Session Viewer — Interface I1](#session-viewer--interface-i1)
  - [Date-Based Session Grouping](#date-based-session-grouping)
  - [Pie Charts](#pie-charts)
- [Integration with Other Commands](#integration-with-other-commands)
- [Related Publications](#related-publications)

---

## Usage Patterns

The Knowledge system supports three entry patterns for interacting with commands. All commands in this publication work through any of them.

| Pattern | How | Example | Best for |
|---------|-----|---------|----------|
| **Direct command** | Type the command as your entry prompt | `save` | Known commands, fast one-shot |
| **Natural language** | Describe what you want in plain text | `sauvegarde ma session` | When you don't know the exact syntax |
| **Interactive session** | `interactif` + command or request in description | `interactif` then `resume interrupted work` | Multi-step sessions, chaining commands |

In interactive mode, `help` is displayed automatically at session start — showing all available commands. The session stays open for follow-up commands until `terminé` or `done`.

See `methodology/commands.md` § "Usage Patterns — Three Ways to Work" for detailed examples.

---

## Quick Reference

| Command | Action |
|---------|--------|
| `wakeup` | Session init — read knowledge, notes, sync assets, print commands |
| `save` | Pre-save summary → commit → push → PR → merge (elevated) or guide |
| `refresh` | Lightweight context restore — re-read CLAUDE.md, git status, reprint help (~5s) |
| `resume` | Crash recovery from `notes/checkpoint.json` |
| `recover` | Search `claude/*` branches for stranded work, cherry-pick/apply |
| `recall <keyword>` | Deep memory search across all knowledge channels |
| `remember ...` | Append text to current session notes file |
| `status` | Read `notes/` and summarize current state |
| `help` / `?` | Print multipart command table (knowledge + project) |

---

## wakeup — Session Init

The `wakeup` command bootstraps a new Claude session with full context recovery. It is the first thing every session runs — the "sunglasses moment."

**Protocol (10 steps):**

1. **Put on the sunglasses** — Read `packetqc/knowledge` CLAUDE.md first
2. **Sync upstream** — Fetch and merge the default branch into the current task branch. Pulls any PRs merged since the session started (e.g., `live/` assets, notes, scaffold files). Essential for re-running `wakeup` mid-session without archiving
3. **Knowledge Evolution check** — Report latest entries as "Recent intelligence"
4. **Read distributed minds** — Scan `minds/` for harvested satellite knowledge
5. Read all `notes/` files — recover cross-session context
6. Read `PLAN.md`, `changelog.txt` — current roadmap + recent history
7. **Sync knowledge assets** — if `live/` folder missing, copy from knowledge
8. Run `git log --oneline -20` — recent commit activity
9. Run `git branch -a` — active branches
10. Summarize: last session, current state, next steps, active branches
11. **Print intelligence + help** — recent evolution entries + multipart command table

**Access method** — try in order:
1. `git clone https://github.com/packetqc/knowledge` — full clone
2. `WebFetch https://raw.githubusercontent.com/packetqc/knowledge/main/CLAUDE.md` — read-only fallback (if 404, try `/master/`)

**Output**: Summary of last session state, what changed since, active branches, next actions, and the full command table.

### Fork & Clone Safety

If you fork or clone this repository, session commands are **owner-scoped** and environmentally isolated:

- **`wakeup`** reads from the original owner's knowledge repo via public HTTPS — a forker gets the methodology (intentionally public) but no credentials or account access
- **`save`** pushes only to the current session's assigned branch — a forker's Claude Code cannot push to the original repo
- **`notes/`** starts blank for every new user — no cross-contamination between owners
- **No credentials or tokens** are stored in session notes, CLAUDE.md, or git history

To use session management for your own projects: replace `packetqc` with your GitHub username in CLAUDE.md. The lifecycle protocol (`wakeup` → work → `save`) adapts to your namespace automatically.

---

## save — Session Save Protocol

The `save` command persists session context and delivers work to the default branch (`main` or `master`) via PR with user approval.

**Protocol (6 steps):**

1. Write session notes to `notes/session-YYYY-MM-DD.md`
2. Commit on current branch (the assigned `claude/<task-id>` branch)
3. `git push -u origin <assigned-task-branch>`
4. Detect default branch: `git remote show origin | grep 'HEAD branch'`
5. Create PR: task branch → default branch (if no PR exists yet)
6. User approves PR → merge lands on default branch

**Why semi-automatic**: Claude Code's proxy restricts push access to the exact assigned branch only. Pushing to the default branch returns 403. The PR is the bridge that crosses this boundary — user approval is the gate.

**What Claude does autonomously**: commit, push to task branch, create PR.

**What requires user action**: approve/merge the PR (one click in GitHub).

**Todo list rule**: When executing `save`, the todo list must include all 4 autonomous steps: write notes, commit, push, create PR.

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

1. **Cherry-pick** — apply specific commits from the stranded branch to the current branch
2. **Diff-apply** — extract the diff and apply it as a new commit

Complements `resume` (which recovers from checkpoint files). `recover` recovers from pushed branches where no checkpoint exists — e.g., after a container restart or session crash after `git push` but before PR creation.

**When to use**: After `resume` finds no checkpoint, or when `recall` discovers stranded work on a `claude/*` branch.

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

Deeper layers require `AskUserQuestion` confirmation before proceeding. If stranded branch work is found, suggests `recover` to cherry-pick/apply it.

---

## remember — Persist Insights

```
remember Add creation date and version to all publications
```

Appends the text to the current session notes file (`notes/session-YYYY-MM-DD.md`). Used to persist insights, decisions, and directives that should carry forward to future sessions.

**Common uses:**
- Record a decision: `remember Chose WAL mode for SQLite concurrent access`
- Flag for harvest: `remember harvest: Page cache sizing degrades at 81%`
- Track a todo: `remember Next session: test the checkpoint strategy`
- Record a preference: `remember User prefers French commit messages`

**Harvest flags**: Text starting with `harvest:` gets collected by the `harvest` command when crawling satellite projects.

---

## status — State Summary

```
status
```

Reads all `notes/` files and summarizes the current project state: last session activity, pending items, active branches, remembered directives.

**Output**: Concise summary suitable for picking up work after a break — what was done, what's next, any blockers.

---

## help — Multipart Command Table

```
help
```

Outputs a **concatenated** command table:

1. **Part 1 — Knowledge commands**: Session management + harvest + content management + live analysis (from `packetqc/knowledge`)
2. **Part 2 — Project commands**: Project-specific commands (from the project's own CLAUDE.md)

Part 1 is always present (inherited from knowledge). Part 2 varies per project. Never duplicate — concatenate.

---

## Session Lifecycle

### The Free Guy Analogy

Without `notes/` and `CLAUDE.md`, every Claude session is an **NPC** — stateless, no memory, same blank start. With the `wakeup` → work → `save` loop, each session inherits everything the previous one learned. Every new Claude instance that reads this repo gets "the sunglasses" — instant awareness.

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

## Remember
- Add creation date and version to all publications

## Next
- Create remaining publications (#6, #7, #8)
```

### Cross-Session Recovery

On `wakeup`, all `notes/` files are read chronologically. The most recent session's "Next" section becomes the starting point. "Remember" directives accumulate across sessions — they're never deleted, only acted upon.

**Recovery time**: ~30 seconds with `wakeup` vs ~15 minutes of manual re-explanation.

### Client Disconnect Recovery

When the client interface (browser tab, desktop app, VS Code) disconnects mid-session — after commits have been pushed but before PR creation completes — the work is safe on the remote branch. The **git push is the durability boundary**.

```
Session work → git push (durable) → PR creation (ephemeral)
                  ↑                        ↑
              survives disconnect     may need re-execution
```

**Recovery paths** (ordered by speed):

| Path | Method | Speed | Recommended |
|------|--------|-------|-------------|
| **A** | Browser refresh / session resume | Instant | Yes (preferred) |
| **B** | Manual PR creation (`gh_helper.py` or GitHub web UI) | Minutes | Yes (if A fails) |
| **C** | New session + `resume` command | ~10s | Yes (if A+B fail) |
| **D** | Wait for harvest | Hours/days | No (too slow) |

**Path A**: Refresh the browser tab — the session may still be alive server-side. Claude Code web sessions persist state across reconnects.

**Path B**: If the session is dead, create the PR manually from the orphan branch: `https://github.com/packetqc/<repo>/compare/<default>...<branch>` or via `gh_helper.py`.

**Path C**: Start a new session, run `resume` — the checkpoint-based recovery creates the PR.

**Key insight**: PR creation is **idempotent** — re-running it for a branch that already has a PR returns the existing PR URL, not a duplicate.

See `methodology/client-disconnect-recovery.md` for the full protocol and resiliency guarantees.

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

**Dedicated helper functions** — each key has a specialized function that handles validation, appending, and deduplication:

```python
from scripts.session_agent import (
    append_request_addon, read_request_addons,
    update_todo_snapshot, update_session_phase, append_pr_number,
    update_git_state, append_time_marker, update_elevation_status,
    update_default_branch, update_work_summary, append_error,
    update_issue_comments_count
)
```

**Auto-commit on write**: Every cache write is automatically committed to git. Both `write_runtime_cache()` and `update_session_data()` call `commit_cache()` immediately after writing to disk — the cache file is `git add`ed and committed with a descriptive message. This ensures the cache is recoverable via `recover` even if the session crashes before a manual commit.

**Write frequency**: Update at every significant state change — after creating a comment, making a key decision, completing a todo step, creating a PR, transitioning phases, and encountering errors. Each write auto-commits.

#### Request Add-Ons — Mid-Session Instruction Tracking

When a user provides supplementary instructions during work (clarifications, updates, scope changes), they are stored as **add-ons** — paired verbatim + synthesis entries that extend the original `request_description`:

```python
# Store a user add-on
append_request_addon(
    verbatim="please also add error handling for the edge case...",
    synthesis="Add error handling for empty input in validation step."
)

# Read all add-ons after compaction
addons = read_request_addons()
for a in addons:
    print(f"#{a['index']}: {a['synthesis']}")
```

Add-ons are **live working data** — sessions must read them on recovery and check them before each todo step. They are the accumulated instructions that survive compaction, ensuring mid-session corrections are never lost.

### Context Loss Recovery

When a session hits the context window limit, the conversation gets **compacted** — prior messages are summarized and the session continues with a fresh context. The mind is lost, but the git state and session cache survive.

**Recovery protocol** (ordered by priority):

1. **Read session cache** — `read_runtime_cache()` recovers issue number, request description, all session_data (decisions, comment IDs, todo state, add-ons, phase, PR numbers). This is the **first recovery action**.
2. **Run `refresh`** — re-reads CLAUDE.md, quick git status, reprints help. Restores formatting rules and methodology.
3. **Run the git recovery line** — confirms branch, uncommitted work, recent commits:

```bash
git branch --show-current && git status -s && git log --oneline -10
```

4. **Read `notes/`** — session notes if written before compaction
5. **Resume work** — no ramp-up, no re-explanation needed

**Why the session cache matters**: Git tells you what code changed. Notes tell you what was discussed. The session cache tells you **what you were doing** — which todo step was in progress, what decisions were made, what errors were hit, what PRs were created. Without the cache, recovery requires manually reconstructing session state from git log and notes. With the cache, recovery is one function call.

**Recovery comparison**:

| Scenario | Recovery mechanism | Time |
|----------|-------------------|------|
| New session (cold start) | `wakeup` — full protocol | ~30 seconds |
| Context loss (mid-session) | Session cache + `refresh` | ~10 seconds |
| Crash (checkpoint exists) | `resume` from checkpoint | ~10 seconds |
| Crash (no checkpoint) | `recover` from stranded branch | ~15 seconds |
| Deep memory search | `recall` — search past sessions, patterns, decisions | ~10 seconds |
| Manual (no tooling) | User re-explains everything | ~15 minutes |

---

## PreToolUse Enforcement (v56)

Two-layer hook architecture that ensures every session follows the protocol before modifying files:

1. **SessionStart hook** — initializes the enforcement state file (`/tmp/.claude-session-state.json`) and prints a short environment summary. Non-blockable — informs only.
2. **PreToolUse hook** — blocks `Edit|Write|NotebookEdit` until two gates pass:

| Gate | Field | Unlocked by | Prevents |
|------|-------|-------------|----------|
| **G1 — Protocol** | `protocol_completed` | `update_enforcement_state()` after wakeup integrity check | Editing files without completing wakeup |
| **G2 — Issue** | `issue_created` | `write_runtime_cache()` with issue number | Editing files without a tracking issue |
| **G7 — Exchanges** | `last_post_time` | `post_exchange()` on each comment | Warning if >5 min since last issue comment |

Exceptions: `/tmp/*`, `.claude/*`, session cache files are always allowed. The deny message tells any Claude instance exactly how to unblock — even with zero knowledge system context.

**Key insight**: `SessionStart` can only inform. `PreToolUse` can enforce (exit code 2 = deny). The v1 system had information without enforcement. The v2 system has both.

---

## Session Viewer — Interface I1

The Session Viewer is an interactive web interface (`/interfaces/session-review/`) that lets users browse session reports. Select any session from the dropdown to see its summary, metrics, time compilation, deliveries, issues, and lessons.

### Date-Based Session Grouping

Sessions from the same day are automatically grouped under the earliest session as root. This reflects the user's reality: one conversation window per day with multiple system-level session restarts.

- The earliest session (by issue creation time) becomes the day's **root** (💬 original)
- All subsequent sessions on that date become **continuations** (🔁)
- The root session aggregates all children's PRs, metrics, commits, and lines changed
- When you select the root session, you see the combined data from the entire day's work

Tree icons in the dropdown and issues table:

| Icon | Meaning |
|------|---------|
| 💬 | Original session (root of day's tree) |
| 🔁 | Continuation (child session, same day) |
| 🔗 | Related issue (non-session) |

### Pie Charts

The Session Viewer displays 4 doughnut charts when data is available:

| Chart | Position | What it shows |
|-------|----------|---------------|
| **Session Scope** | 1st | Child Sessions vs Related Issues — the session's tree structure |
| **Deliverables** | 2nd | Pull Requests, Commits, Issues, Lessons — what was produced |
| **Lines Changed** | 3rd | Additions (green) vs Deletions (red) — code impact balance |
| **Active Time** | 4th | Active vs Inactive time — session utilization |

Below the pie charts, a **Code Impact** horizontal bar chart shows additions/deletions per individual PR.

---

## Integration with Other Commands

| Command | How it uses session management |
|---------|-------------------------------|
| `harvest` | Reads session `remember harvest:` flags |
| `normalize` | Recommended before `save` |
| `I'm live` | Pauses session management during live monitoring |
| `pub new` | Creates files, then `save` commits them |
| `webcard` | Generates GIFs, then `save` commits them |

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | Knowledge | Parent — session management is a core subsystem |
| 3 | AI Session Persistence | Methodology — the "why" behind these commands |
| 4 | Distributed Minds | harvest reads session notes as input data |
| 7 | Harvest Protocol | harvest --review processes flagged `remember harvest:` notes |
| 19 | Interactive Work Sessions | On task received protocol, issue lifecycle |
| 20 | Session Metrics & Time | Pre-save metrics compilation, time blocks |
| 21 | Main Interface | Session Viewer (I1) and Main Navigator (I2) |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
