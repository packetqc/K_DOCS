---
layout: default
title: "Changelog"
description: "Per-issue/PR chronological log of all changes. Factual audit trail — every issue and PR, in order."
permalink: /changelog/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "changelog, issues, pull requests, audit trail, knowledge system, changes"
---

# Changelog

Per-issue/PR chronological log of all changes. Each entry links to the GitHub issue or PR that produced the change.

**This is NOT the same as [News](/news/).** News is an editorial changelog organized by project, quality, structure, and type. Changelog is a factual, chronological audit trail — every issue and PR, in order.

Current version: **v56** | [Source: CHANGELOG.md](https://github.com/{{ site.github_repo }}/blob/main/CHANGELOG.md) | [News (editorial) →]({{ '/news/' | relative_url }})

---

## 2026-03-08

| Issue/PR | Type | Title | Labels |
|----------|------|-------|--------|
| — | Release | Knowledge 2.0 — Interactive Intelligence Framework. Web infrastructure import: 3 interfaces, 6 essential pages, repo-agnostic URL patterns. Migration from v1.10x (packetqc/knowledge). | RELEASE |

## 2026-03-04

| Issue/PR | Type | Title | Labels |
|----------|------|-------|--------|
| [#722](https://github.com/packetqc/knowledge/issues/722) | Issue | SESSION: Implement backup-* branch support in recall/recover memory search | SESSION, FEATURE |
| [#719](https://github.com/packetqc/knowledge/issues/719)–[#721](https://github.com/packetqc/knowledge/issues/721) | Issues | Gold release: inactive time note, recompile sessions, documentation updates | SESSION, ENHANCEMENT |
| [#713](https://github.com/packetqc/knowledge/pull/713)–[#718](https://github.com/packetqc/knowledge/pull/718) | PRs | Time compilation fixes — calendar span, end time bleeding, PR dedup, session scoping | |
| [#707](https://github.com/packetqc/knowledge/pull/707)–[#712](https://github.com/packetqc/knowledge/pull/712) | PRs | Session Viewer — CSS/JS extraction, scope pie chart fixes, collapsed defaults | |
| [#693](https://github.com/packetqc/knowledge/pull/693)–[#706](https://github.com/packetqc/knowledge/pull/706) | PRs | Session Viewer v2 — pie charts, session-scoped time, aggregation, tree table | |
| [#688](https://github.com/packetqc/knowledge/issues/688)–[#691](https://github.com/packetqc/knowledge/pull/691) | Issues+PRs | Native recover/recall Python modules + issue row restoration | SESSION, FEATURE |
| [#675](https://github.com/packetqc/knowledge/issues/675)–[#687](https://github.com/packetqc/knowledge/pull/687) | Issues+PRs | PreToolUse enforcement (v56), G7 enforcement, multi-issue notes, recall/recover split | |
| [#666](https://github.com/packetqc/knowledge/pull/666)–[#674](https://github.com/packetqc/knowledge/pull/674) | PRs | Session tree detection, multi-request detection, Gate G8, related issues enrichment | |

## 2026-03-03

| Issue/PR | Type | Title | Labels |
|----------|------|-------|--------|
| [#611](https://github.com/packetqc/knowledge/issues/611)–[#665](https://github.com/packetqc/knowledge/issues/665) | Issues+PRs | Session notes→issue (v55), custom avatars, Session Viewer fixes, profile restructure, version.json, orientation toggle, Gate G7, multi-issue metrics, related issues table | |
| [#610](https://github.com/packetqc/knowledge/issues/610) | Issue | SESSION: Session notes to issue + CHANGELOG.md | SESSION, ENHANCEMENT |
| [#608](https://github.com/packetqc/knowledge/pull/608) | PR | fix: enforce session lifecycle as mandatory — gates G1-G6 | |
| [#607](https://github.com/packetqc/knowledge/issues/607) | Issue | SESSION: Enforce Session Lifecycle as Mandatory | bug, SESSION |
| [#606](https://github.com/packetqc/knowledge/issues/606) | Issue | SESSION: Fix broken markdown table in knowledge-evolution-archive | bug, SESSION |
| [#605](https://github.com/packetqc/knowledge/pull/605) | PR | Fix broken markdown table in knowledge-evolution-archive.md | |
| [#604](https://github.com/packetqc/knowledge/pull/604) | PR | Add README.md and VERSION.md to essential files | |
| [#603](https://github.com/packetqc/knowledge/issues/603) | Issue | SESSION: Ajouter README.md aux fichiers essentiels | enhancement, SESSION |
| [#602](https://github.com/packetqc/knowledge/pull/602) | PR | healthcheck: satellite probe 2026-03-03 | |
| [#601](https://github.com/packetqc/knowledge/pull/601) | PR | docs: update CLAUDE.md with recent state | |
| [#600](https://github.com/packetqc/knowledge/issues/600) | Issue | SESSION: Update CLAUDE.md with recent state | enhancement, SESSION |

## 2026-03-02

| Issue/PR | Type | Title | Labels |
|----------|------|-------|--------|
| [#578](https://github.com/packetqc/knowledge/issues/578) | Issue | SESSION: Interface webcards for social sharing | SESSION |
| [#575](https://github.com/packetqc/knowledge/pull/575) | PR | docs: #0a Bootstrap Optimization annex | |
| [#574](https://github.com/packetqc/knowledge/pull/574) | PR | docs: CLAUDE.md condensation 3872 to 714 lines | |
| [#556](https://github.com/packetqc/knowledge/issues/556) | Issue | SESSION: Visual Documentation feature | SESSION |

## 2026-03-01

| Issue/PR | Type | Title | Labels |
|----------|------|-------|--------|
| [#544](https://github.com/packetqc/knowledge/pull/544) | PR | feat: iframe embed mode — export toolbar hidden | |
| [#543](https://github.com/packetqc/knowledge/pull/543) | PR | feat: iframe embed mode + universal pub-title anchors | |
| [#542](https://github.com/packetqc/knowledge/pull/542) | PR | feat: navigation state persistence | |
| [#525](https://github.com/packetqc/knowledge/pull/525)–[#541](https://github.com/packetqc/knowledge/pull/541) | PRs | Main Navigator left panel + command links | |
| [#524](https://github.com/packetqc/knowledge/pull/524) | PR | docs: session cache documentation sync | |
| [#522](https://github.com/packetqc/knowledge/pull/522)–[#523](https://github.com/packetqc/knowledge/pull/523) | PRs | Four-channel persistence model | |
| [#521](https://github.com/packetqc/knowledge/issues/521) | Issue | SESSION: Local Session Cache QA + Main Navigator | SESSION, REVIEW |

---

## Format Convention

| Field | Description |
|-------|-------------|
| **Issue/PR** | `#N` with link to GitHub |
| **Type** | `Issue` or `PR` |
| **Title** | Issue/PR title as written |
| **Labels** | GitHub labels |

**Relationship to [News](/news/)**: News is the editorial view — curated, categorized, explaining impact. Changelog is the raw log — every issue/PR, in chronological order, no editorial judgment.

---

*[News (editorial views) →]({{ '/news/' | relative_url }}) | [Plan →]({{ '/plan/' | relative_url }}) | [Links →]({{ '/links/' | relative_url }}) | [Publications →]({{ '/publications/' | relative_url }})*
