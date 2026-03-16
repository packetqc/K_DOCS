---
layout: publication
title: "Conception Main Interface — Full"
description: "Complete reference for the Knowledge 2.0 main interface: Main Navigator three-panel architecture, tab bar system, JSON-driven widget sections, five interactive interfaces, bilingual system, theme engine, and deployment pipeline."
pub_id: "Publication #21 — Full"
version: "v2"
date: "2026-03-16"
permalink: /publications/main-interface/full/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "interface, navigation, web, knowledge, dashboard, navigator, tabs, widgets, complete"
dev_banner: "Interface in development — features and layout may change between sessions."
---

# Conception Main Interface — Complete Documentation
{: #pub-title}

> **Summary**: [Publication #21]({{ '/publications/main-interface/' | relative_url }}) | **Parent**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }})

**Contents**

| | |
|---|---|
| [Navigation Architecture](#navigation-architecture) | Hub hierarchy and five interfaces |
| [Navigator Layout](#navigator-layout) | Three-panel grid: left, center, right |
| [Tab Bar System](#tab-bar-system) | Browser-like tabs with persistence |
| [JSON-Driven Sections](#json-driven-sections) | 10 widget sections from sections.json |
| [Widget Styling](#widget-styling) | Card design, sub-groups, hover effects |
| [Guide System](#guide-system) | Per-interface info buttons and postMessage |
| [Bilingual System](#bilingual-system) | EN/FR switching across all panels |
| [Theme System](#theme-system) | Four themes with CSS variables |
| [Deployment](#deployment) | GitHub Actions workflow |
| [Quality Gates](#quality-gates) | Validation and concordance checks |

---

## Navigation Architecture

The Knowledge 2.0 web platform provides five interactive interfaces accessible through the Main Navigator (I2):

| ID | Interface | Panel | Description |
|----|-----------|-------|-------------|
| I1 | Session Review | center | Interactive session viewer with metrics, charts, time tracking |
| I2 | Main Navigator | top | Three-panel browser: widget directory, content viewer, tab bar |
| I3 | Tasks Workflow | center | Task lifecycle viewer with 8-stage kanban and validation |
| I4 | Project Viewer | center | Project dashboard with boards, milestones, status tracking |
| I5 | Live Mindmap | center | Real-time mindmap visualization of the knowledge graph |

Interfaces use `page_type: interface` in front matter. They share the `publication` layout but with guards that hide the webcard header and language bar. The Main Navigator (I2) acts as the top-level shell — it embeds the other four interfaces in its center panel via iframe.

### Page Hierarchy

```
Landing (/)
    ├── Profile Hub (/profile/)
    │   ├── Resume (/profile/resume/)
    │   ├── Full (/profile/full/)
    │   └── Recommendation (/profile/recommendation/)
    ├── Publications Index (/publications/)
    │   └── #N Publication (/publications/<slug>/)
    │       └── Full (/publications/<slug>/full/)
    ├── Projects Hub (/projects/)
    └── Interfaces Hub (/interfaces/)
        ├── Main Navigator (/interfaces/main-navigator/)  ← I2
        ├── Session Review (/interfaces/session-review/)   ← I1
        ├── Tasks Workflow (/interfaces/task-workflow/)     ← I3
        ├── Project Viewer (/interfaces/project-viewer/)   ← I4
        └── Live Mindmap (/interfaces/live-mindmap/)       ← I5
```

Each page exists in both EN and FR. Auto-generated language bars from the permalink enable seamless switching.

---

## Navigator Layout

The Main Navigator (I2) uses a CSS Grid three-panel layout that fills the entire viewport:

<div class="three-col">
<div class="col" markdown="1">

### Left Panel — Widget Directory

The left panel is a scrollable sidebar (220px default) containing JSON-driven widget sections.

#### Structure
- Sections rendered from `sections.json` registry
- Each section is a collapsible `<details>` element
- Collapse state persisted to localStorage
- Sections ordered by `priority` (ascending)
- Interface links route to center iframe
- Document links route to right panel

#### Resize
- Draggable divider between left and center
- Grid template columns updated on drag
- `dragging` class disables CSS transitions

</div>
<div class="col" markdown="1">

### Center Panel — Interface Viewer

The center panel is a full-height iframe that hosts the active interface.

#### Behavior
- Default: loads first center-target interface by priority from `interfaces.json`
- Interface clicks in left panel swap the iframe `src`
- Standalone mode when Navigator not loaded directly
- Flex-fills remaining vertical space below toolbar chrome

#### Chrome Elements (above grid)
- Language bar (EN/FR toggle)
- Dev banner (conditional from front matter)
- Version banner (pub_id, version, date)
- Export toolbar
- Page title heading (compact 1.4rem)

</div>
<div class="col" markdown="1">

### Right Panel — Document Viewer

The right panel hosts a tab bar and a document viewer iframe for publications and documentation.

#### Behavior
- Starts collapsed (0px width)
- Opens when a document link is clicked in left panel
- Draggable divider between center and right
- Loads documents via iframe

#### Tab Bar
- Browser-like tabs along the top of the right panel
- Each tab shows document title + close button
- Active tab highlighted with accent color
- Clicking a tab switches the right iframe src
- See [Tab Bar System](#tab-bar-system) for full details

</div>
</div>

---

## Tab Bar System

The right panel features a browser-like tab bar for managing multiple open documents simultaneously.

<div class="three-col">
<div class="col" markdown="1">

### Tab Lifecycle

#### Creation
- Document link click in left panel creates a tab
- `tabNavigating` flag suppresses duplicate tab creation during programmatic navigation
- Iframe `load` event creates tabs for user-initiated navigation only

#### Deduplication
- `normUrl(url)` normalizes URLs before comparison
- Strips trailing slashes, resolves to origin + pathname
- If tab with same normalized URL exists, activates it instead

</div>
<div class="col" markdown="1">

### Persistence

#### localStorage
- Tabs array serialized to `navigator-tabs` key
- Restored on page load
- Active tab ID preserved across sessions
- Tab order maintained

#### Soft Cap
- `TAB_MAX = 12` — soft cap on open tabs
- When exceeded, oldest inactive tab is closed
- Active tab is never auto-closed
- User can always close tabs manually via close button

</div>
<div class="col" markdown="1">

### Navigation Flags

#### `tabNavigating`
- Set to `true` before programmatic iframe src changes
- Prevents the iframe `load` handler from creating a duplicate tab
- Reset to `false` once the load event fires
- Ensures tab bar stays in sync with actual navigation

#### Tab Switching
- Click tab → set `tabNavigating = true` → set iframe src
- Load handler sees flag → updates title only, no new tab
- User clicks link in iframe → flag is false → new tab created

</div>
</div>

---

## JSON-Driven Sections

The left panel renders 10 widget sections, each backed by a JSON data file. The section registry is fetched at runtime from `sections.json` with a hardcoded fallback.

### Section Registry

| Priority | Section ID | JSON Source | Content |
|----------|-----------|-------------|---------|
| 1 | `interfaces` | `data/interfaces.json` | 5 interfaces with center/right routing |
| 2 | `documentation` | `data/documentation.json` | Flat card links to publication summaries |
| 3 | `essentials` | `data/essentials.json` | Quick-access essential documents |
| 4 | `commands` | `data/commands.json` | CLI command reference |
| 5 | `methodologies` | `data/methodologies.json` | Methodology guides |
| 6 | `hubs` | `data/hubs.json` | Hub page links (profile, projects, etc.) |
| 7 | `profile` | `data/profile.json` | Author profile links |
| 8 | `publications` | `data/publications.json` | Full publication index |
| 9 | `stories` | `data/stories.json` | Success stories |
| 10 | `configurations` | `data/configurations.json` | System configuration links |

<div class="three-col">
<div class="col" markdown="1">

### Registry Fetch

#### Runtime Loading
- `SECTIONS_URL` points to raw GitHub content
- `fetch()` loads and parses sections.json
- On success: builds widgets from registry
- On failure: falls back to `FALLBACK_WIDGETS` hardcoded array

#### Fallback
- Complete widget list embedded in JS
- Identical structure to sections.json
- Guarantees the navigator works offline

</div>
<div class="col" markdown="1">

### Section Rendering

#### Interfaces Section
- Each interface rendered as a row with link + target
- `center` target: loads in center iframe
- `right` target: opens in right panel tab
- Each row includes an info button (see [Guide System](#guide-system))

#### Documentation Section
- Flat card links (same style as essentials)
- Each item links to a publication summary page
- No sub-groups — simple card list

</div>
<div class="col" markdown="1">

### Collapse State

#### localStorage Persistence
- Each section's open/closed state saved
- Key: `navigator-widgets`
- Restored on page load
- Toggle updates storage immediately
- Default: first 3 sections open

#### Dynamic Default Center
- On load, the first interface with `center` target and lowest priority number becomes the default center iframe content
- Driven by `interfaces.json` data

</div>
</div>

---

## Widget Styling

Widget cards follow a consistent visual language across all sections.

<div class="three-col">
<div class="col" markdown="1">

### Card Design

#### Text Treatment
- Labels in **UPPERCASE** (`text-transform: uppercase`)
- Small font size for density
- Truncated with ellipsis on overflow

#### Colors
- Background: `var(--code-bg)` — theme-aware code background
- Text: inherits from theme
- Border-left: 2px solid transparent (default)

</div>
<div class="col" markdown="1">

### Hover Effects

#### Interaction States
- Hover: `translateX(3px)` — subtle rightward shift
- Hover: accent-colored left border appears
- Hover: `box-shadow` adds depth
- Transition: 0.15s for background, border-color, transform, box-shadow
- Active state: slightly different accent shade

</div>
<div class="col" markdown="1">

### Sub-Groups

#### Bordered Cards
- Sections with sub-categories use bordered card containers
- Visual grouping with border and padding
- Group title as compact header

#### Collapsible Details
- Each section wrapped in `<details>` element
- `<summary>` shows section title with item count
- Arrow indicator for expand/collapse
- Smooth transition on toggle

</div>
</div>

---

## Guide System

Each interface in the left panel and a standalone toolbar include an info button that links to the interface's full documentation.

<div class="three-col">
<div class="col" markdown="1">

### Left Panel Buttons

#### Per-Interface Row
- Each interface row has a link (name) and an info button
- Info button displays as a small circled icon
- Links to `/publications/<pub-slug>/full/`
- Uses `vru()` (view-relative URL) for correct base path

#### Tooltip
- `title` attribute: "User Guide" (EN) / "Guide utilisateur" (FR)
- Language-aware via `LANG` variable

</div>
<div class="col" markdown="1">

### Standalone Toolbar

#### Export Bar Integration
- Info button also appears in the navigator's own toolbar
- Same link target as the left panel button
- Consistent styling with other toolbar actions

</div>
<div class="col" markdown="1">

### postMessage Integration

#### From Embedded Interfaces
- Center-frame interfaces (I1, I3, I4, I5) can send `postMessage` to the parent navigator
- Navigator listens for `message` events on `window`
- Used for: opening documents in right panel, navigation requests
- Enables child interfaces to drive tab creation and document viewing without direct DOM access

</div>
</div>

---

## Bilingual System

Every page in the Knowledge platform has an EN/FR mirror. The Navigator manages language across all three panels.

<div class="three-col">
<div class="col" markdown="1">

### Language Switching

#### URL Transformation
- `stripLang(url)` — removes `/fr/` prefix or `&lang=fr` parameter
- `applyLang(url)` — adds `/fr/` prefix or `&lang=fr` parameter when `LANG === 'fr'`
- Applied to all iframe src changes

#### State Variable
- `LANG` — current language (`'en'` or `'fr'`)
- Detected from URL on load
- Updated on language bar toggle
- All widget labels switch dynamically

</div>
<div class="col" markdown="1">

### Content Mirrors

#### Front Matter
- Matching fields across EN/FR variants
- `permalink` + `permalink_fr` in interface pages
- Identical structure in both languages

#### Widget Labels
- JSON data files contain bilingual labels
- Section titles switch based on `LANG`
- Item labels switch based on `LANG`
- No duplicate templates — single body, runtime i18n

</div>
<div class="col" markdown="1">

### Cross-Panel Sync

#### Language Bar
- Auto-generated from permalink
- Single toggle switches all panels
- Left panel re-renders widget labels
- Center iframe URL transformed via `applyLang()`
- Right panel tabs URLs transformed
- Tab persistence stores language-neutral URLs

#### `normalize` Checks
- Mirror exists for each page
- Links point to correct mirror
- Front matter fields match

</div>
</div>

---

## Theme System

The platform supports four visual themes, all driven by CSS custom properties.

<div class="three-col">
<div class="col" markdown="1">

### Available Themes

| Theme | Type | Description |
|-------|------|-------------|
| Accessible Light | Light | Default. Daltonism-safe palette |
| Accessible Dark | Dark | Auto OS dark mode detection |
| Cayman | Light | Classic blue/white GitHub style |
| Midnight | Dark | Navy/indigo dark theme |

</div>
<div class="col" markdown="1">

### CSS Variables

#### Core Variables
- `--bg` — page background
- `--text` — body text color
- `--accent` — links, active elements
- `--border` — panel dividers, card borders
- `--code-bg` — widget card backgrounds
- `--col-alt` — alternating row color
- `--muted` — secondary text

#### Application
- All components reference variables, never raw colors
- Theme switch updates root variables
- Iframes inherit parent theme via query param or CSS

</div>
<div class="col" markdown="1">

### Selection & Persistence

#### Theme Selector
- Available in export toolbar
- Dropdown with 4 options
- Selection stored in localStorage
- Applied on page load before render

#### OS Detection
- `prefers-color-scheme: dark` media query
- Accessible Dark auto-activates in dark OS
- User selection overrides OS default
- Webcards use `<picture>` with `prefers-color-scheme` for social cards

</div>
</div>

---

## Deployment

<div class="three-col">
<div class="col" markdown="1">

### GitHub Actions Workflow

#### Build Pipeline
- Push to default branch triggers workflow
- GitHub Actions builds static HTML
- Deployed to GitHub Pages
- No Jekyll legacy — direct static deployment

#### Repository
- Source: `packetqc/knowledge`
- Pages branch: auto-managed by Actions
- Assets committed to `docs/` directory

</div>
<div class="col" markdown="1">

### Layouts

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

### Assets

#### Webcards
- Located in `docs/assets/og/`
- Generated by `generate_og_gifs.py`
- Animated GIF 1200x630
- 256-color optimized palette
- Dual theme variants (Cayman + Midnight)
- Dual language variants (EN + FR)

#### Interface Pages
- `page_type: interface` front matter
- Guards hide webcard header and language bar
- Full viewport mode with flex column layout

</div>
</div>

---

## Quality Gates

<div class="three-col">
<div class="col" markdown="1">

### Structural Validation

- `normalize` — structural concordance across EN/FR mirrors
- `pub check` — publication front matter and link validation
- `docs check` — per-page structure and content validation

</div>
<div class="col" markdown="1">

### URL Conformity

- `weblinks --admin` — URL conformity across all pages
- `normUrl()` deduplication in tab bar
- Language-neutral URL storage in localStorage

</div>
<div class="col" markdown="1">

### Interface Testing

- Tab persistence round-trip verification
- Language switch preserves state
- Theme switch preserves state
- postMessage integration between parent and child frames
- Collapse state persistence for widget sections

</div>
</div>

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — the system this interface serves |
| 17 | [Web Production Pipeline]({{ '/publications/web-production-pipeline/' | relative_url }}) | Pipeline — how interface pages are built |
| 22 | [Visual Documentation]({{ '/publications/visual-documentation/' | relative_url }}) | Visual — webcard and diagram generation |
| 23 | [Webcards & Social Sharing]({{ '/publications/webcards-social-sharing/' | relative_url }}) | Social — OG image generation for sharing |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
