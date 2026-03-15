---
layout: publication
title: "Story #26 — Un seul visualiseur pour tous : Un moteur de documentation mono-fichier"
description: "Comment un seul index.html est devenu une plateforme documentaire complète — disposition 3 panneaux, 4 thèmes, export PDF/DOCX, mindmap vivant, routage d'interfaces, et zéro étape de compilation."
pub_id: "Publication #11 — Story #26"
version: "v1"
date: "2026-03-15"
permalink: /fr/publications/success-stories/story-26/
og_image: /assets/og/knowledge-2-en-cayman.gif
keywords: "histoire de succès, visualiseur, documentation, mono-fichier, statique, thèmes, export, panneaux"
---

# Story #26 — Un seul visualiseur pour tous : Un moteur de documentation mono-fichier

> **Publication parente** : [#11 — Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }})

---

<div class="story-section">

> *« Un seul fichier HTML. Aucune étape de compilation. Aucun framework. Aucun serveur. Poussez du markdown sur GitHub, il se rend avec des thèmes, s'exporte en PDF et DOCX, navigue entre trois panneaux, et sert un mindmap interactif vivant. Toute la plateforme documentaire est un seul `index.html`. »*

<div class="story-row">
<div class="story-row-left">

**Détails**

</div>
<div class="story-row-right">

| | |
|---|---|
| Date | 2026-03-15 |
| Catégorie | 🏗️ 🎨 📄 |
| Contexte | Le dépôt Knowledge de production utilise Jekyll + GitHub Pages avec deux mises en page HTML massives (183 Ko au total). Ça fonctionne, mais nécessite une étape de compilation, des dépendances Ruby et des conventions spécifiques à Jekyll. K_DOCS avait besoin de documentation sans tout ça — des fichiers markdown bruts servis par GitHub Pages avec `.nojekyll`, rendus entièrement côté client. |
| Déclenché par | La décision de créer K_DOCS comme un dépôt autonome qui publie la documentation indépendamment du pipeline de production. La contrainte : tout doit fonctionner depuis un seul fichier statique avec zéro traitement côté serveur. |
| Rédigé par | **Claude** (Anthropic, Opus 4.6) — à partir des données de session en direct |

</div>
</div>

## L'architecture — Un fichier fait tout

`docs/index.html` est le moteur documentaire entier. Il gère :

### 1. Pipeline de rendu Markdown

```
Paramètre URL (?doc=chemin) → fetch .md → parse front matter → résoudre Liquid →
marked.parse() → rendre mermaid → injecter dans le DOM
```

- **Analyse du front matter** : Extrait les métadonnées YAML (titre, description, auteur, version, etc.)
- **Résolution Liquid** : Gère `{{ site.baseurl }}`, `{{ page.url }}`, filtre `relative_url`
- **Rendu Mermaid** : Rendu de diagrammes côté client via CDN
- **IAL kramdown** : Supprime la syntaxe `{: #id}` et l'applique comme attributs HTML

### 2. Disposition à trois panneaux

| Panneau | Fonction | Source du contenu |
|---------|---------|---------------|
| Gauche | Navigateur principal — arbre de publications | `interfaces/main-navigator/index.md` |
| Centre | Visualiseur de contenu principal | Tout document markdown |
| Droite | Contenu secondaire / interfaces | Pages d'interface (I1–I5) |

Les panneaux sont séparés par des **diviseurs déplaçables** (14px bureau, 8px mobile) avec des points de préhension et repli clic-par-étape.

### 3. Routage d'interfaces

Le système de routage gère la navigation inter-panneaux sans rechargements complets :

- **Liens d'interface du panneau droit** → route vers le panneau central
- **Liens du navigateur principal** → recharge la page complète
- **Pages embarquées** détectent `window.name` pour le contexte de routage
- **BroadcastChannel** propage les changements d'orientation entre panneaux

### 4. Système à quatre thèmes

Tous les thèmes sont de pures variables CSS — pas de changement de classe, pas de manipulation de style JavaScript :

| Thème | Arrière-plan | Accent | Fonction |
|-------|-----------|--------|---------|
| Daltonisme clair | `#faf6f1` chaud | `#0055b3` | Par défaut, accessible |
| Daltonisme sombre | `#1a1a2e` chaud | `#5599dd` | Sombre + accessible |
| Cayman | `#eff6ff` froid | `#1d4ed8` | Bleu clair |
| Midnight | `#0f172a` froid | `#60a5fa` | Bleu sombre |

Le thème persiste via `localStorage` et s'applique avant le rendu du DOM (script en ligne dans `<head>`).

### 5. Moteur d'export

**PDF** — CSS Paged Media via `window.print()` :
- Style corporatif (pas les couleurs du thème web)
- Page de couverture avec titre, description, auteurs
- Table des matières en page 2 avec saut de page après
- En-tête et pied de page récurrents avec lignes d'accent bleues
- Contrôle de taille `@page`, marges, orphelins/veuves

**DOCX** — Éléments MSO avec Calibri 10pt :
- Même convention TDM-en-page-2
- `rewriteContentLinks()` convertit les chemins internes au format URL du visualiseur
- Même structure de page de couverture

### 6. Webcards et partage social

- Injection de la balise meta `og:image` au chargement du document
- Affichage de webcard adapté au thème (variante cayman pour clair, midnight pour sombre)
- Requête media `prefers-color-scheme` pour auto-détection
- Webcard mindmap vivant via MindElixir quand `live_webcard: mindmap` est défini
- Repli gracieux avec gestionnaire `onerror` pour les images manquantes

### 7. Intégration du mindmap vivant

MindElixir v5.9.3 rend le graphe de connaissances K_MIND directement dans le visualiseur :
- Récupère `mind_memory.md` depuis GitHub
- Applique le filtrage de profondeur depuis `depth_config.json`
- Convertit le texte indenté mermaid en arbre JSON MindElixir
- Synchronisation de thème avec le thème courant du visualiseur

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

## Ce que cela prouve

- **Zéro infrastructure** : Pas de Node.js, pas de Ruby, pas de pipeline CI/CD pour la documentation
- **Parité production** : Reproduit les fonctionnalités clés de 183 Ko de mises en page Jekyll dans un seul fichier
- **Compatibilité URL** : La structure `/docs/publications/<slug>/` correspond à la production pour la double publication
- **Convention plutôt que configuration** : Le front matter YAML est le contrat — le visualiseur s'adapte à ce qu'il trouve
- **Extensible par conception** : Les nouvelles publications sont juste des fichiers markdown avec front matter. Déposez-les, ils se rendent.

</div>

[**Validé**]({{ '/fr/publications/success-stories/story-26/' | relative_url }})

---
