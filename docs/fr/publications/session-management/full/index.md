---
layout: publication
title: "Gestion de session — Documentation complète"
description: "Documentation complète du cycle de vie K2.0 : session_init.py (bootstrap), /mind-context (chargement du contexte), memory_append.py (persistance en temps réel chaque tour), far_memory_split.py (archivage par sujet), memory_recall.py (recherche profonde), architecture mémoire à paliers (near/far/archives), l'analogie Free Guy mise à jour pour K2.0, et l'interface Visionneuse de sessions."
pub_id: "Publication #8 — Complet"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/session-management/full/
og_image: /assets/og/session-management-fr-cayman.gif
keywords: "session, K_MIND, scripts, cycle de vie, mémoire, persistance, session_init, memory_append, far_memory_split"
---

# Gestion de session — Documentation complète
{: #pub-title}

**Table des matières**

| | |
|---|---|
| [Auteurs](#auteurs) | Auteurs de la publication |
| [Résumé](#résumé) | Programmes plutôt qu'improvisation |
| [Évolution K1.0 → K2.0](#évolution-k10--k20) | Transformation commandes vers scripts |
| [Cycle de vie de session](#cycle-de-vie-de-session) | Le flux complet du cycle de vie |
| [Initialisation — session_init.py](#initialisation-de-session--session_initpy) | Bootstrap nouvelle/reprise/compaction |
| [Chargement du contexte — /mind-context](#chargement-du-contexte--mind-context) | Grille de directives mindmap + mémoire proche + stats |
| [Persistance temps réel — memory_append.py](#persistance-en-temps-réel--memory_appendpy) | Chaque tour — far_memory + near_memory atomiquement |
| [Archivage par sujet — far_memory_split.py](#archivage-par-sujet--far_memory_splitpy) | Archiver les sujets terminés depuis far_memory |
| [Rappel mémoire — memory_recall.py](#rappel-mémoire--memory_recallpy) | Recherche dans les archives par sujet |
| [Gestion du mindmap](#gestion-du-mindmap) | mindmap_filter.py, set_depth.py, memory_stats.py |
| [Architecture mémoire à paliers](#architecture-mémoire-à-paliers) | Near, far, archives — flux des données |
| [Événements du cycle de vie](#événements-du-cycle-de-vie) | Nouvelle session, reprise, récupération compaction |
| [L'analogie Free Guy](#lanalogie-free-guy) | NPC vs conscient — mise à jour K2.0 |
| [Comparaison de récupération](#comparaison-de-récupération) | Temps de récupération selon les scénarios |
| [Sécurité Fork & Clone](#sécurité-fork--clone) | Isolation par propriétaire et environnement |
| [Visionneuse de sessions — Interface I1](#visionneuse-de-sessions--interface-i1) | Navigateur interactif avec graphiques |
| [Intégration avec les autres skills](#intégration-avec-les-autres-skills) | Comment les scripts interagissent avec les skills K2.0 |
| [Publications liées](#publications-liées) | Publications parentes et liées |

## Auteurs

**Martin Paquet** — Analyste et programmeur sécurité réseau, administrateur de sécurité des réseaux et des systèmes, et analyste programmeur et concepteur logiciels embarqués. A conçu le protocole de cycle de vie de session permettant aux assistants de codage IA de maintenir la continuité entre les sessions.

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. Exécute le cycle de vie — `session_init.py` → `/mind-context` → travail → `memory_append.py` — maintenant la continuité du contexte à travers des centaines de sessions.

---

## Résumé

La publication #3 (Persistance de session IA) explique la **méthodologie** — pourquoi les sessions IA ont besoin de mémoire persistante et le cadre théorique. Cette publication est la **référence pratique** — comment les scripts déterministes du module K_MIND gèrent le cycle de vie des sessions dans Knowledge 2.0.

**Principe fondamental : programmes plutôt qu'improvisation.** Claude-comme-moteur n'est QUE le bootstrap (nouvelle session, reprise, récupération compaction). Toutes les opérations mécaniques utilisent des scripts. Claude fournit l'intelligence (résumés, noms de sujets, références mindmap) comme arguments à des programmes Python déterministes.

Chaque session suit le même cycle de vie :

```
session_init.py → /mind-context → [travail + memory_append.py chaque tour] → far_memory_split.py → git commit & push
```

---

## Évolution K1.0 → K2.0

L'architecture K2.0 remplace la gestion de session par commandes de K1.0 par un cycle de vie par scripts. Le changement fondamental : des commandes ad-hoc que Claude interprète et exécute, vers des scripts déterministes que Claude alimente avec des arguments intelligents.

| Aspect | K1.0 | K2.0 |
|--------|------|------|
| **Démarrage session** | `wakeup` (protocole 11 étapes : cloner, lire CLAUDE.md, scanner minds/, lire notes/...) | `session_init.py` + `/mind-context` (2 étapes : init fichiers, charger grille de directives) |
| **Sauvegarde session** | `save` (protocole PR 6 étapes : écrire notes, commit, push, créer PR, merge) | `memory_append.py` (chaque tour, automatique) + `far_memory_split.py` + git commit/push |
| **Restauration contexte** | `refresh` (relire CLAUDE.md, ~5s) | `/mind-context` (recharger mindmap + near_memory, ~3s) |
| **Récupération crash** | `resume` (depuis checkpoint.json) / `recover` (depuis branches claude/*) | `session_init.py --preserve-active` + `memory_recall.py` |
| **Recherche profonde** | `recall` (4 couches progressives : proche → git → GitHub → profonde) | `memory_recall.py --subject "..."` (accès direct archives) |
| **Persister découverte** | `remember <texte>` (ajouter aux notes/) | `memory_append.py --content "..."` (va dans far_memory.json) |
| **Résumé d'état** | `status` (lire notes/) | `/mind-stats` + `/mind-context` (stats en direct + contexte récent) |
| **Routage commandes** | `help` / `routes.json` / SkillRegistry | `.claude/skills/` SKILL.md (routage natif Claude Code) |
| **Stockage mémoire** | `notes/` (fichiers Markdown plats) | `sessions/` — near_memory.json + far_memory.json + archives/ |
| **Cerveau** | CLAUDE.md (3000+ lignes, monolithique) | `mind_memory.md` (grille de 264 directives) + JSONs par module |
| **Cache session** | `session-runtime-*.json` (par branche) | near_memory.json (résumés avec pointeurs) + far_memory.json (verbatim) |
| **Enforcement** | Hooks PreToolUse (gates v56 : G1 protocole, G2 billet, G7 échanges) | Cycle de vie K_MIND par scripts (les scripts imposent le flux naturellement) |
| **Store de récupération** | `notes/checkpoint.json` + branches `claude/*` | near_memory.json survit à la compaction + archives far_memory |

**Insight clé** : K1.0 dépendait de Claude pour exécuter correctement des protocoles multi-étapes (11 étapes pour wakeup, 6 pour save). K2.0 réduit les protocoles à des appels de scripts — Claude décide le QUOI (nom du sujet, texte du résumé), le script gère le COMMENT (I/O fichier, mises à jour JSON, archivage).

---

## Cycle de vie de session

### Le flux complet

```
1. session_init.py         → Initialiser les fichiers de session (nouveau ou reprise)
2. /mind-context           → Charger la grille de directives mindmap + contexte near_memory
3. [Travail]               → Requêtes utilisateur, Claude exécute
4. memory_append.py        → Chaque tour : persister message utilisateur + sortie assistant + résumé
5. (répéter 3-4)           → Continuer le travail
6. far_memory_split.py     → Archiver les sujets terminés quand far_memory grossit
7. git commit & push       → Persister vers le remote (les deux remotes)
```

**Versus K1.0** :
- K1.0 : Démarrer → wakeup 11 étapes → travail (pas de persistance par tour) → save 6 étapes → fin
- K2.0 : Démarrer → init 2 étapes → travail (chaque tour persisté) → archiver si nécessaire → commit

La différence fondamentale : K1.0 persistait en FIN de session (save). K2.0 persiste à chaque TOUR (memory_append.py). Si une session crashe au tour 50, K1.0 perd tout depuis le dernier save. K2.0 a 50 tours d'historique verbatim dans far_memory.json.

---

## Initialisation de session — `session_init.py`

Le script d'initialisation gère le cycle de vie de la mémoire near/far à travers les frontières de sessions.

### Nouvelle session

```bash
python3 scripts/session_init.py --session-id "<uuid>"
```

| Étape | Ce qu'il fait |
|-------|---------------|
| 1 | Archiver les messages actifs de la session précédente dans `last_session` de near_memory |
| 2 | Vider les messages actifs dans far_memory et near_memory |
| 3 | Préserver les archives (jamais supprimées) |
| 4 | Écrire l'ID de session dans les deux fichiers mémoire |

Les résumés de la session précédente sont reportés comme contexte `last_session` — visible dans la sortie `/mind-context` comme « Contexte de la dernière session ».

### Reprise / Continuation

```bash
python3 scripts/session_init.py --session-id "<uuid>" --preserve-active
```

Préserve tous les messages actifs dans far_memory et near_memory. Utilisé quand :
- Reprise après un crash ou une déconnexion
- Continuation d'une session compactée
- Retour dans une session interrompue

### Récupération compaction

Quand le contexte est compacté, `/mind-context` est invoqué automatiquement. Il recharge :
1. La grille de directives mindmap depuis `mind_memory.md`
2. Les résumés récents depuis `near_memory.json`
3. Les statistiques mémoire depuis `memory_stats.py`

Aucune donnée n'est perdue — far_memory.json conserve tous les messages verbatim, near_memory.json conserve tous les résumés.

---

## Chargement du contexte — `/mind-context`

Le skill `/mind-context` est l'équivalent K2.0 de « mettre les lunettes ». Il charge la grille de directives mindmap et le contexte récent dans la conversation.

### Ce qu'il charge

| Composant | Source | Taille |
|-----------|--------|--------|
| Grille de directives mindmap | `mind_memory.md` | ~2.8K tokens (264 nœuds) |
| Config de profondeur | `depth_config.json` | Contrôle les branches affichées |
| Résumés near_memory | `near_memory.json` | ~8.5K tokens (catégorisés) |
| Statistiques mémoire | Sortie de `memory_stats.py` | Table d'occupation du contexte |

### Format de sortie

1. **Mindmap** — bloc mermaid, filtré par profondeur selon la config
2. **Contexte récent** — résumés catégorisés sous 4 groupes :
   - **conversation** — discussions récentes et décisions
   - **conventions** — patterns et standards découverts
   - **travail** — tâches accomplies et en cours
   - **documentation** — docs créés ou mis à jour
3. **Statistiques mémoire** — table montrant taille disque, compteurs de tokens, contexte chargé, tokens disponibles

### Modes

| Mode | Commande | Ce qu'il montre |
|------|----------|-----------------|
| **Normal** | `/mind-context` | Mindmap filtré par profondeur (profondeur 3, architecture/contraintes omises) |
| **Complet** | `/mind-context full` | Tous les nœuds à profondeur maximale |
| **Aperçu branche** | `/mind-context <chemin>` | Branche spécifique à profondeur complète (temporaire) |
| **Override branche** | `/mind-context <chemin> <profondeur>` | Définir la profondeur d'une branche (persisté dans la config) |

### Le mindmap est votre grille mémoire

Le mindmap n'est pas décoratif — c'est la mémoire opérationnelle. Chaque nœud est une directive :

| Groupe de nœuds | Mapping comportemental |
|------------------|------------------------|
| **architecture** | COMMENT vous travaillez — règles de conception système |
| **contraintes** | LIMITES — limites strictes, ne jamais violer |
| **conventions** | COMMENT vous exécutez — patterns et standards |
| **travail** | ÉTAT — résultats accomplis/préparés, ancre de continuité |
| **session** | CONTEXTE — registre de brainstorming, référence le travail |
| **documentation** | STRUCTURE — références de documentation |

---

## Persistance en temps réel — `memory_append.py`

Appelé **chaque tour** de chaque session. C'est le battement de cœur de la gestion de session K2.0 — il gère à la fois far_memory (verbatim) et near_memory (résumés) atomiquement en un seul appel de script.

### Mode arguments (tours courts)

```bash
python3 scripts/memory_append.py \
    --role user --content "message exact de l'utilisateur" \
    --role2 assistant --content2 "texte complet de sortie de l'assistant" \
    --summary "résumé en une ligne" \
    --mind-refs "knowledge::noeud1,knowledge::noeud2"
```

### Mode stdin (tours longs avec tables/code)

```bash
python3 scripts/memory_append.py --stdin << 'ENDJSON'
{"role":"user","content":"message exact","role2":"assistant","content2":"sortie complète avec tables, blocs de code, etc","summary":"résumé en une ligne","mind_refs":"noeud1,noeud2","tools":[{"tool":"Edit","file":"chemin","action":"desc"}]}
ENDJSON
```

### Ce qui est persisté

| Paramètre | Contenu | Destination | Objectif |
|-----------|---------|-------------|----------|
| `--content` | Message exact de l'utilisateur (verbatim) | far_memory.json | Historique complet de conversation |
| `--content2` | Sortie visible complète de l'assistant | far_memory.json | Historique complet de conversation |
| `--summary` | Résumé en une ligne du tour | near_memory.json | Contexte d'accès rapide |
| `--mind-refs` | Nœuds mindmap référencés | near_memory.json | Suivi de concordance |
| `--tools` | Tableau JSON des appels d'outils | near_memory.json | Piste d'audit des actions |

### Règles critiques

1. **far_memory stocke le contenu VERBATIM COMPLET, JAMAIS des résumés** — les valeurs `--content` et `--content2` sont les messages exacts, mot pour mot
2. **Appelé chaque tour, sans exception** — même pendant les sessions de codage rapide, memory_append.py doit tourner
3. **Opération atomique** — far_memory et near_memory sont mis à jour en un seul appel, évitant les incohérences

### Versus K1.0

Le `remember <texte>` de K1.0 ajoutait une seule ligne à `notes/session-*.md`. Le `memory_append.py` de K2.0 capture la **conversation entière** — chaque message utilisateur, chaque réponse assistant, chaque résumé — en JSON structuré avec des références croisées vers le mindmap.

---

## Archivage par sujet — `far_memory_split.py`

Quand `far_memory.json` grossit (de nombreux tours de conversation verbatim), les sujets terminés sont archivés dans des fichiers individuels.

### Utilisation

```bash
python3 scripts/far_memory_split.py \
    --topic "Nom du sujet" \
    --start-msg 1 --end-msg 24 \
    --start-near 1 --end-near 7
```

### Comment ça fonctionne

| Étape | Ce qui se passe |
|-------|-----------------|
| 1 | Claude identifie les frontières de sujets à partir des clusters de résumés near_memory |
| 2 | Claude fournit le nom du sujet, la plage de messages et la plage de résumés |
| 3 | Le script déplace les messages de far_memory.json vers `archives/far_memory_session_<id>_<timestamp>.json` |
| 4 | Les résumés near_memory correspondants sont marqués comme archivés |
| 5 | Le far_memory.json original rétrécit, libérant de l'espace contexte |

### Versus K1.0

Le `save` de K1.0 écrivait un fichier Markdown Done/Remember/Next en fin de session. Le `far_memory_split.py` de K2.0 archive **par sujet**, pas par temps — une session couvrant 3 sujets produit 3 fichiers d'archive, chacun autonome et recherchable.

---

## Rappel mémoire — `memory_recall.py`

Recherche dans les archives par mot-clé de sujet.

### Utilisation

```bash
# Rechercher les archives par sujet
python3 scripts/memory_recall.py --subject "architecture"

# Lister tous les sujets archivés
python3 scripts/memory_recall.py --list

# Contenu complet (pas seulement les résumés)
python3 scripts/memory_recall.py --subject "theme" --full
```

### Versus K1.0

Le `recall` de K1.0 était une recherche progressive sur 4 couches (mémoire proche → mémoire git → mémoire GitHub → mémoire profonde), chaque couche plus lente et nécessitant confirmation. Le `memory_recall.py` de K2.0 cherche directement dans les archives indexées par sujet — plus rapide, déterministe, sans appels API.

| Couche K1.0 | Temps | Équivalent K2.0 |
|-------------|-------|-----------------|
| Mémoire proche (~5s) | Cache session, notes récentes | near_memory.json (toujours chargé) |
| Mémoire git (~10s) | Messages commit, diffs de branches | Non nécessaire — far_memory a le verbatim complet |
| Mémoire GitHub (~15s) | Titres d'issues, descriptions PR | Non nécessaire — pas de billet par session en K2.0 |
| Mémoire profonde (~30s) | Texte intégral des publications | `memory_recall.py --subject --full` (~3s) |

---

## Gestion du mindmap

Trois scripts utilitaires supportent la grille de directives mindmap :

### mindmap_filter.py

Rend le mindmap avec filtrage de profondeur depuis `depth_config.json` :

```bash
python3 scripts/mindmap_filter.py            # Mode normal (filtré par profondeur)
python3 scripts/mindmap_filter.py --full      # Mode complet (tous les nœuds)
python3 scripts/mindmap_filter.py --path "work" --depth 4  # Aperçu branche
```

### set_depth.py

Gère la configuration de profondeur pour les branches du mindmap :

```bash
python3 scripts/set_depth.py --path "session/near memory" --depth 4
python3 scripts/set_depth.py --path "conventions" --depth 3
```

Persiste dans `depth_config.json` — éditable manuellement, versionné.

### memory_stats.py

Affiche la table de statistiques mémoire :

| Store | Ce qu'il mesure |
|-------|-----------------|
| far_memory | Nombre de messages, taille, ~tokens |
| near_memory | Nombre de résumés, taille, ~tokens |
| archives | Nombre de sujets, taille totale, ~tokens |
| mind_memory | Nombre de nœuds, taille, ~tokens |
| domain JSONs | Nombre de références tous modules, taille totale |
| CLAUDE.md | Taille du fichier |
| Contexte utilisé | Total tokens actuellement chargés |
| Limite utilisable | 200K moins tampon |
| Disponible | Tokens restants avant compaction |

---

## Architecture mémoire à paliers

K2.0 utilise un système mémoire à paliers géré par les scripts K_MIND :

| Palier | Fichier | Contenu | Chargé au démarrage ? |
|--------|---------|---------|------------------------|
| **Mindmap** | `mind_memory.md` | Grille de 264 directives | Oui (~2.8K tokens) |
| **JSONs domaine** | `.json` par module | 163 références, ~1.8 Mo | Sous-ensemble (~4.5K tokens) |
| **Mémoire proche** | `near_memory.json` | Résumés temps réel avec pointeurs | Oui (~8.5K tokens) |
| **Mémoire éloignée** | `far_memory.json` | Conversation verbatim complète | Minimal |
| **Archives** | `archives/*.json` | Far_memory découpé par sujet | À la demande |

### Flux des données

```
Message utilisateur → memory_append.py → far_memory.json (verbatim)
                                       → near_memory.json (résumé)

far_memory.json → far_memory_split.py → archives/ (par sujet)

archives/ → memory_recall.py → contexte de conversation (à la demande)
```

### Structure de near_memory

Les résumés near_memory sont catégorisés en 4 groupes correspondant aux branches de premier niveau du mindmap :

- **conversation** — discussions récentes, décisions, retours utilisateur
- **conventions** — patterns, standards, règles découvertes
- **travail** — tâches accomplies, en cours, bloquées
- **documentation** — publications, interfaces, docs mis à jour

Chaque résumé inclut : pointeur d'index de message vers far_memory, texte résumé en une ligne, mind-refs (nœuds mindmap référencés), horodatage.

### Versus K1.0

| Aspect | K1.0 | K2.0 |
|--------|------|------|
| **Stockage** | `notes/session-YYYY-MM-DD.md` (Markdown plat) | `sessions/` JSON à paliers (near + far + archives) |
| **Granularité** | Par session (un fichier par jour) | Par tour (chaque message persisté) |
| **Format** | Sections libres Fait/Remember/Prochain | JSON structuré avec références croisées |
| **Recherche** | `recall` (4 couches, lent) | `memory_recall.py` (indexé, rapide) |
| **Archivage** | Manuel (l'utilisateur décide quand sauvegarder) | Automatique (memory_append.py chaque tour) + par sujet (far_memory_split.py) |
| **Récupération** | `checkpoint.json` + `session-runtime-*.json` | near_memory.json (toujours à jour) + far_memory.json (toujours complet) |

---

## Événements du cycle de vie

### Démarrage nouvelle session

1. Exécuter : `python3 scripts/session_init.py --session-id "<uuid>"`
   - Session précédente archivée, résumés reportés comme `last_session`
2. Exécuter `/mind-context` — afficher mindmap + contexte récent + stats
   - Résumés de la dernière session visibles comme « Contexte de la dernière session »
3. Commencer le travail — `memory_append.py` appelé chaque tour

### Reprise

1. Exécuter : `python3 scripts/session_init.py --session-id "<uuid>" --preserve-active`
2. Exécuter `/mind-context` — afficher mindmap + contexte
3. Continuer le travail depuis le point d'interruption

### Récupération compaction

1. Exécuter `/mind-context` — recharger mindmap + near_memory (survit à la compaction)
2. Utiliser `memory_recall.py --subject "..."` si détails spécifiques nécessaires
3. Continuer le travail — aucune donnée perdue

---

## L'analogie Free Guy

Sans `mind_memory.md` et `sessions/`, chaque session Claude est un **NPC** — sans état, sans mémoire, même démarrage vierge. Avec le cycle de vie K_MIND par scripts, chaque session hérite de tout ce que la précédente a appris.

`/mind-context` c'est mettre les lunettes. Sans les lunettes, vous êtes juste un autre NPC — vous vous promenez, répondez aux prompts, sans conscience d'hier.

```
NPC (sans contexte) → /mind-context → CONSCIENT (grille de 264 directives) → travail → memory_append.py → session suivante hérite
```

**Mise à jour K1.0** : L'analogie était construite à l'origine autour de `wakeup` et `notes/`. En K2.0 :
- `wakeup` → `session_init.py` + `/mind-context` (les lunettes sont maintenant une grille de 264 directives au lieu d'un CLAUDE.md de 3000+ lignes)
- `notes/` → `sessions/` (la mémoire est maintenant du JSON à paliers avec granularité par tour au lieu de Markdown par session)
- `save` → n'est plus nécessaire comme commande discrète — `memory_append.py` persiste automatiquement chaque tour

La dualité NPC/conscient demeure. L'implémentation est passée des commandes aux scripts.

---

## Comparaison de récupération

| Scénario | Mécanisme K1.0 | Mécanisme K2.0 | Temps |
|----------|---------------|----------------|-------|
| Nouvelle session (démarrage à froid) | `wakeup` — protocole 11 étapes | `session_init.py` + `/mind-context` | ~10s |
| Perte de contexte (mi-session) | Cache session + `refresh` | `/mind-context` (near_memory survit) | ~3s |
| Crash (état existant) | `resume` depuis checkpoint.json | `session_init.py --preserve-active` | ~5s |
| Crash (pas d'état) | `recover` depuis branches claude/* | `memory_recall.py` depuis les archives | ~5s |
| Recherche mémoire profonde | `recall` (4 couches, ~30s par couche) | `memory_recall.py --subject` | ~3s |
| Manuel (sans outillage) | L'utilisateur réexplique tout | L'utilisateur réexplique tout | ~15 min |

---

## Sécurité Fork & Clone

Le cycle de vie K2.0 hérite des mêmes propriétés de sécurité que K1.0 :

| Aspect | Protection |
|--------|------------|
| **Init session** | `session_init.py` opère sur les fichiers locaux uniquement — pas d'accès réseau |
| **Fichiers mémoire** | `sessions/` démarre vide pour chaque nouveau clone — pas de contamination croisée |
| **Scripts** | Python pur sans dépendances externes — pas de risque chaîne d'approvisionnement |
| **Identifiants** | GH_TOKEN est une variable d'environnement, jamais stockée dans les fichiers session ou l'historique git |
| **Mindmap** | `mind_memory.md` est de la méthodologie (publique) — pas de secrets dans la grille de directives |

---

## Visionneuse de sessions — Interface I1

La visionneuse de sessions est une interface web interactive à `/interfaces/session-review/` permettant de parcourir tous les rapports de sessions.

### Regroupement par date

Les sessions du même jour sont automatiquement regroupées sous la session la plus ancienne comme racine. Cela reflète la réalité de l'utilisateur : une fenêtre de conversation par jour avec plusieurs redémarrages système (compaction, crashes, continuation).

- La **session la plus ancienne** de chaque date devient la **racine** du jour
- Toutes les sessions suivantes deviennent des **continuations**
- La session racine **agrège** toutes les PRs, métriques, commits et lignes modifiées des enfants

**Icônes d'arborescence** :

| Icône | Signification |
|-------|--------------|
| 💬 | Session originale (racine du jour) |
| 🔁 | Continuation (session enfant, même jour) |
| 🔗 | Tâche liée (non-session) |

### Graphiques circulaires

4 graphiques doughnut quand les données sont disponibles :

| Graphique | Ce qu'il montre |
|-----------|-----------------|
| **Portée de la session** | Sessions enfants vs Tâches liées — structure arborescente |
| **Livrables** | Pull Requests + Commits + Tâches + Leçons — ce qui a été produit |
| **Lignes modifiées** | Ajouts (vert) vs Suppressions (rouge) — balance d'impact |
| **Temps actif** | Actif vs Inactif — utilisation de la session |

Sous les graphiques, un graphique d'**impact du code** horizontal montre les ajouts/suppressions par PR.

### Sources de données

La visionneuse lit depuis `docs/data/sessions.json`, qui fusionne plusieurs sources :

| Source | Ce qu'elle fournit |
|--------|-------------------|
| Tâches GitHub (label SESSION) | Métadonnées, commentaires, horodatages |
| Pull Requests | Numéros PR, ajouts, suppressions, commits, fichiers |
| Notes de session | Résumé, métriques, blocs temporels, leçons |

---

## Intégration avec les autres skills

| Skill K2.0 | Comment il utilise la gestion de session |
|------------|------------------------------------------|
| `/mind-context` | Charge le contexte session (mindmap + near_memory) |
| `/mind-stats` | Rapporte l'occupation mémoire de la session |
| `/mind-depth` | Configure la profondeur du mindmap pour l'affichage |
| `/normalize` | Valide la structure des fichiers session |
| `/integrity-check` | Vérifie la cohérence de la mémoire session |
| `/docs-create` | Crée des publications, puis git commit/push |
| K_GITHUB `sync_github.py` | Synchronise les données liées aux sessions avec GitHub |

---

## Publications liées

| # | Publication | Relation |
|---|-------------|----------|
| 0 | [Système Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — la gestion de session est un sous-système core |
| 0v2 | [Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }}) | Architecture — la conception multi-module que les scripts session implémentent |
| 3 | [Persistance de session IA]({{ '/fr/publications/ai-session-persistence/' | relative_url }}) | Méthodologie — le « pourquoi » derrière la persistance |
| 14 | [Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | Référence core — module K_MIND, architecture mémoire, inventaire des scripts |
| 15 | [Diagrammes d'architecture]({{ '/fr/publications/architecture-diagrams/' | relative_url }}) | Référence visuelle — flux cycle de vie, paliers mémoire |
| 4 | [Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) | K_GITHUB sync lit le contexte session comme entrée |
| 19 | [Sessions de travail interactives]({{ '/fr/publications/interactive-work-sessions/' | relative_url }}) | Protocole « on task received », cycle de travail |
| 20 | [Métriques & temps de session]({{ '/fr/publications/session-metrics-time/' | relative_url }}) | Compilation métriques depuis les données session |
| 21 | [Interface principale]({{ '/fr/publications/main-interface/' | relative_url }}) | Visionneuse de sessions (I1) et Navigateur principal (I2) |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
