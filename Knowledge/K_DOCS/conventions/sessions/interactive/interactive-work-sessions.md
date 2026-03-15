# Interactive Work Sessions — Convention

> Adapted from `packetqc/knowledge:knowledge/methodology/interactive-work-sessions.md`

Resilient, multi-delivery interactive sessions that survive crashes, produce progressive deliverables, and persist knowledge through multiple channels.

## When to Use

| Session type | Examples |
|-------------|----------|
| **Interactive design** | Features, architectures, webcards, UI layouts |
| **Interactive documentation** | Publications, methodologies, success stories |
| **Interactive feature development** | Commands, scripts, pipelines |
| **Interactive diagnostic** | Rendering, integration, behavioral problems |

## Core Principles

1. **GitHub Issue as session anchor** — external persistence survives crashes
2. **Progressive commits** — each step committed, no big-bang at end
3. **Push as savepoint** — push at milestones, recover retrieves stranded work
4. **Todo-driven execution** — one `in_progress` at a time, mark `completed` immediately
5. **User correction > AI assumption** — follow redirects immediately, never reinterpret
6. **Context budget awareness** — focus on essential files, avoid unbounded searches

## Session Protocol

1. **Anchor** — create GitHub issue before first file touch (title confirmation via user)
2. **Plan** — break request into atomic, ordered TodoWrite items
3. **Execute** — per todo: work → commit → push → mark completed → issue comment
4. **Corrections** — stop → acknowledge → adapt → learn
5. **Deliver** — essential files check → commit → push → PR
6. **Close** — integrity check → pre-save summary → post session notes → close issue

## Five Persistence Channels

| Channel | Survives crash | Survives compaction | Real-time |
|---------|---------------|-------------------|-----------|
| **Git** (commits, branches) | Yes (if pushed) | Yes | No |
| **Notes** (session-*.md) | Yes (if committed) | No | No |
| **GitHub Issue** (comments) | Yes (API-persisted) | Yes | Yes |
| **Cache** (session-runtime JSON) | Yes (auto-committed) | Yes | Yes |
| **Startup Hook** (hooks/startup) | Yes (code on disk) | Yes | Yes |

## Session Type Patterns

### Interactive Diagnostic → `interactive-diagnostic.md`
Document → Compare → Eliminate → Pivot → Isolate → Resolve

### Interactive Documentation → `interactive-documentation.md`
Gather → Structure → Expand → Web pages → Essential files → Deliver

### Interactive Conception → `interactive-conception.md`
Anchor → Ideate → Explore → Propose → Prototype → Validate → Formalize → Deliver

## Anti-Patterns

| Anti-pattern | Fix |
|-------------|-----|
| Big bang commit | Progressive commits at each todo |
| Push at end only | Push at each major milestone |
| No issue anchor | Open issue at session start |
| Silent todo completion | Each completed todo = one issue comment |
| Ignoring user corrections | Try user's suggestion first |
| Unbounded file scanning | Target essential files only |
