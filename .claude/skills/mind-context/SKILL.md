---
name: mind-context
description: "Load K_MIND context. Usage: /mind-context (normal), /mind-context full (all nodes), /mind-context <path> <depth> (set branch depth and render)."
allowed-tools: Read, Grep, Glob, Bash
---

## K_MIND — Active Context

Arguments: $ARGUMENTS

### Mind Map
!`python3 -c "
import subprocess, sys
args = '''$ARGUMENTS'''.strip()
if args == 'full':
    subprocess.run(['python3', 'scripts/mindmap_filter.py', '--full'])
elif args and args != 'full':
    parts = args.rsplit(' ', 1)
    if len(parts) == 2 and parts[1].lstrip('-').isdigit():
        path, depth = parts[0], parts[1]
        subprocess.run(['python3', 'scripts/set_depth.py', '--path', path, '--depth', depth])
        subprocess.run(['python3', 'scripts/mindmap_filter.py'])
    else:
        subprocess.run(['python3', 'scripts/mindmap_filter.py', '--path', args, '--depth', '99'])
else:
    subprocess.run(['python3', 'scripts/mindmap_filter.py'])
"`

### Depth Config
!`python3 scripts/set_depth.py --list`

### Display Conventions (from conventions.json)
!`python3 -c "
import json
with open('conventions/conventions.json') as f:
    data = json.load(f)
for ref in data['references']:
    if ref['name'].startswith('mindmap_'):
        print(f\"**{ref['name']}**: {ref['description']}\")
        print()
"`

### Active Conversation (Near Memory — Categorized by Group)
!`python3 -c "
import json
with open('sessions/near_memory.json') as f:
    data = json.load(f)
# Determine source: current session or last session (for fresh starts)
last = data.get('last_session')
has_last = last and last.get('summaries')
# Use current session summaries, or fall back to last session's summaries for fresh starts
source_summaries = data['summaries'] if data['summaries'] else (last['summaries'] if has_last else [])
categories = {'conversation': [], 'conventions': [], 'work': [], 'documentation': []}
for s in source_summaries[-10:]:
    refs = s.get('mind_memory_refs', [])
    placed = False
    for ref in refs:
        for cat in ['conventions', 'work', 'documentation']:
            if ref.startswith(cat):
                categories[cat].append(s['summary'])
                placed = True
                break
        if placed:
            break
    if not placed:
        categories['conversation'].append(s['summary'])
# Output categorized (last 3 per category, always show all categories)
for cat in ['conversation', 'conventions', 'work', 'documentation']:
    items = categories[cat][-3:]
    print(f\"**{cat}**\")
    if items:
        for item in items:
            print(f\"  - {item}\")
    else:
        print(f\"  - (none)\")
    print()
"`

### Memory Stats
!`python3 scripts/memory_stats.py`

---

## The Mindmap Is Your Memory Grid

**The mindmap is not decoration — it is your operating memory.** Every node is a directive that governs how you behave in this session. After loading, you MUST internalize all nodes before proceeding with any task.

**Node groups and what they mean for your behavior:**

- **architecture** nodes → Define HOW you work. System design rules. Follow as implementation constraints.
- **constraints** nodes → Define BOUNDARIES. Hard limits. Never violate.
- **conventions** nodes → Define HOW you execute. Patterns and standards. Apply consistently.
- **work** nodes → Define STATE. Accomplished/staged results. Continuity anchor.
- **session** nodes → Define CONTEXT. Brainstorming record. References work for concordance.
- **documentation** nodes → Define STRUCTURE. Documentation references (TBD).

**On every load:** Walk the full tree mentally. Each node is a rule you commit to follow.

---

**Display conventions:**

Depth filtering is driven by `conventions/depth_config.json` (human-editable). The config specifies:
- `default_depth`: depth limit for all top-level groups (default: 3)
- `omit`: branches hidden in normal mode (default: architecture, constraints)
- `overrides`: per-branch depth overrides (e.g. session/near memory: 4)

**Normal mode** (`/mind-context`): Runs `mindmap_filter.py` with depth config. Uses `%%{init: {'theme': 'default', 'mindmap': {'useMaxWidth': true}}}%%`.

**Full mode** (`/mind-context full`): All nodes at max depth.

**Branch override** (`/mind-context <path> <depth>`): Sets depth for a branch, persists to config, and renders.

**Branch peek** (`/mind-context <path>`): Temporarily shows a branch at full depth without saving.

**MANDATORY OUTPUT RULE:** After loading the data above, you MUST follow this sequence:
1. **READ** the full mindmap source, display conventions, and memory grid rules — internalize every node as an operational directive BEFORE rendering
2. **COPY the exact script output verbatim** — do NOT rephrase, summarize, or reformat ANY of the three sections below
3. **OUTPUT** three sections, each copied EXACTLY from the script output above:
   - **Mindmap**: copy the mermaid code block from mindmap_filter.py output EXACTLY as-is, inside a ```mermaid fence
   - **Recent Context**: copy the near_memory categorized output EXACTLY as-is — all 4 categories (conversation, conventions, work, documentation), all bullet points — VERBATIM
   - **Memory Stats**: copy the markdown table from memory_stats.py output EXACTLY as-is — all rows including Subtotal, System overhead, Conversation, Context used, Usable limit, Available
4. A session confirmation line

**CRITICAL:** The scripts above already generate perfectly formatted output. Your job is to COPY it, not interpret it. Do NOT summarize section 2 into fewer lines. Do NOT drop table rows from section 3. Do NOT say "context loaded" — show the actual data.

**DO NOT** silently consume this data. **DO NOT** just say "context loaded". The user MUST see all three sections rendered EXACTLY as the scripts produced them.

After outputting, confirm you are in an active K_MIND session, that you have internalized the memory grid, and will maintain all memory files using scripts per CLAUDE.md instructions. Read CLAUDE.md now for full maintenance instructions.

**Available scripts** (run these, don't improvise):
- Every turn: `python3 scripts/memory_append.py --role user --content "..." --role2 assistant --content2 "..." --summary "..." --mind-refs "..."`
- Split topics: `python3 scripts/far_memory_split.py --topic "..." --start-msg N --end-msg N --start-near N --end-near N`
- Recall memory: `python3 scripts/memory_recall.py --subject "..." [--full] [--list]`
- New session: `python3 scripts/session_init.py --session-id "..." [--preserve-active]`
- Set depth: `python3 scripts/set_depth.py --path "..." --depth N`
- Filter mindmap: `python3 scripts/mindmap_filter.py [--full] [--path "..." --depth N]`
- Memory stats: `python3 scripts/memory_stats.py`
