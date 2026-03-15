# Webcard Generation — Methodology

> Adapted from `packetqc/knowledge:knowledge/methodology/methodology-webcard.md`

Animated OG social preview GIFs for publications and pages.

---

## Spec

| Parameter | Value |
|-----------|-------|
| **Size** | 1200 x 630 px |
| **Format** | Animated GIF |
| **Themes** | 4 themes — Daltonism Light, Daltonism Dark, Cayman, Midnight |
| **Languages** | EN + FR (4 GIFs total per card) |
| **Output** | `docs/assets/og/<slug>-<lang>-<theme>.gif` |
| **Quantization** | 256 colors, MEDIANCUT, Floyd-Steinberg dithering |

---

## Naming Convention

```
<slug>-<lang>-<theme>.gif
```

Examples:
- `knowledge-system-en-cayman.gif`
- `knowledge-2-fr-midnight.gif`
- `live-mindmap-en-cayman.gif`

---

## Dual-Theme Palettes

| Color | Cayman (light) | Midnight (dark) |
|-------|---------------|-----------------|
| `BG_TOP` | `#eff6ff` blue-50 | `#0f172a` deep navy |
| `BG_BOT` | `#dbeafe` blue-100 | `#1e1b4b` dark indigo |
| `ACCENT_BLUE` | `#1d4ed8` blue-700 | `#60a5fa` bright blue |
| `TEXT_WHITE` | `#0f172a` dark text | `#e2e8f0` light text |
| `TEXT_MUTED` | `#475569` | `#94a3b8` |
| `BOX_BG` | `#eff6ff` blue-50 | `#1e293b` dark fill |

**Rule**: Never hardcode colors — always use theme globals. The `set_theme()` function switches all globals at once.

---

## Animation Types

| Type | Animation | Best for |
|------|-----------|----------|
| **Diagram** | Hub-and-spoke, nodes appear sequentially | System architectures |
| **Split-panel** | Left/right panels revealing content | Before/after, comparison |
| **Index** | Cards appearing one by one | Collection pages |
| **Text-card** | Title + keywords appearing sequentially | Simple publications |
| **Mindmap** | Progressive branch-by-branch build | Knowledge graphs |

### Standard Progressive Reveal Pattern

| Frame | Action | Color state |
|-------|--------|-------------|
| 0 | Base only (title + subtitle) | — |
| 1–5 | Elements appear progressively | Previous → normal, new → dim |
| 6 | All elements visible | Start brighten pulse |
| 7 | Final frame | Full brightness, thicker borders |

---

## Live Webcard Alternative

K_DOCS supports **live webcards** via `live_webcard: mindmap` in front matter. Instead of a static GIF, the viewer renders an interactive MindElixir mindmap in the webcard area.

| Aspect | Static GIF | Live Webcard |
|--------|-----------|--------------|
| Source | Pre-generated `docs/assets/og/` | `mind_memory.md` fetched at runtime |
| Interactivity | None | Click +/- to expand, Ctrl+click expand all |
| Theme | Matches `<picture>` prefers-color-scheme | Updates live with viewer theme |
| Social sharing | Works everywhere (og:image) | Falls back to `og_image` for social |

**Convention**: Set both `og_image` (for social sharing) AND `live_webcard: mindmap` (for viewer display) when a live mindmap webcard is desired.

---

## K_DOCS Webcard Generators

### MindElixir Capture Pipeline (Primary)

Two-step pipeline that captures actual MindElixir rendering via headless Chrome:

**Step 1 — Capture frames** (`capture_mindmap.js`):
```bash
node Knowledge/K_DOCS/scripts/capture_mindmap.js daltonism-light          # Normal mode
node Knowledge/K_DOCS/scripts/capture_mindmap.js daltonism-dark --full    # Full mode (all branches)
```

- Renders MindElixir v5.9.3 in headless Puppeteer (1200x630)
- Applies theme palette via `changeTheme()` API
- Progressive scene-based animation (3 movies)
- Output: `/tmp/mindmap-frames/frame-*.png`

