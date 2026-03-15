#!/usr/bin/env python3
"""Sync satellite from core — lightweight updater for wakeup.

Downloads to any satellite, run at wakeup step 0.5 (or manually).
Clones packetqc/knowledge (shallow), compares critical files, copies diffs.

Usage:
    python3 knowledge/engine/scripts/sync_from_core.py          # from repo root
    python3 knowledge/engine/scripts/sync_from_core.py --check   # dry-run: report only
    python3 knowledge/engine/scripts/sync_from_core.py --self-update  # update THIS script first
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CORE_REPO = "https://github.com/packetqc/knowledge.git"
# Wakeup step 0 clones core here — reuse if available (avoids double clone)
WAKEUP_CLONE_PATH = Path("/tmp/knowledge")

# Critical files/dirs to sync from core to satellite
SYNC_TARGETS = [
    ".claude/skills",
    ".claude/routes.json",
    ".claude/knowledge_prerempli.json.example",
    "CLAUDE.md",
    "knowledge/engine",
    "knowledge/methodology",
    "knowledge/data/projects",
]


def run(cmd, check=False):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)


def find_root():
    """Find repo root from script location or cwd."""
    # Try from script location: scripts/ -> engine/ -> knowledge/ -> ROOT
    script_dir = Path(__file__).resolve().parent
    root_from_script = script_dir.parent.parent.parent
    if (root_from_script / ".git").is_dir():
        return root_from_script

    # Try from cwd
    cwd = Path.cwd()
    if (cwd / ".git").is_dir():
        return cwd

    print("ERROR: Not in a git repository.")
    sys.exit(1)


def clone_core(tmpdir):
    """Clone core repo (shallow). Returns path or None."""
    core_path = Path(tmpdir) / "knowledge"
    r = run(f"git clone --depth 1 {CORE_REPO} {core_path}")
    if r.returncode != 0:
        print(f"  ERROR: Could not clone core: {r.stderr.strip()}")
        return None
    return core_path


def sync(root, core_path, dry_run=False):
    """Compare and sync files. Returns (updated, skipped, identical) counts."""
    updated = 0
    added = 0
    identical = 0

    for rel in SYNC_TARGETS:
        src = core_path / rel
        dst = root / rel

        if not src.exists():
            continue

        if src.is_dir():
            for src_file in src.rglob("*"):
                if src_file.is_file():
                    rel_file = src_file.relative_to(core_path)
                    dst_file = root / rel_file

                    if not dst_file.exists():
                        if not dry_run:
                            dst_file.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copy2(str(src_file), str(dst_file))
                        print(f"  + {rel_file}")
                        added += 1
                    elif src_file.read_bytes() != dst_file.read_bytes():
                        if not dry_run:
                            shutil.copy2(str(src_file), str(dst_file))
                        print(f"  ~ {rel_file}")
                        updated += 1
                    else:
                        identical += 1
        else:
            if not dst.exists():
                if not dry_run:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(str(src), str(dst))
                print(f"  + {rel}")
                added += 1
            elif src.read_bytes() != dst.read_bytes():
                if not dry_run:
                    shutil.copy2(str(src), str(dst))
                print(f"  ~ {rel}")
                updated += 1
            else:
                identical += 1

    return updated, added, identical


def self_update(root, core_path):
    """Update this script from core."""
    src = core_path / "knowledge" / "engine" / "scripts" / "sync_from_core.py"
    dst = root / "knowledge" / "engine" / "scripts" / "sync_from_core.py"
    if src.exists():
        if not dst.exists() or src.read_bytes() != dst.read_bytes():
            shutil.copy2(str(src), str(dst))
            print("  Self-updated sync_from_core.py from core")
            return True
        print("  sync_from_core.py already up to date")
    return False


def main():
    parser = argparse.ArgumentParser(description="Sync satellite from core")
    parser.add_argument("--check", action="store_true", help="Dry-run: report only")
    parser.add_argument("--self-update", action="store_true", help="Update this script first")
    args = parser.parse_args()

    root = find_root()
    print(f"Satellite root: {root}")
    print(f"Syncing from: {CORE_REPO}")

    # Reuse wakeup step 0 clone if it exists (avoids double clone)
    reused = False
    tmpdir = None
    if WAKEUP_CLONE_PATH.is_dir() and (WAKEUP_CLONE_PATH / ".git").is_dir():
        core_path = WAKEUP_CLONE_PATH
        reused = True
        print(f"  Reusing existing clone: {WAKEUP_CLONE_PATH}")
    else:
        tmpdir = tempfile.mkdtemp(prefix="knowledge-sync-")
        core_path = clone_core(tmpdir)
        if core_path is None:
            sys.exit(1)

        if args.self_update:
            self_update(root, core_path)
            print()

        mode = "CHECK" if args.check else "SYNC"
        print(f"\n  [{mode}] Comparing {len(SYNC_TARGETS)} targets...")

        updated, added, identical = sync(root, core_path, dry_run=args.check)

        print(f"\n  Result: {added} added, {updated} updated, {identical} identical")

        if args.check:
            if added + updated > 0:
                print(f"  Run without --check to apply {added + updated} changes.")
            else:
                print("  Satellite is up to date with core.")
        else:
            if added + updated > 0:
                print(f"  {added + updated} files synced from core.")
            else:
                print("  Satellite is up to date with core.")
    finally:
        if tmpdir and not reused:
            shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    main()
