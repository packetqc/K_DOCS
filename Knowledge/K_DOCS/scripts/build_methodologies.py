#!/usr/bin/env python3
"""
Build methodology data for the main navigator.

Scans Knowledge/K_*/methodology/*.md and writes docs/data/methodologies.json.
The navigator fetches this JSON at runtime to build the Methodologies widget.

Run on demand or when methodology files change.
Re-running preserves manually edited priorities and FR titles.

Usage:
    python3 Knowledge/K_DOCS/scripts/build_methodologies.py
"""

import json
import re
import sys
from pathlib import Path

# Raw GitHub base for production serving (viewer fetches these directly)
RAW_BASE = "https://raw.githubusercontent.com/packetqc/knowledge/main"

# Repo root (script lives in Knowledge/K_DOCS/scripts/)
REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
KNOWLEDGE_DIR = REPO_ROOT / "Knowledge"
OUTPUT_FILE = REPO_ROOT / "docs" / "data" / "methodologies.json"


def read_title(md_path: Path) -> str:
    """Read the first # heading from a markdown file."""
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "---":
                    for line2 in f:
                        if line2.strip() == "---":
                            break
                    continue
                m = re.match(r"^#\s+(.+)$", line)
                if m:
                    return m.group(1).strip()
    except Exception:
        pass
    return md_path.stem.replace("-", " ").title()


def scan_modules():
    """Scan all K_* modules for methodology files."""
    items = []
    priority = 1
    for mod_dir in sorted(KNOWLEDGE_DIR.glob("K_*")):
        meth_dir = mod_dir / "methodology"
        if not meth_dir.is_dir():
            continue
        files = sorted(meth_dir.glob("*.md"))
        if not files:
            continue
        for f in files:
            rel_path = str(f.relative_to(REPO_ROOT)).replace("\\", "/")
            items.append({
                "title": read_title(f),
                "title_fr": "",
                "file": f.name,
                "module": mod_dir.name,
                "path": f"{RAW_BASE}/{rel_path}",
                "priority": priority,
            })
            priority += 1
    return items


def main():
    items = scan_modules()
    if not items:
        print("No methodology files found.", file=sys.stderr)
        sys.exit(1)

    # Merge with existing data (preserve manual edits + respect removed items)
    removed = []
    if OUTPUT_FILE.exists():
        try:
            existing = json.loads(OUTPUT_FILE.read_text(encoding="utf-8"))
            edit_map = {e["path"]: e for e in existing.get("items", [])}
            removed = existing.get("removed", [])
            removed_paths = {r["path"] for r in removed}
            for item in items:
                if item["path"] in edit_map:
                    prev = edit_map[item["path"]]
                    item["priority"] = prev.get("priority", item["priority"])
                    if prev.get("title_fr"):
                        item["title_fr"] = prev["title_fr"]
            # Filter out items that were manually moved to removed
            items = [i for i in items if i["path"] not in removed_paths]
        except Exception:
            pass

    data = {
        "generated_by": "Knowledge/K_DOCS/scripts/build_methodologies.py",
        "section": "methodologies",
        "title": "Methodologies",
        "title_fr": "Méthodologies",
        "open": False,
        "items": items,
        "removed": removed,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    modules = sorted(set(i["module"] for i in items))
    print(f"Written {OUTPUT_FILE.relative_to(REPO_ROOT)}: {len(items)} items across {len(modules)} modules.")


if __name__ == "__main__":
    main()
