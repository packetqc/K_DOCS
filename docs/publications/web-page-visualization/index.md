---
layout: publication
title: "Web Page Visualization — Local Rendering Pipeline"
description: "A self-contained pipeline for rendering web pages and Mermaid diagrams as images from an AI coding assistant's environment. Zero external dependencies. Reusable across interactive diagnostics, design, and document management."
pub_id: "Publication #16"
version: "v1"
date: "2026-02-26"
permalink: /publications/web-page-visualization/
og_image: /assets/og/web-page-visualization-en-cayman.gif
keywords: "web visualization, Mermaid rendering, Playwright, Chromium, AI diagnostics, document management, self-contained pipeline"
---

# Web Page Visualization
{: #pub-title}

> **Related**: [#13 — Web Pagination & Export]({{ '/publications/web-pagination-export/' | relative_url }})
> | [#15 — Architecture Diagrams]({{ '/publications/architecture-diagrams/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | What this capability does and why it matters |
| [Architecture](#architecture) | Component inventory and data flow |
| [Use Cases](#use-cases) | Three reuse domains |
| [Mermaid Source Preservation](#mermaid-source-preservation) | The hybrid format design |
| [Full Documentation](#full-documentation) | Complete technical reference |

## Target Audience

| Audience | Focus |
|----------|-------|
| **Network/System Admins** | Architecture — self-contained design, zero network calls |
| **Programmers** | Pipeline code patterns — reusable Python/Playwright |
| **Technical Managers** | Use Cases — three reuse domains |
| **Documentation Engineers** | Source Preservation + Web Pipeline Exclusion |

## Abstract

A **self-contained, zero-dependency pipeline** for rendering web pages and Mermaid diagrams as images, directly from an AI coding assistant's environment. Uses only pre-installed tools (Python, Playwright, Chromium) and a local npm package (mermaid.js) — no external services, no CDN calls at rendering time.

The capability emerged from a diagnostic need (Issue #334) and proved immediately reusable across three domains:

1. **Interactive diagnostics** — Claude renders the page, identifies issues, proposes fixes
2. **Interactive design** — Visual validation during iterative web page construction
3. **Document management** — Screenshots for publications, diagram images for export pipelines

## Architecture

```
urllib (fetch HTML) → self-contained HTML → Playwright + Chromium → npm mermaid → screenshots
```

| Component | Role | External? |
|-----------|------|-----------|
| **urllib** | Fetch live page HTML | No — bypasses proxy |
| **Playwright** | Headless browser automation | No — pre-installed |
| **Chromium** | Full DOM rendering engine | No — pre-installed binary |
| **npm mermaid** | Mermaid code → SVG | No — local npm package |

**Zero network calls at rendering time.** urllib bypasses the container proxy via direct socket connections — the same mechanism `gh_helper.py` uses for GitHub API calls.

## Use Cases

### 1. Interactive Diagnostics

Claude renders the page, sees the actual output, and diagnoses rendering issues — all in one session. Real-world validation: Issue #334, 14 Mermaid diagrams on the FR Architecture Diagrams page, user confirmed: *"ça semble fonctionner le visual d'une page web"*.

### 2. Interactive Design

During iterative web page construction, Claude renders the current state to validate layout, styling, and bilingual mirrors — without the user needing to refresh a browser.

### 3. Document Management

Generating visual artifacts: screenshots for publications, Mermaid-to-PNG for DOCX export (Mermaid.js is not supported in Word), visual validation reports for `pub check` and `docs check`.

## Mermaid Source Preservation

When diagrams are pre-rendered to PNG, the original Mermaid source is preserved in `<details class="mermaid-source">` collapsible sections — visible on GitHub source view, hidden on web pages. This solves the chicken-and-egg problem: the source that generates the diagram travels with the rendered output.

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="diagram-midnight.png">
  <img src="diagram-cayman.png" alt="Diagram">
</picture>

<details class="mermaid-source">
<summary>Mermaid source</summary>
...
</details>
```

The `.mermaid-source` class triggers CSS hiding + JS exclusion in both layouts — preventing mermaid.js from double-rendering preserved source blocks.

## Full Documentation

[All sections with code patterns, validation results, and security analysis are documented in the]({{ '/publications/web-page-visualization/full/' | relative_url }}) **complete version**.
