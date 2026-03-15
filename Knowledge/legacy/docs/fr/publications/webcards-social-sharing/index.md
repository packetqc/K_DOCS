---
layout: publication
title: "Webcards & Partage social — Aperçus OG animés pour publications d'ingénierie IA"
description: "Chaque page de Knowledge possède un aperçu social OG animé unique — un GIF 1200x630 servant à la fois d'en-tête visuel sur GitHub Pages et de carte sociale sur LinkedIn, Twitter et Facebook. Cette publication documente ce que sont les webcards, comment les partager, et le comportement spécifique de chaque plateforme."
pub_id: "Publication #5"
version: "v2"
date: "2026-02-21"
permalink: /fr/publications/webcards-social-sharing/
og_image: /assets/og/webcards-social-sharing-fr-cayman.gif
keywords: "webcards, image OG, GIF animé, partage social, dynamique, artefacts de connaissances"
---

# Webcards & Partage social — Aperçus OG animés
{: #pub-title}

> **Publication parente** : [#0 — Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) — le système auquel ces webcards appartiennent

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Vue d'ensemble du système de webcards et origine |
| [Qu'est-ce qu'un webcard](#quest-ce-quun-webcard) | Spécifications des aperçus sociaux OG animés et types de cartes |
| [Webcards dynamiques — artefacts de connaissances vivants](#webcards-dynamiques--artefacts-de-connaissances-vivants) | Cartes pilotées par les données reflétant l'état en direct |
| [Deux modes de partage](#deux-modes-de-partage) | Partage par URL de page vs URL d'image |
| [Comportement des plateformes](#comportement-des-plateformes) | Gestion par LinkedIn, Twitter, Facebook, Slack |
| [Recettes pratiques](#recettes-pratiques) | Guides de partage étape par étape pour mobile et bureau |
| [Dépannage](#dépannage) | Mauvais liens, images manquantes, aperçus périmés |
| [Architecture technique](#architecture-technique) | Intégration HTML, front matter, script générateur |

## Résumé

Chaque page web de Knowledge possède un **aperçu social OG animé unique** — un GIF 1200x630 qui sert à la fois d'en-tête visuel sur GitHub Pages et de carte pour les réseaux sociaux lors du partage sur LinkedIn, Twitter ou Facebook. Ce sont les **webcards**.

Né d'un problème réel : le partage d'une publication sur LinkedIn depuis un mobile pointait vers le fichier markdown GitHub au lieu de la publication GitHub Pages. Cela a conduit à l'ajout de balises `<link rel="canonical">` et à la documentation du flux de partage correct.

## Qu'est-ce qu'un webcard

Un webcard est un **GIF animé** (1200x630 pixels, 256 couleurs optimisées, tramage Floyd-Steinberg) représentant une page web. Chaque page obtient une animation unique adaptée à son contenu — pas de modèles génériques. Double thème : **Cayman** (clair, sarcelle/émeraude) + **Midnight** (sombre, marine/indigo) — détection automatique par le navigateur via `prefers-color-scheme`. Ensemble total : 40 GIFs (10 pages x 2 thèmes x 2 langues), ~7 Mo au total.

| Type de carte | Pages | Animation |
|---------------|-------|-----------|
| `corporate` | Hub profil, CV, profil complet | Photo avec anneau de bordure pulsant et changeant de couleur |
| `diagram` | Pipeline MPLIB, Session en direct | Les nœuds du pipeline s'activent séquentiellement |
| `split-panel` | Connaissances distribuées, Tableau de bord | Le panneau gauche défile + le panneau droit coule |
| `cartoon` | Persistance IA | Transformation Vicky NPC vers AWARE |
| `index` | Index des publications | Les cartes apparaissent une par une, puis brillent |

## Webcards dynamiques — artefacts de connaissances vivants

Les webcards ne sont pas de simples images décoratives — ce sont des **artefacts de connaissances** qui lisent les données en direct du système et les restituent visuellement. Le contenu d'un webcard dynamique change entre les générations car les données sous-jacentes changent.

**Le flux de données** : Données de connaissances (documents sources, tables satellites, état du système) → fonction d'analyse → script générateur → GIF animé → en-tête GitHub Pages + aperçu social OG.

| Aspect | Cartes statiques | Cartes dynamiques |
|--------|-----------------|-------------------|
| **Source de contenu** | Codé en dur dans le générateur | Analysé depuis les documents de connaissances |
| **Résultat entre les générations** | Identique | Différent (reflète les nouvelles données) |
| **Intégration aux connaissances** | Conception unique | Continue — lit l'état en direct |
| **Exemple** | Profil, pipeline, persistance | Tableau de bord (#4a) |

**#4a en action** : Le webcard du tableau de bord lit la table réelle de l'inventaire satellite — noms, versions, dérive, santé — et restitue l'état actuel du réseau dans le GIF. Ce que vous voyez dans l'image EST les vraies données. Regénéré automatiquement après chaque `harvest --healthcheck`.

**Le webcard EST le rapport d'état** : Une carte #4a montrant tout en vert signifie que le réseau est en santé. Du rouge et orange signifie que des satellites nécessitent attention. Trois préoccupations convergent dans les webcards : **visibilité** (identité visuelle unique par page), **actualité** (les cartes dynamiques reflètent l'état en direct), et **découvrabilité** (les balises OG assurent des aperçus sociaux riches).

Les plateformes sociales affichent la **première image** comme aperçu statique. L'animation complète joue sur GitHub Pages.

| Contexte | Animation |
|----------|-----------|
| GitHub Pages (en-tête de page) | Animation complète |
| LinkedIn / Twitter / Facebook | Première image seulement |
| Slack / Discord | Parfois (au survol) |

## Deux modes de partage

**Mode 1 — Partager l'URL de la page** (recommandé) : Partagez `packetqc.github.io/knowledge/publications/...`. Les plateformes lisent les balises méta OG et affichent titre + description + première image du webcard. Le clic mène à la publication.

**Mode 2 — Partager l'URL de l'image directement** : Partagez l'URL `.gif`. Certaines plateformes peuvent jouer l'animation, mais sans titre, sans description, le clic mène au fichier image. À utiliser uniquement pour montrer l'animation.

## Comportement des plateformes

| Plateforme | Comportement |
|------------|-------------|
| **LinkedIn** | Première image statique. Cache agressif — utilisez le [Post Inspector](https://www.linkedin.com/post-inspector/) pour rafraîchir. Suit `<link rel="canonical">` pour l'URL de clic. |
| **Twitter** | Première image statique. Carte `summary_large_image`. Cache ~7 jours. |
| **Facebook** | Peut jouer l'animation GIF en ligne. Utilisez le [Sharing Debugger](https://developers.facebook.com/tools/debug/) pour rafraîchir. |
| **Slack/Discord** | Aperçu riche avec première image. L'image directe peut jouer au survol. |

## Recettes pratiques

**Partager sur LinkedIn (Mobile)** : Naviguez vers `packetqc.github.io/knowledge/publications/...` (PAS `github.com`), appuyez sur Partager, choisissez LinkedIn.

**Partager sur LinkedIn (Bureau)** : Copiez l'URL GitHub Pages, collez dans un post LinkedIn, attendez la carte d'aperçu, vérifiez qu'elle affiche le titre + le webcard.

**Forcer le rafraîchissement LinkedIn** : Allez au [Post Inspector](https://www.linkedin.com/post-inspector/), collez l'URL, cliquez Inspecter, vérifiez les données.

## Dépannage

| Symptôme | Correction |
|----------|------------|
| **Mauvais lien dans LinkedIn** | Vous avez partagé depuis `github.com` au lieu de `packetqc.github.io`. Vérifiez la barre d'adresse. |
| **Pas d'image de prévisualisation** | Vérifiez `og_image` dans le front matter, vérifiez que le GIF existe dans `docs/assets/og/`. |
| **L'animation ne joue pas** | Normal — les réseaux sociaux affichent uniquement la première image. |
| **Aperçu périmé** | Utilisez les outils de débogage de cache spécifiques à chaque plateforme. |

## Architecture technique

Les deux layouts (`default.html` et `publication.html`) incluent les balises méta `og:image`, `twitter:image` et `<link rel="canonical">`. Chaque page nécessite `og_image` dans le front matter YAML pointant vers son GIF. Script générateur : `scripts/generate_og_gifs.py`.

---

[**Lire la documentation complète →**]({{ '/fr/publications/webcards-social-sharing/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
