---
layout: publication
title: "Main Navigator — User Guide (Full)"
description: "Complete user guide for the Main Navigator: panel management, widget sections, document viewer, tabs, language switching, and advanced features."
pub_id: "User Guide — I2 (Full)"
version: "v1"
date: "2026-03-16"
permalink: /publications/guide-main-navigator/full/
keywords: "user guide, main navigator, interface, tutorial, complete"
---

# Main Navigator — User Guide
{: #pub-title}

> **Interface**: [Main Navigator (I2)]({{ '/interfaces/main-navigator/' | relative_url }}) | [Summary version]({{ '/publications/guide-main-navigator/' | relative_url }})

## Table of Contents

| | |
|---|---|
| [Getting Started](#getting-started) | Open and orient yourself |
| [Three-Panel Layout](#three-panel-layout) | Left, center, right |
| [Panel Resizing](#panel-resizing) | Drag and click-to-cycle |
| [Left Panel Widgets](#left-panel-widgets) | All content sections |
| [Center Panel](#center-panel) | Interfaces and tools |
| [Right Panel & Tabs](#right-panel--tabs) | Document viewer with tab bar |
| [Language Switching](#language-switching) | EN/FR toggle |
| [Theme Support](#theme-support) | Light and dark themes |
| [State Persistence](#state-persistence) | What survives a reload |
| [Troubleshooting](#troubleshooting) | Common issues |

## Getting Started

The Main Navigator (I2) is the central hub of the Knowledge platform. It consolidates all content — interfaces, publications, guides, methodologies, configurations, and project data — into a single three-panel browser.

**Opening the navigator:**
- Direct URL: `/interfaces/main-navigator/`
- It opens as a full-page interface (replaces the current page)

## Three-Panel Layout

The navigator uses a CSS grid with 5 columns: left panel, left divider, center panel, right divider, right panel.

| Panel | Default Size | Content |
|-------|-------------|---------|
| **Left** | 220px | Widget directory |
| **Center** | Fills remaining | Interfaces (iframes) |
| **Right** | 0px (hidden) | Document viewer (iframe) |

## Panel Resizing

**Drag**: grab a divider and drag horizontally to resize adjacent panels.

**Click-to-cycle** (divider click without drag):
- **Left divider**: cycles 0px → 220px → 320px
- **Right divider**: cycles 0px → 50% → full width → 0px

The right panel auto-extends when you click a document link in the left panel.

## Left Panel Widgets

Widgets are collapsible `<details>` elements, each loading data from a JSON file. Sections include:

| Widget | Content | Opens in |
|--------|---------|----------|
| **Interfaces** | I1–I5 + documentation link | Center panel |
| **Documentation** | User guides, admin guides, quick starts | Right panel |
| **Essentials** | Key reference documents | Right panel |
| **Commands** | Grouped command reference | Right panel |
| **Methodologies** | Operational methodology files (by module) | Right panel |
| **Hubs** | Cross-reference hub pages | Right panel |
| **Profile** | Resume, recommendation, full profile | Right panel |
| **Publications** | 27 technical publications (summary + full) | Right panel |
| **Stories** | Success stories collection | Right panel |
| **Configurations** | Domain JSON config files (by module) | Right panel |

Widget open/closed states are saved to localStorage.

## Center Panel

The center panel hosts interactive interfaces via iframe:
- **Default**: Tasks Workflow (I3) loads on startup
- Click an interface in the left panel to switch
- The last-viewed interface is restored on page reload

## Right Panel & Tabs

The right panel is a document viewer with a **tab bar**:

- Every document you open creates a tab
- Click tabs to switch between documents
- Click × on a tab to close it
- Tabs persist across page reloads (localStorage)
- Maximum 12 tabs — oldest non-active tab auto-closes when exceeded

The viewer renders:
- **Markdown** with headings, tables, mermaid diagrams, and TOC
- **JSON** as formatted tables with smart titles and clickable links
- **Publications** with full chrome bar (metadata, version, authors)

## Language Switching

The navigator supports EN/FR:
- Language is detected from the URL path (`/fr/` prefix)
- Widget labels and titles switch based on `title_fr` fields in JSON data
- Document links are rewritten to match the active language

## Theme Support

The navigator inherits the site theme (light/dark). Themes propagate to both iframes automatically via a MutationObserver on `data-theme`.

## State Persistence

The following state survives page reloads (stored in localStorage):

| State | Key |
|-------|-----|
| Left panel width | `navigator-left-state` |
| Right panel width | `navigator-right-state` |
| Center iframe URL | `navigator-center-url` |
| Right iframe URL | `navigator-right-url` |
| Active link highlight | `navigator-active-href` |
| Widget open/closed | `navigator-widgets` |
| Sub-detail open/closed | `navigator-subdetails` |
| Tab bar state | `navigator-tabs` |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Widgets show no items | Check network tab — JSON files may fail to load from raw.githubusercontent.com |
| Right panel won't open | Click the right divider to cycle sizes |
| Tabs not appearing | Ensure you're clicking links (not middle-click opening in new tab) |
| Theme mismatch | Hard refresh (Ctrl+Shift+R) to re-sync theme across iframes |
| Language not switching | Check that FR versions of pages exist at `/fr/` paths |

---

**[Launch Main Navigator (I2) →]({{ '/interfaces/main-navigator/' | relative_url }})**

*See also: [Main Interface — Technical Publication]({{ '/publications/main-interface/' | relative_url }})*

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
