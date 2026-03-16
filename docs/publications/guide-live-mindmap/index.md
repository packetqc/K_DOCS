---
layout: publication
title: "Live Mindmap — User Guide"
pub_id: "Guide — Live Mindmap"
version: "v1"
date: "2026-03-16"
permalink: /publications/guide-live-mindmap/
og_image: /assets/og/live-knowledge-network-en-cayman.gif
keywords: "guide, mindmap, visualization, interactive, knowledge graph"
---

# Live Mindmap — User Guide
{: #pub-title}

> **Interface**: [Live Mindmap (I5)]({{ '/interfaces/live-mindmap/' | relative_url }}) | [Full version]({{ '/publications/guide-live-mindmap/full/' | relative_url }})

**Contents**

| | |
|---|---|
| [Getting Started](#getting-started) | Open the mindmap and orient yourself |
| [Navigation](#navigation) | Pan, zoom, expand and collapse nodes |
| [Toolbar Controls](#toolbar-controls) | View modes, theme, reload, fit |
| [Node Interaction](#node-interaction) | Select, expand, Ctrl+click |
| [Real-Time Updates](#real-time-updates) | Live data from GitHub |
| [Tips](#tips) | Keyboard shortcuts and best practices |

## Getting Started

The Live Mindmap renders the K_MIND memory system as an interactive knowledge graph powered by **MindElixir v5**. Every node is a directive — architecture rules, conventions, work state, or session context — read live from the `mind_memory.md` mermaid source on GitHub.

**To open it:**
- From the **Main Navigator**: click *I5 Live Mindmap* in the left panel
- Direct URL: `/interfaces/live-mindmap/`

## Navigation

| Action | How |
|--------|-----|
| **Pan** | Click + drag on the background |
| **Zoom** | Mouse wheel scroll or pinch gesture |
| **Select** | Click any node to highlight it |
| **Expand one level** | Click the `+` toggle on a collapsed node |
| **Collapse one level** | Click the `-` toggle on an expanded node |
| **Expand all levels** | `Ctrl + Click` (or `Cmd + Click`) on the `+` toggle |

## Toolbar Controls

The control bar at the top provides:

| Button | Action |
|--------|--------|
| **Normal / Full** | View mode selector — *Normal* hides architecture/constraints branches; *Full* shows everything |
| **Theme** | Switch between Auto, Cayman, Midnight, Daltonism Light, Daltonism Dark |
| **Reload** | Re-fetch the mindmap source from GitHub (clears cache) |
| **Center** | Re-center the map without changing zoom level |
| **Fit** | Scale the entire map to fit the visible area |
| **Fullscreen** | Toggle browser fullscreen on the mindmap container |
| **?** | Open/close the built-in help panel on the right side |

## Node Interaction

- **Click a node** to select it — the node and its connections are highlighted
- **Expand/Collapse** — each parent node has a `+`/`-` toggle to reveal or hide children
- **Ctrl+Click on `+`** — recursively expands all descendant levels at once
- Nodes are **read-only** — the mindmap cannot be edited from the interface

## Real-Time Updates

The mindmap data is fetched live from the GitHub repository (`Knowledge/K_MIND/mind/mind_memory.md`). The depth configuration (`depth_config.json`) controls which branches appear in Normal mode.

- **Reload** re-fetches both files from GitHub
- Theme changes propagate instantly via BroadcastChannel — no reload needed
- The mindmap auto-fits on window resize and fullscreen toggle

## Tips

- Use **Fit** after expanding many branches to recenter the view
- In **Normal** mode, architecture and constraints are hidden to reduce noise — switch to **Full** when you need the complete picture
- The **help panel** (`?` button) remembers its open/closed state across page loads
- All 5 themes (including two daltonism-accessible variants) apply to both the page and the MindElixir canvas

---

**[Launch Live Mindmap (I5) ->]({{ '/interfaces/live-mindmap/' | relative_url }})**

*See also: [Live Mindmap — Technical Publication]({{ '/publications/live-mindmap/' | relative_url }})*
