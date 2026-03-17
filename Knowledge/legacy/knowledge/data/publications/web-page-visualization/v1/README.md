# Web Page Visualization — Publication Documentation

**Publication #16 — Local Rendering Pipeline for AI-Assisted Development**

*By Martin Paquet & Claude (Anthropic, Opus 4.6)*
*v1 — February 2026*

---

## Authors

**Martin Paquet** — Network Security Analyst Programmer, Network and System Security Administrator, Embedded Software Designer and Programmer. 30 years of experience spanning embedded systems, network security, telecom, and software development. Autodidact and builder by nature.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Implemented the rendering pipelines, validated the approach against security-by-design constraints, and documented the methodology from interactive development sessions.

---

## Abstract

This publication documents a **self-contained, zero-dependency pipeline** for rendering web pages and Mermaid diagrams as images, directly from an AI coding assistant's environment. The pipeline uses only pre-installed tools (Python, Playwright, Chromium) and a local npm package (mermaid.js) — no external services, no CDN calls at rendering time, no API dependencies.

The capability emerged from a diagnostic need: verifying how web pages actually render (Mermaid diagrams, CSS theming, bilingual layout) without requiring the user to manually check in a browser. It proved immediately reusable across three domains:

1. **Interactive diagnostics** — Claude renders the page, identifies rendering issues, proposes fixes — all within the same session
2. **Interactive design** — Visual validation during iterative web page construction (layout changes, CSS theming, bilingual mirrors)
3. **Document management** — Generating screenshots for publications, converting Mermaid diagrams for export pipelines (PDF, DOCX), visual comparison of before/after changes

The pipeline respects the knowledge system's *autosuffisant* quality: one `git clone` bootstraps everything. No external service means no service to break, no API key to manage, no network dependency at rendering time.

---

## Table of Contents

