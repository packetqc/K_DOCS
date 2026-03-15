---
layout: publication
title: "Conception Main Interface"
description: "The main web interface for navigating and interacting with the Knowledge system: primary entry points, navigation architecture, page hierarchy, and user interaction patterns."
pub_id: "Publication #21"
version: "v1"
date: "2026-02-27"
permalink: /publications/main-interface/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "interface, navigation, web, knowledge, dashboard"
dev_banner: "Interface in development — features and layout may change between sessions."
---

# Conception Main Interface
{: #pub-title}

> **Parent publication**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Knowledge system main interface |
| [Navigation Architecture](#navigation-architecture) | Page hierarchy and entry points |
| [Launch Interface](#launch-interface) | Open the Main Navigator (I2) |

## Target Audience

| Audience | Focus |
|----------|-------|
| **End users** | Navigation, page discovery, interaction patterns |
| **Web developers** | Page hierarchy, layout integration, hub architecture |
| **AI assistants** | Interface conventions, command entry points |

## Abstract

The main web interface for navigating and interacting with the Knowledge system. Documents the primary entry points, navigation architecture, page hierarchy, and user interaction patterns that form the system's web presence on GitHub Pages.

**[Launch Main Navigator (Interface I2) →]({{ '/interfaces/main-navigator/' | relative_url }})**

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

Each page exists in both EN and FR with language bar navigation.

## Launch Interface

**[Open Main Navigator (Interface I2) →]({{ '/interfaces/main-navigator/' | relative_url }})** — Three-panel navigation with inline content viewer.

**[Open Session Review (Interface I1) →]({{ '/interfaces/session-review/' | relative_url }})** — Interactive session viewer with metrics and charts.

**[Open Tasks Workflow (Interface I3) →]({{ '/interfaces/task-workflow/' | relative_url }})** — Task workflow viewer with 8 stages and validation tracking.

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
