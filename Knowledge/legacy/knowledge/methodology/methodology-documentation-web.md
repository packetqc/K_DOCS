# Web Production Pipeline — Methodology

How source markdown becomes a live web page on GitHub Pages. Operational companion to Publication #17.

> See also: `methodology/methodology-system-web-visualization.md` (post-pipeline rendering) and `methodology/methodology-system-web-export.md` (PDF/DOCX export)

---

## Pipeline Overview

```
Markdown source (author writes once)
    ↓ pub new (scaffold)
Three-tier split (source → summary → complete)
    ↓ front matter injection
Bilingual mirrors (EN + FR per web tier)
    ↓ Jekyll processing
Liquid → kramdown → HTML
    ↓ layout wrapping
publication.html or default.html
    ↓ client-side enhancements
Mermaid, themes, cross-references, export
    ↓ GitHub Pages deployment
Live web page (dual-theme, bilingual, exportable)
```

**Principle**: The source document is written once. Everything downstream is derived. The pipeline is deterministic — same source always produces the same output.

---

## Three-Tier Publication Structure

Each publication exists at three levels, bilingual (5 files per publication):

| Tier | Location | Purpose |
|------|----------|---------|
| **Source** | `publications/<slug>/v1/README.md` | Canonical document, English only |
| **Summary** (web) | `docs/publications/<slug>/index.md` | Quick overview, links to complete |
| **Complete** (web) | `docs/publications/<slug>/full/index.md` | Full documentation on GitHub Pages |

Bilingual: each web tier has EN + FR mirrors (`docs/fr/publications/<slug>/...`).

---

## Jekyll Processing — Three Ordered Passes

| Pass | Engine | What it does |
|------|--------|-------------|
| 1 | **Liquid** | Template processing — `{{ }}` variables, `{% %}` logic, `relative_url` filter |
| 2 | **kramdown** | Markdown → HTML — GFM dialect with `parse_block_html: true` |
| 3 | **Layout** | Wrapping — injects CSS, JS, OG tags, version banner |

**Critical**: Liquid runs first. Any `{{ }}` in markdown content (including Mermaid hexagonal nodes) is interpreted by Liquid before kramdown sees it.

---

## Front Matter Contract

Required fields for every web page:

| Field | Required by | Example |
|-------|-------------|---------|
| `layout` | Jekyll | `publication` or `default` |
| `title` | SEO, OG tags | `"Web Production Pipeline"` |
| `description` | SEO, OG tags | `"Complete production pipeline..."` |
| `permalink` | URL routing | `/publications/web-production-pipeline/` |
| `og_image` | Social sharing | `/assets/og/knowledge-system-en-cayman.gif` |

Publication pages add: `pub_id`, `version`, `date`, `keywords`.

---

## kramdown Gotchas

Operational knowledge — things that break the pipeline silently.

### 1. `<details>` blank line parsing (PR #345)

Blank lines inside `<details>` blocks cause kramdown to exit HTML block mode. `</summary>` gets escaped as `&lt;/summary&gt;`, creating cascading nesting that swallows all subsequent page content.

**Rule**: Never leave blank lines inside `<details>` blocks in Jekyll-processed markdown.

```markdown
<!-- WRONG — blank line causes kramdown to exit HTML mode -->
<details>
<summary>Title</summary>

Content here
</details>

<!-- CORRECT — no blank lines inside the block -->
<details>
<summary>Title</summary>
Content here
</details>
```

### 2. Liquid `{{ }}` stripping

Any `{{ }}` in content is interpreted by Liquid before kramdown processes it. Mermaid hexagonal nodes (`{{ }}` syntax) are silently stripped.

**Workaround**: Use `{% raw %}...{% endraw %}` around Mermaid blocks that use hexagonal nodes, or avoid `{{ }}` syntax in Mermaid diagrams.

### 3. `parse_block_html: true`

