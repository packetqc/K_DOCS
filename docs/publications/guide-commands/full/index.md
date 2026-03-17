---
layout: publication
title: "Commands — Full Reference"
description: "Complete command reference for the Knowledge platform — all commands, syntax, examples, and implementation details."
pub_id: "User Guide — Commands"
version: "v1"
date: "2026-03-17"
permalink: /publications/guide-commands/full/
keywords: "commands, reference, session, harvest, publications, projects, live, visual, network, normalize"
---

# Commands — Full Reference
{: #pub-title}

> **Module**: K_TOOLS — Command Framework & Utilities

**Contents**

| | |
|---|---|
| [Usage Patterns](#usage-patterns) | Three ways to invoke commands |
| [Session Management](#session-management) | Session lifecycle commands |
| [Normalize](#normalize) | Structure concordance |
| [Harvest](#harvest) | Distributed knowledge |
| [Publications](#publications) | Content management |
| [Project Management](#project-management) | Project tracking |
| [Live Session](#live-session) | Live analysis |
| [Visuals](#visuals) | Video documentation |
| [Live Network](#live-network) | Network beacon |
| [Multipart Help](#multipart-help) | How help is assembled |
| [Command Registry](#command-registry) | Internal routing |

---

## Usage Patterns

The Knowledge system accepts requests through **three entry patterns**. Every command works with all three.

### 1. Direct Command

Type a command as your session entry prompt. The system detects the command, executes it, and reports the result.

```
project create mon projet
harvest --healthcheck
pub check --all
```

**Best for**: Known commands with clear syntax. Fast, one-shot execution.

### 2. Natural Language

Describe what you want in plain language. The system interprets your intent and maps it to the appropriate command.

```
peux-tu me créer un projet ayant comme titre "go for it"
vérifie la fraîcheur de toutes mes publications
j'aimerais voir l'état du réseau de satellites
```

**Best for**: When you know what you want but not the exact syntax.

### 3. Interactive Session

Enter interactive mode with a command or request. The system displays `help` automatically, executes your initial request, then stays in free-form mode for follow-up work.

```
interactif
project create mon nouveau projet
```

**Best for**: Multi-step work sessions, exploratory tasks, chaining several operations. Type `terminé` or `done` to end.

### Pattern Comparison

| Pattern | Entry | Execution | Session | Follow-up |
|---------|-------|-----------|---------|-----------|
| **Direct** | Command syntax | Immediate | Single command | New prompt needed |
| **Natural language** | Plain text | Interpreted → executed | Single request | New prompt needed |
| **Interactive** | `interactif` + description | Help displayed → request executed | Persistent free-form | Type next command or `terminé` |

---

## Session Management

| Command | What It Does |
|---------|-------------|
| `wakeup` | **Auto-runs on session start** — never type as entry prompt. Mid-session: deep re-sync after PRs merged |
| `refresh` | Lightweight mid-session context restore — re-read CLAUDE.md, git status, reprint help |
| `help` / `aide` / `?` | **Multipart help** — print knowledge commands + project-specific commands (concatenated) |
| `status` | Read `notes/` and summarize current state |
| `save` | Pre-save summary → save context, commit, push, create PR to default branch |
| `remember ...` | Append text to current session notes |
| `elevate` | Elevate session to full autonomous — detects `GH_TOKEN` env var or `/tmp/.gh_token` temp file |
| `resume` | Resume interrupted session from checkpoint (crash recovery) |
| `recover` | Search `claude/*` branches for stranded work, cherry-pick/apply to current branch |
| `recall` | Deep memory search across all knowledge channels — near memory first, deeper with confirmation |
| `checkpoint` | Show current checkpoint state (or "no active checkpoint" if none) |
| `<cmd> ?` | Contextual help for any command — usage, examples, publication link |

---

## Normalize

| Command | What It Does |
|---------|-------------|
| `normalize` | Audit and fix knowledge structure concordance |
| `normalize --fix` | Apply concordance fixes automatically |
| `normalize --check` | Report only, no changes |

---

## Harvest

Distributed knowledge management — pull, review, stage, and promote insights from satellite projects.

| Command | What It Does |
|---------|-------------|
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

---

## Publications

Content management — create, validate, sync, review, export, and generate webcards.

| Command | What It Does |
|---------|-------------|
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
| `profile update` | Refresh all 8 profile files with current stats |
| `<cmd> ?` | Contextual help for any pub/doc/webcard/weblinks/profile command |

---

## Project Management

| Command | What It Does |
|---------|-------------|
| `project list` | List all projects with P# index, type, status, satellite count |
| `project info <P#>` | Show project details — identity, publications, satellites, evolution, stories |
| `project create <name>` | Full creation: register P# + GitHub Project board + web presence |
| `project register <name>` | Register a new project with P# ID — creates `projects/<slug>.md` |
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

---

## Live Session

Real-time stream monitoring and analysis.

| Command | What It Does |
|---------|-------------|
| `I'm live` | Pull latest clips, extract last frame from newest clip, report UI state |
| `multi-live` | Monitor multiple streams simultaneously, report comparative state |
| `recipe` | Print the live capture quick recipe (OBS + stream_capture.py params) |
| `<cmd> ?` | Contextual help for any live session command |

### `I'm live` Flow
1. `git pull origin <branch> --rebase`
2. Extract last frame from newest clip (highest number = newest)
3. Report: active tab, entry range, page number, log count, button states, anomalies
4. On follow-up, pull and extract again

### `recipe` Output
```
Live Capture — Quick Recipe

1. Windows: Start OBS → Tools → RTSP Server → Start (port 8554, path /live)
2. WSL:
   cd /path/to/project
   python3 live/stream_capture.py --dynamic --rtsp rtsp://localhost:8554/live --scale 0.75 --crf 22 --push-interval 5
3. Claude: "I'm live" — starts monitoring clips
4. Stop: Ctrl+C in WSL (clips persist for montage, cleaned at next start)

Presets:
  QA session (recommended):  --scale 0.75 --crf 22 --push-interval 5
  UART text (sharp):         --scale 1.0  --crf 22 --clip-secs 3
  High quality debug:        --scale 1.0  --crf 18 --fps 30
  Save bandwidth:            --fps 10     --clip-secs 5 --crf 32
```

---

## Visuals

Automated documentation from video recordings using OpenCV + Pillow + NumPy.

| Command | What It Does |
|---------|-------------|
| `visual <path>` | Extract evidence frames from video (default: detection mode) |
| `visual <path> --timestamps 10 30 60` | Extract frames at specific seconds |
| `visual <path> --times HH:MM:SS ...` | Extract frames at clock times |
| `visual <path> --dates "YYYY-MM-DD HH:MM:SS" ...` | Extract frames at date-times |
| `visual <path> --detect` | Scan video for significant frames automatically |
| `visual <path> --detect --subjects kw1 kw2` | Content-aware detection with keyword hints |
| `visual --repo owner/repo --file path/video.mp4` | Fetch and process video from GitHub |
| `visual <path> --report` | Generate markdown evidence report |
| `visual <path> --sheet` | Generate contact sheet (thumbnail grid) |
| `visual <path> --dedup` | Deduplicate near-identical frames |
| `visual <path> --info` | Show video metadata only (no extraction) |
| `deep <description>` | Frame-by-frame deep analysis of a spotted anomaly |
| `analyze <path>` | Static video file analysis with state progression timeline |
| `<cmd> ?` | Contextual help for any visual command |

### Detection Heuristics

| Detector | What It Finds | Method |
|----------|--------------|--------|
| Scene change | Visual transitions | Histogram correlation |
| Text density | Text-heavy frames | Adaptive threshold + morphology |
| Edge density | Diagrams, tables, code | Canny edge detection |
| Structured content | Grids, forms | Horizontal + vertical line detection |

### Full Pipeline
```
visual recording.mp4 --detect --dedup --report --sheet --title "Sprint Demo Evidence"
```

---

## Live Network

| Command | What It Does |
|---------|-------------|
| `beacon` | Knowledge beacon status and peer discovery |
| `<cmd> ?` | Contextual help for any live network command |

---

## Multipart Help

The `help` command assembles output from two sources:

```
┌───────────────────────────────────┐
│  Part 1: Knowledge Commands       │  ← from K_TOOLS (this module)
│  (session + live analysis)        │     Always present in every project
├───────────────────────────────────┤
│  Part 2: Project Commands         │  ← from <project>/CLAUDE.md
│  (project-specific)               │     Varies per project
└───────────────────────────────────┘
```

**Rule**: Any project that reads the Knowledge system inherits Part 1 automatically. Part 2 is defined by each project independently. Commands are never duplicated — they are concatenated.

---

## Command Registry

Every command is backed by a skill and registered in the command registry. When matching user input, the registry uses **longest-match-first** sorting — `harvest --healthcheck` matches before `harvest`, `normalize --fix` matches before `normalize`.

| Group | Skill Files | Methodology |
|-------|------------|-------------|
| **Session** | wakeup.md, resume.md, recall.md | session-protocol.md, checkpoint-resume.md |
| **Harvest** | harvest.md, healthcheck.md | production-development-minds.md |
| **Publications** | pub.md, pub-export.md, webcard.md, profile-update.md | documentation-generation.md, web-pagination-export.md |
| **Project** | project-create.md, project-manage.md | project-management.md, project-create.md |
| **Normalize** | normalize.md | Publication #6 |
| **Live** | live-session.md | interactive-diagnostic.md |
| **Visual** | visual.md | visual-documentation.md |

---

*This guide evolves as legacy commands are imported into the K_TOOLS module.*

*See also: [Main Navigator Guide]({{ '/publications/guide-main-navigator/' | relative_url }}) — [Knowledge 2.0]({{ '/publications/knowledge-2-0/' | relative_url }})*
