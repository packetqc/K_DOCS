---
layout: publication
title: "Tableau de bord des connaissances distribuées — Statut du cerveau maître et du réseau satellite"
description: "Tableau de bord vivant suivant le réseau de connaissances distribuées : version du cerveau maître, statut des projets satellites, dérive de version, connaissances récoltées et publications découvertes. Mis à jour à chaque synchronisation K_GITHUB."
pub_id: "Publication #4a"
version: "v3"
date: "2026-03-16"
permalink: /fr/publications/distributed-knowledge-dashboard/
og_image: /assets/og/knowledge-dashboard-fr-cayman.gif
keywords: "tableau de bord, satellites, bilan de santé, dérive, sévérité, état du réseau"
---

# Tableau de bord des connaissances distribuées — Statut du cerveau maître et du réseau satellite
{: #pub-title}

> **Publication parente** : [#4 — Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) — l'architecture que ce tableau de bord visualise | **Référence core** : [#14 — Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Concept et objectif du tableau de bord vivant |
| [Réseau satellite](#réseau-satellite) | Inventaire satellite en temps réel avec icônes de sévérité |
| [Connaissances acquises](#connaissances-acquises) | Découvertes récoltées avec flux de promotion |
| [Publications découvertes](#publications-découvertes) | Contenu technique trouvé dans les dépôts satellites |
| [Statut du cerveau maître](#statut-du-cerveau-maître) | Version et statistiques du dépôt central |
| [Le réseau](#le-réseau) | Composants et leurs rôles |
| [Couches de connaissances](#couches-de-connaissances) | Hiérarchie core, prouvé, récolté, session |
| [Cycle de vie d'une découverte](#cycle-de-vie-dune-découverte) | De la note de session aux connaissances core |

## Résumé

Les assistants de codage IA acquièrent une mémoire persistante via `mind_memory.md` et `sessions/` — mais chaque projet évolue indépendamment. Le **système de Knowledge distribuées** les connecte : un cerveau maître pousse le module K_MIND vers les satellites au démarrage de session, et K_GITHUB `sync_github.py` synchronise les connaissances évoluées.

Cette publication est un **tableau de bord vivant** — mis à jour à chaque synchronisation K_GITHUB. C'est la conscience de soi du réseau.

## Réseau satellite

> Mis à jour à chaque synchronisation K_GITHUB. N'inclut que les dépôts que l'utilisateur possède et auxquels Claude Code a reçu accès — aucun dépôt externe ou tiers.

<div class="table-wrap" markdown="1">

| Satellite | Version | Dérive | Bootstrap | Sessions | Assets | Live | Pubs | Santé | Harvest |
|-----------|---------|--------|-----------|----------|--------|------|------|-------|---------|
|[knowledge](https://github.com/packetqc/knowledge) (self)|v47|🟢 0|🟢 **core**|🟢 16|🟢 core|🟢 1| sain | 2026-03-03 |2026-02-23|
|[MPLIB](https://github.com/packetqc/MPLIB)|v31|🔴 16|🟢 actif|🟢 2|🟢 déployé|⚪ 0| sain | 2026-03-03 |2026-02-22|
| [knowledge-live](https://github.com/packetqc/knowledge-live) | v39 | 🔴 8 | 🟢 actif | 🟢 7 | 🟢 déployé | ⚪ 0 | 1 | 🟢 sain | 2026-02-24 |
|[STM32N6570-DK_SQLITE](https://github.com/packetqc/STM32N6570-DK_SQLITE)|v31|🔴 16|🟢 actif|🟢 3|🟢 déployé|⚪ 0| sain | 2026-03-03 |2026-02-22|
| [MPLIB_DEV_STAGING](https://github.com/packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE) | v31 | 🔴 16 | 🟢 actif | 🟢 5 | 🟢 déployé | ⚪ 0 | 0 | 🔴 inaccessible | 2026-02-22 |
|[PQC](https://github.com/packetqc/PQC)|v0|🔴 47|🔴 manquant|⚪ 0|🔴 manquant|⚪ 0| sain | 2026-03-03 |2026-02-22|

</div>

> **Icônes** : 🟢 actuel/sain — 🟡 dérive mineure — 🟠 dérive modérée — 🔴 critique/manquant — ⚪ inactif

## Connaissances acquises

> Cliquez sur une commande pour la copier — collez-la dans Claude Code pour avancer la découverte.
>
> **Flux** : `synchronisé` → 🔍 réviser dans `far_memory archives/` → 📦 assigner type → ✅ promouvoir vers `conventions.json` ou `work.json`

| # | Découverte | Source | Statut | Actions |
|---|------------|--------|--------|---------|
| 1 | Dégradation taille cache pages (81%) | STM32N6570-DK_SQLITE | récolté | 🔍 `harvest --review 1` 📦 `harvest --stage 1 lesson` ✅ `harvest --promote 1` 🔄 `harvest --auto 1` |
| 2 | Latence printf en chemin critique (1-5 ms) | STM32N6570-DK_SQLITE | récolté | 🔍 `harvest --review 2` 📦 `harvest --stage 2 lesson` ✅ `harvest --promote 2` 🔄 `harvest --auto 2` |
| 3 | Mismatch taille slot vs page (memsys5) | STM32N6570-DK_SQLITE | récolté | 🔍 `harvest --review 3` 📦 `harvest --stage 3 lesson` ✅ `harvest --promote 3` 🔄 `harvest --auto 3` |
| 4 | Abstraction multi-RTOS (FreeRTOS/ThreadX) | MPLIB | récolté | 🔍 `harvest --review 4` 📦 `harvest --stage 4 pattern` ✅ `harvest --promote 4` 🔄 `harvest --auto 4` |
| 5 | Limitation CubeMX N6570-DK | MPLIB | récolté | 🔍 `harvest --review 5` 📦 `harvest --stage 5 lesson` ✅ `harvest --promote 5` 🔄 `harvest --auto 5` |
| 6 | TouchGFX MVP avec services backend | MPLIB | récolté | 🔍 `harvest --review 6` 📦 `harvest --stage 6 pattern` ✅ `harvest --promote 6` 🔄 `harvest --auto 6` |
| 7 | Dimensionnement ML-KEM/ML-DSA embarqué | PQC | récolté | 🔍 `harvest --review 7` 📦 `harvest --stage 7 pattern` ✅ `harvest --promote 7` 🔄 `harvest --auto 7` |
| 8 | Conformité librairies PQC (WolfSSL=prod) | PQC | récolté | 🔍 `harvest --review 8` 📦 `harvest --stage 8 pattern` ✅ `harvest --promote 8` 🔄 `harvest --auto 8` |
| 9 | Pattern stockage certificats en flash | PQC | récolté | 🔍 `harvest --review 9` 📦 `harvest --stage 9 pattern` ✅ `harvest --promote 9` 🔄 `harvest --auto 9` |
| 10 | Méthodologie de staging de modules assistée par IA | MPLIB_DEV_STAGING_WITH_CLAUDE | récolté | 🔍 `harvest --review 10` 📦 `harvest --stage 10 methodology` ✅ `harvest --promote 10` 🔄 `harvest --auto 10` |
| 11 | Opérations d'instances parallèles (core + satellite) | MPLIB_DEV_STAGING_WITH_CLAUDE | récolté | 🔍 `harvest --review 11` 📦 `harvest --stage 11 methodology` ✅ `harvest --promote 11` 🔄 `harvest --auto 11` |
| 12 | Cycle de vie bootstrap en deux fusions (bootstrap → normalize → healthcheck) | MPLIB_DEV_STAGING_WITH_CLAUDE | récolté | 🔍 `harvest --review 12` 📦 `harvest --stage 12 methodology` ✅ `harvest --promote 12` 🔄 `harvest --auto 12` |
| 13 | Principe de wrapper minimal satellite (~30 lignes, pas ~120) | MPLIB_DEV_STAGING_WITH_CLAUDE | récolté | 🔍 `harvest --review 13` 📦 `harvest --stage 13 methodology` ✅ `harvest --promote 13` 🔄 `harvest --auto 13` |
| 14 | Méthodologie relais d'évolution — nouveau type `evolution` pour harvest | knowledge-live | **promu** | ✅ Promu comme entrée d'évolution v39 |
| 15 | Projets gérés — scaffold sous-dossier, routage harvest | knowledge-live | **promu** | ✅ Promu comme P6 + mise à jour méthodologie |
| 16 | Convergence autonome — sessions élevées convergent sans relais humain | knowledge-live | récolté | 🔍 `harvest --review 16` 📦 `harvest --stage 16 pattern` ✅ `harvest --promote 16` 🔄 `harvest --auto 16` |
| 17 | Intégration PQC beacon — protocole v0→v1, flag --secure | knowledge-live | récolté | 🔍 `harvest --review 17` 📦 `harvest --stage 17 docs` ✅ `harvest --promote 17` 🔄 `harvest --auto 17` |
| 18 | Intégration bidirectionnelle GitHub Project | knowledge-live | **promu** | ✅ Promu vers methodology/github-project-integration.md |
| 19 | Convention TAG: — miroir de la structure knowledge | knowledge-live | **promu** | ✅ Promu vers methodology/github-project-integration.md |
| 20 | Convention entité — #N:story/#N:task/#N:bug | knowledge-live | **promu** | ✅ Promu vers methodology/github-project-integration.md |
| 21 | Qualité candidate « Intégré » — intégration plateforme | knowledge-live | **promu** | ✅ Promu comme qualité core #13 dans CLAUDE.md |
| 22 | Lecteur de tableau de bord gh_helper.py + réconciliation bidirectionnelle | knowledge-live | **promu** | ✅ Promu vers core scripts/gh_helper.py (836→1494 lignes) |
| 23 | Feuille de route dynamique — publication web pilotée par le tableau de bord | knowledge-live | **promu** | ✅ Promu vers core scripts/sync_roadmap.py + méthodologie |
| 24 | Preuve autonome — cycle zéro intervention manuelle GitHub UI | knowledge-live | **promu** | ✅ Promu vers methodology/github-project-integration.md |

## Publications découvertes

Publications détectées dans les dépôts satellites :

| Titre | Satellite | Statut | Actions |
|-------|-----------|--------|---------|
| Doc architecture (pipeline SQLite) | STM32N6570-DK_SQLITE | **publié** — Publication core #1 | 🔍 `harvest --review pub:stm32` |
| #1 Intégration GitHub Project | knowledge-live | récolté — trois niveaux bilingue | 🔍 `harvest --review pub:kl1` |

## Statut du cerveau maître

| Champ | Valeur |
|-------|--------|
| Version actuelle | **v47** |
| Entrées d'évolution | 47 |
| Publications | 14 (#0–#12 + #4a tableau de bord + #9a conformité) |
| Patterns | 4 |
| Écueils documentés | 17 |

## Le réseau

| Composant | Rôle |
|-----------|------|
| **Cerveau maître** (`packetqc/knowledge`) | Dépôt central : module K_MIND, JSONs de domaine, publications |
| **Satellites** (dépôts projets) | Projets indépendants qui héritent et font évoluer les connaissances |
| **Push** (démarrage session) | Les satellites chargent le module K_MIND au démarrage — « mettre les lunettes » |
| **Sync** (entrant) | K_GITHUB `sync_github.py` synchronise les connaissances satellites de manière bidirectionnelle |
| **Versionnage** (v1–v47) | Chaque entrée d'évolution est une version. Dérive = satellite en retard. |

## Couches de connaissances

| Couche | Stabilité | Contenu |
|--------|-----------|---------|
| **Core** (mind_memory.md) | Stable | Grille de directives 264 nœuds — identité, méthodologie |
| **Prouvé** (conventions.json, work.json) | Validé | Éprouvé à travers les projets, par module |
| **Récolté** (far_memory archives/) | En évolution | Frais des expériences satellites |
| **Session** (sessions/) | Éphémère | near_memory + far_memory par session |

## Cycle de vie d'une découverte

```
Note de session → sync K_GITHUB → far_memory archives/ → validé entre projets → conventions.json/work.json → mind_memory.md
```

Les découvertes migrent vers le haut à travers les couches en prouvant leur valeur à travers plusieurs projets. Le tableau de bord suit cette progression — mis à jour à chaque synchronisation K_GITHUB.

---

[**Lire la documentation complète →**]({{ '/fr/publications/distributed-knowledge-dashboard/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
*Ceci est un document vivant — mis à jour à chaque synchronisation K_GITHUB.*
