---
layout: publication
title: "Pagination web et exportation — Conventions de mise en page et pipelines d'exportation"
description: "Trois conventions de mise en page (publication.html, default.html, modèle @page trois zones), PDF sans dépendances via CSS Paged Media, et DOCX côté client via blob HTML-vers-Word avec éléments MSO. En-têtes courants, pieds de page par page, canvas→PNG pour Mermaid/camemberts/émojis, conversion flex→table pour rangées de stories."
pub_id: "Publication #13"
version: "v1"
date: "2026-02-25"
permalink: /fr/publications/web-pagination-export/
og_image: /assets/og/session-management-en-cayman.gif
keywords: "PDF, DOCX, exportation, pagination, CSS Paged Media, publication.html, mise en page, MSO, canvas, Mermaid"
---

# Pagination web et exportation
{: #pub-title}

> **Publication parente** : [#0 — Système de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Projets** : [P6 — Documentation des exportations](https://github.com/packetqc/knowledge/blob/main/projects/export-documentation.md) · [P8 — Système de documentation](https://github.com/packetqc/knowledge/blob/main/projects/documentation-system.md)

**Contenu**

| | |
|---|---|
| [Résumé](#résumé) | Trois mises en page, deux formats d'exportation, une source de vérité |
| [Trois conventions de mise en page](#trois-conventions-de-mise-en-page) | publication.html · default.html · @page trois zones |
| [Frontières de portée](#frontières-de-portée-des-mises-en-page) | Ce que chaque mise en page inclut et exclut |
| [Pipeline PDF](#pipeline-dexportation-pdf) | CSS Paged Media — zéro dépendance |
| [Pipeline DOCX](#pipeline-dexportation-docx) | Blob HTML-vers-Word avec éléments MSO |
| [Patron Canvas → PNG](#patron-canvas--png) | Correction canonique pour les limites de rendu Word |
| [Barre de langue](#barre-de-langue) | Bascule EN↔FR auto-générée |
| [Modèle Dév→Prod](#modèle-dévprod) | Cycle de promotion knowledge-live → knowledge |

## Résumé

Cette publication documente le **système de pagination web et d'exportation** du cadre Knowledge. Trois conventions de mise en page définissent chaque page. Deux pipelines d'exportation en dérivent — PDF via CSS Paged Media natif au navigateur, DOCX via blob HTML-vers-Word avec éléments MSO courants.

Le système produit des exportations de qualité production en utilisant uniquement les capacités natives du navigateur : en-têtes courants sur chaque page, pieds de page par page avec numéros de page, page de couverture sans en-tête/pied, diagrammes et émojis rendus sur canvas, et mise en page Word-compatible pour le contenu flex. Aucun serveur, aucun service externe.

**Source** : sessions knowledge-live (dév) 2026-02-24/25, promu vers knowledge (prod). 37 PR sur 2 dépôts.

## Trois conventions de mise en page

Le cadre Knowledge utilise exactement trois fichiers de mise en page HTML :

| Mise en page | Fichier | Utilisation | Exportation |
|-------------|---------|------------|-------------|
| **Publication** | `docs/_layouts/publication.html` | Publications techniques, documentation | PDF + DOCX |
| **Défaut** | `docs/_layouts/default.html` | Pages de profil, pages d'accueil, hubs | Aucune |
| **@page trois zones** | CSS dans `publication.html` | Zones d'impression PDF | PDF seulement |

**publication.html** — la pile d'exportation complète : barre d'outils (PDF + DOCX), fonction `printAs()`, règles CSS Paged Media `@page`, éléments MSO courants, barre de langue (EN↔FR auto), bannière de version, en-tête webcard, CSS 4 thèmes, Mermaid, références croisées.

**default.html** — identité visuelle seulement : en-tête webcard, CSS 4 thèmes, balises OG, Mermaid. Pas d'infrastructure d'exportation.

## Frontières de portée des mises en page

| Fonctionnalité | `publication.html` | `default.html` |
|----------------|:-----------------:|:--------------:|
| Barre d'outils export (PDF + DOCX) | ✅ | ❌ |
| `printAs()` + CSS Paged Media | ✅ | ❌ |
| Éléments MSO courants | ✅ | ❌ |
| Barre de langue (EN↔FR) | ✅ | ❌ |
| Bannière de version | ✅ | ❌ |
| En-tête webcard (GIF OG) | ✅ | ✅ |
| CSS 4 thèmes (Cayman/Midnight) | ✅ | ✅ |
| Balises meta OG | ✅ | ✅ |
| Diagrammes Mermaid | ✅ | ✅ |

**Principe de conception** : `default.html` est la couche d'identité visuelle minimale. `publication.html` est `default.html` + pile d'exportation complète. L'infrastructure d'exportation est dans `publication.html` **seulement**.

## Pipeline d'exportation PDF

Export PDF sans dépendances via CSS Paged Media natif au navigateur :

| Couche | Technologie | Rôle |
|--------|-------------|------|
| Déclencheur | `window.print()` | Ouvre la boîte de dialogue d'impression |
| Mise en page | `@media print` | Cache les éléments non-contenu |
| Pagination | `@page` CSS Paged Media | Boîtes marginales, en-têtes/pieds courants |
| Dynamique | JS `beforeprint`/`afterprint` | Injection de contenu, contrôle du nom de fichier |

**Mise en page trois zones** : Marge d'en-tête (zone 1) → Zone de contenu (zone 2) → Marge de pied (zone 3). Filets bleus (2pt solid #1d4ed8) aux frontières. Page de couverture (`@page :first`) efface toutes les boîtes marginales.

**En-tête courant** : Une seule boîte `@top-left` à `width: 100%` — une seule boîte garantit un seul filet. Deux boîtes → Chrome produit un double filet.

**Saut de page TOC intelligent** : JS mesure la hauteur du TOC vs le seuil demi-page (Lettre : 441px, Légal : 585px). Applique `page-break-before: always` au premier `h2` seulement si le TOC dépasse le seuil.

**Nom de fichier PDF** : `PUB_ID - Titre - VER.pdf` — manipulation de `document.title` avant l'impression, restauré sur `afterprint`.

## Pipeline d'exportation DOCX

Blob HTML-vers-Word avec éléments MSO pour les en-têtes/pieds courants par page :

| Élément MSO | ID | Rôle |
|-------------|-----|------|
| `mso-element:header` | `h1` | En-tête courant — toutes pages sauf première |
| `mso-element:footer` | `f1` | Pied courant — toutes pages sauf première |
| `mso-element:header` | `fh1` | En-tête première page — vide (page de couverture) |
| `mso-element:footer` | `ff1` | Pied première page — vide (page de couverture) |

MIME : `application/msword` → extension `.doc`. S'ouvre dans Word, LibreOffice, Google Docs.

**Nettoyage des éléments** : Tous les éléments web sont supprimés (barre d'outils, barre de langue, bannière de version, widgets de board, en-tête webcard, liens de retour, notifications toast, blocs source mermaid).

## Patron Canvas → PNG

Word ne peut pas afficher les URI de données SVG, les SVG en ligne, ni les polices d'émojis couleur. Le patron canonique pour tout graphique rendu par le navigateur :

```
Graphique rendu par le navigateur → SVG/texte → chargement Image → canvas → toDataURL('image/png') → <img src="data:image/png;...">
```

Appliqué à :
- **Diagrammes Mermaid** (async) — SVG → `XMLSerializer` → `encodeURIComponent` → `Image.onload` → canvas → PNG
- **Camemberts** (async) — SVG inline XML → `encodeURIComponent` → `Image.onload` → canvas → PNG
- **Émojis couleur** (sync) — `ctx.fillText()` avec police emoji couleur → PNG (synchrone)

## Barre de langue

Auto-générée depuis `page.permalink` — aucun indicateur front matter requis :

- Pages EN (`/publications/<slug>/`) → « English (this page) · Français »
- Pages FR (`/fr/publications/<slug>/`) → « Français (cette page) · English »

Position : premier élément de `.container`, au-dessus de la barre de publication. Masquée en impression et dans l'export DOCX.

## Modèle Dév→Prod

```
knowledge-live (dév/pré-prod) → valider sur GitHub Pages live
    → harvest vers knowledge  → promouvoir la méthodologie
knowledge (production)        → tous les satellites héritent au wakeup
```

Le sprint de 2 jours (2026-02-24/25) : 19 PR dans knowledge-live (dév) + 18 PR dans knowledge (prod) = 37 PR au total. Les 3 conventions de mise en page validées, pipeline PDF prêt pour la production, pipeline DOCX prêt pour la production.

---

[**Lire la documentation complète →**]({{ '/fr/publications/web-pagination-export/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
