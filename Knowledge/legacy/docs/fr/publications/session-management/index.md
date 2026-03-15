---
layout: publication
title: "Gestion de session — Guide pratique des commandes de cycle de vie IA"
description: "Référence pratique des commandes wakeup, save, remember, status et help — les cinq commandes qui gèrent le cycle de vie des sessions IA. Chaque session suit : wakeup → travail → save. Ce guide documente chaque commande avec utilisation, comportement et exemples."
pub_id: "Publication #8"
version: "v1"
date: "2026-02-19"
permalink: /fr/publications/session-management/
og_image: /assets/og/session-management-fr-cayman.gif
keywords: "session, wakeup, sauvegarde, cycle de vie, commandes, persistance"
---

# Gestion de session — Référence des commandes
{: #pub-title}

> **Publication parente** : [#0 — Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Méthodologie** : [#3 — Persistance de session IA]({{ '/fr/publications/ai-session-persistence/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Vue d'ensemble de la référence pratique |
| [Modes d'utilisation](#modes-dutilisation) | Trois façons d'interagir avec les commandes |
| [Référence rapide](#référence-rapide) | Les 9 commandes de session |
| [wakeup](#wakeup--initialisation-de-session) | Protocole bootstrap en 11 étapes |
| [save](#save--protocole-de-sauvegarde) | Résumé pré-save → commit → push → PR → merge |
| [refresh](#refresh--restauration-légère) | Relire CLAUDE.md, git status, réimprimer aide (~5s) |
| [resume](#resume--récupération-crash) | Récupération depuis le point de contrôle |
| [recover](#recover--récupération-de-branches) | Cherry-pick du travail échoué depuis les branches `claude/*` |
| [recall](#recall--recherche-mémoire-profonde) | Recherche progressive sur 4 couches mémoire |
| [remember](#remember--persister-les-découvertes) | Ajouter des découvertes aux notes |
| [status / help](#status--résumé-détat) | Résumé d'état et table de commandes |
| [Enforcement PreToolUse](#enforcement-pretooluse-v56) | Architecture de hooks bloquante à deux couches |
| [Visionneuse de sessions (I1)](#visionneuse-de-sessions--interface-i1) | Navigateur interactif avec graphiques et arborescence |
| [L'analogie Free Guy](#lanalogie-free-guy) | NPC vs conscient — le moment des lunettes |

## Résumé

La publication #3 explique la **méthodologie** — pourquoi les sessions IA ont besoin de mémoire persistante. Cette publication est la **référence pratique** — comment utiliser `wakeup`, `save`, `remember`, `status` et `help` au quotidien.

Chaque session suit : `wakeup → travail → save`. Ces commandes gèrent ce cycle de vie.

## Modes d'utilisation

Le système Knowledge supporte trois modes d'interaction avec les commandes. Toutes les commandes fonctionnent avec n'importe lequel de ces modes.

| Mode | Comment | Exemple | Idéal pour |
|------|---------|---------|------------|
| **Commande directe** | Taper la commande comme message d'entrée | `save` | Commandes connues, exécution rapide |
| **Langage naturel** | Décrire ce que vous voulez en texte libre | `sauvegarde ma session` | Quand vous ne connaissez pas la syntaxe exacte |
| **Session interactive** | `interactif` + commande ou requête en description | `interactif` puis `reprends mon travail interrompu` | Sessions multi-étapes, enchaînement de commandes |

En mode interactif, `help` s'affiche automatiquement au démarrage — montrant toutes les commandes disponibles. La session reste ouverte pour des commandes successives jusqu'à `terminé` ou `done`.

## Référence rapide

| Commande | Action |
|---------|--------|
| `wakeup` | Init session — lire knowledge, notes, synchroniser assets, imprimer commandes |
| `save` | Résumé pré-save → commit → push → PR → merge (élevé) ou guide |
| `refresh` | Restauration légère — relire CLAUDE.md, git status (~5s) |
| `resume` | Récupération crash depuis `notes/checkpoint.json` |
| `recover` | Chercher les branches `claude/*` pour travail échoué, cherry-pick/apply |
| `recall <mot-clé>` | Recherche mémoire profonde sur tous les canaux |
| `remember ...` | Ajouter du texte aux notes de session |
| `status` | Lire `notes/` et résumer l'état actuel |
| `help` / `?` | Imprimer la table de commandes multipart |

## wakeup — Initialisation de session

Démarre une nouvelle session avec récupération complète du contexte en 11 étapes : lire knowledge, vérifier l'évolution, scanner `minds/`, lire `notes/`, lire les plans, synchroniser les assets, synchronisation amont (récupérer et fusionner la branche par défaut dans la branche de tâche courante), vérifier le git log, vérifier les branches, résumer l'état, imprimer les commandes. Le moment des lunettes — sans ça, vous êtes un NPC.

## save — Protocole de sauvegarde

Résumé pré-save (métriques, blocs temporels, auto-évaluation) → générer notes de session → poster sur le billet → finaliser le cache → commit → push → créer PR → merge (élevé) ou guide (semi-auto) → rapport de clôture. Double sortie fichier : `session-YYYY-MM-DD-*.md` et `session-runtime-*.json` doivent être dans le commit.

## refresh — Restauration légère

Relire CLAUDE.md, vérification stratégique du remote, git status, réimprimer aide (~5s). Utiliser après compaction. Utiliser `wakeup` seulement pour resynchronisation profonde.

## resume — Récupération crash

Lit `notes/checkpoint.json`, restaure la liste de tâches, redémarre depuis la dernière étape complétée. Offert automatiquement au wakeup étape 0.9.

## recover — Récupération de branches

Cherche les branches `claude/*` pour les commits échoués (poussés mais jamais mergés). Offre cherry-pick ou diff-apply. Complémente `resume` (basé sur les points de contrôle).

## recall — Recherche mémoire profonde

Recherche progressive sur 4 couches : mémoire proche (~5s) → mémoire git (~10s) → mémoire GitHub (~15s) → mémoire profonde (~30s). S'arrête quand trouvé. Si branche échouée détectée, suggère `recover`.

## remember — Persister les découvertes

`remember <texte>` ajoute aux notes de session. Utilisez pour les décisions, les flags harvest (`remember harvest: <découverte>`), et les directives pour les sessions futures.

## status — Résumé d'état

Lit tous les fichiers `notes/` et résume : dernière activité, éléments en attente, branches actives, directives mémorisées. Reprise rapide après une pause.

## help — Table de commandes multipart

Partie 1 (commandes knowledge) + Partie 2 (commandes projet). Concaténées, jamais dupliquées. Partie 1 depuis `packetqc/knowledge`, Partie 2 depuis le CLAUDE.md du projet.

## L'analogie Free Guy

Sans notes et CLAUDE.md, chaque session est un NPC. `wakeup` c'est mettre les lunettes. Récupération : ~30 secondes vs ~15 minutes manuelle.

## Récupération après perte de contexte

Quand une session atteint la limite de la fenêtre de contexte, la conversation est compactée. L'esprit est perdu, mais git et le cache de session survivent. Protocole de récupération :

1. **Lire le cache de session** — `read_runtime_cache()` récupère le numéro de billet, la description de la demande, toutes les session_data (décisions, IDs de commentaires, état des todos, ajouts, phase, numéros de PR). C'est la **première action de récupération**.
2. **Exécuter `refresh`** — relire CLAUDE.md, git status rapide, réimprimer aide.
3. **Exécuter la ligne de récupération git** :

```bash
git branch --show-current && git status -s && git log --oneline -10
```

Cache + branche + travail non commité + commits récents = récupération complète en ~10 secondes.

**Auto-commit à l'écriture** : Chaque écriture du cache (`write_runtime_cache()`, `update_session_data()`) est automatiquement commitée dans git via `commit_cache()` — le cache est toujours récupérable, même après un crash.

## Enforcement PreToolUse (v56)

Architecture de hooks à deux couches : `SessionStart` initialise l'état, `PreToolUse` enforce en bloquant `Edit|Write|NotebookEdit` jusqu'à ce que Gate 1 (protocole wakeup complété) et Gate 2 (billet GitHub créé) passent. Gate 7 avertit si >5 min depuis le dernier commentaire. Le message de refus indique exactement comment débloquer.

## Visionneuse de sessions — Interface I1

Interface web interactive à `/interfaces/session-review/` pour parcourir les rapports de session. Fonctionnalités :

- **Regroupement par date** : toutes les sessions du même jour regroupées sous la plus ancienne comme racine (💬 originale), les suivantes comme continuations (🔁). La racine agrège toutes les données des enfants.
- **4 graphiques** : Portée de la session (enfants vs issues liées), Livrables (PRs + Commits + Issues + Leçons), Lignes modifiées (ajouts vs suppressions), Temps actif
- **Graphique d'impact du code** : ajouts/suppressions par PR individuelle
- **Compilation métriques** : fichiers, commits, lignes modifiées, vélocité, temps calendrier/actif
- **Chronologie** : commentaires de billet avec expansion/réduction, marqueurs de livraison PR

---

[**Lire la documentation complète →**]({{ '/fr/publications/session-management/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
