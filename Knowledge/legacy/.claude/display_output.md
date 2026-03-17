# Quick Commands Reference

The user types short phrases to trigger specific Claude actions.

---

## Multipart Help Architecture

The `help` command outputs a **concatenated** command table from two sources:

```
┌───────────────────────────────────┐
│  Part 1: Knowledge Commands       │  ← from packetqc/knowledge (this repo)
│  (session + live analysis)        │     Always present in every project
├───────────────────────────────────┤
│  Part 2: Project Commands         │  ← from <project>/CLAUDE.md
│  (project-specific)               │     Varies per project
└───────────────────────────────────┘
```

**Rule**: Any repo that reads `packetqc/knowledge` inherits Part 1 automatically. Part 2 is defined by each project independently. Commands are never duplicated — they are concatenated.

---

## Usage Patterns — Three Ways to Work

The Knowledge system accepts requests through **three entry patterns**. Every command listed below works with all three — choose the pattern that fits your workflow.

### 1. Direct Command

Type a command as your session entry prompt. The system detects the command, executes it, and reports the result.

```
project create mon projet
```
```
harvest --healthcheck
```
```
pub check --all
```

**Best for**: Known commands with clear syntax. Fast, one-shot execution.

### 2. Natural Language

Describe what you want in plain language. The system interprets your intent and maps it to the appropriate command or workflow.

```
peux-tu me créer un projet ayant comme titre "go for it"
```
```
vérifie la fraîcheur de toutes mes publications
```
```
j'aimerais voir l'état du réseau de satellites
```

**Best for**: When you know what you want but not the exact command syntax. The system understands intent and acts accordingly.

### 3. Interactive Session

Enter interactive mode with a command or request in the description. The system starts an interactive session, displays `help` automatically, executes your initial request, then stays in free-form mode for follow-up work.

```
interactif
project create mon nouveau projet
```
```
interactif
je veux créer un projet, ajouter des publications et générer les webcards
```
```
interactif
diagnostic sur le pipeline de build
```

**Best for**: Multi-step work sessions, exploratory tasks, or when you want to chain several operations. The session persists until you type `terminé` or `done`.

### Pattern Comparison

| Pattern | Entry | Execution | Session | Follow-up |
|---------|-------|-----------|---------|-----------|
| **Direct** | Command syntax | Immediate | Single command | New prompt needed |
| **Natural language** | Plain text | Interpreted → executed | Single request | New prompt needed |
| **Interactive** | `interactif` + description | Help displayed → request executed | Persistent free-form | Type next command or `terminé` |

**Key insight**: The interactive pattern combines the best of both worlds — your initial description (command or natural language) starts the first task, and the persistent session lets you continue with any combination of commands, natural language, or free-form instructions until you're done.

---

## Part 1 — Knowledge Commands (Always Available)

### Session Management

| Command | What Claude Does |
|---------|-----------------|
| `wakeup` | **Auto-runs on session start** — never type as entry prompt. Mid-session: deep re-sync after PRs merged |
| `refresh` | Lightweight mid-session context restore — re-read CLAUDE.md, git status, reprint help |
| `help` / `aide` / `?` | **Multipart help** — print knowledge commands + project-specific commands (concatenated) |
| `status` | Read `notes/` and summarize current state |
| `save` | Pre-save summary (v50) → save context, commit, push, create PR to default branch |
| `remember ...` | Append text to current session notes |
| `elevate` | Elevate session to full autonomous — detects `GH_TOKEN` env var or `/tmp/.gh_token` temp file |
| `resume` | Resume interrupted session from checkpoint (crash recovery) |
| `recover` | Search `claude/*` branches for stranded work, cherry-pick/apply to current branch (resiliency) |
| `recall` | Deep memory search across all knowledge channels — near memory first, deeper with confirmation |
| `checkpoint` | Show current checkpoint state (or "no active checkpoint" if none) |
| `normalize` | Audit and fix knowledge structure concordance |
| `normalize --fix` | Apply concordance fixes automatically |
| `normalize --check` | Report only, no changes |
| `<cmd> ?` | Contextual help for any command — usage, examples, publication link |

### Harvest — Distributed Knowledge

| Command | What Claude Does |
|---------|-----------------|
| `harvest <project>` | Pull distributed knowledge from a satellite project into `minds/` |
| `harvest --list` | List all harvested projects with version + drift status |
| `harvest --procedure` | Guided promotion walkthrough — steps, state, next actions |
| `harvest --healthcheck` | Full network sweep — all satellites, update dashboard, process auto-promotes |
| `harvest --review <N>` | Mark insight #N as reviewed (human validated) |
| `harvest --stage <N> <type>` | Stage for integration (type: lesson, pattern, methodology, evolution, docs, project) |
| `harvest --promote <N>` | Promote to core knowledge now (writes to patterns/ or lessons/) |
| `harvest --auto <N>` | Enable auto-promote on next healthcheck run |
| `harvest --fix <project>` | Update satellite's CLAUDE.md to latest knowledge version |
| `harvest <cmd> ?` | Contextual help for any harvest subcommand |

