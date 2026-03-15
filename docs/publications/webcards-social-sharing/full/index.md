---
layout: publication
title: "Webcards & Social Sharing — Complete Documentation"
description: "Complete documentation for the webcard system: animated OG social previews, card types and animations, static vs dynamic behavior, two sharing modes, platform-specific behavior for LinkedIn/Twitter/Facebook/Slack, step-by-step sharing recipes, troubleshooting guide, and technical architecture."
pub_id: "Publication #5 — Full"
version: "v2"
date: "2026-02-21"
permalink: /publications/webcards-social-sharing/full/
og_image: /assets/og/webcards-social-sharing-en-cayman.gif
keywords: "webcards, OG image, animated GIF, social sharing, dynamic, knowledge artifacts"
---

# Webcards & Social Sharing — Complete Documentation
{: #pub-title}

**Contents**

| | |
|---|---|
| [Authors](#authors) | Publication authors |
| [Abstract](#abstract) | Webcard system overview and origin story |
| [What Webcards Are](#what-webcards-are) | Animated OG social preview specifications |
| &nbsp;&nbsp;[How They're Used](#how-theyre-used) | Page header, OG image, and Twitter card roles |
| &nbsp;&nbsp;[Card Types](#card-types) | Corporate, diagram, split-panel, cartoon, index |
| [Content-Inspired Design](#content-inspired-design) | How card visuals derive from publication concepts |
| [Dynamic Webcards — Living Knowledge Artifacts](#dynamic-webcards--living-knowledge-artifacts) | Data-driven cards that reflect live system state |
| &nbsp;&nbsp;[What "Dynamic" Means](#what-dynamic-means) | Content changes between generation runs |
| &nbsp;&nbsp;[Static vs Dynamic — Architecture Comparison](#static-vs-dynamic--architecture-comparison) | Hardcoded vs data-parsed generation |
| &nbsp;&nbsp;[How #4a (Knowledge Dashboard) Works](#how-4a-knowledge-dashboard-works) | Satellite table parsed into animated GIF |
| &nbsp;&nbsp;[The Dynamic Pattern — Reusable Architecture](#the-dynamic-pattern--reusable-architecture) | Parse structured data, render into GIF |
| &nbsp;&nbsp;[How This Connects to Knowledge](#how-this-connects-to-knowledge) | Visibility, currency, and discoverability |
| [Display Behavior — What You See Depends Where](#display-behavior--what-you-see-depends-where) | Animation on GitHub Pages, static on social platforms |
| [Two Sharing Modes](#two-sharing-modes) | Page URL vs image URL sharing |
| &nbsp;&nbsp;[Mode 1: Share the Page URL](#mode-1-share-the-page-url-recommended) | Rich preview with title, description, and webcard |
| &nbsp;&nbsp;[Mode 2: Share the Image URL Directly](#mode-2-share-the-image-url-directly) | Image only, no context or click-through |
| &nbsp;&nbsp;[Comparison](#comparison) | Side-by-side feature comparison of both modes |
| [Platform Behavior](#platform-behavior) | How each social platform handles OG images |
| &nbsp;&nbsp;[LinkedIn](#linkedin) | Static first frame, aggressive cache |
| &nbsp;&nbsp;[Twitter (X)](#twitter-x) | Summary large image card, 7-day cache |
| &nbsp;&nbsp;[Facebook](#facebook) | May play GIF animation inline |
| &nbsp;&nbsp;[Slack / Discord](#slack--discord) | Rich preview, may play on hover |
| [How-To Recipes](#how-to-recipes) | Step-by-step sharing guides |
| &nbsp;&nbsp;[Share a Publication on LinkedIn (Mobile)](#share-a-publication-on-linkedin-mobile) | Mobile browser share workflow |
| &nbsp;&nbsp;[Share a Publication on LinkedIn (Desktop)](#share-a-publication-on-linkedin-desktop) | Desktop paste and preview workflow |
| &nbsp;&nbsp;[Force LinkedIn to Refresh a Stale Preview](#force-linkedin-to-refresh-a-stale-preview) | Post Inspector cache-clearing steps |
| &nbsp;&nbsp;[Showcase the Animation](#showcase-the-animation-not-the-page) | Direct GIF URL sharing for animation display |
| [Troubleshooting](#troubleshooting) | Wrong links, missing images, stale previews |
| [Technical Architecture](#technical-architecture) | HTML integration, front matter, generator |
| &nbsp;&nbsp;[HTML Integration](#html-integration) | OG meta tags and canonical URL setup |
| &nbsp;&nbsp;[Front Matter](#front-matter) | YAML og_image field requirement |
| &nbsp;&nbsp;[Generator](#generator) | generate_og_gifs.py usage and options |
| &nbsp;&nbsp;[GIF Optimization](#gif-optimization) | Color palette, dithering, and file sizes |
| [Related Publications](#related-publications) | Links to sibling publications |

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Designed the webcard system as part of the knowledge architecture — giving every publication a unique, animated social identity that works across platforms.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Co-designed the webcard specification, built the generator script, and documented the social sharing workflow after encountering platform-specific behaviors during real sharing attempts.

---

## Abstract

Every web page in Knowledge has a unique **animated OG social preview** — a 1200x630 GIF that serves as both a visual header on GitHub Pages and a social media card when shared on LinkedIn, Twitter, or Facebook. These are **webcards**.

This publication documents:

| Topic | Description |
|-------|-------------|
| **What webcards are** | Animated GIFs tailored to each page's content, bilingual (EN/FR) |
| **Content-inspired design** | How each card's visuals are derived from its publication's core concept |
| **Static vs dynamic generation** | Hardcoded cards vs data-driven cards (like the Knowledge Dashboard) |
| **Display behavior** | Social platforms show the first frame; GitHub Pages plays the full animation |
| **Two sharing modes** | Share the page URL (recommended) vs share the image directly |
| **Platform behavior** | How LinkedIn, Twitter, Facebook, and Slack handle OG images |
| **Practical recipes** | Step-by-step guides for mobile and desktop sharing |
| **Troubleshooting** | LinkedIn cache, wrong URLs, missing previews |

Born from a real issue: sharing a publication on LinkedIn from mobile resulted in the link pointing to the GitHub markdown file instead of the GitHub Pages publication. This led to adding `<link rel="canonical">` tags and documenting the correct sharing workflow.

---

## What Webcards Are

A webcard is an **animated GIF** that represents a web page:

| Property | Value |
|----------|-------|
| Size | 1200x630 pixels |
| Format | Animated GIF, 256-color optimized palettes |
| Dithering | Floyd-Steinberg |
| Loop | Infinite (`loop=0`) |
| Theme | Dual: Cayman (light, teal/emerald) + Midnight (dark, navy/indigo) |
| Detection | `<picture>` + `prefers-color-scheme` media query |
| Total set | 40 GIFs (10 pages x 2 themes x 2 languages) |
| Total size | ~7 MB for all 40 |
| Generator | `scripts/generate_og_gifs.py` |
| Output | `docs/assets/og/<page-type>-<lang>-<theme>.gif` |

Each page gets a unique animation tailored to its content — not generic templates.

### How They're Used

| Usage | Description |
|-------|-------------|
| **Page header** | Displayed as a full-width banner above page content on GitHub Pages |
| **OG image** | Referenced in `<meta property="og:image">` for social sharing previews |
| **Twitter card** | Referenced in `<meta name="twitter:image">` for Twitter previews |

### Card Types

| Type | Pages | Frames | Animation |
|------|-------|--------|-----------|
| `corporate` | Profile hub, resume, full profile | 8 | Photo with pulsing color-cycling border ring |
| `diagram` | MPLIB Pipeline, Live Session | 7-8 | Pipeline nodes activate sequentially |
| `split-panel` | Distributed Minds, Knowledge Dashboard | 8 | Left panel cycles + right panel flows |
| `cartoon` | AI Persistence | 10 | Vicky NPC to AWARE transformation |
| `index` | Publications index | 8 | Cards appear one by one, then glow |

---

## Content-Inspired Design

Every webcard is **derived from** the publication it represents — not from a generic template library. The card type, animation, text, and visual elements are chosen based on what the publication actually documents:

| Publication | Why this card design |
|-------------|---------------------|
| **Profile** (corporate) | The author's photo is the centerpiece — pulsing border ring draws attention to the person behind the work |
| **MPLIB Pipeline** (diagram) | Documents a 5-stage data pipeline — the webcard animates those exact stages left-to-right |
| **Live Session** (diagram) | Documents a 6-stage real-time analysis flow — the webcard pulses data through those stages |
| **AI Persistence** (cartoon) | The Free Guy analogy (NPC→AWARE) is the publication's core metaphor — Vicky's transformation IS the concept |
| **Distributed Minds** (split-panel) | Bidirectional knowledge flow (push + harvest) — left panel shows layers, right panel shows the flow between master and satellites |
| **Knowledge Dashboard** (split-panel) | Network status with satellite inventory — the webcard renders the actual satellite table data |
| **Publications Index** (index) | A collection of publications — the webcard shows cards appearing one by one |

**Design rule**: Read the publication first, then design the webcard to visualize its core concept. The animation should tell the publication's story in 2-3 seconds.

---

## Static vs Dynamic Generation

Most webcards are **statically designed** — the text, layout, and animation are hardcoded in the generator script based on the publication's content at design time. When the publication content changes significantly, the webcard is manually regenerated.

One webcard is **dynamically generated** — Publication #4a (Knowledge Dashboard) reads **live data** from the satellite network status table via `parse_dashboard_data()`:

| Aspect | Static cards (most) | Dynamic card (#4a) |
|--------|--------------------|--------------------|
| Content source | Hardcoded in generator script | Parsed from README satellite table |
| When to regenerate | After significant content changes | On every `harvest --healthcheck` |
| What changes between runs | Nothing (identical output) | Satellite names, versions, drift, health status |
| Data function | None | `parse_dashboard_data()` |
| Examples | All profile, pipeline, persistence, index cards | Knowledge Dashboard only |

**Why #4a is dynamic**: The Dashboard is a living document — satellite status changes on every `harvest` run. Hardcoding satellite names and versions would make the webcard stale immediately. Instead, `parse_dashboard_data()` reads the actual satellite inventory table from `publications/distributed-knowledge-dashboard/v1/README.md` and renders the current network state into the GIF. Top N rows are rendered where N fits the card's content area.

**Future candidates**: Any publication that documents live, changing data could benefit from dynamic generation. The pattern established by #4a — parse structured data from the source document, render it into the GIF — is reusable.

---

## Display Behavior — What You See Depends Where

The same webcard looks different depending on where it's displayed:

| Context | What you see | Animation |
|---------|-------------|-----------|
| **GitHub Pages** (page header) | Full animated GIF playing in loop | Yes — all frames |
| **LinkedIn post preview** | First frame only (static) | No |
| **Twitter card** | First frame only (static) | No |
| **Facebook link preview** | First frame only (static) | No |
| **Slack/Discord unfurl** | First frame (may play on hover) | Sometimes |
| **Direct image URL in browser** | Full animated GIF | Yes |
| **Direct image in messaging app** | Depends on app | Sometimes |

**Design implication**: The first frame of every webcard must be self-explanatory — it's what most people will see. The animation is a bonus for visitors who reach the actual GitHub Pages site.

---

## Two Sharing Modes

### Mode 1: Share the Page URL (Recommended)

**What you share**: `{{ site.baseurl }}/publications/distributed-minds/`

**What happens**:

| Step | Action |
|------|--------|
| **Crawl** | Social platform's crawler fetches the page |
| **Read tags** | Reads `og:title`, `og:description`, `og:image` meta tags from the HTML `<head>` |
| **Download** | Downloads the webcard GIF from the `og:image` URL |
| **Display** | Shows title + description + first frame of webcard as preview card |
| **Click-through** | Goes to your publication page |

**Result**: Rich preview with title, description, and webcard image. The link takes readers to your publication.

### Mode 2: Share the Image URL Directly

**What you share**: `{{ site.baseurl }}/assets/og/distributed-minds-en.gif`

**What happens**:

| Step | Action |
|------|--------|
| **Detect** | Social platform sees a direct image link |
| **Display** | Shows the image (may play animation or show first frame) |
| **No context** | No associated title or description — just the image |
| **Click-through** | Goes to the image file, not the publication |

**Result**: Shows the webcard animation (on some platforms) but provides no context and no link to the publication. Use this only when you specifically want to showcase the animation itself.

### Comparison

| Aspect | Page URL (Mode 1) | Image URL (Mode 2) |
|--------|-------------------|---------------------|
| Shows title | Yes | No |
| Shows description | Yes | No |
| Shows webcard | Yes (first frame) | Yes (may animate) |
| Click goes to | Publication page | Image file |
| SEO value | High | None |
| Recommended for | All sharing | Showcasing the animation |

---

## Platform Behavior

### LinkedIn

| Aspect | Behavior |
|--------|----------|
| **Page share** | Shows link preview card with title, description, first frame of webcard |
| **Image share** | Shows image only |
| **Animation** | Never plays — always static first frame |
| **Cache** | Aggressive caching — may show stale data for hours/days |
| **Cache clear** | Use [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/) to force refresh |
| **Canonical** | Follows `<link rel="canonical">` and `og:url` for click-through URL |
| **Known issue** | If canonical or og:url is wrong, the click-through goes to the wrong page |

### Twitter (X)

| Aspect | Behavior |
|--------|----------|
| **Page share** | Shows `summary_large_image` card with title, description, webcard first frame |
| **Image share** | Shows image in tweet |
| **Animation** | Never plays in card preview — static first frame |
| **Cache** | Caches for ~7 days |
| **Cache clear** | Use [Twitter Card Validator](https://cards-dev.twitter.com/validator) |

### Facebook

| Aspect | Behavior |
|--------|----------|
| **Page share** | Shows link preview with title, description, webcard |
| **Image share** | May play GIF animation inline |
| **Animation** | Sometimes plays in preview (Facebook supports GIF playback) |
| **Cache** | Use [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/) to refresh |

### Slack / Discord

| Aspect | Behavior |
|--------|----------|
| **Link unfurl** | Shows rich preview with title, description, first frame |
| **Direct image** | May play GIF on hover or inline |
| **No cache issue** | Re-fetches on each share |

---

## How-To Recipes

### Share a Publication on LinkedIn (Mobile)

```
Step 1 — Open the publication on GitHub Pages
         URL must start with: packetqc.github.io/K_DOCS/
         NOT: github.com/packetqc/knowledge/blob/...

Step 2 — Verify the URL bar shows packetqc.github.io
         If it shows github.com, you're on the wrong site

Step 3 — Tap the Share button in your browser

Step 4 — Choose LinkedIn

Step 5 — Add your commentary and post
```

### Share a Publication on LinkedIn (Desktop)

```
Step 1 — Copy the GitHub Pages URL:
         {{ site.baseurl }}/publications/<slug>/

Step 2 — In LinkedIn, click "Start a post"

Step 3 — Paste the URL — wait for the preview card to load
         You should see: title + description + webcard first frame

Step 4 — If the preview looks wrong, use Post Inspector first:
         https://www.linkedin.com/post-inspector/

Step 5 — Add commentary and post
```

### Force LinkedIn to Refresh a Stale Preview

```
Step 1 — Go to https://www.linkedin.com/post-inspector/

Step 2 — Paste the full GitHub Pages URL

Step 3 — Click "Inspect"

Step 4 — Verify:
         - Title matches your publication
         - Description is correct
         - Image shows your webcard (first frame)
         - Canonical URL points to packetqc.github.io (not github.com)

Step 5 — If correct, share the link — LinkedIn now uses the fresh data
```

### Showcase the Animation (Not the Page)

```
Step 1 — Find the webcard URL:
         {{ site.baseurl }}/assets/og/<card>-<lang>.gif
         Example: .../assets/og/distributed-minds-en.gif

Step 2 — Share this URL directly in your post

Step 3 — On some platforms (Facebook, Slack), the animation will play
         On LinkedIn/Twitter, only the first frame shows
```

---

## Troubleshooting

### LinkedIn shows wrong preview or links to GitHub markdown

**Symptoms**: Shared the page, but clicking the link in LinkedIn goes to `github.com/packetqc/knowledge/blob/...` instead of `packetqc.github.io/K_DOCS/...`.

**Causes and fixes**:

| Cause | Fix |
|-------|-----|
| You were on the GitHub markdown view, not GitHub Pages | Check URL bar: must be `packetqc.github.io`, not `github.com` |
| LinkedIn cached a stale preview | Use [Post Inspector](https://www.linkedin.com/post-inspector/) to refresh |
| Missing canonical tag | Fixed in v20 — `<link rel="canonical">` added to both layouts |
| og:url pointing to wrong URL | Verify front matter has correct `permalink` |

### Preview shows no image

| Check | Action |
|-------|--------|
| **Front matter** | Verify `og_image` is set in the page's YAML |
| **GIF file** | Check that the GIF file exists in `docs/assets/og/` |
| **Regenerate** | Run `webcard <target>` to regenerate missing GIFs |
| **Crawler view** | Use platform-specific debugger to check what the crawler sees |

### Animation doesn't play on social media

**This is expected behavior.** LinkedIn, Twitter, and Facebook show the first frame as a static preview. Animation only plays in specific contexts:

| Context | Animation plays? |
|---------|-----------------|
| **GitHub Pages site** | Yes (page header) |
| **GIF URL in browser** | Yes (direct viewing) |
| **Messaging apps** | Sometimes (Slack, Discord, iMessage) |

Design every webcard so the first frame is self-explanatory.

### Shared on mobile but link is wrong

When using the mobile browser's "Share" function:

| Step | What happens |
|------|-------------|
| **Browser shares URL** | The browser shares the URL from the address bar |
| **Wrong site possible** | If you navigated from GitHub to a publication, you may be on `github.com` (the markdown renderer), not `packetqc.github.io` (GitHub Pages) |
| **Prevention** | Always navigate to the GitHub Pages URL directly before sharing |

**Quick check**: Look at the page — if you see a full-width animated GIF header at the top, you're on GitHub Pages. If you see rendered markdown without a header, you're on GitHub.

---

## Technical Architecture

### HTML Integration

Both layouts (`default.html` and `publication.html`) include:

```html
<!-- OG image for social sharing -->
<meta property="og:image" content="{% raw %}{{ page.og_image | absolute_url }}{% endraw %}" />

<!-- Canonical URL — LinkedIn uses this as click-through -->
<link rel="canonical" href="{% raw %}{{ page.url | absolute_url }}{% endraw %}" />

<!-- Page header display -->
<div class="webcard-header">
  <img src="{% raw %}{{ page.og_image | relative_url }}{% endraw %}" alt="{% raw %}{{ page.title }}{% endraw %}" />
</div>
```

### Front Matter

Every page requires `og_image` in its YAML front matter:

```yaml
og_image: /assets/og/distributed-minds-en-cayman.gif
```

Naming convention: `assets/og/<page-type>-<lang>-<theme>.gif` (e.g., `resume-en-cayman.gif`, `resume-en-midnight.gif`)

### Generator

`scripts/generate_og_gifs.py` generates all webcards in both themes:

```bash
python3 scripts/generate_og_gifs.py              # All cards, both themes
python3 scripts/generate_og_gifs.py --theme midnight  # One theme only
python3 scripts/generate_og_gifs.py #5            # One publication, both themes
python3 scripts/generate_og_gifs.py profile --theme cayman --lang en  # Specific
```

### Theme Detection

Both layouts use `<picture>` with `prefers-color-scheme` media query to auto-serve the matching webcard:

| Context | Webcard served |
|---------|---------------|
| Light mode browser | Cayman webcard (teal/emerald gradient) |
| Dark mode browser | Midnight webcard (navy/indigo gradient) |
| Social sharing (`og:image`) | Always Cayman (light) |

### GIF Optimization

| Property | Value |
|----------|-------|
| **Color palette** | 256-color per frame (MEDIANCUT quantization) |
| **Dithering** | Floyd-Steinberg for smooth gradients |
| **Frame sizes** | 120-765 KB individual |
| **Total size** | ~7 MB for all 40 GIFs |

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — webcards are part of the system |
| 3 | [AI Session Persistence]({{ '/publications/ai-session-persistence/' | relative_url }}) | Has `cartoon` type webcard (Vicky NPC to AWARE) |
| 4 | [Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }}) | Has `split-panel` type webcard |
| 4a | [Knowledge Dashboard]({{ '/publications/distributed-knowledge-dashboard/' | relative_url }}) | Has data-driven `split-panel` webcard |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
