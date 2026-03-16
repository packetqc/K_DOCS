---
layout: publication
title: "Revue de sessions — Guide utilisateur"
description: "Comment utiliser l'interface Revue de sessions : naviguer les sessions, lire les metriques, explorer les graphiques et la chronologie, et exporter les rapports."
pub_id: "Guide — Session Review"
version: "v1"
date: "2026-03-16"
permalink: /fr/publications/guide-session-review/
og_image: /assets/og/session-review-fr-cayman.gif
keywords: "guide, session, revue, metriques, graphiques, chronologie, guide utilisateur"
---

# Session Review — User Guide
{: #pub-title}

> **Full guide**: [Session Review — User Guide (Full)]({{ '/publications/guide-session-review/full/' | relative_url }})

**Contents**

| | |
|---|---|
| [What Is Session Review?](#what-is-session-review) | Purpose and overview |
| [Getting Started](#getting-started) | How to open and navigate |
| [Key Features](#key-features) | Metrics, charts, timeline, deliveries |
| [Tips](#tips) | Get the most out of the interface |

## What Is Session Review?

Session Review (I1) is the interactive dashboard for exploring work sessions. Each session captures what was accomplished, how long it took, what was delivered, and what was learned. The interface turns raw session data into a structured, visual report you can browse section by section.

**[Open Session Review (I1) &rarr;]({{ '/interfaces/session-review/' | relative_url }})**

## Getting Started

1. **Select a session** from the dropdown at the top — sessions are grouped by date and prefixed with the start time
2. **Choose a view** using the second dropdown: All sections, Tasks Overview, Metrics Dashboard, or Timeline
3. **Scroll** through the report — each section is displayed in sequence

The "All Sessions" view (no session selected) shows summary cards for every available session, giving you a quick overview of recent activity.

## Key Features

| Feature | What It Shows |
|---------|---------------|
| **Summary** | Session title, date, branch, type, and a brief description of what was accomplished |
| **Metrics** | Pull requests, files modified, lines changed, commits, tasks, and lessons — broken down by category |
| **Charts** | Pie charts for scope distribution, metrics breakdown, code lines, and time allocation |
| **Time Compilation** | Active time, calendar time, and time blocks categorized as Machine / Human / Inactive |
| **Deliveries** | List of pull requests with line counts, file counts, and direct GitHub links |
| **Lessons Learned** | Methodology insights, patterns discovered, and pitfalls encountered |

## Tips

- **Emoji indicators** in the dropdown tell you what data is available: deliveries, notes, or linked GitHub issues
- **Section filter** lets you focus on just the metrics or timeline without scrolling through the full report
- Sessions are displayed in your **local timezone** — a session worked on in the evening will appear under today's date, not tomorrow's UTC date
- Only sessions from **v52+** (2026-02-27 onwards) appear — earlier sessions lack the structured data this viewer requires

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
