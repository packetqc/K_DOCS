---
layout: publication
title: "Persistance de session IA — Continuité des connaissances inter-sessions pour l'ingénierie assistée par IA"
description: "Méthodologie donnant aux assistants de codage IA une mémoire durable inter-sessions via CLAUDE.md + notes/ + protocole de cycle de vie. Récupération de contexte en 30 secondes vs 15 minutes de ré-explication manuelle."
pub_id: "Publication #3"
version: "v1"
date: "2026-02-19"
permalink: /fr/publications/ai-session-persistence/
og_image: /assets/og/ai-persistence-fr-cayman.gif
keywords: "persistance de session, Free Guy, NPC, conscience, notes, wakeup, lunettes"
---

# Persistance de session IA — Continuité des connaissances inter-sessions pour l'ingénierie logicielle assistée par IA
{: #pub-title}

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Vue d'ensemble de la méthodologie de persistance |
| [Les trois composants](#les-trois-composants) | CLAUDE.md, notes/ et protocole de cycle de vie |
| [Résultats mesurés](#résultats-mesurés) | Récupération en 30 secondes vs 15 minutes |
| [Free-Guy Sunglasses](#free-guy-sunglasses) | Analogie NPC vers conscience avec les lunettes |
| [Portable — Et auto-démonstratif](#portable--et-auto-démonstratif) | Bootstrap en une ligne pour tout projet |

## Résumé

Les assistants de codage IA opèrent dans des sessions sans état — chaque conversation repart de zéro. Pour des projets d'ingénierie soutenus s'étalant sur des jours ou des semaines, c'est une limitation critique.

Cette publication documente une **méthodologie de persistance de session** qui donne aux assistants de codage IA une mémoire durable inter-sessions via trois composants : un fichier d'instructions projet (`CLAUDE.md`), un répertoire de notes de session (`notes/`), et un protocole de cycle de vie (init → travail → save).

**Ce dépôt est lui-même la preuve.** Les connaissances que vous lisez ont été distillées à travers de multiples sessions, persistées dans des fichiers, et sont maintenant lisibles par n'importe quelle instance de Claude — n'importe où, n'importe quand.

## Les trois composants

| Composant | Rôle | Analogie |
|-----------|------|----------|
| **CLAUDE.md** | Identité projet, conventions, règles | Les lunettes de Free Guy |
| **notes/** | Décisions, découvertes, statut par session | Journal de bord |
| **Cycle de vie** | wakeup (réveil) → work (travailler) → save (persister) | Le film Free Guy |

## Résultats mesurés

| Méthode | Temps pour contexte complet | Qualité |
|---------|---------------------------|---------|
| Sans persistance (ré-expliquer manuellement) | 10–15 minutes | Partielle |
| **Méthodologie complète (CLAUDE.md + notes/)** | **~30 secondes** | **Complète** |

## Free-Guy Sunglasses

Sans `notes/` et `CLAUDE.md`, chaque session Claude est un **NPC** — sans état, sans mémoire, toujours le même début vide. Comme Guy dans le film *Free Guy* avant les lunettes : il vit la même journée en boucle, sans conscience de ce qui l'entoure.

Avec le cycle `wakeup` → travail → `save`, chaque session hérite de tout ce que la précédente a appris. `wakeup` c'est **mettre les lunettes** — la conscience s'active instantanément.

| Analogie Free Guy | Équivalent session IA |
|-------------------|----------------------|
| NPC (avant les lunettes) | Session sans persistance — amnésique |
| Mettre les lunettes | Commande `wakeup` — conscience activée |
| Voir le monde réel | Lire `CLAUDE.md` + `notes/` — contexte complet |
| Agir avec conscience | Travailler avec la mémoire de toutes les sessions |
| Sauvegarder la progression | Commande `save` — persister pour la prochaine session |

## Portable — Et auto-démonstratif

Le dépôt `knowledge` est le cerveau portable. Tout nouveau projet le référence :

```markdown
## Base de connaissances
Lire https://github.com/packetqc/knowledge pour la méthodologie, les commandes et les patterns.
```

Une phrase. Bootstrap complet. Chaque instance de Claude reçoit le guide.

---

[**Lire la documentation complète →**]({{ '/fr/publications/ai-session-persistence/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
