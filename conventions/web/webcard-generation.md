# Webcard Generation — Convention

> Adapted from `packetqc/knowledge:knowledge/methodology/methodology-webcard.md`

Animated OG social preview GIFs for publications and pages.

## Spec

| Parameter | Value |
|-----------|-------|
| **Size** | 1200 x 630 px |
| **Format** | Animated GIF |
| **Themes** | 4 themes: cayman, midnight, daltonism-light, daltonism-dark |
| **Languages** | EN + FR |
| **Output** | `docs/assets/og/<slug>-<lang>-<theme>.gif` |
| **Quantization** | 256 colors, MEDIANCUT, Floyd-Steinberg dithering |

## Naming Convention

```
<slug>-<lang>-<theme>.gif
```
Examples: `knowledge-system-en-cayman.gif`, `knowledge-2-fr-midnight.gif`

## Theme Palettes

| Color | Light (cayman) | Dark (midnight) |
|-------|---------------|-----------------|
| BG_TOP | `#eff6ff` | `#0f172a` |
| BG_BOT | `#dbeafe` | `#1e1b4b` |
| ACCENT_BLUE | `#1d4ed8` | `#60a5fa` |
| TEXT | `#0f172a` | `#e2e8f0` |
| MUTED | `#475569` | `#94a3b8` |

**Rule**: Never hardcode colors — always use theme globals. `set_theme()` switches all at once.

## Animation Types

| Type | Best for |
|------|----------|
| **Corporate** | Profile pages (photo + pulsing border) |
| **Diagram** | System architectures (hub-and-spoke, sequential nodes) |
| **Split-panel** | Before/after, comparison |
| **Cartoon** | Narrative, metaphor |
| **Index** | Collection pages (cards appearing with glow) |
| **Text-card** | Simple publications (title + keywords) |

## Standard 8-Frame Sequence

| Frame | Action |
|-------|--------|
| 0 | Base only (title + subtitle) |
| 1-5 | Elements appear progressively (dim → normal) |
| 6 | All visible, start brighten pulse |
| 7 | Final frame, full brightness |

## Base Image Structure

1. Gradient background (BG_TOP → BG_BOT)
2. Subtle grid (40px, 15% opacity)
3. Top/bottom accent bars (3px gradient: blue → purple → cyan → green)

## Layout Zones

| Zone | Y range | Content |
|------|---------|---------|
| Title | 50-120 | Publication number + title + subtitle |
| Content | 140-530 | Diagram, keywords, panels |
| Footer | 580-620 | Author line + repo link |

## Checklist — New Webcard

1. Choose animation type based on content
2. Create `gen_<slug>(lang)` function
3. Define EN + FR text variants
4. Layout: title (50-120), content (140-530), footer
5. Animation: 8 frames, progressive reveal, dim→normal→brighten
6. Use theme globals (never hardcode)
7. Register in CARD_REGISTRY, CARD_GROUPS, PUB_ALIASES
8. Generate and verify 4+ GIFs per publication
9. Set `og_image` in front matter
