# Web Page Visualization — Methodology

> Adapted from `packetqc/knowledge:knowledge/methodology/web-page-visualization.md`

A local, self-contained pipeline for rendering web pages and Mermaid diagrams as images. No external services, no CDN, no API calls at runtime. Security-by-design compliant.

## When to Use

- **Diagnostic sessions** — Show the user how a web page actually renders (Mermaid diagrams, layout, CSS)
- **Design reviews** — Visual comparison of EN/FR page variants, before/after changes
- **Webcard generation** — Generate animated GIF webcards for social sharing (og:image)
- **Documentation** — Generate page screenshots for publications or issue comments
- **Visual validation** — Verify rendering after changes without requiring the user to check in a browser

## Architecture

```
urllib (fetch HTML) → self-contained HTML → Playwright + Chromium → npm mermaid → screenshots
```

| Component | Role | External? |
|-----------|------|-----------|
| **urllib** | Fetch live page HTML | No — Python stdlib |
| **Playwright** | Headless browser automation | No — local package |
| **Chromium** | DOM rendering engine | No — pre-installed binary |
| **npm mermaid** | Mermaid diagram rendering | No — local npm package |

**Zero network calls at rendering time.** The only network call is the initial HTML fetch (optional — can render from local files).

## Prerequisites

### Pre-installed (Claude Code environment)
- Python 3.11+ with `playwright` package
- Chromium binary in Playwright cache

### Installed at session start
```bash
mkdir -p /tmp/mermaid-local-test && cd /tmp/mermaid-local-test && npm init -y --silent && npm install mermaid
```

## Pipeline 1: Full Page Visualization

Render a complete web page as the user sees it, with all Mermaid diagrams rendered.

### Steps

1. **Fetch HTML** — via `urllib.request` (bypasses proxy, returns raw HTML)
2. **Extract body content** — strip external CSS/JS references
3. **Build self-contained HTML** — inject styling inline
4. **Launch Playwright** — Chromium with `--no-sandbox`, `--disable-gpu`
5. **Inject mermaid.js** — via `page.add_script_tag(path=...)` from local npm
6. **Render Mermaid blocks** — convert `<code class="language-mermaid">` to SVG
7. **Capture screenshots** — full-page or viewport-by-viewport

## Pipeline 4: Local Viewer Rendering (Validation)

Render an interface or document through the local viewer as the user sees it — with theme, layout, and all JS applied. Use this as the **first step** when fixing any CSS/layout issue on web pages.

```bash
# Render interface with daltonism-dark theme
python3 scripts/render_web_page.py --viewer "interfaces/claude-interface/index.md" --theme daltonism-dark -o /tmp/check.png

# Other themes
python3 scripts/render_web_page.py --viewer "interfaces/live-mindmap/index.md" --theme midnight -o /tmp/mindmap.png

# Custom wait time for heavy JS rendering
python3 scripts/render_web_page.py --viewer "interfaces/session-review/index.md" --wait 5000 -o /tmp/review.png
```

**Validation workflow**: Fix code → `--viewer` render → Read the PNG → confirm visually → push. Never push CSS fixes without local visual confirmation.

The `--viewer` flag:
1. Reads the doc's markdown file from `docs/`
2. Extracts the `{::nomarkdown}` HTML block
3. Wraps it in a standalone page with theme CSS vars
4. Renders via Playwright `set_content()` (bypasses proxy/navigation issues)
5. Screenshots the viewport

## Pipeline 2: Mermaid Diagram to Image

Render individual Mermaid diagrams as SVG or PNG with transparent background.

```bash
python3 scripts/render_web_page.py --mermaid diagram.mmd --output diagram.png
python3 scripts/render_web_page.py --mermaid diagram.mmd --output diagram.svg
python3 scripts/render_web_page.py --mermaid-dir diagrams/ --output-dir rendered/
```

## Pipeline 3: Animated Webcard Generation

Generate animated GIF webcards for social sharing (og:image). Uses the mindmap as source:

```bash
python3 scripts/generate_mindmap_webcard.py                    # Both themes
python3 scripts/generate_mindmap_webcard.py --theme cayman     # Light only
python3 scripts/generate_mindmap_webcard.py --theme midnight   # Dark only
```

**Output**: `live-mindmap-{lang}-{theme}.gif` in `docs/assets/og/`

Features:
- Progressive frame animation (builds branch-by-branch)
- 1200x630 webcard format with gradient header/footer bars
- Two theme variants: cayman (light) and midnight (dark)
- Optimized 256-color GIF with Floyd-Steinberg dithering

## Mermaid Source Preservation

When Mermaid diagrams are pre-rendered to PNG images, the original Mermaid source must be preserved:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="diagram-midnight.png">
  <img src="diagram-cayman.png" alt="Diagram">
</picture>

<details class="mermaid-source">
<summary>Mermaid source</summary>

```mermaid
graph TB
    A --> B
```

</details>
```

**Rules**:
1. Every pre-rendered diagram retains its source in `<details class="mermaid-source">`
2. The source block uses standard mermaid fencing
3. When updating a diagram, edit the source first, then re-render
4. The Mermaid source is the **single source of truth** — PNG is derived

**Viewer exclusion**: `.mermaid-source` blocks are hidden via CSS (`display: none !important`) and skipped by the mermaid renderer (`if (el.closest('.mermaid-source')) return;`).

## K_DOCS Viewer vs Production Context

| Aspect | Production (Jekyll) | K_DOCS Viewer |
|--------|-------------------|---------------|
| Mermaid rendering | CDN mermaid.js in layout | CDN mermaid.js in viewer |
| Live mindmap | N/A | MindElixir v5.9.3 |
| Theme system | CSS in layout + `data-theme` | Same pattern in viewer |
| Webcard | Static `<picture>` element | Static OR live (`live_webcard: mindmap`) |
| Source preservation | `<details class="mermaid-source">` | Same convention |
| Liquid `{{ }}` conflict | Yes — `{% raw %}` required | No — viewer resolves client-side |

**Key improvement**: The K_DOCS viewer resolves Liquid tags client-side, eliminating the need for `{% raw %}` wrappers around Mermaid blocks with hexagonal nodes.

## Constraints

| Constraint | Impact | Workaround |
|-----------|--------|------------|
| Proxy blocks `page.goto()` | Cannot navigate to external URLs | Fetch via urllib, render locally |
| External CSS/JS hang | Page load timeouts | Self-contained HTML |
| Large inline scripts | `set_content()` timeouts | `page.add_script_tag(path=...)` |

## Completion

Visualizations are assets that accompany publications (diagrams, screenshots, rendered pages). After producing visualization assets, ensure the parent publication follows the **Publication Completion Checklist** in `methodology/documentation-generation.md#publication-completion-checklist` to register the publication across all system surfaces.

## Related

- Original methodology: `packetqc/knowledge:knowledge/methodology/web-page-visualization.md`
- `methodology/web-production-pipeline.md` — Viewer pipeline
- `methodology/web-pagination-export.md` — PDF/DOCX export pipeline
- `methodology/documentation-generation.md` — Publication completion checklist
- Webcard generator: `Knowledge/K_DOCS/scripts/generate_mindmap_webcard.py`
