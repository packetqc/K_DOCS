---
layout: publication
title: "Pipeline de production web"
description: "Pipeline complet de production des pages web Knowledge : structure à trois niveaux, miroirs bilingues, traitement Jekyll, système de mise en page, architecture de thèmes, pipeline d'assets, mécanismes d'exclusion et déploiement GitHub Pages."
pub_id: "Publication #17"
version: "v1"
date: "2026-02-26"
permalink: /fr/publications/web-production-pipeline/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "pipeline, jekyll, kramdown, production, web, deploiement"
---

# Pipeline de production web
{: #pub-title}

> **Publication parente** : [#0 — Système de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Companion export** : [#13 — Pagination web & export]({{ '/fr/publications/web-pagination-export/' | relative_url }}) | **Post-pipeline** : [#16 — Visualisation de pages web]({{ '/fr/publications/web-page-visualization/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Résumé](#resume) | Du markdown source à la page web en ligne |
| [Vue d'ensemble](#vue-densemble-du-pipeline) | Flux de bout en bout en 10 étapes |
| [Structure à trois niveaux](#structure-de-publication-a-trois-niveaux) | Source → Résumé → Complet |
| [Traitement Jekyll](#traitement-jekyll) | Liquid → kramdown → HTML |
| [Mécanismes d'exclusion](#mecanismes-dexclusion) | Ce qui est filtré, masqué ou transformé |
| [Documentation complète](#documentation-complete) | Référence complète du pipeline |

## Audience cibleé

| Audience | Quoi privilégier |
|----------|-----------------|
| **Auteurs de publications** | Rédaction source, contrat front matter, structure 3 niveaux |
| **Développeurs web** | Traitement Jekyll, système de mise en page, architecture de thèmes |
| **Administrateurs système** | Déploiement GitHub Pages, pipeline d'assets, comportement CDN |
| **Assistants IA** | Mécanismes d'exclusion, particularités kramdown, commandes pipeline |

## Résumé

Chaque page web du système Knowledge suit un pipeline de production déterministe : le markdown source est rédigé une seule fois, structuré en un système à trois niveaux (source → résumé → complet), traité par le moteur kramdown de Jekyll avec les templates Liquid, enveloppé dans des mises en page adaptatives aux thèmes, et déployé automatiquement sur GitHub Pages.

Cette publication documente le pipeline complet — de la première ligne de markdown à une page web en ligne, bilingue, à double thème et exportable. Elle couvre les fichiers structurants, les étapes de traitement et surtout les **mécanismes d'exclusion** — ce qui ne se retrouve pas dans la page web finale et pourquoi.

La [documentation complète]({{ '/fr/publications/web-production-pipeline/full/' | relative_url }}) couvre les 12 sections avec les spécifications détaillées.

## Vue d'ensemble du pipeline

```
Markdown source (l'auteur écrit une seule fois)
    ↓ pub new (création du squelette)
Division à trois niveaux (source → résumé → complet)
    ↓ injection du front matter
Miroirs bilingues (EN + FR pour chaque niveau web)
    ↓ traitement Jekyll
Templates Liquid → kramdown → HTML
    ↓ enveloppement par la mise en page
publication.html ou default.html
    ↓ améliorations côté client
Mermaid, thèmes, références croisées, export
    ↓ déploiement GitHub Pages
Page web en ligne (double thème, bilingue, exportable)
```

**Principe clé** : Le document source est écrit une seule fois. Tout ce qui suit est dérivé. Le pipeline est déterministe — la même source produit toujours le même résultat.

## Structure de publication à trois niveaux

Chaque publication existe à trois niveaux :

| Niveau | Emplacement | Objectif |
|--------|-------------|----------|
| **Source** | `publications/<slug>/v1/README.md` | Document canonique, anglais uniquement |
| **Résumé** | `docs/publications/<slug>/index.md` | Point d'entrée web, aperçu rapide |
| **Complet** | `docs/publications/<slug>/full/index.md` | Documentation web complète |

**5 fichiers par publication** : 1 source + 2 pages web EN + 2 pages web FR.

Les pages résumé renvoient vers leur page complète. Les pages complètes renvoient vers leur résumé. EN renvoie vers FR et vice versa. Tous les liens internes utilisent le filtre `relative_url`.

## Traitement Jekyll

Trois passes ordonnées transforment le markdown en HTML :

| Passe | Moteur | Ce qu'il fait |
|-------|--------|--------------|
| 1 | **Liquid** | Traitement des templates — variables {% raw %}`{{ }}`{% endraw %}, logique {% raw %}`{% %}`{% endraw %}, filtres URL |
| 2 | **kramdown** | Markdown → HTML — dialecte GFM avec `parse_block_html: true` |
| 3 | **Mise en page** | Enveloppement — injecte CSS, JS, OG tags, bannière de version |

{% raw %}**Critique** : Liquid s'exécute en premier. Tout `{{ }}` dans le contenu markdown (y compris les hexagones Mermaid) est interprété par Liquid avant que kramdown ne le voie.{% endraw %}

## Mécanismes d'exclusion

Tout ce qui est dans la source n'apparaît pas sur la page web en ligne :

| Couche | Ce qui est exclu | Pourquoi |
|--------|-----------------|----------|
| **CSS** | Blocs `.mermaid-source` | Préservation source — visible dans git, masqué sur le web |
| **CSS** (`@media print`) | Barre d'outils, barre de langue, webcard, navigation | Sortie PDF propre |
| **JavaScript** | Blocs Mermaid dans `.mermaid-source` | Empêche le double-rendu |
| **kramdown** | Contenu {% raw %}`{{ }}`{% endraw %} dans les blocs de code | Liquid traite avant kramdown |
| **kramdown** | `</tags>` dans `<details>` avec lignes vides | L'analyse HTML quitte sur ligne vide |

Les exclusions sont architecturales — elles reflètent les contraintes de la chaîne de traitement Jekyll, pas des bogues.

## Documentation complète

La [documentation complète]({{ '/fr/publications/web-production-pipeline/full/' | relative_url }}) inclut les 12 sections :

| # | Section | Ce qu'elle couvre |
|---|---------|------------------|
| 1 | Rédaction source | Écriture du document markdown canonique |
| 2 | Structure à trois niveaux | Division source → résumé → complet |
| 3 | Miroirs bilingues | Architecture parallèle EN/FR |
| 4 | Contrat front matter | Métadonnées YAML requises |
| 5 | Traitement Jekyll | Transformation Liquid → kramdown → HTML |
| 6 | Système de mise en page | publication.html vs default.html |
| 7 | Système de thèmes | CSS 4 thèmes avec détection automatique |
| 8 | Pipeline d'assets | Webcards, diagrammes, images, médias |
| 9 | Mécanismes d'exclusion | Ce qui est filtré, masqué ou transformé |
| 10 | Déploiement | Construction automatique GitHub Pages |
| 11 | Commandes pipeline | pub, docs, webcard, normalize |
| 12 | Pièges connus | Particularités kramdown, limites proxy, pièges de rendu |

**Source** : [Issue #347](https://github.com/packetqc/knowledge/issues/347) — Session de génération de documentation.

---

## Publications liées

| # | Publication | Relation |
|---|-------------|---------|
| 0 | [Système de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — le système que ce pipeline dessert |
| 5 | [Webcards & partage social]({{ '/fr/publications/webcards-social-sharing/' | relative_url }}) | Pipeline d'assets — aperçus OG sociaux |
| 6 | [Normalize & concordance]({{ '/fr/publications/normalize-structure-concordance/' | relative_url }}) | Porte de qualité — validation de concordance |
| 13 | [Pagination web & export]({{ '/fr/publications/web-pagination-export/' | relative_url }}) | Export — PDF/DOCX depuis la sortie pipeline |
| 14 | [Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | Contexte — pipeline comme composant |
| 16 | [Visualisation de pages web]({{ '/fr/publications/web-page-visualization/' | relative_url }}) | Post-pipeline — rendu et diagnostics |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
