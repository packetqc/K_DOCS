#!/usr/bin/env python3
"""
Build configurations data for the main navigator.

Scans Knowledge/K_*/ for domain JSON config files and writes
docs/data/configurations.json. The navigator fetches this at runtime.

Included patterns:
  - architecture/architecture.json
  - constraints/constraints.json
  - conventions/conventions.json
  - conventions/depth_config.json
  - documentation/documentation.json
  - work/work.json
  - data/projects.json (K_PROJECTS only)

Usage:
    python3 Knowledge/K_DOCS/scripts/build_configurations.py
"""

import json
import sys
from pathlib import Path

RAW_BASE = "https://raw.githubusercontent.com/packetqc/knowledge/main"

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
KNOWLEDGE_DIR = REPO_ROOT / "Knowledge"
OUTPUT_FILE = REPO_ROOT / "docs" / "data" / "configurations.json"

# Config file patterns to include (relative to module root)
CONFIG_PATTERNS = [
    "architecture/architecture.json",
    "constraints/constraints.json",
    "conventions/conventions.json",
    "conventions/depth_config.json",
    "documentation/documentation.json",
    "work/work.json",
    "data/projects.json",
]

# Human-friendly names for config types
TYPE_NAMES = {
    "architecture.json": ("Architecture", "Architecture"),
    "constraints.json": ("Constraints", "Contraintes"),
    "conventions.json": ("Conventions", "Conventions"),
    "depth_config.json": ("Depth Config", "Config profondeur"),
    "documentation.json": ("Documentation", "Documentation"),
    "work.json": ("Work", "Travail"),
    "projects.json": ("Projects Data", "Données projets"),
}


def scan_configs():
    """Scan all K_* modules for configuration files."""
    items = []
    priority = 0

    # System-level config (Knowledge/modules.json)
    modules_json = KNOWLEDGE_DIR / "modules.json"
    if modules_json.exists():
        rel_path = str(modules_json.relative_to(REPO_ROOT)).replace("\\", "/")
        items.append({
            "title": "Module Registry",
            "title_fr": "Registre des modules",
            "file": "modules.json",
            "module": "System",
            "path": f"{RAW_BASE}/{rel_path}",
            "priority": priority,
        })
    priority = 1

    for mod_dir in sorted(KNOWLEDGE_DIR.glob("K_*")):
        mod_name = mod_dir.name
        for pattern in CONFIG_PATTERNS:
            cfg = mod_dir / pattern
            if not cfg.exists():
                continue
            rel_path = str(cfg.relative_to(REPO_ROOT)).replace("\\", "/")
            fname = cfg.name
            title_en, title_fr = TYPE_NAMES.get(fname, (fname, fname))
            items.append({
                "title": title_en,
                "title_fr": title_fr,
                "file": fname,
                "module": mod_name,
                "path": f"{RAW_BASE}/{rel_path}",
                "priority": priority,
            })
            priority += 1
    return items


def main():
    items = scan_configs()
    if not items:
        print("No configuration files found.", file=sys.stderr)
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
            items = [i for i in items if i["path"] not in removed_paths]
        except Exception:
            pass

    data = {
        "generated_by": "Knowledge/K_DOCS/scripts/build_configurations.py",
        "section": "configurations",
        "title": "Configurations",
        "title_fr": "Configurations",
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
