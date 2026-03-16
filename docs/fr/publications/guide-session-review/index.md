---
layout: publication
title: "Revue de session — Guide utilisateur"
description: "Comment utiliser l'interface Revue de session : sélectionner des sessions, explorer les métriques, parcourir la chronologie et examiner les livrables."
pub_id: "Guide utilisateur — I1"
version: "v1"
date: "2026-03-16"
lang: fr
permalink: /fr/publications/guide-session-review/
keywords: "guide utilisateur, revue de session, interface, tutoriel"
---

# Revue de session — Guide utilisateur
{: #pub-title}

> **Interface** : [Revue de session (I1)]({{ '/fr/interfaces/session-review/' | relative_url }})

**Sommaire**

| | |
|---|---|
| [Démarrage](#démarrage) | Ouvrir l'interface et sélectionner une session |
| [Sélecteur de session](#sélecteur-de-session) | Choisir et filtrer les sessions |
| [Aperçu des sections](#aperçu-des-sections) | Ce que chaque section affiche |
| [Astuces](#astuces) | Tirer le meilleur parti du visualiseur |

## Démarrage

L'interface Revue de session vous permet d'explorer les sessions de travail terminées — leurs métriques, chronologie, livrables et leçons apprises.

**Pour l'ouvrir :**
- Depuis le **Navigateur principal** : cliquez sur *I1 Revue de session* dans le panneau gauche
- URL directe : `/fr/interfaces/session-review/`

## Sélecteur de session

En haut de l'interface, deux menus déroulants contrôlent l'affichage :

1. **Session** — choisissez une session spécifique ou *Toutes les sessions* pour une vue d'ensemble
2. **Vue** — filtrez par section : Tout, Aperçu des tâches, Tableau de bord métriques, ou Chronologie

Les sessions sont listées par date (plus récentes en premier). Seules les sessions v52+ sont disponibles.

## Aperçu des sections

Chaque rapport de session contient jusqu'à 5 sections :

| Section | Contenu |
|---------|---------|
| **Résumé** | Objectifs, contexte et résultat de la session |
| **Métriques** | Compteurs de messages, utilisation des outils, indicateurs de productivité |
| **Compilation temporelle** | Suivi de durée et allocation du temps |
| **Livrables** | Fichiers créés ou modifiés, commits et artefacts |
| **Leçons apprises** | Ce qui a fonctionné, ce qui n'a pas fonctionné, améliorations |

## Astuces

- **Comparer** : ouvrez deux sessions dans des onglets séparés pour comparer les métriques
- **Imprimer/PDF** : utilisez la fonction d'impression du navigateur — styles optimisés pour l'impression
- **Source de données** : les données proviennent de `docs/data/sessions.json`, rafraîchies en fin de session

---

**[Lancer Revue de session (I1) →]({{ '/fr/interfaces/session-review/' | relative_url }})**

*Voir aussi : [Revue de session — Publication technique]({{ '/fr/publications/session-review/' | relative_url }})*
