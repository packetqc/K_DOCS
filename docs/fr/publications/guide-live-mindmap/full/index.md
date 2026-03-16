---
layout: publication
title: "Mindmap vivant — Guide utilisateur (Complet)"
pub_id: "Guide — Live Mindmap (Full)"
version: "v1"
date: "2026-03-16"
lang: fr
permalink: /fr/publications/guide-live-mindmap/full/
og_image: /assets/og/live-knowledge-network-fr-cayman.gif
keywords: "guide, mindmap, visualisation, interactif, graphe de connaissances, complet"
---

# Live Mindmap — User Guide
{: #pub-title}

> **Interface**: [Live Mindmap (I5)]({{ '/interfaces/live-mindmap/' | relative_url }}) | [Summary version]({{ '/publications/guide-live-mindmap/' | relative_url }})

## Table of Contents

| | |
|---|---|
| [Getting Started](#getting-started) | Open and orient yourself |
| [Navigation — Pan & Zoom](#navigation--pan--zoom) | Move around the graph |
| [Node Interaction](#node-interaction) | Select, expand, collapse |
| [Toolbar Controls](#toolbar-controls) | View modes, theme, reload |
| [MindElixir Controls](#mindelixir-controls) | Engine-level behaviors |
| [View Modes](#view-modes) | Normal vs Full |
| [Theme System](#theme-system) | 5 themes with accessibility |
| [Real-Time Data Pipeline](#real-time-data-pipeline) | GitHub fetch and caching |
| [Help Panel](#help-panel) | Built-in contextual help |
| [Fullscreen Mode](#fullscreen-mode) | Immersive viewing |
| [Node Groups Reference](#node-groups-reference) | What each branch means |
| [Troubleshooting](#troubleshooting) | Common issues and fixes |

## Getting Started

The Live Mindmap (I5) is an interactive visualization of the K_MIND memory system. Powered by **MindElixir v5.9.3**, it parses the mermaid mindmap from `mind_memory.md`, converts it to a navigable tree, and renders it in real-time with theme-aware colors.

**Opening the interface:**
- From the **Main Navigator** (I2): click *I5 Live Mindmap* in the Interfaces section
- Direct URL: `/interfaces/live-mindmap/`
- The interface loads in the center panel of the navigator, or standalone

On load, the mindmap fetches data from GitHub, applies the depth configuration, converts the mermaid syntax to MindElixir format, and renders the tree with top-level branches collapsed.

## Navigation — Pan & Zoom

| Action | How |
|--------|-----|
| **Pan** | Click + drag on the background (empty area) |
| **Zoom in** | Scroll wheel up, or pinch out |
| **Zoom out** | Scroll wheel down, or pinch in |
| **Center without zoom** | Click the **Center** toolbar button |
| **Fit entire map** | Click the **Fit** toolbar button |

The map automatically fits to the container on first load (after a 200ms render delay) and re-fits on window resize or fullscreen toggle.

## Node Interaction

**Selecting nodes:**
- Click any node to select it — the node is visually highlighted
- Nodes are read-only; the interface does not allow editing

**Expanding and collapsing:**
- Each parent node displays a `+` or `-` toggle icon
- Click `+` to expand one level of children
- Click `-` to collapse that level
- **Ctrl+Click** (or **Cmd+Click** on macOS) on `+` to recursively expand all descendant levels at once

When using Ctrl+Click expand-all, the interface resets all descendant expanded states first, then lets MindElixir handle the full expansion — this prevents partial expand issues.

**What happens on load:**
- All top-level group nodes start **collapsed** (at depth >= 1)
- You progressively reveal branches by clicking `+` toggles

## Toolbar Controls

The control bar at the top of the interface:

| Control | Type | Action |
|---------|------|--------|
| **View selector** | Dropdown | Switch between *Normal* and *Full* mode |
| **Theme selector** | Dropdown | Choose from Auto, Cayman, Midnight, Daltonism Light, Daltonism Dark |
| **Reload** | Button | Re-fetch mindmap and config from GitHub (clears cache) |
| **Center** | Button | Re-center the map at current zoom level |
| **Fit** | Button | Scale the entire tree to fit the visible container |
| **Fullscreen** | Button | Toggle browser fullscreen on the mindmap container |
| **?** | Button | Toggle the help panel (right side) |
| **Status** | Text | Shows current mode, node count, and last load time |

## MindElixir Controls

The interface uses MindElixir v5.9.3 with these configuration choices:

| Setting | Value | Meaning |
|---------|-------|---------|
| `direction` | `SIDE` | Nodes branch left and right from the root |
| `editable` | `false` | No node editing allowed |
| `keypress` | `false` | Keyboard shortcuts disabled (prevents conflicts) |
| `toolBar` | `false` | Built-in MindElixir toolbar hidden (custom toolbar used instead) |
| `contextMenu` | `false` | Right-click menu disabled |
| `allowUndo` | `false` | No undo stack |

These settings make the mindmap a pure read-only viewer optimized for exploration.

## View Modes

**Normal mode** (default):
- Fetches the full mindmap but applies the `omit` filter from `depth_config.json`
- By default, `architecture` and `constraints` branches are hidden
- Focuses on work-relevant nodes: conventions, work, session, documentation

**Full mode:**
- Displays all branches including architecture and constraints
- No filtering applied
- Use this when you need the complete knowledge picture

Both modes start with top-level nodes collapsed. The status bar shows the current mode and total node count.

## Theme System

Five themes are available, each defining both the page CSS variables and the MindElixir canvas colors:

| Theme | Type | Description |
|-------|------|-------------|
| **Auto** | Adaptive | Follows OS preference (prefers-color-scheme) |
| **Cayman** | Light | Blue accent on white — classic GitHub Pages look |
| **Midnight** | Dark | Blue accent on navy — low-light reading |
| **Daltonism Light** | Light | High-contrast with blue/orange — accessibility optimized |
| **Daltonism Dark** | Dark | High-contrast with blue/orange on dark — accessibility optimized |

Theme changes are:
- Applied instantly to both the page and the MindElixir canvas
- Synced across tabs via `BroadcastChannel('kdocs-theme-sync')`
- Persisted in `localStorage('kdocs-theme')`
- Received from the Main Navigator when running inside it

## Real-Time Data Pipeline

The mindmap data flows through this pipeline:

1. **Fetch** — `mind_memory.md` is fetched from the GitHub raw URL (`raw.githubusercontent.com`)
2. **Extract** — the mermaid code block is extracted via regex
3. **Filter** — in Normal mode, `depth_config.json` is applied to omit branches
4. **Convert** — the mermaid syntax is parsed into a MindElixir node tree (indentation-based hierarchy)
5. **Render** — MindElixir renders the interactive tree with the current theme
6. **Collapse** — top-level groups are collapsed programmatically
7. **Fit** — the map scales to fit the container

Both the mermaid source and the config are cached in memory after first fetch. Use the **Reload** button to clear the cache and re-fetch.

## Help Panel

Click the `?` button to toggle a side panel with contextual help:

- Navigation shortcuts (scroll, click+drag, Ctrl+Click)
- Expand/collapse instructions
- Toolbar button descriptions
- Explanation of what the mindmap represents

The panel's open/closed state is persisted in `localStorage('mindmap-help-open')` and restored on page load.

The help content is bilingual (EN/FR) — it automatically renders in the page's detected language.

## Fullscreen Mode

Click **Fullscreen** to expand the mindmap container to browser fullscreen. The map automatically re-fits on entering and exiting fullscreen.

Exit with `Esc` or by clicking the **Fullscreen** button again.

## Node Groups Reference

The root node is `knowledge`, branching into these top-level groups:

| Group | Visible in | Meaning |
|-------|-----------|---------|
| **architecture** | Full only | System design rules — how things are built |
| **constraints** | Full only | Hard limits — boundaries that must not be violated |
| **conventions** | Both | Reusable patterns — how to execute operations consistently |
| **work** | Both | Accomplished and staged results — the continuity anchor |
| **session** | Both | Current conversation context — brainstorming record |
| **documentation** | Both | Documentation structure references |

Each group contains hierarchical sub-nodes. The depth varies: work and session branches grow dynamically as sessions progress, while architecture and constraints are relatively stable.

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| "Loading..." stays forever | GitHub raw URL unreachable | Check network; try Reload |
| "No mermaid block found" | Source file format changed | Verify `mind_memory.md` contains a ` ```mermaid ` block |
| Mindmap shows but is empty | All branches filtered out | Switch to Full mode |
| Nodes overlap or unreadable | Zoom level too low | Click **Fit** or scroll to zoom in |
| Theme not applied | Cache mismatch | Hard refresh (`Ctrl+Shift+R`) |
| Slow with many nodes | 500+ visible nodes | Collapse unused branches; use Normal mode |
| Ctrl+Click expand not working | Browser intercepts Ctrl+Click | Try Cmd+Click on macOS |

---

**[Launch Live Mindmap (I5) ->]({{ '/interfaces/live-mindmap/' | relative_url }})**

*See also: [Live Mindmap — Technical Publication]({{ '/publications/live-mindmap/' | relative_url }})*

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
