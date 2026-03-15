---
layout: publication
title: "Web Production Pipeline — Full"
description: "Complete reference for the Knowledge web production pipeline: source authoring, three-tier structure, bilingual mirrors, front matter contract, Jekyll processing (Liquid + kramdown), layout system, 4-theme CSS, asset pipeline, exclusion mechanisms, deployment, pipeline commands, and known gotchas."
pub_id: "Publication #17 — Full"
version: "v1"
date: "2026-02-26"
permalink: /publications/web-production-pipeline/full/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "pipeline, jekyll, kramdown, production, web, deployment, exclusion"
---

# Web Production Pipeline — Complete Documentation
{: #pub-title}

> **Summary**: [Publication #17]({{ '/publications/web-production-pipeline/' | relative_url }}) | **Parent**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }})

**Contents**

| | |
|---|---|
| [Pipeline Overview](#pipeline-overview) | End-to-end flow from source to live page |
| [1. Source Authoring](#1-source-authoring) | Writing the canonical markdown document |
| [2. Three-Tier Structure](#2-three-tier-publication-structure) | Source → Summary → Complete |
| [3. Bilingual Mirrors](#3-bilingual-mirror-system) | EN/FR parallel page architecture |
| [4. Front Matter Contract](#4-front-matter-contract) | Required YAML metadata for every page |
| [5. Jekyll Processing](#5-jekyll-processing) | Liquid → kramdown → HTML transformation |
| [6. Layout System](#6-layout-system) | publication.html vs default.html feature split |
| [7. Theme System](#7-theme-system) | 4-theme CSS with browser auto-detection |
| [8. Asset Pipeline](#8-asset-pipeline) | Webcards, diagrams, images, media |
| [9. Exclusion Mechanisms](#9-exclusion-mechanisms) | What gets filtered, hidden, or transformed |
| [10. Deployment](#10-deployment) | GitHub Pages auto-build from docs/ |
| [11. Pipeline Commands](#11-pipeline-commands) | pub, docs, webcard, normalize tooling |
| [12. Known Gotchas](#12-known-gotchas) | kramdown quirks, proxy limits, rendering traps |
| [Pipeline Diagram](#pipeline-diagram) | Visual flow of the complete pipeline |

---

## Pipeline Overview

```
Source markdown (author writes once)
    ↓ pub new (scaffold)
Three-tier split (source → summary → complete)
    ↓ front matter injection
Bilingual mirrors (EN + FR for each web tier)
    ↓ Jekyll processing
Liquid templates → kramdown → HTML
    ↓ layout wrapping
publication.html or default.html
    ↓ client-side enhancements
Mermaid, themes, cross-refs, export
    ↓ GitHub Pages deployment
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
  assets/                ← static assets (diagrams, images)
  media/                 ← dynamic assets (video, captures)
```

**Authoring rules**:
- Standard GitHub-Flavored Markdown (GFM)
- Mermaid diagrams in fenced code blocks
- No Liquid tags in source (source is platform-independent)
- No front matter in source (front matter is added in the web tiers)
- Internal links use relative paths within the document

The source file is readable on GitHub directly (GitHub renders markdown natively). It is also the input for `pub sync` which propagates changes to web tiers.

---

## 2. Three-Tier Publication Structure

Each publication exists at three levels, serving different audiences:

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

| Language | Path pattern |
|----------|-------------|
| English | `docs/publications/<slug>/` |
| French | `docs/fr/publications/<slug>/` |

**What differs between mirrors**:

| Element | EN | FR |
|---------|----|----|
| `title` | English title | French title |
| `description` | English description | French description |
| `permalink` | `/publications/<slug>/` | `/fr/publications/<slug>/` |
| `og_image` | `<card>-en-cayman.gif` | `<card>-fr-cayman.gif` |
| Body text | English | French |
| Language bar | English-primary | French-primary |

**What stays identical**: `layout`, `pub_id`, `version`, `date`, document structure, Mermaid diagrams, table structures, asset references (unless language-specific).

**Language bar** — auto-generated by the `publication.html` layout from the `permalink` field:
- If permalink contains `/fr/` → French-primary bar with English link
- If permalink does not contain `/fr/` → English-primary bar with French link
- Uses `relative_url` filter for mirror link generation

---

## 4. Front Matter Contract

Every web page in `docs/` must include YAML front matter. This is the contract between the author and the pipeline.

**Required fields** (all pages):

| Field | Purpose | Example |
|-------|---------|---------|
| `layout` | Layout template | `publication` or `default` |
| `title` | Page title, OG title | `"Web Production Pipeline"` |
| `description` | Meta description, OG description | `"Complete production pipeline..."` |
| `permalink` | URL path, language bar | `/publications/web-production-pipeline/` |
| `og_image` | Webcard, social preview | `/assets/og/knowledge-system-en-cayman.gif` |

**Additional fields** (publication pages):

| Field | Purpose | Example |
|-------|---------|---------|
| `pub_id` | Version banner display | `"Publication #17"` |
| `version` | Version banner, PDF filename | `"v1"` |
| `date` | Version banner, freshness | `"2026-02-26"` |
| `keywords` | Cross-reference injection | `"pipeline, jekyll, kramdown"` |

**Auto-generated by layout** (not in front matter):
- Generated timestamp (client-side JavaScript `new Date()`)
- Author list (hardcoded in layout)
- Language bar (computed from permalink)
- Theme CSS variables (computed from browser preference)

---

## 5. Jekyll Processing

GitHub Pages uses Jekyll to transform markdown into HTML. The processing happens in three ordered passes.

### Pass 1: Liquid Template Processing

Jekyll's Liquid engine runs **first**, before any markdown processing.

**What Liquid handles**:
{% raw %}
- `{{ variable }}` — variable interpolation
- `{% if condition %}` — conditional blocks
- `{{ '/path/' | relative_url }}` — URL filters (adds baseurl `/knowledge/`)
- Layout inheritance and content injection

**Critical rule**: Liquid processes ALL `{{ }}` patterns — including those inside markdown code fences. Mermaid diagrams with `{{` notation (hexagon shapes) get their content **stripped** by Liquid before kramdown ever sees them.
{% endraw %}

### Pass 2: kramdown Markdown → HTML

After Liquid, kramdown converts markdown to HTML using GFM dialect.

**Configuration** (`docs/_config.yml`):

| Setting | Value | Effect |
|---------|-------|--------|
| `markdown` | `kramdown` | Markdown engine selection |
| `kramdown.input` | `GFM` | GitHub-Flavored Markdown dialect |
| `kramdown.parse_block_html` | `true` | Raw HTML blocks pass through |

`parse_block_html: true` is essential for `<picture>`, `<source>`, `<div>`, and other HTML elements used in the pipeline. However, kramdown's HTML block parser has specific rules about when it exits HTML mode — blank lines inside HTML blocks cause kramdown to revert to markdown mode.

### Pass 3: Layout Template Wrapping

The resulting HTML is injected into the layout specified by `layout:` in front matter. The layout provides the complete HTML document structure: `<html>`, `<head>`, `<body>`, CSS, JavaScript, OG meta tags, and all interactive features.

---

## 6. Layout System

Two layouts serve different page types.

### publication.html — Full Publication Stack

| Feature | Description |
|---------|-------------|
| Version banner | `pub_id` + `version` + `date` + generated timestamp + authors |
| Language bar | Auto-generated EN↔FR toggle from permalink |
| Export toolbar | PDF (Letter/Legal) + DOCX buttons |
| `printAs()` | Browser-native PDF via `window.print()` + CSS Paged Media |
| CSS `@page` | Running headers, three-column footers, cover page |
| MSO elements | DOCX running header/footer |
| Mermaid rendering | CDN-loaded mermaid.js |
| Cross-references | Keyword→publication link injection at page bottom |
| Webcard header | Animated OG GIF with dual-theme `<picture>` |
| 4-theme CSS | Cayman, Midnight, Daltonism Light, Daltonism Dark |

### default.html — Profile and Landing Pages

| Feature | publication.html | default.html |
|---------|-----------------|-------------|
| Webcard header | Yes | Yes |
| OG meta tags | Yes | Yes |
| 4-theme CSS | Yes | Yes |
| Mermaid rendering | Yes | Yes |
| Export toolbar | Yes | **No** |
| Version banner | Yes | **No** |
| Language bar | Yes | **No** |
| CSS Paged Media | Yes | **No** |
| Cross-references | Yes | **No** |

**Selection rule**: Publications use `publication`. Profile, hub, index, and landing pages use `default`.

---

## 7. Theme System

Pages adapt to 4 visual themes:

| Theme | Mode | Background | Accents |
|-------|------|-----------|---------|
| **Cayman** | Light | Teal/emerald gradient | Teal, cyan, emerald |
| **Midnight** | Dark | Navy/indigo gradient | Blue, purple, cyan |
| **Daltonism Light** | Light | Neutral | Blue + orange |
| **Daltonism Dark** | Dark | Neutral dark | Blue + orange |

**Selection**: Browser `prefers-color-scheme` (automatic) → theme selector dropdown (manual override) → CSS variables in `:root`.

**Webcard matching**: `<picture>` element serves matching webcard GIF via `<source media="(prefers-color-scheme: dark)">`.

**Social sharing**: `og:image` always uses Cayman (light) — social platforms don't support theme-responsive images.

---

## 8. Asset Pipeline

### Webcards (OG Social Previews)

```
docs/assets/og/<card>-<lang>-<theme>.gif
```

- 1200×630 pixels, 256-color, animated GIF
- 4 variants per page: EN/FR × Cayman/Midnight
- Generated by `scripts/generate_og_gifs.py`
- Referenced in front matter as `og_image`

### Pre-Rendered Diagrams

```
docs/assets/diagrams/<pub-slug>/diagram-NN-<lang>-<theme>.png
```

- Rendered locally via Playwright + Chromium + npm mermaid (#16)
- Embedded via `<picture>` elements with theme-responsive `<source>`
- Source Mermaid preserved in publication source files

### Publication Assets

```
publications/<slug>/v1/assets/    ← source (images, diagrams)
publications/<slug>/v1/media/     ← source (video, captures)
docs/publications/<slug>/assets/  ← synced copy (web-accessible)
```

`pub sync` copies assets source → docs (one-way, source is truth).

---

## 9. Exclusion Mechanisms

The pipeline has multiple layers that filter, hide, or transform content between source and rendered output.

### CSS Exclusions

| Selector | What it hides | Context |
|----------|---------------|---------|
| `.mermaid-source` | Mermaid source `<details>` blocks | Web rendering |
| `@media print` | Toolbar, lang bar, webcard, nav | PDF export |

### JavaScript Exclusions

| Check | What it skips | Context |
|-------|---------------|---------|
| `el.closest('.mermaid-source')` | Mermaid blocks in hidden containers | Prevents double-rendering |
| DOCX cleanup | Toolbar, lang bar, cross-refs, webcards | Clean DOCX export |

### kramdown Processing Exclusions

| Pattern | Behavior | Impact |
|---------|----------|--------|
| {% raw %}`{{ }}`{% endraw %} inside code fences | Liquid strips content | Mermaid hexagons lose labels |
| `</summary>` inside `<details>` with blank lines | HTML-escaped to `&lt;/summary&gt;` | Cascading nesting breaks page |
| Raw HTML after blank line in HTML block | kramdown exits HTML mode | Closing tags become text |

### Visibility Matrix

| Context | Source | Web | PDF | DOCX | Git |
|---------|--------|-----|-----|------|-----|
| Body content | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mermaid source blocks | ✅ | ❌ | ❌ | ❌ | ✅ |
| Navigation elements | — | ✅ | ❌ | ❌ | — |
| Webcard header | — | ✅ | ❌ | ❌ | — |
| Export toolbar | — | ✅ | ❌ | ❌ | — |
| Cross-references | — | ✅ | ❌ | ❌ | — |
| Theme selector | — | ✅ | ❌ | ❌ | — |
| Language bar | — | ✅ | ❌ | ❌ | — |

---

## 10. Deployment

### GitHub Pages Configuration

| Setting | Value |
|---------|-------|
| Source | `docs/` folder on default branch |
| URL | `https://packetqc.github.io` |
| Baseurl | `/knowledge` |
| Build | Automatic on merge to default branch |

### Deployment Flow

```
Author merges PR to default branch
    ↓
GitHub Pages detects change in docs/
    ↓
Jekyll builds static HTML
    ↓
Static files deployed to CDN
    ↓
Live at packetqc.github.io/knowledge/ (~1-5 min)
```

### URL Structure

| Page type | URL pattern |
|-----------|------------|
| EN Summary | `/knowledge/publications/<slug>/` |
| EN Complete | `/knowledge/publications/<slug>/full/` |
| FR Summary | `/knowledge/fr/publications/<slug>/` |
| FR Complete | `/knowledge/fr/publications/<slug>/full/` |

The `relative_url` filter ensures all internal links work with the `/knowledge/` baseurl prefix.

---

## 11. Pipeline Commands

### Publication Lifecycle

| Command | Stage | Action |
|---------|-------|--------|
| `pub new <slug>` | Scaffolding | Create 5 files + update indexes |
| `pub sync <#>` | Synchronization | Compare source vs web, sync assets |
| `pub check <#>` | Validation | Verify structure, front matter, links |
| `pub list` | Inventory | Show all publications with status |
| `pub export <#> --pdf` | Export | PDF via CSS Paged Media |
| `pub export <#> --docx` | Export | DOCX via HTML-to-Word |

### Content Quality

| Command | Stage | Action |
|---------|-------|--------|
| `doc review <#>` | Freshness | Check against current knowledge state |
| `docs check <path>` | Validation | Front matter, links, mirror, OG |
| `normalize` | Concordance | EN/FR mirrors, front matter, links, assets |
| `normalize --fix` | Repair | Auto-fix structural issues |

### Asset Generation

| Command | Stage | Action |
|---------|-------|--------|
| `webcard <target>` | Generation | Animated OG GIFs |
| `webcard --apply` | Deployment | Generate + commit + push |

---

## 12. Known Gotchas

### Liquid Strips Mermaid Hexagons

{% raw %}**Problem**: Mermaid's `{{label}}` hexagon syntax collides with Liquid's `{{ variable }}` interpolation. Liquid runs first and silently replaces the content with empty string.{% endraw %}

**Fix**: Pre-render Mermaid diagrams to PNG using local rendering (#16), bypassing Liquid entirely.

### kramdown Escapes Tags in Details Blocks

**Problem**: `<details>` blocks with markdown code fences and blank lines cause kramdown to exit HTML block mode. Subsequent closing tags (`</summary>`, `</details>`) are HTML-escaped to `&lt;/summary&gt;`.

**Symptom**: Page appears to stop rendering after the first `<details>` block. All subsequent content is swallowed inside invisible collapsed elements.

**Fix**: Remove `<details>` blocks from web pages, or ensure they contain only inline HTML. Source preserved in git, not on web.

### baseurl Requires relative_url Filter

**Problem**: Internal links without `relative_url` filter resolve to wrong URLs (missing `/knowledge/` prefix).

**Fix**: Every internal link uses {% raw %}`{{ '/path/' | relative_url }}`{% endraw %}. `normalize` flags hardcoded paths.

### CDN Resources May Not Load

**Problem**: Container proxy may block external CDN requests (Mermaid JS, fonts).

**Fix**: Inline fallback CSS in layouts. Pre-render critical diagrams to PNG.

---

## Pipeline Diagram

```
┌─────────────────────────────────────────────────────┐
│               SOURCE AUTHORING                       │
│  publications/<slug>/v1/README.md + assets/ + media/ │
└────────────────────────┬────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│            THREE-TIER SPLIT (pub new)                │
│  EN Summary + EN Complete + FR Summary + FR Complete  │
└────────────────────────┬────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│            FRONT MATTER INJECTION                    │
│  layout, title, description, permalink, og_image,    │
│  pub_id, version, date, keywords                     │
└────────────────────────┬────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│         JEKYLL PROCESSING (3 passes)                 │
{% raw %}│  1. Liquid: {{ }}, {% %}, relative_url               │{% endraw %}
│  2. kramdown: markdown → HTML (GFM)                  │
│  3. Layout: publication.html / default.html          │
│                                                      │
{% raw %}│  ⚠ EXCLUSIONS: Liquid strips {{ }}, kramdown         │{% endraw %}
│    escapes </tags>, CSS hides .mermaid-source         │
└────────────────────────┬────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│            CLIENT-SIDE ENHANCEMENTS                  │
│  Mermaid.js, theme switcher, cross-refs, export      │
└────────────────────────┬────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│          GITHUB PAGES DEPLOYMENT                     │
│  Merge → Jekyll build → CDN → Live (~1-5 min)       │
└─────────────────────────────────────────────────────┘
```

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — the system this pipeline serves |
| 5 | [Webcards & Social Sharing]({{ '/publications/webcards-social-sharing/' | relative_url }}) | Asset pipeline — OG social previews |
| 6 | [Normalize]({{ '/publications/normalize-structure-concordance/' | relative_url }}) | Quality gate — concordance validation |
| 13 | [Web Pagination & Export]({{ '/publications/web-pagination-export/' | relative_url }}) | Export — PDF/DOCX from pipeline output |
| 14 | [Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }}) | Context — pipeline as architectural component |
| 15 | [Architecture Diagrams]({{ '/publications/architecture-diagrams/' | relative_url }}) | Visual — Diagram 6 shows publication pipeline |
| 16 | [Web Page Visualization]({{ '/publications/web-page-visualization/' | relative_url }}) | Post-pipeline — rendering and diagnostics |

**Source**: [Issue #347](https://github.com/packetqc/knowledge/issues/347) — Documentation generation session.

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
