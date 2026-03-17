# Live Session Capture — Portable Tooling

Stream-to-git bridge for real-time visual analysis by Claude Code. Works with any project.

---

## What This Provides

| File | Purpose |
|------|---------|
| `stream_capture.py` | Capture engine — WSL/Linux, 3 source modes, rolling MP4 clips, git sync |
| `dynamic/` | Output queue — rolling clips land here, git-tracked |
| `static/` | Input folder — drop pre-recorded videos for post-session analysis |

---

## How It Gets Into a Project

When Claude reads `packetqc/knowledge` on `wakeup`, the `live/` folder is part of the knowledge assets. If the active project doesn't have `live/`, Claude syncs it:

```
knowledge/live/             →  <project>/live/
  stream_capture.py                stream_capture.py
  dynamic/.gitkeep                 dynamic/.gitkeep
  static/.gitkeep                  static/.gitkeep
  README.md                        README.md
```

No clips are synced — only tooling. Clips are generated locally at runtime.

---

## Prerequisites

### Software (one-time install)

- **OBS Studio** (Windows) with [OBS RTSP Server plugin](https://github.com/iamscottxu/obs-rtsp)
- **WSL2** (Ubuntu) or native Linux
- **Python 3.7+** with OpenCV (`pip install opencv-python`)
- **ffmpeg** (for frame extraction on Claude side)
- **Git** (WSL uses Windows `git.exe` for credentials — auto-detected)

### One-time setup

```bash
python3 live/stream_capture.py --setup
```

Installs ffmpeg, OpenCV, Pillow, and optional mss (WSLg screen capture).

---

## Startup Checklist

Two sides must be ready. Missing any step = clips don't reach Claude.

### Client-side (user's machine)

| # | Step | Verify |
|---|------|--------|
| 1 | **OBS Studio running** — scene set to capture target (board, terminal, UI) | OBS preview shows live content |
| 2 | **OBS Virtual Camera started** — Tools > Start Virtual Camera | "Stop Virtual Camera" button visible = active |
| 3 | **OBS RTSP Server started** — Tools > RTSP Server > Start (port 8554, path `/live`) | "Stop" button visible = streaming |
| 4 | **WSL terminal open** — `cd` to project repo root (`/mnt/d/knowledge` or equivalent) | `git status` works |
| 5 | **On main branch** — `git checkout main && git pull origin main` | Branch shows `main`, latest commits pulled |
| 6 | **Launch capture script** | See command below |

```bash
python3 live/stream_capture.py --dynamic --rtsp rtsp://localhost:8554/live --scale 0.75 --crf 22 --push-interval 5
```

**Verify capture is working:**
- `WSL2 detected — remapping to Windows host: rtsp://172.x.x.x:8554/live` (normal — WSL2 remaps localhost to Windows host IP)
- `Cleaned N residual clips from previous session` (startup cleanup)
- `clip #1 (XX KB) | queue: XX KB | pushes: 0` → clips being captured
- `[GIT] push #1` → clips reaching remote (may take 5-10 seconds for first push)

### Claude-side (reception)

| # | Step | Verify |
|---|------|--------|
| 1 | **Session active** on the project repo | Wakeup completed |
| 2 | **`live/` folder exists** in the repo | Synced from knowledge on wakeup |
| 3 | **`.gitignore` allows force-add** | Script uses `git add --force` to bypass `live/dynamic/*.mp4` ignore rule |
| 4 | **Remote main receives clip commits** | `git fetch origin main && git log origin/main --oneline -3` shows `live: clip update` |
| 5 | **Enter capture mode** | Type `I'm live` |

### Common failures

| Symptom | Cause | Fix |
|---------|-------|-----|
| `Cannot open RTSP` | Virtual Camera not started in OBS | Start Virtual Camera first, then RTSP Server |
| Clips captured but `pushes: 0` | Old script without `--force` fix | `git pull origin main` to get latest script |
| Push errors / non-fast-forward | Remote has commits script doesn't have (github-actions bot) | Script auto-pulls with `--rebase` before push (fixed in PR #491) |
| `TypeError: 'Event' object is not callable` on Ctrl+C | Old script with `_stop` naming conflict | `git pull origin main` to get `_stop_event` fix (PR #493) |
| Clips stall after first rotation | Old script without delete-before-encode | `git pull origin main` (PR #491) |
| Script says remapping to 172.x.x.x | Normal — WSL2 localhost ≠ Windows localhost | RTSP reaches Windows host via resolved IP |
| h264 `mmco: unref short failure` (red text) | FFmpeg decoder warnings from RTSP stream jitter | Harmless — does not affect clip quality |
| Files not removed on restart | Old script without startup cleanup | `git pull origin main` (PR #491) |

---

## Quick Start

### 1. Start OBS (Windows)

1. Open OBS Studio
2. Set your scene to capture the board / serial terminal
3. **Start Virtual Camera** (Tools > Start Virtual Camera) — **required for RTSP source**
4. **Start RTSP Server** (Tools > RTSP Server > Start) — port 8554, path `/live`

### 2. Launch Capture (WSL)

```bash
cd /path/to/your/project
git checkout main && git pull origin main
python3 live/stream_capture.py --dynamic --rtsp rtsp://localhost:8554/live --scale 0.75 --crf 22 --push-interval 5
```

### 3. Tell Claude

```
I'm live
```

Claude pulls the latest clip, extracts the last frame, and reports what it sees.

### 4. Stop

Press **Ctrl+C** in WSL. Clips persist for review; cleaned at next start.

---

## Capture Modes

| Mode | Flag | Use Case |
|------|------|----------|
| RTSP stream | `--rtsp URL` | OBS on Windows, IP camera |
| File watch | `--file PATH` | PowerShell screenshot loop via `/mnt/c/...` |
| Screen grab | `--screen` | WSLg X11 (captures WSL GUI windows only) |

---

## Recommended Presets

| Use Case | Settings | Est. bandwidth |
|----------|----------|----------------|
| **QA session (recommended)** | `--scale 0.75 --crf 22 --push-interval 5` | ~250 MB/hr |
| UART text (sharp) | `--scale 1.0 --crf 22 --clip-secs 3` | ~400 MB/hr |
| High quality debug | `--scale 1.0 --crf 18 --fps 30` | ~500 MB/hr |
| Save bandwidth | `--fps 10 --clip-secs 5 --crf 32` | ~80 MB/hr |

---

## Multi-Source Capture

Run separate instances for different feeds:

```bash
# Terminal 1: UI capture
python3 live/stream_capture.py --dynamic --rtsp rtsp://localhost:8554/live --scale 0.75 --crf 22

# Terminal 2: UART capture (second OBS scene)
python3 live/stream_capture.py --dynamic --rtsp rtsp://localhost:8554/uart --scale 1.0 --crf 22 --prefix uart
```

Produces:
```
live/dynamic/
  clip_0.mp4, clip_1.mp4, clip_2.mp4     # UI feed
  uart_0.mp4, uart_1.mp4, uart_2.mp4     # UART feed
```

Use `multi-live` in Claude to get a comparative report across all sources.

---

## Claude Commands (from knowledge)

| Command | What Claude Does |
|---------|-----------------|
| `I'm live` | Pull latest clip, extract last frame, report UI/UART state |
| `multi-live` | Monitor all clip families, report comparative state |
| `deep <desc>` | Frame-by-frame forensic analysis of anomaly |
| `analyze <path>` | Static video analysis with state timeline |
| `recipe` | Print capture quick recipe with presets |

---

## Troubleshooting

See **Common failures** table in the Startup Checklist section above for the full list.

---

## Clip Discard — Lifecycle Management

When Claude is NOT actively monitoring (discussion, planning, interaction), clips must be actively deleted to prevent accumulation.

| File | Purpose |
|------|---------|
| `clip_discard.py` | Clip lifecycle manager — discard/capture mode transitions, cleanup across local + git + remote |

### Usage

```bash
# Report clip state across all locations
python3 live/clip_discard.py --status

# Full cleanup (local + git + remote check)
python3 live/clip_discard.py --discard

# Local only — no git operations
python3 live/clip_discard.py --discard --local

# Wait for capture to stop before cleaning
python3 live/clip_discard.py --discard --wait --wait-timeout 120

# Also check a specific branch
python3 live/clip_discard.py --discard --branch main

# JSON output for programmatic use
python3 live/clip_discard.py --status --json
```

### Capture Detection

The discard script detects if the capture script is actively pushing clips by checking the age of the last clip-related commit. If the last commit on `live/dynamic/` is less than 60 seconds old, capture is considered active.

- `--status` shows `📡 Capture ACTIVE` or `⏸️ Capture idle`
- `--discard` warns about race conditions when capture is active
- `--discard --wait` polls until capture stops, then auto-cleans

### Mode Transitions

| User says | Mode | Action |
|-----------|------|--------|
| `I'm live` | → Capture | Pull clips, extract frames, analyze |
| `pause` | → Discard | Stop monitoring, run `clip_discard.py --discard` |
| `resume capture` | → Capture | Resume monitoring (same as `I'm live`) |

**Important**: Ctrl+C the capture script BEFORE entering discard mode. Discard can't clean `main` while capture pushes clips every ~5 seconds.

---

## SessionAgent — Ticket Sync

Autonomous watchdog for GitHub issue comment synchronization during live sessions.

| File | Purpose |
|------|---------|
| `scripts/session_agent.py` | Agent that posts session events as real-time comments on GitHub issues |

### Python initialization

```python
from scripts.session_agent import SessionAgent
agent = SessionAgent('packetqc/knowledge', issue_number=478)
agent.start()
```

### CLI usage

```bash
# Start the agent (burst mode: 10s ticks, 20s watchdog)
python3 scripts/session_agent.py start packetqc/knowledge 478

# Feed events to the agent
python3 scripts/session_agent.py feed user "User message" "description"
python3 scripts/session_agent.py feed step_start "Step Name" "what will be done"
python3 scripts/session_agent.py feed step_complete "Step Name" "results"
python3 scripts/session_agent.py feed bot "Bot note" "details"

# Agent control
python3 scripts/session_agent.py tick      # Manual heartbeat
python3 scripts/session_agent.py status    # Show agent state
python3 scripts/session_agent.py stop      # Graceful shutdown
```

**Feed types:** `user`, `step_start`, `step_complete`, `bot`, `compaction`

**Requires:** `GH_TOKEN` env var set with classic PAT (`repo` + `project` scopes)

---

## Design Notes

- **Self-discovering paths**: Script uses `__file__` to find `dynamic/` and `static/` relative to itself
- **No project-specific hardcoding**: Same script works in any repo
- **Git integration**: Auto-detects branch, uses `git.exe` in WSL2 for Windows credentials
- **WSL2 host remapping**: `fix_wsl_url()` remaps `localhost` to Windows host IP (from `/etc/resolv.conf`) because WSL2 localhost points to the VM, not Windows
- **Force-add past .gitignore**: `git add --force` overrides `live/dynamic/*.mp4` ignore rule for clip delivery
- **Pull-rebase before push**: Handles concurrent remote commits (e.g. github-actions board sync) that cause non-fast-forward errors
- **Squash on exit**: Rolls up clip commits into one (disable with `--no-squash`)
- **3-clip rolling queue**: `clip_0` > `clip_1` > `clip_2` > `clip_0`... (newest = highest number)
- **Startup cleanup**: Deletes residual clips + cleans git index on every restart
