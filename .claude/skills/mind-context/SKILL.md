---
name: mind-context
description: Load K_MIND context — reduced mindmap (session, work, conventions, documentation) plus recent session context. Use /mind-context for dynamic nodes only, /mind-context full for complete mindmap. Call at session start, resume, or compaction recovery.
allowed-tools: Read, Grep, Glob
---

## K_MIND — Active Context

Arguments: $ARGUMENTS

### Mind Map
!`cat mind/mind_memory.md`

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

**After presenting the context**, confirm you are in an active K_MIND session and will maintain all memory files in real-time per CLAUDE.md instructions. Read CLAUDE.md now for full maintenance instructions.
