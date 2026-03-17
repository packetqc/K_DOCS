#!/usr/bin/env python3
"""
Knowledge Migration — Self-contained script.

Download to any satellite repo, chmod +x, run it.
1. Restructures legacy knowledge into knowledge/ directory
2. Clones core repo and syncs ALL missing files (skills, engine, methodology, etc.)
3. Remaps all path references
4. Verifies all critical files are present
5. Commits and pushes

Usage:
    curl -O <url>/knowledge_migrate.py
    chmod +x knowledge_migrate.py
    ./knowledge_migrate.py
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from dataclasses import dataclass, field


CORE_REPO = "https://github.com/packetqc/knowledge.git"

# Directories and files to sync from core to satellite (relative paths)
CORE_SYNC = [
    ".claude/skills",
    ".claude/routes.json",
    ".claude/knowledge_prerempli.json.example",
    ".claude/display_output.md",
    "CLAUDE.md",
    "knowledge/engine",
    "knowledge/methodology",
    "knowledge/data/projects",
    "knowledge/engine/knowledge_config/__init__.py",
    "knowledge/engine/scripts/session_agent/__init__.py",
]


# =============================================================================
# STEP 0: Sync from core — clone core and copy missing files
# =============================================================================

def step_sync_from_core(root):
    """Clone core repo and sync all missing/outdated files to satellite."""
    banner("STEP 2/5 — Sync from core")

    tmpdir = tempfile.mkdtemp(prefix="knowledge-core-")
    core_path = Path(tmpdir) / "knowledge"

    print(f"  Cloning core repo into {tmpdir}...")
    r = run(f"git clone --depth 1 {CORE_REPO} {core_path}", check=False)
    if r.returncode != 0:
        print(f"  ERROR: Could not clone core repo.")
        print(f"  {r.stderr.strip()}")
        print(f"  Continuing without sync — manual copy may be needed.")
        shutil.rmtree(tmpdir, ignore_errors=True)
        return False

    synced = 0
    for rel in CORE_SYNC:
        src = core_path / rel
        dst = root / rel

        if not src.exists():
            print(f"  SKIP (not in core): {rel}")
            continue

        if src.is_dir():
            if dst.exists():
                # Merge: copy files that don't exist or are different
                for src_file in src.rglob("*"):
                    if src_file.is_file():
                        rel_file = src_file.relative_to(src)
                        dst_file = dst / rel_file
                        if not dst_file.exists():
                            dst_file.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copy2(str(src_file), str(dst_file))
                            synced += 1
                            print(f"  + {rel}/{rel_file}")
                        else:
                            # Overwrite if content differs
                            if src_file.read_bytes() != dst_file.read_bytes():
                                shutil.copy2(str(src_file), str(dst_file))
                                synced += 1
                                print(f"  ~ {rel}/{rel_file}")
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(str(src), str(dst))
                n = sum(1 for _ in dst.rglob("*") if _.is_file())
                synced += n
                print(f"  + {rel}/ ({n} files)")
        else:
            # Single file
            dst.parent.mkdir(parents=True, exist_ok=True)
            if not dst.exists():
                shutil.copy2(str(src), str(dst))
                synced += 1
                print(f"  + {rel}")
            elif src.read_bytes() != dst.read_bytes():
                shutil.copy2(str(src), str(dst))
                synced += 1
                print(f"  ~ {rel}")

    # Cleanup
    shutil.rmtree(tmpdir, ignore_errors=True)

    print(f"\n  Total: {synced} files synced from core")
    return synced > 0


# =============================================================================
# STEP 1: Restructure — move files into knowledge/ tree
# =============================================================================

ENGINE_DIRS = {
    "scripts": "knowledge/engine/scripts",
    "knowledge_config": "knowledge/engine/knowledge_config",
    "live": "knowledge/engine/live",
}
ENGINE_FILES = {
    "hello_world.py": "knowledge/engine/hello_world.py",
}
METHODOLOGY_DIRS = {
    "methodology": "knowledge/methodology",
    "lessons": "knowledge/methodology/lessons",
    "patterns": "knowledge/methodology/patterns",
}
DATA_DIRS = {
    "notes": "knowledge/data/notes",
    "projects": "knowledge/data/projects",
    "minds": "knowledge/data/minds",
    "publications": "knowledge/data/publications",
    "evidence": "knowledge/data/evidence",
    "references": "knowledge/data/references",
}
WEB_DIRS = {
    # "docs" stays at root — GitHub Pages only supports / or /docs as source
    "assets": "knowledge/web/assets",
    "profile": "knowledge/web/profile",
    "tmp-renders": "knowledge/web/tmp-renders",
}
ROOT_FILES_MOVE = {
    "CHANGELOG.md": "knowledge/CHANGELOG.md",
    "VERSION.md": "knowledge/VERSION.md",
    "PLAN.md": "knowledge/PLAN.md",
    "LINKS.md": "knowledge/web/LINKS.md",
    "NEWS.md": "knowledge/web/NEWS.md",
    "STORIES.md": "knowledge/data/STORIES.md",
    "knowledge-evolution-archive.md": "knowledge/methodology/knowledge-evolution-archive.md",
    "migrate_to_knowledge.sh": "knowledge/engine/legacy/migrate_to_knowledge.sh",
}
CLAUDE_DIR_MOVE = {
    "knowledge_resultats.json": "knowledge/state/knowledge_resultats.json",
    "knowledge_prerempli.json.example": "knowledge/engine/templates/knowledge_prerempli.json.example",
    "display_output.md": "knowledge/state/display_output.md",
    "projects.json": "knowledge/data/projects.json",
    "routes.json": "knowledge/engine/routes.json",
}
CLAUDE_DIR_KEEP = {"skills", "settings.json", "settings.local.json"}
RUNTIME_STATE = {"checkpoint_execution.json", "preuve_execution.json", "journal_actions.json"}

# Files that always stay at root
ROOT_KEEP = {"CLAUDE.md", "README.md", "LICENSE", ".gitignore", ".gitattributes"}


# =============================================================================
# STEP 2: Remap — update path references in CLAUDE.md + .claude/ skills
# =============================================================================

REMAP_RULES = [
    ("scripts/session_agent", "knowledge/engine/scripts/session_agent"),
    ("scripts/", "knowledge/engine/scripts/"),
    ("knowledge_config/", "knowledge/engine/knowledge_config/"),
    ("live/dynamic/", "knowledge/engine/live/dynamic/"),
    ("live/static/", "knowledge/engine/live/static/"),
    ("live/stream_capture.py", "knowledge/engine/live/stream_capture.py"),
    ("live/knowledge_beacon.py", "knowledge/engine/live/knowledge_beacon.py"),
    ("live/knowledge_scanner.py", "knowledge/engine/live/knowledge_scanner.py"),
    ("methodology/", "knowledge/methodology/"),
    ("lessons/", "knowledge/methodology/lessons/"),
    ("patterns/", "knowledge/methodology/patterns/"),
    ("notes/session-runtime-", "knowledge/state/sessions/session-runtime-"),
    ("notes/pending-", "knowledge/state/sessions/pending-"),
    ("notes/checkpoint.json", "knowledge/state/checkpoint.json"),
    ("notes/", "knowledge/data/notes/"),
    ("projects/", "knowledge/data/projects/"),
    ("minds/", "knowledge/data/minds/"),
    ("publications/", "knowledge/data/publications/"),
    ("evidence/", "knowledge/data/evidence/"),
    ("references/", "knowledge/data/references/"),
    # docs/ stays at root — GitHub Pages only supports / or /docs as source
    ("assets/", "knowledge/web/assets/"),
    ("profile/README", "knowledge/web/profile/README"),
    ("profile/", "knowledge/web/profile/"),
]

IMPORT_REMAP = [
    ("from scripts.", "from knowledge.engine.scripts."),
    ("import scripts.", "import knowledge.engine.scripts."),
    ("from knowledge_config.", "from knowledge.engine.knowledge_config."),
]

EXCLUDE_PATTERNS = [
    "knowledge/engine/", "knowledge/methodology/", "knowledge/data/",
    "knowledge/web/", "knowledge/state/", ".claude/skills/", "~/.claude/",
]


# =============================================================================
# Implementation
# =============================================================================

def banner(text):
    w = 64
    print()
    print("=" * w)
    print(f"  {text}")
    print("=" * w)
    print()


def run(cmd, check=True):
    """Run shell command, return output."""
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and r.returncode != 0:
        print(f"  ERROR: {cmd}")
        print(f"  {r.stderr.strip()}")
    return r


def detect_legacy(root):
    """Detect legacy knowledge structure. Returns list of indicators."""
    indicators = []

    claude_md = root / "CLAUDE.md"
    if claude_md.exists():
        content = claude_md.read_text()
        if "<!-- knowledge-version:" in content:
            indicators.append("Legacy version tag in CLAUDE.md")
        if "knowledge-validation" in content:
            indicators.append("Knowledge-validation boot sequence in CLAUDE.md")
        if len(content) > 500:
            indicators.append(f"Large CLAUDE.md ({len(content)} chars)")

    if (root / "scripts").is_dir():
        indicators.append("scripts/ at root")
    if (root / "methodology").is_dir():
        indicators.append("methodology/ at root")
    if (root / "notes").is_dir():
        n = len(list((root / "notes").glob("session-*.md")))
        indicators.append(f"notes/ at root ({n} session files)")
    if not (root / "knowledge").is_dir():
        indicators.append("No knowledge/ directory")

    # Detect incomplete migration (knowledge/ exists but critical files missing)
    if (root / "knowledge").is_dir():
        missing = []
        for path, label in [
            (".claude/skills", "skills"),
            ("knowledge/engine/scripts/gh_helper.py", "gh_helper"),
            ("knowledge/methodology/methodology-knowledge.md", "methodology"),
        ]:
            if not (root / path).exists():
                missing.append(label)
        if missing:
            indicators.append(f"Incomplete migration (missing: {', '.join(missing)})")

    return indicators


def step_restructure(root):
    """Move files/dirs into knowledge/ tree."""
    banner("STEP 1/5 — Restructure legacy into knowledge/")

    if (root / "knowledge").is_dir():
        print("  knowledge/ already exists — skipping restructure")
        return False

    # Pre-create target dirs
    for d in ["knowledge/engine/legacy", "knowledge/engine/templates",
              "knowledge/state/sessions", "knowledge/data", "knowledge/web",
              "knowledge/methodology/lessons", "knowledge/methodology/patterns"]:
        (root / d).mkdir(parents=True, exist_ok=True)

    moved = 0

    # Move directories
    for mapping in [ENGINE_DIRS, METHODOLOGY_DIRS, DATA_DIRS, WEB_DIRS]:
        for src, dst in mapping.items():
            s, d = root / src, root / dst
            if s.is_dir():
                # Special: extract runtime JSONs from notes/ before moving
                if src == "notes":
                    state_dir = root / "knowledge" / "state" / "sessions"
                    for f in list(s.glob("session-runtime-*.json")) + list(s.glob("pending-*.json")):
                        shutil.move(str(f), str(state_dir / f.name))
                        moved += 1

                d.parent.mkdir(parents=True, exist_ok=True)
                if d.exists():
                    # Merge into existing
                    for item in list(s.iterdir()):
                        target = d / item.name
                        if not target.exists():
                            shutil.move(str(item), str(target))
                            moved += 1
                    shutil.rmtree(str(s), ignore_errors=True)
                else:
                    shutil.move(str(s), str(d))
                    moved += 1
                print(f"  {src}/ -> {dst}/")

    # Move engine files
    for src, dst in ENGINE_FILES.items():
        s = root / src
        if s.is_file():
            (root / dst).parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(s), str(root / dst))
            moved += 1
            print(f"  {src} -> {dst}")

    # Move root markdown files
    for src, dst in ROOT_FILES_MOVE.items():
        s = root / src
        if s.exists():
            (root / dst).parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(s), str(root / dst))
            moved += 1
            print(f"  {src} -> {dst}")

    # Move .claude/ items
    claude_dir = root / ".claude"
    if claude_dir.is_dir():
        for item in list(claude_dir.iterdir()):
            name = item.name
            if name in CLAUDE_DIR_MOVE:
                dst = root / CLAUDE_DIR_MOVE[name]
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(item), str(dst))
                moved += 1
                print(f"  .claude/{name} -> {CLAUDE_DIR_MOVE[name]}")
            elif name in RUNTIME_STATE:
                dst = root / "knowledge" / "state" / name
                shutil.move(str(item), str(dst))
                moved += 1
                print(f"  .claude/{name} -> knowledge/state/{name}")
            elif name == "__pycache__":
                shutil.rmtree(str(item))
                print(f"  .claude/{name} (deleted cache)")

    print(f"\n  Total: {moved} items moved")
    return True


def step_remap(root):
    """Remap old path references in CLAUDE.md and .claude/ skills."""
    banner("STEP 3/5 — Remap path references")

    files = []
    for name in ["CLAUDE.md", ".claude/routes.json"]:
        p = root / name
        if p.exists():
            files.append(p)
    for pattern in [".claude/skills/*/SKILL.md", ".claude/skills/*/*.md"]:
        files.extend(root.glob(pattern))
    files = sorted(set(files))

    total = 0
    for filepath in files:
        content = filepath.read_text()
        lines = content.splitlines(keepends=True)
        new_lines = []
        file_changes = 0

        for line in lines:
            new_line = line
            # Python imports
            for old, new in IMPORT_REMAP:
                if old in new_line and new not in new_line:
                    new_line = new_line.replace(old, new)
                    file_changes += 1
            # Path references
            for old, new in REMAP_RULES:
                if old in new_line and new not in new_line:
                    # Don't remap if already in a knowledge/ path
                    skip = False
                    for excl in EXCLUDE_PATTERNS:
                        idx = new_line.find(old)
                        if idx > 0 and excl in new_line[max(0, idx-30):idx+len(old)]:
                            skip = True
                            break
                    if not skip:
                        new_line = new_line.replace(old, new)
                        file_changes += 1
            new_lines.append(new_line)

        if file_changes > 0:
            filepath.write_text("".join(new_lines))
            rel = filepath.relative_to(root)
            print(f"  {rel}: {file_changes} remaps")
            total += file_changes

    print(f"\n  Total: {total} path references remapped across {len(files)} files")
    return total


def step_commit(root):
    """Git add, commit, push."""
    banner("STEP 4/5 — Commit & push")

    os.chdir(str(root))

    # Check for changes
    r = run("git status --porcelain")
    if not r.stdout.strip():
        print("  No changes to commit")
        return False

    changed = len(r.stdout.strip().splitlines())
    print(f"  {changed} files changed")

    # Get current branch
    r = run("git branch --show-current")
    branch = r.stdout.strip()
    print(f"  Branch: {branch}")

    # Commit
    run("git add -A")
    msg = "feat: knowledge v2.0 migration — sync core + restructure + remap paths"
    r = run(f'git commit -m "{msg}"')
    if r.returncode == 0:
        print(f"  Committed: {msg}")
    else:
        print(f"  Commit failed: {r.stderr.strip()}")
        return False

    # Push with retry
    for attempt in range(4):
        r = run(f"git push -u origin {branch}", check=False)
        if r.returncode == 0:
            print(f"  Pushed to origin/{branch}")
            return True
        wait = 2 ** (attempt + 1)
        print(f"  Push failed (attempt {attempt+1}/4), retrying in {wait}s...")
        import time
        time.sleep(wait)

    print("  Push failed after 4 attempts. Push manually.")
    return False


def step_report(root):
    """Final report."""
    banner("STEP 5/5 — Verify completeness")

    # Verify critical files exist
    checks = [
        (".claude/skills", "Skills directory"),
        (".claude/routes.json", "Routes config"),
        ("CLAUDE.md", "Boot file"),
        ("knowledge/engine/scripts/gh_helper.py", "GitHub helper"),
        ("knowledge/engine/scripts/executer_demande.py", "Command executor"),
        ("knowledge/methodology/methodology-knowledge.md", "Knowledge methodology"),
        ("knowledge/engine/knowledge_config/__init__.py", "Knowledge config parser"),
        ("knowledge/engine/scripts/session_agent/__init__.py", "Session agent module"),
    ]

    all_ok = True
    for path, label in checks:
        p = root / path
        exists = p.exists()
        status = "OK" if exists else "MISSING"
        if not exists:
            all_ok = False
        print(f"  [{status}] {label}: {path}")

    if not all_ok:
        print("\n  WARNING: Some critical files are missing!")
        print("  The satellite may not function correctly.")
    else:
        print("\n  All critical files present.")

    banner("Migration complete")

    print("  New structure:")
    print("  .")
    print("  ├── CLAUDE.md          # Boot file (paths updated)")
    print("  ├── README.md")
    print("  ├── LICENSE")
    print("  ├── .claude/")
    print("  │   └── skills/        # Claude Code skills (paths updated)")
    print("  └── knowledge/")
    print("      ├── engine/        # scripts, live, config")
    print("      ├── methodology/   # how-to docs, lessons, patterns")
    print("      ├── data/          # notes, projects, minds, publications")
    print("      ├── web/           # docs, assets, profile")
    print("      └── state/         # runtime JSONs (sessions)")
    print()
    print("  Next steps:")
    print("  1. Start a new Claude Code session on this repo")
    print("  2. The new session will boot with updated paths")
    print("  3. Delete this migration script: rm knowledge_migrate.py")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Knowledge Migration — restructure legacy repos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    ./knowledge_migrate.py              # Interactive (default)
    ./knowledge_migrate.py --dry-run    # Show plan without executing
    ./knowledge_migrate.py --yes        # Skip confirmation
        """)
    parser.add_argument("--dry-run", action="store_true", help="Show plan only")
    parser.add_argument("--yes", "-y", action="store_true", help="Skip confirmation")
    parser.add_argument("--root", default=".", help="Repo root (default: current dir)")

    args = parser.parse_args()
    root = Path(args.root).resolve()

    # Safety checks
    if not (root / ".git").is_dir():
        print("ERROR: Not a git repository. Run from your satellite repo root.")
        sys.exit(1)

    # Detect
    banner("KNOWLEDGE MIGRATION")
    indicators = detect_legacy(root)

    if not indicators:
        print("  No legacy indicators found. This repo may already be migrated.")
        print("  Run with --dry-run to inspect anyway.")
        if not args.yes:
            sys.exit(0)

    print("  Legacy indicators detected:")
    for ind in indicators:
        print(f"    * {ind}")
    print()

    if args.dry_run:
        print("  DRY-RUN mode — no changes will be made.")
        print("  The plan above shows what would happen.")
        print("  Run without --dry-run to execute.")
        sys.exit(0)

    if not args.yes:
        print("  This will restructure the repo into knowledge/ and update all paths.")
        print("  Changes will be committed and pushed.")
        resp = input("\n  Proceed? [y/N] ").strip().lower()
        if resp not in ("y", "yes"):
            print("  Aborted.")
            sys.exit(0)

    # Execute — order matters:
    # 1. Restructure legacy files into knowledge/ first
    # 2. THEN sync from core to fill gaps (won't conflict with knowledge/ check)
    # 3. Remap path references
    did_restructure = step_restructure(root)
    did_sync = step_sync_from_core(root)
    remapped = step_remap(root)

    if did_sync or did_restructure or remapped:
        step_commit(root)

    step_report(root)


if __name__ == "__main__":
    main()
