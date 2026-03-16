---
layout: publication
title: "Conception Interface Principale — Complet"
description: "Reference complete de l'interface principale du systeme Knowledge K2.0 : disposition trois panneaux, cinq interfaces iframe, panneau gauche piloté par JSON, barre d'onglets avec persistance, et bouton info contextuel."
pub_id: "Publication #21 — Complet"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/main-interface/full/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "interface, navigation, web, connaissances, tableau de bord, trois panneaux, iframe, complet"
dev_banner: "Interface en developpement — les fonctionnalites et la mise en page peuvent changer entre les sessions."
---

# Conception Interface Principale — Documentation complete
{: #pub-title}

> **Resume** : [Publication #21]({{ '/fr/publications/main-interface/' | relative_url }}) | **Parent** : [#0 — Systeme de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }})

**Table des matieres**

| | |
|---|---|
| [Disposition trois panneaux](#disposition-trois-panneaux) | Architecture gauche / centre / droite |
| [Interfaces](#interfaces) | Cinq interfaces iframe (I1–I5) |
| [Panneau gauche](#panneau-gauche) | Sections widgets pilotees par JSON |
| [Panneau centre](#panneau-centre) | Conteneur iframe avec commutation dynamique |
| [Panneau droite](#panneau-droite) | Visualiseur de documents avec barre d'onglets |
| [Bouton info](#bouton-info) | Panneau info contextuel par interface |
| [Registre sections.json](#registre-sectionsjson) | Chargement dynamique des sections |
| [Systeme de themes](#systeme-de-themes) | Quatre themes avec variables CSS |
| [Deploiement](#deploiement) | GitHub Actions et pipeline de production |
| [Hub des projets](#hub-des-projets) | Navigation par hierarchie de projets |

---

## Disposition trois panneaux

Le navigateur principal K2.0 utilise une disposition a trois panneaux persistants :

```
┌─────────────────────────────────────────────────────────────────┐
│                     Navigateur principal (I2)                    │
├──────────────┬──────────────────────────┬───────────────────────┤
│   GAUCHE     │        CENTRE            │       DROITE          │
│              │                          │                       │
│  Sections    │   Interfaces iframe      │  Visualiseur docs     │
│  widgets     │   (I1, I3, I4, I5)       │  + barre d'onglets    │
│  JSON        │                          │                       │
│              │   Defaut dynamique       │  Onglets navigateur   │
│  10 sections │   depuis interfaces.json │  Persistance local    │
│  depliables  │                          │  Deduplication URL    │
│              │                          │  Limite souple 12     │
├──────────────┴──────────────────────────┴───────────────────────┤
│                     Barre d'outils                              │
└─────────────────────────────────────────────────────────────────┘
```

<div class="three-col">
<div class="col" markdown="1">

### Panneau gauche

- 10 sections widgets pilotees par JSON
- Chaque section est un widget depliable
- Style carte `widget-card` : MAJUSCULES, arriere-plan `var(--code-bg)`
- Hover : `translateX(3px)` + bordure accent gauche + `box-shadow`
- Sous-groupes en cartes bordees avec elements `<details>` depliables
- Liens declenchent l'ouverture dans le panneau centre ou droite selon `target`

</div>
<div class="col" markdown="1">

### Panneau centre

- Conteneur iframe pour les interfaces I1, I3, I4, I5
- Interface par defaut dynamique depuis `interfaces.json` (priorite la plus haute)
- Commutation via clics dans le panneau gauche
- Communication bidirectionnelle par `postMessage`
- Les interfaces chargees dans le centre sont des pages autonomes

</div>
<div class="col" markdown="1">

### Panneau droite

- Visualiseur de documents integre (iframe)
- Barre d'onglets style navigateur en haut
- Persistance `localStorage` des onglets ouverts
- Deduplication automatique des URLs
- Limite souple de 12 onglets
- Fermeture par clic sur le `×` de chaque onglet
- Onglet actif surligne avec la couleur d'accent du theme

</div>
</div>

---

## Interfaces

Cinq interfaces composent la plateforme K2.0. Chacune est une page autonome chargeable en iframe dans le panneau centre :

| ID | Interface | Cible | Description |
|----|-----------|-------|-------------|
| I1 | Revue de session | centre | Analyse interactive de session avec chronologie, graphiques de metriques et detail par message |
| I2 | Navigateur principal | top | Hub de navigation central — la coquille trois panneaux elle-meme |
| I3 | Flux de travail | centre | Machine a etats des taches avec etapes, transitions et statuts d'avancement |
| I4 | Visualiseur projets | centre | Tableau de bord du portfolio de projets avec integration board et metriques |
| I5 | Mindmap vivant | centre | Mindmap interactif en temps reel propulse par MindElixir v5 |

Les interfaces utilisent `page_type: interface` dans le front matter. Elles partagent le layout `publication` mais avec des gardes qui masquent l'en-tete webcard et la barre de langue.

---

## Panneau gauche

<div class="three-col">
<div class="col" markdown="1">

### 10 sections JSON

Le panneau gauche charge ses sections depuis un registre `sections.json` avec fallback code en dur :

| Priorite | Section |
|----------|---------|
| 1 | Profile |
| 2 | Configurations |
| 3 | Interfaces |
| 4 | Documentation |
| 5 | Methodologies |
| 6 | Hubs |
| 7 | Publications |
| 8 | Stories |
| 9 | Essentials |
| 10 | Commands |

Chaque section est un fichier JSON independant (`data/<section>.json`) charge au runtime.

</div>
<div class="col" markdown="1">

### Style widget-card

Les elements du panneau gauche suivent un patron visuel uniforme :

- **Texte** : MAJUSCULES pour les titres de section
- **Arriere-plan** : `var(--code-bg)` — s'adapte au theme
- **Hover** : `translateX(3px)` + bordure accent gauche + `box-shadow`
- **Sous-groupes** : cartes bordees avec fond leger
- **Details depliables** : elements `<details>` pour les contenus secondaires
- **Icones** : indicateurs visuels optionnels par section

</div>
<div class="col" markdown="1">

### Section Documentation

La section Documentation utilise un format de liens plats identique a celui des essentiels :

- Pas de sous-groupes ou de cartes imbriquees
- Liste directe de liens vers les documents
- Chaque lien ouvre le document dans le panneau droite
- Meme style `widget-card` que les autres sections
- Contenu pilote par `data/documentation.json`

### Section Interfaces

- Liste les 5 interfaces avec icones
- Clic ouvre l'interface dans le panneau centre
- Interface active surlignable
- `target: "center"` ou `target: "top"` dans le JSON

</div>
</div>

---

## Registre sections.json

Le fichier `sections.json` est le registre central des sections du panneau gauche :

```json
{
  "sections": [
    { "id": "profile",        "json": "data/profile.json",        "priority": 1 },
    { "id": "configurations", "json": "data/configurations.json", "priority": 2 },
    { "id": "interfaces",     "json": "data/interfaces.json",     "priority": 3 },
    ...
  ]
}
```

- Charge au runtime par le navigateur principal
- Fallback code en dur si le fichier est indisponible
- L'ordre d'affichage suit la priorite croissante
- Chaque entree pointe vers un fichier JSON independant
- Nouvelles sections ajoutables sans modifier le code de l'interface

---

## Bouton info

<div class="three-col">
<div class="col" markdown="1">

### Bouton dans le panneau gauche

Chaque interface dans la section Interfaces du panneau gauche affiche un bouton **info** :

- Icone info sur chaque carte d'interface
- Clic ouvre un panneau d'information contextuelle
- Contenu : description, raccourcis, guide rapide
- Fermeture par clic exterieur ou bouton

</div>
<div class="col" markdown="1">

### Barre d'outils autonome

Les interfaces chargees dans le centre disposent de leur propre barre d'outils avec un bouton info autonome :

- Bouton **info** dans la barre d'outils de l'interface
- Communication par `postMessage` avec le navigateur parent
- Le contenu info est specifique a chaque interface
- Fonctionne meme si l'interface est ouverte hors du navigateur

</div>
<div class="col" markdown="1">

### Communication postMessage

Le protocole `postMessage` assure la communication entre le navigateur et les interfaces iframe :

- Navigation : l'interface demande l'ouverture d'un document dans le panneau droite
- Info : l'interface signale l'affichage de son panneau info
- Theme : le navigateur propage le changement de theme aux iframes
- Langue : le navigateur propage le changement de langue

</div>
</div>

---

## Systeme bilingue

<div class="three-col">
<div class="col" markdown="1">

### Commutation de langue

- Bascule EN/FR disponible dans le navigateur
- Le changement propage a toutes les interfaces chargees
- Les fichiers JSON contiennent `title` et `title_fr`, `description` et `description_fr`
- Les labels de section basculent sans rechargement

</div>
<div class="col" markdown="1">

### Miroirs de contenu

- Chaque page existe en EN et FR
- Front matter : champs correspondants
- Structure : hierarchie identique
- Liens : pointent vers les pairs de meme langue
- Webcards : variantes `-en` / `-fr`

</div>
<div class="col" markdown="1">

### Verifications `normalize`

- Miroir existe pour chaque page
- Liens pointent vers le bon miroir
- Champs front matter correspondent
- Concordance structurelle validee

</div>
</div>

---

## Systeme de themes

Quatre themes disponibles, geres par variables CSS :

<div class="three-col">
<div class="col" markdown="1">

### Themes disponibles

| Theme | Description |
|-------|-------------|
| **Accessible clair** | Defaut, daltonisme-safe |
| **Accessible sombre** | Mode sombre auto OS |
| **Cayman** | Bleu/blanc classique |
| **Midnight** | Marine/indigo sombre |

</div>
<div class="col" markdown="1">

### Propagation

- Selecteur dans la barre d'outils du navigateur
- Variables CSS pilotent toutes les couleurs
- Le changement propage aux iframes via `postMessage`
- Persistance du choix dans `localStorage`

</div>
<div class="col" markdown="1">

### Webcards

- GIF OG anime 1200x630 par page
- Double theme (Cayman + Midnight)
- `<picture>` avec `prefers-color-scheme`
- Partage social utilise la variante Cayman
- Generes dans `docs/assets/og/`

</div>
</div>

---

## Deploiement

<div class="three-col">
<div class="col" markdown="1">

### Pipeline GitHub Actions

- Push sur la branche par defaut
- GitHub Actions declenche le build
- Deploiement direct sans Jekyll legacy
- HTML statique deploye sur GitHub Pages

</div>
<div class="col" markdown="1">

### Assets

- Webcards dans `docs/assets/og/`
- Fichiers JSON dans `docs/data/`
- Scripts d'interface autonomes par page
- CSS partage avec surcharges par interface

</div>
<div class="col" markdown="1">

### Portes de qualite

- `normalize` — concordance structurelle
- `pub check` — validation publication
- `docs check` — validation par page
- `weblinks --admin` — conformite URLs
- Validation JSON integree au build

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
| 20 | [Documentation visuelle]({{ '/fr/publications/visual-documentation/' | relative_url }}) | Visuels — diagrammes et captures generes |
| 22 | [Webcards et partage social]({{ '/fr/publications/webcards-social-sharing/' | relative_url }}) | Webcards — images OG pour le partage |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