**Step 2 — Stitch GIF** (`stitch_webcard.py`):
```bash
python3 Knowledge/K_DOCS/scripts/stitch_webcard.py daltonism-light
python3 Knowledge/K_DOCS/scripts/stitch_webcard.py daltonism-dark
```

- Adds KNOWLEDGE header bar (gradient) + footer bar (accent)
- Shows node count and theme name
- 800ms per frame (cinematic pace), 3000ms hold on final
- Floyd-Steinberg dithering, 256 colors, optimized GIF

### Cinematic Animation — 3 Movies

| Movie | Name | Sequence |
|-------|------|----------|
| **1** | The Emergence | Root alone → depth 1 → depth 2 → depth 3 (hold) |
| **2** | The Collapse | Depth 3 → 2 → 1 (hold) |
| **3** | The Exploration | Each branch opens depth 2→3→4→5, holds, collapses before next |

**Normal mode**: Overview max depth 2, exploration max depth 3 (~20 frames)
**Full mode** (`--full`): Overview max depth 3, exploration max depth 5 (~118 frames). Includes architecture and constraints branches.

**Timing**: 800ms per frame for cinematic pace. 3000ms hold on final frame. Typical output: 121 frames (118 + 3 hold), ~2MB per GIF.

### Pillow Fallback Generator

Static fallback at `Knowledge/K_DOCS/scripts/generate_mindmap_webcard.py`:

```bash
python3 scripts/generate_mindmap_webcard.py --theme cayman
```

Features: Pillow-only rendering, bezier curves, 4 themes. Use when headless Chrome is unavailable.

---

## Base Image Structure

Every frame starts from:
1. **Gradient background** — vertical lerp from `BG_TOP` to `BG_BOT`
2. **Subtle grid** — 40px grid lines at 15% opacity
3. **Top accent bar** — 3px gradient line (blue → purple → cyan → green)
4. **Bottom accent bar** — 3px gradient line

---

## Layout Guidelines

| Zone | Y range | Content |
|------|---------|---------|
| **Title** | 50-120 | Publication number + title + subtitle |
| **Content** | 140-530 | Diagram, keywords, panels, mindmap |
| **Footer** | 580-620 | Author line + repo link |

---

## Checklist — New Webcard

1. [ ] Choose animation type based on content
2. [ ] Define EN + FR text variants
3. [ ] Layout: title zone (50-120), content zone (140-530), footer
4. [ ] Use theme globals (never hardcode colors)
5. [ ] Generate both themes
6. [ ] Verify: GIFs produced for each lang/theme combo
7. [ ] Set `og_image` in front matter (daltonism-light variant as default)
8. [ ] Generate redirect `index.html` alongside `index.md` for social sharing

---

## Social Sharing Redirect Pages

Every page with an `og_image` needs a lightweight `index.html` alongside its `index.md`:

```html
<!DOCTYPE html><html><head>
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="https://site/assets/og/slug-lang-cayman.gif">
<meta http-equiv="refresh" content="0;url=/K_DOCS/index.html?doc=path/index.md">
</head><body>Redirecting...</body></html>
```

**Why**: Social media crawlers don't execute JavaScript. The viewer is a single `index.html` that loads content via `?doc=` — crawlers only see the base page. Redirect pages provide og:image to crawlers and instant redirect to the viewer for humans.

**Convention**: Generated from front matter fields (`title`, `description`, `og_image`, `permalink`). Must be regenerated when new pages are created or `og_image` changes.

---

## Related

- Original: `packetqc/knowledge:knowledge/methodology/methodology-webcard.md`
- `methodology/web-page-visualization.md` — Rendering pipeline
- `methodology/documentation-generation.md` — Front matter contract
- Generator scripts: `Knowledge/K_DOCS/scripts/capture_mindmap.js` + `stitch_webcard.py`
- Fallback: `Knowledge/K_DOCS/scripts/generate_mindmap_webcard.py`
