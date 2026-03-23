# Interactive Conception — Convention

> Adapted from `packetqc/knowledge:knowledge/methodology/interactive-conception.md`

Ideating, prototyping, and validating new capabilities through interactive collaboration.

## When to Use

- Designing a new system capability (command, protocol, architecture)
- Exploring ideas without clear implementation path
- Prototyping features needing user validation before formalization
- Architecture exploration and pattern discovery

## Core Principles

1. **Ideas before structure** — let the concept form before forcing publication structure
2. **User validation gates** — present proposals before building
3. **Capture before formalize** — raw notes preserve ideas if session crashes
4. **Progressive crystallization** — idea → notes → methodology → publication (each a commit)
5. **Meta-awareness** — conception sessions discover patterns about the process itself

## Phase Pattern

| Phase | Action | Commit |
|-------|--------|--------|
| **Anchor** | Session issue protocol — create issue, post verbatim demand | — |
| **Ideate** | User shares idea, Claude expands | — |
| **Explore** | Read existing code/methodology for context | — |
| **Propose** | Present structured proposal to user | — |
| **Prototype** | Create initial files (methodology, source, scripts) | Per artifact |
| **Validate** | User reviews, provides corrections | — |
| **Iterate** | Apply corrections, refine | Per correction |
| **Formalize** | If validated, promote to publication | Per publication |
| **Deliver** | Essential files + push + PR | Final push |
