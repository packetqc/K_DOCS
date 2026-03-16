---
layout: publication
title: "Conception Main Interface"
description: "The main web interface for navigating and interacting with the Knowledge system: three-panel navigator, five specialized interfaces, JSON-driven widget sections, and tab-based document navigation."
pub_id: "Publication #21"
version: "v2"
date: "2026-03-16"
permalink: /publications/main-interface/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "interface, navigation, web, knowledge, dashboard, navigator, tabs"
dev_banner: "Interface in development — features and layout may change between sessions."
---

# Conception Main Interface
{: #pub-title}

> **Parent publication**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Knowledge system main interface |
| [Interfaces](#interfaces) | Five specialized interfaces |
| [Navigation Architecture](#navigation-architecture) | Three-panel layout and entry points |
| [Left Panel Sections](#left-panel-sections) | JSON-driven widget sections |
| [Tab Navigation](#tab-navigation) | Multi-document tab bar |
| [Launch Interface](#launch-interface) | Open the Main Navigator (I2) |

## Target Audience

| Audience | Focus |
|----------|-------|
| **End users** | Navigation, page discovery, interaction patterns |
| **Web developers** | Three-panel layout, JSON-driven sections, tab architecture |
| **AI assistants** | Interface conventions, command entry points |

## Abstract

The Knowledge K2.0 main web interface provides a unified three-panel navigator for accessing all system interfaces, documentation, and publications. Five specialized interfaces serve distinct roles — session review, navigation, task workflow, project viewing, and live mindmap visualization. The left panel is driven by JSON configuration with 10 widget sections, the center panel hosts interfaces via iframe, and the right panel provides a tab-based document viewer with persistent state.

**[Launch Main Navigator (Interface I2) →]({{ '/interfaces/main-navigator/' | relative_url }})**

## Interfaces

| ID | Interface | Target | Role |
|----|-----------|--------|------|
| I1 | Session Review | center | Interactive session viewer with metrics and charts |
| I2 | Main Navigator | top | Three-panel hub — left widgets, center interfaces, right documents |
| I3 | Tasks Workflow | center | Task workflow viewer with stages and validation tracking |
| I4 | Project Viewer | center | Project detail viewer with board integration |
| I5 | Live Mindmap | center | Real-time mindmap visualization |

The center panel defaults dynamically to the first center-target interface by priority.

## Navigation Architecture

The Main Navigator (I2) uses a three-panel layout:

```
┌──────────────────────────────────────────────────────┐
│                   Main Navigator                     │
├──────────┬──────────────────┬────────────────────────┤
│  LEFT    │     CENTER       │        RIGHT           │
│          │                  │  ┌──┬──┬──┬──┐         │
│ JSON-    │  Interfaces      │  │T1│T2│T3│T4│ Tab bar │
│ driven   │  via iframe      │  ├──┴──┴──┴──┤         │
│ widget   │                  │  │           │         │
│ sections │  (I1,I3,I4,I5)   │  │ Document  │         │
│          │                  │  │ viewer    │         │
│ 10       │                  │  │           │         │
│ sections │                  │  │           │         │
├──────────┴──────────────────┴────────────────────────┤
│              Bilingual (EN/FR)                       │
└──────────────────────────────────────────────────────┘
```

Each interface card in the left panel includes an info button that opens its user guide as a tab in the right panel.

## Left Panel Sections

10 JSON-driven widget sections with UPPERCASE card labels, hover translateX(3px), and accent border styling:

| Section | Content |
|---------|---------|
| Interfaces | Links to I1–I5 with info buttons |
| Documentation | Flat card links to user guides |
| Essentials | Core system references |
| Commands | Available slash commands |
| Methodologies | Process and workflow docs |
| Hubs | Hub page links (Profile, Publications, Projects) |
| Profile | Resume, full profile, recommendations |
| Publications | All publication links |
| Stories | Success stories collection |
| Configurations | System configuration references |

## Tab Navigation

The right content panel provides multi-document navigation:

- **Tab bar** at top of right panel for switching between open documents
- **localStorage persistence** — tabs survive page reloads and session changes
- **URL dedup** — opening an already-open document activates its existing tab
- **Soft cap of 12 tabs** — oldest tab auto-closed when limit reached

## Launch Interface

**[Open Main Navigator (Interface I2) →]({{ '/interfaces/main-navigator/' | relative_url }})** — Three-panel navigation with inline content viewer.

**[Open Session Review (Interface I1) →]({{ '/interfaces/session-review/' | relative_url }})** — Interactive session viewer with metrics and charts.

**[Open Tasks Workflow (Interface I3) →]({{ '/interfaces/task-workflow/' | relative_url }})** — Task workflow viewer with stages and validation tracking.

**[Open Project Viewer (Interface I4) →]({{ '/interfaces/project-viewer/' | relative_url }})** — Project detail viewer with board integration.

[All interfaces →]({{ '/interfaces/' | relative_url }})

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — the system this interface serves |
| 17 | [Web Production Pipeline]({{ '/publications/web-production-pipeline/' | relative_url }}) | Pipeline — how interface pages are built |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
*Deployment: Custom GitHub Actions workflow (static HTML, no Jekyll)*
