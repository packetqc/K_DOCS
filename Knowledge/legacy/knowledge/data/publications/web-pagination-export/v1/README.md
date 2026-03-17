# Web Pagination & Export — Publication Documentation

**Publication #13 — Layout Conventions, PDF Pipeline, DOCX Pipeline**

*By Martin Paquet & Claude (Anthropic, Opus 4.6)*
*v1 — February 2026*

---

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Designed the three-convention layout system and both export pipelines (PDF via CSS Paged Media, DOCX via HTML-to-Word blob with MSO elements).

**Claude** (Anthropic, Opus 4.6) — AI development partner. Implemented the full PDF and DOCX export pipelines, canvas→PNG conversion for Mermaid/pie/emoji, flex→table story row conversion, and JSZip OOXML post-processing. Source: knowledge-live sessions 2026-02-24/25.

---

## Abstract

This publication documents the **web pagination and export system** for the Knowledge publication framework. It covers three layout conventions that every publication follows, the full PDF export pipeline (CSS Paged Media, zero external dependencies), and the full DOCX export pipeline (HTML-to-Word blob with MSO elements for running headers/footers).

The system achieves production-quality exports — running headers, per-page footers with page numbers, cover page with no header/footer, smart TOC page breaks, canvas-rendered diagrams and emoji — using only browser-native capabilities and client-side JavaScript. No server, no backend, no external service.

**Key principle**: The web layout is the source of truth. PDF and DOCX are sibling derived formats, both produced from the same HTML source with format-specific rendering adaptations.

---

## Table of Contents

