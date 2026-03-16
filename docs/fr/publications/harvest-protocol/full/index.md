---
layout: publication
title: "Protocole Harvest — Documentation complète"
description: "Documentation complète du protocole harvest : toutes les commandes avec exemples, pipeline de promotion étape par étape, healthcheck réseau, remédiation des satellites, aide contextuelle, gestion d'erreurs, flux de travail courants et inventaire des connaissances."
pub_id: "Publication #7 — Complet"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/harvest-protocol/full/
og_image: /assets/og/harvest-protocol-fr-cayman.gif
keywords: "récolte, promotion, bilan de santé, satellites, perspectives, dérive de version"
---

# Protocole Harvest — Documentation complète
{: #pub-title}

**Table des matières**

| | |
|---|---|
| [Auteurs](#auteurs) | Auteurs de la publication |
| [Résumé](#résumé) | Guide pratique de collecte de connaissances distribuées |
| [Référence rapide](#référence-rapide) | Toutes les commandes harvest en un coup d'oeil |
| [Concept fondamental](#concept-fondamental) | Flux bidirectionnel et portée d'accès |
| [Récolter un satellite](#récolter-un-satellite) | Protocole en 10 étapes pour extraire les connaissances |
| [Le pipeline de promotion](#le-pipeline-de-promotion) | Flux réviser, préparer, promouvoir, auto-promouvoir |
| [Healthcheck réseau](#healthcheck-réseau) | Balayage complet avec icônes de sévérité |
| [Remédiation des satellites](#remédiation-des-satellites) | Correction de dérive basée sur le pull |
| [Aide contextuelle](#aide-contextuelle) | Ajouter `?` pour la documentation en ligne |
| [Gestion d'erreurs](#gestion-derreurs) | Rapport d'erreurs sans échec silencieux |
| [Flux de travail courants](#flux-de-travail-courants) | Vérification quotidienne, nouvelle découverte, procédures guidées |
| [Ce qui est récolté](#ce-qui-est-récolté) | Catégories de connaissances extraites |
| [Inventaire des connaissances](#inventaire-des-connaissances) | Vérifications de l'état bootstrap des satellites |
| [Publications liées](#publications-liées) | Publications parentes et liées |

## Auteurs

**Martin Paquet** — Analyste et programmeur sécurité réseau, administrateur de sécurité des réseaux et des systèmes, et analyste programmeur et concepteur logiciels embarqués. Architecte du protocole harvest — le mécanisme de flux inverse qui ramène les connaissances évoluées des projets satellites vers le cerveau maître central.

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. Exécute les opérations harvest, parcourt les dépôts satellites, extrait les découvertes et gère le pipeline de promotion.

---

## Résumé

La publication #4 (Connaissances distribuées) documente l'**architecture** du flux bidirectionnel de connaissances. Cette publication est le **guide pratique** — comment K_GITHUB `sync_github.py` remplace les commandes `harvest` de K1.0.

---

## Référence rapide

| Commande | Action |
|---------|--------|
| `sync_github.py <projet>` | Synchroniser depuis un satellite |
| `harvest --list` | Lister tous les projets avec version + dérive |
| `harvest --procedure` | Procédure guidée de promotion |
| K_GITHUB + K_VALIDATION `/integrity-check` | Balayage réseau complet + file d'auto-promotion |
| `harvest --review <N>` | Marquer la découverte #N comme révisée |
| `harvest --stage <N> <type>` | Préparer pour intégration |
| Manuel : mettre à jour `conventions.json` ou `work.json` | Promouvoir vers le core maintenant |
| `harvest --auto <N>` | Mettre en file pour le prochain healthcheck |
| K_GITHUB sync vers satellite | Mettre à jour le CLAUDE.md du satellite |
| `harvest <cmd> ?` | Aide contextuelle pour toute sous-commande |

---

## Concept fondamental

| Direction | Description |
|-----------|-------------|
| **Push (sortant)** | Au démarrage de session, les satellites chargent le module K_MIND (`mind_memory.md` + JSONs de domaine). |
| **Harvest (entrant)** | K_GITHUB `sync_github.py` gère la synchronisation bidirectionnelle — extrayant les connaissances évoluées et les plaçant dans `far_memory archives/`. |

```
Projet satellite → sync_github.py → far_memory archives/ → révision → promotion → connaissances core
```

**Portée d'accès** : Harvest n'opère que sur les dépôts que l'utilisateur possède et auxquels Claude Code a reçu accès via sa configuration d'application GitHub. Aucun dépôt externe ou tiers n'est jamais parcouru. C'est une frontière de sécurité délibérée.

Tout accès satellite utilise le HTTPS public : `https://github.com/packetqc/<projet>`, ciblant la branche par défaut (`main` ou `master`).

### Sécurité : Fork & Clone

Si vous forkez ou clonez ce dépôt, le protocole harvest est **limité au propriétaire** et isolé par environnement :

| Aspect | Protection |
|--------|------------|
| **Aucun identifiant ni jeton** | Harvest utilise uniquement des URLs HTTPS publiques — rien n'est stocké |
| **Les URLs satellites** | Référencent les dépôts du propriétaire original — le harvest d'un forkeur lit les données publiques (lecture seule) ou échoue gracieusement (403/404 → marqué `unreachable`) |
| **L'accès en écriture** | Limité par session — `harvest --fix` ne peut pousser que vers la branche assignée de la session courante |
| **Les données archives** | Spécifiques aux satellites du propriétaire original — repartent à zéro quand vous exécutez vos propres harvests |

Pour utiliser harvest avec vos propres projets : remplacez `packetqc` par votre nom d'utilisateur GitHub dans CLAUDE.md. Le protocole s'adapte — vos satellites, votre espace de noms, vos données.

---

## Récolter un satellite

```
sync_github.py STM32N6570-DK_SQLITE
```

**Protocole (10 étapes) :**

| Étape | Action |
|-------|--------|
| 1. Énumérer les branches | `git ls-remote` |
| 2. Vérifier les curseurs | Comparer chaque HEAD avec le dernier SHA récolté |
| 3. Scanner le nouveau contenu | `CLAUDE.md`, `sessions/`, conventions, flags `remember harvest:` |
| 4. Inventaire des connaissances | Le satellite dispose-t-il du module K_MIND et des JSONs de domaine ? |
| 5. Vérification de version | Lire `<!-- knowledge-version: vN -->` |
| 6. Extraire | Méthodologie, patterns, pièges, instructions Claude |
| 7. Mettre à jour | Écrire dans les archives |
| 8. Rapporter | Nouveautés, dérive, candidats à promotion |
| 9. Mettre à jour le tableau de bord | Rafraîchir le tableau satellite |
| 10. Regénérer les webcards | Si les données ont changé |

**Incrémental** : Chaque harvest stocke un curseur (SHA + date). Le prochain harvest ne scanne que les nouveaux commits.

---

## Le pipeline de promotion

| Étape | <span id="promotion-icons">Icône</span> | Commande | Effet |
|-------|------|---------|--------|
| Réviser | 🔍 | `harvest --review N` | L'humain a lu et validé |
| Préparer | 📦 | `harvest --stage N <type>` | Préparé pour intégration |
| Promouvoir | ✅ | `harvest --promote N` | Écrit dans le core maintenant |
| Auto | 🔄 | `harvest --auto N` | En file pour le prochain healthcheck |

**Types de cibles :**

| Type | Fichier cible | Pour quoi |
|------|------------|----------|
| `lesson` | `conventions.json (pièges)` | Ce qui a cassé |
| `pattern` | `conventions.json (patterns)` | Approches prouvées |
| `methodology` | `methodology/` | Améliorations de processus |
| `evolution` | nœuds `mind_memory.md` ou `work.json` | Découvertes architecturales sur le système lui-même |
| `docs` | Publications ou pages docs | Documentation |

---

## Healthcheck réseau

```
K_GITHUB + K_VALIDATION /integrity-check
```

Balayage complet de tous les satellites connus :

| Étape | Action |
|-------|--------|
| 1 | Parcourir chaque satellite (incrémental) |
| 2 | Mettre à jour les icônes de sévérité dans le tableau de bord |
| 3 | Traiter la file d'auto-promotion |
| 4 | Regénérer les webcards si les données ont changé |
| 5 | Commettre, pousser sur la branche de tâche, créer PR ciblant la branche par défaut |
| 6 | Rapporter : comptes sain/stale/inaccessible, distribution de dérive |

**Icônes de sévérité :**

| <span id="severity-icons">Icône</span> | Sévérité | Utilisé pour |
|------|----------|----------|
| 🟢 | Actuel / Sain | Dérive 0, Bootstrap actif, Sessions 1+ |
| 🟡 | Dérive mineure | Dérive 1-3, Santé stale |
| 🟠 | Dérive modérée | Dérive 4-7 |
| 🔴 | Critique / Manquant | Dérive 8+, Bootstrap manquant |
| ⚪ | Inactif | Sessions 0, Santé en attente |

---

## Remédiation des satellites

```
K_GITHUB sync vers satellite
```

| Étape | Action |
|-------|--------|
| 1 | Lire le tag `<!-- knowledge-version: vN -->` du satellite |
| 2 | Générer un push du module K_MIND mis à jour |
| 3 | Enregistrer la remédiation dans les archives |
| 4 | La correction atteint `main` quand l'utilisateur approuve la PR |
| 5 | Le satellite s'auto-répare au prochain démarrage de session |

**Pourquoi basé sur le pull ?** L'accès push de Claude Code est limité par le proxy : par dépôt et par branche. Impossible de pousser vers les dépôts satellites. Le satellite lit le core mis à jour à son prochain démarrage de session — auto-réparation.

---

## Aide contextuelle

Ajoutez `?` à toute sous-commande :

```
harvest ?                    # Toutes les commandes avec descriptions
harvest --review ?           # Découvertes révisables, utilisation, exemples
harvest --stage ?            # Types valides, découvertes préparées
harvest --promote ?          # Ce qui est écrit où, exemples
harvest --fix ?              # Dérive actuelle des satellites, exemples
```

---

## Gestion d'erreurs

Ne jamais échouer silencieusement. Chaque commande incomplète affiche :

| Élément | Description |
|---------|-------------|
| Ce qui est incorrect | L'erreur spécifique ou le paramètre manquant |
| Utilisation correcte | La syntaxe de commande avec les arguments requis |
| Contexte de l'état actuel | Découvertes disponibles, satellites, etc. |
| Exemple fonctionnel | Une commande prête à copier-coller |

---

## Flux de travail courants

**Vérification quotidienne :**
```
harvest --list
harvest --healthcheck
```

**Nouvelle découverte :**
```
harvest STM32N6570-DK_SQLITE
harvest --review 1
harvest --stage 1 lesson
harvest --promote 1
```

**Satellite en retard :**
```
harvest --list
harvest --fix STM32N6570-DK_SQLITE
```

**Procédure guidée :**
```
harvest --procedure
```

---

## Ce qui est récolté

| Catégorie | Exemples |
|----------|----------|
| **Instructions Claude** | Directives spécifiques au projet pouvant se généraliser |
| **Patterns évolués** | Nouveaux patterns découverts |
| **Nouveaux pièges** | Ce qui a cassé, pas encore dans `conventions.json` |
| **Progrès méthodologiques** | Améliorations de processus, nouveaux scripts et skills |
| **Publications** | Écrits techniques dans les dépôts satellites |
| **Flags harvest** | Notes marquées `remember harvest: <découverte>` |

---

## Inventaire des connaissances

| Vérification | Signification |
|-------|---------------|
| `mind_memory.md` + scripts K_MIND présents | Lunettes actives |
| `sessions/` existe — Mémoire session à paliers active | Persistance de session active |
| K_DOCS `scripts/` présent — Outillage documentation déployé | Outillage live déployé |
| Propre `conventions.json` ou `work.json` par module | A évolué sa propre couche |
| `publications/` avec contenu | A du matériel publiable |
| Dépôt accessible | Harvest peut atteindre le satellite |

---

## Publications liées

| # | Publication | Relation |
|---|-------------|----------|
| 0 | [Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — harvest est un sous-système core |
| 4 | [Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) | Architecture — le système dans lequel harvest opère |
| 4a | [Tableau de bord]({{ '/fr/publications/distributed-knowledge-dashboard/' | relative_url }}) | Sortie — harvest met à jour le tableau de bord |
| 3 | [Persistance de session IA]({{ '/fr/publications/ai-session-persistence/' | relative_url }}) | Fondation — les notes de session sont les données d'entrée de harvest |
| 14 | [Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | Référence core — module K_MIND, architecture mémoire |
| 0v2 | [Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }}) | Architecture — conception multi-module |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
