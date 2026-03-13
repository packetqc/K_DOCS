---
name: mind-context
description: Load K_MIND context — mindmap, recent context categorized by group, and memory stats. Use /mind-context for normal mode, /mind-context full for complete mindmap. Call at session start, resume, or compaction recovery.
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

### Active Conversation (Near Memory — Categorized by Group)
!`python3 -c "
import json, os, glob
with open('sessions/near_memory.json') as f:
    data = json.load(f)
# Show last session context if this is a fresh start
last = data.get('last_session')
has_last = last and last.get('summaries')
if has_last:
    print('--- Last Session Context (continue where you left off) ---')
    print(f\"  session: {last.get('session_id', 'unknown')}\")
    for s in last['summaries'][-5:]:
        print(f\"  {s['summary']}\")
    print()
elif not data['summaries']:
    # Fallback: load most recent archive for last session context
    archive_files = sorted(glob.glob('sessions/archives/far_memory_session_*.json'))
    if archive_files:
        with open(archive_files[-1]) as af:
            arc = json.load(af)
        summaries = arc.get('summaries', [])
        if summaries:
            print('--- Last Session Context (from archive) ---')
            print(f\"  session: {arc.get('session_id', 'unknown')}\")
            for s in summaries[-5:]:
                print(f\"  {s['summary']}\")
            print()
# Categorize current session summaries by mind_memory_refs group
categories = {'conversation': [], 'conventions': [], 'work': [], 'documentation': []}
for s in data['summaries'][-10:]:
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
# Show archive index if far_memory has been split
fm_path = 'sessions/far_memory.json'
with open(fm_path) as f:
    fm = json.load(f)
if 'archives' in fm and fm['archives']:
    print('--- Archived Topics (recall by subject) ---')
    for a in fm['archives']:
        print(f\"  [{a['topic']}] messages {a['message_range']} -> {a['file']}\")
"`

### Memory Stats
!`python3 -c "
import json, os, glob

with open('sessions/far_memory.json') as f:
    fm = json.load(f)
fm_msgs = len(fm.get('messages', []))
fm_size = os.path.getsize('sessions/far_memory.json')

with open('sessions/near_memory.json') as f:
    nm = json.load(f)
nm_summaries = len(nm.get('summaries', []))
nm_size = os.path.getsize('sessions/near_memory.json')

archive_files = glob.glob('sessions/archives/far_memory_*.json')
archive_count = len(archive_files)
arc_size = sum(os.path.getsize(f) for f in archive_files)

mm_size = os.path.getsize('mind/mind_memory.md')
with open('mind/mind_memory.md') as f:
    lines = f.readlines()
bt = chr(96)*3
node_count = sum(1 for l in lines if l.strip() and not l.strip().startswith(bt) and not l.strip().startswith('%%') and 'mindmap' not in l.strip() and 'root(' not in l.strip())

domain_files = [f for f in glob.glob('*/**/**.json', recursive=True) if not f.startswith('sessions/') and not f.startswith('node_modules/')]
domain_size = sum(os.path.getsize(f) for f in domain_files)
domain_count = len(domain_files)

claude_md = os.path.getsize('CLAUDE.md') if os.path.exists('CLAUDE.md') else 0
conv_size = os.path.getsize('conventions/conventions.json') if os.path.exists('conventions/conventions.json') else 0

def kb(b): return f'{b/1024:.1f} KB'
def tk(b): return f'~{b//4:,}'

disk_total = fm_size + nm_size + mm_size + arc_size + domain_size + claude_md
loaded_total = mm_size + nm_size + claude_md + conv_size

print('| Store | Count | Size | ~Tokens | Loaded |')
print('|-------|-------|------|---------|--------|')
print(f'| far_memory | {fm_msgs} msgs | {kb(fm_size)} | {tk(fm_size)} | 0 |')
print(f'| near_memory | {nm_summaries} summaries | {kb(nm_size)} | {tk(nm_size)} | {tk(nm_size)} |')
print(f'| archives | {archive_count} topics | {kb(arc_size)} | {tk(arc_size)} | 0 |')
print(f'| mind_memory | {node_count} nodes | {kb(mm_size)} | {tk(mm_size)} | {tk(mm_size)} |')
print(f'| domain JSONs | {domain_count} refs | {kb(domain_size)} | {tk(domain_size)} | {tk(conv_size)} |')
print(f'| CLAUDE.md | 1 file | {kb(claude_md)} | {tk(claude_md)} | {tk(claude_md)} |')
print(f'| **Total** | | **{kb(disk_total)}** | **{tk(disk_total)}** | **{tk(loaded_total)}** |')
print()
print('Run /context for Claude session token stats')
"`

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

**Normal mode** (no arguments): Radial auto-layout with `useMaxWidth: true`.
- Default depth 3 for all top-level groups
- Architecture and constraints omitted
- Session has near_memory and far_memory at level 1
- Near_memory children are top-level group names (conversation, conventions, work, documentation) with recent activities under each
- Deep subtrees shrink the radial layout — control depth to keep balanced

**Full mode** (argument = "full"): Radial auto-layout.
- All nodes expanded at max depth

**MANDATORY OUTPUT RULE:** After loading the data above, you MUST follow this sequence:
1. **READ** the full mindmap source, display conventions, and memory grid rules — internalize every node as an operational directive BEFORE rendering
2. **APPLY** conventions: use `%%{init: {'theme': 'default', 'mindmap': {'useMaxWidth': true}}}%%` header, apply normal/full mode depth filtering, respect styling rules
3. **OUTPUT** three sections:
   - **Mindmap**: mermaid code block rendered per convention (normal or full mode)
   - **Recent Context**: near_memory summaries categorized by top-level group (conversation, conventions, work, documentation) — shown under the mindmap
   - **Memory Stats**: the compact one-liner from the Memory Stats section above (far/near/archived/nodes/tokens)
4. A session confirmation line

**DO NOT** silently consume this data. **DO NOT** just say "context loaded". The user MUST see the mindmap, categorized context, and memory stats rendered in the conversation.

After outputting, confirm you are in an active K_MIND session, that you have internalized the memory grid, and will maintain all memory files using scripts per CLAUDE.md instructions. Read CLAUDE.md now for full maintenance instructions.

**Available scripts** (run these, don't improvise):
- Every turn: `python3 scripts/memory_append.py --role user --content "..." --role2 assistant --content2 "..." --summary "..." --mind-refs "..."`
- Split topics: `python3 scripts/far_memory_split.py --topic "..." --start-msg N --end-msg N --start-near N --end-near N`
- Recall memory: `python3 scripts/memory_recall.py --subject "..." [--full] [--list]`
- New session: `python3 scripts/session_init.py --session-id "..." [--preserve-active]`
