# Publication #17 — Web Production Pipeline

**From Source Markdown to Live GitHub Pages**

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
*Version: v1 — February 2026*

---

## Abstract

Every web page in the Knowledge system follows a deterministic production pipeline: source markdown is authored once, structured into a three-tier publication system (source → summary → complete), processed by Jekyll's kramdown engine with Liquid templating, wrapped in theme-aware layouts, and deployed automatically to GitHub Pages. This publication documents the complete pipeline — from the first line of markdown to a live, bilingual, dual-theme, exportable web page.

The pipeline is not a build script. It is an architecture — a set of conventions, structured files, processing rules, and exclusion mechanisms that together produce consistent, maintainable web output from plain markdown input. Understanding the pipeline is essential for anyone creating, debugging, or extending Knowledge publications.

**Parent publication**: [#0 — Knowledge System](https://packetqc.github.io/knowledge/publications/knowledge-system/)

**Related publications**:

| # | Publication | Relationship |
|---|-------------|-------------|
| 13 | [Web Pagination & Export](https://packetqc.github.io/knowledge/publications/web-pagination-export/) | Export stage — PDF/DOCX generation from the pipeline's HTML output |
| 14 | [Architecture Analysis](https://packetqc.github.io/knowledge/publications/architecture-analysis/) | System context — publication pipeline as architectural component |
| 15 | [Architecture Diagrams](https://packetqc.github.io/knowledge/publications/architecture-diagrams/) | Visual — Diagram 6 shows the publication pipeline flow |
| 16 | [Web Page Visualization](https://packetqc.github.io/knowledge/publications/web-page-visualization/) | Post-pipeline — local rendering and diagnostics after generation |
| 5 | [Webcards & Social Sharing](https://packetqc.github.io/knowledge/publications/webcards-social-sharing/) | Asset pipeline — animated OG social preview generation |
| 6 | [Normalize & Structure Concordance](https://packetqc.github.io/knowledge/publications/normalize-structure-concordance/) | Quality gate — concordance validation across the pipeline |

---

## Table of Contents

| | |
|---|---|
| [Pipeline Overview](#pipeline-overview) | End-to-end flow from source to live page |
| [Source Authoring](#1-source-authoring) | Writing the canonical markdown document |
| [Three-Tier Structure](#2-three-tier-publication-structure) | Source → Summary → Complete |
| [Bilingual Mirror System](#3-bilingual-mirror-system) | EN/FR parallel page architecture |
| [Front Matter Contract](#4-front-matter-contract) | Required YAML metadata for every page |
| [Jekyll Processing](#5-jekyll-processing) | Liquid → kramdown → HTML transformation |
| [Layout System](#6-layout-system) | publication.html vs default.html feature split |
| [Theme System](#7-theme-system) | 4-theme CSS with browser auto-detection |
| [Asset Pipeline](#8-asset-pipeline) | Webcards, diagrams, images, media |
| [Exclusion Mechanisms](#9-exclusion-mechanisms) | What gets filtered, hidden, or transformed |
| [Deployment](#10-deployment) | GitHub Pages auto-build from docs/ |
| [Pipeline Commands](#11-pipeline-commands) | pub, docs, webcard, normalize tooling |
| [Known Gotchas](#12-known-gotchas) | kramdown quirks, proxy limits, rendering traps |
| [Pipeline Diagram](#pipeline-diagram) | Visual flow of the complete pipeline |

---

## Pipeline Overview

```
Source markdown (author writes once)
    ↓
Three-tier split (source → summary → complete)
    ↓
Bilingual mirrors (EN + FR for each web tier)
    ↓
Front matter injection (YAML metadata)
    ↓
Jekyll processing (Liquid templates → kramdown → HTML)
    ↓
Layout wrapping (publication.html or default.html)
    ↓
Theme CSS application (Cayman/Midnight/Daltonism × browser preference)
    ↓
Client-side enhancements (Mermaid rendering, cross-references, export toolbar)
    ↓
GitHub Pages deployment (automatic from docs/ on default branch)
    ↓
Live web page (dual-theme, bilingual, exportable)
```

**Key principle**: The source document is written once. Everything downstream is derived. The pipeline is deterministic — the same source always produces the same output.

---

## 1. Source Authoring

Every publication starts as a single markdown file:

```
publications/<slug>/v1/README.md
```

This is the **canonical source** — the single source of truth. All web pages are derived from it. The source is English-only (French translations are created during the three-tier split).

**Source structure**:

```
publications/<slug>/v1/
  README.md              ← canonical document
  assets/                ← static assets (diagrams, images, drawings)
  media/                 ← dynamic assets (video, animated captures)
```

**Authoring rules**:
- Standard GitHub-Flavored Markdown (GFM)
- Mermaid diagrams in fenced code blocks (` ```mermaid `)
- Tables, headings, links, images — all standard markdown
- No Liquid tags in source (source is platform-independent)
- No front matter in source (front matter is added in the web tiers)
- Internal links use relative paths within the document

The source file is readable on GitHub directly (GitHub renders markdown natively). It is also the input for `pub sync` which propagates changes to web tiers.

---

## 2. Three-Tier Publication Structure

Each publication exists at three levels, serving different audiences and contexts:

| Tier | Location | Purpose | Content |
|------|----------|---------|---------|
| **Source** | `publications/<slug>/v1/README.md` | Canonical document, versioned | Full content, English only |
| **Summary** | `docs/publications/<slug>/index.md` | Web entry point, quick overview | Abstract, key highlights, link to complete |
| **Complete** | `docs/publications/<slug>/full/index.md` | Full web documentation | Complete content rendered on GitHub Pages |

**File tree for one publication** (bilingual):

```
publications/<slug>/v1/
  README.md                                    ← Source (EN only)

docs/publications/<slug>/
  index.md                                     ← EN Summary
  full/
    index.md                                   ← EN Complete

docs/fr/publications/<slug>/
  index.md                                     ← FR Summary
  full/
    index.md                                   ← FR Complete
```

**Total: 5 files per publication** (1 source + 4 web pages).

**Cross-linking rules**:
- Summary pages link to their same-language complete page
- Complete pages link back to their summary
- EN pages link to FR mirrors and vice versa
- All internal links use Jekyll's `relative_url` filter

**Why three tiers?**
- **Source** stays clean, versioned, platform-independent — readable on GitHub without Jekyll
- **Summary** serves as landing page — social sharing previews land here
- **Complete** serves deep readers — full documentation with all diagrams and tables

---

## 3. Bilingual Mirror System

Every web page (summary and complete) exists in two languages. The EN and FR pages are structural mirrors — same sections, same order, same assets, different language.

**Path convention**:

| Language | Path pattern | Example |
|----------|-------------|---------|
| English | `docs/publications/<slug>/` | `docs/publications/harvest-protocol/index.md` |
| French | `docs/fr/publications/<slug>/` | `docs/fr/publications/harvest-protocol/index.md` |

**What differs between mirrors**:
- `title` and `description` in front matter (translated)
- `permalink` — FR adds `/fr/` prefix
- `og_image` — FR uses `-fr-` webcard variant
- Body text (translated)
- Language bar direction (EN-primary vs FR-primary)

**What stays identical**:
- `layout`, `pub_id`, `version`, `date`
- Document structure (same headings, same order)
- Mermaid diagram syntax (language-neutral)
- Asset references (shared unless language-specific)
- Table structures

**Language bar** — auto-generated by the `publication.html` layout from the `permalink` field. No front matter flag needed. EN pages detect the absence of `/fr/` and show English-primary bar. FR pages detect `/fr/` and show French-primary bar.

---

## 4. Front Matter Contract

Every web page in `docs/` must include YAML front matter between `---` delimiters. This is the contract between the author and the pipeline.

**Required fields** (all pages):

```yaml
---
layout: publication          # or default
title: "Page Title"
description: "Meta description for OG/SEO"
permalink: /publications/<slug>/
og_image: /assets/og/<card>-en-cayman.gif
---
```

**Additional fields** (publication pages):

```yaml
pub_id: "Publication #17"
version: "v1"
date: "2026-02-26"
keywords: "pipeline, jekyll, kramdown, production"
```

**What the layout extracts from front matter**:

| Field | Used for |
|-------|----------|
| `layout` | Which layout template wraps the content |
| `title` | `<title>` tag, OG title, version banner, PDF filename |
| `description` | `<meta name="description">`, OG description |
| `permalink` | URL path, language bar generation, canonical URL |
| `og_image` | Webcard header, `og:image` meta tag, `twitter:image` |
| `pub_id` | Version banner display |
| `version` | Version banner, PDF filename |
| `date` | Version banner, freshness tracking |
| `keywords` | Cross-reference injection (keyword→publication links) |

**Auto-generated by layout** (not in front matter):
- Generated timestamp (client-side JavaScript `new Date()`)
- Author list (hardcoded in layout)
- Language bar (computed from permalink)
- Theme CSS variables (computed from browser preference)

---

## 5. Jekyll Processing

GitHub Pages uses Jekyll to transform markdown into HTML. The processing happens in three ordered passes:

### Pass 1: Liquid Template Processing

Jekyll's Liquid engine runs first, before any markdown processing.

**What Liquid handles**:
- `{{ variable }}` — variable interpolation
- `{% if condition %}` — conditional blocks
- `{{ '/path/' | relative_url }}` — URL filters (adds baseurl `/knowledge/`)
- Layout inheritance and content injection

**Critical rule**: Liquid processes ALL `{{ }}` patterns — including those inside markdown code fences. This means Mermaid diagrams with `{{` notation (e.g., hexagon shapes) get their content **stripped** by Liquid before kramdown ever sees them. This is a known gotcha (see [Known Gotchas](#12-known-gotchas)).

### Pass 2: kramdown Markdown → HTML

After Liquid, kramdown converts markdown to HTML using GFM (GitHub-Flavored Markdown) dialect.

**Jekyll configuration** (`docs/_config.yml`):

```yaml
markdown: kramdown
kramdown:
  input: GFM
  parse_block_html: true
```

**What kramdown handles**:
- Headings, paragraphs, lists, blockquotes
- Tables (GFM pipe syntax)
- Fenced code blocks (` ``` `)
- Inline code, bold, italic, links, images
- HTML pass-through (with `parse_block_html: true`)

**HTML block parsing** — `parse_block_html: true` means kramdown allows raw HTML blocks to pass through unchanged. This is essential for `<picture>`, `<source>`, `<div>` elements used in the pipeline. However, kramdown's HTML block parser has specific rules about when it exits HTML mode (see [Known Gotchas](#12-known-gotchas)).

### Pass 3: Layout Template Wrapping

The resulting HTML is injected into the layout template specified by `layout:` in front matter. The layout provides:
- `<html>`, `<head>`, `<body>` wrapper
- CSS (themes, typography, tables, code blocks)
- JavaScript (Mermaid rendering, cross-references, export, theme switcher)
- OG meta tags
- Webcard header
- Version banner (publication layout)
- Language bar (publication layout)
- Export toolbar (publication layout)

---

## 6. Layout System

Two layouts serve different page types:

### publication.html — Full Publication Stack

Used for all publications and technical documentation.

**Features**:

| Feature | Description |
|---------|-------------|
| Version banner | `pub_id` + `version` + `date` + generated timestamp + authors |
| Language bar | Auto-generated EN↔FR toggle from permalink |
| Export toolbar | PDF (Letter/Legal) + DOCX buttons |
| `printAs()` function | Browser-native PDF via `window.print()` + CSS Paged Media |
| CSS Paged Media `@page` | Running headers, three-column footers, cover page |
| MSO elements | DOCX running header/footer |
| Mermaid rendering | CDN-loaded mermaid.js, `renderMermaid()` function |
| Cross-references | Keyword→publication link injection at page bottom |
| Webcard header | Animated OG GIF with dual-theme `<picture>` |
| 4-theme CSS | Cayman, Midnight, Daltonism Light, Daltonism Dark |

### default.html — Profile and Landing Pages

Used for profile pages, landing pages, project hubs, publication index.

**Features**:

| Feature | Included? |
|---------|-----------|
| Webcard header | Yes |
| OG meta tags | Yes |
| 4-theme CSS | Yes |
| Mermaid rendering | Yes |
| Export toolbar | **No** |
| Version banner | **No** |
| Language bar | **No** |
| CSS Paged Media | **No** |
| Cross-references | **No** |

**Layout selection rule**: If the page is a publication (summary or complete), use `publication`. If it's a profile, hub, index, or landing page, use `default`.

---

## 7. Theme System

The pipeline produces pages that adapt to 4 visual themes:

| Theme | Mode | Background | Text | Accents |
|-------|------|-----------|------|---------|
| **Cayman** | Light | Teal/emerald gradient | Dark slate | Teal, cyan, emerald |
| **Midnight** | Dark | Navy/indigo gradient | Light slate | Blue, purple, cyan |
| **Daltonism Light** | Light (accessible) | Neutral | Dark | Blue + orange |
| **Daltonism Dark** | Dark (accessible) | Neutral dark | Light | Blue + orange |

**Selection mechanism**:
1. **Browser preference** (automatic): `@media (prefers-color-scheme: dark)` switches to Midnight
2. **Theme selector** (manual): Dropdown in page header sets `html[data-theme]` attribute
3. **CSS variables**: `:root` defines theme colors, overridden by `[data-theme]` and `@media`

**Webcard theme matching**: The `<picture>` element in the webcard header uses `<source media="(prefers-color-scheme: dark)">` to serve the matching webcard GIF variant.

**Social sharing**: OG image (`og:image` meta tag) always uses the Cayman (light) variant — social platforms don't support theme-responsive images.

---

## 8. Asset Pipeline

### Webcards (OG Social Previews)

Every web page has a unique animated OG GIF:

```
docs/assets/og/<card>-<lang>-<theme>.gif
```

- 1200×630 pixels, 256-color, animated, infinite loop
- 4 variants per page: EN Cayman, EN Midnight, FR Cayman, FR Midnight
- Generated by `scripts/generate_og_gifs.py`
- Referenced in front matter as `og_image`

### Pre-Rendered Diagrams

When Mermaid diagrams need dual-theme or reliable rendering:

```
docs/assets/diagrams/<pub-slug>/diagram-NN-<lang>-<theme>.png
```

- Rendered locally using Playwright + Chromium + npm mermaid (Publication #16)
- Embedded via `<picture>` elements with theme-responsive `<source>`
- Source mermaid preserved in publication source files

### Publication Assets (Forecasted)

```
publications/<slug>/v1/assets/    ← source (images, diagrams)
publications/<slug>/v1/media/     ← source (video, captures)
docs/publications/<slug>/assets/  ← synced copy (accessible by web)
```

`pub sync` copies assets from source to docs. One-way sync — source is truth.

---

## 9. Exclusion Mechanisms

Not everything in the markdown source appears on the live web page. The pipeline has multiple exclusion layers:

### CSS Exclusions (display: none)

| Selector | What it hides | Why |
|----------|---------------|-----|
| `.mermaid-source` | `<details>` blocks with Mermaid source code | Source preservation — visible in git, hidden on web |
| `@media print` rules | Export toolbar, language bar, webcard header, navigation | Clean PDF/DOCX output |

### JavaScript Exclusions

| Check | What it skips | Why |
|-------|---------------|-----|
| `el.closest('.mermaid-source')` | Mermaid blocks inside hidden source containers | Prevents double-rendering |
| Element cleanup before DOCX | Toolbar, lang bar, cross-refs, webcards | Clean export content |

### kramdown Processing Exclusions

kramdown transforms or excludes certain patterns during markdown→HTML conversion:

| Pattern | Behavior | Impact |
|---------|----------|--------|
| `{{ }}` inside code fences | Liquid strips content before kramdown | Mermaid hexagons lose their labels |
| `</summary>` inside `<details>` with blank lines | HTML-escaped to `&lt;/summary&gt;` | Cascading nesting breaks page rendering |
| Raw HTML after blank line in HTML block | kramdown exits HTML mode, re-enters markdown | Closing tags become text |

### Content-Level Exclusions

| What | Excluded from | Present in |
|------|---------------|------------|
| Mermaid source blocks | Web rendering, PDF, DOCX | Git source, AI reading |
| Navigation elements | PDF, DOCX | Web rendering |
| Theme selector | PDF, DOCX | Web rendering |
| Webcard header | PDF, DOCX | Web rendering |
| Cross-reference section | PDF, DOCX | Web rendering |

---

## 10. Deployment

### GitHub Pages Configuration

```yaml
# docs/_config.yml
url: "https://packetqc.github.io"
baseurl: "/knowledge"
```

GitHub Pages is configured to build from the `docs/` folder on the default branch (`main`).

### Deployment Flow

```
Author commits to default branch (via PR merge)
    ↓
GitHub Pages detects change in docs/
    ↓
Jekyll builds static HTML from markdown + layouts
    ↓
Static files deployed to packetqc.github.io/knowledge/
    ↓
CDN caches updated (~1-5 minutes)
    ↓
Live page accessible at permalink URL
```

**Deployment is automatic** — no manual build step. Every merge to the default branch triggers a rebuild. The `docs/` folder is the deployment root — only files under `docs/` are published.

### URL Structure

```
https://packetqc.github.io/knowledge/publications/<slug>/          ← EN Summary
https://packetqc.github.io/knowledge/publications/<slug>/full/     ← EN Complete
https://packetqc.github.io/knowledge/fr/publications/<slug>/       ← FR Summary
https://packetqc.github.io/knowledge/fr/publications/<slug>/full/  ← FR Complete
```

The `relative_url` filter ensures all internal links work correctly with the `/knowledge/` baseurl prefix.

---

## 11. Pipeline Commands

The Knowledge system provides commands to manage the pipeline:

### Publication Lifecycle

| Command | Pipeline stage | Action |
|---------|---------------|--------|
| `pub new <slug>` | Scaffolding | Create 5 files + update indexes |
| `pub sync <#>` | Synchronization | Compare source vs web, sync assets |
| `pub check <#>` | Validation | Verify structure, front matter, links, mirrors |
| `pub check --all` | Validation | Validate all publications |
| `pub list` | Inventory | Show all publications with status |
| `pub export <#> --pdf` | Export | Generate PDF via CSS Paged Media |
| `pub export <#> --docx` | Export | Generate DOCX via HTML-to-Word |

### Content Quality

| Command | Pipeline stage | Action |
|---------|---------------|--------|
| `doc review <#>` | Freshness | Check content against current knowledge state |
| `doc review --list` | Freshness | Quick version drift inventory |
| `docs check <path>` | Page validation | Front matter, links, mirror, OG image |
| `docs check --all` | Page validation | Validate all doc pages |

### Asset Generation

| Command | Pipeline stage | Action |
|---------|---------------|--------|
| `webcard <target>` | Asset generation | Generate animated OG GIFs |
| `webcard --apply` | Asset deployment | Generate all + commit + push |

### Structure Enforcement

| Command | Pipeline stage | Action |
|---------|---------------|--------|
| `normalize` | Concordance audit | Check EN/FR mirrors, front matter, links, assets |
| `normalize --fix` | Concordance repair | Auto-fix structural issues |

---

## 12. Known Gotchas

Lessons learned from operating the pipeline. Each gotcha documents a real failure encountered in production.

### Liquid Strips Mermaid Hexagons

**Problem**: Mermaid's hexagon syntax `{{label}}` uses double curly braces — the same syntax Liquid uses for variable interpolation. Jekyll processes Liquid before kramdown, so `{{label}}` is interpreted as a Liquid variable (which doesn't exist) and silently replaced with empty string.

**Symptom**: Hexagon shapes in Mermaid diagrams render without their labels.

**Fix**: Pre-render Mermaid diagrams to PNG using the local rendering pipeline (Publication #16), which bypasses Jekyll's Liquid processing entirely.

### kramdown Escapes Closing Tags in Details Blocks

**Problem**: When `<details>` blocks contain markdown code fences with blank lines between the `</summary>` tag and the code fence, kramdown exits HTML block mode on the blank line. It then treats `</summary>` and `</details>` as text, HTML-escaping them to `&lt;/summary&gt;` and `&lt;/details&gt;`.

**Symptom**: The `<summary>` element never closes. All subsequent page content is swallowed inside nested, collapsed `<summary>` elements. The page appears to stop rendering after the first `<details>` block.

**Impact**: This broke all four Publication #15 (Architecture Diagrams) pages — only Section 1 was visible. Content for Sections 2-14 was trapped inside invisible collapsed elements.

**Fix**: Remove `<details>` blocks from web pages entirely, or ensure they contain only inline HTML (no markdown code fences, no blank lines). For Mermaid source preservation, keep the source in publication source files and git, not in the web pages.

**Root cause**: kramdown's `parse_block_html` mode has strict rules about when it enters and exits HTML block parsing. A blank line signals the end of an HTML block, causing kramdown to revert to markdown mode for subsequent lines — even if they're inside an unclosed HTML element.

### CDN Resources May Not Load

**Problem**: The container proxy may block or intercept external CDN requests (CSS, JavaScript libraries). This affects client-side rendering of Mermaid diagrams and external fonts.

**Symptom**: Mermaid diagrams show as raw code blocks. Fonts fall back to system defaults.

**Fix**: The layouts include inline fallback CSS. Mermaid is loaded from CDN with a fallback message. For critical diagrams, pre-render to PNG.

### baseurl Breaks Without relative_url

**Problem**: The Jekyll site has `baseurl: "/knowledge"`. Any internal link that doesn't use the `relative_url` filter will resolve to the wrong URL.

**Example**: `/publications/foo/` resolves to `packetqc.github.io/publications/foo/` (missing `/knowledge/`). The correct form is `{{ '/publications/foo/' | relative_url }}` which resolves to `/knowledge/publications/foo/`.

**Fix**: Every internal link must use `relative_url`. `normalize` checks for hardcoded paths and flags them.

### print CSS Hides Essential Elements

**Problem**: `@media print` CSS rules hide navigation, toolbar, webcard, and language bar. If export-specific CSS is too aggressive, it may also hide content.

**Fix**: Export cleanup functions carefully select which elements to hide. The `printAs()` function manages the print lifecycle (inject `@page` size → print → restore). Elements that should appear in PDF but not on screen use `@media print { display: block }`.

---

## Pipeline Diagram

The complete production pipeline as a visual flow:

```
┌─────────────────────────────────────────────────────────┐
│                    SOURCE AUTHORING                      │
│  publications/<slug>/v1/README.md (canonical, EN only)   │
│  + assets/ + media/                                      │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│               THREE-TIER SPLIT (pub new)                 │
│                                                          │
│  docs/publications/<slug>/index.md      ← EN Summary     │
│  docs/publications/<slug>/full/index.md ← EN Complete    │
│  docs/fr/publications/<slug>/index.md   ← FR Summary     │
│  docs/fr/publications/<slug>/full/index.md ← FR Complete │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  FRONT MATTER INJECTION                   │
│  layout, title, description, permalink, og_image,        │
│  pub_id, version, date, keywords                         │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│              JEKYLL PROCESSING (3 passes)                 │
│                                                          │
│  Pass 1: Liquid templates ({{ }}, {% %}, filters)        │
│  Pass 2: kramdown (markdown → HTML, GFM dialect)         │
│  Pass 3: Layout wrapping (publication.html / default.html)│
│                                                          │
│  ⚠ EXCLUSIONS:                                           │
│  - Liquid strips {{ }} from Mermaid hexagons              │
│  - kramdown escapes </tags> inside <details> blocks      │
│  - CSS hides .mermaid-source blocks                       │
│  - JS skips mermaid rendering in .mermaid-source          │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│                   ASSET PIPELINE                         │
│                                                          │
│  Webcards: scripts/generate_og_gifs.py → assets/og/      │
│  Diagrams: Playwright + Chromium → assets/diagrams/       │
│  Source assets: pub sync → docs/<slug>/assets/            │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│              CLIENT-SIDE ENHANCEMENTS                     │
│                                                          │
│  Mermaid.js: renders ```mermaid blocks to SVG             │
│  Theme switcher: Cayman/Midnight/Daltonism selection     │
│  Cross-references: keyword → publication link injection   │
│  Export toolbar: PDF (printAs) + DOCX buttons            │
│  Language bar: EN↔FR toggle from permalink               │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│            GITHUB PAGES DEPLOYMENT                       │
│                                                          │
│  Merge to default branch → Jekyll builds docs/ →         │
│  Static HTML at packetqc.github.io/knowledge/            │
│  Auto-deploy ~1-5 minutes after merge                    │
└─────────────────────────────────────────────────────────┘
```

---

## Summary

The web production pipeline transforms plain markdown into rich, bilingual, theme-aware, exportable web pages through a deterministic chain: source → three-tier split → front matter → Jekyll processing → layout wrapping → client-side enhancement → deployment.

The pipeline's strength is its convention-driven nature. Every file goes in a predictable place, every page follows the same front matter contract, every layout provides the same feature set. The `pub` commands manage the lifecycle; `normalize` enforces concordance; `docs check` validates output.

The pipeline's weakness is Jekyll's processing order — Liquid runs before kramdown, creating edge cases where markdown content is modified before the markdown engine sees it. The known gotchas (Liquid stripping Mermaid syntax, kramdown escaping HTML tags in details blocks) are architectural constraints of the processing chain, not bugs. Understanding these constraints is key to avoiding rendering failures.

Publication #16 (Web Page Visualization) covers what happens **after** this pipeline produces HTML — local rendering, screenshots, and diagnostics. Publication #13 (Web Pagination & Export) covers the **export stage** — transforming the pipeline's HTML into PDF and DOCX. Together, these three publications (#13, #16, #17) document the complete journey from markdown to printed document.

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
