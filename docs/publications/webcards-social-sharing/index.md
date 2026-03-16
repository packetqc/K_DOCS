---
layout: publication
title: "Webcards & Social Sharing — Animated OG Previews for AI-Engineered Publications"
description: "Every knowledge page has a unique animated OG social preview — a 1200x630 GIF serving as both a visual header on GitHub Pages and a social media card on LinkedIn, Twitter, and Facebook. This publication documents what webcards are, how to share them, and platform-specific behavior."
pub_id: "Publication #5"
version: "v2"
date: "2026-02-21"
permalink: /publications/webcards-social-sharing/
og_image: /assets/og/webcards-social-sharing-en-cayman.gif
keywords: "webcards, OG image, animated GIF, social sharing, dynamic, knowledge artifacts"
---

# Webcards & Social Sharing — Animated OG Previews
{: #pub-title}

> **Parent publication**: [#0 — Knowledge]({{ '/publications/knowledge-system/' | relative_url }}) — the system these webcards belong to

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Webcard system overview and origin story |
| [What Webcards Are](#what-webcards-are) | Animated OG social preview specifications and card types |
| [Dynamic Webcards — Living Knowledge Artifacts](#dynamic-webcards--living-knowledge-artifacts) | Data-driven cards that reflect live system state |
| [Two Sharing Modes](#two-sharing-modes) | Page URL vs image URL sharing |
| [Platform Behavior](#platform-behavior) | LinkedIn, Twitter, Facebook, Slack handling |
| [How-To Recipes](#how-to-recipes) | Step-by-step sharing guides for mobile and desktop |
| [Troubleshooting](#troubleshooting) | Wrong links, missing images, stale previews |
| [Technical Architecture](#technical-architecture) | HTML integration, front matter, generator script |

## Abstract

Every web page in Knowledge has a unique **animated OG social preview** — a 1200x630 GIF that serves as both a visual header on GitHub Pages and a social media card when shared on LinkedIn, Twitter, or Facebook. These are **webcards**.

Born from a real issue: sharing a publication on LinkedIn from mobile resulted in the link pointing to the GitHub markdown file instead of the GitHub Pages publication. This led to adding `<link rel="canonical">` tags and documenting the correct sharing workflow.

## What Webcards Are

A webcard is an **animated GIF** (1200x630 pixels, 256-color optimized, Floyd-Steinberg dithering) that represents a web page. Each page gets a unique animation tailored to its content — not generic templates. Dual-theme: **Cayman** (light, teal/emerald) + **Midnight** (dark, navy/indigo) — browser auto-detects via `prefers-color-scheme`. Total set: 40 GIFs (10 pages x 2 themes x 2 languages), ~7 MB total.

| Card Type | Pages | Animation |
|-----------|-------|-----------|
| `corporate` | Profile hub, resume, full profile | Photo with pulsing color-cycling border ring |
| `diagram` | MPLIB Pipeline, Live Session | Pipeline nodes activate sequentially |
| `split-panel` | Distributed Minds, Knowledge Dashboard | Left panel cycles + right panel flows |
| `cartoon` | AI Persistence | Vicky NPC to AWARE transformation |
| `index` | Publications index | Cards appear one by one, then glow |

## Dynamic Webcards — Living Knowledge Artifacts

Webcards are not just decorative images — they are **knowledge artifacts** that read live data from the system and render it visually. A dynamic webcard's content changes between generation runs because the underlying data changes.

**The data flow**: Knowledge data (source documents, satellite tables, system state) → parser function → generator script → animated GIF → GitHub Pages header + OG social preview.

| Aspect | Static cards | Dynamic cards |
|--------|-------------|---------------|
| **Content source** | Hardcoded in generator | Parsed from knowledge documents |
| **Output between runs** | Identical | Different (reflects new data) |
| **Knowledge integration** | One-time design | Continuous — reads live state |
| **Example** | Profile, pipeline, persistence | Knowledge Dashboard (#4a) |

**#4a in action**: The Dashboard webcard reads the actual Satellite Network Status table — satellite names, versions, drift, health — and renders the current network state into the GIF. What you see in the image IS the real data. Regenerated automatically after every `harvest --healthcheck`.

**The webcard IS the status report**: A #4a card showing all green means the network is healthy. Red and orange means satellites need attention. Three knowledge concerns converge in webcards: **visibility** (unique visual identity per page), **currency** (dynamic cards reflect live state), and **discoverability** (OG tags ensure rich social previews).

Social platforms show the **first frame** as static preview. Full animation plays on GitHub Pages.

| Context | Animation |
|---------|-----------|
| GitHub Pages (page header) | Full animation |
| LinkedIn / Twitter / Facebook | First frame only |
| Slack / Discord | Sometimes (hover) |

## Two Sharing Modes

**Mode 1 — Share the Page URL** (recommended): Share `packetqc.github.io/K_DOCS/publications/...`. Platforms read OG meta tags and display title + description + webcard first frame. Click-through goes to the publication.

**Mode 2 — Share the Image URL directly**: Share the `.gif` URL. Some platforms may play the animation, but no title, no description, click-through goes to the image file. Use only to showcase the animation.

## Platform Behavior

| Platform | Behavior |
|----------|----------|
| **LinkedIn** | Static first frame. Aggressive cache — use [Post Inspector](https://www.linkedin.com/post-inspector/) to refresh. Follows `<link rel="canonical">` for click-through. |
| **Twitter** | Static first frame. `summary_large_image` card. Caches ~7 days. |
| **Facebook** | May play GIF animation inline. Use [Sharing Debugger](https://developers.facebook.com/tools/debug/) to refresh. |
| **Slack/Discord** | Rich preview with first frame. Direct image may play on hover. |

## How-To Recipes

**Share on LinkedIn (Mobile)**: Navigate to `packetqc.github.io/K_DOCS/publications/...` (NOT `github.com`), tap Share, choose LinkedIn.

**Share on LinkedIn (Desktop)**: Copy the GitHub Pages URL, paste in LinkedIn post, wait for preview card, verify it shows title + webcard.

**Force LinkedIn Refresh**: Go to [Post Inspector](https://www.linkedin.com/post-inspector/), paste URL, click Inspect, verify data.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| **Wrong link in LinkedIn** | You shared from `github.com` instead of `packetqc.github.io`. Check URL bar. |
| **No preview image** | Verify `og_image` in front matter, check GIF exists in `docs/assets/og/`. |
| **Animation doesn't play** | Expected — social platforms show first frame only. |
| **Stale preview** | Use platform-specific cache debugger tools. |

## Technical Architecture

Both layouts (`default.html` and `publication.html`) include `og:image`, `twitter:image`, and `<link rel="canonical">` meta tags. Every page requires `og_image` in YAML front matter pointing to its GIF. Generator script: `scripts/generate_og_gifs.py`.

---

[**Read the full documentation →**]({{ '/publications/webcards-social-sharing/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
