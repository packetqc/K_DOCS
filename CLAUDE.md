# K_MIND — Memory System Instructions

## Core Principle: Mind-First — The Mindmap Is Your Memory Grid

Always read `mind/mind_memory.md` FIRST as your primary context. This is the hive view — one glance to see everything. Only dig into domain JSON files and session memory files when you need full details.

**The mindmap is not decoration — it is your operating memory.** Every node is a directive that governs how you behave. On every load (start, resume, compaction recovery), walk the full tree and internalize each node as a rule you commit to follow:

- **architecture** nodes → HOW you work. System design rules. Follow as implementation constraints.
- **constraints** nodes → BOUNDARIES. Hard limits. Never violate.
- **conventions** nodes → HOW you execute. Patterns and standards. Apply consistently.
- **work** nodes → STATE. What's accomplished/staged. Your continuity anchor.
- **session** nodes → CONTEXT. Current brainstorming record. References work for concordance.
- **documentation** nodes → STRUCTURE. Documentation references.

If a node says "scripts handle all mechanical operations" — you use scripts. If a node says "split by summarized subjects not size" — you split by subject. The mindmap is your contract with the system.

## Core Principle: Programs Over Improvisation

Claude-as-engine is ONLY the bootstrap (new session, resume, compaction recovery). All mechanical operations use scripts. Claude provides intelligence (summaries, topic names) as arguments to deterministic programs.

## File Structure

- `mind/mind_memory.md` — Core mermaid mindmap. The subconscious mind. Primary reference.
- `sessions/far_memory.json` — Full verbatim conversation history.
- `sessions/near_memory.json` — Real-time summaries with pointers to far_memory and mind_memory.
- `sessions/archives/` — Topic-based far_memory archive files.
- `architecture/architecture.json` — System design references (static).
- `constraints/constraints.json` — Known limitations references (semi-dynamic).
- `work/work.json` — Accomplished/staged work results. The stable reference point for continuity.
- `conventions/conventions.json` — Reusable patterns discovered during work (growing).
- `documentation/documentation.json` — Documentation structure references (TBD).

## Scripts (deterministic programs)

- `scripts/memory_append.py` — Append messages to far_memory + summary to near_memory. Called every turn.
- `scripts/far_memory_split.py` — Archive completed topics from far_memory by subject.
- `scripts/memory_recall.py` — Search and load archived memory by subject keyword.
- `scripts/session_init.py` — Initialize fresh session files (preserves archives).

## Lifecycle Events

### MANDATORY: Mindmap Output Rule

**Every time `/mind-context` is invoked — whether at session start, resume, compaction recovery, or on demand — Claude MUST output the mermaid mindmap code block and the recent near_memory summaries as visible text in the conversation.** This is not optional. The mindmap is the user's primary interface to the knowledge system. Failing to output it defeats the purpose of the skill. The output must include:
1. The mermaid code block (reduced or full per mode)
2. Last session context (if fresh start — shows where work was left off)
3. The last 5 near_memory summaries from current session
4. Session confirmation

### On New Session Start
1. Run: `python3 scripts/session_init.py --session-id "<id>"`
   - Previous session is auto-archived but its summaries are carried forward in `near_memory.json` under `last_session`
2. Run `/mind-context` and **output the mindmap and context visually**
   - The last session's summaries will be displayed as "Last Session Context" so Claude and user can see where work was left off
   - Use this context to orient: check work nodes in the mindmap for accomplished tasks, and last session summaries for recent activity
3. Begin real-time maintenance using scripts

### On Resume
1. Run: `python3 scripts/session_init.py --session-id "<id>" --preserve-active`
2. Run `/mind-context` and **output the mindmap and context visually**
3. Dig into memory files as needed for continuity
4. Continue real-time maintenance using scripts

### On Compaction Recovery
1. Run `/mind-context` and **output the mindmap and context visually**
2. Use `python3 scripts/memory_recall.py --subject "<topic>"` if needed for specific details
3. Continue real-time maintenance using scripts

### Full Context
Run `/mind-context full` when you need the complete mindmap including architecture and constraints trees.

## Every Turn — Real-Time Maintenance

1. **Run the append script** (handles far_memory + near_memory atomically):
   ```bash
   python3 scripts/memory_append.py \
       --role user --content "user message" \
       --role2 assistant --content2 "assistant response" \
       --summary "one-line summary" \
       --mind-refs "knowledge::node1,knowledge::node2"
   ```
2. Update `mind/mind_memory.md` mindmap nodes as needed
3. Update domain JSON files when relevant knowledge is produced
4. `session` and `work` child nodes in the mindmap use inline refs: `[far:N,near:N]`

## Far Memory Topic Splitting

When `sessions/far_memory.json` grows large, run:
```bash
python3 scripts/far_memory_split.py \
    --topic "Topic Name" \
    --start-msg 1 --end-msg 24 \
    --start-near 1 --end-near 7
```

Claude identifies topic boundaries from near_memory summary clusters, then calls the script.

## Memory Recall

To recall a past topic:
```bash
python3 scripts/memory_recall.py --subject "architecture"
python3 scripts/memory_recall.py --list
python3 scripts/memory_recall.py --subject "theme" --full
```

## Mindmap Node Groups — Behavioral Mapping

Each group maps to a behavioral category. When you read a node, you adopt its directive:

- **architecture** — Static. System design. HOW you work. Changes only when the system evolves.
- **constraints** — Semi-dynamic. Known limitations. BOUNDARIES you never violate.
- **conventions** — Growing. Reusable patterns. HOW you execute every operation.
- **work** — Dynamic. Accomplished/staged results. STATE you check before starting new tasks.
- **session** — Dynamic. Brainstorming record. CONTEXT that references work for concordance.
- **documentation** — TBD. Documentation structure. REFERENCES to be defined later.

## Session Files Role

Session files (far_memory, near_memory) are the dynamic brainstorming record. They reference accomplished work in `work/` for concordance and continuity of working and building activities.
