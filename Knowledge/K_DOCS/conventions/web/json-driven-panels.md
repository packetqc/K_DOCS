# JSON-Driven Panel Sections — Convention

## Principle

Navigator left-panel widget sections are **data-driven**: each section loads its content from a JSON file in `docs/data/` at runtime. No hardcoded item lists in the navigator JS.

## JSON File Structure

Each section has a JSON file at `docs/data/<section>.json`:

```json
{
  "generated_by": "Knowledge/K_DOCS/scripts/build_<section>.py",
  "items": [
    {
      "title": "English title",
      "title_fr": "French title",
      "module": "K_DOCS",
      "path": "https://raw.githubusercontent.com/packetqc/knowledge/main/...",
      "priority": 1
    }
  ]
}
```

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | English display label |
| `title_fr` | string | French display label (empty string = fallback to EN) |
| `priority` | number | Sort order (lower = higher in list) |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `module` | string | Grouping key (renders as collapsible sub-details) |
| `path` | string | Raw GitHub URL or viewer-relative path |
| `file` | string | Source filename for traceability |

## Build Script Pattern

Each JSON has a companion build script at `Knowledge/K_DOCS/scripts/build_<section>.py`:

- Scans source directories for content
- Reads titles from markdown `# headings`
- Assigns incremental priority
- **Preserves manual edits** on re-run (priority, title_fr)
- Writes to `docs/data/<section>.json`

## Navigator Widget Declaration

In the navigator's `WIDGETS` array, a JSON-driven section is declared with a single `json` property:

```javascript
{ id:'<section>', title: t.<section>, open:false, json:'data/<section>.json' }
```

## Navigator Rendering

The `w.json` handler in the navigator:

1. Fetches the JSON file relative to `BASE`
2. Sorts items by `priority`
3. Groups by `module` (if present) into collapsible `<details>` sub-sections
4. Picks `title_fr` or `title` based on current `LANG`
5. Creates links targeting `content-frame` via the viewer's `?doc=` parameter

## Viewer Support

The viewer (`docs/index.html`) has a **direct doc fallback**: when `?doc=` contains a path not in the registered `DOCS` array, it calls `loadDocument()` directly. This enables raw GitHub URLs and any external markdown path.

## Reference Implementation

- JSON: `docs/data/methodologies.json`
- Script: `Knowledge/K_DOCS/scripts/build_methodologies.py`
- Navigator: `docs/interfaces/main-navigator/index.md` (widget declaration + `w.json` renderer)
- Viewer fallback: `docs/index.html` (directDoc handling)
