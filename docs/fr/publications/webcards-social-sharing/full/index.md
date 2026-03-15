---
layout: publication
title: "Webcards & Partage social — Documentation complète"
description: "Documentation complète du système de webcards : aperçus sociaux OG animés, types de cartes et animations, comportement statique vs dynamique, deux modes de partage, comportement spécifique LinkedIn/Twitter/Facebook/Slack, recettes de partage étape par étape, guide de dépannage et architecture technique."
pub_id: "Publication #5 — Complet"
version: "v2"
date: "2026-02-21"
permalink: /fr/publications/webcards-social-sharing/full/
og_image: /assets/og/webcards-social-sharing-fr-cayman.gif
keywords: "webcards, image OG, GIF animé, partage social, dynamique, artefacts de connaissances"
---

# Webcards & Partage social — Documentation complète
{: #pub-title}

**Table des matières**

| | |
|---|---|
| [Auteurs](#auteurs) | Auteurs de la publication |
| [Résumé](#résumé) | Vue d'ensemble du système de webcards et origine |
| [Qu'est-ce qu'un webcard](#quest-ce-quun-webcard) | Spécifications des aperçus sociaux OG animés |
| &nbsp;&nbsp;[Comment ils sont utilisés](#comment-ils-sont-utilisés) | Rôles en-tête de page, image OG et carte Twitter |
| &nbsp;&nbsp;[Types de cartes](#types-de-cartes) | Corporate, diagramme, panneau partagé, cartoon, index |
| [Design inspiré du contenu](#design-inspiré-du-contenu) | Comment les visuels dérivent des concepts de publication |
| [Webcards dynamiques — artefacts de connaissances vivants](#webcards-dynamiques--artefacts-de-connaissances-vivants) | Cartes pilotées par les données reflétant l'état en direct |
| &nbsp;&nbsp;[Ce que « dynamique » signifie](#ce-que-dynamique-signifie) | Le contenu change entre les générations |
| &nbsp;&nbsp;[Statique vs dynamique — comparaison architecturale](#statique-vs-dynamique--comparaison-architecturale) | Génération codée en dur vs analysée depuis les données |
| &nbsp;&nbsp;[Comment #4a (tableau de bord) fonctionne](#comment-4a-tableau-de-bord-fonctionne) | Table satellite analysée en GIF animé |
| &nbsp;&nbsp;[Le patron dynamique — architecture réutilisable](#le-patron-dynamique--architecture-réutilisable) | Analyser les données structurées, rendre en GIF |
| &nbsp;&nbsp;[Lien avec Knowledge](#lien-avec-knowledge) | Visibilité, actualité et découvrabilité |
| [Comportement d'affichage — Ce que vous voyez dépend de l'endroit](#comportement-daffichage--ce-que-vous-voyez-dépend-de-lendroit) | Animation sur GitHub Pages, statique sur les réseaux sociaux |
| [Deux modes de partage](#deux-modes-de-partage) | Partage par URL de page vs URL d'image |
| &nbsp;&nbsp;[Mode 1 : Partager l'URL de la page](#mode-1--partager-lurl-de-la-page-recommandé) | Aperçu riche avec titre, description et webcard |
| &nbsp;&nbsp;[Mode 2 : Partager l'URL de l'image directement](#mode-2--partager-lurl-de-limage-directement) | Image seule, sans contexte ni clic |
| &nbsp;&nbsp;[Comparaison](#comparaison) | Comparaison côte à côte des deux modes |
| [Comportement des plateformes](#comportement-des-plateformes) | Comment chaque plateforme gère les images OG |
| &nbsp;&nbsp;[LinkedIn](#linkedin) | Première image statique, cache agressif |
| &nbsp;&nbsp;[Twitter (X)](#twitter-x) | Carte summary_large_image, cache 7 jours |
| &nbsp;&nbsp;[Facebook](#facebook) | Peut jouer l'animation GIF en ligne |
| &nbsp;&nbsp;[Slack / Discord](#slack--discord) | Aperçu riche, peut jouer au survol |
| [Recettes pratiques](#recettes-pratiques) | Guides de partage étape par étape |
| &nbsp;&nbsp;[Partager sur LinkedIn (Mobile)](#partager-une-publication-sur-linkedin-mobile) | Flux de partage depuis le navigateur mobile |
| &nbsp;&nbsp;[Partager sur LinkedIn (Bureau)](#partager-une-publication-sur-linkedin-bureau) | Flux de collage et prévisualisation bureau |
| &nbsp;&nbsp;[Forcer le rafraîchissement LinkedIn](#forcer-linkedin-à-rafraîchir-un-aperçu-périmé) | Étapes de vidage du cache via Post Inspector |
| &nbsp;&nbsp;[Montrer l'animation](#montrer-lanimation-pas-la-page) | Partage direct de l'URL du GIF pour montrer l'animation |
| [Dépannage](#dépannage) | Mauvais liens, images manquantes, aperçus périmés |
| [Architecture technique](#architecture-technique) | Intégration HTML, front matter, générateur |
| &nbsp;&nbsp;[Intégration HTML](#intégration-html) | Balises méta OG et configuration URL canonique |
| &nbsp;&nbsp;[Front Matter](#front-matter) | Champ YAML og_image requis |
| &nbsp;&nbsp;[Générateur](#générateur) | Utilisation et options de generate_og_gifs.py |
| &nbsp;&nbsp;[Optimisation GIF](#optimisation-gif) | Palette de couleurs, tramage et tailles de fichiers |
| [Publications liées](#publications-liées) | Liens vers les publications connexes |

## Auteurs

**Martin Paquet** — Analyste et programmeur sécurité réseau, administrateur de sécurité des réseaux et des systèmes, et analyste programmeur et concepteur logiciels embarqués. A conçu le système de webcards dans le cadre de l'architecture de connaissances — donnant à chaque publication une identité sociale animée unique fonctionnant sur toutes les plateformes.

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. A co-conçu la spécification des webcards, construit le script générateur, et documenté le flux de partage social après avoir rencontré des comportements spécifiques aux plateformes lors de tentatives de partage réelles.

---

## Résumé

Chaque page web de Knowledge possède un **aperçu social OG animé unique** — un GIF 1200x630 qui sert à la fois d'en-tête visuel sur GitHub Pages et de carte pour les réseaux sociaux lors du partage sur LinkedIn, Twitter ou Facebook. Ce sont les **webcards**.

Cette publication documente :

| Sujet | Description |
|-------|-------------|
| **Ce que sont les webcards** | Des GIFs animés adaptés au contenu de chaque page, bilingues (EN/FR) |
| **Design inspiré du contenu** | Comment les visuels de chaque carte sont dérivés du concept central de sa publication |
| **Génération statique vs dynamique** | Cartes codées en dur vs cartes pilotées par les données (comme le Tableau de bord) |
| **Comportement d'affichage** | Les réseaux sociaux affichent la première image ; GitHub Pages joue l'animation complète |
| **Deux modes de partage** | Partager l'URL de la page (recommandé) vs partager l'image directement |
| **Comportement des plateformes** | Comment LinkedIn, Twitter, Facebook et Slack gèrent les images OG |
| **Recettes pratiques** | Guides étape par étape pour le partage mobile et bureau |
| **Dépannage** | Cache LinkedIn, mauvaises URLs, aperçus manquants |

Né d'un problème réel : le partage d'une publication sur LinkedIn depuis un mobile pointait vers le fichier markdown GitHub au lieu de la publication GitHub Pages. Cela a conduit à l'ajout de balises `<link rel="canonical">` et à la documentation du flux de partage correct.

---

## Qu'est-ce qu'un webcard

Un webcard est un **GIF animé** représentant une page web :

| Propriété | Valeur |
|----------|--------|
| Taille | 1200x630 pixels |
| Format | GIF animé, palettes 256 couleurs optimisées |
| Tramage | Floyd-Steinberg |
| Boucle | Infinie (`loop=0`) |
| Thème | Double : Cayman (clair, sarcelle/émeraude) + Midnight (sombre, marine/indigo) |
| Détection | `<picture>` + requête média `prefers-color-scheme` |
| Ensemble total | 40 GIFs (10 pages x 2 thèmes x 2 langues) |
| Taille totale | ~7 Mo pour les 40 |
| Générateur | `scripts/generate_og_gifs.py` |
| Sortie | `docs/assets/og/<type-page>-<lang>-<thème>.gif` |

Chaque page obtient une animation unique adaptée à son contenu — pas de modèles génériques.

### Comment ils sont utilisés

| Utilisation | Description |
|-------------|-------------|
| **En-tête de page** | Affiché comme bannière pleine largeur au-dessus du contenu sur GitHub Pages |
| **Image OG** | Référencée dans `<meta property="og:image">` pour les aperçus de partage social |
| **Carte Twitter** | Référencée dans `<meta name="twitter:image">` pour les aperçus Twitter |

### Types de cartes

| Type | Pages | Images | Animation |
|------|-------|--------|-----------|
| `corporate` | Hub profil, CV, profil complet | 8 | Photo avec anneau de bordure pulsant et changeant de couleur |
| `diagram` | Pipeline MPLIB, Session en direct | 7-8 | Les nœuds du pipeline s'activent séquentiellement |
| `split-panel` | Connaissances distribuées, Tableau de bord | 8 | Le panneau gauche défile + le panneau droit coule |
| `cartoon` | Persistance IA | 10 | Transformation Vicky NPC vers AWARE |
| `index` | Index des publications | 8 | Les cartes apparaissent une par une, puis brillent |

---

## Design inspiré du contenu

Chaque webcard est **dérivé** de la publication qu'il représente — pas d'une bibliothèque de modèles génériques. Le type de carte, l'animation, le texte et les éléments visuels sont choisis en fonction de ce que la publication documente réellement :

| Publication | Pourquoi ce design de carte |
|-------------|----------------------------|
| **Profil** (corporate) | La photo de l'auteur est la pièce maîtresse — l'anneau pulsant attire l'attention sur la personne derrière le travail |
| **Pipeline MPLIB** (diagram) | Documente un pipeline de données en 5 étapes — le webcard anime ces étapes exactes de gauche à droite |
| **Session en direct** (diagram) | Documente un flux d'analyse en temps réel en 6 étapes — le webcard pulse les données à travers ces étapes |
| **Persistance IA** (cartoon) | L'analogie Free Guy (NPC→AWARE) est la métaphore centrale — la transformation de Vicky EST le concept |
| **Connaissances distribuées** (split-panel) | Flux bidirectionnel (push + harvest) — le panneau gauche montre les couches, le droit montre le flux entre maître et satellites |
| **Tableau de bord** (split-panel) | État du réseau avec inventaire des satellites — le webcard rend les données réelles de la table satellite |
| **Index des publications** (index) | Une collection de publications — le webcard montre les cartes apparaissant une par une |

**Règle de design** : Lire la publication d'abord, puis concevoir le webcard pour visualiser son concept central. L'animation doit raconter l'histoire de la publication en 2-3 secondes.

---

## Génération statique vs dynamique

La plupart des webcards sont **conçus statiquement** — le texte, la mise en page et l'animation sont codés en dur dans le script générateur en fonction du contenu de la publication au moment de la conception. Quand le contenu change significativement, le webcard est régénéré manuellement.

Un webcard est **généré dynamiquement** — la Publication #4a (Tableau de bord) lit les **données en direct** depuis la table d'état du réseau satellite via `parse_dashboard_data()` :

| Aspect | Cartes statiques (majorité) | Carte dynamique (#4a) |
|--------|----------------------------------|----------------------|
| Source du contenu | Codé en dur dans le script | Analysé depuis la table README |
| Quand régénérer | Après des changements significatifs | À chaque `harvest --healthcheck` |
| Ce qui change entre les exécutions | Rien (sortie identique) | Noms des satellites, versions, dérive, état de santé |
| Fonction de données | Aucune | `parse_dashboard_data()` |
| Exemples | Toutes les cartes profil, pipeline, persistance, index | Tableau de bord uniquement |

**Pourquoi #4a est dynamique** : Le Tableau de bord est un document vivant — l'état des satellites change à chaque exécution de `harvest`. Coder en dur les noms et versions des satellites rendrait le webcard périmé immédiatement. Au lieu de cela, `parse_dashboard_data()` lit la table d'inventaire réelle depuis `publications/distributed-knowledge-dashboard/v1/README.md` et rend l'état actuel du réseau dans le GIF. Les N premières lignes sont rendues, où N correspond à ce qui tient dans la zone de contenu de la carte.

**Candidats futurs** : Toute publication documentant des données vivantes et changeantes pourrait bénéficier de la génération dynamique. Le patron établi par #4a — analyser les données structurées du document source, les rendre dans le GIF — est réutilisable.

---

## Comportement d'affichage — Ce que vous voyez dépend de l'endroit

Le même webcard apparaît différemment selon l'endroit où il est affiché :

| Contexte | Ce que vous voyez | Animation |
|----------|------------------|-----------|
| **GitHub Pages** (en-tête de page) | GIF animé complet en boucle | Oui — toutes les images |
| **Aperçu LinkedIn** | Première image seulement (statique) | Non |
| **Carte Twitter** | Première image seulement (statique) | Non |
| **Aperçu Facebook** | Première image seulement (statique) | Non |
| **Unfurl Slack/Discord** | Première image (peut jouer au survol) | Parfois |
| **URL directe dans le navigateur** | GIF animé complet | Oui |
| **Image dans une appli de messagerie** | Dépend de l'appli | Parfois |

**Implication de design** : La première image de chaque webcard doit être auto-explicative — c'est ce que la plupart des gens verront. L'animation est un bonus pour les visiteurs qui atteignent le site GitHub Pages.

---

## Deux modes de partage

### Mode 1 : Partager l'URL de la page (recommandé)

**Ce que vous partagez** : `https://packetqc.github.io/knowledge/publications/distributed-minds/`

**Ce qui se passe** :

| Étape | Action |
|-------|--------|
| **Exploration** | Le robot de la plateforme sociale récupère la page |
| **Lecture des balises** | Lit les balises méta `og:title`, `og:description`, `og:image` depuis le `<head>` HTML |
| **Téléchargement** | Télécharge le GIF webcard depuis l'URL `og:image` |
| **Affichage** | Montre titre + description + première image du webcard comme carte d'aperçu |
| **Clic** | Mène à votre page de publication |

**Résultat** : Aperçu riche avec titre, description et image webcard. Le lien amène les lecteurs à votre publication.

### Mode 2 : Partager l'URL de l'image directement

**Ce que vous partagez** : `https://packetqc.github.io/knowledge/assets/og/distributed-minds-en.gif`

**Ce qui se passe** :

| Étape | Action |
|-------|--------|
| **Détection** | La plateforme sociale voit un lien image direct |
| **Affichage** | Montre l'image (peut jouer l'animation ou montrer la première image) |
| **Sans contexte** | Pas de titre ni de description associés — juste l'image |
| **Clic** | Mène au fichier image, pas à la publication |

**Résultat** : Montre l'animation du webcard (sur certaines plateformes) mais ne fournit aucun contexte et aucun lien vers la publication. À utiliser uniquement quand vous voulez spécifiquement montrer l'animation elle-même.

### Comparaison

| Aspect | URL de la page (Mode 1) | URL de l'image (Mode 2) |
|--------|------------------------|-------------------------|
| Affiche le titre | Oui | Non |
| Affiche la description | Oui | Non |
| Affiche le webcard | Oui (première image) | Oui (peut animer) |
| Le clic mène à | Page de publication | Fichier image |
| Valeur SEO | Élevée | Aucune |
| Recommandé pour | Tout partage | Montrer l'animation |

---

## Comportement des plateformes

### LinkedIn

| Aspect | Comportement |
|--------|-------------|
| **Partage de page** | Affiche la carte d'aperçu avec titre, description, première image du webcard |
| **Partage d'image** | Affiche l'image uniquement |
| **Animation** | Ne joue jamais — toujours première image statique |
| **Cache** | Cache agressif — peut afficher des données périmées pendant des heures/jours |
| **Vider le cache** | Utilisez le [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/) pour forcer le rafraîchissement |
| **Canonical** | Suit `<link rel="canonical">` et `og:url` pour l'URL de clic |
| **Problème connu** | Si canonical ou og:url est incorrect, le clic mène à la mauvaise page |

### Twitter (X)

| Aspect | Comportement |
|--------|-------------|
| **Partage de page** | Affiche la carte `summary_large_image` avec titre, description, première image du webcard |
| **Partage d'image** | Affiche l'image dans le tweet |
| **Animation** | Ne joue jamais dans l'aperçu — première image statique |
| **Cache** | Cache pendant ~7 jours |
| **Vider le cache** | Utilisez le [Twitter Card Validator](https://cards-dev.twitter.com/validator) |

### Facebook

| Aspect | Comportement |
|--------|-------------|
| **Partage de page** | Affiche l'aperçu avec titre, description, webcard |
| **Partage d'image** | Peut jouer l'animation GIF en ligne |
| **Animation** | Joue parfois dans l'aperçu (Facebook supporte la lecture GIF) |
| **Cache** | Utilisez le [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/) pour rafraîchir |

### Slack / Discord

| Aspect | Comportement |
|--------|-------------|
| **Unfurl de lien** | Affiche un aperçu riche avec titre, description, première image |
| **Image directe** | Peut jouer le GIF au survol ou en ligne |
| **Pas de problème de cache** | Récupère à nouveau à chaque partage |

---

## Recettes pratiques

### Partager une publication sur LinkedIn (Mobile)

```
Étape 1 — Ouvrir la publication sur GitHub Pages
         L'URL doit commencer par : packetqc.github.io/knowledge/
         PAS : github.com/packetqc/knowledge/blob/...

Étape 2 — Vérifier que la barre d'adresse affiche packetqc.github.io
         Si elle affiche github.com, vous êtes sur le mauvais site

Étape 3 — Appuyer sur le bouton Partager du navigateur

Étape 4 — Choisir LinkedIn

Étape 5 — Ajouter votre commentaire et publier
```

### Partager une publication sur LinkedIn (Bureau)

```
Étape 1 — Copier l'URL GitHub Pages :
         https://packetqc.github.io/knowledge/publications/<slug>/

Étape 2 — Dans LinkedIn, cliquer sur « Commencer un post »

Étape 3 — Coller l'URL — attendre que la carte d'aperçu se charge
         Vous devriez voir : titre + description + première image du webcard

Étape 4 — Si l'aperçu semble incorrect, utiliser le Post Inspector d'abord :
         https://www.linkedin.com/post-inspector/

Étape 5 — Ajouter un commentaire et publier
```

### Forcer LinkedIn à rafraîchir un aperçu périmé

```
Étape 1 — Aller à https://www.linkedin.com/post-inspector/

Étape 2 — Coller l'URL complète GitHub Pages

Étape 3 — Cliquer sur « Inspect »

Étape 4 — Vérifier :
         - Le titre correspond à votre publication
         - La description est correcte
         - L'image montre votre webcard (première image)
         - L'URL canonique pointe vers packetqc.github.io (pas github.com)

Étape 5 — Si correct, partager le lien — LinkedIn utilise maintenant les données fraîches
```

### Montrer l'animation (pas la page)

```
Étape 1 — Trouver l'URL du webcard :
         https://packetqc.github.io/knowledge/assets/og/<carte>-<lang>.gif
         Exemple : .../assets/og/distributed-minds-fr.gif

Étape 2 — Partager cette URL directement dans votre post

Étape 3 — Sur certaines plateformes (Facebook, Slack), l'animation jouera
         Sur LinkedIn/Twitter, seule la première image s'affiche
```

---

## Dépannage

### LinkedIn affiche un mauvais aperçu ou pointe vers le markdown GitHub

**Symptômes** : Vous avez partagé la page, mais cliquer sur le lien dans LinkedIn mène à `github.com/packetqc/knowledge/blob/...` au lieu de `packetqc.github.io/knowledge/...`.

**Causes et corrections** :

| Cause | Correction |
|-------|------------|
| Vous étiez sur la vue markdown GitHub, pas GitHub Pages | Vérifiez la barre d'adresse : doit être `packetqc.github.io`, pas `github.com` |
| LinkedIn a mis en cache un aperçu périmé | Utilisez le [Post Inspector](https://www.linkedin.com/post-inspector/) pour rafraîchir |
| Balise canonical manquante | Corrigé en v20 — `<link rel="canonical">` ajouté aux deux layouts |
| og:url pointant vers la mauvaise URL | Vérifiez que le front matter a le bon `permalink` |

### L'aperçu n'affiche pas d'image

| Vérification | Action |
|-------------|--------|
| **Front matter** | Vérifiez que `og_image` est défini dans le front matter YAML de la page |
| **Fichier GIF** | Vérifiez que le fichier GIF existe dans `docs/assets/og/` |
| **Régénérer** | Exécutez `webcard <cible>` pour régénérer les GIFs manquants |
| **Vue du robot** | Utilisez le débogueur spécifique à la plateforme pour vérifier ce que le robot voit |

### L'animation ne joue pas sur les réseaux sociaux

**C'est un comportement attendu.** LinkedIn, Twitter et Facebook affichent la première image comme aperçu statique. L'animation joue uniquement dans certains contextes :

| Contexte | Animation joue ? |
|----------|-----------------|
| **Site GitHub Pages** | Oui (en-tête de page) |
| **URL du GIF dans le navigateur** | Oui (visualisation directe) |
| **Applications de messagerie** | Parfois (Slack, Discord, iMessage) |

Concevez chaque webcard pour que la première image soit auto-explicative.

### Partagé depuis le mobile mais le lien est incorrect

Lors de l'utilisation de la fonction « Partager » du navigateur mobile :

| Étape | Ce qui se passe |
|-------|----------------|
| **Le navigateur partage l'URL** | Le navigateur partage l'URL de la barre d'adresse |
| **Mauvais site possible** | Si vous avez navigué depuis GitHub vers une publication, vous êtes peut-être sur `github.com` (le rendu markdown), pas sur `packetqc.github.io` (GitHub Pages) |
| **Prévention** | Naviguez toujours vers l'URL GitHub Pages directement avant de partager |

**Vérification rapide** : Regardez la page — si vous voyez un en-tête GIF animé pleine largeur en haut, vous êtes sur GitHub Pages. Si vous voyez du markdown rendu sans en-tête, vous êtes sur GitHub.

---

## Architecture technique

### Intégration HTML

Les deux layouts (`default.html` et `publication.html`) incluent :

```html
<!-- Image OG pour le partage social -->
<meta property="og:image" content="{% raw %}{{ page.og_image | absolute_url }}{% endraw %}" />

<!-- URL canonique — LinkedIn l'utilise comme URL de clic -->
<link rel="canonical" href="{% raw %}{{ page.url | absolute_url }}{% endraw %}" />

<!-- Affichage en-tête de page -->
<div class="webcard-header">
  <img src="{% raw %}{{ page.og_image | relative_url }}{% endraw %}" alt="{% raw %}{{ page.title }}{% endraw %}" />
</div>
```

### Front Matter

Chaque page nécessite `og_image` dans son front matter YAML :

```yaml
og_image: /assets/og/distributed-minds-fr-cayman.gif
```

Convention de nommage : `assets/og/<type-page>-<lang>.gif`

### Générateur

`scripts/generate_og_gifs.py` génère tous les webcards :

```bash
python3 scripts/generate_og_gifs.py              # Toutes les cartes
python3 scripts/generate_og_gifs.py #5            # Une publication
python3 scripts/generate_og_gifs.py profile       # Un groupe
```

### Optimisation GIF

| Propriété | Valeur |
|----------|--------|
| **Palette de couleurs** | 256 couleurs par image (quantification MEDIANCUT) |
| **Tramage** | Floyd-Steinberg pour des dégradés lisses |
| **Taille par image** | 120-765 Ko individuellement |
| **Taille totale** | ~7 Mo pour les 40 GIFs |

---

## Publications liées

| # | Publication | Relation |
|---|-------------|----------|
| 0 | [Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — les webcards font partie du système |
| 3 | [Persistance de session IA]({{ '/fr/publications/ai-session-persistence/' | relative_url }}) | Possède un webcard type `cartoon` (Vicky NPC vers AWARE) |
| 4 | [Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) | Possède un webcard type `split-panel` |
| 4a | [Tableau de bord]({{ '/fr/publications/distributed-knowledge-dashboard/' | relative_url }}) | Possède un webcard `split-panel` piloté par les données |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
