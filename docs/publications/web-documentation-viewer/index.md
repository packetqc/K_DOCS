---
layout: publication
title: "K_DOCS Web Viewer — Single-File Documentation Engine"
description: "A single index.html that renders markdown publications with 4 themes, PDF/DOCX export, three-panel navigation, live mindmap, and bilingual support — zero build step, zero server dependencies."
permalink: /publications/web-documentation-viewer/
lang: en
permalink_fr: /fr/publications/web-documentation-viewer/
header_title: "K_DOCS Web Viewer"
tagline: "Single-File Documentation Engine"
pub_id: "Publication #23"
pub_meta: "Publication #23 v1 | March 2026"
pub_version: "v1"
pub_number: 23
pub_date: "March 2026"
og_image: /assets/og/knowledge-2-en-cayman.gif
keywords: "documentation viewer, single-file, static, themes, export, panels, mindmap, bilingual"
---

## Overview

The K_DOCS Web Viewer is a **single HTML file** (`docs/index.html`) that serves as a complete documentation platform. It renders markdown files with YAML front matter, applies one of four CSS themes, exports to PDF and DOCX with corporate styling, navigates between three draggable panels, and displays a live interactive mindmap — all with zero build step and zero server-side processing.

### Key Features

| Feature | Description |
|---------|-------------|
| **Markdown pipeline** | Fetch `.md` → parse front matter → resolve Liquid → marked.js → Mermaid → DOM |
| **4-theme system** | Daltonism Light/Dark, Cayman, Midnight — CSS variables + localStorage |
| **Three-panel layout** | Left navigator, center content, right interfaces — draggable dividers |
| **PDF/DOCX export** | Corporate styling, cover page, TOC page 2, running header/footer |
| **Live mindmap** | MindElixir v5.9.3 with depth filtering and theme sync |
| **Bilingual EN/FR** | Language toggle, dual permalinks, dynamic labels |
| **Interface routing** | Cross-panel navigation without full page reloads |
| **Chrome bar** | Unified collapsible metadata bar for all panels |

---

## Read More

- **[Complete documentation](full/)** — Full publication with architecture, pipeline details, and conventions
- **[Success Story #26]({{ '/publications/success-stories/story-26/' | relative_url }})** — The story behind building this viewer

---

*Martin Paquet & Claude (Opus 4.6) | [packetqc/K_DOCS](https://github.com/packetqc/K_DOCS)*
