---
layout: publication
title: "Navigateur principal — Guide utilisateur (Complet)"
description: "Guide utilisateur complet pour le Navigateur principal : gestion des panneaux, widgets, visualiseur, onglets, changement de langue et fonctionnalités avancées."
pub_id: "Guide utilisateur — I2 (Complet)"
version: "v1"
date: "2026-03-16"
lang: fr
permalink: /fr/publications/guide-main-navigator/full/
keywords: "guide utilisateur, navigateur principal, interface, tutoriel, complet"
---

# Navigateur principal — Guide utilisateur
{: #pub-title}

> **Interface** : [Navigateur principal (I2)]({{ '/fr/interfaces/main-navigator/' | relative_url }}) | [Version résumé]({{ '/fr/publications/guide-main-navigator/' | relative_url }})

## Table des matières

| | |
|---|---|
| [Démarrage](#démarrage) | Ouvrir et s'orienter |
| [Disposition trois panneaux](#disposition-trois-panneaux) | Gauche, centre, droite |
| [Redimensionnement](#redimensionnement) | Glisser et clic alterné |
| [Widgets du panneau gauche](#widgets-du-panneau-gauche) | Toutes les sections |
| [Panneau central](#panneau-central) | Interfaces et outils |
| [Panneau droit et onglets](#panneau-droit-et-onglets) | Visualiseur avec barre d'onglets |
| [Changement de langue](#changement-de-langue) | Bascule EN/FR |
| [Thèmes](#thèmes) | Thèmes clair et sombre |
| [Persistance d'état](#persistance-détat) | Ce qui survit au rechargement |
| [Dépannage](#dépannage) | Problèmes courants |

## Démarrage

Le Navigateur principal (I2) est le hub central de la plateforme Knowledge. Il consolide tout le contenu — interfaces, publications, guides, méthodologies, configurations et données de projets — dans un navigateur à trois panneaux.

**Ouvrir le navigateur :** URL directe `/fr/interfaces/main-navigator/`. Il s'ouvre en pleine page.

## Disposition trois panneaux

Le navigateur utilise une grille CSS à 5 colonnes : panneau gauche, diviseur gauche, panneau central, diviseur droit, panneau droit.

| Panneau | Taille par défaut | Contenu |
|---------|-------------------|---------|
| **Gauche** | 220px | Répertoire de widgets |
| **Centre** | Remplit le reste | Interfaces (iframes) |
| **Droite** | 0px (caché) | Visualiseur de documents (iframe) |

## Redimensionnement

**Glisser** : saisissez un diviseur et glissez horizontalement.

**Clic alterné** (clic sans glisser) :
- **Diviseur gauche** : alterne 0px → 220px → 320px
- **Diviseur droit** : alterne 0px → 50% → pleine largeur → 0px

Le panneau droit s'étend automatiquement quand vous cliquez un lien de document.

## Widgets du panneau gauche

Les widgets sont des éléments repliables, chacun chargeant ses données depuis un fichier JSON.

| Widget | Contenu | S'ouvre dans |
|--------|---------|-------------|
| **Interfaces** | I1–I5 + lien documentation | Panneau central |
| **Documentation** | Guides utilisateur, admin, démarrages rapides | Panneau droit |
| **Essentiels** | Documents de référence clés | Panneau droit |
| **Commandes** | Référence groupée des commandes | Panneau droit |
| **Méthodologies** | Fichiers de méthodologie (par module) | Panneau droit |
| **Publications** | 27 publications techniques (résumé + complet) | Panneau droit |
| **Configurations** | Fichiers JSON de configuration (par module) | Panneau droit |

Les états ouvert/fermé sont sauvegardés dans localStorage.

## Panneau central

Le panneau central héberge les interfaces interactives via iframe :
- **Par défaut** : Flux de travail (I3) se charge au démarrage
- Cliquez sur une interface pour basculer
- La dernière interface vue est restaurée au rechargement

## Panneau droit et onglets

Le panneau droit est un visualiseur avec une **barre d'onglets** :

- Chaque document ouvert crée un onglet
- Cliquez les onglets pour basculer entre documents
- Cliquez × pour fermer un onglet
- Les onglets persistent entre rechargements (localStorage)
- Maximum 12 onglets — le plus ancien non-actif se ferme automatiquement

Le visualiseur affiche :
- **Markdown** avec titres, tableaux, diagrammes mermaid et table des matières
- **JSON** en tableaux formatés avec titres intelligents et liens cliquables
- **Publications** avec barre chrome (métadonnées, version, auteurs)

## Changement de langue

Le navigateur supporte EN/FR :
- La langue est détectée depuis le chemin URL (préfixe `/fr/`)
- Les libellés des widgets changent selon les champs `title_fr` dans les JSON
- Les liens de documents sont réécrits pour correspondre à la langue active

## Thèmes

Le navigateur hérite du thème du site (clair/sombre). Les thèmes se propagent aux deux iframes automatiquement.

## Persistance d'état

L'état suivant survit au rechargement (stocké dans localStorage) :

| État | Clé |
|------|-----|
| Largeur panneau gauche | `navigator-left-state` |
| Largeur panneau droit | `navigator-right-state` |
| URL iframe central | `navigator-center-url` |
| URL iframe droit | `navigator-right-url` |
| Lien actif | `navigator-active-href` |
| Widgets ouvert/fermé | `navigator-widgets` |
| Barre d'onglets | `navigator-tabs` |

## Dépannage

| Problème | Solution |
|----------|----------|
| Widgets sans contenu | Vérifiez le réseau — les fichiers JSON peuvent échouer à charger |
| Panneau droit ne s'ouvre pas | Cliquez le diviseur droit pour alterner les tailles |
| Onglets n'apparaissent pas | Assurez-vous de cliquer les liens (pas clic-milieu) |
| Thème désynchronisé | Rafraîchissement forcé (Ctrl+Shift+R) |

---

**[Lancer le Navigateur principal (I2) →]({{ '/fr/interfaces/main-navigator/' | relative_url }})**

*Voir aussi : [Interface principale — Publication technique]({{ '/fr/publications/main-interface/' | relative_url }})*

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
