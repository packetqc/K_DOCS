---
layout: default
title: "Knowledge — Projets"
description: "Vue par projet de l'écosystème Knowledge. Projet central, projets enfants, dépôts satellites et leurs publications — organisés par hiérarchie de projet avec liens à double origine."
permalink: /fr/projects/
og_image: /assets/og/knowledge-system-fr-cayman.gif
project_boards: true
---

# Projets

L'écosystème Knowledge organisé par **hiérarchie de projet**. Chaque projet est une entité de premier ordre avec sa propre identité, ses publications, ses satellites, son évolution et ses histoires.

*Par Martin Paquet & Claude (Anthropic, Opus 4.6)*

**Navigation** : [Publications (liste plate)]({{ '/fr/publications/' | relative_url }}) | **Projets (par hiérarchie)** | [Profil]({{ '/fr/profile/' | relative_url }})

**Table des matières**

- [Registre des projets](#registre-des-projets)
- [Convention d'origine des liens](#convention-dorigine-des-liens)
- [P0 — Knowledge](#p0--knowledge)
- [P1 — MPLIB](#p1--mplib)
- [P2 — STM32 PoC](#p2--stm32-poc)
- [P3 — knowledge-live](#p3--knowledge-live)
- [P4 — MPLIB Dev Staging](#p4--mplib-dev-staging)
- [P5 — PQC](#p5--pqc)
- [P6 — Export Documentation](#p6--export-documentation)
- [P8 — Système de documentation](#p8--système-de-documentation)
- [P9 — Rapport de conformité](#p9--rapport-de-conformité)
- [P13 — Studio 54](#p13--studio-54)

---

## Registre des projets

| ID | Projet | Type | Statut | Satellites | Publications |
|----|--------|------|--------|------------|--------------|
| P0 | [Knowledge](#p0--knowledge) | central | 🟢 actif | 5 | 15 |
| P1 | [MPLIB](#p1--mplib) | enfant | 🟢 actif | 2 | 1 |
| P2 | [STM32 PoC](#p2--stm32-poc) | enfant | 🟢 actif | 1 | 1 |
| P3 | [knowledge-live](#p3--knowledge-live) | enfant | 🟢 actif | 1 | 1 |
| P4 | [MPLIB Dev Staging](#p4--mplib-dev-staging) | enfant | 🟢 actif | 1 | 0 |
| P5 | [PQC](#p5--pqc) | enfant | 🔴 pré-bootstrap | 1 | 0 |
| P6 | [Export Documentation](#p6--export-documentation) | géré | 🟢 actif | 0 | 0 |
| P8 | [Système de documentation](#p8--système-de-documentation) | géré | 🟢 actif | 0 | 0 |
| P9 | [Rapport de conformité](#p9--rapport-de-conformité) | géré | 🟢 actif | 0 | 1 |
| P13 | [Studio 54](#p13--studio-54) | géré | 🟢 actif | 0 | 0 |

---

## Convention d'origine des liens

Les publications et la documentation existent dans plusieurs dépôts, chacun avec son propre site GitHub Pages. L'origine du lien indique la provenance :

| Origine | Signification | URL de base | Badge |
|---------|--------------|-------------|-------|
| **Central** | Révisé, publié, canonique | `packetqc.github.io/knowledge/` | **central** |
| **Satellite** | Développement, staging, docs locaux | `packetqc.github.io/<dépôt>/` | *satellite* |

Les publications centrales sont les versions approuvées et révisées. Les publications satellites sont des documents de travail qui peuvent évoluer indépendamment. Les deux sont accessibles via GitHub Pages — origine différente, même technologie.

---

## P0 — Knowledge

**Type** : central | **Statut** : 🟢 actif | **Dépôt** : [packetqc/knowledge](https://github.com/packetqc/knowledge) | **Board** : [#4](https://github.com/users/packetqc/projects/4)

Le projet maître — méthodologie, publications, réseau distribué, intelligence auto-évolutive.

### Tableau de projet

[GitHub Project Board #4 →](https://github.com/users/packetqc/projects/4) — Feuille de route, travail en cours, fonctionnalités planifiées et prévisions.

Voir aussi : [Plan général]({{ '/fr/plan/' | relative_url }}) (widgets de tableau de bord avec filtres par statut)

<div class="project-board-widget" data-board-number="4"></div>

### Publications centrales (P0)

| Index | # | Titre | Origine | Lien |
|-------|---|-------|---------|------|
| P0/#0 | 0 | Knowledge | **central** | [Lire →]({{ '/fr/publications/knowledge-system/' | relative_url }}) |
| P0/#1 | 1 | Pipeline de stockage MPLIB | **central** →P1 | [Lire →]({{ '/fr/publications/mplib-storage-pipeline/' | relative_url }}) |
| P0/#2 | 2 | Analyse de session live | **central** | [Lire →]({{ '/fr/publications/live-session-analysis/' | relative_url }}) |
| P0/#3 | 3 | Persistance de session IA | **central** | [Lire →]({{ '/fr/publications/ai-session-persistence/' | relative_url }}) |
| P0/#4 | 4 | Esprits distribués | **central** | [Lire →]({{ '/fr/publications/distributed-minds/' | relative_url }}) |
| P0/#4a | 4a | Tableau de bord | **central** | [Lire →]({{ '/fr/publications/distributed-knowledge-dashboard/' | relative_url }}) |
| P0/#5 | 5 | Webcards et partage social | **central** | [Lire →]({{ '/fr/publications/webcards-social-sharing/' | relative_url }}) |
| P0/#6 | 6 | Normalize et concordance | **central** | [Lire →]({{ '/fr/publications/normalize-structure-concordance/' | relative_url }}) |
| P0/#7 | 7 | Protocole Harvest | **central** | [Lire →]({{ '/fr/publications/harvest-protocol/' | relative_url }}) |
| P0/#8 | 8 | Gestion de session | **central** | [Lire →]({{ '/fr/publications/session-management/' | relative_url }}) |
| P0/#9 | 9 | Sécurité par conception | **central** | [Lire →]({{ '/fr/publications/security-by-design/' | relative_url }}) |
| P0/#9a | 9a | Conformité du cycle de vie des jetons | **central** | [Lire →]({{ '/fr/publications/security-by-design/compliance/' | relative_url }}) |
| P0/#10 | 10 | Réseau de connaissances live | **central** →P3 | [Lire →]({{ '/fr/publications/live-knowledge-network/' | relative_url }}) |
| P0/#11 | 11 | Histoires de succès | **central** | [Lire →]({{ '/fr/publications/success-stories/' | relative_url }}) |
| P0/#12 | 12 | Gestion de projet | **central** | [Lire →]({{ '/fr/publications/project-management/' | relative_url }}) |

### Projets enfants

| ID | Projet | Statut | Satellites |
|----|--------|--------|------------|
| P1 | [MPLIB](#p1--mplib) | 🟢 actif | 2 dépôts |
| P2 | [STM32 PoC](#p2--stm32-poc) | 🟢 actif | 1 dépôt |
| P3 | [knowledge-live](#p3--knowledge-live) | 🟢 actif | 1 dépôt |
| P4 | [MPLIB Dev Staging](#p4--mplib-dev-staging) | 🟢 actif | 1 dépôt |
| P5 | [PQC](#p5--pqc) | 🔴 pré-bootstrap | 1 dépôt |

---

## P1 — MPLIB

**Type** : enfant de P0 | **Statut** : 🟢 actif | **Dépôt** : [packetqc/MPLIB](https://github.com/packetqc/MPLIB) | **Board** : [#5](https://github.com/users/packetqc/projects/5)

Bibliothèque de systèmes embarqués haute performance — ingestion de logs SQLite sur ARM Cortex-M55, ThreadX RTOS, TouchGFX UI. La preuve de concept originale qui a validé Knowledge.

### Tableau de projet

[GitHub Project Board #5 →](https://github.com/users/packetqc/projects/5)

<div class="project-board-widget" data-board-number="5"></div>

### Publications

| Index | Titre | Origine | Lien |
|-------|-------|---------|------|
| P0/#1 | Pipeline de stockage MPLIB | **central** | [Lire →]({{ '/fr/publications/mplib-storage-pipeline/' | relative_url }}) |
| P1/S1/D1 | X | *satellite* | X |

### Satellites

| Index | Dépôt | Version | Santé |
|-------|-------|---------|-------|
| P1/S1 | [packetqc/MPLIB](https://github.com/packetqc/MPLIB) | v31 | 🟢 |
| P1/S2 | [packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE](https://github.com/packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE) | v31 | 🟢 |

---

## P2 — STM32 PoC

**Type** : enfant de P0 | **Statut** : 🟢 actif | **Dépôt** : [packetqc/STM32N6570-DK_SQLITE](https://github.com/packetqc/STM32N6570-DK_SQLITE) | **Board** : [#6](https://github.com/users/packetqc/projects/6)

Preuve de concept matérielle pour la bibliothèque MPLIB sur STM32N6570-DK (Cortex-M55 @ 800 MHz).

### Tableau de projet

[GitHub Project Board #6 →](https://github.com/users/packetqc/projects/6)

<div class="project-board-widget" data-board-number="6"></div>

### Publications

| Index | Titre | Origine | Lien |
|-------|-------|---------|------|
| P0/#1 | Pipeline de stockage MPLIB | **central** (partagé avec P1) | [Lire →]({{ '/fr/publications/mplib-storage-pipeline/' | relative_url }}) |
| P2/S1/D1 | doc/readme.md | *satellite* | X |

### Satellites

| Index | Dépôt | Version | Santé |
|-------|-------|---------|-------|
| P2/S1 | [packetqc/STM32N6570-DK_SQLITE](https://github.com/packetqc/STM32N6570-DK_SQLITE) | v31 | 🟢 |

---

## P3 — knowledge-live

**Type** : enfant de P0 | **Statut** : 🟢 actif | **Dépôt** : [packetqc/knowledge-live](https://github.com/packetqc/knowledge-live) | **Board** : [#37](https://github.com/users/packetqc/projects/37)

Découverte et communication inter-instances sécurisées PQC. Premier satellite bootstrappé avec scaffold autonome (v23). Protocole beacon/scanner porté depuis la découverte réseau embarquée STM32H5/N6.

### Tableau de projet

[GitHub Project Board #37 →](https://github.com/users/packetqc/projects/37)

<div class="project-board-widget" data-board-number="37"></div>

### Publications

| Index | Titre | Origine | Lien |
|-------|-------|---------|------|
| P0/#10 | Réseau de connaissances live | **central** | [Lire →]({{ '/fr/publications/live-knowledge-network/' | relative_url }}) |

### Satellites

| Index | Dépôt | Version | Santé |
|-------|-------|---------|-------|
| P3/S1 | [packetqc/knowledge-live](https://github.com/packetqc/knowledge-live) | v31 | 🟢 |

---

## P4 — MPLIB Dev Staging

**Type** : enfant de P1 | **Statut** : 🟢 actif | **Dépôt** : [packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE](https://github.com/packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE) | **Board** : [#8](https://github.com/users/packetqc/projects/8)

Environnement de développement et staging pour MPLIB. Où le protocole de staging itératif (v25) a été validé. Satellite le plus actif par nombre de sessions.

### Tableau de projet

[GitHub Project Board #8 →](https://github.com/users/packetqc/projects/8)

<div class="project-board-widget" data-board-number="8"></div>

### Satellites

| Index | Dépôt | Version | Santé |
|-------|-------|---------|-------|
| P4/S1 | [packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE](https://github.com/packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE) | v31 | 🟢 |

---

## P5 — PQC

**Type** : enfant de P0 | **Statut** : 🔴 pré-bootstrap | **Dépôt** : [packetqc/PQC](https://github.com/packetqc/PQC) | **Board** : [#9](https://github.com/users/packetqc/projects/9)

Dépôt de référence de cryptographie post-quantique. Pas encore intégré à Knowledge.

### Tableau de projet

[GitHub Project Board #9 →](https://github.com/users/packetqc/projects/9)

<div class="project-board-widget" data-board-number="9"></div>

### Satellites

| Index | Dépôt | Version | Santé |
|-------|-------|---------|-------|
| P5/S1 | [packetqc/PQC](https://github.com/packetqc/PQC) | v0 | 🔴 47 versions de retard |

### Remédiation

Ouvrir une session Claude Code dans le dépôt PQC → `wakeup` → le scaffold bootstrap s'active → fusionner le PR.

---

## P6 — Export Documentation

**Type** : géré (dans P3) | **Statut** : 🟢 actif | **Dépôt hôte** : [packetqc/knowledge-live](https://github.com/packetqc/knowledge-live) | **Board** : [#10](https://github.com/users/packetqc/projects/10)

Projet de documentation et gestion de publications multi-usages hébergé dans knowledge-live.

<div class="project-board-widget" data-board-number="10"></div>

---

## P8 — Système de documentation

**Type** : géré (dans P0) | **Statut** : 🟢 actif | **Dépôt hôte** : [packetqc/knowledge](https://github.com/packetqc/knowledge) | **Board** : [#38](https://github.com/users/packetqc/projects/38)

Système de documentation Knowledge — pipeline de publication, révision de docs et gestion de contenu.

<div class="project-board-widget" data-board-number="38"></div>

---

## P9 — Rapport de conformité

**Type** : géré (dans P0) | **Statut** : 🟢 actif | **Dépôt hôte** : [packetqc/knowledge](https://github.com/packetqc/knowledge) | **Board** : [#43](https://github.com/users/packetqc/projects/43)

Évaluation de conformité de la gestion éphémère des jetons Knowledge contre OWASP MCP01:2025, NIST SP 800-63B, FIPS 140-3 et CIS Controls v8. Suit 28 points de contrôle de conformité et 7 éléments de feuille de route à travers 5 phases du cycle de vie.

<div class="project-board-widget" data-board-number="43"></div>

### Publications

| Index | Titre | Origine | Lien |
|-------|-------|---------|------|
| P0/#9a | Conformité du cycle de vie des jetons | **central** | [Lire →]({{ '/fr/publications/security-by-design/compliance/' | relative_url }}) |

---

## P13 — Studio 54

**Type** : géré (dans P0) | **Statut** : 🟢 actif | **Dépôt hôte** : [packetqc/knowledge](https://github.com/packetqc/knowledge) | **Board** : [#50](https://github.com/users/packetqc/projects/50)

Projet Studio 54. Géré au sein du dépôt central Knowledge.

<div class="project-board-widget" data-board-number="50"></div>

---

## À propos

Cette page fournit une **navigation par projet** au-dessus de l'[index des publications]({{ '/fr/publications/' | relative_url }}) existant. Aucune URL existante n'a été modifiée — c'est une vue additive.

| | |
|---|---|
| **Base de connaissances** | [packetqc/knowledge](https://github.com/packetqc/knowledge) |
| **Publications (liste plate)** | [Toutes les publications →]({{ '/fr/publications/' | relative_url }}) |
| **Auteur** | [Martin Paquet →]({{ '/fr/profile/' | relative_url }}) |
| **Contact** | packetqcca@gmail.com |

---

*Modèle d'entité projet introduit dans Knowledge v35 (février 2026).*
*© 2026 Martin Paquet & Claude (Anthropic)*
