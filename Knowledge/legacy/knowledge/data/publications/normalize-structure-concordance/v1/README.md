# Normalize & Structure Concordance

**Publication #6 — Self-Healing Knowledge Architecture**

*By Martin Paquet & Claude (Anthropic, Opus 4.6)*
*v1 — February 2026*

---

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Designed the concordance auditing system to keep the knowledge architecture consistent as it grows — bilingual mirrors, front matter validation, link integrity, and asset synchronization.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Implements the normalize checks, detects structural drift, and applies fixes autonomously when authorized.

---

## Abstract

As Knowledge grows — new pages, new publications, bilingual mirrors, profile variations, OG webcards — structural inconsistencies inevitably appear. A French page missing its English mirror. A profile page that forgot to list the latest publication. An OG image reference pointing to a non-existent GIF.

The `normalize` command is the **self-healing layer** of the knowledge architecture. It audits the entire repo structure against a defined set of concordance rules and reports (or fixes) every deviation. Think of it as a linter for knowledge architecture — not code syntax, but structural integrity.

---

## Table of Contents

- [What Normalize Checks](#what-normalize-checks)
- [Usage](#usage)
- [Concordance Rules](#concordance-rules)
  - [Structure Concordance](#1-structure-concordance)
  - [Layout Concordance](#2-layout-concordance)
  - [Webcard Concordance](#3-webcard-concordance)
  - [Link Concordance](#4-link-concordance)
  - [Asset Concordance](#5-asset-concordance)
  - [Mindset Concordance](#6-mindset-concordance)
  - [Branch Concordance](#7-branch-concordance)
- [When to Run](#when-to-run)
- [Output Format](#output-format)
- [How Fixes Are Applied](#how-fixes-are-applied)
- [Integration with Other Commands](#integration-with-other-commands)
- [Related Publications](#related-publications)

---

## What Normalize Checks

Normalize enforces **9 categories of concordance** across the knowledge repo:

| # | Category | What it ensures |
|---|----------|----------------|
| 1 | **Structure** | Every EN page has an FR mirror. Hub pages link to all subpages. |
| 2 | **Layout** | All pages use correct layouts with required front matter fields. |
| 3 | **Webcard** | Every page has an animated OG GIF and correct `og_image` front matter. |
| 4 | **Link** | Cross-references are consistent — landing pages, indexes, profiles all interlinked. |
| 5 | **Asset** | Required assets exist (social preview, OG GIFs, portraits, publication assets). |
| 6 | **Mindset** | CLAUDE.md reflects current state — publications table, evolution entries, commands. |
| 7 | **Branch** | Default branch detected, GitHub Pages configured, PRs target correct branch. |
| 8 | **Essential files** | README.md, PLAN.md, LINKS.md, NEWS.md, VERSION.md present and web mirrors synced. |
| 9 | **Projects folder** | Flat `.md` files only — no nested subdirectories. |

---

## Usage

```
normalize              # Report only (default: --check)
normalize --check      # Report only, no changes
normalize --fix        # Apply fixes automatically
```

**Mode behavior:**
- `--check` (default): Scans everything, reports what passed and what failed, suggests fixes. Read-only — never modifies files.
- `--fix`: Scans everything, reports results, and applies fixes automatically where possible. Some issues require manual intervention (reported but not auto-fixed).

---

## Concordance Rules

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
- EN page exists → FR mirror must exist (and vice versa)
- Hub pages must link to all their subpages
- Subpages must link back to their hub
- Subpages must link to their language mirror
- Publication summaries link to their complete pages
- Complete pages link back to their summaries

**Common failures:**
- New page created in EN but FR mirror forgotten
- New publication added but only EN summary created
- Hub page not updated to include new subpage

### 2. Layout Concordance

All web pages use the correct layout with required front matter:

**Required front matter fields:**
- `layout` — `default` or `publication`
- `title` — page title
- `description` — meta description for SEO and social sharing
- `permalink` — canonical URL path
- `og_image` — path to animated OG GIF

**Publication pages additionally require:**
- `pub_id` — e.g., "Publication #5" or "Publication #5 — Full"
- `version` — e.g., "v1"
- `date` — publication date

**Table styling standard** (enforced uniformly via layout CSS):
- Font: 0.82rem, line-height 1.4
- Cell padding: 0.35rem 0.5rem
- Headers: white-space: nowrap
- Code in cells: 0.78rem

### 3. Webcard Concordance

Every web page must have a unique animated OG social preview:

**What gets checked:**
- `og_image` front matter is set in every page
- The referenced GIF file exists in `docs/assets/og/`
- Both layouts emit `og:image` and `twitter:image` meta tags
- `<link rel="canonical">` tag is present
- Naming follows convention: `assets/og/<page-type>-<lang>.gif`
- Both EN and FR variants exist for every card

### 4. Link Concordance

Cross-references must be consistent across the entire site:

| Link type | What it checks |
|-----------|---------------|
| Landing → hub | `docs/index.md` links to profile hub and publications index |
| Index → profiles | Publications index links to author profile |
| Profiles → pubs | Profile pages link to publications |
| Knowledge ref | `packetqc/knowledge` referenced in contact tables and footers |
| CLAUDE.md links | Web links in CLAUDE.md match actual permalinks |
| Language toggle | Every page links to its mirror language |
| No hardcoded paths | All internal links use `relative_url` filter |

### 5. Asset Concordance

Required assets exist and are in correct format:

| Asset | Path | Format |
|-------|------|--------|
| Social preview | `assets/social-preview.png` | 1280×640 PNG |
| Social preview source | `assets/social-preview.svg` | SVG |
| OG GIFs | `assets/og/*.gif` | 1200×630 animated GIF |
| Portrait | `references/Martin/me3.JPG` | 782×840 JPEG |
| Vicky avatar | `references/Martin/vicky.png` | 460×460 PNG |
| Publication assets | `publications/<slug>/v1/assets/*` | Various |

### 6. Mindset Concordance

CLAUDE.md must reflect the current state:

- "Who Is Martin" section has correct profile links
- Knowledge Evolution table has recent entries
- Commands table includes all active commands
- Publications table matches actual publications
- Webcard registry matches actual cards

### 7. Branch Concordance

Repository branch configuration:

- Default branch detected: `git remote show origin | grep 'HEAD branch'`
- GitHub Pages publishes from the default branch
- PRs target the default branch
- Task branches (`claude/<task-id>`) are ephemeral

---

## When to Run

| Trigger | Why |
|---------|-----|
| After adding new pages | Ensure EN/FR mirrors, front matter, OG images |
| After adding publications | Ensure 3-tier structure, index entries, profile entries |
| Before creating a PR | Catch issues before they reach main |
| On `wakeup` (knowledge repo) | Self-check on session start |
| After `harvest --promote` | Promoted insights may add new patterns/lessons files |
| After `webcard` generation | Verify GIFs exist and front matter references them |

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
  ✓  CLAUDE.md publications table up to date
  ✗  CLAUDE.md webcard registry missing #6

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
| Missing OG GIF reference | Partial | Set `og_image` in front matter (GIF must be generated separately) |
| Missing FR mirror page | No | Reports the issue — content translation needs human review |
| Missing publication index entry | Yes | Add entry to index following existing pattern |
| CLAUDE.md table out of date | Yes | Add missing entries |

**Semi-automatic delivery**: Like all write operations, `normalize --fix` commits to the assigned task branch and creates a PR targeting `main`. The user approves the PR to deliver fixes.

---

## Integration with Other Commands

| Command | How it uses normalize |
|---------|----------------------|
| `wakeup` | Runs implicit check when knowledge repo is active |
| `pub check` | Uses normalize's validation rules for publications |
| `docs check` | Uses normalize's page validation logic |
| `save` | Normalize check recommended before save |
| `harvest` | Normalize verifies dashboard updates are consistent |
| `webcard` | Normalize verifies GIF references after generation |

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | Knowledge | Parent — normalize is part of the system |
| 5 | Webcards & Social Sharing | Normalize verifies webcard concordance |
| 4a | Knowledge Dashboard | Normalize verifies dashboard data consistency |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
