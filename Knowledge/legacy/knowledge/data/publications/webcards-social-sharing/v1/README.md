# Webcards & Social Sharing — Animated OG Previews for AI-Engineered Publications

**Publication v1 — February 2026**
**Languages / Langues**: English (this document) | [Français](https://packetqc.github.io/knowledge/fr/publications/webcards-social-sharing/)

---

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Designed the webcard system as part of the knowledge architecture — giving every publication a unique, animated social identity that works across platforms.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Co-designed the webcard specification, built the generator script, and documented the social sharing workflow after encountering platform-specific behaviors during real sharing attempts.

---

## Abstract

Every web page in Knowledge has a unique **animated OG social preview** — a 1200×630 GIF that serves as both a visual header on GitHub Pages and a social media card when shared on LinkedIn, Twitter, or Facebook. These are **webcards**.

This publication documents:

1. **What webcards are** — animated GIFs tailored to each page's content, bilingual (EN/FR)
2. **Content-inspired design** — how each card's visuals are derived from its publication's core concept
3. **Dynamic webcards as knowledge artifacts** — how webcards read live system data, reflect actual network state, and serve as visual indicators of knowledge health. The Knowledge Dashboard (#4a) webcard renders real satellite inventory data — names, versions, drift, health status — directly from the source document. The image IS the status report.
4. **The dynamic pattern** — reusable architecture for data-driven webcards: define data source → write parser → design renderer → wire trigger. Any publication reflecting live state is a candidate.
5. **Display behavior** — social platforms show the first frame; GitHub Pages plays the full animation
6. **Two sharing modes** — share the page URL (recommended) vs share the image directly
7. **Platform behavior** — how LinkedIn, Twitter, Facebook, and Slack handle OG images
8. **Practical recipes** — step-by-step guides for mobile and desktop sharing
9. **Troubleshooting** — LinkedIn cache, wrong URLs, missing previews

Born from a real issue: sharing a publication on LinkedIn from mobile resulted in the link pointing to the GitHub markdown file instead of the GitHub Pages publication. This led to adding `<link rel="canonical">` tags and documenting the correct sharing workflow.

---

## What Webcards Are

A webcard is an **animated GIF** that represents a web page:

| Property | Value |
|----------|-------|
| Size | 1200×630 pixels |
| Format | Animated GIF, 256-color optimized palettes |
| Dithering | Floyd-Steinberg |
| Loop | Infinite (`loop=0`) |
| Theme | Dual: Cayman (light, teal/emerald) + Midnight (dark, navy/indigo) |
| Detection | `<picture>` + `prefers-color-scheme` media query |
| Total set | 40 GIFs (10 pages × 2 themes × 2 languages) |
| Total size | ~7 MB for all 40 |
| Generator | `scripts/generate_og_gifs.py` |
| Output | `docs/assets/og/<page-type>-<lang>-<theme>.gif` |

Each page gets a unique animation tailored to its content — not generic templates.

### How They're Used

1. **Page header** — displayed as a full-width banner above page content on GitHub Pages
2. **OG image** — referenced in `<meta property="og:image">` for social sharing previews
3. **Twitter card** — referenced in `<meta name="twitter:image">` for Twitter previews

### Card Types

| Type | Pages | Frames | Animation |
|------|-------|--------|-----------|
| `corporate` | Profile hub, resume, full profile | 8 | Photo with pulsing color-cycling border ring |
| `diagram` | MPLIB Pipeline, Live Session | 7-8 | Pipeline nodes activate sequentially |
| `split-panel` | Distributed Minds, Knowledge Dashboard | 8 | Left panel cycles + right panel flows |
| `cartoon` | AI Persistence | 10 | Vicky NPC→AWARE transformation |
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

## Dynamic Webcards — Living Knowledge Artifacts

Webcards are not just decorative images. They are **knowledge artifacts** — visual representations of the system's actual state that update automatically as the knowledge evolves.

### What "Dynamic" Means

A dynamic webcard **reads live data** from Knowledge and renders it into the GIF at generation time. The image content changes between runs because the underlying data changes. This makes the webcard a visual indicator — glance at it and you see the current state without reading the documentation.

```
Knowledge Data (source of truth)
    ↓ parse function (e.g., parse_dashboard_data())
Generator Script (generate_og_gifs.py)
    ↓ render frames
Animated GIF (docs/assets/og/*.gif)
    ↓ served via GitHub Pages
Page Header + OG Social Preview
```

The generator script is the bridge between structured knowledge data and visual output. Static webcards skip the parse step — their content is hardcoded. Dynamic webcards read the data every time they're regenerated.

### Static vs Dynamic — Architecture Comparison

| Aspect | Static cards | Dynamic cards |
|--------|-------------|---------------|
| **Content source** | Hardcoded text in generator script | Parsed from knowledge documents |
| **When to regenerate** | After publication content changes | On every `harvest --healthcheck` or data change |
| **Output between runs** | Identical (same bytes) | Different (reflects new data) |
| **Data function** | None — text literals in code | `parse_dashboard_data()` or similar |
| **Knowledge integration** | One-time design | Continuous — reads live state |
| **Examples** | Profile, pipeline, persistence, index | Knowledge Dashboard (#4a) |
| **Regeneration trigger** | Manual: `webcard <target>` | Automatic: end of `harvest --healthcheck` |

### How #4a (Knowledge Dashboard) Works

The Dashboard webcard is the first fully dynamic webcard. It visualizes the **satellite network status** by reading the actual data table from the dashboard source document.

**Data flow**:

1. `harvest --healthcheck` scans all satellites, updates the Satellite Network Status table in `publications/distributed-knowledge-dashboard/v1/README.md`
2. `parse_dashboard_data()` reads that table — extracts satellite names, versions, drift counts, health status, severity icons
3. The generator renders a split-panel card: left side shows version metric + animation, right side shows a grid of satellite nodes with scanning highlight effect
4. Each satellite node in the grid reflects its actual status — name, version, and severity color (green/yellow/orange/red)
5. The output GIF literally shows the current state of the distributed knowledge network

**What you see in the webcard IS the real data**:
- Satellite names are the actual repo names from the network
- Version numbers are the actual `knowledge-version` tags from each satellite's CLAUDE.md
- Drift values are the actual gap between satellite version and core version
- Health indicators are the actual accessibility status from the last scan
- The sorting (core first, then by version desc, drift desc) matches the dashboard table

**Regeneration is automatic**: At the end of every `harvest --healthcheck`, if dashboard data changed, the generator runs and produces fresh webcards. The GIFs committed to `docs/assets/og/` are the latest snapshot of the network. When the PR merges and GitHub Pages deploys, anyone viewing the dashboard page sees the current network state in the page header — before reading a single line of text.

### The Dynamic Pattern — Reusable Architecture

The architecture established by #4a is a reusable pattern for any publication that reflects live, changing state:

1. **Define a data source** — a structured table or section in a publication's source document
2. **Write a parser** — a function that extracts structured data from the markdown
3. **Design a renderer** — card layout that maps data fields to visual elements
4. **Wire the trigger** — regenerate automatically when the data source changes (e.g., after healthcheck, after harvest, after normalize)

**Future candidates for dynamic webcards**:

| Card | Data source | What it would show |
|------|------------|-------------------|
| **Publication Index** | `docs/publications/index.md` | Count of publications, latest pub date, completion status |
| **Live Knowledge Network** (#10) | `/tmp/knowledge_peers.json` | Active beacons, peer count, subnet map |
| **Normalize** (#6) | Normalize report output | Pass/fail counts, conformity percentage |
| **Profile** (corporate) | Profile pages, publication count | Dynamic stats — years experience, pub count, project count |

### How This Connects to Knowledge

Webcards sit at the intersection of three knowledge concerns:

| Concern | How webcards address it |
|---------|------------------------|
| **Visibility** | Every publication has a unique visual identity — recognizable at a glance in social feeds, link previews, and page headers |
| **Currency** | Dynamic webcards reflect the actual state of Knowledge — stale webcards mean stale data, fresh webcards mean the system is active |
| **Discoverability** | OG meta tags ensure social platforms render rich previews — the webcard is the first thing a reader sees before clicking through |

Knowledge's health can literally be read from its webcards. A #4a webcard showing all green satellites means the network is healthy. A webcard showing red and orange means satellites need attention. The image IS the status report.

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

**What you share**: `https://packetqc.github.io/knowledge/publications/distributed-minds/`

**What happens**:
1. Social platform's crawler fetches the page
2. Reads `og:title`, `og:description`, `og:image` meta tags from the HTML `<head>`
3. Downloads the webcard GIF from the `og:image` URL
4. Displays: title + description + first frame of webcard as preview card
5. Click-through goes to your publication page

**Result**: Rich preview with title, description, and webcard image. The link takes readers to your publication.

### Mode 2: Share the Image URL Directly

**What you share**: `https://packetqc.github.io/knowledge/assets/og/distributed-minds-en.gif`

**What happens**:
1. Social platform sees a direct image link
2. Displays the image (may play animation or show first frame)
3. No associated title or description — just the image
4. Click-through goes to the image file, not the publication

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

- **Page share**: Shows link preview card with title, description, first frame of webcard
- **Image share**: Shows image only
- **Animation**: Never plays — always static first frame
- **Cache**: Aggressive caching — may show stale data for hours/days
- **Cache clear**: Use [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/) to force refresh
- **Canonical**: Follows `<link rel="canonical">` and `og:url` for click-through URL
- **Known issue**: If canonical or og:url is wrong, the click-through goes to the wrong page

### Twitter (X)

- **Page share**: Shows `summary_large_image` card with title, description, webcard first frame
- **Image share**: Shows image in tweet
- **Animation**: Never plays in card preview — static first frame
- **Cache**: Caches for ~7 days
- **Cache clear**: Use [Twitter Card Validator](https://cards-dev.twitter.com/validator)

### Facebook

- **Page share**: Shows link preview with title, description, webcard
- **Image share**: May play GIF animation inline
- **Animation**: Sometimes plays in preview (Facebook supports GIF playback)
- **Cache**: Use [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/) to refresh

### Slack / Discord

- **Link unfurl**: Shows rich preview with title, description, first frame
- **Direct image**: May play GIF on hover or inline
- **No cache issue**: Re-fetches on each share

---

## How-To Recipes

### Share a Publication on LinkedIn (Mobile)

```
Step 1 — Open the publication on GitHub Pages
         URL must start with: packetqc.github.io/knowledge/
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
         https://packetqc.github.io/knowledge/publications/<slug>/

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
         • Title matches your publication
         • Description is correct
         • Image shows your webcard (first frame)
         • Canonical URL points to packetqc.github.io (not github.com)

Step 5 — If correct, share the link — LinkedIn now uses the fresh data
```

### Showcase the Animation (Not the Page)

```
Step 1 — Find the webcard URL:
         https://packetqc.github.io/knowledge/assets/og/<card>-<lang>.gif
         Example: .../assets/og/distributed-minds-en.gif

Step 2 — Share this URL directly in your post

Step 3 — On some platforms (Facebook, Slack), the animation will play
         On LinkedIn/Twitter, only the first frame shows
```

---

## Troubleshooting

### LinkedIn shows wrong preview or links to GitHub markdown

**Symptoms**: Shared the page, but clicking the link in LinkedIn goes to `github.com/packetqc/knowledge/blob/...` instead of `packetqc.github.io/knowledge/...`.

**Causes and fixes**:

| Cause | Fix |
|-------|-----|
| You were on the GitHub markdown view, not GitHub Pages | Check URL bar: must be `packetqc.github.io`, not `github.com` |
| LinkedIn cached a stale preview | Use [Post Inspector](https://www.linkedin.com/post-inspector/) to refresh |
| Missing canonical tag | Fixed in v20 — `<link rel="canonical">` added to both layouts |
| og:url pointing to wrong URL | Verify front matter has correct `permalink` |

### Preview shows no image

- Verify `og_image` front matter is set in the page's YAML
- Check that the GIF file exists in `docs/assets/og/`
- Run `webcard <target>` to regenerate missing GIFs
- Use platform-specific debugger to check what the crawler sees

### Animation doesn't play on social media

**This is expected behavior.** LinkedIn, Twitter, and Facebook show the first frame as a static preview. Animation only plays:
- On the GitHub Pages site (page header)
- When viewing the GIF URL directly in a browser
- In some messaging apps (Slack, Discord, iMessage)

Design every webcard so the first frame is self-explanatory.

### Shared on mobile but link is wrong

When using the mobile browser's "Share" function:
1. The browser shares the URL from the address bar
2. If you navigated from GitHub to a publication, you may be on `github.com` (the markdown renderer), not `packetqc.github.io` (GitHub Pages)
3. Always navigate to the GitHub Pages URL directly before sharing

**Quick check**: Look at the page — if you see a full-width animated GIF header at the top, you're on GitHub Pages. If you see rendered markdown without a header, you're on GitHub.

---

## Technical Architecture

### HTML Integration

Both layouts (`default.html` and `publication.html`) include:

```html
<!-- OG image for social sharing -->
<meta property="og:image" content="{{ page.og_image | absolute_url }}" />

<!-- Canonical URL — LinkedIn uses this as click-through -->
<link rel="canonical" href="{{ page.url | absolute_url }}" />

<!-- Page header display -->
<div class="webcard-header">
  <img src="{{ page.og_image | relative_url }}" alt="{{ page.title }}" />
</div>
```

### Front Matter

Every page requires `og_image` in its YAML front matter:

```yaml
og_image: /assets/og/distributed-minds-en.gif
```

Naming convention: `assets/og/<page-type>-<lang>.gif`

### Generator

`scripts/generate_og_gifs.py` generates all webcards:

```bash
python3 scripts/generate_og_gifs.py              # All cards
python3 scripts/generate_og_gifs.py #5            # One publication
python3 scripts/generate_og_gifs.py profile       # One group
```

### GIF Optimization

- 256-color palette per frame (MEDIANCUT quantization)
- Floyd-Steinberg dithering for smooth gradients
- Individual frame sizes: 150-694 KB
- Total for all 20 GIFs: ~3.5 MB

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge](../knowledge-system/v1/README.md) | Parent — webcards are part of the system |
| 3 | [AI Session Persistence](../ai-session-persistence/v1/README.md) | Has `cartoon` type webcard (Vicky NPC→AWARE) |
| 4 | [Distributed Minds](../distributed-minds/v1/README.md) | Has `split-panel` type webcard |
| 4a | [Knowledge Dashboard](../distributed-knowledge-dashboard/v1/README.md) | Has data-driven `split-panel` webcard |

---

*Authors: Martin Paquet (packetqcca@gmail.com) & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
