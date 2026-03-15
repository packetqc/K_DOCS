# Webcard Generation — Methodology

Animated OG social preview GIFs for publications and pages. Extracted from `scripts/generate_og_gifs.py` — the living specification.

> See also: `methodology/methodology-documentation-web.md` (web pipeline), Publication #5 (Webcards & Social Sharing)

---

## Spec

| Parameter | Value |
|-----------|-------|
| **Size** | 1200 x 630 px |
| **Format** | Animated GIF |
| **Frames** | 8 (standard), duration 650ms per frame |
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

The `save_gif()` function auto-injects `CURRENT_THEME` into the filename.

---

## Dual-Theme Palettes

| Color | Cayman (light) | Midnight (dark) |
|-------|---------------|-----------------|
| `BG_TOP` | `#eff6ff` blue-50 | `#0f172a` deep navy |
| `BG_BOT` | `#dbeafe` blue-100 | `#1e1b4b` dark indigo |
| `ACCENT_BLUE` | `#1d4ed8` blue-700 | `#60a5fa` bright blue |
| `ACCENT_PURPLE` | `#3b82f6` blue-500 | `#a78bfa` bright purple |
| `ACCENT_CYAN` | `#0284c7` sky-600 | `#22d3ee` bright cyan |
| `ACCENT_GREEN` | `#38bdf8` sky-400 | `#4ade80` bright green |
| `TEXT_WHITE` | `#0f172a` dark text | `#e2e8f0` light text |
| `TEXT_MUTED` | `#475569` | `#94a3b8` |
| `BORDER` | `#93c5fd` blue-300 | `#334155` |
| `BOX_BG` | `#eff6ff` blue-50 | `#1e293b` dark fill |

**Rule**: Never hardcode colors — always use the theme globals (`ACCENT_BLUE`, `TEXT_WHITE`, etc.). The `set_theme()` function switches all globals at once.

---

## Animation Types

Six animation types, each suited to different content:

| Type | Animation | Best for | Example |
|------|-----------|----------|---------|
| **Corporate** | Photo with pulsing border ring | Profile pages | `profile-hub`, `resume` |
| **Diagram** | Hub-and-spoke, nodes appear sequentially | System architectures | `knowledge-system`, `distributed-minds` |
| **Split-panel** | Left/right panels revealing content | Before/after, comparison | `ai-persistence` (NPC→AWARE) |
| **Cartoon** | Character transformation with effects | Narrative, metaphor | `ai-persistence` (Vicky sunglasses) |
| **Index** | Cards appearing one by one with glow | Collection pages | `publications-index` |
| **Text-card** | Title + keywords appearing sequentially | Simple publications | `normalize`, `harvest-protocol`, `security-by-design` |

### Choosing a Type

| Content characteristic | Recommended type |
|----------------------|-----------------|
| Has a central concept + child elements | **Diagram** (hub-and-spoke) |
| Shows a transformation or progression | **Split-panel** or **cartoon** |
| Lists features or keywords | **Text-card** |
| Shows a collection of items | **Index** |
| Features a person or avatar | **Corporate** |
| Data-heavy with flowing pipeline | **Diagram** (pipeline variant) |

---

## Animation Pattern — Standard 8-Frame Sequence

All animations follow the same progressive reveal pattern:

| Frame | Action | Color state |
|-------|--------|-------------|
| 0 | Base only (title + subtitle) | — |
| 1 | First element appears | `dim()` — faded entry |
| 2 | Second element appears | Previous → normal, new → dim |
| 3-5 | Remaining elements appear | Progressive normalization |
| 6 | All elements visible | Start `brighten()` pulse |
| 7 | Final frame | Full brightness, thicker borders |

### Color Lifecycle per Element

```python
# Frame of appearance (age = 0)
border = dim(accent_color, 0.5)
fill = lerp_color(BG_BOT, BOX_BG, 0.5)
text = dim(TEXT_WHITE, 0.6)
width = 2

# Normal state (age > 0, frame < 6)
border = accent_color
fill = BOX_BG
text = TEXT_WHITE
width = 2

# Final pulse (frame >= 6)
border = brighten(accent_color, 1.4)
fill = lerp_color(BOX_BG, accent_color, 0.15)
text = TEXT_WHITE
width = 3
```

---

## Base Image Structure

Every frame starts from `base_image()`:

1. **Gradient background** — vertical lerp from `BG_TOP` to `BG_BOT`
2. **Subtle grid** — 40px grid lines at 15% opacity
3. **Top accent bar** — 3px gradient line at top (blue → purple → cyan → green)
4. **Bottom accent bar** — 3px gradient line at bottom

The base is cached per theme — only rebuilt on `set_theme()`.

---

## Layout Guidelines

| Zone | Y range | Content |
|------|---------|---------|
| **Title** | 50-120 | Publication number + title + subtitle |
| **Content** | 140-530 | Diagram, keywords, panels |
| **Footer** | 580-620 | Author line + repo link |

**Center alignment**: All text uses `anchor="mm"` at `x=600` (horizontal center).

---

## Registration

Every new card requires 3 registrations in `generate_og_gifs.py`:

```python
# 1. CARD_REGISTRY — maps name to function
CARD_REGISTRY = {
    'knowledge-2': gen_knowledge_2,
    ...
}

# 2. CARD_GROUPS — add to appropriate group
CARD_GROUPS = {
    'publications': [..., 'knowledge-2'],
}

# 3. PUB_ALIASES — map publication number to card name
PUB_ALIASES = {
    '0v2': 'knowledge-2',
}
```

---

## Fonts

| Font | Variable | Usage |
|------|----------|-------|
| DejaVu Sans Bold | `FONT_BOLD` | Titles, numbers, keywords |
| DejaVu Sans Regular | `FONT_REGULAR` | Subtitles, descriptions |
| DejaVu Sans Mono | `FONT_MONO` | Code snippets |
| DejaVu Serif | `FONT_SERIF` | Quotes (rare) |

Typical sizes: title 38-48, subtitle 20, keywords 14-18, footer 14.

---

## Checklist — New Webcard

1. [ ] Choose animation type based on content
2. [ ] Create `gen_<slug>(lang)` function
3. [ ] Define EN + FR text variants
4. [ ] Layout: title zone (50-120), content zone (140-530), footer
5. [ ] Animation: 8 frames, progressive reveal, dim→normal→brighten
6. [ ] Use theme globals (never hardcode colors)
7. [ ] Register in `CARD_REGISTRY`, `CARD_GROUPS`, `PUB_ALIASES`
8. [ ] Generate: `python3 scripts/generate_og_gifs.py <slug> --theme all --lang both`
9. [ ] Verify: 4 GIFs produced (`<slug>-{en,fr}-{cayman,midnight}.gif`)
10. [ ] Set `og_image` in front matter

---

## Related

- `scripts/generate_og_gifs.py` — Generator (living specification)
- `methodology/methodology-documentation-web.md` — Web pipeline
- `methodology/methodology-documentation.md` — Front matter contract
- Publication #5 — Webcards & Social Sharing
