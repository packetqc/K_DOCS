---
layout: publication
title: "Sécurité par conception — Architecture de connaissances IA limitée au propriétaire"
description: "Modèle de sécurité pour les dépôts publics de connaissances IA : zéro identifiants stockés, accès en écriture limité par proxy, opérations limitées à l'espace de noms du propriétaire, isolation environnementale et livraison via PR. Modèle de menaces et méthodologie d'audit."
pub_id: "Publication #9"
version: "v3"
date: "2026-03-16"
permalink: /fr/publications/security-by-design/
og_image: /assets/og/security-by-design-fr-cayman.gif
keywords: "sécurité, PQC, contrôle d'accès, fork sûr, confidentialité, portée propriétaire"
---

# Sécurité par conception — Architecture de connaissances IA limitée au propriétaire
{: #pub-title}

> **Publication parente** : [#0 — Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Référence core** : [#14 — Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Vue d'ensemble et architecture sûre publiquement |
| [La question de sécurité](#la-question-de-sécurité) | Pourquoi les dépôts publics nécessitent une sécurité architecturale |
| [Modèle de menaces](#modèle-de-menaces) | Menaces traitées et protections en place |
| [Couches de sécurité](#couches-de-sécurité) | Architecture de défense à sept couches |
| [Audit des identifiants](#audit-des-identifiants) | Résultats de scan complet sur toutes les branches |
| [Sécurité : Fork & Clone](#sécurité--fork--clone) | Garanties pour le fork et clone publics |
| [Niveaux d'accès PAT](#niveaux-daccès-pat) | Niveaux de configuration des jetons et portées |
| [Sécurité du cycle de vie du jeton](#sécurité-du-cycle-de-vie-du-jeton) | Gestion éphémère du jeton de la réception à l'élimination |
| [Principes de conception](#principes-de-conception) | Principes fondamentaux de conception sécuritaire |

## Résumé

Les systèmes de développement assistés par IA qui persistent les connaissances entre sessions et projets font face à une question de sécurité fondamentale : **que se passe-t-il quand le dépôt devient public ?**

Knowledge est conçu dès le départ pour être **sûr publiquement et limité au propriétaire**. Chaque composant opère dans des frontières de sécurité qui rendent le dépôt sûr à forker, cloner et publier :

| Protection | Description |
|------------|-------------|
| **Zéro identifiants stockés** | Aucune clé API, jeton, mot de passe ou certificat dans les fichiers ou l'historique git |
| **Accès en écriture limité par proxy** | Les sessions ne peuvent pousser que vers leur branche assignée dans leur dépôt assigné |
| **Opérations limitées à l'espace de noms** | Toutes les URLs référencent l'espace de noms GitHub du propriétaire |
| **Isolation environnementale** | Fichiers de session, références satellites et `far_memory archives/` sont par propriétaire |
| **Livraison via PR** | Aucune écriture directe aux branches partagées |

## La question de sécurité

Quand un système de développement assisté par IA persiste les connaissances et que ce système vit dans un dépôt git, le rendre public soulève des préoccupations légitimes : fuite d'identifiants, compromission de comptes, contamination croisée entre forkeur et propriétaire, exposition de données et escalade de privilèges.

Knowledge répond à chacune par **conception architecturale** — pas par nettoyage après coup, mais par des décisions qui rendent le stockage d'identifiants inutile et les opérations inter-propriétaires impossibles.

## Modèle de menaces

| Menace | Protection |
|--------|-----------|
| **Vol d'identifiants** | Aucun identifiant stocké — `.gitignore` bloque les patrons sensibles, audit confirme zéro correspondance |
| **Détournement de session** | Les URLs de session expirent ; seulement dans les métadonnées de commit, jamais dans le contenu |
| **Prise de contrôle du dépôt** | Le proxy limite le push à la branche assignée — cross-repo retourne 403 |
| **Infiltration satellite** | La synchronisation K_GITHUB utilise le HTTPS public uniquement — les dépôts privés retournent 403/404 |
| **Exfiltration de données** | `far_memory archives/` ne contient que des métadonnées — aucun code source, aucun identifiant |

## Couches de sécurité

Sept couches de protection indépendantes :

| Couche | Protection | Description |
|--------|------------|-------------|
| 1 | **`.gitignore`** | Bloque `.env`, `.pem`, `.key`, `.p12`, `credentials.*`, `secrets.*` |
| 2 | **Architecture zéro-identifiant** | HTTPS public pour lectures, proxy pour auth — aucun jeton dans le dépôt |
| 3 | **Portée du proxy** | Push vers la branche `claude/<task-id>` assignée uniquement, dépôt courant uniquement |
| 4 | **Livraison via PR** | Tout changement vers `main` requiert l'approbation du propriétaire |
| 5 | **Espace de noms du propriétaire** | Les URLs utilisent `packetqc/<repo>` — le forkeur change l'espace de noms |
| 6 | **Isolation environnementale** | `sessions/`, `far_memory archives/`, tableau de bord sont par propriétaire |
| 7 | **Audit continu** | K_VALIDATION et la synchronisation K_GITHUB incluent des vérifications de sécurité |

## Audit des identifiants

Scan complet à travers toutes les branches :

| Catégorie | Patrons | Résultat |
|----------|----------|--------|
| Jetons GitHub | `ghp_`, `gho_`, `github_pat_` | **Aucun trouvé** |
| Clés API | `sk-`, `sk-ant-`, `AKIA` | **Aucun trouvé** |
| Clés privées | `BEGIN PRIVATE KEY`, `BEGIN RSA` | **Aucun trouvé** |
| Mots de passe | `password=`, `secret=` avec valeurs | **Aucun trouvé** |
| En-têtes d'auth | `Bearer`, `Basic` avec valeurs | **Aucun trouvé** |
| URLs avec identifiants | `://user:pass@host` | **Aucun trouvé** |

## Sécurité : Fork & Clone

**Ce qu'un forkeur obtient** : méthodologie, publications, outillage, données de profil publiées — tout intentionnellement public. Aucun accès aux comptes, aucun identifiant, aucune surface d'attaque.

**Ce qu'un forkeur ne peut pas faire** : pousser vers le dépôt original, accéder aux dépôts privés, compromettre des comptes, modifier les satellites.

**Ce qu'un forkeur change** : remplacer `packetqc` par son nom d'utilisateur GitHub dans CLAUDE.md et mind_memory.md. Le reste s'adapte automatiquement.

## Niveaux d'accès PAT

4 niveaux progressifs de configuration PAT GitHub, du moins au plus privilégié :

| Niveau | Configuration | Active | Mode |
|--------|--------------|--------|------|
| **0** | Sans PAT (proxy seul) | Dépôts publics, push branche assignée, PR manuels | Semi-automatique |
| **1** | Fine-grained lecture seule | + clone/fetch dépôts privés pour harvest | Semi-auto + visibilité privée |
| **2** | Fine-grained lecture-écriture | + création/fusion PR via API + tableaux GitHub Project (autonome complet) | **Recommandé** |
| **3** | PAT classique `repo` | Tout — mais viole le moindre privilège | Non recommandé |

**Niveau 2 minimum confirmé** (validé 2026-02-21 — PR #137 cycle complet) : Seulement **4 permissions** requises : `Contents: RW` + `Pull requests: RW` + `Projects: RW` + `Metadata: Read` (obligatoire, auto-incluse). Issues, Actions, Webhooks, Pages, Administration — aucune nécessaire pour l'autonomie.

Chaque niveau correspond à une découverte architecturale : N0=v17 proxy, N1=v27 jeton éphémère, N2=v28 contournement API, N3=excès classique.

## Sécurité du cycle de vie du jeton

Le jeton traverse 5 phases — réception, persistance en mémoire, utilisation, élimination, vérification post-session. Chaque phase est alignée sur les standards industriels (OWASP Secrets Management, OWASP MCP01:2025, NIST SP 800-63B, FIPS 140-3, CIS Controls). OWASP MCP01:2025 classe la mauvaise gestion des jetons comme le **risque #1** pour les outils de développement IA — notre architecture éphémère par conception répond directement à ce risque.

**Réception** : Coller (recommandé, aucune E/S fichier) ou Enveloppe PQC (chiffrée en transit) ou téléversement d'image (repli, fichier temporaire supprimé immédiatement).

**En mémoire** : Le jeton n'est PAS chiffré en RAM — conforme à la pratique industrielle. Le chiffrement en mémoire sans support matériel (HSM/TPM) est du théâtre sécuritaire. **Futur** : le projet knowledge-live PQC vise le stockage de clés supporté par matériel (STM32 élément sécurisé).

**Élimination** : Fenêtre de contexte détruite à la fin de session. Matériel de clé zéro-écrasé. **Lacune** : Les chaînes Python ne sont pas zéro-écrasées avant le GC — correctif prévu via `ctypes.memset()`.

**Conformité** : OWASP ✅ | NIST SP 800-63B ✅ | NIST SP 800-88 ⚠️ (clés oui, jeton en attente) | CIS 3.10 ✅

## Principes de conception

| Principe | Description |
|----------|-------------|
| **Les identifiants sont inutiles, pas nettoyés** | L'architecture ne requiert jamais de stocker des identifiants |
| **L'espace de noms est la frontière** | La sécurité vient du confinement au propriétaire, pas des secrets |
| **Public par défaut** | Les données privées restent dans l'environnement local, jamais dans le dépôt |
| **Défense en profondeur** | Sept couches indépendantes |
| **Audit-friendly** | Vérifiable avec les outils git standard et le scan regex |
| **Fork-friendly** | Conçu pour être forké. Méthodologie et outillage, pas accès |

---

[**Lire la documentation complète →**]({{ '/fr/publications/security-by-design/full/' | relative_url }}) | [**Rapport de conformité →**]({{ '/fr/publications/security-by-design/compliance/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
