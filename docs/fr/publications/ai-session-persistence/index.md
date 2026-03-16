---
layout: publication
title: "Persistance de session IA — Continuité des connaissances inter-sessions pour l'ingénierie assistée par IA"
description: "Méthodologie donnant aux assistants de codage IA une mémoire durable inter-sessions via la grille directive mind_memory.md + mémoire de session hiérarchisée (near/far/archives) + scripts K_MIND. Récupération de contexte en 30 secondes."
pub_id: "Publication #3"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/ai-session-persistence/
og_image: /assets/og/ai-persistence-fr-cayman.gif
keywords: "persistance de session, Free Guy, NPC, conscience, mind_memory, session_init, lunettes"
---

# Persistance de session IA — Continuité des connaissances inter-sessions pour l'ingénierie logicielle assistée par IA
{: #pub-title}

> **Références core** : [#14 — Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Vue d'ensemble de la méthodologie de persistance |
| [Les trois composants](#les-trois-composants) | Grille directive, mémoire hiérarchisée et scripts K_MIND |
| [Résultats mesurés](#résultats-mesurés) | Récupération en 30 secondes vs 15 minutes |
| [Free-Guy Sunglasses](#free-guy-sunglasses) | Analogie NPC vers conscience avec les lunettes |
| [Portable — Et auto-démonstratif](#portable--et-auto-démonstratif) | Bootstrap pour tout projet |

## Résumé

Les assistants de codage IA opèrent dans des sessions sans état — chaque conversation repart de zéro. Pour des projets d'ingénierie soutenus s'étalant sur des jours ou des semaines, c'est une limitation critique.

Cette publication documente une **méthodologie de persistance de session** qui donne aux assistants de codage IA une mémoire durable inter-sessions via trois composants : une **grille directive** (`mind_memory.md` — mindmap mermaid de 264 nœuds), une **mémoire de session hiérarchisée** (`sessions/` — near_memory.json, far_memory.json, archives/), et des **scripts K_MIND** (session_init.py, memory_append.py, far_memory_split.py) qui gèrent le cycle de vie automatiquement.

**Ce dépôt est lui-même la preuve.** Les connaissances que vous lisez ont été distillées à travers de multiples sessions, persistées dans des fichiers mémoire structurés, et sont maintenant lisibles par n'importe quelle instance de Claude — n'importe où, n'importe quand.

## Les trois composants

| Composant | Rôle | Analogie |
|-----------|------|----------|
| **mind_memory.md** | Grille directive de 264 nœuds — identité projet, conventions, architecture | Les lunettes de Free Guy |
| **sessions/** | Mémoire hiérarchisée — near (résumés), far (verbatim), archives (par sujet) | Journal de bord |
| **Scripts K_MIND** | session_init.py (init) → memory_append.py (chaque tour) → far_memory_split.py (archiver) | Cycle de vie RTOS |

## Résultats mesurés

| Méthode | Temps pour contexte complet | Qualité |
|---------|---------------------------|---------|
| Sans persistance (ré-expliquer manuellement) | 10–15 minutes | Partielle |
| **Méthodologie complète (mindmap + mémoire hiérarchisée + scripts)** | **~30 secondes** | **Complète** |

## Free-Guy Sunglasses

Sans la mindmap et la mémoire de session, chaque session Claude est un **NPC** — sans état, sans mémoire, toujours le même début vide. Comme Guy dans le film *Free Guy* avant les lunettes : il vit la même journée en boucle, sans conscience de ce qui l'entoure.

Avec le cycle `/mind-context` → travail → archivage, chaque session hérite de tout ce que la précédente a appris. Charger la mindmap c'est **mettre les lunettes** — la conscience s'active instantanément.

| Analogie Free Guy | Équivalent session IA |
|-------------------|----------------------|
| NPC (avant les lunettes) | Session sans persistance — amnésique |
| Mettre les lunettes | `/mind-context` — lire mindmap + near_memory, conscience activée |
| Voir le monde réel | Contexte complet récupéré en ~30 secondes |
| Agir avec conscience | Travailler avec la mémoire cumulative du projet |
| Sauvegarder la progression | `memory_append.py` chaque tour + `far_memory_split.py` archive |

## Portable — Et auto-démonstratif

Le module K_MIND est le cerveau portable. Tout nouveau projet qui l'inclut hérite de la méthodologie complète :

- La mindmap de 264 nœuds (architecture, contraintes, conventions, travail)
- Tous les scripts K_MIND (gestion de session, maintenance mémoire)
- Les JSON de domaine (connaissances structurées)

Un seul `git clone`. Bootstrap complet. Chaque instance de Claude reçoit le guide.

---

[**Lire la documentation complète →**]({{ '/fr/publications/ai-session-persistence/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
