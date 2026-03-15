# K_GITHUB — GitHub Integration Module

Knowledge module for GitHub operations, CI/CD, and repository management.

## Structure

```
K_GITHUB/
├── conventions/
│   └── conventions.json    # GitHub workflow conventions
├── documentation/
│   └── documentation.json  # Methodology references
├── methodology/            # GitHub-related methodologies
├── work/
│   └── work.json           # Active GitHub work items
└── README.md
```

## Purpose

K_GITHUB manages:
- GitHub API integration (gh_helper.py conventions)
- Repository management (subtrees, remotes, push workflows)
- Issue and PR protocols (real-time comment protocol)
- Project board integration
- CI/CD and GitHub Pages deployment

## Integration

- Sessions and mindmap stay centralized in K_MIND
- Domain-specific conventions, documentation, and work tracked here
- Scripts in K_MIND auto-detect this module via `K_*` sibling scanning

---

*Part of the Knowledge 2.0 multi-module architecture*
