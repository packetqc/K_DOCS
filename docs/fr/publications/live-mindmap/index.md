---
title: "Mindmap vivant — Graphe de connaissances interactif"
description: "Transforme le mindmap mermaid K_MIND en un graphe de connaissances MindElixir interactif avec filtrage par profondeur, synchronisation de thème et trois points de déploiement — aucune étape de build."
permalink: /fr/publications/live-mindmap/
lang: fr
permalink_en: /publications/live-mindmap/
header_title: "Mindmap vivant"
tagline: "Graphe de connaissances interactif"
pub_id: "Publication #24"
pub_meta: "Publication #24 v1 | Mars 2026"
pub_version: "v1"
pub_number: 24
pub_date: "Mars 2026"
og_image: /assets/og/live-mindmap-en-daltonism-light.gif
live_webcard: mindmap
keywords: "mindmap, MindElixir, graphe de connaissances, interactif, filtrage profondeur, synchronisation thème"
---

## Résumé

Le système mémoire K_MIND stocke son graphe de connaissances sous forme de mindmap mermaid dans `mind_memory.md`. Mermaid le rend en SVG statique — pas d'expansion/réduction, pas de zoom, pas de contrôle de profondeur. Le Mindmap vivant le transforme en graphe de connaissances MindElixir interactif à l'exécution.

Un convertisseur JavaScript parse la syntaxe mermaid et construit un arbre compatible MindElixir. Le système de filtrage par profondeur — un portage de `mindmap_filter.py` — applique les règles de `depth_config.json` dans le navigateur, assurant la cohérence entre les vues CLI et web. Trois points de déploiement servent différents contextes : interface I5 plein écran avec barre d'outils, webcard vivant K2.0, et webcard du visualiseur pour toute page avec `live_webcard: mindmap`.

La synchronisation de thème fait correspondre les quatre thèmes CSS du visualiseur aux palettes MindElixir — les mises à jour se propagent instantanément via `changeTheme()`, sans ré-initialisation. Le système récupère directement depuis l'API brute de GitHub, reflétant toujours le dernier état commité.

```mermaid
mindmap
  root((Mindmap vivant))
    Mermaid vers MindElixir
      Parseur et convertisseur
      Transformation en temps réel
      Détection de forme des nœuds
    Filtrage par profondeur
      depth_config.json
      Mode Normal vs Complet
      Surcharges par branche
      Liste omission
    Trois déploiements
      Interface I5 complète
      Webcard vivant K2.0
      Système de webcard du visualiseur
    Synchro thème
      4 palettes de thèmes
      Mise à jour live changeTheme
      BroadcastChannel
      prefers-color-scheme
    Contrôles
      Centrer et Ajuster
      Plein écran
      Ctrl+Clic tout développer
      Aide bilingue EN FR
```

### Fonctionnalités clés

| Fonctionnalité | Description |
|---------|-------------|
| **Convertisseur Mermaid** | Parse la syntaxe mindmap mermaid → arbre MindElixir à l'exécution |
| **Filtrage par profondeur** | Portage JS de `mindmap_filter.py` avec `depth_config.json` |
| **3 points de déploiement** | Interface I5, webcard K2.0, système de webcard du visualiseur |
| **Synchro 4 thèmes** | Daltonism Clair/Foncé, Cayman, Midnight — `changeTheme()` instantané |
| **Contrôles interactifs** | Expansion/réduction, zoom/panoramique, Ctrl+Clic tout développer |
| **Bilingue** | Libellés EN/FR dans la barre d'outils, panneau d'aide, messages d'état |

---

## En savoir plus

- **[Documentation complète]({{ '/fr/publications/live-mindmap/full/' | relative_url }})** — Publication complète avec détails du convertisseur, filtrage par profondeur et architecture des thèmes
- **[Success Story #25]({{ '/fr/publications/success-stories/story-25/' | relative_url }})** — L'histoire derrière cette réalisation

---

*Martin Paquet & Claude (Opus 4.6) | [packetqc/K_DOCS](https://github.com/packetqc/K_DOCS)*
