---
layout: publication
title: "Story #23 — Knowledge v2.0 : Du questionnaire à une plateforme d'ingénierie vivante"
description: "L'évolution de Knowledge d'un questionnaire de validation de session à une plateforme d'ingénierie complète avec intégration GitHub Project, visualiseurs de progression de tâches, persistance non-bloquante et interfaces en mode paysage."
pub_id: "Publication #11 — Story #23"
version: "v1"
date: "2026-03-08"
permalink: /fr/publications/success-stories/story-23/
og_image: /assets/og/knowledge-2-en-cayman.gif
keywords: "histoire de succès, knowledge 2.0, GitHub Project, progression de tâches, visualiseur de session, non-bloquant, persistance, paysage"
---

# Story #23 — Knowledge v2.0 : Du questionnaire à une plateforme d'ingénierie vivante

> **Publication parente** : [#11 — Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }})

---

<div class="story-section">

> *« Le système knowledge a commencé comme un simple quiz de validation. Maintenant il gère les tableaux GitHub Project, crée et lie les issues, persiste tout localement quand GitHub est indisponible, affiche la progression des tâches en temps réel, et fait tout ça sans jamais bloquer le flux du développeur. C'est l'évolution v2.0. »*

<div class="story-row">
<div class="story-row-left">

**Détails**

</div>
<div class="story-row-right">

| | |
|---|---|
| Date | 2026-03-08 |
| Catégorie | 🚀 ⚙️ 🏗️ |
| Contexte | Knowledge v2.0 a débuté comme un questionnaire de session (A1-A4) validant les demandes utilisateur avant exécution. Au cours d'une seule journée intense, il a évolué en une plateforme d'ingénierie complète : création/validation de tableaux GitHub Project intégrée comme précondition non-bloquante, création d'issues avec liaison automatique au tableau, persistance locale en cas d'indisponibilité GitHub, visualiseur de progression de tâches, visualiseur de session modulaire avec grilles knowledge en temps réel, et interfaces autonomes en mode paysage. |
| Déclenché par | L'évolution naturelle de la v2.0 pendant les tests d'intégration en direct. Chaque capacité a émergé d'un besoin réel : l'utilisateur voulait que les tableaux projet soient validés avant la création d'issues, mais seulement une fois l'exécution lancée (pas pendant la phase menu où les valeurs peuvent encore changer). Le patron de persistance a émergé du principe que les défaillances de systèmes externes ne doivent jamais bloquer le flux de travail local. |
| Rédigé par | **Claude** (Anthropic, Opus 4.6) — à partir des données de session en direct |

</div>
</div>

## L'arc d'évolution

Ce qui rend cette histoire significative n'est pas une fonctionnalité unique, mais la **cohérence architecturale** qui a émergé à travers 30+ pull requests en une seule journée :

### 1. Intégration des tableaux GitHub Project

La fonction `project_ensure()` a été créée pour valider ou créer les tableaux GitHub Project. La décision de conception clé : elle s'exécute comme **précondition au lancement de l'exécution** (A4), pas pendant le menu de validation (A3). Ceci est important car l'utilisateur peut changer la valeur du projet avant de lancer — exécuter `project_ensure()` prématurément serait inutile et potentiellement incorrect.

```
A3 détecte le repo -> l'utilisateur peut modifier -> exécution lancée -> project_ensure() -> création d'issue -> project_item_add()
```

### 2. Patron de persistance non-bloquant

Chaque opération GitHub suit le même patron de résilience :

| Opération | Succès | GitHub indisponible |
|-----------|--------|---------------------|
| `project_ensure()` | Stocke `project_id`, `project_number` | Stocke `local_only: true`, synchronise plus tard |
| `issue_create()` | Stocke `numero`, `url`, `node_id` | Stocke `titre`, `body` sur disque |
| `project_item_add()` | Lien créé | Stocke `pending_board_link: true` |

L'exécution **ne s'arrête jamais**. Les données sont persistées localement et synchronisées à la prochaine occasion. C'est le principe fondamental : *le flux de travail ne doit pas dépendre de systèmes externes*.

### 3. Visualiseur de progression de tâches

L'interface Task Workflow (I3) a gagné une barre de progression persistante — visible immédiatement après la sélection d'une tâche, au-dessus de tout le contenu spécifique à la vue. Huit étapes affichées comme des points connectés (complété/courant/en attente/ignoré), avec des métadonnées montrant l'étape courante, le pourcentage de complétion, le numéro d'issue et la date.

### 4. Modernisation du visualiseur de session

L'interface Session Review (I1) a été reconstruite avec une architecture JavaScript modulaire (session-core.js + session-blocks.js + session-print.js), auto-détection du contexte repo, et une grille de validation knowledge avec étiquettes bilingues et en-têtes bleu pastel.

### 5. Interfaces en mode paysage

Les trois interfaces (I1 Session Review, I2 Main Navigator, I3 Task Workflow) adoptent maintenant l'orientation paysage par défaut en mode autonome. Le layout `publication.html` détecte `page_type: interface` et configure l'orientation par défaut en conséquence. À l'intérieur de l'iframe du Main Navigator, le panneau central force toujours le paysage sur son contenu.

## Impact

| Métrique | Valeur |
|----------|--------|
| Pull Requests | 30+ fusionnés en une seule journée |
| Nouvelles capacités | 5 majeures (tableau projet, persistance non-bloquante, progression de tâches, visualiseur de session v2, interfaces paysage) |
| Fichiers modifiés | 15+ à travers skills, interfaces, layouts et scripts |
| Principe validé | Indépendance des systèmes externes — les pannes GitHub ne bloquent jamais le flux de travail |
| Version | v2.0 sous-version 2 |

## Qualités démontrées

<div class="story-row">
<div class="story-row-left">

**Validées**

</div>
<div class="story-row-right">

Autosuffisant (#1), Autonome (#2), Intuitif (#3), Concis (#4), Adaptable (#5), Intégré (#13)

</div>
</div>

</div>

## Publications connexes

- [#0 — Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }}) — Publication maître
- [#11 — Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }}) — Hub parent
- [#21 — Machine à états du flux de tâches]({{ '/fr/publications/success-stories/story-21/' | relative_url }}) — Histoire précédente du flux de tâches

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
