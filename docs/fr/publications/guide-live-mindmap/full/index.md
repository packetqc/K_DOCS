---
layout: publication
title: "Mindmap vivant — Guide utilisateur (Complet)"
description: "Guide utilisateur complet pour l'interface Mindmap vivant : navigation, types de nœuds, filtrage, thèmes et fonctionnalités avancées."
pub_id: "Guide utilisateur — I5 (Complet)"
version: "v1"
date: "2026-03-16"
lang: fr
permalink: /fr/publications/guide-live-mindmap/full/
keywords: "guide utilisateur, mindmap vivant, interface, tutoriel, complet"
---

# Mindmap vivant — Guide utilisateur
{: #pub-title}

> **Interface** : [Mindmap vivant (I5)]({{ '/fr/interfaces/live-mindmap/' | relative_url }}) | [Version résumé]({{ '/fr/publications/guide-live-mindmap/' | relative_url }})

## Table des matières

| | |
|---|---|
| [Démarrage](#démarrage) | Ouvrir et s'orienter |
| [Contrôles de navigation](#contrôles-de-navigation) | Déplacer, zoomer, sélectionner |
| [Groupes de nœuds](#groupes-de-nœuds) | Catégories de connaissances |
| [Détails des nœuds](#détails-des-nœuds) | Contenu des nœuds |
| [Support thème](#support-thème) | Rendu clair et sombre |
| [Source de données](#source-de-données) | D'où viennent les données |
| [Dépannage](#dépannage) | Problèmes courants |

## Démarrage

Le Mindmap vivant (I5) est une visualisation interactive du système de mémoire Knowledge. Propulsé par MindElixir v5, il affiche l'arbre de connaissances complet.

## Contrôles de navigation

| Action | Comment |
|--------|---------|
| **Déplacer** | Cliquer-glisser le fond |
| **Zoomer** | Molette ou pincement |
| **Sélectionner** | Cliquer un nœud |
| **Déplier/Replier** | Cliquer le bouton ± |
| **Centrer** | Double-cliquer un nœud |
| **Ajuster la vue** | Bouton d'ajustement dans la barre d'outils |

## Groupes de nœuds

Le nœud racine est `knowledge`, avec les groupes :

| Groupe | Couleur | Signification |
|--------|---------|--------------|
| **architecture** | Bleu | Conception système |
| **contraintes** | Rouge | Limites strictes |
| **conventions** | Vert | Modèles et standards |
| **travail** | Orange | État des réalisations |
| **session** | Violet | Contexte de conversation |
| **documentation** | Gris | Références documentaires |

## Détails des nœuds

Chaque nœud correspond à une ligne du fichier mermaid source. Les nœuds représentent des catégories, des éléments de connaissance ou des indicateurs d'état.

## Support thème

Le mindmap s'adapte automatiquement au thème clair/sombre du site. Les changements se propagent en temps réel.

## Source de données

- **Primaire** : `Knowledge/K_MIND/files/mind/architecture-mindmap.md`
- **Moteur** : MindElixir v5
- **Mise à jour** : au début de chaque session et pendant la maintenance mémoire

## Dépannage

| Problème | Solution |
|----------|----------|
| Mindmap vide | Vérifiez le fichier source mermaid |
| Nœuds illisibles | Utilisez le zoom ou le bouton d'ajustement |
| Thème désynchronisé | Rafraîchissement forcé (Ctrl+Shift+R) |
| Performance lente | Repliez les branches inutilisées |

---

**[Lancer Mindmap vivant (I5) →]({{ '/fr/interfaces/live-mindmap/' | relative_url }})**

*Voir aussi : [Mindmap vivant — Publication technique]({{ '/fr/publications/live-mindmap/' | relative_url }})*

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
