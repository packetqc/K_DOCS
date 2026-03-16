---
layout: publication
title: "Web Pagination & Export — Complete Documentation"
description: "Complete documentation: three convention layouts, CSS Paged Media three-zone model, single-box header liner, smart TOC break, PDF filename control, MSO running elements for DOCX, canvas→PNG for Mermaid/pie/emoji, flex→table story row conversion, Word rendering limitations, language bar injection, dev→prod promotion model."
pub_id: "Publication #13 — Full"
version: "v1"
date: "2026-02-25"
permalink: /publications/web-pagination-export/full/
og_image: /assets/og/session-management-en-cayman.gif
keywords: "PDF, DOCX, export, pagination, CSS Paged Media, publication.html, layout, MSO, canvas, Mermaid, emoji, flex, story rows"
---

# Web Pagination & Export — Complete Documentation
{: #pub-title}

**Contents**

| | |
|---|---|
| [Authors](#authors) | Publication authors |
| [Abstract](#abstract) | System overview |
| [Three Convention Layouts](#three-convention-layouts) | publication.html · default.html · three-zone @page |
| [Layout Scope Boundaries](#layout-scope-boundaries--reference-table) | Feature matrix |
| [PDF Export Pipeline](#pdf-export-pipeline) | CSS Paged Media — zero dependencies |
| &nbsp;&nbsp;[Three-Zone Layout](#three-zone-page-layout--pdf) | Zone 1/2/3, independent spacings, canonical values |
| &nbsp;&nbsp;[Running Header — Single-Box Liner](#running-header--single-box-liner) | Why single box, Chrome double-liner bug fix |
| &nbsp;&nbsp;[Three-Column Footer](#three-column-footer) | @bottom-left/center/right |
| &nbsp;&nbsp;[Cover Page](#cover-page--no-running-headers) | @page :first — all boxes cleared |
| &nbsp;&nbsp;[Smart TOC Break](#smart-toc-page-break) | Algorithm and thresholds |
| &nbsp;&nbsp;[PDF Filename Control](#pdf-filename-control) | document.title manipulation |
| &nbsp;&nbsp;[Letter/Legal Size](#letterlegal-paper-size) | Radio selector + @page size injection |
| [DOCX Export Pipeline](#docx-export-pipeline) | HTML-to-Word blob with MSO elements |
| &nbsp;&nbsp;[Convention Hierarchy](#convention-hierarchy) | Web → PDF / DOCX sibling model |
| &nbsp;&nbsp;[Three-Zone Layout — DOCX](#three-zone-page-layout--docx) | MSO element equivalent |
| &nbsp;&nbsp;[MSO Running Elements](#mso-page-sections-and-running-elements) | Header/footer element IDs |
| &nbsp;&nbsp;[Element Cleanup](#element-cleanup) | Web-only elements stripped |
| &nbsp;&nbsp;[Cover Page](#cover-page) | mso-first-header/footer empty |
| &nbsp;&nbsp;[Canvas → PNG — Canonical Pattern](#canvas--png--canonical-pattern) | All browser graphics → Word PNG |
| &nbsp;&nbsp;[Mermaid Diagrams](#mermaid-diagrams--svg-to-png) | SVG → canvas → PNG (async) |
| &nbsp;&nbsp;[Pie Charts](#pie-charts--svg-to-png) | conic-gradient → canvas → PNG (async) |
| &nbsp;&nbsp;[Emoji — Color Icons](#emoji--color-icons-via-canvas) | fillText → PNG (sync) |
| &nbsp;&nbsp;[Story Rows — flex→table](#story-rows--flextable-conversion) | Virtual rows → real HTML tables |
| &nbsp;&nbsp;[Word Rendering Limitations](#word-html-rendering-limitations) | Authoritative limitations table |
| [Language Bar](#language-bar--auto-generated-from-permalink) | Auto EN↔FR from permalink |
| [Dev→Prod Promotion Model](#devprod-promotion-model) | knowledge-live → knowledge cycle |
| [PDF vs DOCX Parity](#pdf-vs-docx-parity) | Three-zone parity table |
| [Related Publications](#related-publications) | Sibling publications |

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Designed the three-convention layout system and both export pipelines (PDF via CSS Paged Media, DOCX via HTML-to-Word blob with MSO elements).

**Claude** (Anthropic, Opus 4.6) — AI development partner. Implemented the full PDF and DOCX export pipelines, canvas→PNG conversion for Mermaid/pie/emoji, flex→table story row conversion, and language bar auto-injection. Source: knowledge-live sessions 2026-02-24/25.

---

## Abstract

This publication documents the **web pagination and export system** for the Knowledge publication framework. Three layout conventions define every page. Two export pipelines derive from those layouts — PDF via browser-native CSS Paged Media, DOCX via HTML-to-Word blob with MSO running elements.

The system achieves production-quality exports using only browser-native capabilities and client-side JavaScript: running headers on every content page, per-page footers with page numbers, a cover page with no header/footer, canvas-rendered diagrams and emoji, and proper Word-compatible table layout for flex-based content. No server, no backend, no external service.

**Key principle**: The web layout is the source of truth. PDF and DOCX are sibling derived formats, both produced from the same HTML source with format-specific rendering adaptations.

**Source**: knowledge-live (dev) sessions 2026-02-24/25, promoted to knowledge (prod). 37 PRs across 2 repos.

---

## Three Convention Layouts

The Knowledge publication framework uses exactly three HTML layout files. Each serves a distinct purpose with a clear scope boundary.

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

### default.html — Profile and Landing Pages

The `default.html` layout is for pages that present rather than export. It includes visual identity and navigation but not the export stack.

**Includes**: 4-theme CSS, webcard header, OG meta tags, Mermaid.

**Does NOT include**: Export toolbar, `printAs()`, CSS Paged Media `@page` rules, MSO elements, language bar, version banner, cross-references.

**Used for**: `/profile/`, `/profile/resume/`, `/profile/full/`, `/publications/`, landing pages.

### Three-Zone @page Model

The three-zone `@page` model is the CSS Paged Media print architecture embedded within `publication.html`. It divides every printed page into three zones:

```
┌─────────────────────────────────────────────────────────────────┐
│  ZONE 1 — Header Margin Area (@page margin-top: 1.8cm)           │
│  "Publication Title"                   7.5pt, vertical-bottom    │
│  padding-bottom: 0.3cm (text-to-liner gap)                       │
│  ═════════════════════════ border-bottom: 2pt solid #1d4ed8 ═════│← liner
│                         @page padding-top: 0.4cm                 │
├─────────────────────────────────────────────────────────────────┤
│  ZONE 2 — Page Content Area                                     │
│  body → .container → h2, h3, paragraphs, tables, code blocks... │
│  Content flows freely between the two padded gaps               │
│                         @page padding-bottom: 0.4cm             │
├─────────────────────────────────────────────────────────────────┤
│  ════════════════════════ border-top: 2pt solid #1d4ed8 ═════════│← liner
│  padding-top: 0.3cm (liner-to-text gap)                          │
│  "Generated: 2026-02-25 · v1"   "3 / 12"   "Knowledge"          │
│  ZONE 3 — Footer Margin Area (@page margin-bottom: 1.8cm)        │
└─────────────────────────────────────────────────────────────────┘
```

**Key insight**: The margin box fills the **entire** margin area. The border (liner) sits at the boundary between the margin area and the content area. The three spacings are fully independent:

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
  padding-top: 0.3cm;
  border-top: 2pt solid #1d4ed8;
}
```

---

## Layout Scope Boundaries — Reference Table

| Feature | `publication.html` | `default.html` |
|---------|:-----------------:|:--------------:|
| Export toolbar (PDF + DOCX) | ✅ | ❌ |
| `printAs()` function | ✅ | ❌ |
| CSS Paged Media `@page` rules | ✅ | ❌ |
| MSO running header/footer | ✅ | ❌ |
| Language bar (EN↔FR toggle) | ✅ | ❌ |
| Version banner | ✅ | ❌ |
| Cross-reference injection | ✅ | ❌ |
| Webcard header (OG GIF) | ✅ | ✅ |
| 4-theme CSS (Cayman/Midnight) | ✅ | ✅ |
| OG meta tags | ✅ | ✅ |
| Mermaid diagrams | ✅ | ✅ |

**Design principle**: `default.html` is the minimal visual identity layer. `publication.html` is `default.html` + full export stack. Export infrastructure is in `publication.html` **only** — never `default.html`.

---

## PDF Export Pipeline

### CSS Paged Media Stack

Zero-dependency PDF export using browser-native capabilities — no external library:

| Layer | Technology | Role |
|-------|-----------|------|
| Trigger | `window.print()` | Opens browser print dialog |
| Layout | `@media print` | Hides non-content elements, adjusts typography |
| Pagination | `@page` CSS Paged Media | Margin boxes, page size, running headers/footers |
| Dynamic | JavaScript `beforeprint`/`afterprint` | Content injection, TOC analysis, filename control |

Browser support: Chrome/Edge (Blink) best. Firefox supports basic `@page` but not margin boxes. Safari has limited margin box support.

### Three-Zone Page Layout — PDF

See the [three-zone diagram](#three-zone-page-model) above — the PDF layout IS the three-zone model.

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

**Why single box**: Two `@top-*` boxes with different `vertical-align` values + `border-bottom` → Chrome renders borders at two heights → double liner artifact. One box guarantees a single liner regardless of the content or `vertical-align` value. This is the definitive Chrome double-liner fix.

### Three-Column Footer

JS-injected at print time via `printAs()`:

| Position | Content | Example |
|----------|---------|---------|
| `@bottom-left` | Generated timestamp + version | `Generated: 2026-02-25 14:30 · v1` |
| `@bottom-center` | Page numbers | `3 / 12` |
| `@bottom-right` | Brand | `Knowledge` |

Page counter uses CSS Paged Media counters: `counter(page) " / " counter(pages)`.

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

Not all publications need a forced page break after the TOC. A short TOC can share its page with the first section — forcing a break creates a blank page.

**Algorithm** (in `printAs()`, before `window.print()`):

```javascript
var toc = document.querySelector('.toc');
var firstH2 = document.querySelector('.container h2');
var threshold = paperSize === 'legal' ? 585 : 441; // px — half-page
if (toc && firstH2) {
  if (toc.offsetHeight > threshold) {
    firstH2.style.pageBreakBefore = 'always';
  }
}
window.addEventListener('afterprint', function restore() {
  if (firstH2) firstH2.style.pageBreakBefore = '';
  window.removeEventListener('afterprint', restore);
});
```

Thresholds: Letter 441px (half of ~882px content height at 96 DPI), Legal 585px (half of ~1170px).

### PDF Filename Control

`document.title` is manipulated before print to control the browser's suggested PDF save filename:

```javascript
var originalTitle = document.title;
var cleanTitle = document.title
  .replace(/#/g, '')
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

Radio selector in export toolbar:

```html
<label><input type="radio" name="pubPageSize" value="letter" checked> Letter 8.5×11</label>
<label><input type="radio" name="pubPageSize" value="legal"> Legal 8.5×14</label>
```

`printAs(size)` injects a `<style>` tag with `@page { size: letter; }` or `@page { size: legal; }` before calling `window.print()`. The tag is removed on `afterprint`.

---

## DOCX Export Pipeline

### Convention Hierarchy

```
Universal Layout (design spec)
  └── Web Layout (live on GitHub Pages — source of truth)
        ├── PDF Export (derived — CSS Paged Media)
        └── DOCX Export (derived — HTML-to-Word blob with MSO elements)
```

Both PDF and DOCX are **sibling** derived formats from the same source. The web layout is the single source of truth. Neither format is the parent of the other.

### Three-Zone Page Layout — DOCX

The DOCX export implements the same three-zone layout as PDF using **MSO elements** instead of CSS Paged Media:

```
┌─────────────────────────────────────────────────────────────────┐
│  ZONE 1 — Running Header (mso-element:header id="h1")           │
│  Publication Title                         Publication #13       │
│  ════════════════════════ 2pt solid #1d4ed8 ═════════════════════│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ZONE 2 — Page Content (div.Section1)                           │
│  h2, h3, paragraphs, tables, images...                          │
│  Content flows with automatic pagination                        │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  ════════════════════════ 2pt solid #1d4ed8 ═════════════════════│
│  Generated: 2026-02-25 · v1             3/12          Knowledge │
│  ZONE 3 — Running Footer (mso-element:footer id="f1")           │
└─────────────────────────────────────────────────────────────────┘
```

**Cover page exception**: `mso-first-header: fh1` and `mso-first-footer: ff1` are empty — no header or footer on the cover page. Direct equivalent of PDF `@page :first`.

### MSO Page Sections and Running Elements

MSO elements are placed in the HTML body **before** `<div class="Section1">`. Word reads them as header/footer definitions:

| MSO Element | ID | Purpose |
|-------------|-----|---------|
| `mso-element:header` | `h1` | Running header (all pages except first) |
| `mso-element:footer` | `f1` | Running footer (all pages except first) |
| `mso-element:header` | `fh1` | First-page header — empty (cover has no header) |
| `mso-element:footer` | `ff1` | First-page footer — empty (cover has no footer) |

Section CSS connecting content to header/footer:

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

MIME type: `application/msword` → `.doc` extension. Opens in Word, LibreOffice, Google Docs. **No** `<w:DoNotOptimizeForBrowser/>` directive — this restricts MS365 online editing.

### Element Cleanup

All web-only elements stripped from the cloned container before wrapping:

| Element | CSS class | Why removed |
|---------|-----------|-------------|
| Export toolbar | `.pub-export-toolbar` | UI control |
| Back links | `.back-link` | Navigation |
| Top bar | `.pub-topbar` | Navigation bar |
| Cross-references | `.pub-crossrefs` | Auto-generated links |
| Language bar | `.pub-lang-bar` | Language switcher |
| Webcard header | `.webcard-header` | OG image banner |
| Board widgets | `.board-widget`, `.board-section-widget` | Live board |
| Toast | `.copy-toast` | Ephemeral UI |
| Status tag | `.page-status-tag` | Web-only indicator |
| Version banner | `.pub-version-banner` | Metadata block |
| Mermaid source | `pre code.language-mermaid` | Raw source blocks |

This mirrors the `@media print` hide list exactly — same elements, same reason: clean export output from a navigation-rich web page.

### Cover Page

The cover page div (`#pub-cover-page`) is hidden on the web layout and made visible at DOCX export time:

```javascript
var coverPage = document.getElementById('pub-cover-page');
if (coverPage) {
  var coverClone = coverPage.cloneNode(true);
  coverClone.style.display = 'block';
  var coverGen = coverClone.querySelector('#coverGenDate');
  if (coverGen) coverGen.textContent = ts;
  clone.insertBefore(coverClone, clone.firstChild);
}
var origH1 = clone.querySelector('h1');
if (origH1) origH1.style.display = 'none';
```

Cover page CSS: `min-height: 680pt`, `mso-break-after: section-break`. `mso-first-header/footer` ensures no running header or footer on the cover page.

### Canvas → PNG — Canonical Pattern

Word cannot render SVG data URIs, inline SVGs, or color emoji fonts. The canonical pattern for any browser-rendered graphic:

```
Browser-rendered graphic
  → SVG/text
  → <Image> load (async) or fillText (sync)
  → canvas
  → canvas.toDataURL('image/png')
  → <img src="data:image/png;base64,...">
```

**Why canvas**: Word only renders `data:image/png` and `data:image/jpeg` in `<img src>`. SVG data URIs are silently ignored. Canvas converts any browser-rendered graphic to a format Word can display.

**Async variants** (Mermaid, pie charts): Each conversion returns a Promise. `Promise.all([...]).then(...)` ensures all complete before the HTML blob is built.

**Sync variant** (emoji): `ctx.fillText()` is synchronous. Runs before the Promise array, no `Image.onload` needed.

### Mermaid Diagrams — SVG to PNG

Mermaid renders `<pre><code class="language-mermaid">` to `<div class="mermaid"><svg>...</svg></div>`. At DOCX export time, each SVG is converted to PNG:

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

**Important**: Dimensions measured from the **live** SVG (pre-clone) — cloned elements have no layout. **Render guard**: If mermaid hasn't finished rendering when export is clicked, a toast is shown and the export waits 2.5s before retrying (checks `.mermaid:not(:has(svg))`).

### Pie Charts — SVG to PNG

Pie charts use CSS `conic-gradient()` — ignored by Word. At export time, pie elements (`[class*="pie-"]`) are converted to 48×48px PNG images via the same canvas pattern as Mermaid:

```javascript
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
```

Colors: teal (#0f766e) fill on light teal (#99f6e4) background. `Promise.all(promises.concat(pngPromises)).then(...)` handles both pie and Mermaid Promises together.

### Emoji — Color Icons via Canvas

Word falls back to monochrome Unicode glyphs for emoji. PDF uses the browser's native renderer (full color). The DOCX export converts emoji to canvas-rendered PNG to match PDF fidelity:

```javascript
function emojiToPng(ch) {
  var canvas = document.createElement('canvas');
  canvas.width = 32; canvas.height = 32;
  var ctx = canvas.getContext('2d');
  ctx.font = '26px "Segoe UI Emoji","Apple Color Emoji","Noto Color Emoji",serif';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(ch, 16, 16);
  return canvas.toDataURL('image/png');
}

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

**Regex**: `\p{Emoji_Presentation}` matches emoji with graphical presentation. `\uFE0F?` variation selector covers explicit emoji presentation sequences. `ctx.fillText()` is synchronous — runs before `Promise.all`.

### Story Rows — flex→table Conversion

Word completely ignores `display:flex`. Story rows use flex-based two-column layout — "virtual rows" that are not real HTML tables. In DOCX these stack vertically.

**Fix**: Convert each `.story-row` to a real 2-cell `<table>` before building the blob. Border logic applied inline (no CSS pseudo-selectors):

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

**Inner table first-cell styling** (applied **before** flex→table — preserved in `innerHTML` copy):

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

Authoritative reference for DOCX export workarounds:

| Browser CSS/feature | Word renders | Canonical fix |
|---------------------|-------------|---------------|
| `display:flex` | Ignored — blocks stack vertically | JS flex→table conversion |
| `padding-top` on div | Ignored | Use `margin-top` inline style |
| `border-top` on empty div | Ignored | Replace with `<p style="border-bottom:...">` |
| `:first-child`, `:last-child`, `:nth-child` | CSS pseudo-selectors ignored | JS `querySelectorAll` + inline styles |
| `data:image/svg+xml` in `<img src>` | Not rendered (silent) | Canvas→PNG data URI |
| Inline `<svg>` elements | Not rendered | Canvas→PNG data URI |
| Color emoji font (COLR/SBIX) | Monochrome Unicode glyph | Canvas `fillText`→PNG |
| CSS adjacent sibling `.a + .a` | Ignored | JS index-based inline styles |
| CSS `conic-gradient()` | Ignored | Canvas→PNG |

---

## Language Bar — Auto-Generated from Permalink

The language bar is injected by `publication.html` from `page.permalink` — no front matter flag needed:

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

**Print/DOCX**: Hidden via `display: none !important` in `@media print`. Also removed programmatically by DOCX export cleanup (`.pub-lang-bar` in the element cleanup list).

**Convention**: EN pages have `/publications/<slug>/` permalink → "English (this page) · Français". FR pages have `/fr/publications/<slug>/` permalink → "Français (cette page) · English". The `relative_url` filter handles Jekyll's `baseurl` prefix.

---

## Dev→Prod Promotion Model

Layout features are developed and validated on the satellite before being promoted to core:

```
knowledge-live (dev/pre-prod)      → test on live GitHub Pages
    → harvest issue to knowledge   → promote methodology
knowledge (production)             → all satellites inherit on next wakeup
```

| Stage | Repo | GitHub Pages | Purpose |
|-------|------|-------------|---------|
| Development | `knowledge-live` | `packetqc.github.io/K_DOCS-live/` | Test layout features live |
| Harvest | `knowledge` | — | `methodology/web-pagination-export.md` updated |
| Production | `knowledge` | `packetqc.github.io/K_DOCS/` | Canonical layouts deployed |
| Inheritance | All satellites | Satellite GitHub Pages | `wakeup` syncs layouts |

**The satellite IS the staging environment**: Every layout feature is validated on a live GitHub Pages instance before promotion. The 2-day sprint (2026-02-24/25) validated 37 PRs across 2 repos before the layouts reached production.

---

## PDF vs DOCX Parity

Three-zone parity between the two export formats:

| Feature | PDF (CSS Paged Media) | DOCX (MSO elements) |
|---------|----------------------|---------------------|
| Zone 1 — Header | `@top-left { content; border-bottom }` | `mso-element:header` div with table |
| Zone 2 — Content | `@page` content area (margin - padding) | `div.Section1` |
| Zone 3 — Footer | `@bottom-left/center/right` | `mso-element:footer` div with table |
| Cover page exception | `@page :first` clears all boxes | `mso-first-header/footer` set to empty |
| Page numbers | `counter(page) / counter(pages)` | `mso-field-code: PAGE / NUMPAGES` |
| Liner color | `2pt solid #1d4ed8` | `2pt solid #1d4ed8` |
| Three-column footer | `@bottom-left/center/right` | 3-cell table in footer element |
| Pie charts | Browser renders conic-gradient natively | SVG→canvas→PNG at export |
| Mermaid | Browser renders SVGs natively | SVG→canvas→PNG at export |
| Color emoji | Browser uses COLR/SBIX color font | Canvas `fillText`→PNG at export |
| Flex layout | `display:flex` side-by-side columns | JS flex→table at export |
| CSS `:first-child` | Pseudo-selectors resolved by browser | JS `querySelectorAll` + inline styles |

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — this publication documents core layout infrastructure |
| 6 | [Normalize & Structure Concordance]({{ '/publications/normalize-structure-concordance/' | relative_url }}) | Layout concordance checks |
| 8 | [Session Management]({{ '/publications/session-management/' | relative_url }}) | `pub export` command reference |
| 11 | [Success Stories]({{ '/publications/success-stories/' | relative_url }}) | Story row layout documented here |

---

[**← Summary**]({{ '/publications/web-pagination-export/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
*Source: knowledge-live P3/P6 — sessions 2026-02-24/25, 37 PRs across 2 repos*
