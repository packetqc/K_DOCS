---
layout: publication
title: "Live Mindmap — User Guide (Full)"
description: "Complete user guide for the Live Mindmap interface: navigation, node types, filtering, theming, and advanced features."
pub_id: "User Guide — I5 (Full)"
version: "v1"
date: "2026-03-16"
permalink: /publications/guide-live-mindmap/full/
keywords: "user guide, live mindmap, interface, tutorial, complete"
---

# Live Mindmap — User Guide
{: #pub-title}

> **Interface**: [Live Mindmap (I5)]({{ '/interfaces/live-mindmap/' | relative_url }}) | [Summary version]({{ '/publications/guide-live-mindmap/' | relative_url }})

## Table of Contents

| | |
|---|---|
| [Getting Started](#getting-started) | Open and orient yourself |
| [Navigation Controls](#navigation-controls) | Pan, zoom, select |
| [Node Groups](#node-groups) | Knowledge categories |
| [Node Details](#node-details) | What nodes contain |
| [Theme Support](#theme-support) | Light and dark rendering |
| [Data Source](#data-source) | Where the mindmap data comes from |
| [Troubleshooting](#troubleshooting) | Common issues |

## Getting Started

The Live Mindmap (I5) is an interactive visualization of the Knowledge memory system. Powered by MindElixir v5, it renders the full knowledge tree as a navigable, zoomable mindmap.

**Opening the interface:**
- From the **Main Navigator** (I2): click *I5 Live Mindmap*
- Direct URL: `/interfaces/live-mindmap/`

## Navigation Controls

| Action | How |
|--------|-----|
| **Pan** | Click and drag the background |
| **Zoom in/out** | Mouse wheel or pinch gesture |
| **Select node** | Click a node |
| **Expand/collapse** | Click the ± toggle on a node |
| **Center on node** | Double-click a node |
| **Fit to view** | Use the toolbar fit button |

## Node Groups

The root node is `knowledge`, with top-level groups:

| Group | Color | Meaning |
|-------|-------|---------|
| **architecture** | Blue | System design — how things are built |
| **constraints** | Red | Hard limits — what cannot be done |
| **conventions** | Green | Patterns — how to do things consistently |
| **work** | Orange | State — what's been accomplished |
| **session** | Purple | Context — current conversation record |
| **documentation** | Gray | Structure — documentation references |

Each group contains hierarchical sub-nodes representing specific knowledge items.

## Node Details

Each node in the mindmap corresponds to a line in the source mermaid mindmap file. Nodes represent:
- **Categories** — grouping labels (e.g., "near memory", "far memory")
- **Items** — specific knowledge entries (e.g., "live mindmap MindElixir v5")
- **States** — work status indicators (e.g., "en cours", "validation", "approbation")

## Theme Support

The mindmap automatically adapts to the site's light/dark theme:
- **Light theme**: white background, dark text, colored node highlights
- **Dark theme**: dark background, light text, adjusted node colors

Theme changes propagate in real time — no need to reload.

## Data Source

The mindmap data comes from:
- **Primary**: `Knowledge/K_MIND/files/mind/architecture-mindmap.md` — mermaid mindmap source
- **Parsed by**: MindElixir v5 renderer
- **Updated**: at the start of each session and during real-time memory maintenance

The mindmap reflects the current state of the knowledge system — nodes are added, removed, or reorganized as work progresses.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Mindmap shows empty | Check that the mindmap source file exists and is valid mermaid syntax |
| Nodes overlap or are unreadable | Use zoom controls to adjust; try fit-to-view button |
| Theme doesn't match | Hard refresh (Ctrl+Shift+R) to re-sync |
| Performance slow | Very large mindmaps (500+ nodes) may benefit from collapsing unused branches |

---

**[Launch Live Mindmap (I5) →]({{ '/interfaces/live-mindmap/' | relative_url }})**

*See also: [Live Mindmap — Technical Publication]({{ '/publications/live-mindmap/' | relative_url }})*

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
