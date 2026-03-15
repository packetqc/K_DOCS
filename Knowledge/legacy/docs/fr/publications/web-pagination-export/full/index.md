---
layout: publication
title: "Pagination web et exportation — Documentation complète"
description: "Documentation complète : trois conventions de mise en page, modèle CSS Paged Media trois zones, filet d'en-tête une seule boîte, saut TOC intelligent, contrôle du nom de fichier PDF, éléments MSO courants DOCX, canvas→PNG pour Mermaid/camemberts/émojis, conversion flex→table pour rangées de stories, limites de rendu Word, injection de barre de langue, modèle de promotion dév→prod."
pub_id: "Publication #13 — Complète"
version: "v1"
date: "2026-02-25"
permalink: /fr/publications/web-pagination-export/full/
og_image: /assets/og/session-management-en-cayman.gif
keywords: "PDF, DOCX, exportation, pagination, CSS Paged Media, publication.html, mise en page, MSO, canvas, Mermaid, émoji, flex, rangées de stories"
---

# Pagination web et exportation — Documentation complète
{: #pub-title}

**Contenu**

| | |
|---|---|
| [Auteurs](#auteurs) | Auteurs de la publication |
| [Résumé](#résumé) | Vue d'ensemble du système |
| [Trois conventions de mise en page](#trois-conventions-de-mise-en-page) | publication.html · default.html · @page trois zones |
| [Frontières de portée](#frontières-de-portée--tableau-de-référence) | Tableau de fonctionnalités |
| [Pipeline PDF](#pipeline-dexportation-pdf) | CSS Paged Media — zéro dépendance |
| &nbsp;&nbsp;[Mise en page trois zones](#mise-en-page-trois-zones--pdf) | Zones 1/2/3, espacements indépendants, valeurs canoniques |
| &nbsp;&nbsp;[En-tête courant — Filet une boîte](#en-tête-courant--filet-une-seule-boîte) | Pourquoi une seule boîte, correction double filet Chrome |
| &nbsp;&nbsp;[Pied trois colonnes](#pied-de-page-trois-colonnes) | @bottom-left/center/right |
| &nbsp;&nbsp;[Page de couverture](#page-de-couverture--pas-den-têtes-courants) | @page :first — toutes boîtes effacées |
| &nbsp;&nbsp;[Saut TOC intelligent](#saut-de-page-toc-intelligent) | Algorithme et seuils |
| &nbsp;&nbsp;[Contrôle du nom de fichier PDF](#contrôle-du-nom-de-fichier-pdf) | Manipulation de document.title |
| &nbsp;&nbsp;[Format Lettre/Légal](#format-lettrelégal) | Sélecteur radio + injection @page size |
| [Pipeline DOCX](#pipeline-dexportation-docx) | Blob HTML-vers-Word avec éléments MSO |
| &nbsp;&nbsp;[Hiérarchie des conventions](#hiérarchie-des-conventions) | Web → PDF / DOCX modèle frère |
| &nbsp;&nbsp;[Mise en page trois zones — DOCX](#mise-en-page-trois-zones--docx) | Équivalent MSO |
| &nbsp;&nbsp;[Éléments MSO courants](#sections-mso-et-éléments-courants) | IDs d'éléments en-tête/pied |
| &nbsp;&nbsp;[Nettoyage des éléments](#nettoyage-des-éléments) | Éléments web supprimés |
| &nbsp;&nbsp;[Page de couverture](#page-de-couverture-docx) | mso-first-header/footer vide |
| &nbsp;&nbsp;[Patron Canvas → PNG](#patron-canvas--png--canonique) | Tous graphiques navigateur → PNG Word |
| &nbsp;&nbsp;[Diagrammes Mermaid](#diagrammes-mermaid--svg-vers-png) | SVG → canvas → PNG (async) |
| &nbsp;&nbsp;[Camemberts](#camemberts--svg-vers-png) | conic-gradient → canvas → PNG (async) |
| &nbsp;&nbsp;[Émojis — Icônes couleur](#émojis--icônes-couleur-via-canvas) | fillText → PNG (sync) |
| &nbsp;&nbsp;[Rangées de stories — flex→table](#rangées-de-stories--conversion-flextable) | Rangées virtuelles → vraies tables HTML |
| &nbsp;&nbsp;[Limites de rendu Word](#limites-de-rendu-html-dans-word) | Tableau des limites |
| [Barre de langue](#barre-de-langue--auto-générée-depuis-permalink) | EN↔FR auto depuis permalink |
| [Modèle Dév→Prod](#modèle-dévprod) | Cycle knowledge-live → knowledge |
| [Parité PDF/DOCX](#parité-pdfdocx) | Tableau de parité trois zones |
| [Publications connexes](#publications-connexes) | Publications liées |

## Auteurs

**Martin Paquet** — Analyste-programmeur en sécurité réseau, administrateur de la sécurité des réseaux et systèmes, concepteur et programmeur de logiciels embarqués. A conçu le système de trois conventions de mise en page et les deux pipelines d'exportation (PDF via CSS Paged Media, DOCX via blob HTML-vers-Word avec éléments MSO).

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. A implémenté les pipelines complets PDF et DOCX, la conversion canvas→PNG pour Mermaid/camemberts/émojis, la conversion flex→table pour les rangées de stories, et l'injection automatique de la barre de langue. Source : sessions knowledge-live 2026-02-24/25.

---

## Résumé

Cette publication documente le **système de pagination web et d'exportation** du cadre de publications Knowledge. Trois conventions de mise en page définissent chaque page. Deux pipelines d'exportation en dérivent — PDF via CSS Paged Media natif au navigateur, DOCX via blob HTML-vers-Word avec éléments MSO courants.

Le système produit des exportations de qualité production en utilisant uniquement les capacités natives du navigateur et du JavaScript côté client : en-têtes courants sur chaque page de contenu, pieds de page par page avec numéros de page, page de couverture sans en-tête/pied, diagrammes et émojis rendus sur canvas, et mise en page Word-compatible pour le contenu flex. Aucun serveur, aucun service externe.

**Principe clé** : La mise en page web est la source de vérité. PDF et DOCX sont des formats dérivés frères, tous deux produits depuis la même source HTML avec des adaptations de rendu spécifiques à chaque format.

**Source** : sessions knowledge-live (dév) 2026-02-24/25, promu vers knowledge (prod). 37 PR sur 2 dépôts.

---

## Trois conventions de mise en page

Le cadre de publications Knowledge utilise exactement trois fichiers de mise en page HTML. Chacun sert un objectif distinct avec une frontière de portée claire.

| Mise en page | Fichier | Utilisation | Exportation |
|-------------|---------|------------|-------------|
| **Publication** | `docs/_layouts/publication.html` | Publications techniques, documentation | PDF (CSS Paged Media) + DOCX (blob MSO) |
| **Défaut** | `docs/_layouts/default.html` | Pages de profil, pages d'accueil, hubs | Aucune |
| **@page trois zones** | CSS dans `publication.html` | Zones d'impression PDF | PDF seulement |

### publication.html — Pile d'exportation complète

La mise en page `publication.html` est la mise en page complète pour toute page qui sera exportée en PDF ou DOCX. Elle inclut l'infrastructure d'exportation complète :

| Fonctionnalité | Description |
|----------------|-------------|
| **Barre d'outils d'exportation** | Boutons PDF (radio Lettre/Légal) + DOCX dans l'en-tête de page |
| **`printAs()`** | Fonction JS — injecte le format papier, appelle `window.print()`, contrôle le nom de fichier |
| **CSS Paged Media** | Règles `@page` pour la mise en page trois zones, boîtes marginales, filets |
| **Éléments MSO** | En-tête/pied courant DOCX via `mso-element:header/footer` |
| **Barre de langue** | Auto-générée depuis `page.permalink` — bascule EN↔FR |
| **Bannière de version** | Auto-générée depuis le front matter — `pub_id`, `version`, `date`, horodatage généré |
| **En-tête webcard** | Bannière GIF OG animée — double thème (Cayman/Midnight) |
| **CSS 4 thèmes** | Cayman (clair), Midnight (sombre), deux variantes accessibles daltonisme |
| **Mermaid** | Rendu de diagrammes via CDN |
| **Références croisées** | Injection de liens mot-clé vers publications |

### default.html — Pages de profil et d'accueil

La mise en page `default.html` est pour les pages qui présentent plutôt qu'elles n'exportent. Elle inclut l'identité visuelle et la navigation mais pas la pile d'exportation.

**Inclut** : CSS 4 thèmes, en-tête webcard, balises meta OG, Mermaid.

**N'inclut PAS** : Barre d'outils d'exportation, `printAs()`, règles CSS Paged Media `@page`, éléments MSO, barre de langue, bannière de version, références croisées.

**Utilisée pour** : `/profile/`, `/profile/resume/`, `/profile/full/`, `/publications/`, pages d'accueil.

### Modèle @page trois zones

Le modèle `@page` trois zones est l'architecture d'impression CSS Paged Media intégrée dans `publication.html`. Il divise chaque page imprimée en trois zones :

```
┌─────────────────────────────────────────────────────────────────┐
│  ZONE 1 — Marge d'en-tête (@page margin-top: 1.8cm)             │
│  « Titre de la publication »           7,5pt, vertical-bottom   │
│  padding-bottom: 0,3cm (gap texte→filet)                         │
│  ═════════════════════════ border-bottom: 2pt solid #1d4ed8 ═════│← filet
│                         @page padding-top: 0,4cm                 │
├─────────────────────────────────────────────────────────────────┤
│  ZONE 2 — Zone de contenu de page                               │
│  body → .container → h2, h3, paragraphes, tables, blocs code... │
│  Le contenu s'écoule librement entre les deux gaps rembourré     │
│                         @page padding-bottom: 0,4cm             │
├─────────────────────────────────────────────────────────────────┤
│  ════════════════════════ border-top: 2pt solid #1d4ed8 ═════════│← filet
│  padding-top: 0,3cm (gap filet→texte)                            │
│  « Généré : 2026-02-25 · v1 »   « 3 / 12 »   « Knowledge »      │
│  ZONE 3 — Marge de pied (@page margin-bottom: 1.8cm)             │
└─────────────────────────────────────────────────────────────────┘
```

**Insight clé** : La boîte marginale remplit **toute** la zone marginale. Le filet (bordure) se trouve toujours à la frontière entre la zone marginale et la zone de contenu. Les trois espacements sont entièrement indépendants :

| Espacement | Contrôlé par | Valeur actuelle |
|------------|--------------|-----------------|
| Texte ↔ Filet | `padding` sur boîte marginale | 0,3cm |
| Filet ↔ Contenu | `@page { padding }` | 0,4cm |
| Position du filet | `@page { margin }` | 1,8cm depuis le bord de page |

**Valeurs canoniques** (confirmées fonctionnelles dans Chrome/Edge) :

```css
@page {
  margin: 1.8cm 1.5cm 1.8cm 1.5cm;  /* profondeur de zone */
  padding: 0.4cm 0;                   /* gap filet-contenu */
}
@top-left {
  padding-bottom: 0.3cm;              /* gap texte-filet */
  border-bottom: 2pt solid #1d4ed8;   /* le filet */
}
@bottom-left, @bottom-center, @bottom-right {
  padding-top: 0.3cm;
  border-top: 2pt solid #1d4ed8;
}
```

---

## Frontières de portée — Tableau de référence

| Fonctionnalité | `publication.html` | `default.html` |
|----------------|:-----------------:|:--------------:|
| Barre d'outils d'exportation (PDF + DOCX) | ✅ | ❌ |
| Fonction `printAs()` | ✅ | ❌ |
| Règles CSS Paged Media `@page` | ✅ | ❌ |
| Éléments MSO courants | ✅ | ❌ |
| Barre de langue (bascule EN↔FR) | ✅ | ❌ |
| Bannière de version | ✅ | ❌ |
| Injection de références croisées | ✅ | ❌ |
| En-tête webcard (GIF OG) | ✅ | ✅ |
| CSS 4 thèmes (Cayman/Midnight) | ✅ | ✅ |
| Balises meta OG | ✅ | ✅ |
| Diagrammes Mermaid | ✅ | ✅ |

**Principe de conception** : `default.html` est la couche d'identité visuelle minimale. `publication.html` est `default.html` + pile d'exportation complète. L'infrastructure d'exportation est dans `publication.html` **seulement** — jamais dans `default.html`.

---

## Pipeline d'exportation PDF

### CSS Paged Media Stack

Export PDF sans dépendances via les capacités natives du navigateur — aucune bibliothèque externe :

| Couche | Technologie | Rôle |
|--------|-------------|------|
| Déclencheur | `window.print()` | Ouvre la boîte de dialogue d'impression |
| Mise en page | `@media print` | Cache les éléments non-contenu, ajuste la typographie |
| Pagination | `@page` CSS Paged Media | Boîtes marginales, taille de page, en-têtes/pieds courants |
| Dynamique | JS `beforeprint`/`afterprint` | Injection de contenu, analyse TOC, contrôle du nom de fichier |

Support navigateur : Chrome/Edge (Blink) meilleur. Firefox supporte `@page` de base mais pas les boîtes marginales. Safari a un support limité des boîtes marginales.

### Mise en page trois zones — PDF

Voir le [diagramme trois zones](#modèle-page-trois-zones) ci-dessus — la mise en page PDF EST le modèle trois zones.

### En-tête courant — Filet une seule boîte

Utiliser une seule boîte `@top-left` à `width: 100%` avec `border-bottom`. Mettre toutes les autres boîtes d'en-tête à zéro :

```css
@top-left {
  content: "{{ page.title }}";
  width: 100%;
  border-bottom: 2pt solid #1d4ed8;
}
@top-center { content: ""; width: 0; }
@top-right  { content: ""; width: 0; }
```

**Pourquoi une seule boîte** : Deux boîtes `@top-*` avec des valeurs `vertical-align` différentes + `border-bottom` → Chrome rend les bordures à deux hauteurs → artefact de double filet. Une seule boîte garantit un seul filet quelle que soit la valeur de `vertical-align`. C'est la correction définitive du double filet Chrome.

### Pied de page trois colonnes

Injecté par JS au moment de l'impression via `printAs()` :

| Position | Contenu | Exemple |
|----------|---------|---------|
| `@bottom-left` | Horodatage généré + version | `Généré : 2026-02-25 14:30 · v1` |
| `@bottom-center` | Numéros de page | `3 / 12` |
| `@bottom-right` | Marque | `Knowledge` |

Compteur de page via CSS Paged Media : `counter(page) " / " counter(pages)`.

### Page de couverture — Pas d'en-têtes courants

`@page :first` efface toutes les boîtes marginales — pas d'en-tête, pas de pied, pas de filets sur la première page :

```css
@page :first {
  @top-left    { content: ""; border: none; padding: 0; }
  @top-center  { content: ""; width: 0; }
  @top-right   { content: ""; width: 0; }
  @bottom-left { content: ""; border: none; padding: 0; }
  @bottom-center { content: ""; }
  @bottom-right  { content: ""; }
}
```

### Saut de page TOC intelligent

Toutes les publications n'ont pas besoin d'un saut de page forcé après le TOC. Un TOC court peut partager sa page avec la première section — forcer un saut crée une page blanche.

**Algorithme** (dans `printAs()`, avant `window.print()`) :

```javascript
var toc = document.querySelector('.toc');
var firstH2 = document.querySelector('.container h2');
var threshold = paperSize === 'legal' ? 585 : 441; // px — seuil demi-page
if (toc && firstH2) {
  if (toc.offsetHeight > threshold) {
    firstH2.style.pageBreakBefore = 'always';
  }
}
window.addEventListener('afterprint', function restore() {
  if (firstH2) firstH2.style.pageBreakBefore = '';
  window.removeEventListener('afterprint', restore);
});
```

Seuils : Lettre 441px (moitié des ~882px de hauteur de contenu à 96 DPI), Légal 585px (moitié des ~1170px).

### Contrôle du nom de fichier PDF

`document.title` est manipulé avant l'impression pour contrôler le nom de sauvegarde PDF suggéré par le navigateur :

```javascript
var originalTitle = document.title;
var cleanTitle = document.title
  .replace(/#/g, '')
  .replace(/\u2014/g, '-')          // tiret cadratin → tiret
  .replace(/[<>:"/\\|?*]/g, '')     // caractères invalides pour le système de fichiers
  .trim();
document.title = pubId + ' - ' + cleanTitle + ' - ' + version + '.pdf';

window.print();

window.addEventListener('afterprint', function restore() {
  document.title = originalTitle;
  window.removeEventListener('afterprint', restore);
});
```

**Format** : `PUB_ID - Titre - VER.pdf` (ex. : `Publication 13 - Pagination web Export - v1.pdf`).

### Format Lettre/Légal

Sélecteur radio dans la barre d'outils d'exportation ; `printAs(size)` injecte une balise `<style>` avec `@page { size }` avant d'appeler `window.print()`.

---

## Pipeline d'exportation DOCX

### Hiérarchie des conventions

```
Mise en page universelle (spécification de design)
  └── Mise en page web (live sur GitHub Pages — source de vérité)
        ├── Export PDF (dérivé — CSS Paged Media)
        └── Export DOCX (dérivé — blob HTML-vers-Word avec éléments MSO)
```

PDF et DOCX sont des formats dérivés **frères** depuis la même source. La mise en page web est la source de vérité. Aucun format n'est le parent de l'autre.

### Mise en page trois zones — DOCX

L'export DOCX implémente la même mise en page trois zones que le PDF en utilisant des **éléments MSO** au lieu de CSS Paged Media :

```
┌─────────────────────────────────────────────────────────────────┐
│  ZONE 1 — En-tête courant (mso-element:header id="h1")          │
│  Titre de la publication                      Publication #13    │
│  ════════════════════════ 2pt solid #1d4ed8 ═════════════════════│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ZONE 2 — Contenu de page (div.Section1)                        │
│  h2, h3, paragraphes, tables, images...                         │
│  Le contenu s'écoule avec pagination automatique                │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  ════════════════════════ 2pt solid #1d4ed8 ═════════════════════│
│  Généré : 2026-02-25 · v1             3/12          Knowledge   │
│  ZONE 3 — Pied courant (mso-element:footer id="f1")             │
└─────────────────────────────────────────────────────────────────┘
```

**Exception page de couverture** : `mso-first-header: fh1` et `mso-first-footer: ff1` sont vides — pas d'en-tête ni de pied sur la page de couverture. Équivalent direct de `@page :first` en PDF.

### Sections MSO et éléments courants

Les éléments MSO sont placés dans le corps HTML **avant** `<div class="Section1">`. Word les lit comme définitions d'en-tête/pied :

| Élément MSO | ID | Rôle |
|-------------|-----|------|
| `mso-element:header` | `h1` | En-tête courant (toutes pages sauf première) |
| `mso-element:footer` | `f1` | Pied courant (toutes pages sauf première) |
| `mso-element:header` | `fh1` | En-tête première page — vide (couverture sans en-tête) |
| `mso-element:footer` | `ff1` | Pied première page — vide (couverture sans pied) |

CSS de section connectant le contenu à son en-tête/pied :

```css
@page Section1 {
  size: letter;
  margin: 1.8cm 1.5cm 1.8cm 1.5cm;
  mso-header-margin: 0.8cm;
  mso-footer-margin: 0.8cm;
  mso-header: h1;
  mso-footer: f1;
  mso-first-header: fh1;
  mso-first-footer: ff1;
}
div.Section1 { page: Section1; }
```

Type MIME : `application/msword` → extension `.doc`. S'ouvre dans Word, LibreOffice, Google Docs. **Pas** de directive `<w:DoNotOptimizeForBrowser/>` — celle-ci restreint l'édition MS365 en ligne.

### Nettoyage des éléments

Tous les éléments web supprimés du clone avant encapsulation :

| Élément | Classe CSS | Pourquoi supprimé |
|---------|-----------|-------------------|
| Barre d'outils d'exportation | `.pub-export-toolbar` | Contrôle UI |
| Liens de retour | `.back-link` | Navigation |
| Barre supérieure | `.pub-topbar` | Barre de navigation |
| Références croisées | `.pub-crossrefs` | Liens auto-générés |
| Barre de langue | `.pub-lang-bar` | Sélecteur de langue |
| En-tête webcard | `.webcard-header` | Bannière GIF OG |
| Widgets de board | `.board-widget`, `.board-section-widget` | Board live |
| Toast | `.copy-toast` | UI éphémère |
| Indicateur de statut | `.page-status-tag` | Indicateur web seulement |
| Bannière de version | `.pub-version-banner` | Bloc de métadonnées |
| Source mermaid | `pre code.language-mermaid` | Blocs source bruts |

Correspond exactement à la liste de masquage `@media print` — mêmes éléments, même raison.

### Page de couverture DOCX

Le div de page de couverture (`#pub-cover-page`) est masqué sur la mise en page web et rendu visible lors de l'export DOCX :

```javascript
var coverPage = document.getElementById('pub-cover-page');
if (coverPage) {
  var coverClone = coverPage.cloneNode(true);
  coverClone.style.display = 'block';
  var coverGen = coverClone.querySelector('#coverGenDate');
  if (coverGen) coverGen.textContent = ts;
  clone.insertBefore(coverClone, clone.firstChild);
}
var origH1 = clone.querySelector('h1');
if (origH1) origH1.style.display = 'none';
```

CSS de couverture : `min-height: 680pt`, `mso-break-after: section-break`. `mso-first-header/footer` assure l'absence d'en-tête/pied courant sur la couverture.

### Patron Canvas → PNG — Canonique

Word ne peut pas afficher les URI de données SVG, les SVG en ligne, ni les polices d'émojis couleur. Le patron canonique pour tout graphique rendu par le navigateur :

```
Graphique rendu par le navigateur
  → SVG/texte
  → chargement <Image> (async) ou fillText (sync)
  → canvas
  → canvas.toDataURL('image/png')
  → <img src="data:image/png;base64,...">
```

**Pourquoi canvas** : Word ne rend que `data:image/png` et `data:image/jpeg` dans `<img src>`. Les URI de données SVG sont silencieusement ignorées. Canvas convertit tout graphique rendu par le navigateur en format que Word peut afficher.

**Variantes async** (Mermaid, camemberts) : chaque conversion retourne une Promise. `Promise.all([...]).then(...)` assure que tout est terminé avant la construction du blob HTML.

**Variante sync** (émojis) : `ctx.fillText()` est synchrone. S'exécute avant le tableau de Promises, pas d'`Image.onload` nécessaire.

### Diagrammes Mermaid — SVG vers PNG

Mermaid rend `<pre><code class="language-mermaid">` en `<div class="mermaid"><svg>...</svg></div>`. À l'export DOCX, chaque SVG est converti en PNG :

```javascript
var liveMermaidSvgs = Array.from(document.querySelectorAll('.mermaid svg'));
var mermaidDims = liveMermaidSvgs.map(function(svgEl) {
  var rect = svgEl.getBoundingClientRect();
  return { w: Math.round(rect.width) || 700, h: Math.round(rect.height) || 300 };
});
// ... Image.onload → canvas → toDataURL('image/png') → img remplacement ...
```

**Important** : Dimensions mesurées depuis le SVG **live** (pré-clone) — les éléments clonés n'ont pas de mise en page. **Garde de rendu** : Si mermaid n'a pas fini de rendre quand l'export est déclenché, un toast est affiché et l'export attend 2,5s avant de réessayer.

### Camemberts — SVG vers PNG

Les camemberts utilisent `conic-gradient()` CSS — ignoré par Word. À l'export, les éléments camembert (`[class*="pie-"]`) sont convertis en images PNG 48×48px via le même patron canvas que Mermaid.

Couleurs : remplissage sarcelle (#0f766e) sur fond sarcelle clair (#99f6e4). `Promise.all(promises.concat(pngPromises)).then(...)` gère les Promises camembert et Mermaid ensemble.

### Émojis — Icônes couleur via canvas

Word revient aux glyphes Unicode monochrome pour les émojis. PDF utilise le moteur de rendu natif du navigateur (couleur pleine). L'export DOCX convertit les émojis en PNG rendus sur canvas pour correspondre à la fidélité PDF :

```javascript
function emojiToPng(ch) {
  var canvas = document.createElement('canvas');
  canvas.width = 32; canvas.height = 32;
  var ctx = canvas.getContext('2d');
  ctx.font = '26px "Segoe UI Emoji","Apple Color Emoji","Noto Color Emoji",serif';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(ch, 16, 16);  // Le canvas du navigateur utilise la police emoji couleur
  return canvas.toDataURL('image/png');
}
```

**Regex** : `\p{Emoji_Presentation}` correspond aux émojis avec présentation graphique. `\uFE0F?` couvre les séquences de présentation emoji explicites. `ctx.fillText()` est synchrone — s'exécute avant `Promise.all`.

### Rangées de stories — Conversion flex→table

Word ignore complètement `display:flex`. Les rangées de stories utilisent une mise en page deux colonnes basée sur flex — des « rangées virtuelles » qui ne sont pas de vraies tables HTML. Dans DOCX, elles s'empilent verticalement.

**Correction** : Convertir chaque `.story-row` en une vraie `<table>` à 2 cellules avant de construire le blob. Logique de bordure appliquée en inline (pas de pseudo-sélecteurs CSS) :

```javascript
clone.querySelectorAll('.story-section').forEach(function(section) {
  var rows = Array.from(section.querySelectorAll('.story-row'));
  rows.forEach(function(row, i) {
    var isFirst = (i === 0);
    var isLast  = (i === rows.length - 1);
    var bTop    = isLast ? 'none' : (isFirst ? '1px solid #ddd' : 'none');
    var bBottom = isLast ? 'none' : '1px solid #ddd';
    // ... createElement table → tr → tdL + tdR → replaceChild(tbl, row) ...
  });
});
```

**Style de première cellule de table intérieure** (appliqué **avant** flex→table — préservé dans la copie `innerHTML`) :

```javascript
clone.querySelectorAll('.story-row-right table td:first-child').forEach(function(td) {
  td.style.whiteSpace = 'nowrap';
  td.style.fontWeight = '600';
  td.style.width = '140px';
  td.style.color = '#555';
  td.style.border = 'none';
});
```

### Limites de rendu HTML dans Word

Référence faisant autorité pour les contournements d'export DOCX :

| CSS navigateur/fonctionnalité | Word rend | Correction canonique |
|-------------------------------|-----------|---------------------|
| `display:flex` | Ignoré — blocs empilés verticalement | Conversion JS flex→table |
| `padding-top` sur div | Ignoré | Utiliser style inline `margin-top` |
| `border-top` sur div vide | Ignoré | Remplacer par `<p style="border-bottom:...">` |
| `:first-child`, `:last-child`, `:nth-child` | Pseudo-sélecteurs CSS ignorés | JS `querySelectorAll` + styles inline |
| `data:image/svg+xml` dans `<img src>` | Non rendu (silencieux) | URI de données canvas→PNG |
| Éléments `<svg>` en ligne | Non rendus | URI de données canvas→PNG |
| Police emoji couleur (COLR/SBIX) | Glyphe Unicode monochrome | Canvas `fillText`→PNG |
| Frère adjacent CSS `.a + .a` | Ignoré | Styles inline basés sur index JS |
| CSS `conic-gradient()` | Ignoré | URI de données canvas→PNG |

---

## Barre de langue — Auto-générée depuis permalink

La barre de langue est injectée par `publication.html` depuis `page.permalink` — aucun indicateur front matter requis :

```liquid
{% if page.permalink contains '/fr/' %}
<div class="pub-lang-bar">
  <span><strong>Langues / Languages</strong> : Français (cette page)</span>
  <a href="{{ page.permalink | remove: '/fr' | relative_url }}">English</a>
</div>
{% else %}
<div class="pub-lang-bar">
  <span><strong>Languages / Langues</strong>: English (this page)</span>
  <a href="{{ '/fr' | append: page.permalink | relative_url }}">Français</a>
</div>
{% endif %}
```

**Position** : Premier élément de `.container`, au-dessus de la barre de publication.

**Impression/DOCX** : Masquée via `display: none !important` dans `@media print`. Aussi supprimée par le nettoyage de l'export DOCX (`.pub-lang-bar` dans la liste de nettoyage des éléments).

**Convention** : Pages EN ont le permalink `/publications/<slug>/` → « English (this page) · Français ». Pages FR ont le permalink `/fr/publications/<slug>/` → « Français (cette page) · English ». Le filtre `relative_url` gère le préfixe `baseurl` de Jekyll.

---

## Modèle Dév→Prod

Les fonctionnalités de mise en page sont développées et validées sur le satellite avant d'être promues vers le core :

```
knowledge-live (dév/pré-prod)        → tester sur GitHub Pages live
    → issue harvest vers knowledge   → valider inter-dépôt
knowledge (production)               → tous les satellites héritent au wakeup
```

| Étape | Dépôt | GitHub Pages | Rôle |
|-------|-------|-------------|------|
| Développement | `knowledge-live` | `packetqc.github.io/knowledge-live/` | Tester les fonctionnalités de mise en page live |
| Harvest | `knowledge` | — | `methodology/web-pagination-export.md` mis à jour |
| Production | `knowledge` | `packetqc.github.io/knowledge/` | Mises en page canoniques déployées |
| Héritage | Tous satellites | GitHub Pages satellites | `wakeup` synchronise les mises en page |

**Le satellite EST l'environnement de staging** : Chaque fonctionnalité de mise en page est validée sur une instance GitHub Pages live avant la promotion. Le sprint de 2 jours (2026-02-24/25) a validé 37 PR sur 2 dépôts avant que les mises en page atteignent la production.

---

## Parité PDF/DOCX

Tableau de parité trois zones entre les deux formats d'exportation :

| Fonctionnalité | PDF (CSS Paged Media) | DOCX (éléments MSO) |
|----------------|----------------------|---------------------|
| Zone 1 — En-tête | `@top-left { content; border-bottom }` | Div `mso-element:header` avec table |
| Zone 2 — Contenu | Zone de contenu `@page` | `div.Section1` |
| Zone 3 — Pied | `@bottom-left/center/right` | Div `mso-element:footer` avec table |
| Exception couverture | `@page :first` efface toutes boîtes | `mso-first-header/footer` vides |
| Numéros de page | `counter(page) / counter(pages)` | `mso-field-code: PAGE / NUMPAGES` |
| Couleur du filet | `2pt solid #1d4ed8` | `2pt solid #1d4ed8` |
| Pied trois colonnes | `@bottom-left/center/right` | Table 3 cellules dans élément footer |
| Camemberts | Navigateur rend conic-gradient nativement | SVG→canvas→PNG à l'export |
| Mermaid | Navigateur rend SVGs nativement | SVG→canvas→PNG à l'export |
| Émojis couleur | Navigateur utilise police COLR/SBIX | Canvas `fillText`→PNG à l'export |
| Mise en page flex | Colonnes côte à côte `display:flex` | Conversion JS flex→table à l'export |
| CSS `:first-child` | Pseudo-sélecteurs résolus par le navigateur | JS `querySelectorAll` + styles inline |

---

## Publications connexes

| # | Publication | Relation |
|---|-------------|---------|
| 0 | [Système de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — cette publication documente l'infrastructure de mise en page core |
| 6 | [Normalize et concordance structurelle]({{ '/fr/publications/normalize-structure-concordance/' | relative_url }}) | Vérifications de concordance de mise en page |
| 8 | [Gestion de session]({{ '/fr/publications/session-management/' | relative_url }}) | Référence de commande `pub export` |
| 11 | [Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }}) | Mise en page rangées de stories documentée ici |

---

[**← Résumé**]({{ '/fr/publications/web-pagination-export/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
*Source : knowledge-live P3/P6 — sessions 2026-02-24/25, 37 PR sur 2 dépôts*
