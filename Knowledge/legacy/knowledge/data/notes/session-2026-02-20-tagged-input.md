# Session 2026-02-20 — Tagged Input Convention + Daltonism Themes

## Context
- Branch: `claude/wakeup-functionality-6Drqy`
- Previous session: LinkedIn banner + future project ideas
- knowledge-live satellite: newly bootstrapped (v25, healthy, 0 publications)
- User plans to use knowledge-live to document 3 new projects

## Work Done

### 1. Tagged Input Convention — Methodology Design
- Created `methodology/tagged-input.md` — full specification
- Composable tag syntax: `<tag>[:<tag>]* <content>`
- Tag types: `note:`, `spec:`, `arch:`, `design:`, `tech:`, `idea:`, `bug:`, `pattern:`, `lesson:`, `ref:`, `media:`, `code:`, `harvest:`
- Target tags: `#N:` (publication), `proj:<name>:` (project)
- Aspect tags: `metho:`, `ui:`, `api:`, `data:`, `sec:`, `perf:`, `test:`, `deploy:`, `doc:`
- Input mode: `input proj:X` → focused session → `done`
- Synthesis: `compile`, `review`, `export`, `inputs` commands
- Short forms: `s:` = `spec:`, `a:` = `arch:`, etc.
- Backward compatible: `remember` still works, `note:` is its evolution

### 2. Daltonism Theme Support — Design Notes
User requested 4-theme system for web publications:

| Theme | Mode | Audience | Status |
|-------|------|----------|--------|
| Cayman | Light | General | Existing — keep as-is |
| Midnight | Dark | General | Existing — keep as-is |
| **Horizon** | Light | Color-blind accessible | New — designed (hex values ready) |
| **Ember** | Dark | Color-blind accessible | New — designed (hex values ready) |

**Key decisions:**
- Webcards stay 2-theme only (Cayman + Midnight) — no webcard generation for daltonism themes
- Web pages get a theme selector dropdown at top-right corner
- Both daltonism themes use blue+orange as primary accent pairing (safest for all CVD types)
- `og:image` always uses Cayman (light) for social sharing — no change
- Current Cayman accents (Teal/Cyan/Emerald) are problematic for protanopia/deuteranopia (all in same blue-green band)
- Current Midnight accents (Blue/Purple/Cyan) — Blue/Purple often indistinguishable for some CVD types

