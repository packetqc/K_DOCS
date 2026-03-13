---
name: mind-context
description: Load K_MIND context — reduced mindmap (session, work, conventions, documentation) plus recent session context. Use /mind-context for dynamic nodes only, /mind-context full for complete mindmap. Call at session start, resume, or compaction recovery.
allowed-tools: Read, Grep, Glob, Bash
---

## K_MIND — Active Context

Arguments: $ARGUMENTS

### Mind Map
!`cat mind/mind_memory.md`

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

### Active Conversation (Near Memory — Last 5 Summaries)
!`python3 -c "
import json, os
with open('sessions/near_memory.json') as f:
    data = json.load(f)
# Show last 5 summaries as active conversation context
for s in data['summaries'][-5:]:
    print(f\"[near:{s['id']}] {s['summary']}\")
    print(f\"  far_refs: {s['far_memory_refs']}\")
    print(f\"  mind_refs: {s['mind_memory_refs']}\")
    print()
# Show archive index if far_memory has been split
fm_path = 'sessions/far_memory.json'
with open(fm_path) as f:
    fm = json.load(f)
if 'archives' in fm and fm['archives']:
    print('--- Archived Topics (recall by subject) ---')
    for a in fm['archives']:
        print(f\"  [{a['topic']}] messages {a['message_range']} -> {a['file']}\")
"`

---

**Display conventions:**

**Normal mode** (no arguments): Left-right half/half layout.
- Present only the LEFT side nodes: **session**, **work**, **documentation**
- Omit the RIGHT side: architecture, constraints, and conventions subtrees

**Full mode** (argument = "full"): Left-right half/half layout.
- Present the complete mindmap as-is from the file
- LEFT side (first in source): session, work, documentation
- RIGHT side (last in source): architecture, constraints, conventions

**MANDATORY OUTPUT RULE:** After loading the data above, you MUST follow this sequence:
1. **READ** the mindmap source and the display conventions loaded above — internalize theme, layout, and styling rules BEFORE rendering
2. **APPLY** conventions when outputting: preserve the `%%{init:...}%%` theme header, apply normal/full mode filtering per layout convention, respect styling rules
3. **OUTPUT** the mermaid code block with the mindmap (reduced or full per mode) — inside a ```mermaid fence so it renders visually
4. The last 5 near_memory summaries as a formatted list
5. A session confirmation line

**DO NOT** silently consume this data. **DO NOT** just say "context loaded". The user MUST see the mindmap and summaries rendered in the conversation every single time this skill is invoked — at session start, resume, compaction recovery, or on demand.

After outputting, confirm you are in an active K_MIND session and will maintain all memory files using scripts per CLAUDE.md instructions. Read CLAUDE.md now for full maintenance instructions.

**Available scripts** (run these, don't improvise):
- Every turn: `python3 scripts/memory_append.py --role user --content "..." --role2 assistant --content2 "..." --summary "..." --mind-refs "..."`
- Split topics: `python3 scripts/far_memory_split.py --topic "..." --start-msg N --end-msg N --start-near N --end-near N`
- Recall memory: `python3 scripts/memory_recall.py --subject "..." [--full] [--list]`
- New session: `python3 scripts/session_init.py --session-id "..." [--preserve-active]`
