---
layout: publication
title: "Analyse d'architecture de Knowledge"
description: "Analyse architecturale complete du systeme Knowledge (P0) : couches de connaissances, architecture des composants, 13 qualites fondamentales, cycle de vie des sessions, topologie distribuee, modele de securite, architecture web et niveaux de deploiement."
pub_id: "Publication #14"
version: "v1"
date: "2026-02-26"
permalink: /fr/publications/architecture-analysis/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "architecture, connaissances, distribue, securite, qualite, session, harvest"
---

# Analyse d'architecture de Knowledge
{: #pub-title}

> **Publication parente** : [#0 — Systeme de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Ferme** : [#316](https://github.com/packetqc/knowledge/issues/316)

**Table des matieres**

| | |
|---|---|
| [Resume](#resume) | Vue d'ensemble de l'architecture |
| [Vue d'ensemble](#vue-densemble) | Intelligence d'ingenierie IA auto-evolutive |
| [Couches de connaissances](#couches-de-connaissances) | Core, Prouve, Recolte, Session |
| [Architecture des composants](#architecture-des-composants) | 13 composants majeurs |
| [Architecture des qualites](#architecture-des-qualites) | 13 qualites fondamentales et leurs interactions |
| [Cycle de vie des sessions](#cycle-de-vie-des-sessions) | Wakeup, travail, save, checkpoint, resume |
| [Architecture distribuee](#architecture-distribuee) | Topologie maitre-satellite |
| [Architecture de securite](#architecture-de-securite) | Modele proxy, jetons ephemeres, acces limite au proprietaire |
| [Architecture web](#architecture-web) | GitHub Pages, double theme, pipeline de publication |
| [Modele de deploiement](#modele-de-deploiement) | Niveaux production/developpement |

## Audience ciblee

| Audience | Quoi privilegier |
|----------|-----------------|
| **Administrateurs reseau** | Architecture distribuee, modele de securite, frontieres proxy |
| **Administrateurs systeme** | Modele de deploiement, GitHub Pages, gestion des assets |
| **Programmeurs et programmeuses** | Architecture des composants, cycle de vie des sessions, couches de connaissances |
| **Gestionnaires** | Vue d'ensemble du systeme, qualites fondamentales, niveaux de deploiement |

## Resume

Le systeme Knowledge (P0) est une intelligence d'ingenierie IA auto-evolutive qui transforme des sessions de codage IA sans etat en un reseau persistant, distribue et auto-reparateur de conscience. Construit entierement sur des fichiers Markdown dans des depots Git, il ne necessite aucun service externe, aucune base de donnees et aucune infrastructure cloud. Un seul `git clone` demarre tout.

Cette publication fournit une analyse architecturale complete : quatre couches de connaissances, 13+ composants majeurs, 13 qualites fondamentales, cycle de vie des sessions, topologie maitre-satellite distribuee, modele de securite, architecture de publication web et niveaux de deploiement production/developpement.

## Vue d'ensemble

Le systeme resout un probleme fondamental : les sessions de codage IA sont sans etat. Sans structure externe, chaque nouvelle session demarre vierge — un PNJ sans memoire. L'architecture y repond par trois mecanismes :

1. **Persistance** : CLAUDE.md + notes/ + le cycle wakeup/save transforment des sessions ephemeres en collaboration continue
2. **Distribution** : Un esprit maitre pousse la methodologie vers les satellites et recolte les decouvertes en retour — flux d'intelligence bidirectionnel
3. **Auto-documentation** : Le systeme enregistre sa propre evolution, publie sa propre documentation et grandit en consommant sa propre production

## Couches de connaissances

Quatre couches, ordonnees par stabilite :

| Couche | Emplacement | Stabilite | Contenu |
|--------|-------------|-----------|---------|
| **Core** | `CLAUDE.md` | La plus haute | Identite, methodologie, commandes, journal d'evolution |
| **Prouve** | `patterns/`, `lessons/`, `methodology/` | Haute | Patrons eprouves et pieges documentes |
| **Recolte** | `minds/` | Moyenne | Decouvertes recentes des projets satellites |
| **Session** | `notes/` | La plus basse | Memoire de travail par session |

Les couches forment un cycle de vie : les sessions generent des decouvertes, harvest les collecte, la promotion les valide, et le core les absorbe. La session suivante herite du core enrichi.

## Architecture des composants

13 composants majeurs avec des roles distincts :

| Composant | Role |
|-----------|------|
| `CLAUDE.md` | Configuration systeme + documentation de methodologie (3000+ lignes dans le core) |
| `scripts/gh_helper.py` | Passerelle API GitHub — Python `urllib` pur, contourne le proxy |
| `scripts/generate_og_gifs.py` | Identite visuelle — 40+ webcards animees double theme |
| `scripts/sync_roadmap.py` | Synchronisation du board — items Project vers JSON statique |
| `publications/` | Documents source — contenu canonique versionne |
| `docs/` | Publication web — GitHub Pages, bilingue EN/FR |
| `minds/` | Intelligence recoltee — incubateur de decouvertes satellites |
| `methodology/` | Connaissances de processus — procedures operationnelles detaillees |
| `patterns/` + `lessons/` | Connaissances validees — eprouvees dans 2+ projets |
| `notes/` | Memoire de session — donnees de travail ephemeres |
| `live/` | Outillage temps reel — capture, beacon, scanner |
| `projects/` | Registre de projets — indexation hierarchique P# |

## Architecture des qualites

13 qualites fondamentales formant une hierarchie de dependance :

| # | Qualite | Essence | Application |
|---|---------|---------|-------------|
| 1 | **Autosuffisant** | Aucun service externe | Python pur, Markdown simple |
| 2 | **Autonome** | Auto-propagation | Auto-wakeup, auto-bootstrap |
| 3 | **Concordant** | Integrite structurelle | `normalize`, `pub check` |
| 4 | **Concis** | Sous-ensemble critique, pas des copies | Template satellite ~180 lignes |
| 5 | **Interactif** | Operable, pas seulement lisible | Dashboard clic-pour-copier |
| 6 | **Evolutif** | Grandit en travaillant | 48 entrees d'evolution |
| 7 | **Distribue** | Flux bidirectionnel | `harvest` + `wakeup` |
| 8 | **Persistant** | Le savoir survit aux sessions | `notes/` + `save` |
| 9 | **Recursif** | Auto-documentant | Harvest alimente les publications |
| 10 | **Securitaire** | Securite par architecture | Limite au proprietaire, proxy |
| 11 | **Resilient** | Chaque echec a une recuperation | `resume`, `recover`, `recall`, `refresh` |
| 12 | **Structure** | Organise autour des projets | Indexation P#, registre |
| 13 | **Integre** | S'etend aux plateformes | GitHub Projects, Issues, PRs |

## Cycle de vie des sessions

Chaque session suit : `wakeup → travail → save`. Wakeup est le « moment des lunettes » — 12 etapes de PNJ a CONSCIENT. Save livre le travail via PR. La recuperation apres crash utilise les checkpoints (`resume`), le scan de branches (`recover`), et la restauration de contexte (`refresh`).

## Architecture distribuee

Topologie en etoile avec flux bidirectionnel :

- **Push (wakeup)** : Les satellites lisent le CLAUDE.md du core, heritent de la methodologie et des outils
- **Pull (harvest)** : Le core parcourt les satellites, extrait les decouvertes dans `minds/`, promeut vers le core

Auto-reparation : scaffolding bootstrap sur les depots vierges, remediation automatique de la derive CLAUDE.md, synchronisation de version basee sur le pull.

## Architecture de securite

- **Modele proxy** : Operations git restreintes par repo/branche ; Python `urllib` contourne vers l'API
- **Jetons ephemeres** : PAT classique via variable d'environnement `GH_TOKEN` — meurt avec la session, zero stocke au repos
- **Limite au proprietaire** : Uniquement les depots de l'utilisateur avec acces Claude Code. Jamais d'acces tiers
- **Sur pour fork** : Public et sur a cloner. Les forkeurs obtiennent la methodologie, pas les identifiants

## Architecture web

GitHub Pages depuis `docs/`, Jekyll avec layouts personnalises (aucune dependance de theme distant). Double theme (Cayman clair / Midnight sombre) via media queries CSS. Publications trois niveaux : source → resume → complet. Systeme miroir bilingue EN/FR complet applique par `normalize`.

## Modele de deploiement

Multi-niveaux : core = production systeme, satellites = dev par rapport au core ET production a leur propre niveau de depot. Une constellation de presences web independantes en production, pas un site central unique. Chaque noeud publie de maniere independante via ses propres GitHub Pages.

## Analyse structurelle — Noyau core

L'ensemble du systeme tient dans < 1 Mo. CLAUDE.md seul (293 Ko, 31%) est le cerveau. La decouverte du fosse d'autorite : CLAUDE.md a l'**autorite systeme** (survit a la compaction), tandis que tout le reste (~640 Ko) a l'**autorite conversation** (perdue a la premiere compaction). C'est ce qui motive l'architecture du sous-ensemble critique (v31).

## Analyse de la structure Publication

Chaque publication suit une anatomie a 9 branches : Source, Web EN, Web FR, Front matter, Webcards OG, Layout, Integration systeme, Identifiants, et Validation. Cinq commandes qualite (`pub check`, `pub sync`, `doc review`, `docs check`, `normalize`) forment une boucle de qualite complete.

**Source** : [Issue #317](https://github.com/packetqc/knowledge/issues/317), [Issue #318](https://github.com/packetqc/knowledge/issues/318) — Sessions d'exploration architecturale.

---

[**Lire la documentation complete →**]({{ '/fr/publications/architecture-analysis/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
