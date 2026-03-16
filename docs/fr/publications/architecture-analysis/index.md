---
layout: publication
title: "Analyse d'architecture de Knowledge"
description: "Analyse architecturale complete du systeme Knowledge 2.0 : conception a cinq modules (K_MIND, K_DOCS, K_GITHUB, K_PROJECTS, K_VALIDATION), memoire mind-first, routage par skills, visualiseur web JS statique, modele de securite et architecture de deploiement."
pub_id: "Publication #14"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/architecture-analysis/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "architecture, connaissances, K_MIND, modules, memoire, skills, securite"
---

# Analyse d'architecture de Knowledge
{: #pub-title}

> **Publication parente** : [#0 — Systeme de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Reference core** : [#15 — Diagrammes d'architecture]({{ '/fr/publications/architecture-diagrams/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }})

**Table des matieres**

| | |
|---|---|
| [Resume](#resume) | Vue d'ensemble de l'architecture |
| [Vue d'ensemble](#vue-densemble) | Intelligence d'ingenierie IA multi-module |
| [Architecture des modules](#architecture-des-modules) | Cinq modules specialises |
| [Architecture memoire](#architecture-memoire) | Memoire hierarchisee mind-first |
| [Architecture des skills](#architecture-des-skills) | Routage natif par skills Claude Code |
| [Architecture des qualites](#architecture-des-qualites) | 13 qualites fondamentales et application K2.0 |
| [Cycle de vie des sessions](#cycle-de-vie-des-sessions) | Mecanisme de persistance par scripts K_MIND |
| [Architecture distribuee](#architecture-distribuee) | Reseau de connaissances multi-depot |
| [Architecture de securite](#architecture-de-securite) | Modele proxy, jetons ephemeres, acces proprietaire |
| [Architecture web](#architecture-web) | Visualiseur JS statique, 5 interfaces + mindmap live |
| [Modele de deploiement](#modele-de-deploiement) | Strategie double remote, topologie du reseau |

## Audience ciblee

| Audience | Quoi privilegier |
|----------|-----------------|
| **Administrateurs reseau** | Architecture distribuee, modele de securite, frontieres proxy |
| **Administrateurs systeme** | Modele de deploiement, GitHub Pages, structure des modules |
| **Programmeurs et programmeuses** | Architecture des modules, systeme memoire, cycle de vie, routage par skills |
| **Gestionnaires** | Vue d'ensemble, qualites fondamentales, modele de deploiement |

## Resume

Le systeme Knowledge est une intelligence d'ingenierie IA auto-evolutive qui transforme des sessions de codage IA sans etat en un reseau persistant, distribue et auto-reparateur de conscience. Construit sur des fichiers Markdown, des fichiers JSON de domaine et des scripts Python dans des depots Git — aucun service externe, aucune base de donnees, aucune infrastructure cloud.

Cette publication fournit une analyse architecturale complete de la **conception multi-module Knowledge 2.0** : cinq modules specialises, memoire mind-first avec une grille directive de 264 noeuds, memoire de session hierarchisee, routage natif par skills Claude Code, visualiseur web JavaScript statique, et architecture de securite et de deploiement.

## Vue d'ensemble

Le systeme resout un probleme fondamental : les sessions de codage IA sont sans etat. L'architecture K2.0 y repond par trois mecanismes :

1. **Persistance** : Une grille directive de 264 noeuds (`mind_memory.md`) + memoire de session hierarchisee (`near_memory.json` / `far_memory.json` / `archives/`) + scripts K_MIND transforment des sessions ephemeres en collaboration continue
2. **Modularite** : Cinq modules specialises (K_MIND, K_DOCS, K_GITHUB, K_PROJECTS, K_VALIDATION) possedant chacun leur domaine avec scripts, skills, conventions et suivi de travail propres
3. **Auto-documentation** : Le systeme enregistre son evolution dans les JSON de domaine, publie sa documentation via K_DOCS, et grandit en consommant sa propre production

### Evolution K1.0 → K2.0

| Aspect | K1.0 (Monolithique) | K2.0 (Multi-Module) |
|--------|---------------------|---------------------|
| **Cerveau** | `CLAUDE.md` (3000+ lignes) | `mind_memory.md` (grille 264 noeuds) + JSON de domaine |
| **Connaissances** | `patterns/`, `lessons/` | `conventions.json`, `work.json` par module |
| **Memoire de session** | `notes/` (fichiers plats) | `sessions/` — near + far + archives |
| **Routage** | `routes.json` + `SkillRegistry` | `.claude/skills/` SKILL.md (natif Claude Code) |
| **Web** | Jekyll avec `_config.yml` | `.nojekyll` visualiseur JS statique |

## Architecture des modules

Cinq modules specialises sous `Knowledge/` :

| Module | Role | Composants cles |
|--------|------|-----------------|
| **K_MIND** | Memoire core — mindmap, sessions, scripts | `mind_memory.md`, `session_init.py`, `memory_append.py`, `far_memory_split.py`, `memory_recall.py` |
| **K_DOCS** | Documentation — publications, webcards, visualiseur web | `capture_mindmap.js`, `generate_mindmap_webcard.py`, conventions, methodologie |
| **K_GITHUB** | Integration GitHub — sync, boards, saisie ciblee | `sync_github.py`, alias de board, skill tagged-input |
| **K_PROJECTS** | Gestion de projets — registre, compilation | `compile_projects.py`, donnees projets, skills creer/gerer |
| **K_VALIDATION** | Assurance qualite — integrite, normalisation, workflow | `documentation_validation.py`, 29 points de controle, workflow de taches |

Chaque module possede ses propres `conventions.json`, `work.json` et `documentation.json` — aucun fichier unique ne devient un goulot.

## Architecture memoire

Mind-first : toujours lire `mind_memory.md` en premier (vue d'ensemble), puis les JSON de domaine (detail structure), puis les fichiers de session (historique).

| Niveau | Stockage | Contenu | Charge au demarrage ? |
|--------|----------|---------|------------------------|
| **Mindmap** | `mind_memory.md` | Grille directive de 264 noeuds | Oui (~2,8K tokens) |
| **JSON de domaine** | `.json` par module | 163 references, ~1,8 Mo | Sous-ensemble (~4,5K tokens) |
| **Memoire proche** | `near_memory.json` | Resumes temps reel avec pointeurs | Oui (~8,5K tokens) |
| **Memoire lointaine** | `far_memory.json` | Historique verbatim complet | Minimal |
| **Archives** | `archives/` | Far_memory decoupe par sujet | A la demande |

## Architecture des skills

K2.0 remplace `routes.json` / `SkillRegistry` par des fichiers SKILL.md natifs Claude Code dans `.claude/skills/`. 20+ skills repartis sur 5 modules — chacun autonome avec sa propre chaine de methodologie.

## Architecture des qualites

13 qualites fondamentales avec application K2.0 :

| # | Qualite | Application K2.0 |
|---|---------|-------------------|
| 1 | **Autosuffisant** | Markdown + JSON dans Git, scripts Python purs |
| 2 | **Autonome** | `session_init.py` auto-demarre, `/normalize` auto-repare |
| 3 | **Concordant** | `/normalize`, `/integrity-check` (29 points de controle) |
| 4 | **Concis** | Mindmap 264 noeuds comme vue d'ensemble, filtrage par profondeur |
| 5 | **Interactif** | 5 interfaces + mindmap live MindElixir |
| 6 | **Evolutif** | near_memory grandit chaque tour, work.json accumule |
| 7 | **Distribue** | K_MIND pousse via git, K_GITHUB sync |
| 8 | **Persistant** | Memoire hierarchisee (near/far/archives) |
| 9 | **Recursif** | Les publications K_DOCS decrivent l'architecture K_MIND |
| 10 | **Securitaire** | Delimitation proxy, jetons ephemeres, gh_helper.py |
| 11 | **Resilient** | `/mind-context` rechargement, `memory_recall.py`, archives |
| 12 | **Structure** | 5 modules avec JSON propres, registre K_PROJECTS |
| 13 | **Integre** | K_GITHUB gh_helper.py, Projects v2, alias de board |

## Cycle de vie des sessions

Chaque session : `session_init.py → /mind-context → [travail] → memory_append.py (chaque tour) → far_memory_split.py → git commit & push`. Programmes plutot qu'improvisation — Claude fournit l'intelligence comme arguments a des scripts deterministes.

## Architecture distribuee

Topologie en etoile avec flux bidirectionnel. K_MIND est pousse vers les satellites via git. K_GITHUB `sync_github.py` gere la synchronisation bidirectionnelle (remplace le `harvest` K1.0).

## Architecture de securite

- **Modele proxy** : Operations git restreintes par depot/branche ; Python `urllib` contourne vers l'API
- **Jetons ephemeres** : PAT classique via variable `GH_TOKEN` — meurt avec la session, zero stocke au repos
- **Limite au proprietaire** : Uniquement les depots de l'utilisateur avec acces Claude Code
- **Sur pour fork** : Public et sur a cloner — les forkeurs obtiennent la methodologie, pas les identifiants

## Architecture web

Visualiseur JS statique (`.nojekyll`) avec rendu Markdown + mermaid cote client. 4 themes via media queries CSS. 5 interfaces (navigateur, visualiseur projets, revue sessions, workflow taches, index publications) + mindmap live MindElixir. Templates EN/FR unifies avec `translateStatic()` pour i18n (conv-020).

## Modele de deploiement

Strategie double remote : `knowledge` (packetqc/knowledge) + `origin` (packetqc/K_DOCS). Les deux recoivent les push a chaque unite de travail completee.

---

[**Lire la documentation complete →**]({{ '/fr/publications/architecture-analysis/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