- [Three Convention Layouts](#three-convention-layouts)
  - [publication.html — Full Export Stack](#publicationhtml--full-export-stack)
  - [default.html — Profile and Landing Pages](#defaulthtml--profile-and-landing-pages)
  - [Three-Zone @page Model](#three-zone-page-model)
- [PDF Export Pipeline](#pdf-export-pipeline)
  - [CSS Paged Media Stack](#css-paged-media-stack)
  - [Three-Zone Page Layout — PDF](#three-zone-page-layout--pdf)
  - [Running Header — Single-Box Liner](#running-header--single-box-liner)
  - [Three-Column Footer](#three-column-footer)
  - [Cover Page — No Running Headers](#cover-page--no-running-headers)
  - [Smart TOC Page Break](#smart-toc-page-break)
  - [PDF Filename Control](#pdf-filename-control)
  - [Letter/Legal Paper Size](#letterlegal-paper-size)
- [DOCX Export Pipeline](#docx-export-pipeline)
  - [Convention Hierarchy](#convention-hierarchy)
  - [Three-Zone Page Layout — DOCX](#three-zone-page-layout--docx)
  - [MSO Page Sections and Running Elements](#mso-page-sections-and-running-elements)
  - [Element Cleanup](#element-cleanup)
  - [Cover Page](#cover-page)
  - [Canvas → PNG — Canonical Pattern](#canvas--png--canonical-pattern)
  - [Mermaid Diagrams — SVG to PNG](#mermaid-diagrams--svg-to-png)
  - [Pie Charts — SVG to PNG](#pie-charts--svg-to-png)
  - [Emoji — Color Icons via Canvas](#emoji--color-icons-via-canvas)
  - [Story Rows — flex→table Conversion](#story-rows--flextable-conversion)
  - [Word HTML Rendering Limitations](#word-html-rendering-limitations)
- [Language Bar — Auto-Generated from Permalink](#language-bar--auto-generated-from-permalink)
- [Dev→Prod Promotion Model](#devprod-promotion-model)
- [Layout Scope Boundaries — Reference Table](#layout-scope-boundaries--reference-table)
- [Related Publications](#related-publications)

---

## Three Convention Layouts

The Knowledge publication framework uses exactly three HTML layout files. Each serves a distinct purpose with a clear scope boundary.

### Layout Inventory

| Layout | File | Purpose | Export |
|--------|------|---------|--------|
| **Publication** | `docs/_layouts/publication.html` | Technical publications, documentation | PDF (CSS Paged Media) + DOCX (MSO blob) |
| **Default** | `docs/_layouts/default.html` | Profile pages, landing pages, hubs | None |
| **Three-zone @page** | CSS within `publication.html` | PDF print output zones | PDF only |

### publication.html — Full Export Stack

The `publication.html` layout is the full-featured layout for any page that will be exported as PDF or DOCX. It includes the complete export infrastructure:

| Feature | Description |
|---------|-------------|
| **Export toolbar** | PDF (Letter/Legal radio) + DOCX buttons in page header |
| **`printAs()`** | JS function — injects paper size, calls `window.print()`, controls filename |
| **CSS Paged Media** | `@page` rules for three-zone layout, margin boxes, liners |
| **MSO elements** | DOCX running header/footer via `mso-element:header/footer` |
| **Language bar** | Auto-generated from `page.permalink` — EN↔FR toggle |
| **Version banner** | Auto-generated from front matter — `pub_id`, `version`, `date`, generated timestamp |
| **Webcard header** | Animated OG GIF banner — dual-theme (Cayman/Midnight) |
| **4-theme CSS** | Cayman (light), Midnight (dark), two daltonism-accessible variants |
| **Mermaid** | Diagram rendering via CDN |
| **Cross-references** | Keyword-to-publication link injection |

**`@media print` hide list** — elements stripped from PDF output (matches DOCX element cleanup):

```
.pub-export-toolbar    Export toolbar
.back-link             Navigation back links
.pub-topbar            Navigation bar with status tag
.pub-crossrefs         Auto-generated keyword links
.pub-lang-bar          Language switcher
.webcard-header        OG image banner
.board-widget          Live project board widget
.copy-toast            Ephemeral UI feedback
.page-status-tag       Web-only version indicator
.pub-version-banner    Publication/Generated/Authors metadata block
pre code.language-mermaid   Raw mermaid source blocks
```

### default.html — Profile and Landing Pages

The `default.html` layout is for pages that present rather than export. It includes visual identity and navigation but not the export stack:

| Feature | Included |
|---------|----------|
| 4-theme CSS (Cayman/Midnight) | ✅ |
| Webcard header | ✅ |
| OG meta tags | ✅ |
| Mermaid | ✅ |
| Export toolbar | ❌ |
| `printAs()` | ❌ |
| CSS Paged Media `@page` rules | ❌ |
| MSO elements | ❌ |
| Language bar | ❌ |
| Version banner | ❌ |

**Used for**: `/profile/`, `/profile/resume/`, `/profile/full/`, `/publications/`, landing pages.

### Three-Zone @page Model

The three-zone `@page` model is the CSS Paged Media print architecture embedded within `publication.html`. It defines how every printed page is structured:

```
┌─────────────────────────────────────────────────────┐
│  ZONE 1 — Header Margin Area (@page margin-top)      │
│  Publication Title                                   │
│  ═══ 2pt solid #1d4ed8 ═══════════════════════════   │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ZONE 2 — Page Content Area                         │
│  h2, h3, paragraphs, tables, code blocks...         │
│                                                     │
├─────────────────────────────────────────────────────┤
│  ═══ 2pt solid #1d4ed8 ═══════════════════════════   │
│  Generated: 2026-02-25 · v1   3 / 12   Knowledge    │
│  ZONE 3 — Footer Margin Area (@page margin-bottom)   │
└─────────────────────────────────────────────────────┘
```

**Three independent spacings** — tuned separately:

| Spacing | Controlled by | Current value |
|---------|---------------|---------------|
| Text ↔ Liner | `padding` on margin box | 0.3cm |
| Liner ↔ Content | `@page { padding }` | 0.4cm |
| Liner position | `@page { margin }` | 1.8cm from page edge |

**Canonical values** (confirmed working in Chrome/Edge):

```css
@page {
  margin: 1.8cm 1.5cm 1.8cm 1.5cm;  /* zone depth */
  padding: 0.4cm 0;                   /* liner-to-content gap */
}
@top-left {
  padding-bottom: 0.3cm;              /* text-to-liner gap */
  border-bottom: 2pt solid #1d4ed8;   /* the liner */
}
@bottom-left, @bottom-center, @bottom-right {
  padding-top: 0.3cm;                 /* liner-to-text gap */
  border-top: 2pt solid #1d4ed8;      /* the liner */
}
```

---

## PDF Export Pipeline

### CSS Paged Media Stack

Zero-dependency PDF export using browser-native capabilities:

| Layer | Technology | Role |
|-------|-----------|------|
| Trigger | `window.print()` | Opens browser print dialog |
| Layout | `@media print` | Hides non-content elements, adjusts typography |
| Pagination | `@page` CSS Paged Media | Margin boxes, page size, running headers/footers |
| Dynamic | JavaScript `beforeprint`/`afterprint` | Content injection, TOC analysis, filename control |

No external library (html2pdf.js, jsPDF, puppeteer). The browser IS the PDF renderer. Browser support: Chrome/Edge (Blink) best; Firefox supports basic `@page`; Safari has limited margin box support.

### Three-Zone Page Layout — PDF

Every printed page is divided into three zones. The `@page` margin defines zones 1 and 3 (margin boxes). `@page` padding creates the gap between liners and content. Zone 2 is the remaining content area.

**Key insight**: The margin box fills the entire margin area. The blue liner (border) always sits at the boundary between the margin area and the content area. The text-to-liner gap is margin box `padding`. The liner-to-content gap is `@page { padding }`. These three spacings are fully independent.

### Running Header — Single-Box Liner

Use one `@top-left` box at `width: 100%` with `border-bottom`. Zero all other top margin boxes:

```css
@top-left {
  content: "{{ page.title }}";
  width: 100%;
  border-bottom: 2pt solid #1d4ed8;
}
@top-center { content: ""; width: 0; }
@top-right  { content: ""; width: 0; }
```

**Why single box**: Two `@top-*` boxes with different `vertical-align` + `border-bottom` → Chrome renders borders at two heights → double liner. One box guarantees a single liner regardless of the `vertical-align` value.

### Three-Column Footer

JS-injected at print time via `printAs()`:

| Position | Content | Example |
|----------|---------|---------|
| `@bottom-left` | Generated timestamp + version | `Generated: 2026-02-25 14:30 · v1` |
| `@bottom-center` | Page numbers | `3 / 12` |
| `@bottom-right` | Brand | `Knowledge` |

Page counter uses CSS Paged Media: `counter(page) " / " counter(pages)`.

### Cover Page — No Running Headers

`@page :first` clears all margin boxes — no header, no footer, no liners on the first page:

```css
@page :first {
  @top-left    { content: ""; border: none; padding: 0; }
  @top-center  { content: ""; width: 0; }
  @top-right   { content: ""; width: 0; }
  @bottom-left { content: ""; border: none; padding: 0; }
  @bottom-center { content: ""; }
  @bottom-right  { content: ""; }
}
```

### Smart TOC Page Break

Not all publications need a forced page break after the TOC. Applying `page-break-before: always` to all first `h2` elements creates blank pages in short publications where the TOC fits on the same page as the first section.

**Algorithm** (in `printAs()`, before `window.print()`):

```javascript
var toc = document.querySelector('.toc');
var firstH2 = document.querySelector('.container h2');
var threshold = paperSize === 'legal' ? 585 : 441; // px (half-page threshold)
if (toc && firstH2) {
  if (toc.offsetHeight > threshold) {
    firstH2.style.pageBreakBefore = 'always';
  }
}
// Restore on afterprint
window.addEventListener('afterprint', function restore() {
  if (firstH2) firstH2.style.pageBreakBefore = '';
  window.removeEventListener('afterprint', restore);
});
```

Thresholds: Letter: 441px (half of ~882px content height at 96 DPI). Legal: 585px (half of ~1170px).

### PDF Filename Control

`document.title` is manipulated before print to control the browser's suggested save filename:

```javascript
var originalTitle = document.title;
var cleanTitle = document.title
  .replace(/#/g, '')                // # → blank in some browsers
  .replace(/\u2014/g, '-')          // em-dash → hyphen
  .replace(/[<>:"/\\|?*]/g, '')     // filesystem-invalid chars
  .trim();
document.title = pubId + ' - ' + cleanTitle + ' - ' + version + '.pdf';

window.print();

window.addEventListener('afterprint', function restore() {
  document.title = originalTitle;
  window.removeEventListener('afterprint', restore);
});
```

**Format**: `PUB_ID - Title - VER.pdf` (e.g., `Publication 13 - Web Pagination Export - v1.pdf`).

### Letter/Legal Paper Size

Radio selector in export toolbar; `printAs(size)` injects `@page { size }` before calling `window.print()`:

```html
<label><input type="radio" name="pubPageSize" value="letter" checked> Letter 8.5×11</label>
<label><input type="radio" name="pubPageSize" value="legal">  Legal 8.5×14</label>
```

```javascript
function printAs(paperSize) {
  var styleEl = document.createElement('style');
  styleEl.id = 'print-size-override';
  styleEl.textContent = '@page { size: ' + paperSize + '; }';
  document.head.appendChild(styleEl);
  window.print();
  // Cleanup on afterprint
}
```

---

## DOCX Export Pipeline

### Convention Hierarchy

```
Universal Layout (design spec)
  └── Web Layout (live on GitHub Pages — source of truth)
        ├── PDF Export (derived — CSS Paged Media)
        └── DOCX Export (derived — HTML-to-Word blob with MSO elements)
```

Both PDF and DOCX are **sibling** derived formats. Neither is the parent of the other. The web layout is the single source of truth.

### Three-Zone Page Layout — DOCX

The DOCX export implements the same three-zone layout as PDF using **MSO elements** instead of CSS Paged Media:

```
┌─────────────────────────────────────────────────────┐
│  ZONE 1 — Running Header (mso-element:header)        │
│  Publication Title              Publication #13      │
│  ═══ 2pt solid #1d4ed8 ══════════════════════════    │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ZONE 2 — Page Content (div.Section1)               │
│  h2, h3, paragraphs, tables, images...              │
│                                                     │
├─────────────────────────────────────────────────────┤
│  ═══ 2pt solid #1d4ed8 ══════════════════════════    │
│  Generated: 2026-02-25 · v1   3/12   Knowledge      │
│  ZONE 3 — Running Footer (mso-element:footer)        │
└─────────────────────────────────────────────────────┘
```

**Cover page exception**: `mso-first-header` and `mso-first-footer` are empty — no header or footer on the cover page. Matches PDF `@page :first` behavior.

### MSO Page Sections and Running Elements

The DOCX export uses MSO elements placed in the HTML body **before** the `<div class="Section1">` content. Word reads them as header/footer definitions and renders them in the page margin zones:

| MSO Element | ID | Purpose |
|-------------|-----|---------|
| `mso-element:header` | `h1` | Running header (all pages except first) |
| `mso-element:footer` | `f1` | Running footer (all pages except first) |
| `mso-element:header` | `fh1` | First-page header — empty (cover has no header) |
| `mso-element:footer` | `ff1` | First-page footer — empty (cover has no footer) |

Section CSS that connects content to its header/footer:

```css
@page Section1 {
  size: letter;
  margin: 1.8cm 1.5cm 1.8cm 1.5cm;
  mso-header-margin: 0.8cm;
  mso-footer-margin: 0.8cm;
  mso-header: h1;          /* running header for all pages */
  mso-footer: f1;          /* running footer for all pages */
  mso-first-header: fh1;   /* empty header for cover page */
  mso-first-footer: ff1;   /* empty footer for cover page */
}
div.Section1 { page: Section1; }
```

MIME type: `application/msword` → `.doc` extension. Word, LibreOffice, and Google Docs all open the HTML-in-Word format natively.

**Note**: No `<w:DoNotOptimizeForBrowser/>` directive — this directive restricts MS365 online from renaming or editing.

### Element Cleanup

All web-only elements are stripped from the cloned container before wrapping in the Word HTML blob:

| Element | CSS class | Why removed |
|---------|-----------|-------------|
| Export toolbar | `.pub-export-toolbar` | UI control — not content |
| Back links | `.back-link` | Navigation — not content |
| Top bar | `.pub-topbar` | Navigation bar |
| Cross-references | `.pub-crossrefs` | Auto-generated keyword links |
| Language bar | `.pub-lang-bar` | Language switcher |
| Webcard header | `.webcard-header` | OG image banner |
| Board widgets | `.board-widget`, `.board-section-widget` | Live project board |
| Toast notification | `.copy-toast` | Ephemeral UI feedback |
| Status tag | `.page-status-tag` | Web-only version indicator |
| Version banner | `.pub-version-banner` | Publication metadata block |
| Mermaid source | `pre code.language-mermaid` | Raw mermaid code blocks |

This mirrors the `@media print` hide list exactly — same elements, same reason.

### Cover Page

The cover page div (`#pub-cover-page`) is hidden on the web layout (`display:none`) and made visible at DOCX export time:

```javascript
var coverPage = document.getElementById('pub-cover-page');
if (coverPage) {
  var coverClone = coverPage.cloneNode(true);
  coverClone.style.display = 'block';
  var coverGen = coverClone.querySelector('#coverGenDate');
  if (coverGen) coverGen.textContent = ts; // inject generated timestamp
  clone.insertBefore(coverClone, clone.firstChild);
}
// Hide the regular h1 (already on cover page)
var origH1 = clone.querySelector('h1');
if (origH1) origH1.style.display = 'none';
```

Cover page CSS: `min-height: 680pt` (fills one full page), `mso-break-after: section-break` for Word-compatible page break after the cover. The `mso-first-header/footer` ensures the cover page has no running header or footer.

### Canvas → PNG — Canonical Pattern

The canonical approach for any browser-rendered graphic that Word cannot display:

```
Browser-rendered graphic → SVG/text → <Image> load → canvas → toDataURL('image/png') → <img src="data:image/png;...">
```

**Why canvas**: Word only renders `data:image/png` and `data:image/jpeg` in `<img src>`. SVG data URIs (`data:image/svg+xml`) are silently ignored. Inline `<svg>` elements are not rendered. Canvas converts any browser-rendered graphic to a PNG that Word can display.

**Async variants** (Mermaid, pie charts): Each conversion is a Promise. All Promises are collected in an array; `Promise.all([...]).then(...)` ensures all conversions complete before the HTML blob is built.

**Sync variant** (emoji): `ctx.fillText()` is synchronous. Emoji conversion runs before the Promise array is processed.

### Mermaid Diagrams — SVG to PNG

Mermaid renders `<pre><code class="language-mermaid">` → `<div class="mermaid"><svg>...</svg></div>` in the browser. The DOCX export converts each rendered SVG to PNG via canvas:

```javascript
var liveMermaidSvgs = Array.from(document.querySelectorAll('.mermaid svg'));
var mermaidDims = liveMermaidSvgs.map(function(svgEl) {
  var rect = svgEl.getBoundingClientRect();
  return { w: Math.round(rect.width) || 700, h: Math.round(rect.height) || 300 };
});

var pngPromises = cloneMermaidEls.map(function(el, idx) {
  return new Promise(function(resolve) {
    var svgStr = new XMLSerializer().serializeToString(svgEl);
    var svgUrl = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgStr);
    var loader = new Image();
    loader.onload = function() {
      var canvas = document.createElement('canvas');
      canvas.width = dim.w; canvas.height = dim.h;
      var ctx = canvas.getContext('2d');
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, dim.w, dim.h);
      ctx.drawImage(loader, 0, 0, dim.w, dim.h);
      var img = document.createElement('img');
      img.src = canvas.toDataURL('image/png');
      el.parentNode.replaceChild(img, el);
      resolve();
    };
    loader.src = svgUrl;
  });
});
```

**Important**: Dimensions are measured from the **live** SVG (pre-clone) because cloned elements have no layout. **Render guard**: If mermaid has not finished rendering when the export button is clicked, the export shows a toast and waits 2.5s for mermaid to complete before retrying.

### Pie Charts — SVG to PNG

Pie charts use CSS `conic-gradient()` in the web layout, which Word cannot render. At export time, pie elements (matched by `[class*="pie-"]`) are converted to PNG via the same canvas pattern as Mermaid:

```javascript
var promises = [];
clone.querySelectorAll('[class*="pie-"]').forEach(function(el) {
  var m = el.className.match(/pie-(\d+)-(\d+)/);
  if (!m) return;
  var pct = parseInt(m[1], 10);
  // SVG path calculation (angle math)...
  var svgUrl = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgXml);
  var p = new Promise(function(resolve) {
    var loader = new Image();
    loader.onload = function() {
      var canvas = document.createElement('canvas');
      canvas.width = 48; canvas.height = 48;
      var ctx = canvas.getContext('2d');
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, 48, 48);
      ctx.drawImage(loader, 0, 0, 48, 48);
      var img = document.createElement('img');
      img.src = canvas.toDataURL('image/png');
      img.width = 48; img.height = 48;
      el.parentNode.replaceChild(img, el);
      resolve();
    };
    loader.onerror = resolve;
    loader.src = svgUrl;
  });
  promises.push(p);
});
Promise.all(promises.concat(pngPromises)).then(function() { /* build blob */ });
```

Colors: teal (#0f766e) fill on light teal (#99f6e4) background — matches the web pie chart palette.

### Emoji — Color Icons via Canvas

Word falls back to monochrome Unicode glyphs for emoji — it does not invoke system color emoji fonts (COLR/SBIX). PDF uses the browser's native renderer and shows full color. The DOCX export converts emoji to canvas-rendered PNG images to match PDF fidelity:

```javascript
function emojiToPng(ch) {
  var canvas = document.createElement('canvas');
  canvas.width = 32; canvas.height = 32;
  var ctx = canvas.getContext('2d');
  ctx.font = '26px "Segoe UI Emoji","Apple Color Emoji","Noto Color Emoji",serif';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(ch, 16, 16);  // Browser canvas uses color emoji font
  return canvas.toDataURL('image/png');
}

// Walk all text nodes, split on emoji, replace each with <img>
var walker = document.createTreeWalker(clone, NodeFilter.SHOW_TEXT, null, false);
var textNodes = [];
while (walker.nextNode()) { textNodes.push(walker.currentNode); }
textNodes.forEach(function(tn) {
  if (!/\p{Emoji_Presentation}/u.test(tn.textContent)) return;
  var parts = tn.textContent.split(/(\p{Emoji_Presentation}\uFE0F?)/gu);
  if (parts.length <= 1) return;
  var frag = document.createDocumentFragment();
  parts.forEach(function(p) {
    if (!p) return;
    if (/\p{Emoji_Presentation}/u.test(p)) {
      var img = document.createElement('img');
      img.src = emojiToPng(p);
      img.width = 18; img.height = 18;
      img.setAttribute('style', 'vertical-align:middle;display:inline-block;margin:0 1pt;');
      frag.appendChild(img);
    } else {
      frag.appendChild(document.createTextNode(p));
    }
  });
  tn.parentNode.replaceChild(frag, tn);
});
```

**Regex note**: `\p{Emoji_Presentation}` matches Unicode emoji with graphical presentation (🧠🌾🔄🚀⚖️📡🔒🧬⚙️). The `\uFE0F?` variation selector covers explicit emoji presentation sequences. Emoji conversion runs **synchronously before** `Promise.all` — it does not need async `Image.onload`.

### Story Rows — flex→table Conversion

Word's HTML renderer completely ignores `display:flex`. Story rows use flex-based two-column layout (`.story-row-left` | `.story-row-right`) — "virtual rows" that are not real HTML tables. In DOCX, these stack vertically instead of appearing side-by-side.

**Fix**: Convert each `.story-row` div to a real 2-cell `<table>` before building the blob. Border logic applied inline (no CSS pseudo-selectors needed):

```javascript
clone.querySelectorAll('.story-section').forEach(function(section) {
  var rows = Array.from(section.querySelectorAll('.story-row'));
  rows.forEach(function(row, i) {
    var left  = row.querySelector('.story-row-left');
    var right = row.querySelector('.story-row-right');
    if (!left || !right) return;
    var isFirst = (i === 0);
    var isLast  = (i === rows.length - 1);
    var bTop    = isLast ? 'none' : (isFirst ? '1px solid #ddd' : 'none');
    var bBottom = isLast ? 'none' : '1px solid #ddd';
    var tbl = document.createElement('table');
    tbl.setAttribute('style',
      'width:100%;border-collapse:collapse;font-size:9pt;line-height:1.4;' +
      'border-top:' + bTop + ';border-bottom:' + bBottom + ';page-break-inside:avoid;');
    var tr = document.createElement('tr');
    var tdL = document.createElement('td');
    tdL.setAttribute('style',
      'width:110pt;min-width:110pt;vertical-align:top;' +
      'padding:0.15cm 0.3cm;font-weight:600;color:#555;border:none;');
    tdL.innerHTML = left.innerHTML;
    var tdR = document.createElement('td');
    tdR.setAttribute('style', 'vertical-align:top;padding:0.15cm 0.3cm;border:none;');
    tdR.innerHTML = right.innerHTML;
    tr.appendChild(tdL); tr.appendChild(tdR);
    tbl.appendChild(tr);
    row.parentNode.replaceChild(tbl, row);
  });
});
```

**Execution order**: Inner table first-cell styles must be applied **before** this conversion, because the conversion uses `innerHTML` to copy content — inline styles are preserved.

**Inner table first-cell styling** (applied before flex→table):

```javascript
clone.querySelectorAll('.story-row-right table td:first-child').forEach(function(td) {
  td.style.whiteSpace = 'nowrap';
  td.style.fontWeight = '600';
  td.style.width = '140px';
  td.style.color = '#555';
  td.style.border = 'none';
});
clone.querySelectorAll('.toc table td:first-child a').forEach(function(a) {
  a.style.color = '#1d4ed8';
  a.style.textDecoration = 'underline';
});
```

### Word HTML Rendering Limitations

Word's HTML renderer ignores a specific set of CSS features that all browsers support. This table is the authoritative reference for DOCX export workarounds:

| Browser CSS/feature | Word renders | Canonical fix |
|---------------------|-------------|---------------|
| `display:flex` | Ignored — blocks stack vertically | JS flex→table conversion |
| `padding-top` on div | Ignored | Use `margin-top` inline style |
| `border-top` on empty div | Ignored | Replace with `<p style="border-bottom:...">` |
| `:first-child`, `:last-child`, `:nth-child` | CSS pseudo-selectors ignored | JS `querySelectorAll` + inline styles |
| `data:image/svg+xml` in `<img src>` | Not rendered (silent) | Canvas→PNG data URI |
| Inline `<svg>` elements | Not rendered | Canvas→PNG data URI |
| Color emoji font (COLR/SBIX) | Monochrome Unicode glyph | Canvas `fillText`→PNG data URI |
| CSS adjacent sibling `.a + .a` | Ignored | JS index-based inline styles |
| CSS `conic-gradient()` | Ignored | Canvas→PNG data URI |

---

## Language Bar — Auto-Generated from Permalink

The language bar is injected by `publication.html` directly from `page.permalink` — no front matter flag needed:

```liquid
{% if page.permalink contains '/fr/' %}
<div class="pub-lang-bar">
  <span><strong>Langues / Languages</strong> : Français (cette page)</span>
  <a href="{{ page.permalink | remove: '/fr' | relative_url }}">English</a>
</div>
{% else %}
<div class="pub-lang-bar">
  <span><strong>Languages / Langues</strong>: English (this page)</span>
  <a href="{{ '/fr' | append: page.permalink | relative_url }}">Français</a>
</div>
{% endif %}
```

**Position**: First element of `.container`, above `pub-topbar`.

**Print**: Hidden via `display: none !important` in `@media print`. Also removed programmatically by DOCX export cleanup (`.pub-lang-bar` in the element cleanup list).

**Convention**: EN pages have `/publications/<slug>/` permalink → bar shows English (this page) + link to `/fr/publications/<slug>/`. FR pages have `/fr/publications/<slug>/` permalink → bar shows Français (cette page) + link to `/publications/<slug>/`. The `relative_url` filter handles Jekyll's `baseurl` prefix automatically.

---

## Dev→Prod Promotion Model

Layout features are developed and validated on the satellite before being promoted to core:

```
knowledge-live (dev/pre-prod)      → test on live GitHub Pages
    → harvest issue to core        → validate cross-repo
knowledge (production)             → all satellites inherit on next wakeup
```

| Stage | Repo | GitHub Pages | Purpose |
|-------|------|-------------|---------|
| Development | `knowledge-live` | `packetqc.github.io/knowledge-live/` | Test layout features live |
| Harvest | `knowledge` | — | `methodology/web-pagination-export.md` updated |
| Production | `knowledge` | `packetqc.github.io/knowledge/` | Canonical layouts deployed |
| Inheritance | All satellites | All satellite Pages | `wakeup` syncs layouts |

**The satellite IS the staging environment**: Every layout feature is validated on a live GitHub Pages instance (`knowledge-live`) before being promoted. This 2-day work cycle (2026-02-24/25) validated 37 PRs across 2 repos before the layouts were promoted to production.

---

## Layout Scope Boundaries — Reference Table

The authoritative scope table for both layouts:

| Feature | `publication.html` | `default.html` |
|---------|-------------------|----------------|
| Export toolbar (PDF + DOCX) | ✅ | ❌ |
| `printAs()` function | ✅ | ❌ |
| CSS Paged Media `@page` rules | ✅ | ❌ |
| MSO running header/footer | ✅ | ❌ |
| Language bar (EN↔FR toggle) | ✅ | ❌ |
| Version banner | ✅ | ❌ |
| Webcard header (OG GIF) | ✅ | ✅ |
| 4-theme CSS (Cayman/Midnight) | ✅ | ✅ |
| OG meta tags | ✅ | ✅ |
| Mermaid diagrams | ✅ | ✅ |
| Cross-reference injection | ✅ | ❌ |

**Design principle**: `default.html` is the minimal visual identity layer. `publication.html` is `default.html` + full export stack. The export infrastructure is in `publication.html` **only** — never `default.html`.

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge System](../knowledge-system/v1/README.md) | Parent — this publication documents core layout infrastructure |
| 3 | [AI Session Persistence](../ai-session-persistence/v1/README.md) | Session methodology — why sessions need persistent context |
| 6 | [Normalize & Structure Concordance](../normalize-structure-concordance/v1/README.md) | Structure enforcement — checks layout concordance across all pages |
| 8 | [Session Management](../session-management/v1/README.md) | `pub export` command reference |
| P6 | [Export Documentation project](../../projects/export-documentation.md) | Project tracking — 37 PRs across 2 repos, 2-day sprint |
| P8 | [Documentation System project](../../projects/documentation-system.md) | Documentation governance — 3 layouts formally documented |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
*Source: knowledge-live P3/P6 — sessions 2026-02-24/25, PRs #42–#60 (dev) + #287–#304 (prod)*
