---
layout: publication
title: "Interface Principale"
description: "L'interface web principale pour naviguer et interagir avec le systeme Knowledge 2.0 : navigateur trois panneaux, 5 interfaces, barre d'onglets multi-documents, sections JSON et guide utilisateur integre."
pub_id: "Publication #21"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/main-interface/
og_image: /assets/og/main-navigator-fr-cayman.gif
keywords: "interface, navigation, web, connaissances, tableau de bord, navigateur, onglets"
dev_banner: "Interface en developpement — les fonctionnalites et la mise en page peuvent changer entre les sessions."
---

# Interface Principale
{: #pub-title}

> **Publication parente** : [#0 — Systeme de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }})

**Table des matieres**

| | |
|---|---|
| [Resume](#resume) | Hub de 5 interfaces avec navigateur trois panneaux |
| [Les 5 interfaces](#les-5-interfaces) | Revue de session, Navigateur principal, Flux de travail, Visualiseur projets, Mindmap vivant |
| [Navigateur principal](#navigateur-principal) | Disposition trois panneaux, sections JSON, barre d'onglets |
| [Fonctionnalites cles](#fonctionnalites-cles) | Barre d'onglets, guide utilisateur, panneau dynamique |
| [Lancer l'interface](#lancer-linterface) | Ouvrir les interfaces |

## Audience ciblee

| Audience | Quoi privilegier |
|----------|-----------------|
| **Utilisateurs finaux** | Navigation, decouverte des interfaces, onglets multi-documents |
| **Developpeurs web** | Architecture trois panneaux, sections JSON, style widget-card |
| **Assistants IA** | Conventions d'interface, points d'entree, interfaces.json |

## Resume

L'interface principale de Knowledge 2.0 centralise 5 interfaces dans un navigateur a trois panneaux. Le panneau gauche expose 10 sections pilotees par JSON avec un style widget-card (MAJUSCULES, arriere-plans cartes, hover translateX(3px)). Le panneau centre affiche les interfaces en iframe avec un contenu par defaut dynamique depuis `interfaces.json`. Le panneau droit est un visualiseur de documents avec barre d'onglets pour la navigation multi-documents (persistance localStorage). Chaque interface dispose d'un bouton ℹ ouvrant le guide utilisateur.

**[Lancer le Navigateur principal (Interface I2) →]({{ '/fr/interfaces/main-navigator/' | relative_url }})**

## Les 5 interfaces

| # | Interface | Position | Role |
|---|-----------|----------|------|
| I1 | **Revue de session** | Centre | Visualiseur interactif de sessions avec metriques et graphiques |
| I2 | **Navigateur principal** | Haut | Hub trois panneaux : sections, interfaces iframe, visualiseur documents |
| I3 | **Flux de travail** | Centre | Flux de travail des taches avec 8 etapes et suivi de validation |
| I4 | **Visualiseur projets** | Centre | Vue et suivi des projets Knowledge |
| I5 | **Mindmap vivant** | Centre | Carte mentale interactive du systeme de connaissances |

## Navigateur principal

Le Navigateur principal (I2) est le point d'entree du systeme. Il adopte une disposition a trois panneaux :

```
┌─────────────────────────────────────────────────────────┐
│                    Navigateur principal                   │
├──────────────┬──────────────────┬────────────────────────┤
│  Panneau     │  Panneau centre  │  Panneau droit         │
│  gauche      │                  │                        │
│              │  Interfaces      │  Visualiseur           │
│  10 sections │  iframe          │  documents             │
│  JSON        │  (I1–I5)        │                        │
│              │                  │  Barre d'onglets       │
│  Widget-card │  Defaut depuis   │  (localStorage)        │
│  MAJUSCULES  │  interfaces.json │                        │
├──────────────┴──────────────────┴────────────────────────┤
│                   Bouton ℹ Guide utilisateur              │
└─────────────────────────────────────────────────────────┘
```

### Panneau gauche — 10 sections JSON

Le panneau gauche contient 10 sections pilotees par des fichiers JSON. Chaque section utilise le style **widget-card** : titres en MAJUSCULES, arriere-plans cartes, effet hover `translateX(3px)`. La section Documentation utilise des liens plats (comme les essentiels).

### Panneau centre — Interfaces iframe

Le panneau centre charge les interfaces (I1–I5) dans des iframes. Le contenu par defaut est determine dynamiquement depuis `interfaces.json`.

### Panneau droit — Visualiseur documents

Le panneau droit affiche les documents avec une **barre d'onglets** permettant la navigation multi-documents. Les onglets ouverts persistent via localStorage.

## Fonctionnalites cles

- **Barre d'onglets** : navigation multi-documents dans le panneau droit, persistance localStorage
- **Bouton ℹ** : chaque interface dispose d'un bouton ouvrant le guide utilisateur
- **10 sections JSON** : contenu du panneau gauche pilote par des fichiers JSON
- **Style widget-card** : MAJUSCULES, arriere-plans cartes, hover translateX(3px)
- **Panneau centre dynamique** : contenu par defaut depuis interfaces.json

## Lancer l'interface

**[Ouvrir le Navigateur principal (Interface I2) →]({{ '/fr/interfaces/main-navigator/' | relative_url }})** — Navigation a trois panneaux avec visualiseur de contenu integre.

**[Ouvrir la Revue de session (Interface I1) →]({{ '/fr/interfaces/session-review/' | relative_url }})** — Visualiseur interactif de sessions avec metriques et graphiques.

**[Ouvrir le Flux de travail (Interface I3) →]({{ '/fr/interfaces/task-workflow/' | relative_url }})** — Flux de travail des taches avec 8 etapes et suivi de validation.

**[Ouvrir le Visualiseur projets (Interface I4) →]({{ '/fr/interfaces/project-viewer/' | relative_url }})** — Vue et suivi des projets Knowledge.

[Toutes les interfaces →]({{ '/fr/interfaces/' | relative_url }})

---

## Publications liees

| # | Publication | Relation |
|---|-------------|---------|
| 0 | [Systeme de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — le systeme que cette interface dessert |
| 17 | [Pipeline de production web]({{ '/fr/publications/web-production-pipeline/' | relative_url }}) | Pipeline — comment les pages sont construites |
| 24 | [Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }}) | Architecture — le systeme modulaire K2.0 |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
