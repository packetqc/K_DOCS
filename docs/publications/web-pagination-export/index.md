---
layout: publication
title: "Web Pagination & Export — Layout Conventions and Export Pipelines"
description: "Three convention layouts (publication.html, default.html, three-zone @page), zero-dependency PDF via CSS Paged Media, and client-side DOCX via HTML-to-Word blob with MSO elements. Running headers, per-page footers, canvas→PNG for Mermaid/pie/emoji, flex→table for story rows."
pub_id: "Publication #13"
version: "v1"
date: "2026-02-25"
permalink: /publications/web-pagination-export/
og_image: /assets/og/session-management-en-cayman.gif
keywords: "PDF, DOCX, export, pagination, CSS Paged Media, publication.html, layout, MSO, canvas, Mermaid"
---

# Web Pagination & Export
{: #pub-title}

> **Parent publication**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | **Projects**: [P6 — Export Documentation](https://github.com/packetqc/knowledge/blob/main/projects/export-documentation.md) · [P8 — Documentation System](https://github.com/packetqc/knowledge/blob/main/projects/documentation-system.md)

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Three layouts, two export formats, one source of truth |
| [Three Convention Layouts](#three-convention-layouts) | publication.html · default.html · three-zone @page |
| [Layout Scope Boundaries](#layout-scope-boundaries) | What each layout includes and excludes |
| [PDF Export Pipeline](#pdf-export-pipeline) | CSS Paged Media — zero dependencies |
| [DOCX Export Pipeline](#docx-export-pipeline) | HTML-to-Word blob with MSO elements |
| [Canvas → PNG Pattern](#canvas--png-pattern) | Canonical fix for Word rendering limitations |
| [Language Bar](#language-bar) | Auto-generated EN↔FR toggle |
| [Dev→Prod Model](#devprod-promotion-model) | knowledge-live → knowledge promotion cycle |

## Abstract

This publication documents the **web pagination and export system** for the Knowledge framework. Three layout conventions define every page. Two export pipelines derive from those layouts — PDF via browser-native CSS Paged Media, DOCX via HTML-to-Word blob with MSO running elements.

The system achieves production-quality exports using only browser-native capabilities: running headers on every page, per-page footers with page numbers, a cover page with no header/footer, canvas-rendered diagrams and emoji, and proper Word-compatible table layout for flex-based content. No server, no backend, no external service.

**Source**: knowledge-live (dev) sessions 2026-02-24/25, promoted to knowledge (prod). 37 PRs across 2 repos.

## Three Convention Layouts

The Knowledge framework uses exactly three HTML layout files:

| Layout | File | Purpose | Export |
|--------|------|---------|--------|
| **Publication** | `docs/_layouts/publication.html` | Technical publications, documentation | PDF + DOCX |
| **Default** | `docs/_layouts/default.html` | Profile pages, landing pages, hubs | None |
| **Three-zone @page** | CSS within `publication.html` | PDF print output zones | PDF only |

**publication.html** — the full export stack: export toolbar (PDF + DOCX), `printAs()` JS function, CSS Paged Media `@page` rules, MSO running header/footer elements, language bar (auto EN↔FR), version banner, webcard header, 4-theme CSS, Mermaid, cross-references.

**default.html** — visual identity only: webcard header, 4-theme CSS, OG meta tags, Mermaid. No export infrastructure.

## Layout Scope Boundaries

| Feature | `publication.html` | `default.html` |
|---------|:-----------------:|:--------------:|
| Export toolbar (PDF + DOCX) | ✅ | ❌ |
| `printAs()` + CSS Paged Media | ✅ | ❌ |
| MSO running header/footer | ✅ | ❌ |
| Language bar (EN↔FR) | ✅ | ❌ |
| Version banner | ✅ | ❌ |
| Webcard header (OG GIF) | ✅ | ✅ |
| 4-theme CSS (Cayman/Midnight) | ✅ | ✅ |
| OG meta tags | ✅ | ✅ |
| Mermaid diagrams | ✅ | ✅ |

**Design principle**: `default.html` is the minimal visual identity layer. `publication.html` is `default.html` + full export stack. Export infrastructure is in `publication.html` **only**.

## PDF Export Pipeline

Zero-dependency PDF using browser-native CSS Paged Media:

| Layer | Technology | Role |
|-------|-----------|------|
| Trigger | `window.print()` | Opens browser print dialog |
| Layout | `@media print` | Hides non-content elements |
| Pagination | `@page` CSS Paged Media | Margin boxes, running headers/footers |
| Dynamic | `beforeprint`/`afterprint` JS | Content injection, filename control |

**Three-zone layout**: Header margin (zone 1) → Content area (zone 2) → Footer margin (zone 3). Blue liners (2pt solid #1d4ed8) at zone boundaries. Cover page (`@page :first`) clears all margin boxes.

**Running header**: Single `@top-left` box at `width: 100%` — one box guarantees one liner. Two boxes → Chrome renders double liners.

**Smart TOC page break**: JS measures TOC height vs half-page threshold (Letter: 441px, Legal: 585px). Applies `page-break-before: always` to first `h2` only when TOC exceeds the threshold.

**PDF filename**: `PUB_ID - Title - VER.pdf` — `document.title` manipulated before print, restored on `afterprint`.

## DOCX Export Pipeline

HTML-to-Word blob with MSO elements for per-page running headers/footers:

| MSO Element | ID | Purpose |
|-------------|-----|---------|
| `mso-element:header` | `h1` | Running header — all pages except first |
| `mso-element:footer` | `f1` | Running footer — all pages except first |
| `mso-element:header` | `fh1` | First-page header — empty (cover page) |
| `mso-element:footer` | `ff1` | First-page footer — empty (cover page) |

MIME: `application/msword` → `.doc`. Opens in Word, LibreOffice, Google Docs.

**Element cleanup**: All web-only elements stripped (export toolbar, language bar, version banner, board widgets, webcard header, back links, toast notifications, mermaid source blocks).

## Canvas → PNG Pattern

Word cannot render SVG data URIs, inline SVGs, or color emoji fonts. The canonical fix for all browser-rendered graphics that Word ignores:

```
Browser-rendered graphic → SVG/text → Image load → canvas → toDataURL('image/png') → <img src="data:image/png;...">
```

Applied to:
- **Mermaid diagrams** (async) — SVG → `XMLSerializer` → `encodeURIComponent` → `Image.onload` → canvas → PNG
- **Pie charts** (async) — inline SVG XML → `encodeURIComponent` → `Image.onload` → canvas → PNG
- **Color emoji** (sync) — `ctx.fillText()` with color emoji font → PNG (synchronous, no Promise needed)

## Language Bar

Auto-generated from `page.permalink` — no front matter flag needed:

- EN pages (`/publications/<slug>/`) → "English (this page) · Français"
- FR pages (`/fr/publications/<slug>/`) → "Français (cette page) · English"

Position: first element of `.container`, above publication topbar. Hidden in print and DOCX export.

## Dev→Prod Promotion Model

```
knowledge-live (dev/pre-prod) → validate on live GitHub Pages
    → harvest to knowledge    → promote methodology
knowledge (production)        → all satellites inherit on wakeup
```

The 2-day sprint (2026-02-24/25): 19 PRs in knowledge-live (dev) + 18 PRs in knowledge (prod) = 37 PRs total. All 3 layout conventions validated, PDF pipeline production-ready, DOCX pipeline production-ready.

---

[**Read the full documentation →**]({{ '/publications/web-pagination-export/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
