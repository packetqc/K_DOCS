# K_TOOLS — Command & Utilities Module

Knowledge module for the command framework, help system, and operational utilities. Houses all user-facing command definitions, routing, contextual help, and tool scripts imported from the legacy knowledge engine.

## Structure

```
K_TOOLS/
├── conventions/
│   └── conventions.json        # Command framework conventions
├── documentation/
│   └── documentation.json      # Methodology references
├── methodology/
│   └── commands.md             # Master command reference (Part 1)
├── scripts/
│   ├── help_command.py         # Multipart help display
│   └── help_contextual.py     # Per-command contextual help
├── work/
│   └── work.json               # Active work items
└── README.md
```

## Purpose

K_TOOLS manages:
- Command registry and routing (all user-facing slash commands)
- Help system (multipart help display + contextual help per command)
- Command-to-module mapping (which command belongs to which K_* module)
- Operational utility scripts imported from legacy engine

## Command Framework

The help command displays a **multipart concatenated** command table:
- **Part 1**: Knowledge commands (always available, defined here in K_TOOLS)
- **Part 2**: Project-specific commands (defined per-project in CLAUDE.md)

Commands are organized by domain group (Session, Normalize, Harvest, Publications, Project, Live, Visual, Network) and each maps to a target K_* module for execution.

## Integration

- Sessions and mindmap stay centralized in K_MIND
- Domain-specific conventions, documentation, and work tracked here
- Scripts in K_MIND auto-detect this module via `K_*` sibling scanning
- Commands route to their target modules (K_DOCS, K_PROJECTS, K_VALIDATION, etc.)

---

*Part of the Knowledge 2.0 multi-module architecture*
