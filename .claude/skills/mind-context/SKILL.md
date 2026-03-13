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

**Mode**: If arguments contain "full", present the complete mindmap above as-is. Otherwise, present only the dynamic node subtrees: **session**, **work**, **conventions**, **documentation** — omit the architecture and constraints subtrees from your output.

**After presenting the context**, confirm you are in an active K_MIND session and will maintain all memory files in real-time per CLAUDE.md instructions. Read CLAUDE.md now for full maintenance instructions.
