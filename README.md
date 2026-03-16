# Knowledge — Documentation & Knowledge System

**Single-file documentation engine** with live mindmap, 4 themes, PDF/DOCX export, and bilingual EN/FR support.

Built with Claude Code (Anthropic, Opus 4.6) as a multi-module knowledge system. Development happens in [packetqc/K_DOCS](https://github.com/packetqc/K_DOCS) — this production repo receives the same codebase.

---

## What's Inside

| Component | Count | Description |
|-----------|-------|-------------|
| **Publications** | 23+ | Technical documentation in `docs/publications/` — EN + FR |
| **Success Stories** | 26 | Validated capabilities in `docs/publications/success-stories/` |
| **Interfaces** | 5 | Interactive pages: navigator, session review, task workflow, project viewer, live mindmap |
| **Web Viewer** | 1 | `docs/index.html` — single-file documentation engine (~1800 lines) |
| **K_MIND** | 1 | Memory system in `Knowledge/K_MIND/` — mindmap, sessions, conventions |
| **Modules** | 5 | K_MIND (core), K_DOCS, K_VALIDATION, K_PROJECTS, K_GITHUB |

## Key Features

- **Single-File Viewer** — One `index.html` renders all documentation. No build step, no server dependencies
- **4-Theme System** — Daltonism Light/Dark, Cayman, Midnight — CSS variables + localStorage
- **Three-Panel Layout** — Left navigator, center content, right interfaces — draggable dividers
- **PDF/DOCX Export** — Corporate styling, cover page, TOC page 2, running header/footer
- **Live Mindmap** — MindElixir v5.9.3 with depth filtering and theme sync
- **Bilingual EN/FR** — Full French mirror at `docs/fr/`, language toggle, dual permalinks
- **Markdown Pipeline** — Fetch `.md` → parse front matter → resolve Liquid → marked.js → Mermaid → DOM
- **Webcards** — Animated OG images for social preview, theme-aware

## Structure

```
knowledge/
├── CLAUDE.md                    # K_MIND system instructions
├── README.md                    # This file
├── Knowledge/
│   ├── K_MIND/                  # Core: memory system (mindmap, sessions, scripts)
│   ├── K_DOCS/                  # Module: documentation conventions, methodology
│   ├── K_VALIDATION/            # Module: QA, task compilation, session validation
│   ├── K_PROJECTS/              # Module: project management, compilation
│   └── K_GITHUB/                # Module: GitHub integration, sync scripts
└── docs/                        # Documentation (GitHub Pages root)
    ├── index.html               # Single-file viewer engine
    ├── .nojekyll                 # Serve raw markdown (no Jekyll)
    ├── publications/            # EN publications (23+)
    ├── fr/publications/         # FR mirror
    ├── interfaces/              # Interactive pages (I1–I5)
    ├── data/                    # JSON data (sessions, tasks, projects)
    └── assets/og/               # Animated GIF webcards
```

## Live

**Production**: [packetqc.github.io/knowledge](https://packetqc.github.io/knowledge/)

---

**Authors**: Martin Paquet & Claude (Anthropic, Opus 4.6)
