#!/usr/bin/env python3
"""Contextual help — extract help for a specific command from commands.md.

Usage:
  python3 scripts/help_contextual.py "harvest --list"
  python3 scripts/help_contextual.py "pub check"
  python3 scripts/help_contextual.py "visual"

Searches methodology/commands.md for the command in table rows and section headers.
Returns: matching table row(s), parent section, and publication link if available.

Output is written to .claude/display_output.md for markdown rendering
by Claude (display routes), and also printed to stdout for standalone use.
"""
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# scripts/ -> engine/ -> knowledge/ -> ROOT
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))
KNOWLEDGE_DIR = os.path.join(ROOT_DIR, "knowledge")
COMMANDS_PATH = os.path.join(KNOWLEDGE_DIR, "methodology", "commands.md")
DISPLAY_OUTPUT = os.path.join(ROOT_DIR, ".claude", "display_output.md")

# Publication links per group (from issue #60 architecture)
PUB_LINKS = {
    "Session Management": "#8 — Session Management",
    "Harvest": "#7 — Harvest Protocol",
    "Content Management": "#5 — Documentation System",
    "Project Management": "#0 — Knowledge System",
    "Live Session Analysis": "#2 — Live Diagnostic",
    "Visuals": "#22 — Visual Documentation",
    "Live Network": "#10 — Live Network",
    "normalize": "#6 — Normalize",
    "webcard": "#5 — Documentation System",
}


def find_section_for_line(lines, target_idx):
    """Walk backwards from target_idx to find the nearest ### header."""
    for i in range(target_idx, -1, -1):
        if lines[i].startswith("### "):
            return lines[i].lstrip("# ").strip()
    return None


def find_h2_for_line(lines, target_idx):
    """Walk backwards from target_idx to find the nearest ## header."""
    for i in range(target_idx, -1, -1):
        if lines[i].startswith("## ") and not lines[i].startswith("### "):
            return lines[i].lstrip("# ").strip()
    return None


def get_pub_link(section_name):
    """Get publication link for a section."""
    if not section_name:
        return None
    for key, link in PUB_LINKS.items():
        if key.lower() in section_name.lower():
            return link
    return None


def search_command(query):
    """Search for a command in commands.md."""
    if not os.path.exists(COMMANDS_PATH):
        print(f"Error: {COMMANDS_PATH} not found", file=sys.stderr)
        return None

    with open(COMMANDS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    query_lower = query.lower().strip()

    # Build set of line indices that belong to command tables
    # (tables with "| Command |" header rows)
    command_table_lines = set()
    for i, line in enumerate(lines):
        if "| Command |" in line and "|" in line:
            # Found a command table header — mark all rows until next blank/header
            for j in range(i, len(lines)):
                if lines[j].strip() == "" or lines[j].startswith("#"):
                    break
                command_table_lines.add(j)

    # Strategy 1: exact match in command table rows only
    matches = []
    for i, line in enumerate(lines):
        if i not in command_table_lines:
            continue
        if "|" not in line or line.strip().startswith("|---"):
            continue
        # Extract command from table cell (between first pair of backticks)
        backtick_match = re.findall(r"`([^`]+)`", line)
        for cmd in backtick_match:
            if cmd.lower() == query_lower or query_lower in cmd.lower():
                section = find_section_for_line(lines, i)
                h2 = find_h2_for_line(lines, i)
                matches.append({
                    "line": line.strip(),
                    "line_num": i + 1,
                    "section": section,
                    "h2": h2,
                    "exact": cmd.lower() == query_lower,
                })

    # Strategy 2: search in section headers
    section_matches = []
    for i, line in enumerate(lines):
        if line.startswith("### ") and query_lower in line.lower():
            # Collect the section content until next ### or ##
            section_lines = [line]
            for j in range(i + 1, len(lines)):
                if lines[j].startswith("## "):
                    break
                section_lines.append(lines[j])
            section_matches.append({
                "header": line.lstrip("# ").strip(),
                "content": "\n".join(section_lines),
                "line_num": i + 1,
            })

    return {"table_matches": matches, "section_matches": section_matches}


def format_output(query, results):
    """Format the contextual help output as markdown."""
    if not results:
        return f"No help found for `{query}`."

    table_matches = results["table_matches"]
    section_matches = results["section_matches"]

    if not table_matches and not section_matches:
        return f"No help found for `{query}`. Try `help` for the full command list."

    out = []
    out.append(f"## `{query}` — Contextual Help\n")

    # Show exact table matches first
    exact = [m for m in table_matches if m["exact"]]
    partial = [m for m in table_matches if not m["exact"]]

    if exact:
        # Show the table header + matching rows
        out.append("| Command | What Claude Does |")
        out.append("|---------|-----------------|")
        for m in exact:
            out.append(m["line"])
        out.append("")

        # Show section context
        section = exact[0].get("section", "")
        if section:
            out.append(f"**Group**: {section}")
            pub = get_pub_link(section)
            if pub:
                out.append(f"**Publication**: {pub}")
        out.append("")

    if partial and not exact:
        out.append("### Related commands\n")
        out.append("| Command | What Claude Does |")
        out.append("|---------|-----------------|")
        seen = set()
        for m in partial:
            if m["line"] not in seen:
                out.append(m["line"])
                seen.add(m["line"])
        out.append("")

    # Show section details if they exist
    if section_matches:
        for sm in section_matches:
            out.append(f"\n### {sm['header']}\n")
            # Skip the header line itself
            content_lines = sm["content"].split("\n")[1:]
            out.append("\n".join(content_lines).strip())
            out.append("")

    # If we have partial matches but no exact, show them
    if partial and exact:
        out.append("\n### See also\n")
        seen = set()
        for m in partial:
            if m["line"] not in seen and m["line"] not in [e["line"] for e in exact]:
                backticks = re.findall(r"`([^`]+)`", m["line"])
                if backticks:
                    out.append(f"- `{backticks[0]}`")
                seen.add(m["line"])

    return "\n".join(out)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/help_contextual.py <command>", file=sys.stderr)
        print('Example: python3 scripts/help_contextual.py "harvest --list"', file=sys.stderr)
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    results = search_command(query)
    output = format_output(query, results)

    # Write to display file for markdown rendering
    os.makedirs(os.path.dirname(DISPLAY_OUTPUT), exist_ok=True)
    with open(DISPLAY_OUTPUT, "w", encoding="utf-8") as f:
        f.write(output)

    # Also print to stdout for standalone use
    print(output)


if __name__ == "__main__":
    main()
