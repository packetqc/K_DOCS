---
layout: publication
title: "Normalize & Structure Concordance — Complete Documentation"
description: "Complete documentation for the normalize command: 7 concordance categories, detailed rules for structure/layout/webcard/link/asset/mindset/branch checks, output format, auto-fix behavior, integration with other knowledge commands, and when to run."
pub_id: "Publication #6 — Full"
version: "v2"
date: "2026-03-16"
permalink: /publications/normalize-structure-concordance/full/
og_image: /assets/og/normalize-en-cayman.gif
keywords: "normalize, concordance, structure, validation, bilingual, audit"
---

# Normalize & Structure Concordance — Complete Documentation
{: #pub-title}

**Contents**

| | |
|---|---|
| [Authors](#authors) | Publication authors |
| [Abstract](#abstract) | Self-healing knowledge architecture overview |
| [What Normalize Checks](#what-normalize-checks) | The 7 concordance categories at a glance |
| [Usage](#usage) | Command syntax and mode behavior |
| [Concordance Rules in Detail](#concordance-rules-in-detail) | Full specification of every check |
| &nbsp;&nbsp;[1. Structure Concordance](#1-structure-concordance) | EN/FR mirrors, hub-subpage links, summary-complete links |
| &nbsp;&nbsp;[2. Layout Concordance](#2-layout-concordance) | Front matter fields, table styling standard |
| &nbsp;&nbsp;[3. Webcard Concordance](#3-webcard-concordance) | OG GIF existence, meta tags, naming convention |
| &nbsp;&nbsp;[4. Link Concordance](#4-link-concordance) | Cross-references, language toggles, hardcoded paths |
| &nbsp;&nbsp;[5. Asset Concordance](#5-asset-concordance) | Required files and formats |
| &nbsp;&nbsp;[6. Mindset Concordance](#6-mindset-concordance) | mind_memory.md and domain JSON currency checks |
| &nbsp;&nbsp;[7. Branch Concordance](#7-branch-concordance) | Default branch detection and GitHub Pages config |
| [Output Format](#output-format) | Example normalize report output |
| [How Fixes Are Applied](#how-fixes-are-applied) | Auto-fixable vs manual issues |
| [When to Run](#when-to-run) | Triggers and recommended timing |
| [Integration with Other Commands](#integration-with-other-commands) | How normalize works with other commands |
| [Related Publications](#related-publications) | Sibling and parent publications |

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Designed the concordance auditing system to keep the knowledge architecture consistent as it grows — bilingual mirrors, front matter validation, link integrity, and asset synchronization.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Implements the normalize checks, detects structural drift, and applies fixes autonomously when authorized.

---

## Abstract

As Knowledge grows — new pages, publications, bilingual mirrors, profile variations, OG webcards — structural inconsistencies inevitably appear. A French page missing its English mirror. A profile page that forgot to list the latest publication. An OG image reference pointing to a non-existent GIF.

The `normalize` command is the **self-healing layer** of the knowledge architecture. It audits the entire repo structure against 7 categories of concordance rules and reports (or fixes) every deviation. Think of it as a linter for knowledge architecture — not code syntax, but structural integrity.

---

## What Normalize Checks

| # | Category | What it ensures |
|---|----------|----------------|
| 1 | **Structure** | Every EN page has an FR mirror. Hub pages link to all subpages. |
| 2 | **Layout** | All pages use correct layouts with required front matter fields. |
| 3 | **Webcard** | Every page has an animated OG GIF and correct `og_image` front matter. |
| 4 | **Link** | Cross-references are consistent — landing pages, indexes, profiles interlinked. |
| 5 | **Asset** | Required assets exist (social preview, OG GIFs, portraits). |
| 6 | **Mindset** | mind_memory.md reflects current state — publications, evolution entries, module structure. |
| 7 | **Branch** | Default branch detected, GitHub Pages configured, PRs target correctly. |

---

## Usage

```
normalize              # Report only (default: --check)
normalize --check      # Report only, no changes
normalize --fix        # Apply fixes automatically
```

**Mode behavior:**

| Mode | Behavior |
|------|----------|
| `--check` (default) | Scans everything, reports what passed and what failed, suggests fixes. Read-only — never modifies files. |
| `--fix` | Scans everything, reports results, and applies fixes automatically where possible. Some issues require manual intervention (reported but not auto-fixed). |

---

## Concordance Rules in Detail

### 1. Structure Concordance

Every page must have its bilingual mirror:

```
/profile/                        ↔ /fr/profile/
/profile/resume/                 ↔ /fr/profile/resume/
/profile/full/                   ↔ /fr/profile/full/
/publications/<id>/              ↔ /fr/publications/<id>/              (summary)
/publications/<id>/full/         ↔ /fr/publications/<id>/full/         (complete)
```

**What gets checked:**

| Check | Rule |
|-------|------|
| EN/FR mirrors | EN page exists → FR mirror must exist (and vice versa) |
| Hub → subpages | Hub pages must link to all their subpages |
| Subpage → hub | Subpages must link back to their hub |
| Language mirror | Subpages must link to their language mirror |
| Summary → complete | Publication summaries link to their complete pages |
| Complete → summary | Complete pages link back to their summaries |

**Common failures:**

| Failure | Description |
|---------|-------------|
| Missing FR mirror | New page created in EN but FR mirror forgotten |
| Incomplete publication | New publication added but only EN summary created |
| Stale hub page | Hub page not updated to include new subpage |

### 2. Layout Concordance

All web pages use the correct layout with required front matter:

**Required front matter fields (all pages):**

| Field | Example | Purpose |
|-------|---------|---------|
| `layout` | `publication` or `default` | Jekyll layout template |
| `title` | `"Webcards & Social Sharing"` | Page title, OG title |
| `description` | `"Every knowledge page..."` | Meta description, OG description |
| `permalink` | `/publications/webcards-social-sharing/` | Canonical URL path |
| `og_image` | `/assets/og/webcards-social-sharing-en.gif` | Social preview image |

**Additional fields for publication pages:**

| Field | Example | Purpose |
|-------|---------|---------|
| `pub_id` | `"Publication #5"` or `"Publication #5 — Full"` | Publication identifier |
| `version` | `"v1"` | Content version |
| `date` | `"2026-02-19"` | Publication date |

**Table styling standard** — applied uniformly via layout CSS:

| Property | Value |
|----------|-------|
| Font | 0.82rem, line-height 1.4 (smaller than body text for density) |
| Cell padding | 0.35rem 0.5rem (tight but readable) |
| Headers | white-space: nowrap (prevents column header wrapping) |
| Code in cells | 0.78rem (proportionally smaller) |
| Overflow | `.table-wrap` class for horizontal scroll on narrow viewports |

### 3. Webcard Concordance

Every web page must have a unique animated OG social preview:

**What gets checked:**

| Check | Rule |
|-------|------|
| Front matter | `og_image` front matter is set in every page |
| GIF exists | The referenced GIF file exists in `docs/assets/og/` |
| Meta tags | Both layouts emit `og:image` and `twitter:image` meta tags |
| Canonical link | `<link rel="canonical">` tag is present (critical for LinkedIn) |
| Naming convention | Naming follows `assets/og/<page-type>-<lang>.gif` |
| Bilingual variants | Both EN and FR variants exist for every card |
| Format | Images are 1200x630 animated GIF format |

**Card inventory (expected):**

| Card name | EN GIF | FR GIF |
|-----------|--------|--------|
| profile-hub | `profile-hub-en.gif` | `profile-hub-fr.gif` |
| resume | `resume-en.gif` | `resume-fr.gif` |
| full-profile | `full-profile-en.gif` | `full-profile-fr.gif` |
| knowledge-system | `knowledge-system-en.gif` | `knowledge-system-fr.gif` |
| mplib-pipeline | `mplib-storage-pipeline-en.gif` | `mplib-storage-pipeline-fr.gif` |
| live-session | `live-session-analysis-en.gif` | `live-session-analysis-fr.gif` |
| ai-persistence | `ai-session-persistence-en.gif` | `ai-session-persistence-fr.gif` |
| distributed-minds | `distributed-minds-en.gif` | `distributed-minds-fr.gif` |
| knowledge-dashboard | `knowledge-dashboard-en.gif` | `knowledge-dashboard-fr.gif` |
| webcards-social-sharing | `webcards-social-sharing-en.gif` | `webcards-social-sharing-fr.gif` |
| publications-index | `publications-index-en.gif` | `publications-index-fr.gif` |

### 4. Link Concordance

Cross-references must be consistent across the entire site:

| Link type | What it checks |
|-----------|---------------|
| Landing → hub | `docs/index.md` links to profile hub and publications index |
| Index → profiles | Publications index links to author profile |
| Profiles → pubs | Profile pages link to all publications |
| Knowledge ref | `packetqc/knowledge` referenced in contact tables and footers |
| mind_memory.md links | Web links in mind_memory.md match actual permalinks |
| Language toggle | Every page links to its mirror language |
| Summary → complete | Summary pages link to their `/full/` page |
| Complete → summary | Complete pages link back to summary |
| No hardcoded paths | All internal links use `relative_url` filter |
| No broken links | All internal link targets exist as actual pages |

### 5. Asset Concordance

Required assets exist and are in correct format:

| Asset | Expected path | Format |
|-------|------|--------|
| Social preview | `assets/social-preview.png` | 1280x640 PNG |
| Social preview source | `assets/social-preview.svg` | SVG |
| OG GIFs | `assets/og/*.gif` | 1200x630 animated GIF |
| Portrait photo | `references/Martin/me3.JPG` | 782x840 JPEG |
| Vicky avatar | `references/Martin/vicky.png` | 460x460 PNG |
| Publication assets | `publications/<slug>/v1/assets/*` | Various |

**Publication asset sync:** For publications with dedicated assets, `normalize` checks that all files in `publications/<slug>/v1/assets/` and `media/` are synced to `docs/publications/<slug>/assets/` (accessible by web pages).

### 6. Mindset Concordance

mind_memory.md and domain JSONs must reflect the current state:

| Check | What it verifies |
|-------|-----------------|
| Directive grid | Matches actual publications and module structure |
| Domain JSONs | Module conventions.json and work.json match actual state |
| Evolution table | Has recent entries (warns if last entry > 7 days old) |
| Version references | `knowledge-version: vN` matches current version |
| Profile links | Web profile and resume links are valid |
| `pub list` example | Output example matches actual publication count |

### 7. Branch Concordance

| Check | How it verifies |
|-------|----------------|
| Default branch | `git remote show origin \| grep 'HEAD branch'` |
| GitHub Pages source | Reports expected configuration (cannot auto-fix repo settings) |
| PR target | Verifies PRs should target the default branch |
| Task branches | `claude/<task-id>` branches are ephemeral — not expected to persist |

---

## Output Format

```
=== Normalize Report ===

Structure concordance:
  ✓  22 EN/FR page pairs found
  ✓  All hub pages link to subpages
  ✗  /fr/publications/webcards-social-sharing/full/ — missing back-link to summary

Layout concordance:
  ✓  All pages have required front matter
  ✗  /publications/knowledge-system/index.md — missing pub_id field

Webcard concordance:
  ✓  20 OG GIFs found (10 pages × 2 languages)
  ✓  All og_image references valid

Link concordance:
  ✓  Landing page links valid
  ✗  /publications/index.md:15 — hardcoded path (should use relative_url)

Asset concordance:
  ✓  Social preview exists
  ✓  All reference assets present

Mindset concordance:
  ✓  mind_memory.md publications nodes up to date
  ✗  mind_memory.md webcard registry missing #6

Branch concordance:
  ✓  Default branch: main
  ✓  GitHub Pages: main

Summary: 28 checks passed, 3 issues found
```

---

## How Fixes Are Applied

When run with `--fix`:

| Issue type | Auto-fixable | How |
|-----------|-------------|-----|
| Missing front matter field | Yes | Add field with sensible default |
| Missing language toggle link | Yes | Add link to mirror page |
| Hardcoded path | Yes | Replace with `relative_url` filter |
| Missing OG GIF reference | Partial | Set `og_image` in front matter (GIF generated separately) |
| Missing FR mirror page | No | Reports — translation needs human review |
| Missing publication index entry | Yes | Add entry following existing pattern |
| Missing profile entry | Yes | Add row to publication table |
| mind_memory.md/domain JSONs out of date | Yes | Add missing entries |
| Missing back-link | Yes | Add link following existing pattern |
| Missing summary-to-complete link | Yes | Add link at bottom of summary page |

**Semi-automatic delivery**: Like all write operations, `normalize --fix` commits to the assigned task branch and creates a PR targeting the default branch. The user approves the PR to deliver fixes.

---

## When to Run

| Trigger | Why |
|---------|-----|
| After adding new pages | Ensure EN/FR mirrors, front matter, OG images |
| After adding publications | Ensure 3-tier structure, index entries, profile entries |
| Before creating a PR | Catch issues before they reach main |
| On session start (knowledge repo) | Self-check via `/mind-context` |
| After promoting to domain JSONs | New conventions.json/work.json entries may need cross-refs |
| After `webcard` generation | Verify GIFs exist and front matter references them |
| After `pub new` | Verify scaffolded publication is complete |
| Periodically | Detect drift from manual edits or external changes |

---

## Integration with Other Commands

| Command | How it uses normalize |
|---------|----------------------|
| Session start | Runs implicit check when knowledge repo is active project |
| `pub check` | Uses normalize's validation rules for publication-specific checks |
| `docs check` | Uses normalize's page validation logic |
| `commit+push` | Normalize recommended before committing to catch issues early |
| K_GITHUB sync | Normalize verifies dashboard updates are structurally consistent |
| Domain JSON update | After updating conventions.json or work.json, normalize ensures cross-refs |
| `webcard` | After GIF generation, normalize verifies references |
| `pub new` | After scaffolding, normalize verifies completeness |

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — normalize is part of the system |
| 5 | [Webcards & Social Sharing]({{ '/publications/webcards-social-sharing/' | relative_url }}) | Normalize verifies webcard concordance |
| 4a | [Knowledge Dashboard]({{ '/publications/distributed-knowledge-dashboard/' | relative_url }}) | Normalize verifies dashboard consistency |
| 4 | [Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }}) | Normalize checks satellite-related references |
| 14 | [Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }}) | Multi-module architecture design |
| 0v2 | [Knowledge 2.0]({{ '/publications/knowledge-2.0/' | relative_url }}) | K2.0 multi-module architecture reference |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
