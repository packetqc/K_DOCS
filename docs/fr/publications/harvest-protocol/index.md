---
layout: publication
title: "Protocole Harvest — Guide pratique de collecte de connaissances distribuées"
description: "Guide pratique des commandes harvest : extraire les connaissances des projets satellites, le pipeline de promotion (réviser → préparer → promouvoir), healthcheck réseau, remédiation des satellites, et flux de travail quotidiens."
pub_id: "Publication #7"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/harvest-protocol/
og_image: /assets/og/harvest-protocol-fr-cayman.gif
keywords: "récolte, promotion, bilan de santé, satellites, perspectives, dérive de version"
---

# Protocole Harvest — Guide pratique
{: #pub-title}

> **Publication parente** : [#0 — Système Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Référence core** : [#14 — Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }}) | **Architecture** : [#4 — Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }})

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

La publication #4 (Connaissances distribuées) documente l'**architecture** du flux bidirectionnel de connaissances. Cette publication est le **guide pratique** — comment K_GITHUB `sync_github.py` remplace les commandes `harvest` de K1.0 : synchroniser les connaissances depuis les satellites, gérer le pipeline de promotion, exécuter des balayages réseau et suivre la dérive de version.

## Référence rapide

| Commande | Action |
|---------|--------|
| K_GITHUB `sync_github.py <projet>` | Synchroniser depuis un satellite |
| Inventaire K_GITHUB | Lister les satellites avec version + dérive |
| K_GITHUB + K_VALIDATION `/integrity-check` | Balayage réseau |
| Manuel : mettre à jour `conventions.json` ou `work.json` | Promouvoir vers le core |
| K_GITHUB sync vers satellite | Corriger la dérive d'un satellite |

## Concept fondamental

**Push** (sortant) : au démarrage de session, les satellites lisent le module K_MIND. **Harvest** (entrant) : Le module parcourt les satellites, extrait les connaissances évoluées, les place dans `far_memory archives/` pour révision.

**Portée d'accès** : Harvest n'opère que sur les dépôts que l'utilisateur possède et auxquels Claude Code a reçu accès via sa configuration d'application GitHub. Aucun dépôt externe ou tiers n'est jamais parcouru.

Tout accès satellite utilise le HTTPS public : `https://github.com/packetqc/<projet>`, ciblant la branche par défaut (`main` ou `master`).

## Le pipeline de promotion

```
récolté → 🔍 réviser → 📦 préparer → ✅ promouvoir (ou 🔄 auto)
```

| Étape | Action |
|-------|--------|
| **Harvest** | `sync_github.py <projet>` extrait les découvertes dans `far_memory archives/` |
| **Réviser** | Révision manuelle — valider les connaissances extraites (porte de qualité) |
| **Préparer** | Identifier le type cible (lesson, pattern, methodology, evolution, docs) |
| **Promouvoir** | Mettre à jour manuellement `conventions.json` ou `work.json` dans K_MIND |

## Healthcheck réseau

K_GITHUB `sync_github.py` + K_VALIDATION `/integrity-check` balayent tous les satellites connus, mettent à jour les icônes de sévérité (🟢🟡🟠🔴⚪) et regénèrent les webcards du tableau de bord.

## Remédiation des satellites

K_GITHUB `sync_github.py` prépare une mise à jour de version localement. Le satellite s'auto-répare au prochain démarrage de session en lisant le module K_MIND mis à jour — basé sur le pull, pas le push (Claude Code ne peut pas pousser en cross-repo).

## Flux de travail courants

**Vérification quotidienne** : Inventaire K_GITHUB → K_GITHUB `sync_github.py` + K_VALIDATION `/integrity-check`

**Nouvelle découverte** : `sync_github.py <projet>` → révision manuelle → identifier le type cible → mettre à jour `conventions.json` ou `work.json`

**Balayage réseau** : K_GITHUB `sync_github.py` + K_VALIDATION `/integrity-check` pour un balayage complet avec icônes de sévérité.

---

[**Lire la documentation complète →**]({{ '/fr/publications/harvest-protocol/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
