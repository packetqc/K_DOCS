---
layout: publication
title: "Gestion de session — Documentation complète"
description: "Documentation complète des commandes de gestion de session : protocole wakeup (10 étapes), protocole save (livraison semi-automatique), remember (persistance des découvertes), status (récupération d'état), help (table multipart), l'analogie Free Guy, format des notes et récupération inter-sessions."
pub_id: "Publication #8 — Complet"
version: "v1"
date: "2026-02-19"
permalink: /fr/publications/session-management/full/
og_image: /assets/og/session-management-fr-cayman.gif
keywords: "session, wakeup, sauvegarde, cycle de vie, commandes, persistance"
---

# Gestion de session — Documentation complète
{: #pub-title}

**Table des matières**

| | |
|---|---|
| [Auteurs](#auteurs) | Auteurs de la publication |
| [Résumé](#résumé) | Vue d'ensemble de la référence pratique |
| [Modes d'utilisation](#modes-dutilisation) | Trois façons d'interagir avec les commandes |
| [Référence rapide](#référence-rapide) | Les 9 commandes de session |
| [wakeup — Initialisation de session](#wakeup--initialisation-de-session) | Protocole bootstrap en 11 étapes avec récupération de contexte |
| [save — Protocole de sauvegarde](#save--protocole-de-sauvegarde) | Résumé pré-save → commit → push → PR → merge |
| [refresh](#refresh--restauration-légère-du-contexte) | Relire CLAUDE.md, git status, réimprimer aide (~5s) |
| [resume](#resume--récupération-crash-depuis-checkpoint) | Récupération depuis le point de contrôle |
| [recover](#recover--récupération-de-branches) | Cherry-pick du travail échoué depuis les branches `claude/*` |
| [recall](#recall--recherche-mémoire-profonde) | Recherche progressive sur 4 couches mémoire |
| [remember — Persister les découvertes](#remember--persister-les-découvertes) | Ajouter des découvertes aux notes de session |
| [status — Résumé d'état](#status--résumé-détat) | Lire les notes et résumer l'état actuel |
| [help — Table de commandes multipart](#help--table-de-commandes-multipart) | Commandes knowledge + projet concaténées |
| [Cycle de vie de session](#cycle-de-vie-de-session) | Comment les sessions persistent dans le temps |
| &nbsp;&nbsp;[L'analogie Free Guy](#lanalogie-free-guy) | NPC vs conscient — le moment des lunettes |
| &nbsp;&nbsp;[Format des notes de session](#format-des-notes-de-session) | Sections Fait, Remember, Prochain |
| &nbsp;&nbsp;[Récupération inter-sessions](#récupération-inter-sessions) | Comment wakeup restaure le contexte de la session précédente |
| &nbsp;&nbsp;[Récupération après déconnexion client](#récupération-après-déconnexion-client) | Chemins de récupération lors d'une déconnexion en cours de sauvegarde |
| &nbsp;&nbsp;[Cache d'exécution de session](#cache-dexécution-de-session--mémoire-résiliente-à-la-compaction) | Couche mémoire résiliente à la compaction |
| &nbsp;&nbsp;[Récupération après perte de contexte](#récupération-après-perte-de-contexte) | Récupération priorité cache après compaction |
| [Enforcement PreToolUse (v56)](#enforcement-pretooluse-v56) | Architecture de hooks bloquante à deux couches |
| [Visionneuse de sessions — Interface I1](#visionneuse-de-sessions--interface-i1) | Navigateur interactif avec graphiques et arborescence |
| [Intégration avec les autres commandes](#intégration-avec-les-autres-commandes) | Interaction avec harvest, normalize, etc. |
| [Publications liées](#publications-liées) | Publications parentes et liées |

## Auteurs

**Martin Paquet** — Analyste et programmeur sécurité réseau, administrateur de sécurité des réseaux et des systèmes, et analyste programmeur et concepteur logiciels embarqués. A conçu le protocole de cycle de vie de session permettant aux assistants de codage IA de maintenir la continuité entre les sessions.

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. Exécute le cycle de vie — wakeup, travail, save — maintenant la continuité du contexte à travers des centaines de sessions.

---

## Résumé

La publication #3 explique la **méthodologie** — pourquoi les sessions IA ont besoin de mémoire persistante et comment CLAUDE.md + notes/ y parvient. Cette publication est la **référence pratique** — comment utiliser `wakeup`, `save`, `remember`, `status` et `help` au quotidien.

```
wakeup → lire notes/ → résumer l'état → travailler → save → commit & push
```

---

## Modes d'utilisation

Le système Knowledge supporte trois modes d'interaction avec les commandes. Toutes les commandes de cette publication fonctionnent avec n'importe lequel de ces modes.

| Mode | Comment | Exemple | Idéal pour |
|------|---------|---------|------------|
| **Commande directe** | Taper la commande comme message d'entrée | `save` | Commandes connues, exécution rapide |
| **Langage naturel** | Décrire ce que vous voulez en texte libre | `sauvegarde ma session` | Quand vous ne connaissez pas la syntaxe exacte |
| **Session interactive** | `interactif` + commande ou requête en description | `interactif` puis `reprends mon travail interrompu` | Sessions multi-étapes, enchaînement de commandes |

### Commande directe

Taper le nom de la commande directement comme message :

```
save
```
```
pub list
```
```
harvest healthcheck
```

Chemin le plus rapide quand vous connaissez la commande exacte.

### Langage naturel

Décrire ce que vous voulez dans vos propres mots — le système l'achemine vers la bonne commande :

```
sauvegarde ma session
```
```
montre-moi les publications existantes
```
```
peux-tu vérifier mes projets satellites pour de nouvelles découvertes ?
```

Fonctionne en français ou en anglais. L'intention est reconnue et acheminée vers la commande appropriée.

### Session interactive

Commencer avec `interactif` comme message d'entrée, puis fournir une description :

```
interactif
```
> Description : `reprends mon travail interrompu et ensuite crée un nouveau projet test`

En mode interactif :
- `help` s'affiche automatiquement au démarrage de la session
- La description est analysée pour détecter les commandes exécutables
- Plusieurs commandes peuvent être enchaînées en séquence
- La session reste ouverte pour des commandes successives jusqu'à `terminé` ou `done`

---

## Référence rapide

| Commande | Action |
|---------|--------|
| `wakeup` | Init session — lire knowledge, notes, synchroniser assets, commandes |
| `save` | Résumé pré-save → commit → push → PR → merge (élevé) ou guide |
| `refresh` | Restauration légère — relire CLAUDE.md, git status (~5s) |
| `resume` | Récupération crash depuis `notes/checkpoint.json` |
| `recover` | Chercher les branches `claude/*` pour travail échoué, cherry-pick/apply |
| `recall <mot-clé>` | Recherche mémoire profonde sur tous les canaux |
| `remember ...` | Ajouter du texte aux notes de session |
| `status` | Lire `notes/` et résumer l'état actuel |
| `help` / `?` | Table de commandes multipart |

---

## wakeup — Initialisation de session

Démarre une session avec récupération complète du contexte.

| Étape | Action | Ce qu'elle fait |
|------|--------|-------------|
| 0 | **Mettre les lunettes** | Lire `packetqc/knowledge` CLAUDE.md en premier |
| 0.5 | **Scaffolding bootstrap** | Créer les fichiers essentiels manquants sur les dépôts vierges (non destructif) |
| 0.6 | **Démarrer le beacon** | Lancer le beacon pour la découverte inter-instances |
| 0.7 | **Synchronisation amont** | Récupérer et fusionner la branche par défaut dans la branche de tâche courante. Récupère les PR fusionnées depuis le début de la session (ex. assets `live/`, notes, fichiers scaffold). Essentiel pour relancer wakeup en cours de session sans archiver |
| 1 | **Évolution** | Rapporter les dernières entrées |
| 2 | **Connaissances distribuées** | Scanner `minds/` |
| 3 | **Lire les notes** | Tous les fichiers `notes/` |
| 4 | **Lire les plans** | `PLAN.md`, `changelog.txt` |
| 5 | **Synchroniser les assets** | Copier `live/` si manquant |
| 6 | **Git log** | 20 derniers commits |
| 7 | **Branches** | Toutes les branches actives |
| 8 | **Résumer** | Dernière session, état, prochaines étapes |
| 9 | **Imprimer l'aide** | Intelligence + table de commandes |
| 10 | **Demander** | Sur quoi se concentrer |

### Sécurité : Fork & Clone

Si vous forkez ou clonez ce dépôt, les commandes de session sont **limitées au propriétaire** et isolées par environnement :

| Aspect | Protection |
|--------|------------|
| **`wakeup`** | Lit le dépôt knowledge du propriétaire original via HTTPS public — un forkeur obtient la méthodologie (intentionnellement publique) mais aucun accès aux comptes |
| **`save`** | Ne pousse que vers la branche assignée de la session — le Claude Code d'un forkeur ne peut pousser vers le dépôt original |
| **`notes/`** | Démarre vierge pour chaque nouvel utilisateur — aucune contamination entre propriétaires |
| **Identifiants / jetons** | Aucun stocké dans les notes, CLAUDE.md ou l'historique git |

Pour utiliser la gestion de session avec vos propres projets : remplacez `packetqc` par votre nom d'utilisateur GitHub dans CLAUDE.md. Le cycle de vie (`wakeup` → travail → `save`) s'adapte automatiquement à votre espace de noms.

---

## save — Protocole de sauvegarde

Livraison semi-automatique — Claude fait 95%, l'utilisateur fournit un clic.

| Étape | Action | Qui |
|------|--------|-----|
| 1 | Écrire les notes dans `notes/session-YYYY-MM-DD.md` | Claude |
| 2 | Commiter sur la branche de tâche | Claude |
| 3 | `git push -u origin <branche-tâche>` | Claude |
| 4 | Créer PR : branche tâche → `main` | Claude |
| 5 | Approuver/merger la PR | **Utilisateur** |

**Pourquoi semi-automatique** : Le proxy de Claude Code restreint l'accès push à la branche assignée uniquement. Pousser vers la branche par défaut retourne HTTP 403. La PR est le pont.

**Règle de la todo list** : Lors de l'exécution de `save`, la liste doit inclure les 4 étapes autonomes : écrire notes, commettre, pousser, créer PR.

---

## refresh — Restauration légère du contexte

```
refresh
```

Relit CLAUDE.md, effectue une vérification stratégique du remote, git status rapide, relit les notes de session, réimprime l'aide. Pas de clone, pas de sync (~5 secondes). Utiliser après compaction ou quand les règles méthodologiques semblent oubliées. Utiliser `wakeup` seulement pour une resynchronisation profonde.

---

## resume — Récupération crash depuis checkpoint

```
resume
```

Lit `notes/checkpoint.json`, vérifie l'état git, restaure la liste de tâches, et redémarre le protocole depuis la dernière étape complétée. Les points de contrôle sont écrits automatiquement aux frontières d'étapes par les commandes compatibles (`save`, `harvest`, `normalize --fix`, `pub new`, `wakeup`). Supprime automatiquement le checkpoint après un resume réussi.

Offert automatiquement lors du `wakeup` étape 0.9 quand un fichier checkpoint est détecté.

---

## recover — Récupération de branches

```
recover
```

Cherche les branches `claude/*` pour du travail échoué — des commits poussés mais jamais mergés via PR. Affiche les commits non mergés, les diffs de fichiers, et le statut PR pour chaque branche. Offre deux chemins de récupération :

| Chemin | Méthode | Quand utiliser |
|--------|---------|----------------|
| **Cherry-pick** | Appliquer des commits spécifiques depuis la branche échouée | Quand les commits sont propres et autonomes |
| **Diff-apply** | Extraire le diff et appliquer comme nouveau commit | Quand les commits chevauchent le travail actuel |

Complémente `resume` (basé sur les checkpoints). `recover` récupère depuis les branches poussées où aucun checkpoint n'existe.

---

## recall — Recherche mémoire profonde

```
recall <mot-clé ou question>
```

Commande hybride qui cherche à travers tous les canaux de connaissances pour trouver des informations des sessions passées. Recherche progressive sur 4 couches, s'arrête quand une réponse est trouvée :

| Couche | Temps | Ce qu'elle cherche |
|--------|-------|-------------------|
| **Mémoire proche** | ~5s | Cache de session courant, `notes/session-runtime-*.json` récents, `notes/session-*.md` récents |
| **Mémoire git** | ~10s | Messages de commits, noms de branches, diffs de fichiers à travers les branches `claude/*` |
| **Mémoire GitHub** | ~15s | Titres/commentaires d'issues, descriptions de PR, éléments du board (nécessite élévation) |
| **Mémoire profonde** | ~30s | Recherche texte intégral à travers publications, méthodologie, patterns, leçons, minds/ |

Si du travail sur branche échouée est détecté, suggère `recover` pour cherry-pick/appliquer.

---

## remember — Persister les découvertes

```
remember Ajouter date de création et version à toutes les publications
```

| Cas d'usage | Exemple |
|----------|---------|
| Décision | `remember Choisi le mode WAL pour SQLite` |
| Flag harvest | `remember harvest: Cache page se dégrade à 81%` |
| Todo | `remember Prochaine session : tester la stratégie de checkpoint` |
| Préférence | `remember L'utilisateur préfère les messages de commit en français` |

Les textes commençant par `harvest:` sont collectés par `harvest` lors du parcours des satellites.

---

## status — Résumé d'état

Lit tous les fichiers `notes/` et produit un résumé : dernière activité, éléments en attente, branches actives, directives mémorisées. Reprise rapide après une pause.

---

## help — Table de commandes multipart

**Partie 1 — Commandes knowledge** (depuis `packetqc/knowledge`) :

| Groupe | Commandes |
|--------|-----------|
| Gestion de session | `wakeup`, `help`, `status`, `save`, `remember` |
| Normalize | `normalize`, `normalize --fix`, `normalize --check` |
| Harvest | Toutes les sous-commandes `harvest` |
| Publications | `pub list`, `pub check`, `pub new`, `pub sync`, `docs check` |
| Webcards | Cibles `webcard` |
| Session live | `I'm live`, `multi-live`, `deep`, `analyze`, `recipe` |

**Partie 2 — Commandes projet** (depuis le CLAUDE.md du projet) :

| Aspect | Détail |
|--------|--------|
| Source | Le CLAUDE.md du projet |
| Contenu | Variable par projet |

Règle : jamais de duplication — concaténation.

---

## Cycle de vie de session

### L'analogie Free Guy

Sans `notes/` et `CLAUDE.md`, chaque session Claude est un **NPC** — sans état, sans mémoire. Avec la boucle `wakeup → travail → save`, chaque session hérite de tout ce que la précédente a appris.

`wakeup` c'est mettre les lunettes. Sans les lunettes, vous êtes juste un autre NPC.

### Format des notes de session

```markdown
# Notes de session — 2026-02-19

## Fait
1. Créé la Publication #5
2. Corrigé la concordance de langue des layouts

## Remember
- Ajouter date de création et version à tous les docs/pubs

## Prochain
- Créer les publications restantes (#6, #7, #8)
```

### Récupération inter-sessions

Au `wakeup`, tous les fichiers `notes/` sont lus chronologiquement. La section « Prochain » de la session la plus récente devient le point de départ. Les directives « Remember » s'accumulent.

**Temps de récupération** : ~30 secondes avec `wakeup` vs ~15 minutes de ré-explication manuelle.

### Récupération après déconnexion client

Quand l'interface client (onglet navigateur, application bureau, VS Code) se déconnecte en cours de session — après que les commits ont été poussés mais avant la création de PR — le travail est sûr sur la branche distante. Le **git push est la frontière de durabilité**.

| Chemin | Méthode | Vitesse |
|--------|---------|---------|
| **A** | Rafraîchir le navigateur / reprendre la session | Instantané |
| **B** | Création manuelle de PR (`gh_helper.py` ou interface web GitHub) | Minutes |
| **C** | Nouvelle session + commande `resume` | ~10s |
| **D** | Attendre le harvest | Heures/jours (non recommandé) |

### Cache d'exécution de session — Mémoire résiliente à la compaction

Le cache d'exécution de session (`notes/session-runtime-<suffixe>.json`) est la **couche de mémoire résiliente à la compaction**. Les données écrites ici survivent à la compression du contexte, aux crashs et au redémarrage du conteneur. C'est le quatrième canal de persistance — au-delà de git, des notes et des billets GitHub.

**Convention de nommage multi-session** : Chaque session a son propre fichier cache, nommé d'après le suffixe de la branche :

| Branche | Fichier cache |
|---------|--------------|
| `claude/session-cache-qa-0o1sQ` | `session-runtime-0o1sQ.json` |
| `claude/fix-webcards-abc12` | `session-runtime-abc12.json` |

**Fonctions principales** (depuis `scripts/session_agent.py`) :

```python
from scripts.session_agent import write_runtime_cache, read_runtime_cache, update_session_data

# Écrire le cache complet au démarrage
write_runtime_cache(repo="packetqc/knowledge", issue_number=521,
                    issue_title="SESSION: ...", branch="claude/task-xyz")

# Lire le cache après compaction/crash
cache = read_runtime_cache()
issue = cache["issue_number"]
data = cache.get("session_data", {})

# Mettre à jour des clés individuelles pendant le travail
update_session_data("current_todo", "Corriger le bug d'authentification")
```

**Ce qui est persisté dans `session_data`** :

| Clé | Type | But |
|-----|------|-----|
| `comment_ids` | Map étape → ID commentaire | PATCH ⏳→✅ sur commentaires existants |
| `decisions` | Liste de chaînes | Décisions clés pour la récupération de contexte |
| `current_todo` | Chaîne | Étape todo en cours |
| `files_modified` | Liste de chemins | Conscience du périmètre pour les commits |
| `request_addon` | Liste de `{index, timestamp, verbatim}` | Commentaires d'ajout utilisateur verbatim |
| `request_addon_synthesis` | Liste de `{index, timestamp, synthesis}` | Interprétation de Claude pour chaque ajout |
| `todo_snapshot` | Liste de `{content, status}` | État complet de la todo list |
| `session_phase` | Chaîne | Phase du cycle de vie (wakeup/planning/executing/saving/delivered) |
| `pr_numbers` | Liste de `{number, title, status}` | PRs créées cette session |
| `git_state` | `{last_commit_sha, uncommitted_count, timestamp}` | Vérification de l'état de la branche |
| `time_markers` | Liste de `{event, timestamp}` | Chronologie pour la compilation des métriques |
| `elevation_status` | Booléen | Si GH_TOKEN est disponible |
| `default_branch` | Chaîne | Nom de la branche par défaut détectée |
| `work_summary` | Chaîne | Résumé courant des accomplissements |
| `errors_encountered` | Liste de `{error, timestamp}` | Journal d'erreurs pour la détection de motifs |
| `issue_comments_count` | Entier | Nombre de commentaires pour la vérification d'intégrité |

**Auto-commit à l'écriture** : Chaque écriture du cache est automatiquement commitée dans git. `write_runtime_cache()` et `update_session_data()` appellent `commit_cache()` immédiatement après l'écriture sur disque — le fichier cache est ajouté à git et commité avec un message descriptif. Cela garantit que le cache est récupérable via `recall` même si la session crashe avant un commit manuel.

**Fonctions d'aide dédiées** :

```python
from scripts.session_agent import (
    append_request_addon, read_request_addons,
    update_todo_snapshot, update_session_phase, append_pr_number,
    update_git_state, append_time_marker, update_elevation_status,
    update_default_branch, update_work_summary, append_error,
    update_issue_comments_count
)
```

#### Add-ons de requête — Suivi des instructions en cours de session

Quand un utilisateur fournit des instructions supplémentaires pendant le travail, elles sont stockées comme **add-ons** — des entrées appariées verbatim + synthèse :

```python
append_request_addon(
    verbatim="ajoute aussi la gestion d'erreurs pour le cas limite...",
    synthesis="Ajouter la gestion d'erreurs pour les entrées vides."
)
addons = read_request_addons()
```

Les add-ons sont des **données de travail actives** — les sessions doivent les lire à la récupération et les vérifier avant chaque étape todo.

### Récupération après perte de contexte

Quand une session atteint la limite de la fenêtre de contexte, la conversation est **compactée**. L'esprit est perdu, mais l'état git et le cache de session survivent.

**Protocole de récupération** (par priorité) :

| Étape | Action |
|-------|--------|
| 1 | **Lire le cache de session** — `read_runtime_cache()` récupère le numéro du billet, la description de la demande, toutes les session_data (décisions, IDs de commentaires, état todo, add-ons, phase, numéros de PR). C'est la **première action de récupération**. |
| 2 | **Exécuter `refresh`** — relire CLAUDE.md, git status rapide, réimprimer l'aide. Restaure les règles de formatage et la méthodologie. |
| 3 | **Exécuter la ligne de récupération git** — `git branch --show-current && git status -s && git log --oneline -10` |
| 4 | **Lire `notes/`** — notes de session si écrites avant la compaction |
| 5 | **Reprendre le travail** — aucune remise à niveau nécessaire |

**Comparaison de récupération** :

| Scénario | Mécanisme de récupération | Temps |
|----------|--------------------------|-------|
| Nouvelle session (démarrage à froid) | `wakeup` — protocole complet | ~30 secondes |
| Perte de contexte (mi-session) | Cache de session + `refresh` | ~10 secondes |
| Crash (checkpoint existe) | `resume` depuis le checkpoint | ~10 secondes |
| Crash (pas de checkpoint) | `recall` depuis la branche échouée | ~15 secondes |
| Manuel (sans outillage) | L'utilisateur réexplique tout | ~15 minutes |

---

## Enforcement PreToolUse (v56)

Architecture de hooks à deux couches qui assure que chaque session suit le protocole avant de modifier des fichiers.

**Architecture** :

| Couche | Événement hook | Peut bloquer ? | Objectif |
|--------|---------------|----------------|----------|
| **SessionStart** | Init session | Non (informer seulement) | Initialiser le fichier d'état, imprimer le résumé |
| **PreToolUse** | Avant `Edit\|Write\|NotebookEdit` | **Oui** (exit 2 = refus) | Enforcer les gates, bloquer les éditions |

**Gates d'enforcement** :

| Gate | Champ | Déverrouillé par | Empêche |
|------|-------|-----------------|---------|
| **G1 — Protocole** | `protocol_completed` | `update_enforcement_state()` après vérification d'intégrité (étape 0.35) | Éditer des fichiers sans compléter le wakeup |
| **G2 — Issue** | `issue_created` | `write_runtime_cache()` avec numéro d'issue (automatique) | Éditer des fichiers sans billet de suivi |
| **G7 — Échanges** | `last_post_time` | `post_exchange()` à chaque commentaire (continu) | Avertissement si >5 min depuis le dernier commentaire |

**Fichier d'état** : `/tmp/.claude-session-state.json` — éphémère, par conteneur.

**Exceptions** (toujours autorisées) : `/tmp/*`, `.claude/*`, `notes/session-runtime-*`, `notes/checkpoint.json`.

---

## Visionneuse de sessions — Interface I1

Interface web interactive à `/interfaces/session-review/` permettant de parcourir tous les rapports de sessions de connaissances.

### Regroupement par date

Les sessions du même jour sont automatiquement regroupées sous la session la plus ancienne comme racine. Cela reflète la réalité de l'utilisateur : une fenêtre de conversation par jour avec plusieurs redémarrages système (compaction, crashes, continuation).

- La **session la plus ancienne** (par heure de création du billet) de chaque date devient la **racine** du jour (💬 originale)
- Toutes les sessions suivantes deviennent des **continuations** (🔁)
- La session racine **agrège** toutes les PRs, métriques, commits et lignes modifiées des enfants
- Sélectionner la session racine montre l'image combinée du travail de toute la journée

**Icônes d'arborescence** :

| Icône | Signification |
|-------|--------------|
| 💬 | Session originale (racine du jour) |
| 🔁 | Continuation (session enfant, même jour) |
| 🔗 | Issue liée (non-session) |

### Graphiques circulaires

La visionneuse affiche 4 graphiques doughnut quand les données sont disponibles :

| Graphique | Position | Ce qu'il montre |
|-----------|----------|-----------------|
| **Portée de la session** | 1er | Sessions enfants vs Issues liées — la structure arborescente |
| **Livrables** | 2ème | Pull Requests + Commits + Issues + Leçons — ce qui a été produit |
| **Lignes modifiées** | 3ème | Ajouts (vert) vs Suppressions (rouge) — balance d'impact du code |
| **Temps actif** | 4ème | Actif vs Inactif — utilisation de la session |

Sous les graphiques, un **graphique d'impact du code** horizontal montre les ajouts/suppressions par PR individuelle.

---

## Intégration avec les autres commandes

| Commande | Comment elle utilise la gestion de session |
|---------|-------------------------------|
| `harvest` | Lit les flags `remember harvest:` des notes |
| `normalize` | Recommandé avant `save` |
| `I'm live` | Pause le flux régulier pendant le monitoring |
| Toutes les commandes d'écriture | Terminent avec `save` pour livrer via PR |

---

## Publications liées

| # | Publication | Relation |
|---|-------------|----------|
| 0 | [Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — la gestion de session est un sous-système core |
| 3 | [Persistance de session IA]({{ '/fr/publications/ai-session-persistence/' | relative_url }}) | Méthodologie — le « pourquoi » derrière ces commandes |
| 4 | [Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) | harvest lit les notes de session comme données d'entrée |
| 7 | [Protocole Harvest]({{ '/fr/publications/harvest-protocol/' | relative_url }}) | harvest traite les notes `remember harvest:` |
| 19 | [Sessions de travail interactives]({{ '/fr/publications/interactive-work-sessions/' | relative_url }}) | Protocole « on task received », cycle de vie des billets |
| 20 | [Métriques & temps de session]({{ '/fr/publications/session-metrics-time/' | relative_url }}) | Compilation métriques pré-save, blocs temporels |
| 21 | [Interface principale]({{ '/fr/publications/main-interface/' | relative_url }}) | Visionneuse de sessions (I1) et Navigateur principal (I2) |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
