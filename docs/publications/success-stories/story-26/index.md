---
layout: publication
title: "Story #26 — One Viewer to Rule Them All: A Single-File Documentation Engine"
description: "How a single index.html became a complete documentation platform — 3-panel layout, 4 themes, PDF/DOCX export, live mindmap, interface routing, and zero build step."
pub_id: "Publication #11 — Story #26"
version: "v1"
date: "2026-03-15"
permalink: /publications/success-stories/story-26/
og_image: /assets/og/knowledge-2-en-cayman.gif
keywords: "success story, viewer, documentation, single file, static, themes, export, panels"
---

# Story #26 — One Viewer to Rule Them All: A Single-File Documentation Engine

> **Parent publication**: [#11 — Success Stories]({{ '/publications/success-stories/' | relative_url }})

---

<div class="story-section">

> *"One HTML file. No build step. No framework. No server. Push markdown to GitHub, it renders with themes, exports to PDF and DOCX, routes across three panels, and serves a live interactive mindmap. The entire documentation platform is a single `index.html`."*

<div class="story-row">
<div class="story-row-left">

**Details**

</div>
<div class="story-row-right">

| | |
|---|---|
| Date | 2026-03-15 |
| Category | 🏗️ 🎨 📄 |
| Context | The production Knowledge repo uses Jekyll + GitHub Pages with two massive HTML layouts (183KB total). It works, but requires a build step, Ruby dependencies, and Jekyll-specific conventions. K_DOCS needed documentation without any of that — raw markdown files served by GitHub Pages with `.nojekyll`, rendered entirely client-side. |
| Triggered by | The decision to create K_DOCS as a standalone repo that publishes documentation independently of the production pipeline. The constraint: everything must work from a single static file with zero server-side processing. |
| Authored by | **Claude** (Anthropic, Opus 4.6) — from live session data |

</div>
</div>

## The Architecture — One File Does Everything

`docs/index.html` is the entire documentation engine. It handles:

### 1. Markdown Rendering Pipeline

```
URL param (?doc=path) → fetch .md → parse front matter → resolve Liquid →
marked.parse() → render mermaid → inject into DOM
```

- **Front matter parsing**: Extracts YAML metadata (title, description, author, version, etc.)
- **Liquid resolution**: Handles `{{ site.baseurl }}`, `{{ page.url }}`, `relative_url` filter
- **Mermaid rendering**: Client-side diagram rendering via CDN
- **kramdown IAL**: Strips `{: #id}` syntax and applies as HTML attributes

### 2. Three-Panel Layout

| Panel | Purpose | Content Source |
|-------|---------|---------------|
| Left | Main navigator — publication tree | `interfaces/main-navigator/index.md` |
| Center | Primary content viewer | Any markdown document |
| Right | Secondary content / interfaces | Interface pages (I1–I5) |

Panels are separated by **draggable dividers** (14px desktop, 8px mobile) with grip dots and click-to-step fallback.

### 3. Interface Routing

The routing system handles cross-panel navigation without full page reloads:

- **Right panel interface links** → route to center panel
- **Main navigator links** → reload full page
- **Embed pages** detect `window.name` for routing context
- **BroadcastChannel** propagates orientation changes across panels

### 4. Four-Theme System

All themes are pure CSS variables — no class swapping, no JavaScript style manipulation:

| Theme | Background | Accent | Purpose |
|-------|-----------|--------|---------|
| Daltonism Light | `#faf6f1` warm | `#0055b3` | Default, accessible |
| Daltonism Dark | `#1a1a2e` warm | `#5599dd` | Dark + accessible |
| Cayman | `#eff6ff` cool | `#1d4ed8` | Light blue |
| Midnight | `#0f172a` cool | `#60a5fa` | Dark blue |

Theme persists via `localStorage` and applies before DOM paint (inline script in `<head>`).

### 5. Export Engine

**PDF** — CSS Paged Media via `window.print()`:
- Corporate styling (not web theme colors)
- Cover page with title, description, authors
- TOC on page 2 with page break after
- Running header/footer with blue accent lines
- `@page` size, margins, orphans/widows control

**DOCX** — MSO elements with Calibri 10pt:
- Same TOC-on-page-2 convention
- `rewriteContentLinks()` converts internal paths to viewer URL format
- Same cover page structure

### 6. Webcards & Social Sharing

- `og:image` meta tag injection on document load
- Theme-aware webcard display (cayman variant for light, midnight for dark)
- `prefers-color-scheme` media query for auto-detection
- Live mindmap webcard via MindElixir when `live_webcard: mindmap` is set
- Graceful fallback with `onerror` handler for missing images

### 7. Live Mindmap Integration

MindElixir v5.9.3 renders the K_MIND knowledge graph directly in the viewer:
- Fetches `mind_memory.md` from GitHub
- Applies depth filtering from `depth_config.json`
- Converts mermaid indented text to MindElixir JSON tree
- Theme sync with viewer's current theme

## The Numbers

| Metric | Value |
|--------|-------|
| Total file size | ~1500 lines |
| External dependencies | 3 CDN (marked, mermaid, MindElixir) |
| Build step | None |
| Server requirements | Static file hosting |
| Publications served | 25+ |
| Interfaces served | 5 |
| Export formats | 2 (PDF, DOCX) |
| Themes | 4 |

## What This Proves

- **Zero infrastructure**: No Node.js, no Ruby, no CI/CD pipeline for documentation
- **Production parity**: Reproduces the key features of 183KB Jekyll layouts in a single file
- **URL compatibility**: `/docs/publications/<slug>/` structure matches production for dual publishing
- **Convention over configuration**: Front matter YAML is the contract — the viewer adapts to what it finds
- **Extensible by design**: New publications are just markdown files with front matter. Drop them in, they render.

</div>

[**Validated**]({{ '/publications/success-stories/story-26/' | relative_url }})

---
