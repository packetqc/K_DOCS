---
layout: publication
title: "Web Production Pipeline"
description: "Complete production pipeline from source markdown to live GitHub Pages: three-tier publication structure, bilingual mirrors, Jekyll processing, layout system, theme architecture, asset pipeline, exclusion mechanisms, and deployment. How Knowledge web pages are built."
pub_id: "Publication #17"
version: "v1"
date: "2026-02-26"
permalink: /publications/web-production-pipeline/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "pipeline, jekyll, kramdown, production, web, deployment"
---

# Web Production Pipeline
{: #pub-title}

> **Parent publication**: [#0 — Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | **Export companion**: [#13 — Web Pagination & Export]({{ '/publications/web-pagination-export/' | relative_url }}) | **Post-pipeline**: [#16 — Web Page Visualization]({{ '/publications/web-page-visualization/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | From source markdown to live GitHub Pages |
| [Pipeline Overview](#pipeline-overview) | End-to-end flow in 10 stages |
| [Three-Tier Structure](#three-tier-publication-structure) | Source → Summary → Complete |
| [Jekyll Processing](#jekyll-processing) | Liquid → kramdown → HTML |
| [Exclusion Mechanisms](#exclusion-mechanisms) | What gets filtered, hidden, or transformed |
| [Full Documentation](#full-documentation) | Complete pipeline reference with all stages |

## Target Audience

| Audience | Focus |
|----------|-------|
| **Publication authors** | Source authoring, front matter contract, three-tier structure |
| **Web developers** | Jekyll processing, layout system, theme architecture |
| **System administrators** | GitHub Pages deployment, asset pipeline, CDN behavior |
| **AI assistants** | Exclusion mechanisms, kramdown gotchas, pipeline commands |

## Abstract

Every web page in the Knowledge system follows a deterministic production pipeline: source markdown is authored once, structured into a three-tier system (source → summary → complete), processed by Jekyll's kramdown engine with Liquid templating, wrapped in theme-aware layouts, and deployed automatically to GitHub Pages.

This publication documents the complete pipeline — from the first line of markdown to a live, bilingual, dual-theme, exportable web page. It covers the structured files involved, the processing stages, and critically, the **exclusion mechanisms** — what doesn't make it into the final web page and why.

The [complete documentation]({{ '/publications/web-production-pipeline/full/' | relative_url }}) covers all 12 sections with detailed specifications.

## Pipeline Overview

```
Source markdown (author writes once)
    ↓ pub new (scaffold)
Three-tier split (source → summary → complete)
    ↓ front matter injection
Bilingual mirrors (EN + FR for each web tier)
    ↓ Jekyll processing
Liquid templates → kramdown → HTML
    ↓ layout wrapping
publication.html or default.html
    ↓ client-side enhancements
Mermaid, themes, cross-refs, export
    ↓ GitHub Pages deployment
Live web page (dual-theme, bilingual, exportable)
```

**Key principle**: The source document is written once. Everything downstream is derived. The pipeline is deterministic — the same source always produces the same output.

## Three-Tier Publication Structure

Each publication exists at three levels:

| Tier | Location | Purpose |
|------|----------|---------|
| **Source** | `publications/<slug>/v1/README.md` | Canonical document, English only |
| **Summary** | `docs/publications/<slug>/index.md` | Web entry point, quick overview |
| **Complete** | `docs/publications/<slug>/full/index.md` | Full web documentation |

**5 files per publication**: 1 source + 2 EN web pages + 2 FR web pages.

Summary pages link to their complete page. Complete pages link back. EN links to FR and vice versa. All internal links use `relative_url` filter.

## Jekyll Processing

Three ordered passes transform markdown into HTML:

| Pass | Engine | What it does |
|------|--------|-------------|
| 1 | **Liquid** | Template processing — {% raw %}`{{ }}`{% endraw %} variables, {% raw %}`{% %}`{% endraw %} logic, URL filters |
| 2 | **kramdown** | Markdown → HTML — GFM dialect with `parse_block_html: true` |
| 3 | **Layout** | Template wrapping — injects CSS, JS, OG tags, version banner |

{% raw %}**Critical**: Liquid runs first. Any `{{ }}` in markdown content (including Mermaid hexagons) is interpreted as Liquid before kramdown ever sees it.{% endraw %}

## Exclusion Mechanisms

Not everything in the source appears on the live web page:

| Layer | What it excludes | Why |
|-------|-----------------|-----|
| **CSS** | `.mermaid-source` blocks | Source preservation — visible in git, hidden on web |
| **CSS** (`@media print`) | Toolbar, language bar, webcard, navigation | Clean PDF output |
| **JavaScript** | Mermaid blocks inside `.mermaid-source` | Prevents double-rendering |
| **kramdown** | {% raw %}`{{ }}`{% endraw %} content in code fences | Liquid processes before kramdown |
| **kramdown** | `</tags>` inside `<details>` with blank lines | HTML block parsing exits on blank line |

The exclusions are architectural — they reflect constraints of the Jekyll processing chain, not bugs. Understanding them is essential for avoiding rendering failures.

## Full Documentation

The [complete documentation]({{ '/publications/web-production-pipeline/full/' | relative_url }}) includes all 12 sections:

| # | Section | What it covers |
|---|---------|---------------|
| 1 | Source Authoring | Writing the canonical markdown document |
| 2 | Three-Tier Structure | Source → Summary → Complete split |
| 3 | Bilingual Mirrors | EN/FR parallel page architecture |
| 4 | Front Matter Contract | Required YAML metadata for every page |
| 5 | Jekyll Processing | Liquid → kramdown → HTML transformation |
| 6 | Layout System | publication.html vs default.html feature split |
| 7 | Theme System | 4-theme CSS with browser auto-detection |
| 8 | Asset Pipeline | Webcards, diagrams, images, media |
| 9 | Exclusion Mechanisms | What gets filtered, hidden, or transformed |
| 10 | Deployment | GitHub Pages auto-build from docs/ |
| 11 | Pipeline Commands | pub, docs, webcard, normalize tooling |
| 12 | Known Gotchas | kramdown quirks, proxy limits, rendering traps |

**Source**: [Issue #347](https://github.com/packetqc/knowledge/issues/347) — Documentation generation session.

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge System]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — the system this pipeline serves |
| 5 | [Webcards & Social Sharing]({{ '/publications/webcards-social-sharing/' | relative_url }}) | Asset pipeline — animated OG social previews |
| 6 | [Normalize & Structure Concordance]({{ '/publications/normalize-structure-concordance/' | relative_url }}) | Quality gate — concordance validation |
| 13 | [Web Pagination & Export]({{ '/publications/web-pagination-export/' | relative_url }}) | Export stage — PDF/DOCX from pipeline output |
| 14 | [Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }}) | System context — pipeline as component |
| 16 | [Web Page Visualization]({{ '/publications/web-page-visualization/' | relative_url }}) | Post-pipeline — rendering and diagnostics |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
