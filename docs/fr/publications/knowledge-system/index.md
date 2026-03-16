---
layout: publication
title: "Knowledge — Intelligence d'ingénierie IA auto-évolutive"
description: "Publication maître pour packetqc/knowledge : persistance de session, bootstrap portable, flux bidirectionnel de connaissances, auto-guérison consciente des versions, et conscience de soi vivante. Le système qui rend toutes les autres publications possibles — construit en récoltant ses propres enfants."
pub_id: "Publication #0"
version: "v3"
date: "2026-02-24"
permalink: /fr/publications/knowledge-system/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "Knowledge, bootstrap, wakeup, méthodologie, portable, connaissances distribuées"
---

# Knowledge — Intelligence d'ingénierie IA auto-évolutive
{: #pub-title}

**Table des matières**

- [Résumé](#résumé)
- [Hiérarchie des publications](#hiérarchie-des-publications)
- [Contenu du système](#contenu-du-système)
- [Évolution des connaissances](#évolution-des-connaissances)
- [Les enfants](#les-enfants)
- [Annexes](#annexes)

## Résumé

L'ingénierie logicielle avec des assistants IA souffre d'une limitation fondamentale : **l'absence d'état**. Chaque nouvelle session repart de zéro. Quand le travail s'étend sur plusieurs sessions à travers plusieurs projets, l'intelligence accumulée est dispersée et inaccessible.

**Knowledge** (`packetqc/knowledge`) résout ce problème en créant une couche d'intelligence auto-évolutive pour l'ingénierie assistée par IA. **Par conception**, il n'opère que sur les dépôts que l'utilisateur possède et auxquels Claude Code a reçu accès — aucun dépôt externe ou tiers n'est jamais accédé.

| Fonctionnalité | Description |
|----------------|-------------|
| **Persistance de session** | Récupération de contexte en 30 secondes vs 15 minutes manuelles |
| **Bootstrap portable** | Tout projet hérite de la méthodologie, commandes et patterns au démarrage |
| **Flux bidirectionnel** | Les satellites évoluent indépendamment ; harvest ramène les découvertes |
| **Conscient des versions** | 47 versions suivies ; dérive détectée et corrigée automatiquement |
| **Conscient de soi** | Tableau de bord vivant montrant la santé du réseau en temps réel |
| **Pont humain-personne-machine** | GitHub Projects v2 comme suivi style Jira ; GitHub Pages comme documentation style Confluence — 0 $/mois remplace 14,20 $/utilisateur/mois |
| **13 qualités fondamentales** | *Autosuffisant, autonome, concordant, concis, interactif, évolutif, distribué, persistant, récursif, sécuritaire, résilient, structuré, intégré* |
| **Alias d'appel `#`** | Invocation à un seul caractère pour l'entrée de connaissances ciblées avec projet principal implicite et convergence multi-satellite |
| **Compilation de temps** | Chronométrage structuré par tâche : Session active vs Temps calendrier vs Équivalent entreprise, avec graphiques en secteur CSS. Données réelles de Knowledge (historique git) et de l'utilisateur humain (expertise du domaine) — la documentation EST la feuille de temps |

> *« Même le fournisseur Claude Code AI utilise Atlassian Confluence. Pour la gestion de projets répartis entre plusieurs entités et pour la publication web distribuée, j'utilise Knowledge, qui repose sur un abonnement Claude Code AI avec paiement mensuel initial ; GitHub interagit donc avec Knowledge. »*
> — Martin Paquet, architecte de Knowledge

Ceci est la **publication maître** — construite en récoltant ses propres 15 enfants. Les [13 qualités fondamentales]({{ '/fr/publications/knowledge-system/full/#qualites-fondamentales' | relative_url }}) sont l'ADN du système — chacun découvert par la pratique, chacun renforçant les autres.

Le résumé ci-dessus couvre les capacités essentielles ; la documentation complète détaille chaque qualité, chaque mécanisme et chaque cycle de vie du système.

<p style="text-align: right; font-size: 0.78rem;"><a href="{{ '/fr/publications/knowledge-system/full/' | relative_url }}">Lire la documentation complète →</a></p>

## Hiérarchie des publications

Le système de connaissances organise 15 publications dans une hiérarchie parent-enfant. Chaque publication documente une capacité spécifique du réseau.

| # | Publication |
|---|-------------|
| **#0** | [Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) — cette publication |
| **#1** | [MPLIB Storage Pipeline]({{ '/fr/publications/mplib-storage-pipeline/' | relative_url }}) — premier satellite |
| **#2** | [Analyse de session en direct]({{ '/fr/publications/live-session-analysis/' | relative_url }}) — outillage |
| **#3** | [Persistance de session IA]({{ '/fr/publications/ai-session-persistence/' | relative_url }}) — fondation |
| **#4** | [Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) — architecture |
| ↳ **#4a** | [Tableau de bord]({{ '/fr/publications/distributed-knowledge-dashboard/' | relative_url }}) — conscience de soi |
| **#5** | [Webcards et partage social]({{ '/fr/publications/webcards-social-sharing/' | relative_url }}) — identité visuelle |
| **#6** | [Normalize]({{ '/fr/publications/normalize-structure-concordance/' | relative_url }}) — concordance |
| **#7** | [Protocole Harvest]({{ '/fr/publications/harvest-protocol/' | relative_url }}) — guide pratique |
| **#8** | [Gestion de session]({{ '/fr/publications/session-management/' | relative_url }}) — cycle de vie |
| **#9** | [Sécurité par conception]({{ '/fr/publications/security-by-design/' | relative_url }}) — sécurité |
| ↳ **#9a** | [Conformité du cycle de vie des jetons]({{ '/fr/publications/security-by-design/compliance/' | relative_url }}) — conformité |
| **#10** | [Réseau de connaissances live]({{ '/fr/publications/live-knowledge-network/' | relative_url }}) — découverte temps réel |
| **#11** | [Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }}) — validation |
| **#12** | [Gestion de projet]({{ '/fr/publications/project-management/' | relative_url }}) — pont humain-personne-machine |

Chaque publication est née d'un besoin d'ingénierie réel — la hiérarchie reflète comment les capacités ont été découvertes et formalisées.

<p style="text-align: right; font-size: 0.78rem;"><a href="{{ '/fr/publications/knowledge-system/full/#hiérarchie-des-publications' | relative_url }}">Lire la documentation complète →</a></p>

## Contenu du système

Knowledge est organisé en couches, du core stable de méthodologie à la mémoire de session éphémère. Chaque couche sert un rôle différent dans le cycle de vie du système.

| Couche | Contenu | Stabilité |
|--------|---------|-----------|
| **Core** (CLAUDE.md) | Identité, méthodologie, évolution v1–v47, 13 qualités, alias `#` | Stable |
| **Prouvé** (patterns/, lessons/) | 4 patterns, 18 écueils | Validé |
| **Récolté** (minds/) | 24 candidats de 5 satellites | En évolution |
| **Publications** | 15 publications techniques | Versionné |
| **Projets** (projects/) | 9 projets (P0–P9) avec indexation hiérarchique | Structuré |
| **Outillage** (live/, scripts/) | Moteur de capture, beacon, scanner, générateur webcards | Portable |

Les couches collaborent : le core fournit l'identité, les connaissances prouvées fournissent les patterns, les connaissances récoltées fournissent les insights frais, et la mémoire de session assure la continuité.

<p style="text-align: right; font-size: 0.78rem;"><a href="{{ '/fr/publications/knowledge-system/full/#contenu' | relative_url }}">Lire la documentation complète →</a></p>

## Évolution des connaissances

Chaque version représente une découverte architecturale — une nouvelle capacité, un nouvel insight, ou un nouveau mécanisme de propagation. Les versions suivent la conscience, pas les releases.

| v# | Fonctionnalité | Date |
|----|----------------|------|
| v1 | Persistance de session | 2026-02-16 |
| v2 | Analogie Free Guy (lunettes = conscience) | 2026-02-16 |
| v3 | Bootstrap portable | 2026-02-17 |
| v5 | Étape 0 : lunettes d'abord | 2026-02-17 |
| v7 | Normalize (auto-guérison structurelle) | 2026-02-17 |
| v9 | Connaissances distribuées (flux bidirectionnel) | 2026-02-18 |
| v11 | Promotion interactive + healthcheck | 2026-02-18 |
| v12–v17 | Protocole de branches → réalité du proxy | 2026-02-19 |
| v18 | `main` comme point de convergence | 2026-02-19 |
| v20 | Documentation livraison semi-automatique | 2026-02-19 |
| v21 | Portée d'accès — dépôts user-owned seulement | 2026-02-19 |
| v22 | Webcards dual-theme (Cayman + Midnight) | 2026-02-19 |
| v23 | Réseau live + scaffold bootstrap | 2026-02-20 |
| v24 | Commande `refresh` + renommage dashboard | 2026-02-20 |
| v25 | Qualités fondamentales + installation itérative | 2026-02-20 |
| v26 | Alias d'appel `#` + notes projet ciblées + thèmes daltonisme | 2026-02-20 |
| v27 | Protocole de jeton éphémère — accès dépôts privés | 2026-02-21 |
| v28 | Cartographie proxy + contournement API par jeton | 2026-02-21 |
| v29 | Checkpoint/resume — récupération après crash | 2026-02-21 |
| v30 | Protocole d'élévation sécurisé | 2026-02-21 |
| v31 | CLAUDE.md satellite sous-ensemble critique | 2026-02-21 |
| v32 | Commande `recall` + aide contextuelle universelle | 2026-02-21 |
| v33 | Niveaux d'accès PAT — modèle à 4 paliers | 2026-02-21 |
| v34 | Livraison sécurisée par textarea | 2026-02-21 |
| v35 | Projet comme entité de premier ordre — indexation hiérarchique | 2026-02-22 |
| v36 | GitHub helper — outil de secours déployé pour la gestion de PR | 2026-02-22 |
| v37 | Auto-guérison CLAUDE.md satellite — remédiation automatique de dérive | 2026-02-22 |
| v38 | Fusion PR auto-guérison — activation même session | 2026-02-22 |
| v39 | Relais d'évolution — les satellites proposent l'évolution core | 2026-02-22 |
| v40 | Cartographie proxy v2 + tableaux GitHub Project créés | 2026-02-22 |
| v41 | Liaison GitHub Project au dépôt | 2026-02-23 |
| v42 | gh_helper.py comme seule méthode API | 2026-02-23 |
| v43 | Déduplication wakeup — cause racine des crashes API 400 | 2026-02-23 |
| v44 | Convention d'entrée interactive | 2026-02-23 |
| v45 | Correction affichage zéro du jeton | 2026-02-23 |
| v46 | Livraison jeton par environnement + GraphQL | 2026-02-23 |
| v47 | Modèle de déploiement production/développement | 2026-02-23 |

**47 versions en 9 jours.** Le système évolue à la vitesse des projets qu'il dessert.

<p style="text-align: right; font-size: 0.78rem;"><a href="{{ '/fr/publications/knowledge-system/full/#évolution-des-connaissances' | relative_url }}">Lire la documentation complète →</a></p>

---

## Les enfants

Ce système a engendré 15 publications — chacune née d'un besoin d'ingénierie réel, chacune documentant une capacité du réseau de connaissances.

| # | Publication | Rôle |
|---|-------------|------|
| 3 | [Persistance de session IA]({{ '/fr/publications/ai-session-persistence/' | relative_url }}) | **Premier enfant** — la méthodologie fondatrice |
| 1 | [MPLIB Storage Pipeline]({{ '/fr/publications/mplib-storage-pipeline/' | relative_url }}) | Premier satellite — embarqué haute performance |
| 2 | [Analyse de session en direct]({{ '/fr/publications/live-session-analysis/' | relative_url }}) | Outillage — les yeux sur la carte en marche |
| 4 | [Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) | Architecture — intelligence bidirectionnelle |
| 4a | [Tableau de bord]({{ '/fr/publications/distributed-knowledge-dashboard/' | relative_url }}) | Conscience de soi — statut réseau vivant |
| 5 | [Webcards et partage social]({{ '/fr/publications/webcards-social-sharing/' | relative_url }}) | Identité visuelle — aperçus sociaux animés |
| 6 | [Normalize]({{ '/fr/publications/normalize-structure-concordance/' | relative_url }}) | Concordance — auto-guérison structurelle |
| 7 | [Protocole Harvest]({{ '/fr/publications/harvest-protocol/' | relative_url }}) | Guide pratique — collecte distribuée |
| 8 | [Gestion de session]({{ '/fr/publications/session-management/' | relative_url }}) | Cycle de vie — wakeup, save, refresh |
| 9 | [Sécurité par conception]({{ '/fr/publications/security-by-design/' | relative_url }}) | Sécurité — fork & clone sûrs |
| 9a | [Conformité du cycle de vie des jetons]({{ '/fr/publications/security-by-design/compliance/' | relative_url }}) | Conformité — évaluation OWASP, NIST, FIPS |
| 10 | [Réseau de connaissances live]({{ '/fr/publications/live-knowledge-network/' | relative_url }}) | Temps réel — découverte inter-instances |
| 11 | [Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }}) | Validation — capacités démontrées |
| 12 | [Gestion de projet]({{ '/fr/publications/project-management/' | relative_url }}) | Opérations — intégration GitHub Projects |

Chaque enfant renforce le parent : la publication maître (#0) a été construite en récoltant ses propres enfants. Le système se documente lui-même.

## Annexes

| Annexe | Titre | Description |
|--------|-------|-------------|
| 0a | [Optimisation du bootstrap]({{ '/fr/publications/knowledge-system/bootstrap-optimization/' | relative_url }}) | Stratégie de condensation de CLAUDE.md (3872 → 714 lignes, réduction de 81%), carte complète des sections, impact sur le budget de tokens et bonnes pratiques pour maintenir des fichiers bootstrap IA compacts |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
