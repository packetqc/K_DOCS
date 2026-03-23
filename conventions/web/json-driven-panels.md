# JSON-Driven Panel Sections — Convention

## Principle

Navigator left-panel widget sections are **data-driven**: each section loads its content from a JSON file in `docs/data/` at runtime. The section list itself is driven by `Knowledge/sections.json` (fetched at runtime, with hardcoded fallback). No hardcoded item lists in the navigator JS. All translations and descriptions live in the JSON files.

## JSON File Structure

Each section has a JSON file at `docs/data/<section>.json`:

```json
{
  "section": "<section-type>",
  "title": "English Title",
  "title_fr": "French Title",
  "description": "English section description displayed as page companion in viewer.",
  "description_fr": "Description française affichée comme compagnon de page dans le visualiseur.",
  "open": false,
  "items": [ ... ],
  "removed": [ ... ]
}
```

### Section-Level Fields

| Field | Type | Description |
|-------|------|-------------|
| `section` | string | Section type — drives rendering logic (see Section Types) |
| `title` / `title_fr` | string | Widget header label EN/FR |
| `description` / `description_fr` | string | Section description EN/FR — rendered as introductory paragraph in viewer |
| `open` | boolean | Default expanded state (overridden by localStorage) |
| `items` | array | Active items to display |
| `removed` | array | Excluded items (same structure as items, preserved by build scripts) |

### Item Fields (Common)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | yes | English display label |
| `title_fr` | string | yes | French label (empty = fallback to EN) |
| `description` | string | no | English item description — rendered as page companion in viewer |
| `description_fr` | string | no | French item description |
| `priority` | number | yes | Sort order within module group (lower = higher in list, per-module numbering starting at 0) |

### Item Fields (Per Section Type)

| Field | Type | Used By | Description |
|-------|------|---------|-------------|
| `href` | string | interfaces, essentials, hubs, profile, stories | Page path relative to site root |
| `target` | string | interfaces | `"center"`, `"top"`, or `"right"` (default) |
| `pub` | string | interfaces | Guide publication slug — enables ℹ button linking to user guide |
| `module` | string | methodologies, configurations | Grouping key for collapsible sub-details |
| `path` | string | methodologies, configurations | Raw GitHub URL for viewer `?doc=` |
| `slug` | string | publications, documentation | Publication directory slug |
| `has_full` | boolean | documentation | Whether full doc exists (controls icon display in future) |
| `number` | string | publications | Publication number (e.g. `"#24"`) |
| `extra` | array | publications | Additional sub-links `[{title, title_fr, href}]` |
| `group` / `group_fr` | string | commands | Group label EN/FR |
| `pub` | string | commands | Publication path for command links |
| `cmds` | array | commands | Command strings to display |

## Section Types

| Type | Rendering | Grouping | Composite View |
|------|-----------|----------|----------------|
| `interfaces` | `.iface-row` with target routing + ℹ guide button | — | — |
| `documentation` | `.iface-row` with S/F icons | Flattened from `groups[]` | — |
| `essentials` | Simple links | — | — |
| `commands` | Collapsible `.pub-group` categories with `.iface-row` items inside | By `group` | — |
| `methodologies` | Collapsible `.pub-group` categories with `.iface-row` items via viewer `?doc=` | By `module` | — |
| `configurations` | Collapsible `.pub-group` categories with `.iface-row` items via viewer `?doc=` | By `module` | "View All" composite |
| `hubs` | Simple links | — | — |
| `profile` | Simple links | — | — |
| `publications` | `.iface-row` with S/F icons + extra sub-links as icon buttons | — | — |
| `stories` | Simple links | — | — |

## Item Removal

To remove an item without losing history:
1. Move the item from `"items"` to `"removed"` in the JSON
2. The navigator only reads `"items"` — removed items are invisible
3. Build scripts skip items whose `path` appears in `"removed"`

## Section Registry — `Knowledge/sections.json`

Central configuration defining which sections appear in the navigator left-panel and in what order:

```json
{
  "sections": [
    { "id": "interfaces",     "json": "data/interfaces.json",     "priority": 1 },
    { "id": "essentials",     "json": "data/essentials.json",     "priority": 2 },
    ...
  ]
}
```

The navigator fetches this at runtime via raw GitHub URL. On fetch failure, a hardcoded `FALLBACK_WIDGETS` array provides the same sections. To reorder sections, edit priorities in `sections.json`.

## Priority Numbering

Priority counters are **per module group**, not global:

- `SYSTEM` items: 0, 1, ...
- `K_DOCS` items: 0, 1, 2, ...
- `K_GITHUB` items: 0, 1, 2, ...
- Each module group restarts at 0

This avoids cascading renumbering when inserting items into a group.

## Build Script Pattern

Sections with dynamic content have companion build scripts at `Knowledge/K_DOCS/scripts/build_<section>.py`:

- Scans source directories for content
- Reads titles from markdown `# headings` or JSON structure
- Assigns per-module incremental priority (starting at 0 per group)
- **Preserves manual edits** on re-run (priority, title_fr, description, description_fr)
- **Preserves section-level descriptions** on re-run
- **Respects removed array** — never re-adds excluded items
- Writes to `docs/data/<section>.json`

Current build scripts:
- `build_methodologies.py` — scans `Knowledge/K_*/methodology/*.md`
- `build_configurations.py` — scans `Knowledge/K_*/` domain JSON files + `Knowledge/sections.json` + `Knowledge/modules.json` (SYSTEM group)