- [Target Audience](#target-audience)
- [Architecture](#architecture)
- [Pipeline 1: Full Page Visualization](#pipeline-1-full-page-visualization)
- [Pipeline 2: Mermaid Diagram to Image](#pipeline-2-mermaid-diagram-to-image)
- [Use Cases](#use-cases)
- [Mermaid Source Preservation](#mermaid-source-preservation)
- [Web Pipeline Exclusion](#web-pipeline-exclusion)
- [Constraints and Limitations](#constraints-and-limitations)
- [Key Discoveries](#key-discoveries)
- [Validation Results](#validation-results)
- [Security by Design](#security-by-design)
- [Related Publications](#related-publications)

---

## Target Audience

| Audience | What to focus on |
|----------|-----------------|
| **Network/System Administrators** | Architecture section — understand the self-contained design and zero-network-call rendering. Security by Design — no external dependencies |
| **Programmers / Software Developers** | Pipeline code patterns — reusable Python/Playwright patterns. Mermaid Source Preservation — the hybrid `<picture>` + `<details>` approach |
| **Technical Managers** | Use Cases section — three reuse domains (diagnostics, design, document management). Abstract for strategic overview |
| **Documentation Engineers** | Mermaid Source Preservation + Web Pipeline Exclusion — the documentation generation chain design |
| **AI-Assisted Development Practitioners** | Full publication — the paradigm of an AI agent that can see what it builds |

---

## Architecture

The pipeline operates entirely within the Claude Code container environment. No external API calls at rendering time.

```
urllib (fetch HTML) → self-contained HTML → Playwright + Chromium → npm mermaid → screenshots
```

### Component Inventory

| Component | Role | Location | External? |
|-----------|------|----------|-----------|
| **urllib** | Fetch live page HTML from GitHub Pages | Python stdlib | No — bypasses container proxy via direct socket |
| **Playwright** | Headless browser automation | Python package (pre-installed in Claude Code) | No — local package |
| **Chromium** | Full DOM rendering engine with CSS, SVG, JavaScript | `/root/.cache/ms-playwright/chromium-*/chrome-linux/chrome` | No — pre-installed binary |
| **npm mermaid** | Mermaid diagram rendering (code → SVG) | `/tmp/mermaid-local-test/node_modules/mermaid/dist/mermaid.min.js` | No — local npm package |

**Zero network calls at rendering time.** The only network call is the initial HTML fetch via urllib (optional — can also render from local markdown files or generated HTML).

### Why urllib?

The container proxy intercepts standard HTTP clients (`curl`, `requests`, browser navigation via `page.goto()`). Python's `urllib` opens direct socket connections, bypassing the proxy entirely. This is the same mechanism `gh_helper.py` uses for GitHub API calls. It's the universal escape hatch in the Claude Code container environment.

### Why Chromium (not jsdom)?

Previous attempts with jsdom (a JavaScript DOM implementation for Node.js) failed because jsdom doesn't implement SVG DOM methods (`getBBox`, `getComputedTextLength`) that Mermaid requires for diagram layout calculations. Chromium provides a complete DOM with full SVG support — the same rendering engine users see in their browsers.

---

## Pipeline 1: Full Page Visualization

Render a complete web page as the user would see it, with all Mermaid diagrams rendered, CSS applied, and layout computed.

### Steps

1. **Fetch HTML** — via `urllib.request` (bypasses container proxy, returns raw HTML from GitHub Pages)
2. **Extract body content** — strip external CSS/JS references that would hang in the container (CDN links, remote stylesheets)
3. **Build self-contained HTML** — inject GitHub-like CSS styling inline. All styling is embedded — zero external dependencies
4. **Launch Playwright** — headless Chromium with `--no-sandbox`, `--disable-gpu`
5. **Inject mermaid.js** — via `page.add_script_tag(path=...)` from local npm package
6. **Render Mermaid blocks** — programmatically find `<code class="language-mermaid">` elements, render each to SVG via mermaid API
7. **Capture screenshots** — full-page (single image, potentially very tall) and/or viewport-by-viewport (paginated)

### Code Pattern

```python
import asyncio
import os
import re
from playwright.async_api import async_playwright
import urllib.request

MERMAID_JS = "/tmp/mermaid-local-test/node_modules/mermaid/dist/mermaid.min.js"
CHROME = "/root/.cache/ms-playwright/chromium-1194/chrome-linux/chrome"

async def render_web_page(url, output_dir="/tmp"):
    """Render a web page with Mermaid diagrams as screenshots."""

    # 1. Fetch HTML
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")

    # 2. Extract body
    body_match = re.search(r'<body[^>]*>(.*)</body>', html, re.DOTALL)
    body = body_match.group(1) if body_match else html

    # 3. Self-contained HTML with GitHub-like styling
    self_contained = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial;
       max-width: 980px; margin: 0 auto; padding: 20px; line-height: 1.5; color: #24292f; }}
h1, h2 {{ border-bottom: 1px solid #d0d7de; padding-bottom: .3em; }}
table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
th, td {{ border: 1px solid #d0d7de; padding: 6px 13px; }}
th {{ background: #f6f8fa; font-weight: 600; }}
code {{ background: #f6f8fa; padding: 2px 6px; border-radius: 3px; font-size: 85%; }}
pre {{ background: #f6f8fa; padding: 16px; border-radius: 6px; overflow: auto; }}
.mermaid {{ text-align: center; margin: 16px 0; }}
</style>
</head><body>{body}</body></html>"""

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path=CHROME,
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
        )
        page = await browser.new_page(viewport={"width": 1280, "height": 900})

        # 4-5. Load page and inject mermaid.js
        await page.goto("about:blank")
        await page.add_script_tag(path=MERMAID_JS)
        await page.evaluate("""(html) => {
            document.open(); document.write(html); document.close();
        }""", self_contained)
        await page.wait_for_timeout(2000)

        # 6. Render Mermaid blocks
        result = await page.evaluate("""async () => {
            mermaid.initialize({startOnLoad: false, theme: 'default', securityLevel: 'loose'});
            const blocks = document.querySelectorAll('code.language-mermaid');
            let ok = 0, fail = 0;
            for (let i = 0; i < blocks.length; i++) {
                try {
                    const { svg } = await mermaid.render('mmd-' + i, blocks[i].textContent);
                    const div = document.createElement('div');
                    div.className = 'mermaid';
                    div.innerHTML = svg;
                    blocks[i].parentElement.replaceWith(div);
                    ok++;
                } catch(e) { fail++; }
            }
            return {total: blocks.length, ok, fail};
        }""")

        # 7. Screenshots
        await page.screenshot(path=f"{output_dir}/page-full.png", full_page=True)

        height = await page.evaluate("document.body.scrollHeight")
        pages = (height + 899) // 900
        for i in range(pages):
            await page.evaluate(f"window.scrollTo(0, {i * 900})")
            await page.wait_for_timeout(200)
            await page.screenshot(path=f"{output_dir}/page-{i+1}.png")

        await browser.close()
        return result
```

---

## Pipeline 2: Mermaid Diagram to Image

Render individual Mermaid diagrams as SVG or PNG with transparent background. Essential for the DOCX export pipeline (Mermaid is not supported in Word) and for generating standalone diagram images for publications.

### Code Pattern

```python
async def render_mermaid_to_image(diagram_code, output_path, format="png"):
    """Render a single Mermaid diagram to SVG or PNG."""

    with open(MERMAID_JS, "r") as f:
        mermaid_js_content = f.read()

    html = f"""<!DOCTYPE html>
<html><head><script>{mermaid_js_content}</script>
<style>body {{ background: transparent; margin: 0; }}</style>
</head><body>
<div id="target"></div>
<div id="result" style="display:none"></div>
<script>
mermaid.initialize({{startOnLoad: false, theme: 'default', securityLevel: 'loose'}});
async function render() {{
    try {{
        const {{ svg }} = await mermaid.render('diagram', `{diagram_code}`);
        document.getElementById('target').innerHTML = svg;
        document.getElementById('result').textContent = 'OK';
    }} catch(e) {{
        document.getElementById('result').textContent = 'ERROR: ' + e.message;
    }}
}}
render();
</script>
</body></html>"""

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True, executable_path=CHROME,
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
        )
        page = await browser.new_page()
        await page.set_content(html)
        await page.wait_for_timeout(3000)

        result = await page.evaluate("document.getElementById('result').textContent")
        if result == 'OK':
            if format == "svg":
                svg = await page.evaluate("document.querySelector('#target svg').outerHTML")
                with open(output_path, "w") as f:
                    f.write(svg)
            else:  # png
                target = page.locator('#target svg')
                await target.screenshot(path=output_path, type="png")

        await browser.close()
        return result == 'OK'
```

---

## Use Cases

The pipeline serves three distinct domains, each leveraging the same core rendering capability.

### 1. Interactive Diagnostics

When a web page renders incorrectly (Mermaid diagrams broken, CSS theming issues, bilingual layout problems), Claude can render the page, see the actual output, and diagnose the issue — all in one session.

**Workflow**:
1. User reports a rendering problem (or Claude detects one during `pub check`)
2. Claude fetches and renders the page locally
3. Claude analyzes the screenshot — identifies the issue visually
4. Claude proposes and applies a fix
5. Claude re-renders to confirm the fix worked

**Real-world example**: Issue #334 — diagrams on the FR Architecture Diagrams page were rendering incorrectly. Claude rendered the page, identified that 13/14 diagrams rendered correctly (1 failed due to Liquid `{{}}` template conflict, not a rendering issue), and the user confirmed: *"ça semble fonctionner le visual d'une page web"*.

### 2. Interactive Design

During iterative web page construction, Claude renders the current state of a page to validate layout, styling, and content — without the user needing to refresh a browser.

**Workflow**:
1. Claude makes CSS, HTML, or content changes
2. Claude renders the page locally to see the result
3. Claude identifies visual issues (alignment, spacing, theming)
4. Claude adjusts and re-renders
5. User sees the final rendered page as a screenshot

**Applications**:
- Validating EN/FR bilingual mirror pages render identically (same layout, translated content)
- Checking dual-theme support (Cayman light vs Midnight dark)
- Verifying table formatting, code block styling, navigation links
- Previewing new publications before deployment

### 3. Document Management

Generating visual artifacts for the documentation pipeline: screenshots for publications, diagram images for export, visual validation reports.

**Workflow**:
1. `pub check` or `docs check` identifies a page that needs visual validation
2. Claude renders the page and captures screenshots
3. Screenshots serve as evidence for validation reports
4. Mermaid diagrams are rendered to standalone PNG/SVG for DOCX export (Mermaid.js is not supported in Word)

**Applications**:
- Pre-rendering Mermaid diagrams for dual-theme support (`<picture>` with Cayman + Midnight PNGs)
- Converting diagrams for PDF/DOCX export pipeline (Publication #13)
- Generating visual snapshots for issue comments and PR descriptions
- Validating webcard rendering and OG image display

---

## Mermaid Source Preservation

When Mermaid diagrams are pre-rendered to PNG images (for dual-theme support, faster loading, or export compatibility), a critical design decision is required: what happens to the original Mermaid source code?

### The Problem

Pre-rendering replaces ```` ```mermaid ```` code blocks with `<picture>` elements containing PNG images. If the source is removed, the documentation generation chain breaks:

| Without source | With source preserved |
|---------------|----------------------|
| Cannot update diagram — must redraw from scratch | Edit source, re-render |
| Claude sees only pixels — no semantic understanding | Claude reads Mermaid source and understands the architecture |
| Cannot generate different formats (SVG, PDF, different themes) | Source feeds any rendering pipeline |
| Classic chicken-and-egg: need source to regenerate, but source was removed | Complete — source travels with the rendered output |

### The Solution: Hybrid Format

The hybrid format preserves both the rendered output AND the source in the same page:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="diagram-midnight.png">
  <img src="diagram-cayman.png" alt="Diagram" style="max-width:100%;height:auto;">
</picture>

<details class="mermaid-source">
<summary>Mermaid source</summary>

```mermaid
graph TB
    A --> B
```

</details>
```

- The `<picture>` element renders immediately with dual-theme support (browser auto-selects Cayman or Midnight)
- The `<details class="mermaid-source">` element holds the source in a collapsible section
- On GitHub source view: the `<details>` is expandable — click to see the source
- On GitHub Pages web: the `<details>` is hidden (see Web Pipeline Exclusion below)

### Rules

1. Every pre-rendered diagram MUST retain its Mermaid source in a `<details class="mermaid-source">` block immediately after the `<picture>` element
2. The `<details>` summary is "Mermaid source" (EN) or "Source Mermaid" (FR)
3. When updating a diagram, edit the Mermaid source first, then re-render the PNG
4. The Mermaid source is the **single source of truth** — the PNG is a derived artifact

---

## Web Pipeline Exclusion

The `<details class="mermaid-source">` blocks are **excluded from web page rendering** on GitHub Pages. This is a critical design decision that prevents rendering conflicts and error propagation across the documentation pipeline.

### Why Exclusion Is Necessary

Without exclusion, the Mermaid fenced code blocks inside `<details>` are processed by kramdown (Jekyll's markdown engine) into `<code class="language-mermaid">` elements. The layout's `mermaid.js` then attempts to render these — causing three failure modes:

| Failure mode | Impact | Severity |
|-------------|--------|----------|
| **Double rendering** | mermaid.js tries to render diagrams that already exist as pre-rendered PNGs | Page confusion — duplicate diagrams or layout shifts |
| **Parse errors** | Some Mermaid syntax works in standalone rendering but fails in live mermaid.js parser | Cascade failure — one broken diagram can break ALL diagrams on the page |
| **Export contamination** | PDF and DOCX export pipelines pick up raw Mermaid blocks | Broken exports — raw code appears instead of diagrams |

### Exclusion Mechanism

Two layers of defense, applied in both layouts (`publication.html` and `default.html`):

| Layer | What it does | How |
|-------|-------------|-----|
| **CSS** | Hides `.mermaid-source` blocks from rendered page | `display: none !important` + `@media print` rule |
| **JavaScript** | Prevents mermaid.js from processing blocks inside `.mermaid-source` | `if (el.closest('.mermaid-source')) return;` in `renderMermaid()` |

The CSS layer hides the elements visually. The JS layer prevents mermaid.js from finding and processing any `language-mermaid` code blocks within `.mermaid-source` containers — defense in depth in case CSS is stripped or delayed.

### Visibility Matrix

| Context | Mermaid source visible? | Why |
|---------|------------------------|-----|
| GitHub source view (markdown) | **Yes** | GitHub renders `<details>` natively — click to expand |
| Git diff / PR review | **Yes** | Raw markdown shows the full source |
| Claude / AI reading | **Yes** | The markdown file contains the Mermaid code |
| GitHub Pages web rendering | **No** | CSS hides `.mermaid-source`, JS skips rendering |
| PDF export (browser print) | **No** | `@media print` rule + `display: none` |
| DOCX export (HTML-to-Word) | **No** | Export strips hidden elements |

### Convention

Any page that uses pre-rendered Mermaid PNGs with preserved source MUST use `class="mermaid-source"` on the `<details>` wrapper. Without the class, mermaid.js processes the source and causes rendering conflicts. This convention is enforced by `normalize` checks.

---

## Constraints and Limitations

| Constraint | Impact | Workaround |
|-----------|--------|------------|
| **Proxy blocks `page.goto()` to external URLs** | Cannot navigate directly to GitHub Pages | Fetch HTML via urllib first, then load locally via `page.evaluate()` |
| **External CSS/JS references hang** | Page load timeouts if CDN resources referenced in HTML | Build self-contained HTML, strip external refs |
| **Chromium version mismatch** | Playwright package expects newer binary than pre-installed | Use `executable_path` parameter to point to existing binary |
| **Large inline scripts timeout `set_content()`** | Mermaid.js is ~3 MB, too large for inline injection | Use `page.add_script_tag(path=...)` to load from file |
| **Liquid `{{}}` template conflict** | Jekyll strips hexagonal Mermaid nodes using `{{}}` syntax | Local rendering avoids Liquid entirely — diagrams render from source markdown |
| **jsdom lacks SVG DOM** | Node.js DOM implementation doesn't support `getBBox()` | Use Chromium (full DOM) instead of jsdom |

---

## Key Discoveries

Discoveries made during the development of this capability (session 2026-02-26):

1. **Playwright + Chromium is pre-installed** in the Claude Code environment but version-mismatched. Using `executable_path` to the existing Chromium binary bypasses the mismatch entirely.

2. **npm mermaid works locally** when given a real DOM (Chromium). Previous attempts with jsdom failed because jsdom doesn't implement SVG DOM methods (`getBBox`). Chromium provides a complete DOM — the same rendering engine users see in their browsers.

3. **urllib bypasses the container proxy** (Python opens direct sockets). This is the same mechanism `gh_helper.py` uses for GitHub API calls. The container proxy intercepts `curl`, `requests`, and browser `page.goto()` calls — but not raw Python socket connections via urllib.

4. **Self-contained HTML is the key** — stripping external CSS/JS references and injecting content inline avoids the proxy blocking external resources. The page renders locally with no network dependencies.

5. **mermaid.ink was validated but excluded** — the external rendering API (mermaid.ink) works correctly but violates the *autosuffisant* quality (self-sufficient, no external services). The local npm approach provides equivalent capability.

6. **Mermaid source must be preserved alongside pre-rendered images** — removing source blocks when deploying PNGs creates a chicken-and-egg problem. The hybrid `<picture>` + `<details class="mermaid-source">` format preserves both rendering and source.

7. **Web pipeline exclusion is critical** — Mermaid source in `<details>` blocks, if not excluded from web rendering, causes cascade failures: mermaid.js attempts to render blocks that already exist as PNGs, with parse errors propagating across all diagrams on the page.

---

## Validation Results

| Test | Result | Details |
|------|--------|---------|
| Simple Mermaid (graph TB) | OK | SVG 9.9 KB |
| Complex Mermaid (flowchart TD, 12 nodes, emojis) | OK | SVG 154 KB, PNG 55 KB |
| Full page (14 diagrams, FR) | 13/14 OK | 1 failed due to `{{}}` in source — Liquid conflict, not a rendering issue |
| Full page screenshot | OK | 18,080 px height, 2.5 MB PNG |
| Viewport captures | OK | 10 pages at 1280×900 |
| Web pipeline exclusion | OK | `.mermaid-source` blocks hidden on GitHub Pages, visible on GitHub source |

---

## Security by Design

The pipeline enforces the knowledge system's *autosuffisant* quality at every layer:

| Principle | How it applies |
|-----------|---------------|
| **Zero external services** | No CDN, no API, no cloud rendering service. Everything runs locally |
| **Zero network at render time** | The only network call is the optional HTML fetch. Rendering is 100% local |
| **Pre-installed tools only** | Playwright and Chromium are pre-installed in Claude Code. npm mermaid is installed once per session |
| **Proxy-independent** | urllib bypasses the container proxy. No `curl` or `requests` needed |
| **No credentials needed** | The rendering pipeline needs no tokens, no API keys, no authentication |
| **Reproducible** | Same environment, same tools, same output. No variation from external service behavior changes |

---

## Related Publications

| Pub | Title | Relationship |
|-----|-------|-------------|
| #13 | Web Pagination & Export | Integration target — Mermaid-to-image for DOCX export |
| #14 | Architecture Analysis | Content source — architectural understanding drives diagram design |
| #15 | Architecture Diagrams | First test subject — 14 diagrams, dual-theme rendering, source preservation |
| #5 | Webcards & Social Sharing | Parallel concept — generated visual assets for web pages |
| #6 | Normalize & Structure Concordance | Enforcement — `normalize` checks for `.mermaid-source` class convention |

---

## Related Issues

- **Issue #335** — Feature design and implementation tracking
- **Issue #334** — Origin diagnostic session (Mermaid FR rendering) — the diagnostic that discovered this capability
