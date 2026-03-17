---
layout: publication
title: "Gestion de projet — Documentation complète"
description: "Documentation complète de la gestion de projet dans Knowledge : modèle d'entité, indexation hiérarchique (P#/S#/D#), commandes projet, protocole de bootstrap satellite, création de présence web, entrée ciblée, publication à double origine, intégration GitHub Project et convergence multi-instances."
pub_id: "Publication #12 — Complet"
version: "v1"
date: "2026-02-22"
permalink: /fr/publications/project-management/full/
og_image: /assets/og/project-management-fr-cayman.gif
keywords: "projet, gestion, indexation, satellite, bootstrap, hiérarchie"
---

# Gestion de projet — Documentation complète
{: #pub-title}

**Table des matières**

| | |
|---|---|
| [Auteurs](#auteurs) | Auteurs de la publication |
| [Résumé](#résumé) | Vue d'ensemble du système de gestion de projet |
| [Publications liées](#publications-liées) | Publications parentes et connexes |
| [Modèle d'entité projet](#1-modèle-dentité-projet) | Entité à trois niveaux : logique, physique, plateforme |
| &nbsp;&nbsp;[Relations entre projets](#relations-entre-projets) | Types de relations : possède, enfant de, géré |
| &nbsp;&nbsp;[Registre actuel](#registre-actuel) | Index des projets actifs P0 à P9 |
| &nbsp;&nbsp;[Découplage MPLIB](#découplage-mplib) | MPLIB reclassifié comme projet enfant P1 |
| [Indexation hiérarchique](#2-indexation-hiérarchique-psd) | Schéma d'identifiants P#/S#/D# |
| [Commandes projet](#3-commandes-projet) | Commandes CLI pour la gestion de projet |
| [Protocole de bootstrap satellite](#4-protocole-de-bootstrap-satellite) | Installation satellite multi-rondes |
| &nbsp;&nbsp;[Guidage console](#guidage-console-pont-humain) | UX pont humain pour les étapes de bootstrap |
| &nbsp;&nbsp;[Étape 1 — Bootstrap](#étape-1--bootstrap) | Fichiers essentiels et squelette CLAUDE.md |
| &nbsp;&nbsp;[Étape 2 — Normaliser](#étape-2--normaliser) | Application de concordance structurelle |
| &nbsp;&nbsp;[Étape 3 — Créer le projet](#étape-3--créer-le-projet-optionnel) | Présence web et configuration GitHub board |
| &nbsp;&nbsp;[Principe du sous-ensemble critique](#principe-du-sous-ensemble-critique) | ADN comportemental qui survit à la compaction |
| [Création de présence web](#5-création-de-présence-web) | Création de la structure docs GitHub Pages |
| [Entrée ciblée](#6-entrée-ciblée--alias-dappel) | Système d'entrée ciblée `#N:` |
| &nbsp;&nbsp;[Projet principal implicite](#projet-principal-implicite) | Routage par défaut sans préfixe `#N:` |
| &nbsp;&nbsp;[Mode dump brut](#mode-dump-brut) | Classification d'entrée non structurée |
| &nbsp;&nbsp;[Convergence multi-satellites](#convergence-multi-satellites) | Même projet documenté depuis plusieurs dépôts |
| &nbsp;&nbsp;[Détection subconsciente](#détection-subconsciente) | Correspondance automatique insight-publication |
| [Système de liens à double origine](#7-système-de-liens-à-double-origine) | Badges d'origine core vs satellite |
| [Intégration GitHub Project](#8-intégration-github-project) | Création et liaison de boards Projects v2 |
| [Intégration avec les commandes existantes](#9-intégration-avec-les-commandes-existantes) | Extension de harvest, normalize, pub par les commandes projet |
| [Préservation des URLs](#10-préservation-des-urls) | Schéma d'URLs rétrocompatible |
| [Mises à jour concurrentes multi-instances](#11-mises-à-jour-concurrentes-multi-instances) | Édition concurrente par ajout uniquement |
| [Assets requis par projet](#12-assets-requis-par-projet) | Fichiers et assets obligatoires par projet |
| [Cycle de vie du projet](#13-cycle-de-vie-du-projet) | Enregistrer, créer, publier, récolter, évoluer |

## Auteurs

**Martin Paquet** — Analyste et programmeur sécurité réseau, administrateur de sécurité des réseaux et des systèmes, et analyste programmeur et concepteur logiciels embarqués. A conçu le modèle d'entité projet qui donne une identité formelle au réseau de connaissances distribué.

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. Implémente les commandes projet, le bootstrap satellite et la création de présence web à travers le réseau de connaissances.

---

## Résumé

À mesure que le réseau de connaissances est passé d'un seul dépôt à 6+ projets avec plusieurs satellites chacun, un vide structurel est apparu : **les projets n'avaient pas d'identité formelle**. Les dépôts existaient, les publications existaient, les satellites existaient — mais l'entité qui les relie (le projet) était implicite.

La publication #12 documente le modèle d'entité projet v35 qui rend les projets explicites : indexation hiérarchique (P#/S#/D#), modèle à trois niveaux (logique, physique, plateforme), publication à double origine, gestion du cycle de vie satellite et les commandes qui les opèrent.

Cette publication consolide quatre documents de méthodologie :

| Document | Portée |
|----------|--------|
| **Gestion de projet** | Modèle d'entité, indexation, commandes, intégration |
| **Bootstrap satellite** | Protocole de staging itératif en session unique |
| **Création de projet** | Création de présence web pour les satellites |
| **Entrée ciblée** | Alias d'appel `#` pour les connaissances scopées |

---

## Publications liées

| # | Publication | Relation |
|---|------------|----------|
| 0 | [Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — la gestion de projet étend le système central |
| 4 | [Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) | Architecture — les projets organisent le réseau distribué |
| 4a | [Tableau de bord]({{ '/fr/publications/distributed-knowledge-dashboard/' | relative_url }}) | Tableau de bord — statut des projets affiché dans la vue réseau |
| 7 | [Protocole Harvest]({{ '/fr/publications/harvest-protocol/' | relative_url }}) | Collecte — harvest opère sur le contenu indexé par projet |
| 8 | [Gestion de session]({{ '/fr/publications/session-management/' | relative_url }}) | Cycle de vie — les sessions opèrent dans le contexte du projet |
| 11 | [Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }}) | Validation — les jalons de projet deviennent des histoires |

---

## 1. Modèle d'entité projet

Un **projet** est une entité de premier ordre qui existe à trois niveaux :

| Niveau | Signification | Exemple |
|--------|--------------|---------|
| **Logique** | Un corps de travail organisé avec publications, documentation, évolution, histoires | Knowledge (P0) |
| **Physique** | Un ou plusieurs dépôts Git (satellites), ou **aucun** pour les projets gérés | `packetqc/knowledge`, `packetqc/MPLIB` |
| **Plateforme** | Un tableau GitHub Project pour le suivi | Entité GitHub Project (quand élevé) |

Un projet **n'est pas** un dépôt — il **a** des dépôts. Un projet **n'est pas** une publication — il **a** des publications.

### Relations entre projets

| Relation | Signification | Exemple |
|----------|--------------|---------|
| **possède** | Dépôt principal du projet | P0 possède `packetqc/knowledge` |
| **enfant de** | Sous-projet d'un projet parent | P1 (MPLIB) est enfant de P0 |
| **géré** | Aucun dépôt dédié — vit dans un dépôt hôte ou le core | Documentation, processus, initiatives transversales — le tableau est toujours lié à un dépôt |

**Les projets gérés** peuvent vivre comme sous-dossiers dans un dépôt hôte ou uniquement dans le core. Ils obtiennent leur propre P#. Leur tableau GitHub Project est toujours lié à un dépôt : les projets enfants lient à leur propre dépôt, les projets gérés lient au dépôt hôte (ou au dépôt core par défaut). Chaque projet est lié à un dépôt — sans exception.

### Import basé sur la promotion

Quand un projet géré mûrit, le **cycle de promotion** gère l'import et la normalisation :

| Phase | Action |
|-------|--------|
| **Découvrir** | `harvest` détecte le contenu d'un autre projet |
| **Router** | Contenu routé vers l'entrée `minds/` du bon projet |
| **Enregistrer** | Si le projet n'existe pas, `project register` assigne un P# |
| **Réviser** | `harvest --review` valide le contenu |
| **Préparer** | `harvest --stage N <type>` prépare pour l'intégration (type : lesson, pattern, methodology, evolution, docs, project) |
| **Promouvoir** | `harvest --promote N` écrit dans les assets du projet |
| **Normaliser** | `normalize` assure que le contenu suit les conventions |

### Registre actuel

| ID | Projet | Type | Statut |
|----|--------|------|--------|
| P0 | Knowledge | core | actif |
| P1 | MPLIB | enfant | actif |
| P2 | STM32 PoC | enfant | actif |
| P3 | knowledge-live | enfant | actif |
| P4 | MPLIB Dev Staging | enfant (de P1) | actif |
| P5 | PQC | enfant | pré-bootstrap |

### Découplage MPLIB

MPLIB est reclassifié d'asset core à projet enfant (P1). Le titre de l'index des publications est passé de « MPLIB Knowledge » à « Knowledge ». La publication #1 porte la référence croisée `P0/#1 ->P1`.

---

## 2. Indexation hiérarchique (P#/S#/D#)

Trois niveaux d'indexation :

```
Niveau 1: P<n>                    <- Identifiant de projet
Niveau 2: P<n>/S<m>              <- Satellite (instance de dépôt)
Niveau 3: P<n>/#<pub>            <- Publication
           P<n>/S<m>/D<k>         <- Document local au satellite
```

Convention d'affichage : l'index apparaît **à gauche** de l'indicateur de statut dans tous les inventaires. Le marqueur `->P<n>` indique une publication qui documente un projet différent.

---

## 3. Commandes projet

| Commande | Action |
|----------|--------|
| `project list` | Lister les projets avec index P#, type, statut, nombre de satellites |
| `project info <P#>` | Détails du projet — identité, publications, satellites, évolution, histoires, assets |
| `project create <nom>` | Création complète : P# + scaffold + GitHub Project (élevé) + web |
| `project register <nom>` | Enregistrer un projet avec ID P# — crée `projects/<slug>.md` |
| `project review <P#>` | Réviser l'état du projet — docs, pubs, assets, fraîcheur |
| `project review --all` | Réviser tous les projets |

---

## 4. Protocole de bootstrap satellite

Staging itératif en session unique — une session fait tout, l'utilisateur fusionne entre les étapes.

```
Étape 1 : wakeup -> scaffold bootstrap -> commit -> push -> PR
          l'utilisateur fusionne -> refresh -> vérifier étape 1

Étape 2 : normaliser -> trim vers critical-subset -> commit -> push -> PR
          l'utilisateur fusionne -> refresh -> vérifier étape 2

Étape 3 : project create (optionnel) -> commit -> push -> PR
          l'utilisateur fusionne -> refresh -> vérifier étape 3

Final :   « Installation terminée. Toute nouvelle session fera auto-wakeup. »
```

### Guidage console (pont humain)

La session guide activement l'utilisateur à chaque étape manuelle. Ne jamais rester silencieux entre les étapes — toujours imprimer ce qui s'est passé, ce que l'utilisateur doit faire et ce qui suit.

### Étape 1 — Bootstrap

Le wakeup étape 0.5 crée les fichiers essentiels manquants (non destructif) :

| Fichier | Contenu |
|---------|---------|
| `CLAUDE.md` | Sous-ensemble critique (~180 lignes) : pointeur knowledge + ADN comportemental + commandes |
| `README.md` | Nom du dépôt, description, lien vers knowledge |
| `LICENSE` | MIT avec l'année courante |
| `.gitignore` | Ignores standards |
| `notes/.gitkeep` | Dossier de persistance de session |

### Étape 2 — Normaliser

Trim le CLAUDE.md satellite vers la forme critical-subset (~180 lignes). Retirer le contenu d'implémentation profond sur-syncé à l'étape 1. Garder : pointeur knowledge, protocole de session, protocole save, protocole de branche, pont humain, référence complète des 7 groupes de commandes.

### Étape 3 — Créer le projet (optionnel)

Créer la présence web avec `project create <nom>`. Nécessaire uniquement si le satellite produira de la documentation ou des publications.

### Principe du sous-ensemble critique

Le CLAUDE.md satellite porte assez d'ADN pour maintenir un comportement correct même après compaction du contexte. Le thin-wrapper (~30 lignes) perdait tout après compaction. Le critical-subset (~180 lignes) survit. Le miroir complet (~2600 lignes) créerait trop de dérive de version.

---

## 5. Création de présence web

`project create <nom>` construit un site GitHub Pages bilingue complet :

```
<satellite>/
  docs/
    _config.yml, _layouts/, index.md, publications/index.md
    fr/index.md, fr/publications/index.md
    assets/og/.gitkeep
  publications/.gitkeep
```

**10 fichiers, 6 répertoires.** Layouts copiés de knowledge — autonomes, aucune dépendance externe.

---

## 6. Entrée ciblée (alias d'appel `#`)

Le préfixe `#` déclenche le mode d'entrée de connaissances scopées.

| Commande | Action |
|----------|--------|
| `#N: <contenu>` | Note scopée pour la publication/projet #N |
| `#N:methodology:<sujet>` | Insight méthodologique — marqué pour récolte |
| `#N:principle:<sujet>` | Principe de design — marqué pour récolte |
| `#N:info` | Afficher les connaissances accumulées pour #N |
| `#N:done` | Terminer la documentation, compiler le résumé |

### Projet principal implicite

Chaque dépôt a un projet principal. Sans préfixe `#N:`, Claude assume le projet principal du dépôt.

### Mode dump brut

`#N:` accepte l'entrée brute non structurée. Claude classifie en utilisant les connaissances acquises + universelles. Point d'entrée à friction minimale.

### Convergence multi-satellites

Le même projet peut être documenté depuis plusieurs satellites. `#N:` est la clé de routage, pas le dépôt. Harvest unifie toutes les notes distribuées dans `minds/`, la promotion les converge dans le core.

### Détection subconsciente

Pendant la conversation, Claude surveille le contenu lié au domaine d'une publication. Quand c'est évident, Claude suggère la capture — légèrement, pas à chaque message.

---

## 7. Système de liens à double origine

| Origine | Badge | URL de base | Signification |
|---------|-------|-------------|---------------|
| **Core** | **core** | `packetqc.github.io/knowledge/` | Révisé, publié, canonique |
| **Satellite** | *satellite* | `packetqc.github.io/<repo>/` | Développement, staging, local |

Les deux sont valides — même technologie, stade de révision différent.

---

## 8. Intégration GitHub Project

Quand élevé, `project create` crée un tableau GitHub Project — la **couche d'interface humaine**. Deux points d'entrée : `project create` (scaffolding de nouveau projet) et `harvest --promote` (les insights promus créent ou mettent à jour les items du tableau).

| Knowledge (IA-natif) | GitHub Project (humain-natif) |
|------------------------------------------|-------------------------------|
| Métadonnées `projects/<slug>.md` | Tableau avec cartes |
| Entrées d'évolution (v#) | Jalons |
| Insights harvest | Issues (auto-créées) |
| Notes de session | Chronologie d'activité |

Le tableau est la **projection lisible par l'humain** de l'état du projet IA-natif.

---

## 9. Intégration avec les commandes existantes

| Commande | Ce que la gestion de projet ajoute |
|----------|-------------------------------------|
| `harvest --healthcheck` | Tableau de statut des projets |
| `normalize` | Concordance projet — registre, P# uniques, références croisées |
| `pub list` | Colonne d'index projet — `P0/#1` avec `->P1` |
| `doc review --list` | Index projet dans l'inventaire de fraîcheur |

---

## 10. Préservation des URLs

La restructuration projet est **additive** — aucune URL existante ne change. Les pages hub de projet (`/projects/`, `/fr/projects/`) fournissent une couche de navigation supplémentaire qui pointe vers les URLs existantes, organisées par projet.

---

## 11. Mises à jour concurrentes multi-instances

| Mécanisme | Détail |
|-----------|--------|
| **Indexation append-only** | Chaque instance ajoute, ne remplace jamais |
| **Suivi de provenance** | Marqueur `<!-- last-updated-by -->` par document |
| **Concaténation harvest** | Fusionne les index de tous les satellites |
| **Résolution de conflits** | Le timestamp `last-updated` le plus récent gagne |

---

## 12. Assets requis par projet

| Asset | Core (P0) | Enfant (P1+) | But |
|-------|-----------|-------------|-----|
| `CLAUDE.md` | Complet (~2600 lignes) | Sous-ensemble critique (~180 lignes) | ADN comportemental |
| `notes/` | Notes de session | Notes de session | Mémoire éphémère |
| `projects/<nom>.md` | Dans le dépôt core | Enregistré dans le core | Métadonnées projet |
| `live/` | Assets knowledge | Sync depuis le core | Outillage |

---

## 13. Cycle de vie du projet

```
découvrir -> enregistrer -> bootstrap -> créer (plateforme) -> publier -> récolter -> évoluer
```

| Phase | Ce qui se passe | Commande |
|-------|----------------|----------|
| **Découvrir** | Nouveau satellite ou projet conçu | Manuel ou `harvest --healthcheck` |
| **Enregistrer** | ID P# assigné, `projects/<nom>.md` créé | `project register <nom>` |
| **Bootstrap** | CLAUDE.md, notes/, live/, pointeur knowledge | `wakeup` étape 0.5 |
| **Créer** | Tableau GitHub Project + présence web | `project create <nom>` |
| **Publier** | Publications créées et indexées | `pub new <slug>` |
| **Récolter** | Connaissances reviennent vers le core | `harvest <projet>` |
| **Évoluer** | Le journal d'évolution grandit | Continu |

---

## Historique des versions

| Version | Date | Modifications |
|---------|------|---------------|
| v1 | 2026-02-22 | Publication initiale — modèle d'entité projet, indexation, commandes, bootstrap, présence web, entrée ciblée |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