### Content Management

| Command | What Claude Does |
|---------|-----------------|
| `pub list` | List all publications with source/docs/webcard status |
| `pub check <#>` | Validate one publication (source, docs EN/FR, webcard, links, front matter) |
| `pub check --all` | Validate all publications |
| `pub new <slug>` | Scaffold new publication (source + docs EN/FR + front matter + webcard placeholder) |
| `pub sync <#>` | Sync source publication changes to docs web pages |
| `doc review --list` | Quick freshness inventory — version + severity per publication |
| `doc review <#>` | Review publication against current knowledge state |
| `doc review --all` | Review all publications for freshness |
| `docs check <path>` | Validate one doc page (front matter, links, language mirror, OG image) |
| `docs check --all` | Validate all doc pages |
| `webcard <target>` | Generate animated OG GIFs — by card, group, or publication number |
| `weblinks` | Print all GitHub Pages URLs in block code |
| `weblinks --admin` | Same with conformity status indicators per link |
| `pub export <#> --pdf` | Export publication to PDF |
| `pub export <#> --docx` | Export publication to DOCX |
| `profile update` | Refresh all 8 profile files with current stats (versions, publications, issues, stories) |
| `<cmd> ?` | Contextual help for any pub/doc/webcard/weblinks/profile command |

### Project Management

| Command | What Claude Does |
|---------|-----------------|
| `project list` | List all projects with P# index, type, status, satellite count |
| `project info <P#>` | Show project details — identity, publications, satellites, evolution, stories |
| `project create <name>` | Full creation: register P# + GitHub Project board (elevated, linked to repo) + web presence |
| `project register <name>` | Register a new project with P# ID — creates `projects/<slug>.md` in core |
| `project review <P#>` | Review project state — documentation, publications, required assets, freshness |
| `project review --all` | Review all projects |
| `#N: <content>` | Scoped note — `#` call alias routes to project N |
| `#N:methodology:<topic>` | Methodology insight — flagged for doc harvesting |
| `#N:principle:<topic>` | Design principle — flagged for doc harvesting |
| `#N:info` | Show accumulated knowledge for #N |
| `#N:done` | End documentation focus, compile summary |
| `g:<board>:<item>` | Reference a GitHub board item by position |
| `g:<board>:<item>:done` | Mark board item as Done (compilation trigger) |
| `g:<board>:<item>:progress` | Move board item to In Progress |
| `g:<board>:<item>:info` | Detailed board item view |
| `<cmd> ?` | Contextual help for any project command |

### Live Session Analysis

| Command | What Claude Does |
|---------|-----------------|
| `I'm live` | Pull latest clips, extract last frame from newest clip, report UI state |
| `multi-live` | Monitor multiple streams simultaneously, report comparative state |
| `recipe` | Print the live capture quick recipe (OBS + stream_capture.py params) |
| `<cmd> ?` | Contextual help for any live session command |

### Visuals — Automated Documentation from Recordings

| Command | What Claude Does |
|---------|-----------------|
| `visual <path>` | Extract evidence frames from video (default: detection mode) |
| `visual <path> --timestamps 10 30 60` | Extract frames at specific seconds from video start |
| `visual <path> --times HH:MM:SS ...` | Extract frames at clock times (with optional `--video-start`) |
| `visual <path> --dates "YYYY-MM-DD HH:MM:SS" ...` | Extract frames at date-times (with optional `--video-start-datetime`) |
| `visual <path> --detect` | Scan video for significant frames automatically (scene change, text, edges) |
| `visual <path> --detect --subjects kw1 kw2` | Content-aware detection with keyword hints |
| `visual --repo owner/repo --file path/video.mp4` | Fetch and process video from GitHub repository |
| `visual <path> --report` | Generate markdown evidence report |
| `visual <path> --sheet` | Generate contact sheet (thumbnail grid) |
| `visual <path> --dedup` | Deduplicate near-identical frames (perceptual hashing) |
| `visual <path> --info` | Show video metadata only (no extraction) |
| `deep <description>` | Frame-by-frame deep analysis of a spotted anomaly |
| `analyze <path>` | Static video file analysis with state progression timeline |
| `<cmd> ?` | Contextual help for any visual command |

### Live Network

| Command | What Claude Does |
|---------|-----------------|
| `beacon` | Knowledge beacon status and peer discovery |
| `<cmd> ?` | Contextual help for any live network command |

---