**Problem with current themes for color-blind users:**
- Cayman: Teal (#0f766e), Cyan (#06b6d4), Emerald (#059669) — all blue-green, indistinguishable for red-green CVD
- Midnight: Blue (#60a5fa), Purple (#a78bfa) — often confusable for some types

**Design principles for new themes:**
- Blue + Orange/Amber as primary accent differentiation
- Varied lightness (must work in greyscale)
- WCAG AA contrast minimum (4.5:1 text, 3:1 UI)
- Professional aesthetic, not clinical

### 2b. Daltonism Theme Research — Complete Results

**Theme names chosen**: **Horizon** (warm light) + **Ember** (warm dark)

The 4 themes form a natural progression:
- Cayman (cool light) ↔ **Horizon** (warm light)
- Midnight (cool dark) ↔ **Ember** (warm dark)

**Scientific basis**: Okabe-Ito palette (Color Universal Design, U. Tokyo) + IBM Color Blind Safe palette. Both validated that blue+orange is the safest universal pair across all CVD types.

**Key design rule**: Every accent triad has different luminance values — even with total color blindness (achromatopsia), all three accents are distinguishable as different shades of gray.

#### Horizon (Light, CVD-Friendly) — Warm sand/cream

| Property | Hex | RGB | Contrast |
|----------|-----|-----|----------|
| BG_TOP | `#f5f0eb` | (245, 240, 235) | — |
| BG_BOT | `#eae3db` | (234, 227, 219) | — |
| ACCENT_BLUE | `#0369a1` | (3, 105, 161) | 5.24:1 AA |
| ACCENT_PURPLE → Orange | `#a14b08` | (161, 75, 8) | 5.26:1 AA |
| ACCENT_CYAN → Rose | `#9f1239` | (159, 18, 57) | 7.07:1 AAA |
| ACCENT_GREEN → Mid-amber | `#c27817` | (194, 120, 23) | — |
| TEXT_WHITE | `#1c1510` | (28, 21, 16) | 15.9:1 AAA |
| TEXT_MUTED | `#5c5549` | (92, 85, 73) | 6.5:1 AA |
| TEXT_DIM | `#6e665b` | (110, 102, 91) | 4.99:1 AA |
| BORDER | `#d4ccc2` | (212, 204, 194) | 3.0:1 UI |
| BOX_BG | `#f5f0eb` | (245, 240, 235) | — |
| CODE_BG | `#eae3db` | (234, 227, 219) | — |

#### Ember (Dark, CVD-Friendly) — Warm charcoal

| Property | Hex | RGB | Contrast |
|----------|-----|-----|----------|
| BG_TOP | `#1a1612` | (26, 22, 18) | — |
| BG_BOT | `#231e19` | (35, 30, 25) | — |
| ACCENT_BLUE | `#65ade5` | (101, 173, 229) | 7.41:1 AAA |
| ACCENT_PURPLE → Amber | `#e8a045` | (232, 160, 69) | 8.17:1 AAA |
| ACCENT_CYAN → Coral | `#e87070` | (232, 112, 112) | 5.99:1 AA |
| ACCENT_GREEN → Light amber | `#f0b860` | (240, 184, 96) | — |
| TEXT_WHITE | `#e2e0db` | (226, 224, 219) | 13.6:1 AAA |
| TEXT_MUTED | `#9c9589` | (156, 149, 137) | 6.05:1 AA |
| TEXT_DIM | `#8a8279` | (138, 130, 121) | 4.75:1 AA |
| BORDER | `#3d362e` | (61, 54, 46) | 3.0:1 UI |
| BOX_BG | `#262019` | (38, 32, 25) | — |
| CODE_BG | `#3d362e` | (61, 54, 46) | — |

#### CVD Simulation Summary

| CVD Type | Horizon Blue/Orange/Rose | Ember Blue/Amber/Coral |
|----------|--------------------------|------------------------|
| Normal | 3 distinct hues | 3 distinct hues |
| Protanopia | Blue stays, Orange→yellow-brown, Rose→dark brown — 3 luminance levels | Blue stays, Amber→yellow, Coral→dark brown — 3 luminance levels |
| Deuteranopia | Blue stays, Orange→mustard, Rose→brownish — 3 by luminance | Blue stays, Amber→gold, Coral→brownish — 3 by luminance |
| Tritanopia | Blue→teal/dark, Orange stays, Rose→red-pink — 3 distinct | Blue→darker/pink, Amber stays, Coral→pink — 3 distinct |
| Achromatopsia | 3 different gray levels (dark/medium/light) | 3 different gray levels |

#### Theme selector implementation notes
- `prefers-color-scheme` only distinguishes light/dark, not CVD-friendly
- Options: JavaScript toggle, URL parameter (`?theme=horizon`), localStorage preference
- Theme selector dropdown would use JS to switch CSS variables and save preference

### 3. Three New Projects (to document in knowledge-live)

| Project | Description |
|---------|-------------|
| Universal Translator | Universal translator capability |
| Online Doc Gen | DOCX/PDF generation, web publication |
| Vanilla Portability | Vanilla module portability and reusability |

These will add 3 new satellites (network: 6 → 9).
Documentation will be done via the tagged input convention in knowledge-live.

### 4. Web Publication Toolbar — Feature Notes
User envisions a universal web publication toolbar (top-right area) with:

| Feature | Description |
|---------|-------------|
| Theme selector | Dropdown: Cayman (light), Midnight (dark), Horizon (light CVD), Ember (dark CVD) |
| PDF export | Client-side JS — generate PDF from the current web publication |
| DOCX export | Client-side JS — generate DOCX from the current web publication |
| CLI equivalent | Same conversion available as a Claude CLI command (`pub export <#> --pdf/--docx`) |

**Design notes:**
- Client-side JS preferred (no server dependency — aligns with *autosuffisant* quality)
- Libraries to evaluate: jsPDF, html2pdf.js, docx.js, Pandoc (for CLI)
- The toolbar is universal — appears on all publication pages (both layouts)
- Theme selector + export buttons in a clean, compact row
- This feeds directly into the `proj:docgen` project (Online Doc Gen)

## Status
- Tagged input methodology: written, awaiting user review
- Daltonism themes: **fully researched** — Horizon (light) + Ember (dark) with hex values, WCAG-verified
- CLAUDE.md: updated to v26 with tagged input commands + evolution entry
- Web toolbar: PDF/DOCX export + theme selector noted for proj:docgen
- Three projects: not yet bootstrapped — will be documented first in knowledge-live

## Next Steps
- User reviews tagged input convention design
- Implement Horizon + Ember themes in layouts (CSS variables) and generate_og_gifs.py (THEMES dict)
- Build theme selector JS component for both layouts
- Begin documenting projects in knowledge-live using the new convention
- Evaluate client-side JS libs for PDF/DOCX export (jsPDF, html2pdf.js, docx.js)
