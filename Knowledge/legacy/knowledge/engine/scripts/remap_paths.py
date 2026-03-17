#!/usr/bin/env python3
"""
Remap old paths to new knowledge/ structure in CLAUDE.md and .claude/ files.

Usage:
    python3 knowledge/engine/scripts/remap_paths.py --dry-run
    python3 knowledge/engine/scripts/remap_paths.py --execute
"""

import argparse
import re
import sys
from pathlib import Path

# Path remapping rules (order matters — longer prefixes first)
REMAP_RULES = [
    # Engine
    ("scripts/session_agent", "knowledge/engine/scripts/session_agent"),
    ("scripts/", "knowledge/engine/scripts/"),
    ("knowledge_config/", "knowledge/engine/knowledge_config/"),
    ("live/dynamic/", "knowledge/engine/live/dynamic/"),
    ("live/static/", "knowledge/engine/live/static/"),
    ("live/stream_capture.py", "knowledge/engine/live/stream_capture.py"),
    ("live/knowledge_beacon.py", "knowledge/engine/live/knowledge_beacon.py"),
    ("live/knowledge_scanner.py", "knowledge/engine/live/knowledge_scanner.py"),
    # Methodology
    ("methodology/", "knowledge/methodology/"),
    ("lessons/", "knowledge/methodology/lessons/"),
    ("patterns/", "knowledge/methodology/patterns/"),
    # Data
    ("notes/session-runtime-", "knowledge/state/sessions/session-runtime-"),
    ("notes/pending-", "knowledge/state/sessions/pending-"),
    ("notes/checkpoint.json", "knowledge/state/checkpoint.json"),
    ("notes/", "knowledge/data/notes/"),
    ("projects/", "knowledge/data/projects/"),
    ("minds/", "knowledge/data/minds/"),
    ("publications/", "knowledge/data/publications/"),
    ("evidence/", "knowledge/data/evidence/"),
    ("references/", "knowledge/data/references/"),
    # Web (docs/ stays at root — GitHub Pages constraint)
    # ("docs/", ...) — NOT remapped, stays at root
    ("assets/", "knowledge/web/assets/"),
    ("profile/README", "knowledge/web/profile/README"),
    ("profile/", "knowledge/web/profile/"),
]

# Python import remapping (different syntax)
IMPORT_REMAP = [
    ("from scripts.", "from knowledge.engine.scripts."),
    ("import scripts.", "import knowledge.engine.scripts."),
    ("from knowledge_config.", "from knowledge.engine.knowledge_config."),
]

# Files to process
TARGET_FILES = [
    "CLAUDE.md",
    ".claude/routes.json",
]

# Glob patterns for skill files
SKILL_GLOBS = [
    ".claude/skills/*/SKILL.md",
    ".claude/skills/*/*.md",
]

# Paths that should NOT be remapped (already correct or special)
EXCLUDE_PATTERNS = [
    "knowledge/engine/",   # Already remapped
    "knowledge/methodology/",
    "knowledge/data/",
    "knowledge/web/",
    "knowledge/state/",
    ".claude/skills/",     # Skills location is correct
    "~/.claude/",          # User home, not repo
]


def should_remap(line: str, old: str, new: str) -> bool:
    """Check if this line should be remapped (not already done)."""
    if new in line:
        return False
    for excl in EXCLUDE_PATTERNS:
        # Check if the old path appears as part of an already-remapped path
        idx = line.find(old)
        if idx > 0 and excl in line[max(0, idx-30):idx+len(old)]:
            return False
    return old in line


def remap_line(line: str) -> tuple:
    """Remap a single line. Returns (new_line, list_of_changes)."""
    changes = []
    new_line = line

    # Python imports first (special syntax)
    for old, new in IMPORT_REMAP:
        if old in new_line and new not in new_line:
            new_line = new_line.replace(old, new)
            changes.append(f"  import: {old} → {new}")

    # Path remapping
    for old, new in REMAP_RULES:
        if should_remap(new_line, old, new):
            new_line = new_line.replace(old, new)
            changes.append(f"  path: {old} → {new}")

    return new_line, changes


def process_file(filepath: Path, dry_run: bool) -> list:
    """Process a single file. Returns list of changes."""
    if not filepath.exists():
        return []

    content = filepath.read_text()
    lines = content.splitlines(keepends=True)
    all_changes = []
    new_lines = []

    for i, line in enumerate(lines, 1):
        new_line, changes = remap_line(line)
        if changes:
            all_changes.append(f"  L{i}: {changes}")
        new_lines.append(new_line)

    if all_changes and not dry_run:
        filepath.write_text("".join(new_lines))

    return all_changes


def main():
    parser = argparse.ArgumentParser(description="Remap old paths to knowledge/ structure")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true")
    group.add_argument("--execute", action="store_true")
    parser.add_argument("--root", default=".", help="Repo root")

    args = parser.parse_args()
    root = Path(args.root).resolve()

    # Collect target files
    files = []
    for f in TARGET_FILES:
        p = root / f
        if p.exists():
            files.append(p)

    for pattern in SKILL_GLOBS:
        files.extend(root.glob(pattern))

    # Deduplicate
    files = sorted(set(files))

    mode = "DRY-RUN" if args.dry_run else "EXECUTE"
    print(f"{'=' * 60}")
    print(f"  PATH REMAPPING — {mode}")
    print(f"{'=' * 60}")
    print(f"\n  Files to process: {len(files)}\n")

    total_changes = 0
    for filepath in files:
        rel = filepath.relative_to(root)
        changes = process_file(filepath, args.dry_run)
        if changes:
            print(f"\n{rel}:")
            for c in changes:
                print(c)
            total_changes += len(changes)

    print(f"\n{'=' * 60}")
    print(f"  TOTAL: {total_changes} path remappings in {len(files)} files")
    if args.dry_run:
        print(f"  Run with --execute to apply changes")
    else:
        print(f"  Changes applied successfully")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
