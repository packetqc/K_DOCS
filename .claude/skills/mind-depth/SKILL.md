---
name: mind-depth
description: "Show depth config table for all mindmap branches. Usage: /mind-depth (show table), /mind-depth <path> <level> (set and show)."
allowed-tools: Bash
---

## K_MIND — Depth Config

Arguments: $ARGUMENTS

!`python3 -c "
import subprocess, sys
args = '''$ARGUMENTS'''.strip()
if args:
    parts = args.rsplit(' ', 1)
    if len(parts) == 2 and parts[1].lstrip('-').isdigit():
        subprocess.run(['python3', 'scripts/set_depth.py', '--path', parts[0], '--depth', parts[1]])
        print()
subprocess.run(['python3', 'scripts/set_depth.py', '--list'])
"`

Output this table to the user. To change a branch depth: `/mind-depth <path> <level>` (0=omit, -1=reset to default).
