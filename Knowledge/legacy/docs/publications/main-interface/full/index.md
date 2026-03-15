---
layout: publication
title: "Conception Main Interface — Full"
description: "Complete reference for the Knowledge system main interface: navigation architecture, page hierarchy, landing pages, publications navigation, profile integration, and user interaction patterns."
pub_id: "Publication #21 — Full"
version: "v1"
date: "2026-02-27"
permalink: /publications/main-interface/full/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "interface, navigation, web, knowledge, dashboard, complete"
dev_banner: "Interface in development — features and layout may change between sessions."
---

# Conception Main Interface — Complete Documentation
{: #pub-title}

> **Summary**: [Publication #21]({{ '/publications/main-interface/' | relative_url }}) | **Parent**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }})

**Contents**

| | |
|---|---|
| [Navigation Architecture](#navigation-architecture) | Page hierarchy and entry points |
| [Interface Components](#interface-components) | Three-column breakdown of all layers |
| [Projects Hub](#projects-hub) | Navigation by project hierarchy |

---

## Navigation Architecture

The Knowledge web presence is organized as a hierarchy of hub pages with bilingual mirrors:

```
Landing (/)
    ├── Profile Hub (/profile/)
    │   ├── Resume (/profile/resume/)
    │   └── Full (/profile/full/)
    ├── Publications Index (/publications/)
    │   └── #N Publication (/publications/<slug>/)
    │       └── Full (/publications/<slug>/full/)
    └── Projects Hub (/projects/)
```

Each page exists in both EN and FR. Auto-generated language bars from the permalink enable seamless switching. The `publication` layout drives all publication pages with version banners, export bars, cross-references, and theme selection. The `default` layout drives profile pages, landing pages, and hubs.

---

## Interface Components

<div class="three-col">
<div class="col" markdown="1">

### Landing Pages

The landing page (`/`) is the single entry point — a hub linking to all major sections.

#### EN Landing
- Profile hub link
- Publications index link
- Projects hub link
- Quick navigation cards

#### FR Landing
- Mirror structure (`/fr/`)
- Same links, French labels
- Auto-detected from permalink

#### Design Principles
- Minimal — no clutter, direct links
- Bilingual — EN/FR mirrors for every page
- Theme adaptive — respects OS preferences
- Responsive — mobile-first, scales up

</div>
<div class="col" markdown="1">

### Publications Navigation

The publications index (`/publications/`) lists all publications with status and links.

#### Per-Publication Structure
- **Summary** — `/publications/<slug>/`
- **Full** — `/publications/<slug>/full/`
- EN + FR mirrors at both levels

#### Publication Layout Features
- Version banner (pub_id, version, date)
- Export bar (PDF Letter/Legal, DOCX)
- Theme selector (4 themes)
- Language bar (EN/FR toggle)
- Cross-references section
- Keyword links

#### Webcards
- Animated OG GIF per page
- Dual theme (Cayman + Midnight)
- `<picture>` with `prefers-color-scheme`
- Social sharing uses Cayman variant

</div>
<div class="col" markdown="1">

### Profile Integration

The author profile is structured as a hub with subpages, using the `default` layout.

#### Profile Hierarchy
- **Hub** — `/profile/` — overview
- **Resume** — `/profile/resume/` — targeted CV
- **Full** — `/profile/full/` — complete bio

#### Profile Features
- Corporate webcards with photo
- Animated ring (color cycling)
- Timeline dots (career progression)
- Links to publications and projects

#### Theme System
- **Accessible Light** — default (daltonism-safe)
- **Accessible Dark** — auto OS dark mode
- **Cayman** — classic blue/white
- **Midnight** — navy/indigo dark
- Selector in export bar
- CSS variables drive all colors

</div>
</div>

---

<div class="three-col">
<div class="col" markdown="1">

### Layout Architecture

Two layouts serve all pages:

#### `publication.html`
- Full print/export stack
- CSS Paged Media (`@page`)
- Running headers/footers
- Smart TOC page break
- PDF filename sanitization
- Version banner + keywords
- Language bar + cross-refs

#### `default.html`
- No print/export features
- Profile pages, hubs, landing
- Same theme system
- Same webcard header

</div>
<div class="col" markdown="1">

### Bilingual System

Every page has an EN/FR mirror. The system enforces concordance.

#### Language Bar
- Auto-generated from permalink
- EN pages → French link
- FR pages → English link
- Hidden in print
- Uses `relative_url` filter

#### Content Mirrors
- Front matter: matching fields
- Structure: identical hierarchy
- Links: point to same-language peers
- Webcards: `-en` / `-fr` variants

#### `normalize` Checks
- Mirror exists for each page
- Links point to correct mirror
- Front matter fields match

</div>
<div class="col" markdown="1">

### Web Production

Pages are built via Jekyll on GitHub Pages with zero external dependencies.

#### Build Pipeline
- Push to default branch
- GitHub Actions triggers Jekyll
- Static HTML deployed to Pages
- Auto-refresh every 60s

#### Assets
- Webcards in `docs/assets/og/`
- Generated by `generate_og_gifs.py`
- Animated GIF 1200x630
- 256-color optimized palette

#### Quality Gates
- `normalize` — structural concordance
- `pub check` — publication validation
- `docs check` — per-page validation
- `weblinks --admin` — URL conformity

</div>
</div>

---

## Interfaces

| ID | Interface | Description | Launch |
|----|-----------|-------------|--------|
| I1 | Session Review | Interactive session viewer with metrics and charts | [Open I1 →]({{ '/interfaces/session-review/' | relative_url }}) |
| I2 | Main Navigator | Three-panel browser with inline content viewer | [Open I2 →]({{ '/interfaces/main-navigator/' | relative_url }}) |

Interfaces use `page_type: interface` in front matter. They share the `publication` layout but with guards that hide the webcard header and language bar.

---

## Projects Hub

The projects hub (`/projects/`) provides hierarchical navigation across all registered projects.

<div class="three-col">
<div class="col" markdown="1">

#### Project Types

| Type | Description |
|------|-------------|
| `core` | P0 — Knowledge System |
| `child` | Own repo, own board |
| `managed` | No repo, hosted in parent |

</div>
<div class="col" markdown="1">

#### Navigation

- Project list with P# index
- Per-project status indicators
- Links to repo, board, publications
- Cross-project references (`→P#`)

</div>
<div class="col" markdown="1">

#### Dual-Origin Links

- **Core** links — canonical, approved
- **Satellite** links — dev/staging
- Origin badge in hub
- Both valid, different origin

</div>
</div>

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — the system this interface serves |
| 17 | [Web Production Pipeline]({{ '/publications/web-production-pipeline/' | relative_url }}) | Pipeline — how interface pages are built |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
