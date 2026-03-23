# Interface Creation — Methodology

How to create a new interactive interface for the Knowledge platform. Each interface is a self-contained web application rendered inside the viewer's iframe, registered in the central JSON registry, and paired with a user guide publication.

> **Exercise reference**: This methodology was built using the Claude Interface (I6) as the first live exercise.

---

## Checklist — Quick Reference

```
1. Pick ID + slug + prefix
2. Create directory:  docs/interfaces/<slug>/
3. Write index.html   (redirect stub + OG meta)
4. Write index.md     (front matter + HTML/CSS/JS)
5. Register in        docs/data/interfaces.json
6. Update mindmap     mind/mind_memory.md (documentation::interfaces)
7. Create guide pub   docs/publications/guide-<slug>/  (optional, can defer)
8. Generate webcard   webcard <slug>  (optional, can defer)
9. Commit + deploy
```

---

## Step 1 — Identity

Choose three things:

| Item | Convention | Example |
|------|-----------|---------|
| **ID** | `I<N>` sequential | `I6` |
| **Slug** | lowercase-hyphenated | `claude-interface` |
| **CSS prefix** | 2-3 letter abbreviation | `ci-` |

The slug drives all paths: `/interfaces/<slug>/`, `guide-<slug>`, `<slug>-en-cayman.gif`.

---

## Step 2 — Directory Structure

```
docs/interfaces/<slug>/
├── index.html              # Redirect stub with OG meta tags
├── index.md                # Main interface (front matter + embedded HTML/CSS/JS)
├── <slug>.css              # Styles (optional — can inline in index.md)
├── <slug>.js               # Logic (optional — can inline in index.md)
├── <slug>-print.js         # PDF export (optional)
└── <slug>-<helper>.js      # Additional modules (optional)
```

**Decision point**: For simple interfaces, inline everything in `index.md`. For complex ones (3+ views, charts, data processing), split into separate files.

---

## Step 3 — Redirect Stub (`index.html`)

Provides OG social sharing metadata and redirects to the viewer:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta property="og:title" content="<Title> — Knowledge Interface">
<meta property="og:description" content="<Description>">
<meta property="og:type" content="article">
<meta property="og:url" content="https://packetqc.github.io/knowledge/interfaces/<slug>/">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta http-equiv="refresh" content="0;url=../../index.html?doc=interfaces/<slug>/index.md">
<title><Title> — Knowledge Interface</title>
</head>
<body>
<p>Redirecting to <a href="../../index.html?doc=interfaces/<slug>/index.md"><Title></a>...</p>
</body>
</html>
```

---

## Step 4 — Main Interface (`index.md`)

### Front Matter

```yaml
---
layout: publication
page_type: interface
title: "<Display Name>"
description: "<One-line description>"
pub_id: "Interface I<N>"
version: "v1"
date: "YYYY-MM-DD"
permalink: /interfaces/<slug>/
keywords: "<comma, separated, keywords>"
og_image: /assets/og/<slug>-en-cayman.gif
dev_banner: "Interface in development — features and layout may change between sessions."
---
```

### HTML Structure

```markdown
# <Interface Name>

{::nomarkdown}

