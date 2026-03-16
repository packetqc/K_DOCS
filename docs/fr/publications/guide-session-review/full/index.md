---
layout: publication
title: "Revue de session — Guide utilisateur (Complet)"
description: "Guide utilisateur complet pour l'interface Revue de session : navigation, interprétation des métriques, export et utilisation avancée."
pub_id: "Guide utilisateur — I1 (Complet)"
version: "v1"
date: "2026-03-16"
lang: fr
permalink: /fr/publications/guide-session-review/full/
keywords: "guide utilisateur, revue de session, interface, tutoriel, complet"
---

# Revue de session — Guide utilisateur
{: #pub-title}

> **Interface** : [Revue de session (I1)]({{ '/fr/interfaces/session-review/' | relative_url }}) | [Version résumé]({{ '/fr/publications/guide-session-review/' | relative_url }})

## Table des matières

| | |
|---|---|
| [Démarrage](#démarrage) | Ouvrir et s'orienter |
| [Sélecteur de session](#sélecteur-de-session) | Choisir et filtrer |
| [Section Résumé](#section-résumé) | Objectifs, contexte, résultat |
| [Tableau de bord métriques](#tableau-de-bord-métriques) | Graphiques et indicateurs |
| [Compilation temporelle](#compilation-temporelle) | Durée et allocation |
| [Livrables](#livrables) | Fichiers, commits, artefacts |
| [Leçons apprises](#leçons-apprises) | Améliorations de processus |
| [Export et impression](#export-et-impression) | PDF et options d'impression |
| [Dépannage](#dépannage) | Problèmes courants |

## Démarrage

L'interface Revue de session (I1) est un visualiseur en lecture seule pour les sessions de travail terminées. Chaque session capture tout ce qui s'est passé durant une conversation : ce qui a été accompli, combien de temps cela a pris, quels outils ont été utilisés et ce qui a été appris.

**Ouvrir l'interface :**
- Depuis le **Navigateur principal** (I2) : cliquez sur *I1 Revue de session* dans la section Interfaces
- URL directe : `/fr/interfaces/session-review/`
- L'interface se charge dans le panneau central du navigateur

## Sélecteur de session

Deux menus déroulants en haut :

**Menu Session** — Liste toutes les sessions disponibles par date et titre (plus récentes en premier). Sélectionnez *Toutes les sessions* pour une vue d'ensemble.

**Menu Vue** — Filtrer l'affichage :
- *Toutes les sections* — rapport de session complet
- *Aperçu des tâches* — focus sur la progression des tâches
- *Tableau de bord métriques* — graphiques et chiffres uniquement
- *Chronologie* — flux chronologique des messages

> **Note** : Seules les sessions à partir de la version 52+ (2026-02-27) apparaissent.

## Section Résumé

Le résumé fournit un aperçu rapide :
- **Objectifs de la session** — ce que la session devait accomplir
- **Contexte** — projet, branche, état initial
- **Résultat** — ce qui a été réalisé, ce qui reste

## Tableau de bord métriques

Graphiques visuels de productivité :
- **Compteurs de messages** — messages utilisateur, réponses assistant, appels d'outils
- **Utilisation des outils** — quels outils utilisés et à quelle fréquence
- **Indicateurs de productivité** — tâches complétées, fichiers modifiés, commits créés

Les graphiques sont interactifs — survolez pour les valeurs exactes.

## Compilation temporelle

Suivi détaillé du temps :
- **Durée totale** — début à fin
- **Temps actif** — temps entre messages (exclut l'inactivité)
- **Temps par tâche** — durée de chaque tâche
- **Allocation du temps** — diagramme circulaire de la distribution

## Livrables

Tout ce que la session a produit :
- **Fichiers créés** — nouveaux fichiers ajoutés au dépôt
- **Fichiers modifiés** — fichiers existants modifiés
- **Commits** — commits git avec messages
- **Artefacts** — publications, diagrammes, scripts ou autres résultats

## Leçons apprises

Perspectives de processus capturées durant la session :
- **Ce qui a bien fonctionné** — modèles à répéter
- **Ce qui n'a pas fonctionné** — erreurs ou blocages
- **Améliorations de processus** — suggestions pour les futures sessions

## Export et impression

L'interface supporte l'export optimisé pour l'impression :
1. Utilisez la fonction d'impression du navigateur (Ctrl+P / Cmd+P)
2. Une page de couverture est générée automatiquement
3. Les graphiques sont rendus en images statiques à l'impression
4. Sélectionnez *PDF* comme destination pour l'export numérique

## Dépannage

| Problème | Solution |
|----------|----------|
| Aucune session listée | Vérifiez que `docs/data/sessions.json` existe et n'est pas vide |
| Sections vides | La session a peut-être été interrompue avant le résumé pré-sauvegarde |
| Graphiques non rendus | Assurez-vous que JavaScript est activé ; essayez un rafraîchissement forcé |
| Données périmées | Les données sont rafraîchies en fin de session, pas en temps réel |

---

**[Lancer Revue de session (I1) →]({{ '/fr/interfaces/session-review/' | relative_url }})**

*Voir aussi : [Revue de session — Publication technique]({{ '/fr/publications/session-review/' | relative_url }})*

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
