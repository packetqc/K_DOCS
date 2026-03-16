# JSON-Driven Panel Sections — Convention

## Principle

Navigator left-panel widget sections are **data-driven**: each section loads its content from a JSON file in `docs/data/` at runtime. No hardcoded item lists in the navigator JS. All translations live in the JSON files.

## JSON File Structure

Each section has a JSON file at `docs/data/<section>.json`:

```json
{
  "section": "<section-type>",
  "title": "English Title",
  "title_fr": "French Title",
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
| `open` | boolean | Default expanded state (overridden by localStorage) |
| `items` | array | Active items to display |
| `removed` | array | Excluded items (same structure as items, preserved by build scripts) |

### Item Fields (Common)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | yes | English display label |
| `title_fr` | string | yes | French label (empty = fallback to EN) |
| `priority` | number | yes | Sort order (lower = higher in list) |

### Item Fields (Per Section Type)

| Field | Type | Used By | Description |
|-------|------|---------|-------------|
| `href` | string | interfaces, essentials, hubs, profile, stories | Page path relative to site root |
| `target` | string | interfaces | `"center"`, `"top"`, or `"right"` (default) |
| `module` | string | methodologies, configurations | Grouping key for collapsible sub-details |
| `path` | string | methodologies, configurations | Raw GitHub URL for viewer `?doc=` |
| `slug` | string | publications | Publication directory slug |
| `number` | string | publications | Publication number (e.g. `"#24"`) |
| `extra` | array | publications | Additional sub-links `[{title, title_fr, href}]` |
| `group` / `group_fr` | string | commands | Command group label EN/FR |
| `pub` | string | commands | Publication path for command links |
| `cmds` | array | commands | Command strings to display |

## Section Types

| Type | Rendering | Grouping | Composite View |
|------|-----------|----------|----------------|
| `interfaces` | Links with target routing (center/top/right) | — | — |
| `essentials` | Simple links | — | — |
| `commands` | Grouped commands with pub link + cmd spans | By `group` | — |
| `methodologies` | Links via viewer `?doc=` | By `module` | — |
| `configurations` | Links via viewer `?doc=` (JSON rendered as tables) | By `module` | "View All" composite |
| `hubs` | Simple links | — | — |
| `profile` | Simple links | — | — |
| `publications` | Summary + Full sub-links per pub | By publication | — |
| `stories` | Simple links | — | — |

## Item Removal

To remove an item without losing history:
1. Move the item from `"items"` to `"removed"` in the JSON
2. The navigator only reads `"items"` — removed items are invisible
3. Build scripts skip items whose `path` appears in `"removed"`

## Build Script Pattern

Sections with dynamic content have companion build scripts at `Knowledge/K_DOCS/scripts/build_<section>.py`:

- Scans source directories for content
- Reads titles from markdown `# headings` or JSON structure
- Assigns incremental priority
- **Preserves manual edits** on re-run (priority, title_fr)
- **Respects removed array** — never re-adds excluded items
- Writes to `docs/data/<section>.json`

Current build scripts:
- `build_methodologies.py` — scans `Knowledge/K_*/methodology/*.md`
- `build_configurations.py` — scans `Knowledge/K_*/` domain JSON files + `Knowledge/modules.json`

## JSON Rendering in Viewer

The viewer (`docs/index.html`) renders JSON files as formatted HTML tables:

- Detects `.json` extension in `loadDocument(path)`
- Top-level scalar fields → key-value table
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

```javascript
{ id:'<section>', json:'data/<section>.json' }
```

All metadata (title, open state, translations) comes from the JSON — no JS translation block needed.

## Active Sections

| # | Section | JSON File | Build Script | Items |
|---|---------|-----------|-------------|-------|
| 1 | Interfaces | `interfaces.json` | manual | 6 |
| 2 | Essentials | `essentials.json` | manual | 6 |
| 3 | Commands | `commands.json` | manual | 7 groups |
| 4 | Methodologies | `methodologies.json` | `build_methodologies.py` | 16 |
| 5 | Hubs | `hubs.json` | manual | 4 |
| 6 | Profile | `profile.json` | manual | 3 |
| 7 | Publications | `publications.json` | manual | 27 |
| 8 | Stories | `stories.json` | manual | 9 |
| 9 | Configurations | `configurations.json` | `build_configurations.py` | 20 |