## JSON Rendering in Viewer

The viewer (`docs/index.html`) renders JSON files via `renderJsonDocument()`:

- **Smart title**: Uses `title`/`title_fr` (language-aware) as `<h1>` heading instead of raw filename
- **Description paragraph**: Renders `description`/`description_fr` as introductory `<p>` below the heading
- **Clickable links**: URLs ending in `.json` or `.md` render as in-viewer navigation links (`target="content-frame"` via `?doc=`). Other URLs open in new tabs. Site-relative paths navigate in the viewer.
- Top-level scalar fields → key-value table (title/description fields excluded — already rendered above)
- Array of objects → column-based data table
- Nested objects → sub-section tables
- Array of primitives → bullet list

## Composite View

Module-grouped sections support composite rendering via `?docs=url1|url2|...`:

- Groups with multiple JSON items show a **"View All"** / **"Tout voir"** link
- Clicking it loads all group items as one page in the viewer
- Each JSON file renders as a table section separated by `<hr>`
- Items appear in priority order

## Navigator Widget Declaration

The navigator builds widgets from `sections.json`:

```javascript
// Fetched from sections.json at runtime
{ "id": "<section>", "json": "data/<section>.json", "priority": N }
```

All metadata (title, open state, translations, descriptions) comes from the JSON data file — no JS translation block needed.

## Visual Styling Convention

All left-panel items use a widget-card look — not flat text lists:

- **UPPERCASE**: All text (section titles, sub-group summaries, item links) rendered via `text-transform: uppercase`
- **Card items**: Each item has `background: var(--code-bg)`, `border-radius: 4px`, `border-left: 2px solid transparent`
- **Hover feedback**: Items shift 3px right (`translateX(3px)`) with accent left border + box-shadow on hover
- **Sub-groups (`.pub-group`)**: Collapsible `<details>` — summary matches `.iface-row` card style (same background, hover shift, accent border). No outline border, no arrows, no underlines. Sub-items indented `0.6rem` left with `0.2rem` vertical spacing.
- **Active state**: Selected rows use `color: var(--accent)` with `background: var(--col-alt)` and accent left border — same blue accent in both light and dark themes (not inverted bg/fg)
- **No underlines**: Global rule `text-decoration: none !important` on all nav links and summaries
- **Interface rows**: `.iface-row` flex container wraps link + icon buttons, inherits card style with row-level hover
- **Transitions**: `0.12s` transform, `0.15s` background/color/border — smooth but responsive

### Row Icon System

All sections use the same `.iface-row` flex container for items that have right-side action icons. The only variation is which icons appear:

| Icon | Meaning | Data field | Target |
|------|---------|------------|--------|
| **ℹ** | User guide | `pub` | Routes through viewer: `pubUrl(pub, true)` → `?doc=<lang>/publications/<pub>/full/index.md&embed` |
| **S** | Summary | `slug` | Routes through viewer: `pubUrl(slug, false)` → `?doc=<lang>/publications/<slug>/index.md&embed` |
| **F** | Full doc | `has_full` | Routes through viewer: `pubUrl(slug, true)` → `?doc=<lang>/publications/<slug>/full/index.md&embed` |

- All S/F/ℹ buttons use `target="content-frame"` attribute (not `data-target`) so the navigator click handler intercepts them and opens in the tab bar
- Icons are **conditional** — only rendered when the corresponding data field exists/is true
- Row click (on label, not icon) opens the default target (summary for docs, center iframe for interfaces)
- Icon styling: `.iface-pub-btn` — small muted text, hover accent color, same height as row
- Sections without icons (essentials, hubs, profile, stories) use plain `makeLink()` rows
- **pubUrl helper**: `pubUrl(slug, full)` builds viewer-routed URLs with language prefix, avoiding direct `.md` file access (`.nojekyll` sites don't serve `.md` as HTML)

### ℹ Guide Button

Interfaces with a `pub` field get an ℹ button in the navigator left panel (opens guide as tab in content panel) and in their standalone toolbar (postMessage to navigator or new browser tab).

### Tab Bar

The content panel (right) has a tab bar for multi-document navigation:

- Tabs created on left-panel clicks, ℹ button clicks, in-iframe navigation, and postMessage from center-frame
- Persisted in `localStorage['navigator-tabs']` with `{id, title, url}` entries
- URL dedup via `normUrl()`, soft cap 12 tabs, `tabNavigating` flag prevents double creation

### Default Center Panel

The default center-frame URL is resolved dynamically from the first center-target interface in `interfaces.json` (by priority). Saved state in localStorage takes precedence on subsequent loads.

## Active Sections

| # | Section | JSON File | Build Script | Items |
|---|---------|-----------|-------------|-------|
| 1 | Interfaces | `interfaces.json` | manual | 5 |
| 2 | Documentation | `documentation.json` | manual | 6 guides (flat links) |
| 3 | Essentials | `essentials.json` | manual | 6 |
| 4 | Commands | `commands.json` | manual | 7 groups |
| 5 | Methodologies | `methodologies.json` | `build_methodologies.py` | 16 |
| 6 | Hubs | `hubs.json` | manual | 4 |
| 7 | Profile | `profile.json` | manual | 3 |
| 8 | Publications | `publications.json` | manual | 27 |
| 9 | Stories | `stories.json` | manual | 9 |
| 10 | Configurations | `configurations.json` | `build_configurations.py` | 21 |
