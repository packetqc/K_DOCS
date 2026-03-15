# Web Pagination & Export — Methodology

> Adapted from `packetqc/knowledge:knowledge/methodology/web-pagination-export.md`
> Original source: knowledge-live (P3) — T1 / P6 sessions 2026-02-25

---

## CSS Paged Media Print Stack

Zero-dependency PDF export using browser-native capabilities. The export engine lives in the viewer (`docs/index.html`), not in a Jekyll layout.

| Layer | Technology | Role |
|-------|-----------|------|
| Trigger | `window.print()` | Opens browser print dialog |
| Layout | `@media print` | Hides non-content elements, adjusts typography |
| Pagination | `@page` CSS Paged Media | Margin boxes, page size, running headers/footers |
| Dynamic | JavaScript `beforeprint`/`afterprint` | Content injection, TOC analysis, filename control |

No external library (html2pdf.js, jsPDF, puppeteer). The browser IS the PDF renderer.

### Universal Three-Zone Page Layout

Every printed page is divided into exactly three zones:

| Zone | Controlled by | Content |
|------|---------------|---------|
| **Zone 1** — Header | `@page margin-top` + `@top-left` | Publication title, blue liner (2pt solid #1d4ed8) |
| **Zone 2** — Content | Remaining page space | Body text, tables, images, Mermaid diagrams |
| **Zone 3** — Footer | `@page margin-bottom` + `@bottom-*` | Timestamp + version, page N/M, brand — blue liner |

**Three independent spacings**:

| Spacing | Controlled by | Current value |
|---------|---------------|---------------|
| Text ↔ Liner | `padding` on margin box | 0.3cm |
| Liner ↔ Content | `@page { padding }` | 0.4cm |
| Liner position | `@page { margin }` | 1.8cm from page edge |

```css
@page {
  margin: 1.8cm 1.5cm 1.8cm 1.5cm;  /* margin area = liner position */
  padding: 0.4cm 0;                   /* content inset from liner */
}
@top-left {
  padding-bottom: 0.3cm;              /* text-to-liner gap */
  border-bottom: 2pt solid #1d4ed8;   /* the liner */
}
@bottom-* {
  padding-top: 0.3cm;                 /* liner-to-text gap */
  border-top: 2pt solid #1d4ed8;      /* the liner */
}
```

**Cover page exception**: `@page :first` clears all margin boxes — no header, no footer, no liners on the first page.

### Running Header — Single-Box Liner

Use one `@top-left` box at `width: 100%` with `border-bottom`. Zero the other margin boxes:

```css
@top-left {
  content: "Publication Title";
  width: 100%;
  border-bottom: 2pt solid #1d4ed8;
}
@top-center { content: ""; width: 0; }
@top-right  { content: ""; width: 0; }
```

**Why**: Two `@top-*` boxes with different `vertical-align` + `border-bottom` → Chrome renders borders at two heights → double liner. One box = guaranteed single liner.

### Three-Column Footer

JS-injected at print time via `printAs()`:

| Position | Content | Example |
|----------|---------|---------|
| `@bottom-left` | Generated timestamp + version | `Generated: 2026-02-25 14:30 · v1` |
| `@bottom-center` | Page numbers | `3 / 12` |
| `@bottom-right` | Brand | `Knowledge` |

### Smart TOC Page Break

**Algorithm** (in `printAs()` JS):
1. Measure TOC element height
2. Compare against half-page threshold (Letter: 441px, Legal: 585px)
3. If TOC > half-page: force `page-break-before: always` on first `h2`
4. If TOC ≤ half-page: leave as `auto`
5. Restore on `afterprint`

### PDF Filename Control

`document.title` controls the browser's suggested PDF filename:

```javascript
document.title = `${pubId} - ${cleanTitle} - ${version}.pdf`;
// After print — restore original
document.title = originalTitle;
```

### Letter/Legal Paper Size

Radio selector in export toolbar. The `printAs()` function injects `@page { size: letter; }` or `@page { size: legal; }` into a `<style>` tag before calling `window.print()`.

---

## Corporate Styling Convention

**Export styling is corporate, not web theme colors.** Both PDF and DOCX use:

| Property | Value |
|----------|-------|
| Background | White (#ffffff) |
| Accent color | Blue (#1d4ed8) |
| Body font | 10pt (Calibri for DOCX) |
| Headers | Dark (#111) |
| Table headers | Blue background (#dbeafe) |
| Liners | 2pt solid blue |

This is independent of the viewer's 4-theme system. Exports always produce corporate-branded documents regardless of the user's selected theme.

---

## Client-Side DOCX Export

### Convention Hierarchy

```
Universal Layout (design spec)
  └── Web Layout (viewer — source of truth)
        ├── PDF Export (derived — CSS Paged Media)
        └── DOCX Export (derived — HTML-to-Word blob)
```

Both PDF and DOCX are **sibling** derived export formats. The viewer's `@media print` CSS is the reference for both.

### HTML-to-Word Blob with MSO Page Sections

Pure client-side Word document generation with MSO elements for per-page running headers/footers:

| MSO Element | ID | Purpose |
|-------------|-----|---------|
| `mso-element:header` | `h1` | Running header — title + pub ID with blue liner |
| `mso-element:footer` | `f1` | Running footer — timestamp + page N/M + brand |
| `mso-element:header` | `fh1` | First page header — empty (cover page) |
| `mso-element:footer` | `ff1` | First page footer — empty (cover page) |

Key MSO page section CSS:

```css
@page Section1 {
  size: letter;
  margin: 1.8cm 1.5cm 1.8cm 1.5cm;
  mso-header-margin: 0.8cm;
  mso-footer-margin: 0.8cm;
  mso-header: h1;
  mso-footer: f1;
  mso-first-header: fh1;
  mso-first-footer: ff1;
}
div.Section1 { page: Section1; }
```

### Element Cleanup

All web-only elements stripped from the cloned container before export:

| Element | CSS class | Why removed |
|---------|-----------|-------------|
| Export toolbar | `.pub-export-toolbar` | UI control |
| Back links | `.back-link` | Navigation |
| Chrome bar | `.doc-header` | Web navigation |
| Webcard header | `.webcard-header` | OG image banner |
| Toast notification | `.copy-toast` | Ephemeral UI |
| Mermaid source | `pre code.language-mermaid` | Raw code blocks |

### Canvas → PNG — Canonical Pattern

Word only renders `data:image/png` and `data:image/jpeg`. SVG data URIs are silently ignored. The canonical conversion pattern:

```
Browser-rendered graphic → SVG/text → Image load → canvas → toDataURL('image/png') → <img>
```

Applied to:
- **Mermaid diagrams** (SVG → PNG, async)
- **Pie charts** (SVG → PNG, async)
- **Color emoji** (`ctx.fillText()` → PNG, sync)

All conversions complete via `Promise.all()` before the HTML blob is built.

### Word HTML Rendering — Known Limitations

| Browser CSS/feature | Word renders | Fix |
|---------------------|-------------|-----|
| `display:flex` | Ignored — blocks stack | JS flex→table conversion |
| `padding-top` on div | Ignored | Use `margin-top` inline |
| `:first-child`, `:last-child` | Ignored | JS + inline styles |
| `data:image/svg+xml` | Not rendered | Canvas→PNG |
| Color emoji (COLR/SBIX) | Monochrome | Canvas `fillText`→PNG |

### Internal Link Rewriting for Export

The viewer's `rewriteContentLinks()` function converts internal links to viewer URL format (`index.html?doc=<path>`) for PDF/DOCX export. Direct markdown paths would 404 on GitHub Pages since `.nojekyll` serves raw files, not pretty URLs.

### Limitations — PDF vs DOCX

| Feature | PDF | DOCX |
|---------|-----|------|
| Running headers/footers | CSS Paged Media margin boxes | MSO elements |
| Page numbers | `counter(page) / counter(pages)` | `mso-field-code: PAGE / NUMPAGES` |
| Smart TOC break | JS measures height | Fixed cover break only |
| Mermaid | Browser renders natively | SVG→canvas→PNG |
| Color emoji | Browser COLR/SBIX font | Canvas→PNG |

---

## Related

- Original production methodology: `packetqc/knowledge:knowledge/methodology/web-pagination-export.md`
- `methodology/web-production-pipeline.md` — Viewer pipeline (adapted from Jekyll)
- `methodology/web-page-visualization.md` — Local rendering pipeline
