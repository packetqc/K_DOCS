# OG Social Images & LinkedIn Banners — Convention

> Adapted from legacy `generate_og_images.py`, `generate_og_gifs.py`, `generate_linkedin_banner.py`

Social media preview image generation for publications and profile branding.

## OG Images (Static PNG)

| Parameter | Value |
|-----------|-------|
| **Size** | 1200 x 630 px |
| **Format** | PNG |
| **Output** | `docs/assets/og/<slug>-<lang>-<theme>.png` |
| **Themes** | Dark theme default, content-specific visuals |

Used as fallback when animated GIFs aren't supported. Same naming convention as webcards.

## LinkedIn Banner

| Parameter | Value |
|-----------|-------|
| **Size** | 1584 x 396 px |
| **Format** | Animated GIF (10 frames) + static PNG |
| **Style** | Modernist architecture-inspired |
| **Layout** | 2x3 grid with project metrics, scanning effect |

### Banner Content

- Project name and tagline
- 6 metric cells in 2x3 grid (publications, interfaces, sessions, tasks, etc.)
- Scanning animation effect across cells
- Knowledge system branding

## Shared Conventions

- All social images use the same theme palette system as webcards
- Pillow (PIL) for image generation — no external rendering services
- DejaVu font family (Bold, Regular, Mono, Serif)
- Center alignment: `anchor="mm"` at horizontal center
- Output to `docs/assets/og/` directory
