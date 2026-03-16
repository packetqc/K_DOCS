---
layout: publication
title: "Visualiseur projets — Guide utilisateur (Complet)"
description: "Guide utilisateur complet pour le Visualiseur projets : navigation, intégration board, suivi des issues, métriques et export."
pub_id: "Guide utilisateur — I4 (Complet)"
version: "v1"
date: "2026-03-16"
lang: fr
permalink: /fr/publications/guide-project-viewer/full/
keywords: "guide utilisateur, visualiseur projets, interface, tutoriel, complet"
---

# Visualiseur projets — Guide utilisateur
{: #pub-title}

> **Interface** : [Visualiseur projets (I4)]({{ '/fr/interfaces/project-viewer/' | relative_url }}) | [Version résumé]({{ '/fr/publications/guide-project-viewer/' | relative_url }})

## Table des matières

| | |
|---|---|
| [Démarrage](#démarrage) | Ouvrir et s'orienter |
| [Liste des projets](#liste-des-projets) | Parcourir tous les projets |
| [Détail du projet](#détail-du-projet) | Plongée dans un projet |
| [Intégration board](#intégration-board) | Boards GitHub Project |
| [Suivi des issues](#suivi-des-issues) | Issues et PRs liées |
| [Métriques de progression](#métriques-de-progression) | Suivi de complétion |
| [Export et impression](#export-et-impression) | Rapports portfolio |
| [Dépannage](#dépannage) | Problèmes courants |

## Démarrage

Le Visualiseur projets (I4) est un tableau de bord portfolio en lecture seule pour tous les projets Knowledge enregistrés.

## Liste des projets

| Colonne | Description |
|---------|------------|
| **P#** | Identifiant unique (ex : P001) |
| **Titre** | Nom du projet |
| **Statut** | Actif, Terminé, En pause ou Archivé |
| **Board** | Lien vers le board GitHub Project |
| **Issues** | Compte ouvertes / fermées |
| **Progression** | Barre de progression visuelle |

## Détail du projet

Cliquez sur un projet pour voir : description, équipe, dates et chronologie des jalons.

## Intégration board

Chaque projet peut être lié à un board GitHub Project avec numéro, lien direct et compte d'items.

## Suivi des issues

Les issues liées affichent : titre, état, étiquettes et assigné.

## Métriques de progression

- **% de complétion** = issues fermées / total
- **Barre de progression** — indicateur visuel
- **Vélocité** — issues fermées par semaine

## Export et impression

Ctrl+P / Cmd+P avec page de couverture auto-générée.

## Dépannage

| Problème | Solution |
|----------|----------|
| Aucun projet listé | Vérifiez `docs/data/projects.json` |
| Lien board cassé | Le board a peut-être été supprimé ou rendu privé |
| Progression à 0% | Aucune issue liée au projet |

---

**[Lancer Visualiseur projets (I4) →]({{ '/fr/interfaces/project-viewer/' | relative_url }})**

*Voir aussi : [Gestion de projet — Publication technique]({{ '/fr/publications/project-management/' | relative_url }})*

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
