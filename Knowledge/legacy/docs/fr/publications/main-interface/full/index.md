---
layout: publication
title: "Conception Interface Principale — Complet"
description: "Reference complete de l'interface principale du systeme Knowledge : architecture de navigation, hierarchie des pages, pages d'accueil, navigation des publications, integration du profil et patrons d'interaction utilisateur."
pub_id: "Publication #21 — Complet"
version: "v1"
date: "2026-02-27"
permalink: /fr/publications/main-interface/full/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "interface, navigation, web, connaissances, tableau de bord, complet"
dev_banner: "Interface en developpement — les fonctionnalites et la mise en page peuvent changer entre les sessions."
---

# Conception Interface Principale — Documentation complete
{: #pub-title}

> **Resume** : [Publication #21]({{ '/fr/publications/main-interface/' | relative_url }}) | **Parent** : [#0 — Systeme de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }})

**Table des matieres**

| | |
|---|---|
| [Architecture de navigation](#architecture-de-navigation) | Hierarchie des pages et points d'entree |
| [Composants de l'interface](#composants-de-linterface) | Decomposition en trois colonnes de toutes les couches |
| [Hub des projets](#hub-des-projets) | Navigation par hierarchie de projets |

---

## Architecture de navigation

La presence web de Knowledge est organisee en hierarchie de pages hub avec miroirs bilingues :

```
Page d'accueil (/)
    ├── Hub Profil (/profile/)
    │   ├── Resume (/profile/resume/)
    │   └── Complet (/profile/full/)
    ├── Index Publications (/publications/)
    │   └── Publication #N (/publications/<slug>/)
    │       └── Complet (/publications/<slug>/full/)
    └── Hub Projets (/projects/)
```

Chaque page existe en EN et FR. Les barres de langue auto-generees a partir du permalink permettent un basculement transparent. Le layout `publication` pilote toutes les pages de publications avec bannieres de version, barres d'export, references croisees et selection de theme. Le layout `default` pilote les pages de profil, les pages d'accueil et les hubs.

---

## Composants de l'interface

<div class="three-col">
<div class="col" markdown="1">

### Pages d'accueil

La page d'accueil (`/`) est le point d'entree unique — un hub reliant toutes les sections principales.

#### Accueil EN
- Lien hub profil
- Lien index publications
- Lien hub projets
- Cartes de navigation rapide

#### Accueil FR
- Structure miroir (`/fr/`)
- Memes liens, libelles francais
- Auto-detecte depuis le permalink

#### Principes de conception
- Minimal — pas de surcharge, liens directs
- Bilingue — miroirs EN/FR pour chaque page
- Theme adaptatif — respecte les preferences OS
- Responsive — mobile-first, adapte vers le haut

</div>
<div class="col" markdown="1">

### Navigation des publications

L'index des publications (`/publications/`) liste toutes les publications avec statut et liens.

#### Structure par publication
- **Resume** — `/publications/<slug>/`
- **Complet** — `/publications/<slug>/full/`
- Miroirs EN + FR pour les deux niveaux

#### Fonctionnalites du layout publication
- Banniere de version (pub_id, version, date)
- Barre d'export (PDF Letter/Legal, DOCX)
- Selecteur de theme (4 themes)
- Barre de langue (bascule EN/FR)
- Section de references croisees
- Liens par mots-cles

#### Webcards
- GIF OG anime par page
- Double theme (Cayman + Midnight)
- `<picture>` avec `prefers-color-scheme`
- Partage social utilise la variante Cayman

</div>
<div class="col" markdown="1">

### Integration du profil

Le profil auteur est structure en hub avec sous-pages, utilisant le layout `default`.

#### Hierarchie du profil
- **Hub** — `/profile/` — apercu
- **Resume** — `/profile/resume/` — CV cible
- **Complet** — `/profile/full/` — bio complete

#### Fonctionnalites du profil
- Webcards corporate avec photo
- Anneau anime (cycle de couleurs)
- Points de chronologie (progression carriere)
- Liens vers publications et projets

#### Systeme de themes
- **Accessible clair** — defaut (daltonisme-safe)
- **Accessible sombre** — mode sombre auto OS
- **Cayman** — bleu/blanc classique
- **Midnight** — marine/indigo sombre
- Selecteur dans la barre d'export
- Variables CSS pilotent toutes les couleurs

</div>
</div>

---

<div class="three-col">
<div class="col" markdown="1">

### Architecture des layouts

Deux layouts servent toutes les pages :

#### `publication.html`
- Stack d'impression/export complet
- CSS Paged Media (`@page`)
- En-tetes/pieds de page courants
- Saut de page TOC intelligent
- Assainissement nom de fichier PDF
- Banniere de version + mots-cles
- Barre de langue + refs croisees

#### `default.html`
- Pas de fonctions d'impression/export
- Pages profil, hubs, accueil
- Meme systeme de themes
- Meme en-tete webcard

</div>
<div class="col" markdown="1">

### Systeme bilingue

Chaque page a un miroir EN/FR. Le systeme impose la concordance.

#### Barre de langue
- Auto-generee depuis le permalink
- Pages EN → lien francais
- Pages FR → lien anglais
- Masquee en impression
- Utilise le filtre `relative_url`

#### Miroirs de contenu
- Front matter : champs correspondants
- Structure : hierarchie identique
- Liens : pointent vers pairs meme langue
- Webcards : variantes `-en` / `-fr`

#### Verifications `normalize`
- Miroir existe pour chaque page
- Liens pointent vers le bon miroir
- Champs front matter correspondent

</div>
<div class="col" markdown="1">

### Production web

Les pages sont construites via Jekyll sur GitHub Pages sans dependances externes.

#### Pipeline de build
- Push sur la branche par defaut
- GitHub Actions declenche Jekyll
- HTML statique deploye sur Pages
- Rafraichissement auto toutes les 60s

#### Assets
- Webcards dans `docs/assets/og/`
- Generes par `generate_og_gifs.py`
- GIF anime 1200×630
- Palette optimisee 256 couleurs

#### Portes de qualite
- `normalize` — concordance structurelle
- `pub check` — validation publication
- `docs check` — validation par page
- `weblinks --admin` — conformite URLs

</div>
</div>

---

## Hub des projets

Le hub des projets (`/projects/`) fournit une navigation hierarchique a travers tous les projets enregistres.

<div class="three-col">
<div class="col" markdown="1">

#### Types de projets

| Type | Description |
|------|-------------|
| `core` | P0 — Systeme de connaissances |
| `child` | Propre repo, propre board |
| `managed` | Pas de repo, heberge dans parent |

</div>
<div class="col" markdown="1">

#### Navigation

- Liste de projets avec index P#
- Indicateurs de statut par projet
- Liens vers repo, board, publications
- References inter-projets (`→P#`)

</div>
<div class="col" markdown="1">

#### Liens double-origine

- Liens **Core** — canoniques, approuves
- Liens **Satellite** — dev/staging
- Badge d'origine dans le hub
- Les deux sont valides, origine differente

</div>
</div>

---

## Publications liees

| # | Publication | Relation |
|---|-------------|---------|
| 0 | [Systeme de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — le systeme que cette interface dessert |
| 17 | [Pipeline de production web]({{ '/fr/publications/web-production-pipeline/' | relative_url }}) | Pipeline — comment les pages sont construites |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
