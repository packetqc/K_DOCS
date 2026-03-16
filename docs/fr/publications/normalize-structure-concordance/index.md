---
layout: publication
title: "Normalize & Concordance structurelle — Architecture de connaissances auto-réparatrice"
description: "La commande normalize audite et renforce la concordance de Knowledge : miroirs bilingues, validation du front matter, références webcard, intégrité des liens, synchronisation des assets et actualité du mind_memory.md. Un linter pour l'architecture de connaissances."
pub_id: "Publication #6"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/normalize-structure-concordance/
og_image: /assets/og/normalize-fr-cayman.gif
keywords: "normaliser, concordance, structure, validation, bilingue, audit"
---

# Normalize & Concordance structurelle
{: #pub-title}

> **Publication parente** : [#0 — Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }})
>
> **Référence core** : [#14 — Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Vue d'ensemble de l'architecture auto-réparatrice |
| [Ce que normalize vérifie](#ce-que-normalize-vérifie) | Les 7 catégories de concordance |
| [Utilisation](#utilisation) | Syntaxe et modes de commande |
| [Règles de concordance](#règles-de-concordance) | Résumé de toutes les règles de validation |
| [Quand l'exécuter](#quand-lexécuter) | Déclencheurs et moment recommandé |
| [Comment les corrections sont appliquées](#comment-les-corrections-sont-appliquées) | Comportement auto-fix et limites |
| [Intégration avec les autres commandes](#intégration-avec-les-autres-commandes) | Interaction avec les autres commandes |

## Résumé

À mesure que Knowledge grandit — nouvelles pages, publications, miroirs bilingues, variations de profil, webcards OG — des incohérences structurelles apparaissent inévitablement. Une page française sans miroir anglais. Une page de profil qui oublie de lister la dernière publication. Une référence d'image OG pointant vers un GIF inexistant.

La commande `normalize` est la **couche d'auto-réparation** de l'architecture de connaissances. Elle audite l'ensemble du dépôt contre 7 catégories de règles de concordance et rapporte (ou corrige) chaque écart. Pensez-y comme un linter pour l'architecture de connaissances — pas la syntaxe du code, mais l'intégrité structurelle.

## Ce que normalize vérifie

| # | Catégorie | Ce qu'elle assure |
|---|----------|----------------|
| 1 | **Structure** | Chaque page EN a un miroir FR. Les hubs lient toutes les sous-pages. |
| 2 | **Layout** | Toutes les pages utilisent les bons layouts avec les champs front matter requis. |
| 3 | **Webcard** | Chaque page a un GIF OG animé et un `og_image` correct dans le front matter. |
| 4 | **Liens** | Les références croisées sont cohérentes — landing, index, profils interliés. |
| 5 | **Assets** | Les assets requis existent (aperçu social, GIFs OG, portraits). |
| 6 | **Mindset** | mind_memory.md reflète l'état actuel — publications, évolution, structure des modules. |
| 7 | **Branche** | Branche par défaut détectée, GitHub Pages configuré, PRs ciblant correctement. |

## Utilisation

```
normalize              # Rapport seulement (par défaut)
normalize --check      # Rapport seulement, pas de changements
normalize --fix        # Appliquer les corrections automatiquement
```

## Règles de concordance

| Catégorie | Règle |
|-----------|-------|
| **Structure** | Chaque page doit avoir son miroir EN/FR. Les publications suivent la structure 3 niveaux (source, résumé, complet). Les hubs lient toutes les sous-pages ; les sous-pages lient en retour. |
| **Layout** | Toutes les pages nécessitent `layout`, `title`, `description`, `permalink`, `og_image` dans le front matter. Les publications nécessitent en plus `pub_id`, `version`, `date`. |
| **Webcard** | Le `og_image` de chaque page doit pointer vers un `.gif` existant dans `docs/assets/og/`. Les variantes EN et FR doivent exister. Les layouts doivent émettre les balises méta `og:image`, `twitter:image` et `<link rel="canonical">`. |
| **Liens** | Pas de chemins codés en dur — tous les liens internes utilisent le filtre `relative_url`. Bascule de langue présente sur chaque page. Références croisées cohérentes entre index, profil et publications. |
| **Assets** | Aperçu social PNG, GIFs OG, photo portrait et avatar Vicky existent aux chemins attendus. |
| **Mindset** | La grille de directives de mind_memory.md, les JSONs de domaine et les entrées d'évolution correspondent à l'état réel du dépôt. |
| **Branche** | Branche par défaut détectée via `git remote show origin`. Les PRs la ciblent. GitHub Pages publie depuis celle-ci. |

## Quand l'exécuter

| Déclencheur | Pourquoi |
|-------------|----------|
| Après l'ajout de pages ou publications | Assurer les miroirs EN/FR, front matter, images OG |
| Avant de créer une PR | Détecter les problèmes avant la branche par défaut |
| Au démarrage de session (dépôt knowledge) | Auto-vérification via `/mind-context` |
| Après promotion vers les JSONs de domaine | Nouvelles entrées conventions.json/work.json à valider |
| Après la génération de `webcard` | Vérifier les GIFs et leurs références front matter |

## Comment les corrections sont appliquées

Avec `--fix` : les champs front matter manquants reçoivent des valeurs par défaut, les chemins codés en dur reçoivent `relative_url`, les entrées d'index manquantes sont ajoutées. Les pages miroir FR manquantes sont **rapportées mais pas corrigées automatiquement** (la traduction nécessite une révision humaine). Comme toutes les opérations d'écriture, les corrections sont commitées sur la branche de tâche avec une PR ciblant la branche par défaut.

## Intégration avec les autres commandes

`pub check` et `docs check` utilisent les règles de validation de normalize. Le démarrage de session exécute une vérification implicite quand le dépôt knowledge est actif. Le commit+push bénéficie d'une exécution de normalize avant le commit.

---

[**Lire la documentation complète →**]({{ '/fr/publications/normalize-structure-concordance/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
