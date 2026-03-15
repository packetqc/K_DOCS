---
layout: publication
title: "Visualisation de pages web — Pipeline de rendu local"
description: "Un pipeline autonome pour le rendu de pages web et de diagrammes Mermaid en images depuis l'environnement d'un assistant IA. Zéro dépendance externe. Réutilisable en diagnostics interactifs, conception et gestion documentaire."
pub_id: "Publication #16"
version: "v1"
date: "2026-02-26"
permalink: /fr/publications/web-page-visualization/
og_image: /assets/og/web-page-visualization-fr-cayman.gif
keywords: "visualisation web, rendu Mermaid, Playwright, Chromium, diagnostics IA, gestion documentaire, pipeline autonome"
---

# Visualisation de pages web
{: #pub-title}

> **Connexes** : [#13 — Pagination web et exportation]({{ '/fr/publications/web-pagination-export/' | relative_url }})
> | [#15 — Diagrammes d'architecture]({{ '/fr/publications/architecture-diagrams/' | relative_url }})

**Sommaire**

| | |
|---|---|
| [Résumé](#résumé) | Ce que fait cette fonctionnalité et pourquoi c'est important |
| [Architecture](#architecture) | Inventaire des composants et flux de données |
| [Cas d'utilisation](#cas-dutilisation) | Trois domaines de réutilisation |
| [Préservation des sources Mermaid](#préservation-des-sources-mermaid) | Conception du format hybride |
| [Documentation complète](#documentation-complète) | Référence technique complète |

## Public cible

| Audience | Focus |
|----------|-------|
| **Administrateurs réseau/système** | Architecture — conception autonome, zéro appels réseau |
| **Programmeurs/programmeuses** | Patrons de code — Python/Playwright réutilisables |
| **Gestionnaires techniques** | Cas d'utilisation — trois domaines de réutilisation |
| **Ingénieurs documentation** | Préservation des sources + Exclusion pipeline web |

## Résumé

Un **pipeline autonome, zéro dépendance** pour le rendu de pages web et de diagrammes Mermaid en images, directement depuis l'environnement d'un assistant de code IA. Utilise uniquement des outils pré-installés (Python, Playwright, Chromium) et un paquet npm local (mermaid.js) — aucun service externe, aucun appel CDN au moment du rendu.

La fonctionnalité a émergé d'un besoin diagnostique (Issue #334) et s'est révélée immédiatement réutilisable dans trois domaines :

1. **Diagnostics interactifs** — Claude rend la page, identifie les problèmes, propose des correctifs
2. **Conception interactive** — Validation visuelle pendant la construction itérative de pages web
3. **Gestion documentaire** — Captures d'écran pour les publications, images de diagrammes pour les pipelines d'exportation

## Architecture

```
urllib (récupérer HTML) → HTML autonome → Playwright + Chromium → npm mermaid → captures
```

| Composant | Rôle | Externe? |
|-----------|------|----------|
| **urllib** | Récupérer le HTML de la page | Non — contourne le proxy |
| **Playwright** | Automatisation de navigateur headless | Non — pré-installé |
| **Chromium** | Moteur de rendu DOM complet | Non — binaire pré-installé |
| **npm mermaid** | Code Mermaid → SVG | Non — paquet npm local |

**Zéro appels réseau au moment du rendu.** urllib contourne le proxy du conteneur via des connexions socket directes — le même mécanisme que `gh_helper.py` utilise pour les appels API GitHub.

## Cas d'utilisation

### 1. Diagnostics interactifs

Claude rend la page, voit le résultat réel et diagnostique les problèmes de rendu — le tout dans une même session. Validation réelle : Issue #334, 14 diagrammes Mermaid sur la page FR Architecture Diagrams, l'utilisateur a confirmé : *« ça semble fonctionner le visual d'une page web »*.

### 2. Conception interactive

Pendant la construction itérative de pages web, Claude rend l'état courant pour valider la mise en page, le style et les miroirs bilingues — sans que l'utilisateur ait besoin de rafraîchir son navigateur.

### 3. Gestion documentaire

Génération d'artefacts visuels : captures d'écran pour les publications, Mermaid-vers-PNG pour l'exportation DOCX (Mermaid.js n'est pas supporté dans Word), rapports de validation visuelle pour `pub check` et `docs check`.

## Préservation des sources Mermaid

Lorsque les diagrammes sont pré-rendus en PNG, le code source Mermaid original est préservé dans des sections repliables `<details class="mermaid-source">` — visibles dans la vue source GitHub, masquées sur les pages web. Cela résout le problème de l'œuf et la poule : la source qui génère le diagramme voyage avec le résultat rendu.

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="diagram-midnight.png">
  <img src="diagram-cayman.png" alt="Diagramme">
</picture>

<details class="mermaid-source">
<summary>Source Mermaid</summary>
...
</details>
```

La classe `.mermaid-source` déclenche le masquage CSS + l'exclusion JS dans les deux layouts — empêchant mermaid.js de double-rendre les blocs sources préservés.

## Documentation complète

[Toutes les sections avec les patrons de code, les résultats de validation et l'analyse de sécurité sont documentées dans la]({{ '/fr/publications/web-page-visualization/full/' | relative_url }}) **version complète**.
