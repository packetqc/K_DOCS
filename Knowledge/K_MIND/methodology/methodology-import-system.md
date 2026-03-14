# Methodology — K_MIND Import System

## Purpose
Procedure to import K_MIND as a core module into a host project, enabling memory system capabilities in any repository. K_MIND serves as the core Knowledge module — other modules (like K_DOCS) are built on top of it.

## Prerequisites
- Host project with git initialized (can be an empty/vanilla repo)
- Python 3 available
- GitHub access (for clone)
- Use WSL terminal / Claude Code CLI for initialization (not Claude Desktop App)

## Import Procedure

### 1. Create host project (if new)
```bash
mkdir /path/to/project && cd /path/to/project
git init
```

### 2. Import K_MIND
**Option A — Submodule (recommended):** Keeps the link to K_MIND repo for easy updates.
```bash
mkdir -p Knowledge
git submodule add https://github.com/packetqc/K_MIND.git Knowledge/K_MIND
```

**Option B — Clone:** Works but triggers embedded repository warning on `git add`.
```bash
mkdir -p Knowledge
git clone https://github.com/packetqc/K_MIND.git Knowledge/K_MIND
```
> If using clone inside a git repo, `git add .` will warn about embedded repository. Fix with:
> ```bash
> git rm --cached Knowledge/K_MIND
> git submodule add https://github.com/packetqc/K_MIND.git Knowledge/K_MIND
> ```

### 3. Run the install script
```bash
bash Knowledge/K_MIND/scripts/install.sh
```

This script:
- Detects standalone vs imported mode (exits if standalone)
- Creates `.claude/hooks/session-start.sh` — auto-detects `Knowledge/K_MIND/` path
- Creates `.claude/settings.json` with SessionStart hook config
- Copies skills (`mind-context`, `mind-depth`, `mind-stats`, `github`)
- Generates `CLAUDE.md` with:
  - Reference to `Knowledge/K_MIND/CLAUDE.md` as base instructions
  - Lifecycle directive: instructs Claude to auto-invoke `/mind-context` on session start
- Syncs `.claude/memory/` files to Claude Code system directory

### 4. Initial commit
```bash
git add .
git commit -m "init: project with K_MIND memory system"
```

### 5. Launch Claude Code
```bash
claude
```
The `session-start.sh` hook fires, detects `Knowledge/K_MIND/scripts`, initializes the session. The lifecycle directive in CLAUDE.md instructs Claude to invoke `/mind-context` and display the mindmap.

## Modes

### Standalone Mode
K_MIND is at the project root (it IS the project). `install.sh` detects `K_MIND_REL="."` and exits — no install needed. The hook reads `K_MIND_ROOT="."`.

### Imported Mode
K_MIND lives under `Knowledge/K_MIND/`. The hook detects `Knowledge/K_MIND/scripts` and sets `K_MIND_ROOT="Knowledge/K_MIND"`. All scripts use this variable to locate K_MIND files.

## Generated CLAUDE.md
For a vanilla (empty) host project, `install.sh` creates a CLAUDE.md with:
```markdown
# K_MIND Integration
Read and apply Knowledge/K_MIND/CLAUDE.md as base instructions for the K_MIND memory system.

## Lifecycle — On Session Start
When the SessionStart hook outputs "MANDATORY: You MUST now invoke /mind-context",
you MUST immediately invoke /mind-context and output the mindmap visually.
This applies on every new session, resume, and compaction recovery.
```
The lifecycle section is critical — without it, Claude receives the hook message but does not know to act on it (the full instructions are in K_MIND's CLAUDE.md which is loaded as a reference, but the lifecycle trigger must be explicit in the host CLAUDE.md).

## Updating K_MIND in a Host Project
When K_MIND evolves on its remote (new scripts, skills, fixes):
```bash
cd Knowledge/K_MIND
git pull origin main
cd ../..
bash Knowledge/K_MIND/scripts/install.sh   # re-copies skills/hooks if updated
git add . && git commit -m "chore: update K_MIND to latest"
```
New skills added to K_MIND are propagated by re-running `install.sh` which copies all skills from K_MIND's `.claude/skills/` to the host's `.claude/skills/`.

## Known Issues and Lessons Learned

### Clone-in-clone warning
Using `git clone` inside an existing git repo creates an embedded repository. Git warns and outer repo clones won't include the inner repo. Solution: use `git submodule add` instead.

### Lifecycle auto-start
The host CLAUDE.md must contain an explicit lifecycle section. A simple reference to K_MIND's CLAUDE.md is not sufficient — Claude needs the trigger directive in the host's own CLAUDE.md to react to the SessionStart hook output.

### GH_TOKEN for gh_helper.py
`gh_helper.py` reads `GH_TOKEN` from environment. In VS Code, set it via `claudeCode.environmentVariables` in VS Code settings (`settings.json`), using the key name `CLAUDE_CODE_OAUTH_TOKEN` or directly as `GH_TOKEN`. The token is never passed as argument or exposed in session output.

## Key Files
| File | Role |
|------|------|
| `scripts/install.sh` | Bootstrap host project with K_MIND capabilities |
| `scripts/install_memory.sh` | Sync .claude/memory files to Claude Code system |
| `scripts/gh_helper.py` | Portable GitHub API (PR, issues, projects) without gh CLI |
| `.claude/hooks/session-start.sh` | Auto-detect K_MIND location, init session |
| `.claude/skills/github/SKILL.md` | GitHubHelper usage conventions |
| `CLAUDE.md` (generated) | Reference to K_MIND instructions + lifecycle directive |

## Architecture Context
K_MIND is the **core** Knowledge module. Host projects import it under `Knowledge/K_MIND/` to gain:
- Memory system (far_memory, near_memory, mind_memory mindmap)
- Session management (init, resume, compaction recovery)
- Skills (/mind-context, /mind-depth, /mind-stats, /github)
- GitHub automation (gh_helper.py — PR create/merge, issues, projects)
- Real-time memory maintenance (every-turn append via scripts)

Other Knowledge modules (e.g., K_DOCS for documentation) are built as independent repos that import K_MIND as their foundation.
