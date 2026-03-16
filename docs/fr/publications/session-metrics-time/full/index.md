---
layout: publication
title: "Métriques de session et compilation temporelle — Complet"
description: "Méthodologie complète pour les métriques de session et la compilation temporelle : grille de catégories partagée, détail des métriques par todo et tâche, blocs temporels, checklists d'intégration méthodologique, protocole de cumul et exemple concret de la session du 2026-02-26."
pub_id: "Publication #20 — Complet"
version: "v1"
date: "2026-02-26"
permalink: /fr/publications/session-metrics-time/full/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "métriques de session, compilation temporelle, mesure de productivité, tables cumulables, grille de catégories, méthodologie"
---

# Métriques de session et compilation temporelle — Documentation complète
{: #pub-title}

> **Résumé** : [Publication #20]({{ '/fr/publications/session-metrics-time/' | relative_url }}) | **Parent** : [#0 — Système de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }})

**Sommaire**

| | |
|---|---|
| [Résumé](#résumé) | Mesurer la productivité assistée par IA |
| [Le problème](#le-problème) | Ce qui se perd, pourquoi c'est important |
| [La solution](#la-solution) | Grille de catégories, fiche de métriques, feuille de temps |
| [Exemple concret](#exemple-concret--session-2026-02-26) | Compilation complète de session |
| [Intégration méthodologique](#intégration-méthodologique) | Routines post-session |
| [Impact](#impact) | Avant/après, principes de design |

---

## Auteurs

**Martin Paquet** — Analyste-programmeur en sécurité réseau, administrateur de sécurité réseau et systèmes, et concepteur-programmeur de logiciels embarqués. Architecte de la méthodologie de compilation des métriques et du temps — née du besoin de démontrer que les sessions assistées par IA livrent la production hebdomadaire d'une équipe en une seule journée.

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. Co-auteur et compilateur des données de session qui valident cette méthodologie. La compilation elle-même a été produite pendant la session qu'elle mesure.

---

## Résumé

Chaque session de travail interactive génère deux classes de données précieuses : les **métriques** (ce qui a été produit) et le **temps** (combien de temps ça a pris). Ces données sont dispersées dans les commits, les PRs, les billets, les éléments de board et les notes de session — précieuses mais non structurées. Sans compilation, la preuve de productivité disparaît avec la session.

Cette publication introduit **deux méthodologies de compilation** — les fiches de métriques et les feuilles de temps — qui transforment l'activité de session en tables structurées et cumulables. La même grille de catégories (diagnostic, conception, documentation, gestion documentaire, collatéral) organise les deux compilations, avec les **todos comme éléments principaux** et les **tâches comme sous-éléments** dans chaque catégorie.

L'idée clé : ces tables sont **cumulables entre sessions**. Une compilation de session unique montre le travail d'une journée. En cumulant plusieurs sessions, on obtient le sprint d'une semaine. La même grille, les mêmes catégories, la même structure — permettant sommes, moyennes et analyse de tendances sur n'importe quelle période.

La preuve est la session elle-même : 26 février 2026 — 20 PRs fusionnés, ~18 000 lignes ajoutées, 288 fichiers modifiés, 6 publications créées, 4 méthodologies écrites, 3 pièges documentés, répartis sur 5 catégories de travail en environ 10 heures de travail actif. La production hebdomadaire d'une équipe, compilée et mesurée.

---

## Le problème

### Ce qui se perd

| Donnée | Où elle existe | Ce qui se passe |
|--------|---------------|-----------------|
| Fichiers modifiés | `git log --stat` | Enfouis dans 137 commits |
| Temps passé | Horodatages des commits | Dispersés, pas d'agrégation |
| PRs fusionnés | API GitHub | Enregistrements individuels, pas de vue par catégorie |
| Billets résolus | Billets GitHub | Fermés mais pas compilés |
| Publications créées | Dossier `docs/` | Nombre visible, effort invisible |
| Répartition par catégorie | Nulle part | Le développeur sait, personne d'autre ne peut voir |

### Pourquoi c'est important

Le développeur et l'IA livrent la production hebdomadaire d'une équipe en une journée. Mais sans compilation :
- **Aucune preuve** — la productivité est réelle mais non mesurée
- **Aucune tendance** — impossible de comparer les sessions, d'identifier les goulots d'étranglement
- **Aucun rapport** — impossible de démontrer le ROI du développement assisté par IA
- **Aucune planification** — impossible d'estimer les sessions futures à partir des performances passées
- **Aucun héritage** — les sessions successeurs ne peuvent pas apprendre des patterns des prédécesseurs

### La lacune

La publication #19 (Sessions de travail interactives) a codifié **comment** les sessions fonctionnent — patterns de résilience, types de sessions, commits progressifs. Mais elle n'a pas traité **ce qui a été produit** et **combien de temps ça a pris**. La méthodologie pour des sessions productives existe; la mesure de cette productivité n'existait pas.

---

## La solution

Deux outils de compilation avec une structure partagée, cumulables entre sessions.

### Grille de catégories partagée

Le travail de chaque session se répartit dans ces catégories d'interaction :

| Catégorie | Icône | Description | Exemples |
|-----------|-------|-------------|----------|
| **Diagnostic** | 🔍 | Correctifs de bugs, analyse de cause racine, dépannage | Correctif de rendu kramdown, investigation du sélecteur de thème |
| **Conception** | 💡 | Sessions de design, exploration d'architecture, nouvelles idées | Design de préservation des sources Mermaid (v49), méthodologie de compilation |
| **Documentation** | 📝 | Création de publications, fichiers de méthodologie, pages web | Création des publications #17, #18, #19 |
| **Gestion documentaire** | 📋 | Fichiers essentiels, index, NEWS.md, mises à jour de métadonnées | Création de STORIES.md, expansion des fichiers vitaux |
| **Collatéral** | ⚙️ | Billets/boards GitHub, infrastructure, outillage, diagrammes | Mises à jour du board, re-rendu des diagrammes, fermeture de billets |

### Hiérarchie : Todos et tâches

Au sein de chaque catégorie :
- **Todos** (éléments principaux) — les livrables majeurs, en **gras**
- **Tâches** (sous-éléments) — les étapes pour compléter chaque todo, indentées en dessous

Cela reflète la structure TodoWrite utilisée pendant les sessions : un seul todo `in_progress` à la fois, les tâches coulant en dessous.

### Deux fiches de compilation

#### 1. Fiche de compilation des métriques

Pour chaque todo/tâche, capturer ce qui a été **produit** :

| Métrique | Unité | Ce qu'elle mesure |
|----------|-------|-------------------|
| PRs | nombre | Pull requests créés et fusionnés |
| Fichiers | nombre | Fichiers créés ou modifiés |
| Lignes+ | nombre | Lignes de code/contenu ajoutées |
| Lignes− | nombre | Lignes supprimées |
| Billets | nombre | Billets GitHub résolus/fermés |
| Pièges | nombre | Pièges connus documentés |
| Pubs | nombre | Publications créées |
| Métho | nombre | Fichiers de méthodologie créés/mis à jour |
| Évolutions | nombre | Entrées d'évolution de connaissances ajoutées |

#### 2. Feuille de compilation temporelle

Pour chaque todo/tâche, capturer **quand** et **combien de temps** :

| Champ | Format | Ce qu'il capture |
|-------|--------|------------------|
| Début | HH:MM | Quand le travail a commencé (horodatages des commits) |
| Fin | HH:MM | Quand le travail s'est terminé |
| Durée | minutes | Temps de travail actif |
| Type | catégorie | Type d'interaction de session |
| Phase | texte | Quelle phase (hypothèse, création, revue, etc.) |

### Cumul

Les deux fiches utilisent la même grille de catégories. Quand les sessions sont cumulées :

```
Session 2026-02-26 (cette session)
  Diagnostic :     20 min  |  3 PRs, 31 fichiers
  Documentation : 187 min  |  3 pubs, 48 fichiers
  ...
  ─────────────────────────────────────────
  Total session : 337 min  |  25 PRs, 100+ fichiers

Session 2026-02-25 (session précédente)
  Documentation : 240 min  |  2 pubs, 36 fichiers
  Collatéral :    120 min  |  10 PRs, 56 fichiers
  ...
  ─────────────────────────────────────────
  Total session : 480 min  |  15 PRs, 92 fichiers

═══════════════════════════════════════════
Total semaine :  817 min  |  40 PRs, 192+ fichiers
                13,6 hrs  |  ~5,5 pubs
```

---

## Exemple concret : Session 2026-02-26

### Résumé des métriques

**Totaux : 12 todos · 20 PRs · 288 fichiers · +17 974 −6 049 lignes · 6 pubs, 4 métho, 3 pièges**

| Catégorie | Todos | PRs | Fichiers | Lignes+ | Lignes− | Livrables |
|-----------|-------|-----|----------|---------|---------|-----------|
| 🔍 Diagnostic | 1 | 9 | 207 | 9 338 | 5 733 | 3 pièges (#20, #21, #22) |
| 💡 Conception | 4 | 1 | 23 | 3 587 | 23 | 4 méthodologies, v49 |
| 📝 Documentation | 4 | 4 | 43 | 4 358 | 240 | 6 publications (#14–#19) |
| 📋 Gestion doc. | 2 | 2 | 5 | 497 | 0 | STORIES.md, fichiers essentiels |
| ⚙️ Collatéral | — | 4 | 10 | 194 | 53 | 4 PRs collatéraux |
| **Total** | **12** | **20** | **288** | **17 974** | **6 049** | **6 pubs, 4 métho, 3 pièges** |

### Détail des métriques

#### 🔍 Diagnostic (1 todo)

**Totaux : 1 todo · 9 PRs · 207 fichiers · +9 338 −5 733 lignes · 3 pièges**

| # | Todo / Tâche | Billet | PRs | Fichiers | Lignes+ | Lignes− |
|---|--------------|--------|-----|----------|---------|---------|
| **T3** | **Diagnostic diagrammes pages web** | #334 | 9 | 207 | 9 338 | 5 733 |
| | → Remplacer Mermaid par PNG | — | #337 | 30 | 28 | 1 444 |
| | → Diagrammes dual-theme | — | #338 | 62 | 245 | 161 |
| | → Sélecteur de thème + Pub #16 | — | #340 | 23 | 3 354 | 3 |
| | → Re-rendu 28 PNGs | — | #341 | 80 | 3 373 | 5 |
| | → Préservation des sources (v49) | — | #342 | 2 | 2 112 | 202 |
| | → Reconstruction page résumé | — | #343 | 2 | 214 | 2 044 |
| | → Correctif nombre de diagrammes | — | #344 | 4 | 12 | 12 |
| | → Correctif kramdown `<details>` | — | #345 | 4 | 0 | 1 862 |

#### 💡 Conception (4 todos)

**Totaux : 4 todos · 1 PR · 23 fichiers · +3 587 −23 lignes · 4 méthodologies, v49**

| # | Todo / Tâche | Billet | PRs | Fichiers | Lignes+ | Lignes− |
|---|--------------|--------|-----|----------|---------|---------|
| **T4** | **Capacité Web Page Visualization** | #335 | — | *(dans T3)* | | |
| **T10** | **Méthodologie documentaire (méta-métho)** | #355 | #356 | 23 | 3 587 | 23 |
| **T11** | **Publication #20 — Métriques & Temps** | #358 | *(en cours)* | | | |
| **T12** | **Export portrait/paysage** | #357 | *(futur)* | | | |

#### 📝 Documentation (4 todos)

**Totaux : 4 todos · 4 PRs · 43 fichiers · +4 358 −240 lignes · 6 publications**

| # | Todo / Tâche | Billet | PRs | Fichiers | Lignes+ | Lignes− |
|---|--------------|--------|-----|----------|---------|---------|
| **T1** | **Revue documentaire architecture** | #327 | #328 | 14 | 279 | 12 |
| **T2** | **Enrichissement itération 2** | #360 | #333 | 18 | 1 763 | 226 |
| **T5** | **Diagnostic méthodologies** | #361 | #336 | 4 | 417 | 0 |
| **T6** | **Publication #17 Web Production Pipeline** | #347 | #348 | 7 | 1 919 | 2 |

#### 📋 Gestion documentaire (2 todos)

**Totaux : 2 todos · 2 PRs · 5 fichiers · +497 −0 lignes · STORIES.md, fichiers essentiels**

| # | Todo / Tâche | Billet | PRs | Fichiers | Lignes+ | Lignes− |
|---|--------------|--------|-----|----------|---------|---------|
| **T7** | **Vérification méthodologies web** | #350 | #349 | 2 | 150 | 0 |
| **T8** | **Vérification scripts pipeline** | #351 | #352 | 3 | 347 | 0 |

#### ⚙️ Collatéral

**Totaux : 4 PRs · 15 fichiers · +599 −67 lignes · 4 PRs collatéraux, 1 histoire de succès**

| # | Todo / Tâche | PRs | Fichiers | Lignes+ | Lignes− |
|---|--------------|-----|----------|---------|---------|
| | → Correctifs collatéraux T1 | #329–332 | 10 | 194 | 53 |
| **T9** | **Success Story #18** | #354 | 5 | 405 | 14 |

### Résumé temporel

**Totaux : 12 todos · ~10h04 actives · 3 blocs · moy ~50min/todo**

| Catégorie | Todos | Temps total | Moy. par todo |
|-----------|-------|-------------|---------------|
| 🔍 Diagnostic | 1 | ~1h16 | 1h16 |
| 💡 Conception | 4 | ~1h43 | ~26min |
| 📝 Documentation | 4 | ~6h46 | ~1h42 |
| 📋 Gestion doc. | 2 | ~19min | ~10min |
| **Total** | **12** | **~10h04** | **~50min** |

### Détail temporel

#### Bloc : Matin (06:07–08:30) — ~2h23

**Totaux : 2 todos · ~2h23 actives**

| # | Todo | Début | Fin | Durée | Catégorie |
|---|------|-------|-----|-------|-----------|
| **T1** | Revue documentaire architecture | 06:07 | 07:57 | ~1h50 | 📝 Documentation |
| **T2** | Enrichissement itération 2 | 07:57 | ~08:30 | ~33min | 📝 Documentation |

#### Bloc : Après-midi (14:14–19:30) — ~5h16

**Totaux : 3 todos · ~5h16 actives**

| # | Todo | Début | Fin | Durée | Catégorie |
|---|------|-------|-----|-------|-----------|
| **T3** | Diagnostic diagrammes pages web | 14:14 | ~15:30 | ~1h16 | 🔍 Diagnostic |
| **T4** | Capacité Web Page Visualization | 15:30 | 15:33 | ~3min | 💡 Conception |
| **T5** | Diagnostic méthodologies + styling | 15:33 | ~19:30 | ~3h57 | 📝 Documentation |

#### Bloc : Soirée (19:30–22:05) — ~2h35

**Totaux : 7 todos · ~2h35 actives**

| # | Todo | Début | Fin | Durée | Catégorie |
|---|------|-------|-----|-------|-----------|
| **T6** | Publication #17 | 19:30 | ~19:56 | ~26min | 📝 Documentation |
| **T7** | Vérification méthodologies | 19:56 | ~19:56 | ~5min | 📋 Gestion doc. |
| **T8** | Vérification scripts | 19:56 | ~20:10 | ~14min | 📋 Gestion doc. |
| **T9** | Success Story #18 | 20:10 | ~20:25 | ~15min | ⚙️ Collatéral |
| **T10** | Méthodologie documentaire | 20:25 | ~21:40 | ~1h15 | 💡 Conception |
| **T11** | Publication #20 (début) | ~21:40 | ~22:00 | ~20min | 💡 Conception |
| **T12** | Export portrait/paysage (billet seulement) | ~22:00 | ~22:05 | ~5min | 💡 Conception |

*Total : ~10h14 sur 3 blocs, pause ~5h44 entre matin et après-midi*

---

## Intégration méthodologique

### Checklist des métriques (routine post-session)

Exécuter après chaque session pour compiler les métriques :

1. **Statistiques git** — `git log --since="<date>" --stat --oneline | tail -50`
2. **Nombre de PRs** — `git log --since="<date>" --oneline --all | grep -c "Merge"`
3. **Attribution de catégorie** — classifier chaque todo en diagnostic/conception/documentation/gestion-doc/collatéral
4. **Comptage de lignes** — `git diff --stat <start-sha>..<end-sha>`
5. **Statut des billets** — vérifier les billets fermés via `gh_helper.py`
6. **Inventaire des publications** — compter les nouvelles publications, fichiers de méthodologie, entrées d'évolution
7. **Remplir la grille de métriques** — peupler la table catégorie x métriques

### Checklist temporelle (routine post-session)

Exécuter après chaque session pour compiler le temps :

1. **Limites de session** — premier et dernier horodatages de commits
2. **Blocs actifs** — grouper les commits par proximité (< 15 min d'écart = même bloc)
3. **Chronométrage par catégorie** — assigner chaque bloc à une catégorie de travail
4. **Calcul de durée** — sommer les blocs actifs par catégorie
5. **Détection d'inactivité** — écarts > 30 min entre commits = temps non actif
6. **Remplir la grille temporelle** — peupler la table catégorie x temps
7. **Calcul de pourcentage** — part de chaque catégorie dans le temps actif total

### Détection subconsciente

Pendant les sessions de travail, Claude surveille les données dignes de compilation :
- Quand un PR est fusionné → noter les métriques (fichiers, lignes, catégorie)
- Quand un billet est fermé → noter le temps de résolution
- Quand un todo se termine → noter la durée depuis le début
- Quand une session se termine → suggérer la compilation avant `save`

---

## Impact

### Ce que ça permet

| Avant | Après |
|-------|-------|
| « J'ai été productif aujourd'hui » | « 337 min actives, 25 PRs, 3 publications, 9 831 lignes » |
| Aucune comparaison entre sessions | Tables cumulables montrent les tendances hebdomadaires/mensuelles |
| Effort invisible pour les parties prenantes | Preuve structurée de la productivité assistée par IA |
| Aucune donnée de planification | Les données historiques permettent l'estimation des sessions |
| Métriques dispersées dans git | Compilées dans un format standardisé et réutilisable |

### Principes de design

1. **Même grille, deux vues** — métriques et temps partagent la structure de catégories
2. **Todos avant les tâches** — les éléments principaux dirigent la compilation; les tâches sont le détail
3. **Cumulable** — les tables de sessions multiples s'empilent pour l'agrégation
4. **Basé sur les preuves** — toutes les données dérivées de git, PRs, billets (pas des estimations)
5. **Intégré à la routine** — les checklists s'intègrent dans le cycle de vie de session (protocole `save`)
6. **Prêt pour le successeur** — les données compilées sont héritées par la prochaine session via `notes/`

---

## Publications connexes

| # | Publication | Relation |
|---|-------------|---------|
| 19 | [Sessions de travail interactives]({{ '/fr/publications/interactive-work-sessions/' | relative_url }}) | Méthodologie de session qui génère les données compilées ici |
| 8 | [Gestion de session]({{ '/fr/publications/session-management/' | relative_url }}) | Commandes de cycle de vie (wakeup, save) où la compilation s'intègre |
| 3 | [Persistance de session IA]({{ '/fr/publications/ai-session-persistence/' | relative_url }}) | Persistance fondamentale — la compilation est un artefact de persistance |
| 11 | [Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }}) | Les métriques compilées alimentent les récits de validation |
| 4a | [Tableau de bord Knowledge]({{ '/fr/publications/distributed-knowledge-dashboard/' | relative_url }}) | Métriques réseau — même philosophie de compilation au niveau système |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
