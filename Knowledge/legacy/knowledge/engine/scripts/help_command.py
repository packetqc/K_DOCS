#!/usr/bin/env python3
"""Multipart help — print knowledge commands + project-specific commands (concatenated).

Reads Part 1 from methodology/commands.md and outputs the command tables.
Part 2 is project-specific and would come from the active project's CLAUDE.md.

Output is written to .claude/display_output.md for markdown rendering
by Claude (display routes), and also printed to stdout for standalone use.
"""
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# scripts/ -> engine/ -> knowledge/ -> ROOT
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))
KNOWLEDGE_DIR = os.path.join(ROOT_DIR, "knowledge")
COMMANDS_PATH = os.path.join(KNOWLEDGE_DIR, "methodology", "commands.md")
DISPLAY_OUTPUT = os.path.join(ROOT_DIR, ".claude", "display_output.md")


def main():
    if not os.path.exists(COMMANDS_PATH):
        print(f"Erreur: fichier de commandes introuvable: {COMMANDS_PATH}", file=sys.stderr)
        sys.exit(1)

    with open(COMMANDS_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Collect command tables (Part 1) — stop before Full Details sections
    output_lines = []
    for line in lines:
        if line.startswith("## Live Session — Full Details"):
            break
        output_lines.append(line)

    content = "".join(output_lines)

    # Write to display file for markdown rendering
    os.makedirs(os.path.dirname(DISPLAY_OUTPUT), exist_ok=True)
    with open(DISPLAY_OUTPUT, "w", encoding="utf-8") as f:
        f.write(content)

    # Also print to stdout for standalone use
    print(content, end="")
    sys.exit(0)


if __name__ == "__main__":
    main()
