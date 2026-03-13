---
name: mind-context
description: Load K_MIND context — reduced mindmap (session, work, conventions, documentation) plus recent session context. Use /mind-context for dynamic nodes only, /mind-context full for complete mindmap. Call at session start, resume, or compaction recovery.
allowed-tools: Read, Grep, Glob
---

## K_MIND — Active Context

Arguments: $ARGUMENTS

### Mind Map
!`cat mind/mind_memory.md`

### Recent Context (Near Memory — Last 3 Summaries)
!`python3 -c "
import json
with open('sessions/near_memory.json') as f:
    data = json.load(f)
for s in data['summaries'][-3:]:
    print(f\"[near:{s['id']}] {s['summary']}\")
    print(f\"  far_refs: {s['far_memory_refs']}\")
    print(f\"  mind_refs: {s['mind_memory_refs']}\")
    print()
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
