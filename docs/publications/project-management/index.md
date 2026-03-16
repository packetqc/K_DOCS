---
layout: publication
title: "Project Management — First-Class Entities, Hierarchical Indexing, and Satellite Lifecycle"
description: "Projects as first-class entities in Knowledge: hierarchical indexing (P#/S#/D#), three-level entity model, satellite bootstrap protocol, web presence scaffolding, tagged input for scoped knowledge, dual-origin publishing, and GitHub Project integration."
pub_id: "Publication #12"
version: "v2"
date: "2026-03-16"
permalink: /publications/project-management/
og_image: /assets/og/project-management-en-cayman.gif
keywords: "project, management, indexing, satellite, bootstrap, hierarchy"
---

# Project Management — First-Class Entities
{: #pub-title}

> **Parent publication**: [#0 — Knowledge]({{ '/publications/knowledge-system/' | relative_url }}) | **Architecture**: [#4 — Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }}) | **Core reference**: [#14 — Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/publications/knowledge-2.0/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Project management system overview |
| [Project Entity Model](#project-entity-model) | Three-level entity: logical, physical, platform |
| [Hierarchical Indexing](#hierarchical-indexing-psd) | P#/S#/D# hierarchical identifier scheme |
| [Project Commands](#project-commands) | CLI commands for project management |
| [Satellite Bootstrap](#satellite-bootstrap-protocol) | Multi-round satellite installation protocol |
| [Web Presence Scaffolding](#web-presence-scaffolding) | GitHub Pages docs structure creation |
| [Tagged Input](#tagged-input--call-alias) | `#N:` scoped knowledge input system |
| [Dual-Origin Links](#dual-origin-link-system) | Core vs satellite origin badges |

## Abstract

As the knowledge network grew from 1 repo to 6+ projects with multiple satellites, a structural gap emerged: projects had no formal identity. Publication #12 documents the v35→K2.0 project entity model — hierarchical indexing (P#/S#/D#), three-level entities (logical, physical, platform), satellite lifecycle management, and the commands that operate on them. Consolidates four methodology documents: project management, satellite bootstrap, project create, and tagged input.

## Project Entity Model

A **project** exists at three levels: **logical** (organized work with publications, evolution, stories), **physical** (Git repositories, or **none** for managed projects), and **platform** (GitHub Project board). A project is not a repo — it has repos. Current registry: P0 (Knowledge, core), P1 (MPLIB), P2 (STM32 PoC), P3 (knowledge-live), P4 (MPLIB Dev Staging), P5 (PQC).

Three relationship types: **owns** (primary repo), **child-of** (sub-project), **managed** (no dedicated repository — lives in host repo or core, board always links to a repo).

## Hierarchical Indexing (P#/S#/D#)

Three levels: `P<n>` (project), `P<n>/S<m>` (satellite), `P<n>/#<pub>` or `P<n>/S<m>/D<k>` (document). Cross-project marker `->P<n>` shows when a publication documents a different project. Index appears left of status tag in all inventories.

## Project Commands

| Command | Action |
|---------|--------|
| `project list` | List all projects with P# index, type, status, satellite count |
| `project info <P#>` | Show project details — identity, publications, satellites, evolution |
| `project create <name>` | Full creation: register P# + scaffold + GitHub Project (elevated) + web |
| `project register <name>` | Register project with P# ID — creates `projects/<slug>.md` |
| `project review <P#>` | Review project state — docs, pubs, assets, freshness |
| `project review --all` | Review all projects |

## Satellite Bootstrap Protocol

Single-session iterative staging: Round 1 (bootstrap scaffold) -> Round 2 (normalize to critical-subset) -> Round 3 (web presence, optional). One manual step per round: merge the PR. Console guidance (human bridge) prints what happened, what the user needs to do, and what happens next at every step.

## Web Presence Scaffolding

`project create <name>` scaffolds a complete bilingual GitHub Pages site: Jekyll config, layouts (copied from knowledge), EN/FR landing pages, publications hubs, asset placeholders. 10 files, 6 directories. Self-contained — no external theme dependency.

## Tagged Input (`#` Call Alias)

`#N:` routes content to publication/project N. `#N:methodology:<topic>` and `#N:principle:<topic>` flag for K_GITHUB sync. `#N:info` shows accumulated knowledge. Raw dump mode — user provides intelligence, Claude classifies. Multi-satellite convergence: same project documented from any repo, K_GITHUB sync unifies.

## Dual-Origin Link System

Core links (`knowledge/`) are canonical. Satellite links (`<repo>/`) are staging. Both valid — same technology, different review stage. Origin badge in project hub pages.

---

[**Read the full documentation →**]({{ '/publications/project-management/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
