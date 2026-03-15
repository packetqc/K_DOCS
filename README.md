# packetqc/K_DOCS — Documentation & Knowledge System

**Single-file documentation engine** with live mindmap, 4 themes, PDF/DOCX export, and bilingual EN/FR support.

K_DOCS is the documentation satellite of [packetqc/knowledge](https://github.com/packetqc/knowledge) — it publishes technical documentation independently using a zero-build static viewer.

---

## What's Inside

| Component | Count | Description |
|-----------|-------|-------------|
| **Publications** | 23+ | Technical documentation in `docs/publications/` — EN + FR |
| **Success Stories** | 26 | Validated capabilities in `docs/publications/success-stories/` |
| **Interfaces** | 5 | Interactive pages in `docs/interfaces/` — navigator, mindmap, review |
| **Web Viewer** | 1 | `docs/index.html` — single-file documentation engine (~1500 lines) |
| **K_MIND** | 1 | Memory system in `Knowledge/K_MIND/` — mindmap, sessions, conventions |

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
K_DOCS/
├── CLAUDE.md                    # K_MIND system instructions
├── README.md                    # This file
├── LICENSE                      # MIT
├── .claude/skills/              # Claude Code skills
├── Knowledge/
│   ├── K_MIND/                  # Memory system (mindmap, sessions, scripts)
│   └── K_DOCS/                  # Module scripts
└── docs/                        # Documentation (GitHub Pages)
    ├── index.html               # Single-file viewer engine
    ├── publications/            # EN publications (23+)
    ├── fr/publications/         # FR mirror
    ├── interfaces/              # Interactive pages (I1–I5)
    └── assets/og/               # Animated GIF webcards
```

## Live

- **GitHub Pages**: [packetqc.github.io/K_DOCS](https://packetqc.github.io/K_DOCS/)
- **Production**: [packetqc.github.io/knowledge](https://packetqc.github.io/knowledge/)

---

**Authors**: Martin Paquet & Claude (Anthropic, Opus 4.6)
