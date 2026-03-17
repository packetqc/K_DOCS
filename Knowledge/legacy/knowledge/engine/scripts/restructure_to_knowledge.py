#!/usr/bin/env python3
"""
Restructure legacy knowledge repo into knowledge/ directory structure.

Dry-run mode: shows the migration plan without touching anything.
Execute mode: performs the restructuring.

Usage:
    python3 scripts/restructure_to_knowledge.py --dry-run
    python3 scripts/restructure_to_knowledge.py --execute
    python3 scripts/restructure_to_knowledge.py --execute --safe-boot
        (moves everything EXCEPT CLAUDE.md and .claude/ — those get dry-run report only)
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


# =============================================================================
# Classification rules
# =============================================================================

@dataclass
class MoveAction:
    source: str
    destination: str
    category: str
    reason: str


@dataclass
class ConflictAction:
    source: str
    destination: str
    category: str
    reason: str
    resolution: str  # "merge", "keep_both", "user_decision"


@dataclass
class DeleteAction:
    source: str
    category: str
    reason: str


@dataclass
class MigrationPlan:
    moves: list = field(default_factory=list)
    conflicts: list = field(default_factory=list)
    deletes: list = field(default_factory=list)
    keeps: list = field(default_factory=list)  # (path, reason) tuples
    warnings: list = field(default_factory=list)


# What goes into knowledge/engine/ (system machinery)
ENGINE_DIRS = {
    "scripts": "knowledge/engine/scripts",
    "knowledge_config": "knowledge/engine/knowledge_config",
    "live": "knowledge/engine/live",
}

ENGINE_FILES = {
    "hello_world.py": "knowledge/engine/hello_world.py",
}

# What goes into knowledge/methodology/
METHODOLOGY_DIRS = {
    "methodology": "knowledge/methodology",
    "lessons": "knowledge/methodology/lessons",
    "patterns": "knowledge/methodology/patterns",
}

# What goes into knowledge/data/ (user-generated content)
DATA_DIRS = {
    "notes": "knowledge/data/notes",
    "projects": "knowledge/data/projects",
    "minds": "knowledge/data/minds",
    "publications": "knowledge/data/publications",
    "evidence": "knowledge/data/evidence",
    "references": "knowledge/data/references",
}

# What goes into knowledge/web/ (presentation layer)
WEB_DIRS = {
    # "docs" stays at root — GitHub Pages only supports / or /docs as source
    "assets": "knowledge/web/assets",
    "profile": "knowledge/web/profile",
    "tmp-renders": "knowledge/web/tmp-renders",
}

# Directories that MUST stay at root (platform constraints)
ROOT_DIRS_KEEP = {
    "docs": "GitHub Pages source — must be /docs at root",
}

# Root files classification
ROOT_FILES_MOVE = {
    "CHANGELOG.md": ("knowledge/CHANGELOG.md", "engine", "Version history"),
    "VERSION.md": ("knowledge/VERSION.md", "engine", "Version tracking"),
    "PLAN.md": ("knowledge/PLAN.md", "engine", "Roadmap"),
    "LINKS.md": ("knowledge/web/LINKS.md", "web", "Link directory"),
    "NEWS.md": ("knowledge/web/NEWS.md", "web", "News/updates"),
    "STORIES.md": ("knowledge/data/STORIES.md", "data", "User stories"),
    "knowledge-evolution-archive.md": ("knowledge/methodology/knowledge-evolution-archive.md", "methodology", "Evolution history"),
    "migrate_to_knowledge.sh": ("knowledge/engine/legacy/migrate_to_knowledge.sh", "engine", "Legacy migration script"),
}

# Root files that stay at root
ROOT_FILES_KEEP = {
    "CLAUDE.md": "Boot file — stays at root (will be regenerated)",
    "README.md": "Repo entry point — stays at root",
    "LICENSE": "Legal — stays at root",
    ".gitignore": "Git config — stays at root",
    ".gitattributes": "Git config — stays at root",
}

# .claude/ restructuring
CLAUDE_DIR_KEEP = {
    "skills": "Skills stay in .claude/skills/ (Claude Code convention)",
    "settings.json": "Claude Code settings",
    "settings.local.json": "Local settings",
}

CLAUDE_DIR_MOVE = {
    "knowledge_resultats.json": ("knowledge/state/knowledge_resultats.json", "Runtime state"),
    "knowledge_prerempli.json.example": ("knowledge/engine/templates/knowledge_prerempli.json.example", "Template"),
    "display_output.md": ("knowledge/state/display_output.md", "Runtime output"),
    "projects.json": ("knowledge/data/projects.json", "Project registry"),
    "routes.json": ("knowledge/engine/routes.json", "Routing config"),
}

# Patterns for runtime state files (should go to knowledge/state/)
RUNTIME_PATTERNS = [
    "checkpoint_execution.json",
    "preuve_execution.json",
    "journal_actions.json",
]


def detect_legacy_indicators(root: Path) -> list:
    """Detect signs of legacy knowledge structure."""
    indicators = []

    claude_md = root / "CLAUDE.md"
    if claude_md.exists():
        content = claude_md.read_text()
        if "<!-- knowledge-version:" in content:
            indicators.append("Legacy version tag in CLAUDE.md")
        if "knowledge-validation" in content:
            indicators.append("Knowledge validation boot in CLAUDE.md")
        if len(content) > 500:
            indicators.append(f"Large CLAUDE.md ({len(content)} chars) — likely contains inline methodology")

    # Flat skill files (v1 pattern)
    skills_dir = root / ".claude" / "skills"
    if skills_dir.exists():
        for item in skills_dir.iterdir():
            if item.is_file() and item.suffix == ".md":
                indicators.append(f"Flat skill file: .claude/skills/{item.name} (v1 pattern)")

    # Scripts at root
    if (root / "scripts").is_dir():
        indicators.append("Scripts directory at root (should be in knowledge/engine/)")

    # Methodology at root
    if (root / "methodology").is_dir():
        indicators.append("Methodology directory at root (should be in knowledge/methodology/)")

    # Notes at root
    if (root / "notes").is_dir():
        note_count = len(list((root / "notes").glob("session-*.md")))
        runtime_count = len(list((root / "notes").glob("session-runtime-*.json")))
        indicators.append(f"Notes at root: {note_count} session files, {runtime_count} runtime files")

    # No knowledge/ directory
    if not (root / "knowledge").is_dir():
        indicators.append("No knowledge/ directory — full restructuring needed")

    return indicators


def build_plan(root: Path) -> MigrationPlan:
    """Build the migration plan by scanning the repo."""
    plan = MigrationPlan()

    # --- Engine directories ---
    for src, dst in ENGINE_DIRS.items():
        src_path = root / src
        if src_path.is_dir():
            plan.moves.append(MoveAction(src, dst, "engine", f"System machinery → {dst}"))

    # --- Engine files ---
    for src, dst in ENGINE_FILES.items():
        src_path = root / src
        if src_path.is_file():
            plan.moves.append(MoveAction(src, dst, "engine", f"System file → {dst}"))

    # --- Methodology directories ---
    for src, dst in METHODOLOGY_DIRS.items():
        src_path = root / src
        if src_path.is_dir():
            plan.moves.append(MoveAction(src, dst, "methodology", f"Knowledge methodology → {dst}"))

    # --- Data directories ---
    for src, dst in DATA_DIRS.items():
        src_path = root / src
        if src_path.is_dir():
            # Special handling for notes: separate session files from runtime files
            if src == "notes":
                plan.moves.append(MoveAction(src, dst, "data", f"User data → {dst} (session-runtime-*.json → knowledge/state/)"))
            else:
                plan.moves.append(MoveAction(src, dst, "data", f"User data → {dst}"))

    # --- Web directories ---
    for src, dst in WEB_DIRS.items():
        src_path = root / src
        if src_path.is_dir():
            plan.moves.append(MoveAction(src, dst, "web", f"Presentation layer → {dst}"))

    # --- Root files ---
    for src, (dst, cat, reason) in ROOT_FILES_MOVE.items():
        if (root / src).exists():
            plan.moves.append(MoveAction(src, dst, cat, reason))

    for src, reason in ROOT_FILES_KEEP.items():
        if (root / src).exists():
            plan.keeps.append((src, reason))

    # --- .claude/ restructuring ---
    claude_dir = root / ".claude"
    if claude_dir.is_dir():
        for item in claude_dir.iterdir():
            name = item.name
            if name in CLAUDE_DIR_MOVE:
                dst, reason = CLAUDE_DIR_MOVE[name]
                plan.moves.append(MoveAction(f".claude/{name}", dst, "state", reason))
            elif name in CLAUDE_DIR_KEEP or (item.is_dir() and name == "skills"):
                plan.keeps.append((f".claude/{name}", CLAUDE_DIR_KEEP.get(name, "Claude Code convention")))
            elif name in RUNTIME_PATTERNS:
                plan.moves.append(MoveAction(f".claude/{name}", f"knowledge/state/{name}", "state", "Runtime state"))
            elif name == "__pycache__":
                plan.deletes.append(DeleteAction(f".claude/{name}", "cache", "Python cache"))
            elif name.startswith("."):
                plan.keeps.append((f".claude/{name}", "Hidden file — keep"))
            else:
                plan.warnings.append(f"Unknown item in .claude/: {name} — needs manual classification")

    # --- Special: notes runtime files separation ---
    notes_dir = root / "notes"
    if notes_dir.is_dir():
        runtime_files = list(notes_dir.glob("session-runtime-*.json"))
        if runtime_files:
            plan.warnings.append(
                f"{len(runtime_files)} session-runtime-*.json files in notes/ → will move to knowledge/state/sessions/"
            )

    # --- Detect anything we missed ---
    known_items = set()
    for action in plan.moves:
        known_items.add(action.source.split("/")[0])
    for path, _ in plan.keeps:
        known_items.add(path.split("/")[0])
    for action in plan.deletes:
        known_items.add(action.source.split("/")[0])
    known_items.update({".git", ".claude", "knowledge"})

    for item in root.iterdir():
        name = item.name
        if name not in known_items:
            plan.warnings.append(f"Unclassified root item: {name} — needs manual decision")

    return plan


def print_plan(plan: MigrationPlan, root: Path):
    """Pretty-print the migration plan."""
    indicators = detect_legacy_indicators(root)

    print("=" * 70)
    print("  KNOWLEDGE RESTRUCTURING — DRY RUN")
    print("=" * 70)
    print()

    # Legacy detection
    if indicators:
        print("LEGACY INDICATORS DETECTED:")
        for ind in indicators:
            print(f"  ⚠  {ind}")
        print()

    # Target structure tree
    print("TARGET STRUCTURE:")
    print("  knowledge/")
    print("  ├── engine/          # System machinery (scripts, live, config)")
    print("  │   ├── scripts/")
    print("  │   ├── live/")
    print("  │   ├── knowledge_config/")
    print("  │   ├── legacy/      # Old migration scripts")
    print("  │   └── templates/   # Config templates")
    print("  ├── methodology/     # How-to knowledge")
    print("  │   ├── lessons/")
    print("  │   └── patterns/")
    print("  ├── data/            # User-generated content")
    print("  │   ├── notes/")
    print("  │   ├── projects/")
    print("  │   ├── minds/")
    print("  │   ├── publications/")
    print("  │   ├── evidence/")
    print("  │   └── references/")
    print("  ├── web/             # Presentation layer")
    print("  │   ├── docs/")
    print("  │   ├── assets/")
    print("  │   └── profile/")
    print("  └── state/           # Runtime state (gitignored)")
    print()

    # Moves by category
    categories = {}
    for action in plan.moves:
        categories.setdefault(action.category, []).append(action)

    print("MOVES:")
    for cat in ["engine", "methodology", "data", "web", "state"]:
        actions = categories.get(cat, [])
        if actions:
            print(f"\n  [{cat.upper()}]")
            for a in actions:
                print(f"    {a.source:<45} → {a.destination}")
                if a.reason != a.source:
                    print(f"    {'':45}   {a.reason}")

    # Keeps
    if plan.keeps:
        print(f"\n\nKEEPS (stay in place):")
        for path, reason in plan.keeps:
            print(f"    {path:<45}   {reason}")

    # Deletes
    if plan.deletes:
        print(f"\n\nDELETES:")
        for action in plan.deletes:
            print(f"    {action.source:<45}   {action.reason}")

    # Warnings
    if plan.warnings:
        print(f"\n\nWARNINGS (need attention):")
        for w in plan.warnings:
            print(f"  ⚠  {w}")

    # Stats
    print(f"\n\n{'=' * 70}")
    print(f"  SUMMARY: {len(plan.moves)} moves, {len(plan.keeps)} keeps, "
          f"{len(plan.deletes)} deletes, {len(plan.warnings)} warnings")
    print(f"{'=' * 70}")


def execute_plan(plan: MigrationPlan, root: Path, safe_boot: bool = False):
    """Execute the migration plan."""
    if safe_boot:
        print("Executing migration plan (SAFE-BOOT: CLAUDE.md and .claude/ untouched)...")
    else:
        print("Executing migration plan...")
    print()

    # Create target directories
    target_dirs = set()
    for action in plan.moves:
        target_dirs.add(str(Path(action.destination).parent))
    target_dirs.add("knowledge/state")
    target_dirs.add("knowledge/state/sessions")
    target_dirs.add("knowledge/engine/legacy")
    target_dirs.add("knowledge/engine/templates")

    for d in sorted(target_dirs):
        full = root / d
        if not full.exists():
            full.mkdir(parents=True)
            print(f"  Created: {d}/")

    # Execute moves
    for action in plan.moves:
        src = root / action.source
        dst = root / action.destination

        if not src.exists():
            print(f"  SKIP (missing): {action.source}")
            continue

        # Safe-boot: skip .claude/ items and CLAUDE.md
        if safe_boot and (action.source.startswith(".claude/") or action.source == "CLAUDE.md"):
            print(f"  DRY-RUN (safe-boot): {action.source} → {action.destination}")
            continue

        # Special handling for notes: separate runtime files
        if action.source == "notes":
            # Move runtime files to state/sessions/ first
            state_sessions = root / "knowledge" / "state" / "sessions"
            state_sessions.mkdir(parents=True, exist_ok=True)
            for runtime_file in src.glob("session-runtime-*.json"):
                shutil.move(str(runtime_file), str(state_sessions / runtime_file.name))
                print(f"  Moved runtime: notes/{runtime_file.name} → knowledge/state/sessions/")

            # Pending comments too
            for pending in src.glob("pending-*.json"):
                shutil.move(str(pending), str(state_sessions / pending.name))
                print(f"  Moved state: notes/{pending.name} → knowledge/state/sessions/")

        # Move the directory/file
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            if dst.is_dir():
                # Merge: move contents
                for item in src.iterdir():
                    target = dst / item.name
                    if not target.exists():
                        shutil.move(str(item), str(target))
                # Remove now-empty source
                try:
                    src.rmdir()
                except OSError:
                    shutil.rmtree(str(src))
            else:
                print(f"  CONFLICT: {action.destination} already exists — skipping")
                continue
        else:
            shutil.move(str(src), str(dst))

        print(f"  Moved: {action.source} → {action.destination}")

    # Execute deletes
    for action in plan.deletes:
        target = root / action.source
        if target.exists():
            if target.is_dir():
                shutil.rmtree(str(target))
            else:
                target.unlink()
            print(f"  Deleted: {action.source}")

    print()
    print("Migration complete. Review with: git status")
    print("Runtime state dir (knowledge/state/) should be added to .gitignore")


def main():
    parser = argparse.ArgumentParser(description="Restructure knowledge repo")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="Show plan without executing")
    group.add_argument("--execute", action="store_true", help="Execute the restructuring")
    parser.add_argument("--root", default=".", help="Repository root (default: current dir)")
    parser.add_argument("--safe-boot", action="store_true",
                        help="Execute moves but keep CLAUDE.md and .claude/ as dry-run only")

    args = parser.parse_args()
    root = Path(args.root).resolve()

    if not (root / ".git").is_dir():
        print("ERROR: Not a git repository")
        sys.exit(1)

    plan = build_plan(root)

    if args.dry_run:
        print_plan(plan, root)
    elif args.execute:
        print_plan(plan, root)
        print()
        print("Proceeding with execution...")
        print()
        execute_plan(plan, root, safe_boot=args.safe_boot)


if __name__ == "__main__":
    main()
