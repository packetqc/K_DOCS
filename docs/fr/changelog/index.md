---
layout: default
title: "Knowledge — Journal des modifications"
description: "Journal chronologique par issue/PR de toutes les modifications du système Knowledge. Piste d'audit factuelle — chaque issue et PR, en ordre."
permalink: /fr/changelog/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "journal des modifications, issues, pull requests, piste d'audit, système de connaissances, changements"
---

# Journal des modifications

Journal chronologique par issue/PR de toutes les modifications. Chaque entrée pointe vers l'issue ou PR GitHub qui a produit le changement.

**Ce n'est PAS la même chose que les [Nouveautés](/fr/news/).** Les nouveautés sont un journal éditorial organisé par projet, qualité, structure et type. Le journal des modifications est une piste d'audit factuelle — chaque issue et PR, en ordre chronologique.

Version actuelle : **v56** | [Source : CHANGELOG.md](https://github.com/packetqc/knowledge/blob/main/CHANGELOG.md) | [Nouveautés (éditorial) →](/fr/news/)

---

## 2026-03-04

| Issue/PR | Type | Titre | Étiquettes |
|----------|------|-------|------------|
| [#722](https://github.com/packetqc/knowledge/issues/722) | Issue | SESSION: Support des branches backup-* dans recall/recover | SESSION, FEATURE |
| [#719](https://github.com/packetqc/knowledge/issues/719)–[#721](https://github.com/packetqc/knowledge/issues/721) | Issues | Livraison gold : note temps inactif, recompilation sessions, mises à jour docs | SESSION, ENHANCEMENT |
| [#713](https://github.com/packetqc/knowledge/pull/713)–[#718](https://github.com/packetqc/knowledge/pull/718) | PRs | Correctifs compilation temps — portée calendrier, fin temps, dédup PR, cadrage session | |
| [#707](https://github.com/packetqc/knowledge/pull/707)–[#712](https://github.com/packetqc/knowledge/pull/712) | PRs | Session Viewer — extraction CSS/JS, correctifs diagramme portée, défauts repliés | |
| [#693](https://github.com/packetqc/knowledge/pull/693)–[#706](https://github.com/packetqc/knowledge/pull/706) | PRs | Session Viewer v2 — diagrammes, temps cadré session, agrégation, table arbre | |
| [#688](https://github.com/packetqc/knowledge/issues/688)–[#691](https://github.com/packetqc/knowledge/pull/691) | Issues+PRs | Modules Python natifs recover/recall + restauration lignes issues | SESSION, FEATURE |
| [#675](https://github.com/packetqc/knowledge/issues/675)–[#687](https://github.com/packetqc/knowledge/pull/687) | Issues+PRs | Enforcement PreToolUse (v56), enforcement G7, notes multi-issues, séparation recall/recover | |
| [#666](https://github.com/packetqc/knowledge/pull/666)–[#674](https://github.com/packetqc/knowledge/pull/674) | PRs | Détection arbre session, détection multi-requêtes, Gate G8, enrichissement issues liées | |

## 2026-03-03

| Issue/PR | Type | Titre | Étiquettes |
|----------|------|-------|------------|
| [#611](https://github.com/packetqc/knowledge/issues/611)–[#665](https://github.com/packetqc/knowledge/issues/665) | Issues+PRs | Notes session→issue (v55), avatars, correctifs Session Viewer, profil restructuré, version.json, bascule orientation, Gate G7, métriques multi-issues, table issues liées | |
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

| Issue/PR | Type | Titre | Étiquettes |
|----------|------|-------|------------|
| [#578](https://github.com/packetqc/knowledge/issues/578) | Issue | SESSION: Interface webcards for social sharing | SESSION |
| [#575](https://github.com/packetqc/knowledge/pull/575) | PR | docs: #0a Bootstrap Optimization annex | |
| [#574](https://github.com/packetqc/knowledge/pull/574) | PR | docs: CLAUDE.md condensation 3872 → 714 lignes | |
| [#556](https://github.com/packetqc/knowledge/issues/556) | Issue | SESSION: Visual Documentation feature | SESSION |

## 2026-03-01

| Issue/PR | Type | Titre | Étiquettes |
|----------|------|-------|------------|
| [#544](https://github.com/packetqc/knowledge/pull/544) | PR | feat: iframe embed mode — export toolbar hidden | |
| [#543](https://github.com/packetqc/knowledge/pull/543) | PR | feat: iframe embed mode + universal pub-title anchors | |
| [#542](https://github.com/packetqc/knowledge/pull/542) | PR | feat: navigation state persistence | |
| [#525](https://github.com/packetqc/knowledge/pull/525)–[#541](https://github.com/packetqc/knowledge/pull/541) | PRs | Main Navigator left panel + command links | |
| [#524](https://github.com/packetqc/knowledge/pull/524) | PR | docs: session cache documentation sync | |
| [#522](https://github.com/packetqc/knowledge/pull/522)–[#523](https://github.com/packetqc/knowledge/pull/523) | PRs | Four-channel persistence model | |
| [#521](https://github.com/packetqc/knowledge/issues/521) | Issue | SESSION: Local Session Cache QA + Main Navigator | SESSION, REVIEW |

---

## Convention de format

| Champ | Description |
|-------|-------------|
| **Issue/PR** | `#N` avec lien vers GitHub |
| **Type** | `Issue` ou `PR` |
| **Titre** | Titre de l'issue/PR tel qu'écrit |
| **Étiquettes** | Étiquettes GitHub |

**Relation avec les [Nouveautés](/fr/news/)** : Les nouveautés sont la vue éditoriale — organisée, catégorisée, expliquant l'impact. Le journal des modifications est le log brut — chaque issue/PR, en ordre chronologique, sans jugement éditorial.

---

*[Nouveautés (vues éditoriales) →](/fr/news/) | [Plan →](/fr/plan/) | [Liens →](/fr/links/) | [Publications →](/fr/publications/)*
