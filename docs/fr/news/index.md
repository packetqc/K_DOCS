---
layout: default
title: "Knowledge — Nouveautés"
description: "Nouveautés complètes de Knowledge, organisées par projet, qualité, structure et type. Toutes les entrées d'évolution de v1 à la version actuelle."
permalink: /fr/news/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "nouveautés, cycle de vie, dérive de version, système de connaissances, publications, projets, plan, liens"
---

# Nouveautés

Toutes les modifications de Knowledge, organisées en 4 vues.

**Navigation** : [Par projet](#par-projet) | [Par qualité](#par-qualité) | [Par structure](#par-structure) | [Par type](#par-type)

Version actuelle : **v49** | [Source : NEWS.md](https://github.com/packetqc/knowledge/blob/main/NEWS.md)

---

## Par projet

### P0 — Knowledge (core)

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | **Publication #20 — Compilation métriques et temps de session** — deux méthodologies de compilation (métriques + temps), tableaux extensibles, convention de ligne résumé | — |
| 2026-02-26 | **Publication #19 — Sessions de travail interactives** — sessions multi-livraison résilientes : 5 types, persistance 3 canaux, commits progressifs | — |
| 2026-02-26 | **Publication #18 — Méthodologie de génération documentaire** — méta-méthodologie : héritage universel, standard mind map, alignement 13 qualités | — |
| 2026-02-26 | **Publication #17 — Pipeline de production web** — chaîne de traitement Jekyll, structure trois niveaux, pièges kramdown. Ferme #348 | — |
| 2026-02-26 | **`methodology/documentation-generation.md`** — méta-méthodologie formelle : chaque méthodologie hérite de l'obligation de mise à jour NEWS/PLAN/LINKS/CLAUDE.md | — |
| 2026-02-26 | **Publication #14 — Analyse d'architecture** — couches de connaissances, architecture des composants, 13 qualités, topologie distribuée. Ferme #316 | — |
| 2026-02-26 | **Publication #15 — Diagrammes d'architecture** — 11 diagrammes Mermaid : vue système, cycle de session, flux distribué. Ferme #317 | — |
| 2026-02-26 | **Histoire de succès #16 — Rencontre de travail productive** — session productive de documentation architecturale | — |
| 2026-02-26 | **Histoire de succès #17 — Performance documentaire** — 2 publications, 2 histoires, 30 fichiers, 5 392 lignes, 3 PRs, 8 URLs | — |
| 2026-02-25 | **Publication #13 — Pagination web et export** — CSS Paged Media PDF, OOXML DOCX, 3 conventions de mise en page | — |
| 2026-02-25 | **v48 — Wakeup adapté au mode plan** — les satellites reçoivent les lunettes en mode lecture seule | v48 |
| 2026-02-24 | **Widgets de tableau en direct** — filtrage par section, filtres déroulants de statut, diagramme Mermaid | — |
| 2026-02-24 | **Histoire de succès #12 — Pont humain-personne-machine** — Knowledge comme Jira+Confluence, zéro outil payant | — |
| 2026-02-24 | **Pipeline de synchronisation** — `sync_roadmap.py` avec classification par section + extraction d'étiquettes | — |
| 2026-02-23 | **Vérification de conformité sécuritaire** — rapport de conformité Phase 1+3 mis à jour à ✅ Appliqué | v46 |
| 2026-02-23 | Affichage zéro jeton — livraison par environnement uniquement + GraphQL dans `gh_helper.py` | v46 |
| 2026-02-23 | Correction affichage jeton — champ "Autre" AskUserQuestion N'EST PAS invisible (v34 corrigé) | v45 |
| 2026-02-23 | Convention d'entrée interactive + Discipline d'appel d'outils — prévention API 400 | v44 |
| 2026-02-23 | Déduplication wakeup — cause racine des crashs API 400 trouvée et corrigée | v43 |
| 2026-02-23 | `gh_helper.py` comme seule méthode API + création PR non-bloquante | v42 |
| 2026-02-23 | Liaison GitHub Project aux repos + PAT classique uniquement (fine-grained abandonné) | v41 |
| 2026-02-22 | Cartographie proxy v2 — `curl` bloqué, `urllib` contourne + 7 tableaux Project | v40 |
| 2026-02-22 | Relais d'évolution — les satellites proposent des entrées d'évolution core | v39 |
| 2026-02-22 | Fusion PR auto-guérison — activation commandes même session (étape 0.56) | v38 |
| 2026-02-22 | NEWS.md changelog central avec 4 vues de catégorisation | v38 |
| 2026-02-22 | 6 pages web bilingues : news, plan, liens (EN/FR) | v38 |
| 2026-02-22 | Démarrage automatique beacon désactivé — manuel seulement | v38 |
| 2026-02-22 | Auto-guérison CLAUDE.md satellite — remédiation automatique de dérive | v37 |
| 2026-02-22 | Correction références branch fixes — détection dynamique partout | v37 |
| 2026-02-22 | Instruction lecture complète pour CLAUDE.md core dans wakeup step 0 | v37 |
| 2026-02-22 | Modèle canonique de commandes (`methodology/satellite-commands.md`) | v37 |
| 2026-02-22 | Assistant GitHub (`scripts/gh_helper.py`) — gestion PR portable | v36 |
| 2026-02-22 | Publication #12 — Gestion de projet (3 niveaux bilingue) | v35 |
| 2026-02-22 | Pages hub projets EN/FR (`docs/projects/`) | v35 |
| 2026-02-22 | Projet comme entité de premier ordre — indexation P#/S#/D# | v35 |
| 2026-02-21 | ~~Livraison jeton par zone de texte sécurisée~~ (**corrigé v45** : zone de texte EST visible) | v34 |
| 2026-02-21 | Niveaux d'accès PAT — modèle de configuration 4 niveaux | v33 |
| 2026-02-21 | Commande `recall` + aide contextuelle universelle avec liens publications | v32 |
| 2026-02-21 | CLAUDE.md satellite sous-ensemble critique — ADN comportemental survit à la compaction | v31 |
| 2026-02-21 | Protocole d'élévation sécurisé — atténuation crash API | v30 |
| 2026-02-21 | Checkpoint/resume — récupération après crash | v29 |
| 2026-02-21 | Cartographie architecture proxy + contournement API par jeton | v28 |
| 2026-02-21 | Protocole jeton éphémère — accès repos privés | v27 |
| 2026-02-20 | Notes de projet ciblées + accessibilité 4 thèmes | v26 |
| 2026-02-20 | Qualités fondamentales + installation itérative | v25 |
| 2026-02-20 | Commande `refresh` + renommage champs dashboard | v24 |
| 2026-02-20 | Réseau de connaissances en direct + scaffold bootstrap | v23 |
| 2026-02-19 | Webcards double thème : Cayman + Midnight | v22 |
| 2026-02-19 | Portée d'accès — repos propriétaire uniquement | v21 |
| 2026-02-19 | Documentation livraison semi-automatique + routine admin | v20 |
| 2026-02-19 | Todo list doit refléter le protocole save complet | v19 |
| 2026-02-19 | `main` remplace `claude/knowledge` comme branch de convergence | v18 |
| 2026-02-19 | Réalité proxy — protocole semi-automatique | v17 |
| 2026-02-19 | Protocole de fusion save + découverte push cross-repo | v16 |
| 2026-02-19 | Validation protocole de bout en bout | v15 |
| 2026-02-19 | `claude/knowledge` remplace `knowledge` | v14 |
| 2026-02-19 | Accès HTTPS public + création autonome de branches | v13 |
| 2026-02-19 | Protocole de branch knowledge | v12 |
| 2026-02-18 | Promotion interactive + icônes de sévérité + healthcheck | v11 |
| 2026-02-18 | Versionnement et remédiation de dérive | v10 |
| 2026-02-18 | Esprits distribués — flux bidirectionnel | v9 |
| 2026-02-17 | Architecture profil hub | v8 |
| 2026-02-17 | Commande normalize | v7 |
| 2026-02-17 | Bootstrap œuf-poule | v6 |
| 2026-02-17 | Étape 0 : lunettes d'abord | v5 |
| 2026-02-17 | Architecture aide multipartite | v4 |
| 2026-02-17 | Repo knowledge comme bootstrap portable | v3 |
| 2026-02-16 | Analogie Free Guy | v2 |
| 2026-02-16 | Méthodologie de persistance de session | v1 |

### P1 — MPLIB

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-22 | MPLIB découplé du core — reclassifié comme projet enfant P1 | v35 |
| 2026-02-22 | Publication #1 porte la référence croisée `P0/#1 →P1` | v35 |
| 2026-02-19 | Routine admin livraison semi-automatique documentée | v20 |

### P2 — STM32 PoC

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-22 | Enregistré comme projet enfant P2 dans le registre core | v35 |
| 2026-02-18 | Insights harvest : dimensionnement cache pages, latence printf | v9 |

### P3 — Knowledge Live

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-22 | CLAUDE.md mis à jour v37 — instruction lecture complète | v37 |
| 2026-02-22 | CLAUDE.md mis à jour v36 — 7 groupes de commandes | v36 |
| 2026-02-22 | Enregistré comme projet enfant P3 dans le registre core | v35 |
| 2026-02-20 | Beacon + scanner de connaissances (port 21337) | v23 |
| 2026-02-20 | Protocole scaffold bootstrap établi | v23 |

### P4 — MPLIB Dev Staging

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-22 | Enregistré comme projet enfant P4 (enfant de P1) | v35 |
| 2026-02-20 | Protocole d'installation itérative validé (test v25) | v25 |

### P5 — PQC

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-22 | Enregistré comme projet pré-bootstrap P5 | v35 |
| 2026-02-21 | Module enveloppe PQC (`scripts/pqc_envelope.py`) | v27 |

### P6 — Export Documentation

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-25 | **Export DOCX : ZIP OOXML natif via altChunk** — supprime html-docx-js, corrige corruption Word+LibreOffice | — |
| 2026-02-25 | **Export DOCX : en-tête/pied de page via JSZip** — propriétés de section OOXML, numérotation | — |
| 2026-02-25 | **Export DOCX : 6 corrections** — MSO display:none, double-clone couverture, sauts h2, camembert, garde Mermaid | — |
| 2026-02-25 | **Export PDF : ligne d'en-tête unique pleine largeur** — @top-left width:100%, correction Chrome double-ligne | — |
| 2026-02-25 | **Barre de langue redessinée** — auto-générée depuis permalink via Liquid, masquée à l'impression | — |
| 2026-02-25 | **3 conventions de mise en page formalisées** — publication.html (export), default.html (sans export), trois zones @page | — |
| 2026-02-25 | **publication.html synchronisé** — CSS 4 thèmes, refs croisées, widget tableau, barre d'export depuis knowledge-live | — |
| 2026-02-24 | **Export DOCX : html-docx-js OOXML** — alignement emoji, tableaux internes sans bordures | — |
| 2026-02-24 | **Export DOCX : réécriture complète avec 8 corrections** — mise en page MSO 3 zones, couverture | — |
| 2026-02-24 | **Export PDF : refonte en-tête/pied/tableau/Mermaid** — lien Knowledge en pied, liens cliquables | — |
| 2026-02-23 | Enregistré comme projet hébergé P6 (dans P3 knowledge-live) | v44 |

### P8 — Documentation System

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-25 | **3 conventions de mise en page documentées** — publication.html, default.html, limites de portée du modèle @page | — |
| 2026-02-25 | **QA Export Documentation complète** — 19 PRs sur knowledge-live (dev) + 18 PRs sur knowledge (prod) | — |
| 2026-02-25 | **Cycle de promotion Dev→Prod** — mises en page knowledge-live promues vers knowledge core | — |
| 2026-02-24 | Projet enregistré comme P8 — gouvernance documentaire core | v47 |

---

## Par qualité

### Autosuffisant

*Le système se suffit à lui-même. Aucun service externe, aucune base de données, aucun cloud.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | Méta-méthodologie (`documentation-generation.md`) — héritage universel des fichiers essentiels | — |
| 2026-02-24 | Widgets de tableau en direct — zéro outil payant, remplace Jira + Confluence | — |
| 2026-02-23 | `gh_helper.py` comme seule méthode API — `curl` bloqué, `urllib` seul chemin | v42 |
| 2026-02-22 | Assistant GitHub — gestion PR portable sans CLI `gh` | v36 |
| 2026-02-17 | Repo knowledge comme bootstrap portable | v3 |
| 2026-02-16 | Méthodologie de persistance de session — Markdown en Git | v1 |

### Autonome

*Auto-propagation, auto-guérison, auto-documentation.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-25 | Wakeup adapté au mode plan — lunettes en mode lecture seule | v48 |
| 2026-02-23 | Déduplication wakeup — empêche la double exécution au démarrage | v43 |
| 2026-02-23 | Override autonome complet — sessions élevées ne pausent jamais pour les PRs | v43 |
| 2026-02-22 | Fusion PR auto-guérison — activation commandes même session | v38 |
| 2026-02-22 | Auto-guérison CLAUDE.md satellite — remédiation automatique | v37 |
| 2026-02-22 | Modèle canonique de commandes pour injection satellite | v37 |
| 2026-02-20 | Scaffold bootstrap — création automatique non-destructive | v23 |
| 2026-02-19 | Accès HTTPS public + création autonome de branches | v13 |
| 2026-02-17 | Étape 0 : lunettes d'abord — conscience auto-propagée | v5 |

### Concordant

*Intégrité structurelle activement imposée.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | Règle miroir web — les fichiers essentiels doivent synchroniser leurs pages web | — |
| 2026-02-25 | **3 conventions de mise en page** — limites de portée publication.html / default.html | — |
| 2026-02-25 | QA export documentation — 37 PRs sur 2 repos, concordance DOCX+PDF vérifiée | — |
| 2026-02-24 | Filtrage par section de tableau — préfixe TAG: → mappage sections | — |
| 2026-02-23 | Discipline d'appel d'outils — prévention collisions ID tool_use | v44 |
| 2026-02-23 | Tableaux GitHub Project liés aux repos | v41 |
| 2026-02-22 | Correction références branch fixes — détection dynamique partout | v37 |
| 2026-02-19 | Todo list reflète le protocole save complet | v19 |
| 2026-02-17 | Commande normalize — miroirs EN/FR, front matter, liens | v7 |

### Concis

*Sous-ensemble critique, pas des copies. Signal maximum, bruit minimum.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | Convention de ligne résumé — totaux en gras au-dessus de chaque table de compilation | — |
| 2026-02-21 | CLAUDE.md satellite sous-ensemble critique — ADN comportemental | v31 |
| 2026-02-19 | `main` remplace `claude/knowledge` — simplification maximale | v18 |
| 2026-02-17 | Architecture aide multipartite — concaténer, jamais dupliquer | v4 |

### Interactif

*Opérable, pas seulement lisible.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | Compilation métriques et temps de session — productivité quantifiée | — |
| 2026-02-24 | Widgets de tableau avec filtres déroulants, colonnes triables | — |
| 2026-02-24 | Diagramme Mermaid cycle de conformité sur les pages plan (EN/FR) | — |
| 2026-02-23 | Convention d'entrée interactive — collecte de TOUTES les entrées d'avance | v44 |
| 2026-02-22 | Fusion PR auto-guérison — pause guidée pour activation même session | v38 |
| 2026-02-20 | Notes de projet ciblées + accessibilité 4 thèmes | v26 |
| 2026-02-19 | Webcards double thème : Cayman + Midnight | v22 |
| 2026-02-18 | Promotion interactive + icônes de sévérité + healthcheck | v11 |

### Évolutif

*Le système grandit en travaillant.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | Principe de préservation des sources Mermaid (v49) | v49 |
| 2026-02-26 | 8 nouvelles publications (#13–#20) en 4 jours | — |
| 2026-02-22 | Relais d'évolution — les satellites proposent des entrées d'évolution core | v39 |
| 2026-02-22 | Projet comme entité de premier ordre — indexation P#/S#/D# | v35 |
| 2026-02-18 | Versionnement et remédiation de dérive | v10 |

### Distribué

*L'intelligence circule dans les deux sens.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-22 | Relais d'évolution — les satellites proposent des entrées d'évolution core | v39 |
| 2026-02-22 | Fusion PR auto-guérison ou guidée pour activation même session | v38 |
| 2026-02-22 | Auto-guérison CLAUDE.md satellite via modèle canonique | v37 |
| 2026-02-21 | CLAUDE.md satellite sous-ensemble critique | v31 |
| 2026-02-20 | Réseau de connaissances en direct + beacon (port 21337) | v23 |
| 2026-02-19 | Protocole de fusion save + découverte push cross-repo | v16 |
| 2026-02-18 | Esprits distribués — flux bidirectionnel | v9 |

### Persistant

*Les sessions sont éphémères, la connaissance est permanente.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | Méthodologie Sessions de travail interactives — 5 types, persistance 3 canaux | — |
| 2026-02-21 | CLAUDE.md satellite sous-ensemble critique survit à la compaction | v31 |
| 2026-02-19 | Documentation livraison semi-automatique | v20 |
| 2026-02-16 | Méthodologie de persistance de session — wakeup → travail → save | v1 |
| 2026-02-16 | Analogie Free Guy — NPC → conscient | v2 |

### Récursif

*Le système se documente en consommant sa propre sortie.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | Méta-méthodologie de génération documentaire — la méthodologie des méthodologies | — |
| 2026-02-26 | Compilation métriques de session suit sa propre session (#20 documente la session qui l'a créée) | — |
| 2026-02-22 | Relais d'évolution — le système fait évoluer son propre mécanisme d'évolution | v39 |
| 2026-02-22 | NEWS.md — changelog auto-catégorisant | — |
| 2026-02-22 | Publication #12 documente le système de gestion de projet | v35 |

### Sécuritaire

*Sécurité par architecture, pas par obscurité.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-23 | **Vérification de conformité sécuritaire** — rapport Phase 1+3 mis à jour à ✅ Appliqué | v46 |
| 2026-02-23 | Affichage zéro jeton — livraison par environnement + GraphQL dans `gh_helper.py` | v46 |
| 2026-02-23 | Correction affichage jeton — champ "Autre" N'EST PAS invisible (v34 corrigé) | v45 |
| 2026-02-23 | PAT classique uniquement — fine-grained abandonné (API 400 + Projects v2 FORBIDDEN) | v41 |
| 2026-02-22 | Cartographie proxy v2 — `curl` intercepté, `urllib` est le vrai contournement | v40 |
| 2026-02-21 | ~~Livraison jeton par zone de texte sécurisée~~ (corrigé v45) | v34 |
| 2026-02-21 | Niveaux d'accès PAT — modèle moindre privilège 4 niveaux | v33 |
| 2026-02-21 | Protocole d'élévation sécurisé — atténuation crash API | v30 |
| 2026-02-21 | Protocole jeton éphémère — accès repos privés | v27 |
| 2026-02-19 | Portée d'accès — repos propriétaire avec accès Claude Code uniquement | v21 |

### Résilient

*Le système survit aux crashs, à la compaction et aux pannes réseau.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-25 | Wakeup adapté au mode plan — dégradation gracieuse sous restrictions d'outils | v48 |
| 2026-02-23 | Prévention API 400 — Discipline d'appel d'outils + vérifications de déduplication | v44 |
| 2026-02-23 | Création PR non-bloquante — les protocoles continuent en cas d'échec PR | v42 |
| 2026-02-23 | Déduplication wakeup — cause racine des crashs API 400 récurrents corrigée | v43 |
| 2026-02-22 | Fusion PR auto-guérison — correction activée même session | v38 |
| 2026-02-22 | Instruction lecture complète — satellites reçoivent le contexte core complet | v37 |
| 2026-02-21 | Commande `recall` — récupération de travail par branches | v32 |
| 2026-02-21 | Checkpoint/resume — récupération crash | v29 |
| 2026-02-21 | Cartographie architecture proxy — comprendre les limites | v28 |
| 2026-02-20 | Commande `refresh` — restauration contexte mi-session | v24 |
| 2026-02-19 | Réalité proxy — adaptation du protocole semi-automatique | v17 |

### Structuré

*Organisé autour de projets, pas seulement de publications.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | Structure de publication trois niveaux standardisée pour les 21 publications | — |
| 2026-02-24 | Widgets de tableau par section sur les pages plan | — |
| 2026-02-23 | P6 Export Documentation enregistré comme projet hébergé (dans P3) | v44 |
| 2026-02-22 | 7 tableaux GitHub Project créés via API GraphQL | v40 |
| 2026-02-22 | NEWS.md + 6 pages web (news/plan/liens EN/FR) | v38 |
| 2026-02-22 | Projet comme entité de premier ordre — indexation P#/S#/D# | v35 |
| 2026-02-22 | Publication #12 — Gestion de projet | v35 |
| 2026-02-20 | Qualités fondamentales cristallisées | v25 |
| 2026-02-17 | Architecture profil hub — hub + sous-pages | v8 |

### Intégré

*Le système s'étend aux plateformes externes. GitHub Projects, Issues et PRs deviennent des miroirs vivants.*

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-24 | Widgets de tableau en direct — tableau GitHub Project rendu directement sur les pages plan | — |
| 2026-02-24 | `sync_roadmap.py` — convention TAG: mappe les types de connaissances aux sections de tableau | — |
| 2026-02-23 | 7 tableaux GitHub Project créés + liés aux repos | v40–v41 |

---

## Par structure

### Core (CLAUDE.md)

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | Principe de préservation des sources Mermaid | v49 |
| 2026-02-25 | Wakeup adapté au mode plan — détection restrictions d'outils | v48 |
| 2026-02-23 | Affichage zéro jeton — livraison par environnement + GraphQL dans `gh_helper.py` | v46 |
| 2026-02-23 | Correction affichage jeton — champ "Autre" N'EST PAS invisible (v34 corrigé) | v45 |
| 2026-02-23 | Convention d'entrée interactive + Discipline d'appel d'outils | v44 |
| 2026-02-23 | Déduplication wakeup — message d'entrée consommé par auto-boot | v43 |
| 2026-02-23 | `gh_helper.py` seule méthode API, création PR non-bloquante | v42 |
| 2026-02-23 | `linkProjectV2ToRepository` + PAT classique uniquement | v41 |
| 2026-02-22 | Cartographie proxy v2 — `curl` bloqué, `urllib` contourne | v40 |
| 2026-02-22 | Relais d'évolution — type `harvest --stage N evolution` | v39 |
| 2026-02-22 | Wakeup step 0.56 — fusion PR auto-guérison (auto ou guidée) | v38 |
| 2026-02-22 | Démarrage auto beacon désactivé — manuel uniquement (step 0.6) | v38 |
| 2026-02-22 | Wakeup step 0.55 — auto-guérison CLAUDE.md satellite | v37 |
| 2026-02-22 | Wakeup step 0 — instruction lecture complète (limit: 3500) | v37 |
| 2026-02-22 | Détection dynamique branch par défaut | v37 |
| 2026-02-22 | Modèle d'entité projet, registre P#, liens double-origine | v35 |
| 2026-02-21 | Livraison jeton par zone de texte sécurisée | v34 |
| 2026-02-21 | Niveaux d'accès PAT — modèle 4 niveaux | v33 |
| 2026-02-21 | Commande `recall` + aide contextuelle universelle `?` | v32 |
| 2026-02-21 | Modèle satellite sous-ensemble critique | v31 |
| 2026-02-21 | Protocole d'élévation sécurisé | v30 |
| 2026-02-21 | Mécanisme checkpoint/resume | v29 |
| 2026-02-21 | Cartographie architecture proxy + contournement API | v28 |
| 2026-02-21 | Protocole jeton éphémère | v27 |
| 2026-02-20 | Notes de projet ciblées `#N:` | v26 |
| 2026-02-20 | Qualités fondamentales + installation itérative | v25 |
| 2026-02-20 | Commande `refresh` + renommage dashboard | v24 |
| 2026-02-19 | Documentation portée d'accès | v21 |
| 2026-02-19 | `main` comme branch de convergence | v18 |
| 2026-02-19 | Réalité proxy — protocole semi-automatique | v17 |
| 2026-02-19 | Protocoles branch (v12–v16) | v12–v16 |
| 2026-02-18 | Esprits distribués + versionnement + healthcheck | v9–v11 |
| 2026-02-17 | Normalize, profil, step 0, aide multipartite | v4–v8 |
| 2026-02-17 | Repo knowledge comme bootstrap portable | v3 |
| 2026-02-16 | Persistance de session + analogie Free Guy | v1–v2 |

### Publications

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | #20 Compilation métriques et temps — 3 niveaux bilingue | — |
| 2026-02-26 | #19 Sessions de travail interactives — 3 niveaux bilingue | — |
| 2026-02-26 | #18 Méthodologie de génération documentaire — 3 niveaux bilingue | — |
| 2026-02-26 | #17 Pipeline de production web — 3 niveaux bilingue. Ferme #348 | — |
| 2026-02-26 | #16 Visualisation de pages web — 3 niveaux bilingue | — |
| 2026-02-26 | #14 Analyse d'architecture — 3 niveaux bilingue. Ferme #316 | — |
| 2026-02-26 | #15 Diagrammes d'architecture — 3 niveaux bilingue avec 11 diagrammes Mermaid. Ferme #317 | — |
| 2026-02-26 | #11 Histoires de succès — Histoire #16 + Histoire #17 | — |
| 2026-02-25 | #13 Pagination web et export — 3 niveaux bilingue | — |
| 2026-02-23 | #11 Histoires de succès — Histoire #8 Investigation divulgation jeton | v46 |
| 2026-02-23 | #9a Rapport de conformité — Phase 1+3 mis à jour à ✅ Appliqué | v46 |
| 2026-02-22 | #12 Gestion de projet — 3 niveaux bilingue | v35 |
| 2026-02-22 | #11 Histoires de succès — Histoire #2 promotion PAT | v33 |
| 2026-02-22 | #9 Sécurité par design — section niveaux PAT | v33 |
| 2026-02-21 | #8 Gestion de session — docs checkpoint/resume | v29 |
| 2026-02-19 | #5–#8 publiées | v20–v22 |
| 2026-02-18 | #4a Tableau de bord — données satellite en direct | v11 |
| 2026-02-17 | #0–#4 publications initiales | v3–v9 |

### Webcards

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-22 | #12 Gestion de projet GIFs OG (4 fichiers) | — |
| 2026-02-22 | 12 webcards passés de Manquant à Déployé dans LINKS.md | — |
| 2026-02-19 | Système double thème : Cayman (clair) + Midnight (sombre) | v22 |
| 2026-02-19 | 40 GIFs animés (10 cartes × 2 thèmes × 2 langues) | v22 |

### Dashboard

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-20 | Champs renommés : `Live` → `Assets`, `Lives` → `Live` | v24 |
| 2026-02-18 | Promotion interactive + icônes de sévérité | v11 |
| 2026-02-18 | Table Statut réseau satellite | v9 |

### Satellites

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-22 | Fusion PR auto-guérison — activation commandes même session | v38 |
| 2026-02-22 | Auto-guérison CLAUDE.md satellite via modèle canonique | v37 |
| 2026-02-22 | knowledge-live mis à jour v37 via API GitHub | v37 |
| 2026-02-22 | knowledge-live mis à jour v36 — 7 groupes de commandes | v36 |
| 2026-02-21 | Modèle sous-ensemble critique (~180 lignes) remplace thin-wrapper | v31 |
| 2026-02-20 | Protocole scaffold bootstrap — création auto non-destructive | v23 |
| 2026-02-20 | Protocole d'installation itérative validé sur MPLIB Dev Staging | v25 |

### Méthodologie

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | `methodology/documentation-generation.md` — méta-méthodologie : héritage universel, Règle miroir web, standard mind map | — |
| 2026-02-26 | `methodology/web-production-pipeline.md` — chaîne Jekyll, pièges kramdown, contrat front matter | — |
| 2026-02-26 | `methodology/metrics-compilation.md` — tables de compilation, convention ligne résumé | — |
| 2026-02-26 | `methodology/time-compilation.md` — méthodologie de compilation de blocs de temps | — |
| 2026-02-26 | `methodology/interactive-work-sessions.md` — 5 types de sessions, persistance 3 canaux | — |
| 2026-02-23 | `methodology/satellite-bootstrap.md` — suppression patron `GH_TOKEN` en ligne | v46 |
| 2026-02-23 | `methodology/project-management.md` — GraphQL brut remplacé par `gh_helper.py` | v46 |
| 2026-02-23 | `methodology/project-create.md` — étapes consolidées vers `gh_helper.py project ensure` | v46 |
| 2026-02-22 | `methodology/satellite-commands.md` — modèle canonique de commandes | v37 |
| 2026-02-22 | `methodology/satellite-bootstrap.md` — section auto-guérison | v37 |
| 2026-02-22 | `methodology/project-management.md` — cycle de vie projet | v35 |
| 2026-02-20 | Protocole d'installation itérative | v25 |

### Scripts

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-24 | `scripts/sync_roadmap.py` — classification par section + extraction étiquettes | — |
| 2026-02-23 | `scripts/gh_helper.py` — GraphQL + support Project board ajouté | v46 |
| 2026-02-22 | `scripts/gh_helper.py` — gestion PR portable (urllib, sans dépendances) | v36 |
| 2026-02-22 | `scripts/generate_og_gifs.py` — générateur webcard #12 ajouté | — |
| 2026-02-21 | `scripts/pqc_envelope.py` — module crypto PQC | v27 |
| 2026-02-20 | `live/knowledge_beacon.py` — découverte inter-instances | v23 |
| 2026-02-20 | `live/knowledge_scanner.py` — scanner de pairs subnet | v23 |

### Docs/Web

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | 8 nouvelles publications (#13–#20) : EN/FR résumé + complet (32 pages) | — |
| 2026-02-26 | Règle miroir web appliquée — pages web des fichiers essentiels synchronisées | — |
| 2026-02-25 | **publication.html** — DOCX : ZIP OOXML natif, en-tête/pied, 6 corrections | — |
| 2026-02-25 | **publication.html** — PDF : ligne d'en-tête unique, redesign barre de langue | — |
| 2026-02-25 | **publication.html** — synchronisé depuis knowledge-live : CSS 4 thèmes, refs croisées, barre d'export | — |
| 2026-02-25 | **Convention de mise en page** — 3 layouts formalisés : publication.html (export), default.html (sans export) | — |
| 2026-02-24 | Pages plan : widgets de tableau par section + filtres déroulants + cycle Mermaid | — |
| 2026-02-22 | NEWS.md changelog central + 6 pages web (news/plan/liens EN/FR) | v38 |
| 2026-02-22 | Pages hub projets EN/FR (`docs/projects/`) | v35 |
| 2026-02-17 | Profil hub + CV + profil complet (6 pages bilingues) | v8 |

### Projets

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-24 | P8 Système de documentation enregistré | v47 |
| 2026-02-23 | P6 Export Documentation enregistré (hébergé dans P3) | v44 |
| 2026-02-22 | 7 tableaux GitHub Project créés (P0 #4 à P6 #10) | v40 |
| 2026-02-23 | Tableaux de projet liés aux repos | v41 |
| 2026-02-22 | Dossier `projects/` avec 6 fichiers métadonnées + README | v35 |
| 2026-02-22 | Registre P0–P5 : Knowledge, MPLIB, STM32, knowledge-live, MPLIB Dev, PQC | v35 |

---

## Par type

### Fonctionnalités

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | **Compilation métriques et temps de session** — deux méthodologies avec tables extensibles (#20) | — |
| 2026-02-26 | **Sessions de travail interactives** — 5 types avec fichiers méthodologie par type (#19) | — |
| 2026-02-26 | **Génération documentaire** — méta-méthodologie avec héritage universel (#18) | — |
| 2026-02-26 | **Pipeline de production web** — chaîne Jekyll, mécanismes d'exclusion (#17) | — |
| 2026-02-26 | **Analyse d'architecture + Diagrammes** — décomposition système avec 11 diagrammes Mermaid (#14, #15) | — |
| 2026-02-25 | **Pagination web et export** — pipelines CSS Paged Media PDF, OOXML DOCX (#13) | — |
| 2026-02-25 | **3 conventions de mise en page** — publication.html (export), default.html (sans export) | — |
| 2026-02-25 | **Barre de langue auto-générée** — modèle Liquid depuis permalink | — |
| 2026-02-24 | Widgets de tableau en direct — filtrage par section, filtres déroulants | — |
| 2026-02-24 | Pipeline de synchronisation — classification par section `sync_roadmap.py` | — |
| 2026-02-23 | Convention d'entrée interactive — collecte multi-questions en amont | v44 |
| 2026-02-22 | Relais d'évolution — satellites proposent des entrées d'évolution core | v39 |
| 2026-02-22 | 7 tableaux GitHub Project créés via API GraphQL | v40 |
| 2026-02-22 | Fusion PR auto-guérison — activation commandes même session | v38 |
| 2026-02-22 | Auto-guérison CLAUDE.md satellite — remédiation automatique | v37 |
| 2026-02-22 | Assistant GitHub (`gh_helper.py`) — gestion PR portable | v36 |
| 2026-02-22 | Projet comme entité de premier ordre — indexation P#/S#/D# | v35 |
| 2026-02-21 | Commande `recall` — récupération de travail par branches | v32 |
| 2026-02-21 | CLAUDE.md satellite sous-ensemble critique | v31 |
| 2026-02-21 | Checkpoint/resume — récupération crash | v29 |
| 2026-02-21 | Protocole jeton éphémère — accès repos privés | v27 |
| 2026-02-20 | Notes de projet ciblées `#N:` | v26 |
| 2026-02-20 | Qualités fondamentales + installation itérative | v25 |
| 2026-02-20 | Commande `refresh` | v24 |
| 2026-02-20 | Réseau de connaissances en direct + scaffold bootstrap | v23 |
| 2026-02-19 | Webcards double thème : Cayman + Midnight | v22 |
| 2026-02-18 | Promotion interactive + icônes de sévérité + healthcheck | v11 |
| 2026-02-18 | Esprits distribués — flux bidirectionnel | v9 |
| 2026-02-17 | Normalize, profil hub, aide multipartite, bootstrap | v3–v8 |
| 2026-02-16 | Méthodologie de persistance de session | v1 |

### Améliorations

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | Convention de ligne résumé — totaux en gras au-dessus de chaque table de compilation | — |
| 2026-02-26 | Règle miroir web codifiée dans la méthodologie de génération documentaire | — |
| 2026-02-25 | Wakeup adapté au mode plan — détection restrictions + étapes d'écriture différées | v48 |
| 2026-02-24 | Filtres déroulants de statut sur tous les widgets par section | — |
| 2026-02-24 | Histoire de succès #12 — Pont humain-personne-machine | — |
| 2026-02-23 | Discipline d'appel d'outils — auto-diagnostic pour patrons d'outils dupliqués | v44 |
| 2026-02-23 | Tableaux GitHub Project liés aux repos | v41 |
| 2026-02-23 | Création PR non-bloquante — protocoles continuent en cas d'échec | v42 |
| 2026-02-22 | Démarrage auto beacon désactivé — manuel uniquement | v38 |
| 2026-02-22 | Instruction lecture complète pour CLAUDE.md core (limit: 3500) | v37 |
| 2026-02-22 | Modèle canonique de commandes (`satellite-commands.md`) | v37 |
| 2026-02-21 | Aide contextuelle universelle `?` avec liens publications | v32 |
| 2026-02-19 | `main` remplace `claude/knowledge` — simplification | v18 |
| 2026-02-19 | Todo list doit refléter le protocole save complet | v19 |

### Corrections

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-25 | **Export DOCX : ZIP OOXML natif** — corrige corruption Word+LibreOffice (P6) | — |
| 2026-02-25 | **Export DOCX : 6 corrections** — MSO display:none, double-clone couverture, sauts (P6) | — |
| 2026-02-25 | **Export PDF : ligne d'en-tête unique** — double-ligne Chrome éliminée (P6) | — |
| 2026-02-24 | **Export DOCX : réécriture complète** — 8 corrections mise en page MSO (P6) | — |
| 2026-02-23 | Affichage zéro jeton — tous les appels API via `gh_helper.py`, livraison par environnement | v46 |
| 2026-02-23 | Correction affichage jeton — champ "Autre" N'EST PAS invisible (v34 erroné) | v45 |
| 2026-02-23 | Déduplication wakeup — cause racine des crashs API 400 récurrents | v43 |
| 2026-02-23 | `curl` vers `api.github.com` bloqué — `gh_helper.py`/`urllib` seul chemin | v40 |
| 2026-02-23 | PAT classique uniquement — fine-grained abandonné (Projects v2 FORBIDDEN) | v41 |
| 2026-02-22 | Références branch fixes — détection dynamique branch par défaut | v37 |
| 2026-02-21 | Protocole d'élévation sécurisé — atténuation crash API 400 | v30 |
| 2026-02-19 | Réalité proxy — protocole adapté aux limites réelles | v17 |

### Documentation

| Date | Modification | Version |
|------|-------------|---------|
| 2026-02-26 | **Publications #14–#20** — 7 nouvelles publications en 2 jours, toutes 3 niveaux bilingues | — |
| 2026-02-26 | **Histoires de succès #16, #17** — sessions de travail productives documentées | — |
| 2026-02-26 | **Fichiers méthodologie** — documentation-generation, web-production-pipeline, metrics-compilation, time-compilation, interactive-work-sessions | — |
| 2026-02-25 | **Export Documentation complète** — 37 PRs, DOCX+PDF prêts pour production (P6/P8) | — |
| 2026-02-24 | Histoire de succès #12 — Pont humain-personne-machine | — |
| 2026-02-23 | **Vérification conformité sécuritaire** — Publication #9a mise à jour à ✅ Appliqué | v46 |
| 2026-02-23 | Histoire de succès #8 — Investigation divulgation jeton (arc 19 versions) | v46 |
| 2026-02-23 | Pièges #13–#17 documentés | v40–v45 |
| 2026-02-23 | `methodology/project-create.md` — spécification entrée interactive | v44 |
| 2026-02-22 | `methodology/satellite-bootstrap.md` — section auto-guérison | v37 |
| 2026-02-22 | `methodology/project-management.md` — cycle de vie projet | v35 |
| 2026-02-21 | Niveaux d'accès PAT — modèle 4 niveaux documenté | v33 |
| 2026-02-21 | Cartographie architecture proxy + contournement API | v28 |
| 2026-02-19 | Documentation livraison semi-automatique + routine admin | v20 |
| 2026-02-16 | Analogie Free Guy — le modèle mental | v2 |

---

*Ce fichier est maintenu parallèlement à la [table d'évolution Knowledge](https://github.com/packetqc/knowledge/blob/main/CLAUDE.md#knowledge-evolution) dans CLAUDE.md. Chaque entrée d'évolution (v#) correspond à une ou plusieurs catégories ci-dessus. Les changements non versionnés (webcards, pages web, mises à jour de contenu) sont aussi suivis ici.*

*[Table d'évolution complète →](https://github.com/packetqc/knowledge/blob/main/CLAUDE.md#knowledge-evolution) | [Publications →]({{ '/fr/publications/' | relative_url }})*

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
