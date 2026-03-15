---
layout: publication
title: "Story #25 — Live Mindmap Memory: From Static Diagram to Interactive Knowledge Graph"
description: "How the K_MIND mindmap evolved from a static mermaid diagram to an interactive MindElixir knowledge graph with depth filtering, theme sync, and real-time GitHub fetching."
pub_id: "Publication #11 — Story #25"
version: "v1"
date: "2026-03-15"
permalink: /publications/success-stories/story-25/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "success story, mindmap, MindElixir, interactive, knowledge graph, depth filtering, themes"
---

# Story #25 — Live Mindmap Memory: From Static Diagram to Interactive Knowledge Graph

> **Parent publication**: [#11 — Success Stories]({{ '/publications/success-stories/' | relative_url }})

---

<div class="story-section">

> *"The mindmap started as a text file rendered by mermaid. Now it's a live, interactive knowledge graph you can pan, zoom, and explore — fetched in real-time from the repository, depth-filtered by configuration, and themed to match your viewer. The mind became visible."*

<div class="story-row">
<div class="story-row-left">

**Details**

</div>
<div class="story-row-right">

| | |
|---|---|
| Date | 2026-03-15 |
| Category | 🧠 🎨 ⚙️ |
| Context | K_MIND stores its operating memory as a mermaid mindmap in `mind_memory.md`. This file is the system's subconscious — every node is a directive. But viewing it required rendering static mermaid diagrams. The goal: make the knowledge graph explorable, interactive, and always current. |
| Triggered by | Building the K2.0 publication section on "The Mindmap Memory" — the static mermaid rendering felt inadequate for explaining a living system. The mindmap needed to *be* alive. |
| Authored by | **Claude** (Anthropic, Opus 4.6) — from live session data |

</div>
</div>

## The Evolution — Three Phases

### Phase 1: Static Mermaid (Baseline)

The mindmap existed only as a mermaid code block in `mind_memory.md`. Claude rendered it via `/mind-context` skill output. Users could see it but not interact with it. No zoom, no pan, no exploration.

### Phase 2: Custom Interactive Mermaid (v2)

Built a standalone I5 interface that:
- Fetched `mind_memory.md` from GitHub in real-time
- Applied depth filtering (JS port of `mindmap_filter.py`)
- Rendered via mermaid.js with custom pan/zoom/click handlers
- Added Normal/Full view dropdown
- Click any node → breadcrumb path display

**The limitation**: All interactivity was hand-built — mouse drag for pan, wheel for zoom, touch pinch, SVG rect overlays for highlights. Hundreds of lines of custom event handling code. Fragile. No drag-and-drop. No smooth animations.

### Phase 3: MindElixir (v3) — Current

Replaced the entire custom implementation with **MindElixir v5.9.3** — a dedicated mind mapping library:

| Feature | Custom v2 | MindElixir v3 |
|---------|-----------|---------------|
| Pan | Custom mousedown/move handlers | Built-in |
| Zoom | Custom wheel + pinch handlers | Built-in with smooth animation |
| Node interaction | Custom SVG rect overlays | Built-in selection + focus |
| Touch support | Custom touchstart/move/end | Built-in |
| Theme support | None | 4 themes synced with viewer |
| Code complexity | ~400 lines custom JS | ~50 lines configuration |
| Drag-and-drop | Not possible | Built-in (disabled for viewer) |

## The Depth Filtering Pipeline

The mindmap has 140+ nodes across 6 groups. Showing everything overwhelms. The depth filtering system controls visibility:

```
mind_memory.md → depth_config.json → filterMindmap() → MindElixir data → render
```

- `default_depth: 3` — show 3 levels deep by default
- `omit: ["architecture", "constraints"]` — hide implementation details in normal mode
- `overrides: {"session/near memory": 4}` — per-branch depth control
- **Full mode**: all nodes expanded at maximum depth

The filter runs in JavaScript (ported from Python `mindmap_filter.py`), converting mermaid indented text to MindElixir's `{topic, id, children}` JSON tree.

## Theme Sync — 4 Themes

MindElixir themes map directly to the viewer's CSS variable system:

| Viewer Theme | MindElixir Mapping | Background | Root Node |
|---|---|---|---|
| Cayman | Blue palette, light | `#eff6ff` | `#1d4ed8` |
| Midnight | Blue palette, dark | `#0f172a` | `#1e40af` |
| Daltonism Light | Warm palette, light | `#faf6f1` | `#0055b3` |
| Daltonism Dark | Warm palette, dark | `#1a1a2e` | `#2a4a7a` |

The I5 interface includes a theme dropdown. Embedded instances auto-detect from the viewer's `data-theme` attribute or `prefers-color-scheme`.

## Three Deployment Points

The live mindmap renders in three locations from the same data source:

1. **I5 Interface** — Full-featured standalone page with theme dropdown, Normal/Full toggle, Center/Fit/Fullscreen controls
2. **K2.0 Publication** — Inline embed in Section 1 "The Mindmap Memory" with auto-theme
3. **Viewer Webcard** — Live preview card when `live_webcard: mindmap` is set in front matter

All three fetch from `raw.githubusercontent.com`, apply depth filtering, convert to MindElixir format, and render with theme-appropriate colors.

## What This Proves

- **Mind-first is visible**: The operating memory isn't hidden — it's a first-class interactive element
- **Library over custom**: 400 lines of fragile custom code → 50 lines of MindElixir configuration with better UX
- **Convention propagation**: Depth config, theme system, and filtering logic are shared across all three deployment points
- **Real-time by default**: Every render fetches current data from the repository — the mindmap is always live

</div>

[**Validated**]({{ '/publications/success-stories/story-25/' | relative_url }})

---
