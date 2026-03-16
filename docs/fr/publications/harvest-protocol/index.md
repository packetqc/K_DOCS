---
layout: publication
title: "Protocole Harvest — Guide pratique de collecte de connaissances distribuées"
description: "Guide pratique des commandes harvest : extraire les connaissances des projets satellites, le pipeline de promotion (réviser → préparer → promouvoir), healthcheck réseau, remédiation des satellites, et flux de travail quotidiens."
pub_id: "Publication #7"
version: "v1"
date: "2026-02-19"
permalink: /fr/publications/harvest-protocol/
og_image: /assets/og/harvest-protocol-fr-cayman.gif
keywords: "récolte, promotion, bilan de santé, satellites, perspectives, dérive de version"
---

# Protocole Harvest — Guide pratique
{: #pub-title}

> **Publication parente** : [#0 — Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Architecture** : [#4 — Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Vue d'ensemble du guide pratique |
| [Référence rapide](#référence-rapide) | Toutes les commandes harvest en un coup d'oeil |
| [Concept fondamental](#concept-fondamental) | Flux bidirectionnel et portée d'accès |
| [Le pipeline de promotion](#le-pipeline-de-promotion) | Flux réviser, préparer, promouvoir |
| [Healthcheck réseau](#healthcheck-réseau) | Balayage complet avec icônes de sévérité |
| [Remédiation des satellites](#remédiation-des-satellites) | Correction de dérive basée sur le pull |
| [Flux de travail courants](#flux-de-travail-courants) | Vérification quotidienne, nouvelle découverte, procédures guidées |

## Résumé

La publication #4 (Connaissances distribuées) documente l'**architecture** du flux bidirectionnel de connaissances. Cette publication est le **guide pratique** — comment utiliser `harvest` au quotidien : extraire les connaissances des satellites, réviser les découvertes, promouvoir vers le core, exécuter des balayages réseau et corriger la dérive de version.

## Référence rapide

| Commande | Action |
|---------|--------|
| `harvest <projet>` | Extraire les connaissances d'un satellite dans `minds/` |
| `harvest --list` | Lister tous les projets avec version + dérive |
| `harvest --procedure` | Procédure guidée de promotion |
| `harvest --healthcheck` | Balayage réseau complet + auto-promotion |
| `harvest --review <N>` | Marquer comme révisé par l'humain |
| `harvest --stage <N> <type>` | Préparer pour intégration (lesson, pattern, methodology, evolution, docs) |
| `harvest --promote <N>` | Promouvoir vers le core maintenant |
| `harvest --auto <N>` | Mettre en file pour auto-promotion au prochain healthcheck |
| `harvest --fix <projet>` | Mettre à jour le CLAUDE.md du satellite |

## Concept fondamental

**Push** (sortant) : Au `wakeup`, les satellites lisent le cerveau maître. **Harvest** (entrant) : Le maître parcourt les satellites, extrait les connaissances évoluées, les place dans `minds/` pour révision.

**Portée d'accès** : Harvest n'opère que sur les dépôts que l'utilisateur possède et auxquels Claude Code a reçu accès via sa configuration d'application GitHub. Aucun dépôt externe ou tiers n'est jamais parcouru.

Tout accès satellite utilise le HTTPS public : `https://github.com/packetqc/<projet>`, ciblant la branche par défaut (`main` ou `master`).

## Le pipeline de promotion

```
récolté → 🔍 réviser → 📦 préparer → ✅ promouvoir (ou 🔄 auto)
```

| Étape | Action |
|-------|--------|
| **Harvest** | `harvest <projet>` extrait les découvertes dans `minds/` |
| **Réviser** | `harvest --review N` marque comme validé par l'humain (porte de qualité) |
| **Préparer** | `harvest --stage N lesson` assigne le type cible |
| **Promouvoir** | `harvest --promote N` écrit dans le core maintenant, ou `harvest --auto N` met en file |

## Healthcheck réseau

`harvest --healthcheck` balaye tous les satellites connus, met à jour les icônes de sévérité (🟢🟡🟠🔴⚪), traite la file d'auto-promotion et regénère les webcards du tableau de bord.

## Remédiation des satellites

`harvest --fix <projet>` prépare une mise à jour de version localement. Le satellite s'auto-répare au prochain `wakeup` en lisant le core mis à jour — basé sur le pull, pas le push (Claude Code ne peut pas pousser en cross-repo).

## Flux de travail courants

**Vérification quotidienne** : `harvest --list` → `harvest --healthcheck`

**Nouvelle découverte** : `harvest <projet>` → `harvest --review N` → `harvest --stage N lesson` → `harvest --promote N`

**Guidé** : `harvest --procedure` pour une procédure étape par étape avec l'état actuel.

---

[**Lire la documentation complète →**]({{ '/fr/publications/harvest-protocol/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
