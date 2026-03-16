---
layout: publication
title: "Normalize & Structure Concordance — Self-Healing Knowledge Architecture"
description: "The normalize command audits and enforces concordance across Knowledge: bilingual mirrors, front matter validation, webcard references, link integrity, asset synchronization, and mind_memory.md currency. A linter for knowledge architecture."
pub_id: "Publication #6"
version: "v2"
date: "2026-03-16"
permalink: /publications/normalize-structure-concordance/
og_image: /assets/og/normalize-en-cayman.gif
keywords: "normalize, concordance, structure, validation, bilingual, audit"
---

# Normalize & Structure Concordance
{: #pub-title}

> **Parent publication**: [#0 — Knowledge]({{ '/publications/knowledge-system/' | relative_url }}) | **Core reference**: [#14 — Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/publications/knowledge-2.0/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Self-healing knowledge architecture overview |
| [What Normalize Checks](#what-normalize-checks) | The 7 concordance categories |
| [Usage](#usage) | Command syntax and modes |
| [Concordance Rules](#concordance-rules) | Summary of all validation rules |
| [When to Run](#when-to-run) | Triggers and recommended timing |
| [How Fixes Are Applied](#how-fixes-are-applied) | Auto-fix behavior and limitations |
| [Integration with Other Commands](#integration-with-other-commands) | How normalize works with other commands |

## Abstract

As Knowledge grows — new pages, publications, bilingual mirrors, profile variations, OG webcards — structural inconsistencies inevitably appear. A French page missing its English mirror. A profile page that forgot to list the latest publication. An OG image reference pointing to a non-existent GIF.

The `normalize` command is the **self-healing layer** of the knowledge architecture. It audits the entire repo against 7 categories of concordance rules and reports (or fixes) every deviation. Think of it as a linter for knowledge architecture — not code syntax, but structural integrity.

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

## Usage

```
normalize              # Report only (default)
normalize --check      # Report only, no changes
normalize --fix        # Apply fixes automatically
```

## Concordance Rules

| Category | Rule |
|----------|------|
| **Structure** | Every page must have its EN/FR mirror. Publications follow 3-tier structure (source, summary, complete). Hub pages link to all subpages; subpages link back. |
| **Layout** | All pages require `layout`, `title`, `description`, `permalink`, `og_image` in front matter. Publications additionally need `pub_id`, `version`, `date`. |
| **Webcard** | Every page's `og_image` must point to an existing `.gif` in `docs/assets/og/`. Both EN and FR variants must exist. Layouts must emit `og:image`, `twitter:image`, and `<link rel="canonical">` meta tags. |
| **Link** | No hardcoded paths — all internal links use `relative_url` filter. Language toggles present on every page. Cross-references between index, profile, and publication pages are consistent. |
| **Asset** | Social preview PNG, OG GIFs, portrait photo, and Vicky avatar all exist at expected paths. |
| **Mindset** | mind_memory.md directive grid, domain JSONs, and evolution entries match actual repo state. |
| **Branch** | Default branch detected via `git remote show origin`. PRs target it. GitHub Pages publishes from it. |

## When to Run

| Trigger | Why |
|---------|-----|
| After adding new pages or publications | Ensure EN/FR mirrors, front matter, OG images |
| Before creating a PR | Catch issues before they reach the default branch |
| On session start (knowledge repo) | Self-check via `/mind-context` |
| After promoting to domain JSONs | New conventions.json/work.json entries may need cross-refs |
| After `webcard` generation | Verify GIFs exist and front matter references them |

## How Fixes Are Applied

With `--fix`: missing front matter fields get sensible defaults, hardcoded paths get `relative_url`, missing index entries get added. Missing FR mirror pages are **reported but not auto-fixed** (translation needs human review). Like all write operations, fixes are committed to the task branch with a PR targeting the default branch.

## Integration with Other Commands

`pub check` and `docs check` use normalize's validation rules. Session start runs an implicit check when the knowledge repo is active. Commit+push benefits from a normalize run before committing.

---

[**Read the full documentation →**]({{ '/publications/normalize-structure-concordance/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