<style>
/* 1. Interface-prefixed variables (light defaults) */
:root {
  --ci-success: #16a34a;
  --ci-warning: #d97706;
}
/* 2. Dark theme overrides */
[data-theme="midnight"] { --ci-success: #4ade80; --ci-warning: #fbbf24; }
/* 3. Component styles — always use var(--prop, fallback) */
.ci-toolbar { background: var(--code-bg, #eee8df); }
</style>

<div id="ci-viewer" data-baseurl="{{ site.baseurl }}">
  <!-- Toolbar -->
  <div class="ci-toolbar">
    <a class="iface-info-btn" data-pub="guide-<slug>" title="User Guide">ℹ</a>
  </div>

  <!-- Empty state -->
  <div id="ci-empty-state" class="ci-empty">
    <p>Loading...</p>
  </div>

  <!-- Main view containers -->
  <div id="ci-main-view" style="display:none;">
    <!-- Interface content here -->
  </div>
</div>

<script>
(function() {
  'use strict';
  var lang = (document.documentElement.lang === 'fr'
    || window.location.pathname.indexOf('/fr/') !== -1) ? 'fr' : 'en';
  var L = {
    en: { title: 'Interface Title' },
    fr: { title: 'Titre interface' }
  };
  var t = L[lang] || L.en;

  // ── Init ──
  // ── Event listeners ──
  // ── Data fetch ──
  // ── Rendering ──
})();
</script>

{:/nomarkdown}
```

### CSS Rules

1. **Never redefine wrapper variables** (`--fg`, `--bg`, `--muted`, `--accent`, `--border`, `--code-bg`, `--col-alt`) — the viewer injects them themed
2. **Prefix all custom variables** with your 2-3 letter prefix: `--ci-*`
3. **Always use fallbacks**: `var(--fg, #1f2328)` never bare `var(--fg)`
4. **Dark theme**: override only your prefixed variables under `[data-theme="midnight"]`

### JavaScript Rules

1. **IIFE wrapper** — no globals leak
2. **Bilingual L10n** — `L = { en: {...}, fr: {...} }`, alias `t = L[lang] || L.en`
3. **Language detection** — `document.documentElement.lang` + pathname check
4. **ℹ button** — standard `iface-info-btn` pattern with `postMessage` to parent for guide navigation

---

## Step 5 — Registration (`interfaces.json`)

Add entry to `docs/data/interfaces.json`:

```json
{
  "title": "<Title>", "title_fr": "<Titre>",
  "description": "<EN description>",
  "description_fr": "<FR description>",
  "href": "/interfaces/<slug>/", "target": "center",
  "pub": "guide-<slug>",
  "priority": <N>
}
```

- `target`: `"center"` (loads in center iframe) or `"top"` (replaces entire page)
- `priority`: lower = higher in list. `0` = default loaded on first visit
- `pub`: slug of the guide publication (optional, omit if no guide yet)

**External URLs**: If `href` starts with `https://`, the main navigator passes it through without prepending the site base path.

---

## Step 6 — Mindmap Update

Add the new interface node under `documentation::interfaces` in `mind/mind_memory.md`:

```
I<N> <Name>
```

---

## Step 7 — Guide Publication (optional, can defer)

Create matching guide at `docs/publications/guide-<slug>/`:
- `index.md` — summary
- `full/index.md` — full user guide

Use `pub new guide-<slug>` command to scaffold.

---

## Step 8 — Webcard (optional, can defer)

Generate OG image: `webcard <slug>`

Places animated GIF at `docs/assets/og/<slug>-en-cayman.gif`.

---

## Common Patterns

### Data Sources

| Pattern | When to Use | Example |
|---------|------------|---------|
| **JSON file** | Static/semi-static registry data | `fetch(BASE + '/data/projects.json')` |
| **GitHub API** | Live repo data (issues, PRs, branches) | `fetch('https://api.github.com/repos/...')` |
| **External API** | Third-party service integration | Claude API, external services |
| **Computed** | Derived from other data already loaded | Metrics, aggregations |

### Module Splitting

| Complexity | Approach |
|-----------|----------|
| Simple (1 view, < 300 lines JS) | Inline everything in `index.md` |
| Medium (2-3 views, 300-800 lines) | `index.md` + `<slug>.css` + `<slug>.js` |
| Complex (4+ views, charts, print) | Full module split: core, render, charts, print, time |

### Communication with Parent (Main Navigator)

```javascript
// Open a guide publication in the right panel
window.parent.postMessage({
  type: 'open-pub',
  url: pubUrl,
  title: 'Guide Title'
}, '*');
```

---

## Anti-Patterns

- **Redefining wrapper variables** — breaks theme consistency
- **Bare `var()` without fallback** — breaks when loaded outside viewer
- **Global JS variables** — always use IIFE
- **Hardcoded English** — always use L10n object
- **Missing redirect stub** — breaks social sharing / direct link access

---

## Completion

When an interface and its guide publication are ready, follow the **Publication Completion Checklist** in `methodology/documentation-generation.md#publication-completion-checklist` — page creation, HTML redirects, viewer index registration, navigator data, parent index updates, and link registry. Interfaces produce both the interactive page and a guide publication — both need full registration.

---

## Related

- `methodology/documentation-generation.md` — Content standards, quality checklist, and publication completion checklist
- `methodology/webcard-generation.md` — OG image generation for social sharing
