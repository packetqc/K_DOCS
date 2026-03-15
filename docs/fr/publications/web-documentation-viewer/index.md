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

## Aperçu

Le visualiseur Web K_DOCS est un **fichier HTML unique** (`docs/index.html`) qui sert de plateforme documentaire complète. Il rend les fichiers markdown avec front matter YAML, applique un des quatre thèmes CSS, exporte en PDF et DOCX avec style corporatif, navigue entre trois panneaux déplaçables et affiche un mindmap interactif vivant — le tout sans étape de compilation et sans traitement côté serveur.

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
