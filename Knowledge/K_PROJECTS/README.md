# K_PROJECTS — Project Management Module

Knowledge module for project tracking, milestones, and cross-project coordination.

## Structure

```
K_PROJECTS/
├── conventions/
│   └── conventions.json    # Project management conventions
├── documentation/
│   └── documentation.json  # Methodology references
├── methodology/            # Project management methodologies
├── work/
│   └── work.json           # Active project work items
└── README.md
```

## Purpose

K_PROJECTS manages:
- Project definitions and milestones
- Cross-module coordination (K_MIND, K_DOCS, K_VALIDATION)
- GitHub project board integration
- Release planning and tracking

## Integration

- Sessions and mindmap stay centralized in K_MIND
- Domain-specific conventions, documentation, and work tracked here
- Scripts in K_MIND auto-detect this module via `K_*` sibling scanning

---

*Part of the Knowledge 2.0 multi-module architecture*
