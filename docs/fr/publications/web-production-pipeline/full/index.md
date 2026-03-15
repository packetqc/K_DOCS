---
layout: publication
title: "Pipeline de production web — Complet"
description: "Référence complète du pipeline de production web Knowledge : rédaction source, structure à trois niveaux, miroirs bilingues, contrat front matter, traitement Jekyll (Liquid + kramdown), système de mise en page, CSS 4 thèmes, pipeline d'assets, mécanismes d'exclusion, déploiement, commandes et pièges connus."
pub_id: "Publication #17 — Complet"
version: "v1"
date: "2026-02-26"
permalink: /fr/publications/web-production-pipeline/full/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "pipeline, jekyll, kramdown, production, web, deploiement, exclusion"
---

# Pipeline de production web — Documentation complète
{: #pub-title}

> **Résumé** : [Publication #17]({{ '/fr/publications/web-production-pipeline/' | relative_url }}) | **Parent** : [#0 — Système de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Vue d'ensemble](#vue-densemble-du-pipeline) | Flux de bout en bout |
| [1. Rédaction source](#1-redaction-source) | Écriture du document markdown canonique |
| [2. Structure à trois niveaux](#2-structure-de-publication-a-trois-niveaux) | Source → Résumé → Complet |
| [3. Miroirs bilingues](#3-systeme-de-miroirs-bilingues) | Architecture parallèle EN/FR |
| [4. Contrat front matter](#4-contrat-front-matter) | Métadonnées YAML requises |
| [5. Traitement Jekyll](#5-traitement-jekyll) | Liquid → kramdown → HTML |
| [6. Système de mise en page](#6-systeme-de-mise-en-page) | publication.html vs default.html |
| [7. Système de thèmes](#7-systeme-de-themes) | CSS 4 thèmes avec détection automatique |
| [8. Pipeline d'assets](#8-pipeline-dassets) | Webcards, diagrammes, images, médias |
| [9. Mécanismes d'exclusion](#9-mecanismes-dexclusion) | Ce qui est filtré, masqué ou transformé |
| [10. Déploiement](#10-deploiement) | Construction automatique GitHub Pages |
| [11. Commandes pipeline](#11-commandes-pipeline) | pub, docs, webcard, normalize |
| [12. Pièges connus](#12-pieges-connus) | Particularités kramdown, limites proxy, pièges de rendu |
| [Diagramme du pipeline](#diagramme-du-pipeline) | Flux visuel du pipeline complet |

---

## Vue d'ensemble du pipeline

```
Markdown source (l'auteur écrit une seule fois)
    ↓ pub new (création du squelette)
Division à trois niveaux (source → résumé → complet)
    ↓ injection du front matter
Miroirs bilingues (EN + FR pour chaque niveau web)
    ↓ traitement Jekyll
Templates Liquid → kramdown → HTML
    ↓ enveloppement par la mise en page
publication.html ou default.html
    ↓ améliorations côté client
Mermaid, thèmes, références croisées, export
    ↓ déploiement GitHub Pages
Page web en ligne (double thème, bilingue, exportable)
```

**Principe clé** : Le document source est écrit une seule fois. Tout ce qui suit est dérivé. Le pipeline est déterministe.

---

## 1. Rédaction source

Chaque publication commence par un seul fichier markdown :

```
publications/<slug>/v1/README.md
```

C'est la **source canonique** — l'unique source de vérité. Toutes les pages web en sont dérivées. La source est uniquement en anglais (les traductions françaises sont créées lors de la division à trois niveaux).

**Structure source** :

```
publications/<slug>/v1/
  README.md              ← document canonique
  assets/                ← assets statiques (diagrammes, images)
  media/                 ← assets dynamiques (vidéo, captures)
```

**Règles de rédaction** :
- Markdown standard GitHub-Flavored (GFM)
- Diagrammes Mermaid en blocs de code délimités
- Pas de balises Liquid dans la source (source indépendante de la plateforme)
- Pas de front matter dans la source (ajouté aux niveaux web)
- Liens internes en chemins relatifs

Le fichier source est lisible directement sur GitHub. C'est aussi l'entrée de `pub sync` qui propage les changements aux niveaux web.

---

## 2. Structure de publication à trois niveaux

Chaque publication existe à trois niveaux :

| Niveau | Emplacement | Objectif | Contenu |
|--------|-------------|----------|---------|
| **Source** | `publications/<slug>/v1/README.md` | Document canonique, versionné | Contenu complet, anglais uniquement |
| **Résumé** | `docs/publications/<slug>/index.md` | Point d'entrée web | Résumé, points clés, lien vers complet |
| **Complet** | `docs/publications/<slug>/full/index.md` | Documentation web complète | Contenu complet rendu sur GitHub Pages |

**Arborescence pour une publication** (bilingue) :

```
publications/<slug>/v1/
  README.md                                    ← Source (EN uniquement)

docs/publications/<slug>/
  index.md                                     ← Résumé EN
  full/
    index.md                                   ← Complet EN

docs/fr/publications/<slug>/
  index.md                                     ← Résumé FR
  full/
    index.md                                   ← Complet FR
```

**Total : 5 fichiers par publication** (1 source + 4 pages web).

**Règles de liaisons croisées** :
- Les résumés renvoient vers leur page complète dans la même langue
- Les pages complètes renvoient vers leur résumé
- Les pages EN renvoient vers les miroirs FR et vice versa
- Tous les liens internes utilisent le filtre `relative_url` de Jekyll

---

## 3. Système de miroirs bilingues

Chaque page web (résumé et complet) existe en deux langues. Les pages EN et FR sont des miroirs structurels — mêmes sections, même ordre, mêmes assets, langue différente.

**Convention de chemins** :

| Langue | Modèle de chemin |
|--------|-----------------|
| Anglais | `docs/publications/<slug>/` |
| Français | `docs/fr/publications/<slug>/` |

**Ce qui diffère entre miroirs** :

| Élément | EN | FR |
|---------|----|----|
| `title` | Titre anglais | Titre français |
| `description` | Description anglaise | Description française |
| `permalink` | `/publications/<slug>/` | `/fr/publications/<slug>/` |
| `og_image` | `<carte>-en-cayman.gif` | `<carte>-fr-cayman.gif` |
| Texte du corps | Anglais | Français |
| Barre de langue | Anglais principal | Français principal |

**Ce qui reste identique** : `layout`, `pub_id`, `version`, `date`, structure du document, diagrammes Mermaid, structures de tableaux, références d'assets.

---

## 4. Contrat front matter

Chaque page web dans `docs/` doit inclure un front matter YAML.

**Champs requis** (toutes les pages) :

| Champ | Objectif | Exemple |
|-------|----------|---------|
| `layout` | Modèle de mise en page | `publication` ou `default` |
| `title` | Titre de la page, titre OG | `"Pipeline de production web"` |
| `description` | Méta description, description OG | `"Pipeline complet..."` |
| `permalink` | Chemin URL, barre de langue | `/fr/publications/web-production-pipeline/` |
| `og_image` | Webcard, aperçu social | `/assets/og/knowledge-system-fr-cayman.gif` |

**Champs additionnels** (pages de publication) :

| Champ | Objectif | Exemple |
|-------|----------|---------|
| `pub_id` | Affichage bannière de version | `"Publication #17"` |
| `version` | Bannière de version, nom PDF | `"v1"` |
| `date` | Bannière de version, fraîcheur | `"2026-02-26"` |
| `keywords` | Injection de références croisées | `"pipeline, jekyll, kramdown"` |

---

## 5. Traitement Jekyll

GitHub Pages utilise Jekyll pour transformer le markdown en HTML. Le traitement se fait en trois passes ordonnées.

### Passe 1 : Traitement des templates Liquid

Le moteur Liquid de Jekyll s'exécute **en premier**, avant tout traitement markdown.

**Ce que Liquid gère** :
{% raw %}
- `{{ variable }}` — interpolation de variables
- `{% if condition %}` — blocs conditionnels
- `{{ '/chemin/' | relative_url }}` — filtres URL (ajoute le baseurl `/knowledge/`)

**Règle critique** : Liquid traite TOUS les motifs `{{ }}` — y compris ceux dans les blocs de code markdown. Les diagrammes Mermaid avec la notation `{{` (hexagones) voient leur contenu **supprimé** par Liquid avant que kramdown ne les voie.
{% endraw %}

### Passe 2 : kramdown Markdown → HTML

| Paramètre | Valeur | Effet |
|-----------|--------|-------|
| `markdown` | `kramdown` | Moteur markdown |
| `kramdown.input` | `GFM` | Dialecte GitHub-Flavored |
| `kramdown.parse_block_html` | `true` | Les blocs HTML bruts passent |

`parse_block_html: true` est essentiel pour les éléments `<picture>`, `<source>`, `<div>`. Cependant, les lignes vides dans les blocs HTML font que kramdown revient en mode markdown.

### Passe 3 : Enveloppement par la mise en page

Le HTML résultant est injecté dans la mise en page spécifiée par `layout:` dans le front matter.

---

## 6. Système de mise en page

### publication.html — Pile complète de publication

| Fonctionnalité | Description |
|----------------|-------------|
| Bannière de version | `pub_id` + `version` + `date` + horodatage + auteurs |
| Barre de langue | Bascule EN↔FR auto-générée depuis le permalink |
| Barre d'export | Boutons PDF (Letter/Legal) + DOCX |
| `printAs()` | PDF natif navigateur via `window.print()` + CSS Paged Media |
| CSS `@page` | En-têtes courants, pieds de page à trois colonnes, page de couverture |
| Rendu Mermaid | mermaid.js chargé depuis CDN |
| Références croisées | Injection de liens mot-clé→publication en bas de page |
| En-tête webcard | GIF OG animé avec `<picture>` double thème |
| CSS 4 thèmes | Cayman, Midnight, Daltonisme clair, Daltonisme sombre |

### default.html — Pages profil et pages d'accueil

| Fonctionnalité | publication.html | default.html |
|----------------|-----------------|-------------|
| En-tête webcard | Oui | Oui |
| Balises OG | Oui | Oui |
| CSS 4 thèmes | Oui | Oui |
| Rendu Mermaid | Oui | Oui |
| Barre d'export | Oui | **Non** |
| Bannière de version | Oui | **Non** |
| Barre de langue | Oui | **Non** |
| CSS Paged Media | Oui | **Non** |
| Références croisées | Oui | **Non** |

---

## 7. Système de thèmes

| Thème | Mode | Arrière-plan | Accents |
|-------|------|-------------|---------|
| **Cayman** | Clair | Dégradé bleu sarcelle/émeraude | Sarcelle, cyan, émeraude |
| **Midnight** | Sombre | Dégradé marine/indigo | Bleu, violet, cyan |
| **Daltonisme clair** | Clair | Neutre | Bleu + orange |
| **Daltonisme sombre** | Sombre | Neutre sombre | Bleu + orange |

**Sélection** : `prefers-color-scheme` du navigateur (automatique) → sélecteur de thème (choix manuel) → variables CSS dans `:root`.

**Partage social** : `og:image` utilise toujours Cayman (clair) — les plateformes sociales ne supportent pas les images adaptatives au thème.

---

## 8. Pipeline d'assets

### Webcards (aperçus sociaux OG)

- `docs/assets/og/<carte>-<lang>-<theme>.gif`
- 1200×630 pixels, 256 couleurs, GIF animé
- 4 variantes par page : EN/FR × Cayman/Midnight
- Généré par `scripts/generate_og_gifs.py`

### Diagrammes pré-rendus

- `docs/assets/diagrams/<pub-slug>/diagram-NN-<lang>-<theme>.png`
- Rendus localement via Playwright + Chromium + npm mermaid (#16)
- Intégrés via éléments `<picture>` avec `<source>` adaptatif au thème

### Assets de publication

- `pub sync` copie les assets source → docs (synchronisation unidirectionnelle)

---

## 9. Mécanismes d'exclusion

### Exclusions CSS

| Sélecteur | Ce qu'il masque | Contexte |
|-----------|----------------|---------|
| `.mermaid-source` | Blocs `<details>` source Mermaid | Rendu web |
| `@media print` | Barre d'outils, barre de langue, webcard, nav | Export PDF |

### Exclusions JavaScript

| Vérification | Ce qu'il saute | Contexte |
|--------------|----------------|---------|
| `el.closest('.mermaid-source')` | Blocs Mermaid dans conteneurs masqués | Empêche double-rendu |
| Nettoyage DOCX | Barre d'outils, barre de langue, refs croisées | Export DOCX propre |

### Exclusions kramdown

| Motif | Comportement | Impact |
|-------|-------------|--------|
| {% raw %}`{{ }}`{% endraw %} dans blocs de code | Liquid supprime le contenu | Hexagones Mermaid perdent leurs labels |
| `</summary>` dans `<details>` avec lignes vides | Échappé en `&lt;/summary&gt;` | Imbrication en cascade casse la page |

### Matrice de visibilité

| Contexte | Source | Web | PDF | DOCX | Git |
|----------|--------|-----|-----|------|-----|
| Contenu principal | ✅ | ✅ | ✅ | ✅ | ✅ |
| Blocs source Mermaid | ✅ | ❌ | ❌ | ❌ | ✅ |
| Éléments de navigation | — | ✅ | ❌ | ❌ | — |
| En-tête webcard | — | ✅ | ❌ | ❌ | — |
| Barre d'export | — | ✅ | ❌ | ❌ | — |

---

## 10. Déploiement

| Paramètre | Valeur |
|-----------|--------|
| Source | Dossier `docs/` sur la branche par défaut |
| URL | `https://packetqc.github.io` |
| Baseurl | `/knowledge` |
| Construction | Automatique lors de la fusion à la branche par défaut |

```
Fusion PR vers branche par défaut
    ↓
GitHub Pages détecte le changement dans docs/
    ↓
Jekyll construit le HTML statique
    ↓
Fichiers déployés sur CDN (~1-5 min)
    ↓
En ligne à packetqc.github.io/K_DOCS/
```

---

## 11. Commandes pipeline

### Cycle de vie des publications

| Commande | Étape | Action |
|----------|-------|--------|
| `pub new <slug>` | Création | Créer 5 fichiers + mettre à jour les index |
| `pub sync <#>` | Synchronisation | Comparer source vs web, synchroniser les assets |
| `pub check <#>` | Validation | Vérifier structure, front matter, liens |
| `pub list` | Inventaire | Afficher toutes les publications avec statut |

### Qualité du contenu

| Commande | Étape | Action |
|----------|-------|--------|
| `doc review <#>` | Fraîcheur | Vérifier contre l'état actuel des connaissances |
| `docs check <chemin>` | Validation | Front matter, liens, miroir, OG |
| `normalize` | Concordance | Miroirs EN/FR, front matter, liens, assets |

---

## 12. Pièges connus

### Liquid supprime les hexagones Mermaid

{% raw %}**Problème** : La syntaxe `{{label}}` de Mermaid entre en collision avec `{{ variable }}` de Liquid. Liquid s'exécute en premier et remplace silencieusement le contenu.{% endraw %}

**Correction** : Pré-rendre les diagrammes Mermaid en PNG via le rendu local (#16).

### kramdown échappe les balises dans les blocs details

**Problème** : Les blocs `<details>` avec des blocs de code markdown et des lignes vides font que kramdown quitte le mode HTML. Les balises fermantes sont échappées en `&lt;/summary&gt;`.

**Symptôme** : La page semble arrêter son rendu après le premier bloc `<details>`. Tout le contenu suivant est englouti dans des éléments repliés invisibles.

**Correction** : Retirer les blocs `<details>` des pages web. Source préservée dans git.

### baseurl nécessite le filtre relative_url

**Problème** : Les liens internes sans filtre `relative_url` pointent vers les mauvaises URLs (préfixe `/knowledge/` manquant).

**Correction** : Chaque lien interne utilise {% raw %}`{{ '/chemin/' | relative_url }}`{% endraw %}. `normalize` signale les chemins codés en dur.

---

## Diagramme du pipeline

```
┌─────────────────────────────────────────────────────┐
│               RÉDACTION SOURCE                       │
│  publications/<slug>/v1/README.md + assets/ + media/ │
└────────────────────────┬────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│        DIVISION À TROIS NIVEAUX (pub new)            │
│  Résumé EN + Complet EN + Résumé FR + Complet FR     │
└────────────────────────┬────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│         INJECTION DU FRONT MATTER                    │
│  layout, title, description, permalink, og_image,    │
│  pub_id, version, date, keywords                     │
└────────────────────────┬────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│       TRAITEMENT JEKYLL (3 passes)                   │
{% raw %}│  1. Liquid : {{ }}, {% %}, relative_url              │{% endraw %}
│  2. kramdown : markdown → HTML (GFM)                 │
│  3. Mise en page : publication.html / default.html   │
│                                                      │
{% raw %}│  ⚠ EXCLUSIONS : Liquid supprime {{ }}, kramdown      │{% endraw %}
│    échappe </tags>, CSS masque .mermaid-source        │
└────────────────────────┬────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│        AMÉLIORATIONS CÔTÉ CLIENT                     │
│  Mermaid.js, sélecteur de thème, refs croisées,      │
│  export PDF/DOCX                                     │
└────────────────────────┬────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│        DÉPLOIEMENT GITHUB PAGES                      │
│  Fusion → Construction Jekyll → CDN → En ligne       │
└─────────────────────────────────────────────────────┘
```

---

## Publications liées

| # | Publication | Relation |
|---|-------------|---------|
| 0 | [Système de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — le système que ce pipeline dessert |
| 5 | [Webcards & partage social]({{ '/fr/publications/webcards-social-sharing/' | relative_url }}) | Pipeline d'assets — aperçus OG sociaux |
| 6 | [Normalize & concordance]({{ '/fr/publications/normalize-structure-concordance/' | relative_url }}) | Porte de qualité — validation de concordance |
| 13 | [Pagination web & export]({{ '/fr/publications/web-pagination-export/' | relative_url }}) | Export — PDF/DOCX depuis la sortie pipeline |
| 14 | [Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | Contexte — pipeline comme composant |
| 16 | [Visualisation de pages web]({{ '/fr/publications/web-page-visualization/' | relative_url }}) | Post-pipeline — rendu et diagnostics |

**Source** : [Issue #347](https://github.com/packetqc/knowledge/issues/347) — Session de génération de documentation.

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
