---
layout: publication
title: "Visualiseur Web K_DOCS — Moteur de documentation mono-fichier"
description: "Un seul index.html qui rend les publications markdown avec 4 thèmes, export PDF/DOCX, navigation à trois panneaux, mindmap vivant et support bilingue — zéro étape de compilation, zéro dépendance serveur."
permalink: /fr/publications/web-documentation-viewer/full/
lang: fr
permalink_en: /publications/web-documentation-viewer/full/
header_title: "Visualiseur Web K_DOCS"
tagline: "Moteur de documentation mono-fichier"
pub_id: "Publication #23 — Complète"
pub_meta: "Publication #23 v1 | Mars 2026"
pub_version: "v1"
pub_number: 23
pub_date: "Mars 2026"
og_image: /assets/og/knowledge-2-fr-cayman.gif
keywords: "visualiseur documentation, mono-fichier, statique, thèmes, export, panneaux, mindmap, bilingue"
---

# Visualiseur Web K_DOCS — Moteur de documentation mono-fichier

> **Parent** : [Publication #23 — Sommaire]({{ '/fr/publications/web-documentation-viewer/' | relative_url }})

---

## Résumé

Le visualiseur Web K_DOCS résout un problème fondamental : comment servir une documentation riche et interactive depuis un seul fichier statique, sans étape de compilation et sans traitement côté serveur. Le système Knowledge de production (`packetqc/knowledge`) repose sur Jekyll + GitHub Pages avec deux mises en page HTML massives (183 Ko au total). Ce pipeline fonctionne mais nécessite Ruby, une étape de compilation et des conventions spécifiques à Jekyll qui créent des pièges fragiles (suppression Liquid, problèmes d'analyse kramdown, sorties de mode bloc `<details>`).

Le visualiseur remplace tout cela par un seul `index.html` qui récupère le markdown à l'exécution, analyse le front matter YAML, résout les tags Liquid côté client, rend les diagrammes Mermaid et sert un mindmap interactif MindElixir vivant. Quatre thèmes CSS (Cayman, Midnight, Daltonisme Clair/Sombre) persistent via localStorage. L'export corporatif PDF et DOCX utilise CSS Paged Media et les éléments MSO respectivement — zéro dépendance externe. Une disposition à trois panneaux avec diviseurs déplaçables héberge 25+ publications et 5 interfaces. Toute la plateforme documentaire se déploie avec `git push`.

```mermaid
mindmap
  root((Visualiseur Web))
    Pipeline de rendu
      Récupération et analyse markdown
      Front matter YAML
      Résolveur Liquid
      Diagrammes Mermaid
    Système 4 thèmes
      Cayman et Midnight
      Daltonisme Clair et Sombre
      Persistance localStorage
    Disposition 3 panneaux
      Diviseurs déplaçables
      Routage interfaces
      Convention barre chrome
    Moteur export
      PDF via CSS Paged Media
      DOCX via éléments MSO
      Style corporatif
    Mindmap vivant
      MindElixir v5
      Filtrage profondeur
      Sync thèmes
    Bilingue EN FR
```

---

<div class="story-section">

## 1. Philosophie de conception

Le visualiseur Web K_DOCS existe parce que le système Knowledge de production (`packetqc/knowledge`) utilise Jekyll + GitHub Pages avec deux mises en page HTML massives (183 Ko au total). Ce pipeline fonctionne mais nécessite Ruby, une étape de compilation et des conventions spécifiques à Jekyll.

K_DOCS avait besoin de documentation **sans rien de tout ça** — des fichiers markdown bruts servis par GitHub Pages avec `.nojekyll`, rendus entièrement côté client. La contrainte : tout doit fonctionner depuis un seul fichier statique avec zéro traitement côté serveur.

### La contrainte mono-fichier

Un seul fichier `index.html` contient :
- Tout le CSS (4 thèmes, styles d'impression, points de rupture responsifs)
- Tout le JavaScript (pipeline markdown, moteur d'export, gestion des panneaux, intégration mindmap)
- Toute la structure HTML (disposition trois panneaux, barre d'outils, barres chrome)

**Pourquoi mono-fichier ?** Le déploiement est un `git push`. Pas de bundler, pas de transpileur, pas de pipeline CI/CD. Le visualiseur EST la plateforme documentaire.

## 2. Pipeline de rendu Markdown

```
Paramètre URL (?doc=chemin) → fetch .md → analyser front matter → résoudre Liquid →
marked.parse() → rendre mermaid → injecter dans le DOM
```

### Analyse du front matter

Le visualiseur extrait le front matter YAML (entre les délimiteurs `---`) et mappe les champs vers la barre chrome, `<title>`, la balise meta `og:image` et les métadonnées d'export.

Champs requis : `title`, `description`, `permalink`
Champs optionnels : `pub_id`, `pub_meta`, `pub_version`, `pub_date`, `header_title`, `tagline`, `source_url`, `citation`, `og_image`, `permalink_fr`/`permalink_en`, `lang`, `keywords`

### Résolution des tags Liquid

Le visualiseur résout un sous-ensemble de la syntaxe Liquid Jekyll côté client :

| Tag | Résolution |
|-----|-----------|
| `{{ site.baseurl }}` | Auto-détecté depuis `window.location.pathname` |
| `{{ page.url }}` | Permalien du document courant |
| `{{ '...' \| relative_url }}` | Préfixe le baseurl au chemin |

Les syntaxes Liquid à guillemets simples et doubles sont supportées. Le résolveur s'applique avant l'analyse markdown.

### Support kramdown IAL

Les listes d'attributs en ligne kramdown (`{: #id}`, `{: .class}`) sont supprimées du source markdown et appliquées comme attributs HTML sur l'élément précédent.

## 3. Système à quatre thèmes

Tous les thèmes sont de pures propriétés CSS personnalisées — aucune manipulation de style JavaScript :

| Thème | Arrière-plan | Accent | Usage |
|-------|-----------|--------|-------|
| Daltonisme clair | `#faf6f1` chaud | `#0055b3` | Par défaut, accessible |
| Daltonisme sombre | `#1a1a2e` chaud | `#5599dd` | Sombre + accessible |
| Cayman | `#eff6ff` froid | `#1d4ed8` | Bleu clair |
| Midnight | `#0f172a` froid | `#60a5fa` | Bleu sombre |

La sélection de thème persiste via `localStorage` et s'applique **avant le rendu du DOM** (script en ligne dans `<head>`) pour éviter le flash de mauvais thème.

La media query `prefers-color-scheme` auto-sélectionne clair/sombre à la première visite.

## 4. Disposition à trois panneaux

| Panneau | Fonction | Source du contenu |
|---------|---------|-----------------|
| Gauche | Navigateur principal — arbre de publications | `interfaces/main-navigator/index.md` |
| Centre | Visualiseur de contenu principal | Tout document markdown |
| Droite | Contenu secondaire / interfaces | Pages d'interface (I1–I5) |

### Diviseurs déplaçables

Les panneaux sont séparés par des diviseurs verticaux (14px bureau, 8px mobile) avec :
- **Mode glisser** : `mousedown/mousemove/mouseup` avec superposition pour empêcher l'interférence des iframes
- **Clic par étapes** : Le diviseur gauche cycle [0, 220, 320]px. Le diviseur droit cycle 0 → 50% → plein → 0
- **Points de préhension** : 5 points centrés verticalement comme repère visuel
- **Responsif** : Media query CSS `(max-width: 768px)` change la largeur du diviseur

La grille utilise `grid-template-columns` avec des valeurs en pixels. Les transitions sont désactivées pendant le glissement pour un suivi fluide.

## 5. Routage d'interfaces

Le système de routage gère la navigation inter-panneaux sans rechargements complets :

- **Liens d'interface dans le panneau droit** → routent vers le panneau central via détection de `window.name`
- **Liens du navigateur principal** → rechargent la page complète (contexte d'origine différent)
- **Liens externes** → s'ouvrent toujours dans un nouvel onglet
- **BroadcastChannel** propage les changements d'orientation entre panneaux

Le navigateur utilise des iframes `srcdoc` avec origine nulle, donc l'accès inter-documents du navigateur au contenu du panneau n'est pas possible — le routage utilise `postMessage` à la place.

## 6. Moteur d'export

### PDF — CSS Paged Media

L'export utilise `window.print()` avec un CSS complet `@media print` et `@page` :

- **Style corporatif** : Fond blanc (#fff), texte noir (#111), accent bleu (#1d4ed8)
- **Page de couverture** : Titre, description, ligne de séparation, pub_meta, horodatage, auteurs — centrés
- **TDM** : Page 2 avec `page-break-after: always`
- **En-tête récurrent** : Titre avec ligne bleue inférieure (CSS `@top-center`)
- **Pied récurrent** : Horodatage · version à gauche, K_DOCS à droite, ligne bleue supérieure
- **Contrôle de page** : Format A4, marges, orphelins/veuves, `break-inside: avoid` sur les tableaux

La première page (couverture) a des en-têtes/pieds récurrents vides via le sélecteur de page `:first`.

### DOCX — Éléments MSO

L'export DOCX génère du HTML avec des éléments spécifiques à Microsoft Office :

- **Calibri 10pt** pour le corps du texte
- **Même convention TDM-en-page-2** que le PDF
- `rewriteContentLinks()` convertit les chemins internes au format URL du visualiseur (`index.html?doc=`)
- **Même structure de page de couverture** que le PDF
- Convention de nommage : `PUB_ID - Titre - VER.docx`

## 7. Convention barre chrome

Tous les panneaux utilisent la même fonction `buildChromeBar()` :

**Partie non repliable** (toujours visible) :
- Lien permalien "Actual Page" vers l'URL de production

**Partie repliable** (flèche basculante, repliée par défaut) :
- pub_id, titre avec badge de version
- Accroche/description
- pub_meta, pub_date
- URL source, horodatage de génération, citation
- Auteurs (séparés par `&`, affichés sur des lignes séparées)

État persisté dans `localStorage` par panneau.

## 8. Intégration du mindmap vivant

MindElixir v5.9.3 rend le graphe de connaissances K_MIND directement dans le visualiseur :

### Pipeline

```
mind_memory.md (GitHub brut) → depth_config.json → filterMindmap() →
mermaidToMindElixir() → MindElixir.init() → rendu
```

### Trois points de déploiement

1. **Interface I5** — Page autonome avec menu déroulant de thèmes, bascule Normal/Complet, contrôles Centrer/Ajuster/Plein écran
2. **Publication Knowledge 2.0** — Embarquement en ligne avec auto-détection de thème
3. **Webcard du visualiseur** — Carte de prévisualisation quand `live_webcard: mindmap` est défini dans le front matter

### Synchronisation de thèmes

Quatre thèmes MindElixir correspondent aux thèmes du visualiseur :

| Thème visualiseur | Palette MindElixir | Arrière-plan | Nœud racine |
|---|---|---|---|
| Cayman | Bleu, clair | `#eff6ff` | `#1d4ed8` |
| Midnight | Bleu, sombre | `#0f172a` | `#1e40af` |
| Daltonisme clair | Chaud, clair | `#faf6f1` | `#0055b3` |
| Daltonisme sombre | Chaud, sombre | `#1a1a2e` | `#2a4a7a` |

### Filtrage de profondeur

Port JavaScript de `mindmap_filter.py` :
- `default_depth: 3` — afficher 3 niveaux de profondeur par défaut
- `omit: ["architecture", "constraints"]` — masquer les détails d'implémentation en mode normal
- `overrides: {"session/near memory": 4}` — contrôle de profondeur par branche
- Règle du plus-long-match pour la résolution des surcharges

## 9. Support bilingue

Le visualiseur supporte le contenu en anglais et en français :

- **Bascule de langue** : Boutons EN/FR dans l'en-tête
- **Permaliens doubles** : `permalink` + `permalink_fr` (docs EN) ou `permalink_en` (docs FR)
- **Étiquettes dynamiques** : "Contents" ↔ "Table des matières", etc.
- **Paramètre URL** : `?lang=fr` pour la navigation française
- **Miroir FR complet** : Le répertoire `docs/fr/` reflète la structure de `docs/`

## 10. Webcards et partage social

- Injection de la balise meta `og:image` au chargement du document
- Affichage de webcard adapté au thème (variante cayman pour clair, midnight pour sombre)
- Media query `prefers-color-scheme` pour auto-détection
- Webcard mindmap vivant via MindElixir quand `live_webcard: mindmap` est défini
- Repli gracieux avec gestionnaire `onerror` pour les images manquantes

## Les chiffres

| Métrique | Valeur |
|--------|-------|
| Taille totale du fichier | ~1500 lignes |
| Dépendances externes | 3 CDN (marked, mermaid, MindElixir) |
| Étape de compilation | Aucune |
| Prérequis serveur | Hébergement de fichiers statiques |
| Publications servies | 25+ |
| Interfaces servies | 5 |
| Formats d'export | 2 (PDF, DOCX) |
| Thèmes | 4 |
| Langues | 2 (EN, FR) |

</div>

---

*Martin Paquet & Claude (Opus 4.6) | [packetqc/K_DOCS](https://github.com/packetqc/K_DOCS)*
