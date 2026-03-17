---
layout: publication
title: "Interface Principale"
description: "L'interface web principale pour naviguer et interagir avec le systeme de connaissances : points d'entree principaux, architecture de navigation, hierarchie des pages et patrons d'interaction utilisateur."
pub_id: "Publication #21"
version: "v1"
date: "2026-02-27"
permalink: /fr/publications/main-interface/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "interface, navigation, web, connaissances, tableau de bord"
dev_banner: "Interface en developpement — les fonctionnalites et la mise en page peuvent changer entre les sessions."
---

# Interface Principale
{: #pub-title}

> **Publication parente** : [#0 — Systeme de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }})

**Table des matieres**

| | |
|---|---|
| [Resume](#resume) | Interface principale du systeme de connaissances |
| [Architecture de navigation](#architecture-de-navigation) | Hierarchie des pages et points d'entree |
| [Lancer l'interface](#lancer-linterface) | Ouvrir le Navigateur principal (I2) |

## Audience ciblee

| Audience | Quoi privilegier |
|----------|-----------------|
| **Utilisateurs finaux** | Navigation, decouverte des pages, patrons d'interaction |
| **Developpeurs web** | Hierarchie des pages, integration des mises en page, architecture des hubs |
| **Assistants IA** | Conventions d'interface, points d'entree des commandes |

## Resume

L'interface web principale pour naviguer et interagir avec le systeme de connaissances. Documente les points d'entree principaux, l'architecture de navigation, la hierarchie des pages et les patrons d'interaction utilisateur qui forment la presence web du systeme sur GitHub Pages.

**[Lancer le Navigateur principal (Interface I2) →]({{ '/fr/interfaces/main-navigator/' | relative_url }})**

## Architecture de navigation

La presence web de Knowledge est organisee en hierarchie de pages hub avec miroirs bilingues :

```
Page d'accueil (/)
    ├── Hub Profil (/profile/)
    │   ├── Resume (/profile/resume/)
    │   └── Complet (/profile/full/)
    ├── Index Publications (/publications/)
    │   └── Publication #N (/publications/<slug>/)
    │       └── Complet (/publications/<slug>/full/)
    └── Hub Projets (/projects/)
```

Chaque page existe en EN et FR avec une barre de navigation de langue.

## Lancer l'interface

**[Ouvrir le Navigateur principal (Interface I2) →]({{ '/fr/interfaces/main-navigator/' | relative_url }})** — Navigation a trois panneaux avec visualiseur de contenu integre.

**[Ouvrir la Revision de sessions (Interface I1) →]({{ '/fr/interfaces/session-review/' | relative_url }})** — Visualiseur interactif de sessions avec metriques et graphiques.

**[Ouvrir le Flux de travail des taches (Interface I3) →]({{ '/fr/interfaces/task-workflow/' | relative_url }})** — Visualiseur du flux de travail avec 8 etapes et suivi de validation.

[Toutes les interfaces →]({{ '/fr/interfaces/' | relative_url }})

---

## Publications liees

| # | Publication | Relation |
|---|-------------|---------|
| 0 | [Systeme de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — le systeme que cette interface dessert |
| 17 | [Pipeline de production web]({{ '/fr/publications/web-production-pipeline/' | relative_url }}) | Pipeline — comment les pages sont construites |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
