---
layout: publication
title: "K_DOCS Web Viewer — Single-File Documentation Engine"
description: "A single index.html that renders markdown publications with 4 themes, PDF/DOCX export, three-panel navigation, live mindmap, and bilingual support — zero build step, zero server dependencies."
permalink: /publications/web-documentation-viewer/full/
lang: en
permalink_fr: /fr/publications/web-documentation-viewer/full/
header_title: "K_DOCS Web Viewer"
tagline: "Single-File Documentation Engine"
pub_id: "Publication #23 — Full"
pub_meta: "Publication #23 v1 | March 2026"
pub_version: "v1"
pub_number: 23
pub_date: "March 2026"
og_image: /assets/og/knowledge-2-en-cayman.gif
keywords: "documentation viewer, single-file, static, themes, export, panels, mindmap, bilingual"
---

# K_DOCS Web Viewer — Single-File Documentation Engine

> **Parent**: [Publication #23 — Summary]({{ '/publications/web-documentation-viewer/' | relative_url }})

---

<div class="story-section">

## 1. Design Philosophy

The K_DOCS Web Viewer exists because the production Knowledge system (`packetqc/knowledge`) uses Jekyll + GitHub Pages with two massive HTML layouts (183 KB total). That pipeline works but requires Ruby, a build step, and Jekyll-specific conventions.

K_DOCS needed documentation **without any of that** — raw markdown files served by GitHub Pages with `.nojekyll`, rendered entirely client-side. The constraint: everything must work from a single static file with zero server-side processing.

### The Single-File Constraint

One `index.html` file contains:
- All CSS (4 themes, print styles, responsive breakpoints)
- All JavaScript (markdown pipeline, export engine, panel management, mindmap integration)
- All HTML structure (three-panel layout, toolbar, chrome bars)

**Why single-file?** Deployment is a `git push`. No bundler, no transpiler, no CI/CD pipeline. The viewer IS the documentation platform.

## 2. Markdown Rendering Pipeline

```
URL parameter (?doc=path) → fetch .md → parse front matter → resolve Liquid →
marked.parse() → render mermaid → inject into DOM
```

### Front Matter Parsing

The viewer extracts YAML front matter (between `---` delimiters) and maps fields to the chrome bar, `<title>`, `og:image` meta tag, and export metadata.

Required fields: `title`, `description`, `permalink`
Optional fields: `pub_id`, `pub_meta`, `pub_version`, `pub_date`, `header_title`, `tagline`, `source_url`, `citation`, `og_image`, `permalink_fr`/`permalink_en`, `lang`, `keywords`

### Liquid Tag Resolution

The viewer resolves a subset of Jekyll Liquid syntax client-side:

| Tag | Resolution |
|-----|-----------|
| `{{ site.baseurl }}` | Auto-detected from `window.location.pathname` |
| `{{ page.url }}` | Current document permalink |
| `{{ '...' \| relative_url }}` | Prepends baseurl to path |

Both single-quoted and double-quoted Liquid syntax are supported. The resolver applies before markdown parsing.

### Kramdown IAL Support

Kramdown inline attribute lists (`{: #id}`, `{: .class}`) are stripped from the markdown source and applied as HTML attributes on the preceding element.

## 3. Four-Theme System

All themes are pure CSS custom properties — no JavaScript style manipulation:

| Theme | Background | Accent | Use Case |
|-------|-----------|--------|----------|
| Daltonism Light | `#faf6f1` warm | `#0055b3` | Default, accessible |
| Daltonism Dark | `#1a1a2e` warm | `#5599dd` | Dark + accessible |
| Cayman | `#eff6ff` cool | `#1d4ed8` | Blue light |
| Midnight | `#0f172a` cool | `#60a5fa` | Blue dark |

Theme selection persists via `localStorage` and applies **before DOM render** (inline script in `<head>`) to prevent flash of wrong theme.

The `prefers-color-scheme` media query auto-selects light/dark on first visit.

## 4. Three-Panel Layout

| Panel | Function | Content Source |
|-------|----------|---------------|
| Left | Main navigator — publication tree | `interfaces/main-navigator/index.md` |
| Center | Primary content viewer | Any markdown document |
| Right | Secondary content / interfaces | Interface pages (I1–I5) |

### Draggable Dividers

Panels are separated by vertical dividers (14px desktop, 8px mobile) with:
- **Drag mode**: `mousedown/mousemove/mouseup` with overlay to prevent iframe interference
- **Click-to-step**: Left divider cycles [0, 220, 320]px. Right divider cycles 0 → 50% → full → 0
- **Grip dots**: 5 vertically-centered dots as visual affordance
- **Responsive**: CSS media query `(max-width: 768px)` switches divider width

Grid uses `grid-template-columns` with pixel values. Transitions disabled during drag for smooth tracking.

## 5. Interface Routing

The routing system manages cross-panel navigation without full page reloads:

- **Interface links in right panel** → route to center panel via `window.name` detection
- **Main navigator links** → reload full page (different origin context)
- **External links** → always open in new browser tab
- **BroadcastChannel** propagates orientation changes between panels

The navigator uses `srcdoc` iframes with null origin, so cross-document access from navigator to panel content is not possible — routing uses `postMessage` instead.

## 6. Export Engine

### PDF — CSS Paged Media

Export uses `window.print()` with comprehensive `@media print` and `@page` CSS:

- **Corporate styling**: White background (#fff), black text (#111), blue accent (#1d4ed8)
- **Cover page**: Title, description, separator line, pub_meta, timestamp, authors — centered
- **TOC**: Page 2 with `page-break-after: always`
- **Running header**: Title with blue bottom liner (CSS `@top-center`)
- **Running footer**: Timestamp · version left, K_DOCS right, blue top liner
- **Page control**: A4 size, margins, orphans/widows, `break-inside: avoid` on tables

The first page (cover) has empty running headers/footers via `:first` page selector.

### DOCX — MSO Elements

DOCX export generates HTML with Microsoft Office-specific elements:

- **Calibri 10pt** body text
- **Same TOC-on-page-2** convention as PDF
- `rewriteContentLinks()` converts internal paths to viewer URL format (`index.html?doc=`)
- **Same cover page** structure as PDF
- Filename convention: `PUB_ID - Title - VER.docx`

## 7. Chrome Bar Convention

All panels use the same `buildChromeBar()` function:

**Non-collapsible part** (always visible):
- "Actual Page" permalink to production URL

**Collapsible part** (toggle arrow, collapsed by default):
- pub_id, title with version badge
- Tagline/description
- pub_meta, pub_date
- Source URL, generated timestamp, citation
- Authors (split by `&`, displayed on separate lines)

State persisted in `localStorage` per panel.

## 8. Live Mindmap Integration

MindElixir v5.9.3 renders the K_MIND knowledge graph directly in the viewer:

### Pipeline

```
mind_memory.md (GitHub raw) → depth_config.json → filterMindmap() →
mermaidToMindElixir() → MindElixir.init() → render
```

### Three Deployment Points

1. **Interface I5** — Standalone page with theme dropdown, Normal/Full toggle, Center/Fit/Fullscreen controls
2. **Knowledge 2.0 publication** — Inline embed with auto-theme detection
3. **Viewer webcard** — Preview card when `live_webcard: mindmap` is set in front matter

### Theme Sync

Four MindElixir themes map to viewer themes:

| Viewer Theme | MindElixir Palette | Background | Root Node |
|---|---|---|---|
| Cayman | Blue, light | `#eff6ff` | `#1d4ed8` |
| Midnight | Blue, dark | `#0f172a` | `#1e40af` |
| Daltonism Light | Warm, light | `#faf6f1` | `#0055b3` |
| Daltonism Dark | Warm, dark | `#1a1a2e` | `#2a4a7a` |

### Depth Filtering

JavaScript port of `mindmap_filter.py`:
- `default_depth: 3` — show 3 depth levels by default
- `omit: ["architecture", "constraints"]` — hide implementation details in normal mode
- `overrides: {"session/near memory": 4}` — per-branch depth control
- Longest-match-wins rule for override resolution

## 9. Bilingual Support

The viewer supports English and French content:

- **Language toggle**: EN/FR buttons in header
- **Dual permalinks**: `permalink` + `permalink_fr` (EN docs) or `permalink_en` (FR docs)
- **Dynamic labels**: "Contents" ↔ "Table des matières", etc.
- **URL parameter**: `?lang=fr` for French navigation
- **Full FR mirror**: `docs/fr/` directory mirrors `docs/` structure

## 10. Webcards & Social Sharing

- `og:image` meta tag injection on document load
- Theme-aware webcard display (cayman variant for light, midnight for dark)
- `prefers-color-scheme` media query for auto-detection
- Live mindmap webcard via MindElixir when `live_webcard: mindmap` is set
- Graceful fallback with `onerror` handler for missing images

## The Numbers

| Metric | Value |
|--------|-------|
| Total file size | ~1500 lines |
| External dependencies | 3 CDN (marked, mermaid, MindElixir) |
| Build step | None |
| Server requirement | Static file hosting |
| Publications served | 25+ |
| Interfaces served | 5 |
| Export formats | 2 (PDF, DOCX) |
| Themes | 4 |
| Languages | 2 (EN, FR) |

</div>

---

*Martin Paquet & Claude (Opus 4.6) | [packetqc/K_DOCS](https://github.com/packetqc/K_DOCS)*
