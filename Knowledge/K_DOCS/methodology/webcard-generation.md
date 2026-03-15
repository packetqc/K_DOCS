# Webcard Generation — Methodology

> Adapted from `packetqc/knowledge:knowledge/methodology/methodology-webcard.md`

Animated OG social preview GIFs for publications and pages.

---

## Spec

| Parameter | Value |
|-----------|-------|
| **Size** | 1200 x 630 px |
| **Format** | Animated GIF |
| **Themes** | Dual — Cayman (light) + Midnight (dark) |
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

## K_DOCS Webcard Generator

The mindmap webcard generator lives at `Knowledge/K_DOCS/scripts/generate_mindmap_webcard.py`:

```bash
python3 scripts/generate_mindmap_webcard.py                    # Both themes
python3 scripts/generate_mindmap_webcard.py --theme cayman     # Light only
python3 scripts/generate_mindmap_webcard.py --theme midnight   # Dark only
```

Features:
- Reads `mind_memory.md` as source
- Progressive frame animation (branch-by-branch build)
- 1200x630 format with gradient header/footer bars
- Floyd-Steinberg dithering for optimized GIF

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
7. [ ] Set `og_image` in front matter (cayman variant as default)

---

## Related

- Original: `packetqc/knowledge:knowledge/methodology/methodology-webcard.md`
- `methodology/web-page-visualization.md` — Rendering pipeline
- `methodology/documentation-generation.md` — Front matter contract
- Generator script: `Knowledge/K_DOCS/scripts/generate_mindmap_webcard.py`
