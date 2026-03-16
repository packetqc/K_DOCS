---
layout: publication
title: "Flux de travail — Guide utilisateur (Complet)"
description: "Guide utilisateur complet pour l'interface Flux de travail : progression des étapes, portes de validation, vues, export et dépannage."
pub_id: "Guide utilisateur — I3 (Complet)"
version: "v1"
date: "2026-03-16"
lang: fr
permalink: /fr/publications/guide-tasks-workflow/full/
keywords: "guide utilisateur, flux de travail, interface, tutoriel, complet"
---

# Flux de travail — Guide utilisateur
{: #pub-title}

> **Interface** : [Flux de travail (I3)]({{ '/fr/interfaces/task-workflow/' | relative_url }}) | [Version résumé]({{ '/fr/publications/guide-tasks-workflow/' | relative_url }})

## Table des matières

| | |
|---|---|
| [Démarrage](#démarrage) | Ouvrir et s'orienter |
| [Sélecteur de tâche](#sélecteur-de-tâche) | Choisir et filtrer |
| [Vue Tableau de bord](#vue-tableau-de-bord) | Vue d'ensemble |
| [Vue Détail](#vue-détail) | Informations complètes |
| [Vue Validation](#vue-validation) | Conformité et tests |
| [Étapes du flux](#étapes-du-flux) | Cycle de vie en 8 étapes |
| [Export et impression](#export-et-impression) | Sortie PDF |
| [Dépannage](#dépannage) | Problèmes courants |

## Démarrage

L'interface Flux de travail (I3) visualise la progression des tâches à travers un cycle de vie en 8 étapes. C'est l'interface par défaut chargée dans le panneau central du Navigateur principal.

## Sélecteur de tâche

**Menu Tâche** — Liste toutes les tâches suivies. *Toutes les tâches* pour le tableau de bord.

**Menu Vue** — Trois vues : Tableau de bord, Détail, Validation.

## Vue Tableau de bord

- **Distribution des étapes** — combien de tâches dans chaque étape
- **Barres de progression** — progression visuelle par tâche
- **Activité récente** — dernières transitions d'étapes
- **Taux de complétion** — pourcentage de tâches atteignant TERMINÉ

## Vue Détail

Sélectionnez une tâche pour voir :
- **Métadonnées** — ID, titre, date de création
- **Historique des étapes** — transitions chronologiques avec horodatages
- **Issues liées** — issues et PRs GitHub associées
- **Livrables** — fichiers, commits et artefacts produits

## Vue Validation

- **Portes de validation** — quelles portes passées/échouées par transition
- **Statut des tests** — résultats des tests unitaires
- **Conformité** — respect des exigences du cycle d'ingénierie

## Étapes du flux

| # | Étape | Condition d'entrée | Porte de sortie |
|---|-------|--------------------|-----------------|
| 1 | **INITIAL** | Tâche reçue | Classification terminée |
| 2 | **CLASSIFIÉ** | Type défini | Plan créé |
| 3 | **PLANIFIÉ** | Plan approuvé | Travail commencé |
| 4 | **EN_COURS** | Développement actif | Implémentation terminée |
| 5 | **REVUE** | Revue code/travail | Vérifications passées |
| 6 | **VALIDÉ** | Validation passée | Commit et push |
| 7 | **LIVRÉ** | Poussé au remote | Métriques enregistrées |
| 8 | **TERMINÉ** | Tâche fermée | — |

## Export et impression

Ctrl+P / Cmd+P pour l'impression. Page de couverture auto-générée.

## Dépannage

| Problème | Solution |
|----------|----------|
| Aucune tâche listée | Vérifiez `docs/data/tasks.json` |
| Étape inconnue | La tâche utilise peut-être un ancien nom d'étape |
| Barres de progression vides | Assurez-vous que les tâches ont des horodatages de transition |

---

**[Lancer Flux de travail (I3) →]({{ '/fr/interfaces/task-workflow/' | relative_url }})**

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
