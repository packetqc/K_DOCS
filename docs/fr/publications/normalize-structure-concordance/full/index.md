---
layout: publication
title: "Normalize & Concordance structurelle — Documentation complète"
description: "Documentation complète de la commande normalize : 7 catégories de concordance, règles détaillées pour structure/layout/webcard/liens/assets/mindset/branche, format de sortie, comportement auto-fix, intégration avec les autres commandes et quand l'exécuter."
pub_id: "Publication #6 — Complet"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/normalize-structure-concordance/full/
og_image: /assets/og/normalize-fr-cayman.gif
keywords: "normaliser, concordance, structure, validation, bilingue, audit"
---

# Normalize & Concordance structurelle — Documentation complète
{: #pub-title}

**Table des matières**

| | |
|---|---|
| [Auteurs](#auteurs) | Auteurs de la publication |
| [Résumé](#résumé) | Vue d'ensemble de l'architecture auto-réparatrice |
| [Ce que normalize vérifie](#ce-que-normalize-vérifie) | Les 7 catégories de concordance en un coup d'oeil |
| [Utilisation](#utilisation) | Syntaxe et comportement des modes |
| [Règles de concordance détaillées](#règles-de-concordance-détaillées) | Spécification complète de chaque vérification |
| &nbsp;&nbsp;[1. Concordance de structure](#1-concordance-de-structure) | Miroirs EN/FR, liens hub-sous-pages, résumé-complet |
| &nbsp;&nbsp;[2. Concordance de layout](#2-concordance-de-layout) | Champs front matter, standard de style des tableaux |
| &nbsp;&nbsp;[3. Concordance webcard](#3-concordance-webcard) | Existence des GIF OG, balises méta, convention de nommage |
| &nbsp;&nbsp;[4. Concordance des liens](#4-concordance-des-liens) | Références croisées, bascule de langue, chemins codés |
| &nbsp;&nbsp;[5. Concordance des assets](#5-concordance-des-assets) | Fichiers requis et formats |
| &nbsp;&nbsp;[6. Concordance de mindset](#6-concordance-de-mindset) | Vérifications d'actualité du mind_memory.md |
| &nbsp;&nbsp;[7. Concordance de branche](#7-concordance-de-branche) | Détection de branche par défaut et config GitHub Pages |
| [Format de sortie](#format-de-sortie) | Exemple de rapport normalize |
| [Comment les corrections sont appliquées](#comment-les-corrections-sont-appliquées) | Problèmes auto-corrigeables vs manuels |
| [Quand l'exécuter](#quand-lexécuter) | Déclencheurs et moment recommandé |
| [Intégration avec les autres commandes](#intégration-avec-les-autres-commandes) | Comment normalize interagit avec les autres commandes |
| [Publications liées](#publications-liées) | Publications parentes et liées |

## Auteurs

**Martin Paquet** — Analyste et programmeur sécurité réseau, administrateur de sécurité des réseaux et des systèmes, et analyste programmeur et concepteur logiciels embarqués. A conçu le système d'audit de concordance pour maintenir l'architecture de connaissances cohérente au fil de sa croissance — miroirs bilingues, validation du front matter, intégrité des liens et synchronisation des assets.

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. Implémente les vérifications normalize, détecte la dérive structurelle et applique les corrections de façon autonome lorsqu'autorisé.

---

## Résumé

À mesure que Knowledge grandit — nouvelles pages, publications, miroirs bilingues, variations de profil, webcards OG — des incohérences structurelles apparaissent inévitablement. Une page française sans miroir anglais. Une page de profil qui oublie de lister la dernière publication. Une référence d'image OG pointant vers un GIF inexistant.

La commande `normalize` est la **couche d'auto-réparation** de l'architecture de connaissances. Elle audite l'ensemble du dépôt contre 7 catégories de règles de concordance et rapporte (ou corrige) chaque écart. Pensez-y comme un linter pour l'architecture de connaissances — pas la syntaxe du code, mais l'intégrité structurelle.

---

## Ce que normalize vérifie

| # | Catégorie | Ce qu'elle assure |
|---|----------|----------------|
| 1 | **Structure** | Chaque page EN a un miroir FR. Les hubs lient toutes les sous-pages. |
| 2 | **Layout** | Toutes les pages utilisent les bons layouts avec les champs requis. |
| 3 | **Webcard** | Chaque page a un GIF OG animé et un `og_image` correct. |
| 4 | **Liens** | Références croisées cohérentes — landing, index, profils. |
| 5 | **Assets** | Les assets requis existent (aperçu social, GIFs, portraits). |
| 6 | **Mindset** | mind_memory.md reflète l'état actuel. |
| 7 | **Branche** | Branche par défaut détectée, GitHub Pages configuré. |

---

## Utilisation

```
normalize              # Rapport seulement (par défaut : --check)
normalize --check      # Rapport seulement, pas de changements
normalize --fix        # Appliquer les corrections automatiquement
```

---

## Règles de concordance détaillées

### 1. Concordance de structure

Chaque page doit avoir son miroir bilingue :

```
/profile/                        ↔ /fr/profile/
/profile/resume/                 ↔ /fr/profile/resume/
/profile/full/                   ↔ /fr/profile/full/
/publications/<id>/              ↔ /fr/publications/<id>/              (résumé)
/publications/<id>/full/         ↔ /fr/publications/<id>/full/         (complet)
```

**Ce qui est vérifié :**

| Vérification | Règle |
|--------------|-------|
| Miroirs EN/FR | Page EN existe → miroir FR doit exister (et inversement) |
| Hub → sous-pages | Les hubs doivent lier toutes leurs sous-pages |
| Sous-page → hub | Les sous-pages doivent lier en retour vers leur hub |
| Miroir linguistique | Les sous-pages doivent lier vers leur miroir linguistique |
| Résumé → complet | Les résumés de publications lient vers leur page complète |
| Complet → résumé | Les pages complètes lient en retour vers leur résumé |

### 2. Concordance de layout

**Champs front matter requis (toutes les pages) :**

| Champ | Exemple | But |
|-------|---------|-----|
| `layout` | `publication` ou `default` | Template Jekyll |
| `title` | `"Webcards & Partage social"` | Titre de page, titre OG |
| `description` | `"Chaque page..."` | Description méta, description OG |
| `permalink` | `/fr/publications/webcards-social-sharing/` | Chemin URL canonique |
| `og_image` | `/assets/og/webcards-social-sharing-fr.gif` | Image d'aperçu social |

**Champs supplémentaires pour les publications :**

| Champ | Exemple | But |
|-------|---------|-----|
| `pub_id` | `"Publication #5"` | Identifiant de publication |
| `version` | `"v1"` | Version du contenu |
| `date` | `"2026-02-19"` | Date de publication |

### 3. Concordance webcard

**Ce qui est vérifié :**

| Vérification | Règle |
|--------------|-------|
| Front matter | `og_image` est défini dans le front matter de chaque page |
| GIF existe | Le fichier GIF référencé existe dans `docs/assets/og/` |
| Balises méta | Les deux layouts émettent les balises méta `og:image` et `twitter:image` |
| Lien canonique | La balise `<link rel="canonical">` est présente (critique pour LinkedIn) |
| Convention de nommage | Le nommage suit `assets/og/<type-page>-<lang>.gif` |
| Variantes bilingues | Les variantes EN et FR existent pour chaque carte |

### 4. Concordance des liens

| Type de lien | Ce qui est vérifié |
|-----------|---------------|
| Landing → hub | `docs/index.md` lie vers le hub profil et l'index des publications |
| Index → profils | L'index des publications lie vers le profil de l'auteur |
| Profils → pubs | Les pages de profil listent toutes les publications |
| Référence knowledge | `packetqc/knowledge` référencé dans les tables de contact |
| Liens mind_memory.md | Les liens web correspondent aux permalinks réels |
| Bascule de langue | Chaque page lie vers son miroir |
| Résumé → complet | Les résumés lient vers leur page `/full/` |
| Complet → résumé | Les pages complètes lient en retour |
| Pas de chemins codés | Tous les liens internes utilisent `relative_url` |

### 5. Concordance des assets

| Asset | Chemin attendu | Format |
|-------|------|--------|
| Aperçu social | `assets/social-preview.png` | 1280x640 PNG |
| Source SVG | `assets/social-preview.svg` | SVG |
| GIFs OG | `assets/og/*.gif` | 1200x630 GIF animé |
| Photo portrait | `references/Martin/me3.JPG` | 782x840 JPEG |
| Avatar Vicky | `references/Martin/vicky.png` | 460x460 PNG |

### 6. Concordance de mindset

| Vérification | Ce qui est validé |
|-------|-----------------|
| Grille de directives | Correspond aux publications et à la structure des modules |
| JSONs de domaine | conventions.json et work.json correspondent à l'état réel |
| Tableau d'évolution | A des entrées récentes |
| Références de version | `knowledge-version: vN` correspond à la version actuelle |

### 7. Concordance de branche

| Vérification | Comment |
|-------|----------------|
| Branche par défaut | `git remote show origin \| grep 'HEAD branch'` |
| Source GitHub Pages | Rapporte la configuration attendue |
| Cible des PRs | Vérifie que les PRs ciblent la branche par défaut |

---

## Format de sortie

```
=== Rapport Normalize ===

Concordance de structure :
  ✓  22 paires de pages EN/FR trouvées
  ✓  Tous les hubs lient leurs sous-pages
  ✗  /fr/publications/webcards-social-sharing/full/ — lien retour manquant

Concordance de layout :
  ✓  Toutes les pages ont le front matter requis

Concordance webcard :
  ✓  20 GIFs OG trouvés (10 pages × 2 langues)

Concordance des liens :
  ✓  Liens de la landing page valides
  ✗  /publications/index.md:15 — chemin codé en dur

Concordance des assets :
  ✓  Aperçu social existe

Concordance de mindset :
  ✓  Tableau des publications à jour

Concordance de branche :
  ✓  Branche par défaut : main

Résumé : 28 vérifications réussies, 2 problèmes trouvés
```

---

## Comment les corrections sont appliquées

Avec `--fix` :

| Type de problème | Auto-corrigeable | Comment |
|-----------|-------------|-----|
| Champ front matter manquant | Oui | Ajout avec valeur par défaut |
| Lien de bascule de langue manquant | Oui | Ajout du lien vers la page miroir |
| Chemin codé en dur | Oui | Remplacement par `relative_url` |
| Référence GIF OG manquante | Partiel | `og_image` ajouté (GIF généré séparément) |
| Page miroir FR manquante | Non | Rapporté — la traduction nécessite une révision humaine |
| Entrée d'index manquante | Oui | Ajout suivant le pattern existant |
| Entrée de profil manquante | Oui | Ajout de ligne au tableau |
| Mindmap/JSONs obsolètes | Oui | Ajout des entrées manquantes |

**Livraison semi-automatique** : Comme toutes les opérations d'écriture, les corrections sont commitées sur la branche de tâche avec une PR ciblant la branche par défaut.

---

## Quand l'exécuter

| Déclencheur | Pourquoi |
|---------|-----|
| Après l'ajout de pages | Assurer les miroirs EN/FR, front matter, images OG |
| Après l'ajout de publications | Assurer la structure 3 niveaux, entrées d'index |
| Avant de créer une PR | Détecter les problèmes avant main |
| Au démarrage de session (dépôt knowledge) | Auto-vérification via `/mind-context` |
| Après promotion vers les JSONs de domaine | Nouvelles entrées conventions.json/work.json |
| Après génération `webcard` | Vérifier les GIFs et références |
| Après `pub new` | Vérifier que le scaffold est complet |

---

## Intégration avec les autres commandes

| Commande | Comment elle utilise normalize |
|---------|----------------------|
| Démarrage de session | Vérification implicite quand le dépôt knowledge est actif |
| `pub check` | Utilise les règles de validation pour les publications |
| `docs check` | Utilise la logique de validation de page |
| commit+push | Normalize recommandé avant le commit |
| K_GITHUB sync | Vérifie la cohérence des mises à jour du tableau de bord |
| `webcard` | Vérifie les références après génération |

---

## Publications liées

| # | Publication | Relation |
|---|-------------|----------|
| 0 | [Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — normalize fait partie du système |
| 5 | [Webcards & Partage social]({{ '/fr/publications/webcards-social-sharing/' | relative_url }}) | Normalize vérifie la concordance webcard |
| 4a | [Tableau de bord]({{ '/fr/publications/distributed-knowledge-dashboard/' | relative_url }}) | Normalize vérifie la cohérence du tableau de bord |
| 4 | [Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) | Normalize vérifie les références satellites |
| 14 | [Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | Conception architecture multi-module |
| 0v2 | [Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }}) | Référence architecture multi-module K2.0 |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
