# K_MIND — Memory System Instructions

## Core Principle: Mind-First

Always read `mind/mind_memory.md` FIRST as your primary context. This is the hive view — one glance to see everything. Only dig into domain JSON files and session memory files when you need full details.

## File Structure

- `mind/mind_memory.md` — Core mermaid mindmap. The subconscious mind. Primary reference.
- `sessions/far_memory.json` — Full verbatim conversation history.
- `sessions/near_memory.json` — Real-time summaries with pointers to far_memory and mind_memory.
- `architecture/architecture.json` — System design references (static).
- `constraints/constraints.json` — Known limitations references (semi-dynamic).
- `work/work.json` — Accomplished/staged work results. The stable reference point for continuity.
- `conventions/conventions.json` — Reusable patterns discovered during work (growing).
- `documentation/documentation.json` — Documentation structure references (TBD).

## Lifecycle Events

### On Session Start
1. Read `mind/mind_memory.md` first
2. Begin real-time maintenance of all memory files
3. Only read session/domain files when needing details

### On Resume
1. Re-read `mind/mind_memory.md` to restore context
2. Dig into memory files as needed for continuity
3. Continue real-time maintenance

### On Compaction Recovery
1. Re-read `mind/mind_memory.md` — this is your primary recovery source
2. Read `sessions/near_memory.json` for recent summary context
3. Dig into `sessions/far_memory.json` only if needed for specific details
4. Continue real-time maintenance

## Every Turn — Real-Time Maintenance

1. Append user message and assistant response to `sessions/far_memory.json` (verbatim)
2. Update `sessions/near_memory.json` with a summary and pointers
3. Update `mind/mind_memory.md` mindmap nodes as needed
4. Update domain JSON files when relevant knowledge is produced
5. `session` and `work` child nodes in the mindmap use inline refs: `[far:N,near:N]`

## Mindmap Node Groups

- **architecture** — Static. System design. Changes only when the system evolves.
- **constraints** — Semi-dynamic. Known limitations from conception decisions.
- **session** — Dynamic. The brainstorming record. References accomplished work for concordance and continuity.
- **work** — Dynamic. Accomplished/staged work results. The stable reference point that session brainstorming anchors against.
- **conventions** — Growing. Reusable patterns and standards accumulated during building.
- **documentation** — TBD. Documentation structure to be defined later.

## Session Files Role

Session files (far_memory, near_memory) are the dynamic brainstorming record. They reference accomplished work in `work/` for concordance and continuity of working and building activities.
