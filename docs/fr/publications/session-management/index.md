---
layout: publication
title: "Gestion de session — Cycle de vie K_MIND par scripts"
description: "Référence pratique du cycle de vie K2.0 : session_init.py (bootstrap), /mind-context (chargement du contexte), memory_append.py (persistance en temps réel), far_memory_split.py (archivage par sujet), memory_recall.py (recherche profonde) — programmes plutôt qu'improvisation, scripts déterministes avec l'intelligence de Claude comme arguments."
pub_id: "Publication #8"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/session-management/
og_image: /assets/og/session-management-fr-cayman.gif
keywords: "session, K_MIND, scripts, cycle de vie, mémoire, persistance, session_init, memory_append"
---

# Gestion de session — Cycle de vie K_MIND par scripts
{: #pub-title}

> **Publication parente** : [#0 — Système Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Référence core** : [#14 — Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | [#15 — Diagrammes d'architecture]({{ '/fr/publications/architecture-diagrams/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Programmes plutôt qu'improvisation |
| [Évolution K1.0 → K2.0](#évolution-k10--k20) | Transformation commandes vers scripts |
| [Cycle de vie de session](#cycle-de-vie-de-session) | session_init.py → /mind-context → travail → memory_append.py → far_memory_split.py → git |
| [Initialisation de session](#initialisation-de-session--session_initpy) | Bootstrap par script déterministe |
| [Chargement du contexte](#chargement-du-contexte--mind-context) | Grille de directives mindmap + mémoire proche |
| [Persistance en temps réel](#persistance-en-temps-réel--memory_appendpy) | Chaque tour — far_memory + near_memory atomiquement |
| [Archivage par sujet](#archivage-par-sujet--far_memory_splitpy) | Archiver les sujets terminés depuis far_memory |
| [Rappel mémoire](#rappel-mémoire--memory_recallpy) | Recherche dans les archives par sujet |
| [Statistiques mémoire](#statistiques-mémoire--mind-stats) | Occupation du contexte et tokens disponibles |
| [Visionneuse de sessions (I1)](#visionneuse-de-sessions--interface-i1) | Navigateur interactif avec graphiques et regroupement |
| [L'analogie Free Guy](#lanalogie-free-guy) | NPC vs conscient — mise à jour K2.0 |

## Résumé

La publication #3 (Persistance de session IA) explique la **méthodologie** — pourquoi les sessions IA ont besoin de mémoire persistante. Cette publication est la **référence pratique** — comment les scripts déterministes du module K_MIND gèrent le cycle de vie des sessions dans Knowledge 2.0.

**Principe fondamental : programmes plutôt qu'improvisation.** Claude fournit l'intelligence (résumés, noms de sujets, références mindmap) comme arguments à des scripts Python déterministes. Chaque opération mécanique est scriptée — pas d'écriture de notes libre, pas de gestion d'état manuelle.

Chaque session suit :

```
session_init.py → /mind-context → [travail + memory_append.py chaque tour] → far_memory_split.py → git commit & push
```

## Évolution K1.0 → K2.0

| K1.0 (Commandes) | K2.0 (Scripts) |
|-------------------|----------------|
| `wakeup` (bootstrap 11 étapes) | `session_init.py` + `/mind-context` |
| `save` (protocole PR 6 étapes) | `memory_append.py` (chaque tour) + `far_memory_split.py` + git commit/push |
| `refresh` (relire CLAUDE.md) | `/mind-context` (recharger mindmap + near_memory) |
| `resume` / `recover` | `session_init.py --preserve-active` + `memory_recall.py` |
| `recall` (recherche 4 couches) | `memory_recall.py --subject "..."` |
| `remember <texte>` | `memory_append.py --content "..."` |
| `status` (lire notes/) | `/mind-stats` + `/mind-context` |
| `help` / `?` | `.claude/skills/` SKILL.md (Claude Code natif) |
| `notes/` (fichiers plats) | `sessions/` — near_memory.json + far_memory.json + archives/ |
| CLAUDE.md (3000+ lignes) | `mind_memory.md` (grille de 264 directives) + JSONs par module |
| Cache `session-runtime-*.json` | near_memory.json (résumés) + far_memory.json (verbatim) |
| Hooks PreToolUse (gates v56) | Cycle de vie K_MIND par scripts (les scripts imposent le flux) |

## Cycle de vie de session

```
session_init.py → /mind-context → [travail] → memory_append.py (chaque tour) → far_memory_split.py → git commit & push
```

Chaque session, chaque tour, chaque sujet. Les scripts gèrent toutes les opérations mécaniques — Claude fournit l'intelligence comme arguments.

## Initialisation de session — `session_init.py`

Initialise les fichiers de session et gère le cycle de vie de la mémoire near/far.

| Mode | Commande | Ce qu'il fait |
|------|----------|---------------|
| **Nouvelle session** | `session_init.py --session-id "<id>"` | Archiver la session précédente, reporter les résumés dans `last_session` |
| **Reprise** | `session_init.py --session-id "<id>" --preserve-active` | Préserver les messages actifs, restaurer le contexte |
| **Récupération compaction** | (auto via `/mind-context`) | Recharger mindmap + near_memory depuis le disque |

## Chargement du contexte — `/mind-context`

Le skill `/mind-context` charge la grille de directives mindmap et les résumés near_memory. Sortie :

1. **Mindmap** — bloc mermaid depuis `mind_memory.md` (264 nœuds, ~2.8K tokens)
2. **Contexte récent** — résumés near_memory catégorisés (conversation, conventions, travail, documentation)
3. **Statistiques mémoire** — taille disque, compteurs de tokens, contexte chargé, tokens disponibles

Modes : normal (filtré par profondeur), complet (tous les nœuds), aperçu de branche (chemin spécifique en profondeur complète).

## Persistance en temps réel — `memory_append.py`

Appelé **chaque tour**. Gère far_memory + near_memory atomiquement.

| Paramètre | Contenu | Destination |
|-----------|---------|-------------|
| `--content` | Message exact de l'utilisateur (verbatim) | far_memory.json |
| `--content2` | Sortie complète de l'assistant (verbatim) | far_memory.json |
| `--summary` | Résumé en une ligne | near_memory.json |
| `--mind-refs` | Nœuds mindmap référencés | near_memory.json |
| `--tools` | Appels d'outils effectués | near_memory.json |

Supporte le mode `--stdin` pour les contenus longs (tables, blocs de code, diagrammes mermaid).

## Archivage par sujet — `far_memory_split.py`

Quand far_memory grossit, archiver les sujets terminés :

```bash
python3 scripts/far_memory_split.py \
    --topic "Nom du sujet" \
    --start-msg 1 --end-msg 24 \
    --start-near 1 --end-near 7
```

Claude identifie les frontières de sujets à partir des clusters de résumés near_memory. Le script déplace les messages vers `archives/far_memory_session_<id>_<timestamp>.json`.

## Rappel mémoire — `memory_recall.py`

Recherche dans les archives par sujet :

```bash
python3 scripts/memory_recall.py --subject "architecture"   # Rechercher
python3 scripts/memory_recall.py --list                       # Lister les archives
python3 scripts/memory_recall.py --subject "theme" --full     # Contenu complet
```

Remplace la recherche progressive K1.0 à 4 couches par un accès direct aux archives indexées.

## Statistiques mémoire — `/mind-stats`

Montre l'occupation du contexte par store mémoire :

| Store | Ce qu'il mesure |
|-------|-----------------|
| far_memory | Nombre de messages verbatim + taille |
| near_memory | Nombre de résumés + taille |
| archives | Nombre de sujets + taille totale |
| mind_memory | Nombre de nœuds + taille |
| domain JSONs | Nombre de références + taille totale |
| Contexte utilisé | Total de tokens chargés |
| Disponible | Tokens restants avant compaction |

## Visionneuse de sessions — Interface I1

Interface web interactive à `/interfaces/session-review/` pour parcourir les rapports de session. Fonctionnalités :

- **Regroupement par date** : sessions du même jour regroupées sous la plus ancienne comme racine, les suivantes comme continuations. La racine agrège toutes les données des enfants.
- **4 graphiques** : Portée de la session, Livrables, Lignes modifiées, Temps actif
- **Graphique d'impact du code** : ajouts/suppressions par PR individuelle
- **Compilation métriques** : fichiers, commits, lignes modifiées, vélocité, temps calendrier/actif
- **Chronologie** : commentaires de tâche avec expansion/réduction

## L'analogie Free Guy

Sans `mind_memory.md` et `sessions/`, chaque session Claude est un **NPC** — sans état, sans mémoire. Avec le cycle de vie K_MIND par scripts (`session_init.py` → `/mind-context` → travail → `memory_append.py`), chaque session hérite de tout ce que la précédente a appris.

`/mind-context` c'est mettre les lunettes. Sans les lunettes, vous êtes juste un autre NPC.

```
NPC (sans contexte) → /mind-context → CONSCIENT (grille de 264 directives) → travail → memory_append.py → session suivante hérite
```

Récupération : ~10 secondes avec `/mind-context` vs ~15 minutes de ré-explication manuelle.

---

[**Lire la documentation complète →**]({{ '/fr/publications/session-management/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
