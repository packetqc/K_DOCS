---
layout: publication
title: "Gestion de projet — Entités de premier ordre, indexation hiérarchique et cycle de vie satellite"
description: "Les projets comme entités de premier ordre dans Knowledge : indexation hiérarchique (P#/S#/D#), modèle d'entité à trois niveaux, protocole de bootstrap satellite, création de présence web, entrée ciblée pour connaissances scopées, publication à double origine et intégration GitHub Project."
pub_id: "Publication #12"
version: "v1"
date: "2026-02-22"
permalink: /fr/publications/project-management/
og_image: /assets/og/project-management-fr-cayman.gif
keywords: "projet, gestion, indexation, satellite, bootstrap, hiérarchie"
---

# Gestion de projet — Entités de premier ordre
{: #pub-title}

> **Publication parente** : [#0 — Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Architecture** : [#4 — Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Vue d'ensemble du système de gestion de projet |
| [Modèle d'entité projet](#modèle-dentité-projet) | Entité à trois niveaux : logique, physique, plateforme |
| [Indexation hiérarchique](#indexation-hiérarchique-psd) | Schéma d'identifiants P#/S#/D# |
| [Commandes projet](#commandes-projet) | Commandes CLI pour la gestion de projet |
| [Bootstrap satellite](#protocole-de-bootstrap-satellite) | Protocole d'installation satellite multi-rondes |
| [Création de présence web](#création-de-présence-web) | Création de la structure docs GitHub Pages |
| [Entrée ciblée](#entrée-ciblée--alias-dappel) | Système d'entrée ciblée `#N:` |
| [Liens à double origine](#système-de-liens-à-double-origine) | Badges d'origine core vs satellite |

## Résumé

À mesure que le réseau de connaissances est passé de 1 dépôt à 6+ projets avec plusieurs satellites chacun, un vide structurel est apparu : les projets n'avaient pas d'identité formelle. La publication #12 documente le modèle d'entité projet v35 — indexation hiérarchique (P#/S#/D#), entités à trois niveaux (logique, physique, plateforme), gestion du cycle de vie satellite et les commandes qui les opèrent. Consolide quatre documents de méthodologie : gestion de projet, bootstrap satellite, création de projet et entrée ciblée.

## Modèle d'entité projet

Un **projet** existe à trois niveaux : **logique** (travail organisé avec publications, évolution, histoires), **physique** (dépôts Git, ou **aucun** pour les projets gérés) et **plateforme** (tableau GitHub Project). Un projet n'est pas un dépôt — il a des dépôts. Registre actuel : P0 (Knowledge, core), P1 (MPLIB), P2 (STM32 PoC), P3 (knowledge-live), P4 (MPLIB Dev Staging), P5 (PQC).

Trois types de relations : **possède** (dépôt principal), **enfant de** (sous-projet), **géré** (aucun dépôt dédié — vit dans un dépôt hôte ou le core, le tableau est toujours lié à un dépôt).

## Indexation hiérarchique (P#/S#/D#)

Trois niveaux : `P<n>` (projet), `P<n>/S<m>` (satellite), `P<n>/#<pub>` ou `P<n>/S<m>/D<k>` (document). Le marqueur inter-projets `->P<n>` indique qu'une publication documente un projet différent. L'index apparaît à gauche de l'indicateur de statut dans tous les inventaires.

## Commandes projet

| Commande | Action |
|----------|--------|
| `project list` | Lister les projets avec index P#, type, statut, nombre de satellites |
| `project info <P#>` | Détails du projet — identité, publications, satellites, évolution |
| `project create <nom>` | Création complète : P# + scaffold + GitHub Project (élevé) + web |
| `project register <nom>` | Enregistrer un projet avec ID P# — crée `projects/<slug>.md` |
| `project review <P#>` | Réviser l'état du projet — docs, pubs, assets, fraîcheur |
| `project review --all` | Réviser tous les projets |

## Protocole de bootstrap satellite

Staging itératif en session unique : Étape 1 (scaffold bootstrap) -> Étape 2 (normaliser vers critical-subset) -> Étape 3 (présence web, optionnel). Une seule action manuelle par étape : fusionner la PR. Le guidage console (pont humain) imprime ce qui s'est passé, ce que l'utilisateur doit faire et ce qui se passe ensuite à chaque étape.

## Création de présence web

`project create <nom>` construit un site GitHub Pages bilingue complet : config Jekyll, layouts (copiés de knowledge), pages d'accueil EN/FR, hubs de publications, placeholders d'assets. 10 fichiers, 6 répertoires. Autonome — aucune dépendance à un thème externe.

## Entrée ciblée (alias d'appel `#`)

`#N:` route le contenu vers la publication/projet N. `#N:methodology:<sujet>` et `#N:principle:<sujet>` marquent pour la récolte. `#N:info` affiche les connaissances accumulées. Mode dump brut — l'utilisateur fournit l'intelligence, Claude classifie. Convergence multi-satellites : même projet documenté depuis n'importe quel dépôt, harvest unifie.

## Système de liens à double origine

Les liens core (`knowledge/`) sont canoniques. Les liens satellite (`<repo>/`) sont en staging. Les deux sont valides — même technologie, stade de révision différent. Badge d'origine dans les pages hub de projet.

---

[**Lire la documentation complète →**]({{ '/fr/publications/project-management/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
