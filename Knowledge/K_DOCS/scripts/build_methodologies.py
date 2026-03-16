#!/usr/bin/env python3
"""
Build methodology section for the main navigator.

Scans Knowledge/K_*/methodology/*.md and generates:
1. JS methods:[] array for the navigator widget
2. Translation keys (EN/FR) for methodology titles

Run on demand or when methodology files change.
Output is pasted into docs/interfaces/main-navigator/index.md.

Usage:
    python3 Knowledge/K_DOCS/scripts/build_methodologies.py
"""

import os
import re
import sys
from pathlib import Path

# Raw GitHub base for production serving (viewer fetches these directly)
RAW_BASE = "https://raw.githubusercontent.com/packetqc/knowledge/main"

# Repo root (script lives in Knowledge/K_DOCS/scripts/)
REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
KNOWLEDGE_DIR = REPO_ROOT / "Knowledge"


def slugify(name: str) -> str:
    """Convert filename to a JS-safe translation key."""
    return name.replace("-", "_").replace(".md", "")


def read_title(md_path: Path) -> str:
    """Read the first # heading from a markdown file."""
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                # Skip front matter
                if line == "---":
                    in_front = True
                    for line2 in f:
                        if line2.strip() == "---":
                            break
                    continue
                m = re.match(r"^#\s+(.+)$", line)
                if m:
                    return m.group(1).strip()
    except Exception:
        pass
    # Fallback: humanize filename
    return md_path.stem.replace("-", " ").title()


def scan_modules():
    """Scan all K_* modules for methodology files."""
    modules = {}
    for mod_dir in sorted(KNOWLEDGE_DIR.glob("K_*")):
        meth_dir = mod_dir / "methodology"
        if not meth_dir.is_dir():
            continue
        mod_name = mod_dir.name  # e.g. K_DOCS
        files = sorted(meth_dir.glob("*.md"))
        if files:
            modules[mod_name] = []
            for f in files:
                rel_path = f.relative_to(REPO_ROOT)
                title_en = read_title(f)
                modules[mod_name].append({
                    "file": f.name,
                    "slug": slugify(f.name),
                    "title_en": title_en,
                    "raw_url": f"{RAW_BASE}/{rel_path}",
                    "rel_path": str(rel_path),
                })
    return modules


def generate_js(modules):
    """Generate the JS methods:[] array block."""
    lines = []
    lines.append("    { id:'methodologies', title: t.methodologies, open:false, methods:[")

    mod_keys = list(modules.keys())
    for i, mod_name in enumerate(mod_keys):
        items = modules[mod_name]
        key = "m_" + mod_name.lower()  # e.g. m_k_docs
        comma = "," if i < len(mod_keys) - 1 else ""
        lines.append(f"      {{ g: t.{key}, items:[")
        for j, item in enumerate(items):
            tkey = f"m_{item['slug']}"
            icomma = "," if j < len(items) - 1 else ""
            lines.append(f"        {{t: t.{tkey}, p:'{item['raw_url']}'}}{icomma}")
        lines.append(f"      ]}}{comma}")

    lines.append("    ]},")
    return "\n".join(lines)


def generate_translations(modules):
    """Generate translation key suggestions for EN and FR."""
    lines_en = []
    lines_fr = []

    # Module group keys
    for mod_name in modules:
        key = "m_" + mod_name.lower()
        lines_en.append(f"      {key}: '{mod_name}',")
        lines_fr.append(f"      {key}: '{mod_name}',")

    # Item keys
    for mod_name, items in modules.items():
        for item in items:
            tkey = f"m_{item['slug']}"
            lines_en.append(f"      {tkey}: '{item['title_en']}',")
            lines_fr.append(f"      {tkey}: '{item['title_en']}',  // TODO: translate")

    return "\n".join(lines_en), "\n".join(lines_fr)


def main():
    modules = scan_modules()
    if not modules:
        print("No methodology files found.", file=sys.stderr)
        sys.exit(1)

    print("=" * 60)
    print("METHODOLOGY WIDGET DATA (paste into navigator widget list)")
    print("=" * 60)
    print(generate_js(modules))

    en_keys, fr_keys = generate_translations(modules)
    print()
    print("=" * 60)
    print("TRANSLATION KEYS — EN")
    print("=" * 60)
    print(en_keys)
    print()
    print("=" * 60)
    print("TRANSLATION KEYS — FR")
    print("=" * 60)
    print(fr_keys)

    print()
    print(f"Scanned {sum(len(v) for v in modules.values())} files across {len(modules)} modules.")


if __name__ == "__main__":
    main()