The `_config.yml` setting `parse_block_html: true` lets kramdown process markdown inside HTML blocks. This is required for `<div>` wrappers but interacts with `<details>` parsing (see gotcha #1).

### 4. Indented HTML inside `<div>` renders as code

With `parse_block_html: true`, any HTML indented 4+ spaces inside a `<div>` is interpreted by kramdown as a **code block**. Tags like `<h4>` and `<p>` appear as raw text instead of rendered HTML.

**Rule**: Never indent HTML content inside `<div>` blocks. All tags must start at column 0.

```html
<!-- WRONG — 4-space indent = code block in kramdown -->
<div class="feature-grid">
  <div class="feature-card">
    <h4>Title</h4>
    <p>Content</p>
  </div>
</div>

<!-- CORRECT — no indentation inside divs -->
<div class="feature-grid">
<div class="feature-card">
<h4>Title</h4>
<p>Content</p>
</div>
</div>
```

---

## Exclusion Mechanisms

Not everything in source appears on the live web page:

| Layer | What is excluded | Why |
|-------|-----------------|-----|
| **CSS** | `.mermaid-source` blocks | Source preservation — visible in git, hidden on web |
| **CSS** (`@media print`) | Toolbar, language bar, webcard, navigation | Clean PDF output |
| **JavaScript** | Mermaid blocks inside `.mermaid-source` | Prevents double-rendering |
| **kramdown** | `{{ }}` in code blocks | Liquid processes before kramdown |
| **kramdown** | `</tags>` in `<details>` with blank lines | HTML block mode exits on blank line |

These exclusions are architectural — they reflect Jekyll processing chain constraints, not bugs.

---

## Pipeline Commands

| Command | Action |
|---------|--------|
| `pub new <slug>` | Scaffold new publication (source + docs EN/FR + front matter) |
| `pub sync <#>` | Sync source changes to docs web pages |
| `pub check <#>` | Validate publication structure, links, front matter |
| `normalize` | Audit full knowledge structure concordance |
| `docs check <path>` | Validate individual doc page |

---

## Layout Portability (CC ↔ knowledge)

The two layouts (`publication.html`, `default.html`) are shared between `packetqc/knowledge` (v2) and `packetqc/knowledge` (v1). They are designed to be **portable** — customized per repo via `_config.yml` variables, not hardcoded values.

### Portable Variables

All repo-specific values are injected via `site.*` variables in `_config.yml`:

| Variable | CC value | knowledge value | Used by |
|----------|----------|-----------------|---------|
| `github_repo` | `packetqc/knowledge` | `packetqc/knowledge` | Raw content URLs, version.json fetch |
| `title` | `Knowledge 2.0 — Interactive Intelligence Framework` | `Knowledge System` | `og:site_name`, page titles |
| `baseurl` | `/CC` | `/knowledge` | All relative URLs, asset paths |
| `url` | `https://packetqc.github.io` | `https://packetqc.github.io` | Canonical URLs, OG tags |
| `knowledge_version` | `v2.0` | `v1.0` | Version badge display |

### What the Layouts Use

Both layouts use `{{ site.github_repo | default: "packetqc/knowledge" }}` for:
- `version.json` raw URL fetch (runtime version display)
- `version.json` fallback URL
- `og:site_name` uses `{{ site.title | default: 'Knowledge' }}`

### Migration Checklist (CC → knowledge)

When redeploying layouts from CC into the knowledge repo (v1 → v2 unification):

1. **Copy layouts**: `docs/_layouts/publication.html` and `docs/_layouts/default.html`
2. **Update `_config.yml`**: change `github_repo: "packetqc/knowledge"` → `github_repo: "packetqc/knowledge"`
3. **Copy `docs/data/version.json`**: update content for knowledge repo publications
4. **Webcards**: regenerate via `scripts/generate_og_gifs.py` (already produces both themes × both languages)
5. **No layout edits needed** — all repo-specific values flow from `_config.yml`

### Migration Checklist (knowledge → CC)

If pulling updated layouts back from knowledge into CC:

1. **Copy layouts**: same two files
2. **Verify `_config.yml`**: `github_repo` must be `"packetqc/knowledge"`
3. **No other changes needed** — Liquid variables handle the rest

### Files Involved

| File | Role |
|------|------|
| `docs/_layouts/publication.html` | Full publication layout (themes, export, webcards, mermaid) |
| `docs/_layouts/default.html` | Hub/index layout (themes, pub-cards, TOC, board widget) |
| `docs/_config.yml` | Jekyll config — single source of repo-specific values |
| `docs/data/version.json` | Runtime version data consumed by layouts |

---

## Interface vs Publication

Interfaces share the same layout (`publication.html`) and export pipeline as publications, but are dynamic JavaScript applications rather than static documentation.

| Aspect | Publication | Interface |
|--------|-------------|-----------|
| Content | Static markdown documentation | Dynamic JavaScript application |
| Interactivity | Minimal (theme, TOC) | Heavy (data viewers, charts, navigation) |
| Webcard | Animated OG GIF per page | Animated OG GIF — social media only (not displayed on page) |
| Language bar | Auto-generated EN/FR toggle | None — bilingual handled internally |
| Export | PDF/DOCX via CSS Paged Media | Same export pipeline |
| Layout | `publication` | `publication` with `page_type: interface` |
| URL path | `/publications/<slug>/` | `/interfaces/<slug>/` |
| Numbering | `#<n>` | `I<n>` |

**Front matter key**: `page_type: interface` — triggers conditional rendering in `publication.html` (no OG image preload, no webcard display, landscape default, interface-specific back-link).

---

## Related

- Publication #17 — Web Production Pipeline (full documentation)
- Issue #347 — Documentation generation session
- Issue #351 — Production rendering script creation and deployment
- `scripts/render_web_page.py` — Production rendering script (Playwright + Chromium + npm mermaid)
- `methodology/methodology-system-web-visualization.md` — Local rendering pipeline (post-pipeline)
- `methodology/methodology-system-web-export.md` — PDF/DOCX export pipeline
- Publication #13 — Web Pagination & Export
- Publication #16 — Web Page Visualization
