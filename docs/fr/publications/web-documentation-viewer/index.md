---
layout: publication
title: "Visualiseur Web K_DOCS — Moteur de documentation mono-fichier"
description: "Un seul index.html qui rend les publications markdown avec 4 thèmes, export PDF/DOCX, navigation à trois panneaux, mindmap vivant et support bilingue — zéro étape de compilation, zéro dépendance serveur."
permalink: /fr/publications/web-documentation-viewer/
lang: fr
permalink_en: /publications/web-documentation-viewer/
header_title: "Visualiseur Web K_DOCS"
tagline: "Moteur de documentation mono-fichier"
pub_id: "Publication #23"
pub_meta: "Publication #23 v1 | Mars 2026"
pub_version: "v1"
pub_number: 23
pub_date: "Mars 2026"
og_image: /assets/og/knowledge-2-fr-cayman.gif
keywords: "visualiseur documentation, mono-fichier, statique, thèmes, export, panneaux, mindmap, bilingue"
---

## Résumé

Le visualiseur Web K_DOCS résout un problème fondamental : comment servir une documentation riche et interactive depuis un seul fichier statique, sans étape de compilation et sans traitement côté serveur. Le système Knowledge de production (`packetqc/knowledge`) repose sur Jekyll + GitHub Pages avec deux mises en page HTML massives (183 Ko au total). Ce pipeline fonctionne mais nécessite Ruby, une étape de compilation et des conventions spécifiques à Jekyll qui créent des pièges fragiles (suppression Liquid, problèmes d'analyse kramdown, sorties de mode bloc `<details>`).

Le visualiseur remplace tout cela par un seul `index.html` qui récupère le markdown à l'exécution, analyse le front matter YAML, résout les tags Liquid côté client, rend les diagrammes Mermaid et sert un mindmap interactif MindElixir vivant. Quatre thèmes CSS (Cayman, Midnight, Daltonisme Clair/Sombre) persistent via localStorage. L'export corporatif PDF et DOCX utilise CSS Paged Media et les éléments MSO respectivement — zéro dépendance externe. Une disposition à trois panneaux avec diviseurs déplaçables héberge 25+ publications et 5 interfaces. Toute la plateforme documentaire se déploie avec `git push`.

```mermaid
mindmap
  root((Visualiseur Web))
    Pipeline de rendu
      Récupération et analyse markdown
      Front matter YAML
      Résolveur Liquid
      Diagrammes Mermaid
    Système 4 thèmes
      Cayman et Midnight
      Daltonisme Clair et Sombre
      Persistance localStorage
    Disposition 3 panneaux
      Diviseurs déplaçables
      Routage interfaces
      Convention barre chrome
    Moteur export
      PDF via CSS Paged Media
      DOCX via éléments MSO
      Style corporatif
    Mindmap vivant
      MindElixir v5
      Filtrage profondeur
      Sync thèmes
    Bilingue EN FR
```

### Fonctionnalités clés

| Fonctionnalité | Description |
|----------------|-------------|
| **Pipeline markdown** | Récupérer `.md` → analyser front matter → résoudre Liquid → marked.js → Mermaid → DOM |
| **Système 4 thèmes** | Daltonisme Clair/Sombre, Cayman, Midnight — variables CSS + localStorage |
| **Disposition 3 panneaux** | Navigateur gauche, contenu centre, interfaces droite — diviseurs déplaçables |
| **Export PDF/DOCX** | Style corporatif, page de couverture, TDM page 2, en-tête/pied récurrents |
| **Mindmap vivant** | MindElixir v5.9.3 avec filtrage de profondeur et sync de thème |
| **Bilingue EN/FR** | Bascule de langue, permaliens doubles, étiquettes dynamiques |
| **Routage d'interfaces** | Navigation inter-panneaux sans rechargements complets |
| **Barre chrome** | Barre de métadonnées repliable unifiée pour tous les panneaux |

---

## Lire la suite

- **[Documentation complète](full/)** — Publication complète avec architecture, détails du pipeline et conventions
- **[Story #26]({{ '/fr/publications/success-stories/story-26/' | relative_url }})** — L'histoire derrière la construction de ce visualiseur

---

*Martin Paquet & Claude (Opus 4.6) | [packetqc/K_DOCS](https://github.com/packetqc/K_DOCS)*
