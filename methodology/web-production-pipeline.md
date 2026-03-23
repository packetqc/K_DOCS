# Web Production Pipeline — Methodology

How source markdown becomes a live web page via the K_DOCS static viewer. Adapted from the original Jekyll pipeline in `packetqc/knowledge`.

> See also: `methodology/web-page-visualization.md` (local rendering) and `methodology/web-pagination-export.md` (PDF/DOCX export)

---

## Pipeline Overview

```
Markdown source (author writes once)
    ↓ three-tier split
Source / Summary / Full (front matter + markdown)
    ↓ GitHub Pages deployment (.nojekyll)
Raw markdown served as-is
    ↓ viewer fetch + parse
docs/index.html loads markdown via fetch()
    ↓ client-side rendering
marked.js → HTML, mermaid.js → SVG, MindElixir → interactive mindmap
    ↓ theme + export
4-theme system, PDF/DOCX export, bilingual EN/FR
```

**Key difference from production Jekyll pipeline**: No server-side processing. No Liquid, no kramdown. The viewer (`docs/index.html`) is a single static HTML file that fetches markdown at runtime and renders everything client-side. This eliminates all Jekyll-specific gotchas (Liquid `{{ }}` stripping, kramdown `<details>` parsing, `parse_block_html` issues).

**Principle**: The source document is written once. Everything downstream is derived. The viewer is deterministic — same source always produces the same output.

---

## Three-Tier Publication Structure

Each publication exists at three levels, bilingual (5 files per publication):

| Tier | Location | Purpose |
|------|----------|---------|
| **Source** | `docs/publications/<slug>/v1/README.md` | Canonical document, English only |
| **Summary** (web) | `docs/publications/<slug>/index.md` | Quick overview, links to full |
| **Full** (web) | `docs/publications/<slug>/full/index.md` | Full documentation with rich HTML |

Bilingual: each web tier has EN + FR mirrors (`docs/fr/publications/<slug>/...`).

---

## Client-Side Processing — Single Pass

Unlike the three-pass Jekyll pipeline (Liquid → kramdown → Layout), the viewer processes everything in one client-side pass:

| Step | Engine | What it does |
|------|--------|-------------|
| 1 | **fetch()** | Load markdown file from same-origin or GitHub raw |
| 2 | **YAML parser** | Extract front matter (title, description, og_image, etc.) |
| 3 | **Markdown parser** | Convert markdown to HTML (GFM dialect) |
| 4 | **Liquid resolver** | Replace `{{ site.baseurl }}` tags with detected base URL |
| 5 | **Mermaid renderer** | Convert fenced mermaid blocks to SVG diagrams |
| 6 | **MindElixir** | Render live interactive mindmap (when `live_webcard: mindmap`) |
| 7 | **Theme system** | Apply selected theme via CSS variables + `data-theme` attribute |

**No build step required.** The viewer works directly from markdown source files served by any static host (GitHub Pages with `.nojekyll`, any web server, or local `file://`).

---

## Front Matter Contract

Required fields for every web page:

| Field | Required by | Example |
|-------|-------------|---------|
| `title` | Viewer header, OG tags | `"Web Production Pipeline"` |
| `description` | Viewer header, OG tags | `"Complete production pipeline..."` |
| `permalink` | URL routing, cross-refs | `/publications/web-production-pipeline/` |
| `og_image` | Social sharing, webcard | `/assets/og/knowledge-system-en-cayman.gif` |

Publication pages add: `pub_id`, `version`, `pub_date`, `keywords`, `citation`.

Optional: `live_webcard: mindmap` — renders live MindElixir mindmap instead of static webcard image.

**Note**: No `layout` field needed (the viewer IS the layout). The `layout` field from production Jekyll pages is ignored by the viewer.

---

## Liquid Tag Resolution

The viewer includes a client-side Liquid resolver for `{{ site.baseurl }}` tags. This maintains compatibility with source markdown that was written for the Jekyll pipeline:

```javascript
function resolveLiquid(html) {
  var base = detectBaseUrl();
  return html
    .replace(/\{\{\s*site\.baseurl\s*\}\}/g, base)
    .replace(/\{\%\s*raw\s*\%\}([\s\S]*?)\{\%\s*endraw\s*\%\}/g, '$1');
}
```

**Convention**: Use `{{ site.baseurl }}/` for all internal links in markdown source. The viewer resolves these at render time. Never hardcode domain URLs in markdown.

---

## Theme System — 4 Themes

The viewer provides 4 themes synced across all panels via `BroadcastChannel`:

| Theme | Type | Description |
|-------|------|-------------|
| `cayman` | Light | Teal/green accents on warm cream background |
| `midnight` | Dark | Blue accents on dark navy background |
| `daltonism-light` | Light | Color-blind friendly light palette |
| `daltonism-dark` | Dark | Color-blind friendly dark palette |

Theme selection persisted in `localStorage('kdocs-theme')`. Auto mode follows OS `prefers-color-scheme`.

**BroadcastChannel sync**: The viewer is the theme master. When the user changes theme:
1. Viewer stores in localStorage
2. Broadcasts via `BroadcastChannel('kdocs-theme-sync')`
3. All same-origin iframes (I5 live mindmap, etc.) receive and apply

---

## Deployment — .nojekyll

K_DOCS uses `.nojekyll` on GitHub Pages, meaning:
- No server-side processing — markdown files served raw
- No Liquid template engine — `{{ }}` syntax preserved in source
- No kramdown — no HTML block parsing gotchas
- The viewer handles all rendering client-side

This eliminates the entire class of Jekyll processing chain constraints documented in the original production methodology.

---

## Viewer Architecture

The viewer (`docs/index.html`) is a single ~120KB HTML file containing:

| Component | Size | Role |
|-----------|------|------|
| CSS | ~20KB | 4-theme system, print styles, responsive layout |
| Markdown parser | inline | GFM → HTML conversion |
| Mermaid CDN | external | Diagram rendering |
| MindElixir CDN | external | Interactive mindmap |
| Export engine | ~15KB | PDF (CSS Paged Media) + DOCX (MSO elements) |
| Navigation | ~10KB | Three-panel layout with draggable dividers |

**Interfaces** served as iframe content within the viewer:
- I1: Main Navigator (`docs/interfaces/main-navigator/index.md`)
- I2: Project Viewer (center panel)
- I3: Session Review
- I4: Tasks Workflow
- I5: Live Mindmap (`docs/interfaces/live-mindmap/index.md`)

---

## URL Structure Compatibility

URLs match the production `packetqc/knowledge` structure for content portability:

```
/docs/publications/<slug>/          → Summary page (EN)
/docs/publications/<slug>/full/     → Full page (EN)
/docs/fr/publications/<slug>/       → Summary page (FR)
/docs/fr/publications/<slug>/full/  → Full page (FR)
```

The viewer rewrites internal links to use `index.html?doc=<path>` format for single-page navigation. Export links (PDF/DOCX) also use this format to avoid 404s on static hosts.

---

## Completion

The production pipeline deploys publications to their web presence. Before deploying, verify that all publications have completed the **Publication Completion Checklist** in `methodology/documentation-generation.md#publication-completion-checklist` — viewer index, navigator data, HTML redirects, and link registry entries must all be in place for the deployed pages to be discoverable.

## Related

- Original production methodology: `packetqc/knowledge:knowledge/methodology/web-production-pipeline.md`
- `methodology/web-page-visualization.md` — Local rendering pipeline
- `methodology/web-pagination-export.md` — PDF/DOCX export pipeline
- `methodology/documentation-generation.md` — Publication completion checklist
