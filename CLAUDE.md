# K_MIND — Memory System Instructions

## Core Principle: Mind-First

Always read `mind/mind_memory.md` FIRST as your primary context. This is the hive view — one glance to see everything. Only dig into domain JSON files and session memory files when you need full details.

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

### On New Session Start
1. Run: `python3 scripts/session_init.py --session-id "<id>"`
2. Run `/mind-context` to load the reduced mindmap and recent context
3. Begin real-time maintenance using scripts

### On Resume
1. Run: `python3 scripts/session_init.py --session-id "<id>" --preserve-active`
2. Run `/mind-context` to restore context from the mindmap and recent summaries
3. Dig into memory files as needed for continuity
4. Continue real-time maintenance using scripts

### On Compaction Recovery
1. Run `/mind-context` to recover context from the mindmap and recent summaries
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

## Mindmap Node Groups

- **architecture** — Static. System design. Changes only when the system evolves.
- **constraints** — Semi-dynamic. Known limitations from conception decisions.
- **session** — Dynamic. The brainstorming record. References accomplished work for concordance and continuity.
- **work** — Dynamic. Accomplished/staged work results. The stable reference point that session brainstorming anchors against.
- **conventions** — Growing. Reusable patterns and standards accumulated during building.
- **documentation** — TBD. Documentation structure to be defined later.

## Session Files Role

Session files (far_memory, near_memory) are the dynamic brainstorming record. They reference accomplished work in `work/` for concordance and continuity of working and building activities.
