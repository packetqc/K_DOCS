---
layout: publication
title: "Story #24 — Le Toggle : Restructuration de Knowledge avec filet de sécurité"
description: "Comment une stratégie de migration satellite-en-premier a transformé une restructuration risquée du dépôt en une opération validée et réversible — 852 fichiers déplacés, 158 chemins recartographiés, zéro bris."
pub_id: "Publication #11 — Story #24"
version: "v1"
date: "2026-03-10"
permalink: /fr/publications/success-stories/story-24/
keywords: "histoire de succès, restructuration knowledge, migration, toggle, satellite, dry-run"
---

# Story #24 — Le Toggle : Restructuration de Knowledge avec filet de sécurité

> **Publication parente** : [#11 — Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }})

---

<div class="story-section">

## Le problème

Le dépôt knowledge avait grandi de manière organique — `scripts/`, `methodology/`, `notes/`, `publications/`, `docs/`, `live/`, `evidence/`, `patterns/`, `lessons/`, `minds/`, `projects/`, `profile/`, `assets/` — tout au niveau racine. Quinze répertoires en compétition pour l'attention. Les satellites bootstrappés depuis cette structure héritaient de l'étalement.

Le jonglage de versions core/satellite (`<!-- knowledge-version: v47 -->`) ajoutait de la friction sans valeur. Chaque satellite devait savoir à quelle version il était, ce qui manquait, ce qui avait dérivé. Comptabilité manuelle déguisée en automatisation.

L'objectif : un seul répertoire `knowledge/` avec des subdivisions claires. Moteur séparé des données. Méthodologie séparée de la présentation. État d'exécution séparé de tout.

## L'approche — Toggle

Au lieu de restructurer le core en direct en espérant que rien ne casse, utiliser une **stratégie toggle** :

1. Construire le script de migration sur la branche core
2. **Fusionner vers main** avant de partager (piège #25 — appris à la dure, eu un 404)
3. Déposer le script sur un satellite, l'exécuter, valider
4. Si le satellite fonctionne → appliquer au core avec confiance

Le script de migration (`knowledge_migrate.py`) est auto-contenu. Un seul fichier. Télécharger, `chmod +x`, exécuter. Quatre étapes :

- **Détecter** les indicateurs hérités (tags de version, structure plate, scripts à la racine)
- **Restructurer** en `knowledge/` (moteur, méthodologie, données, web, état)
- **Recartographier** 158+ références de chemins dans CLAUDE.md et tous les skills
- **Commit & push**

## Les chiffres

| Métrique | Valeur |
|--------|-------|
| Fichiers déplacés | 852 |
| Références de chemins recartographiées | 158 (skills + CLAUDE.md) |
| URLs GitHub mises à jour | 44 (publications EN + FR) |
| Répertoires racine éliminés | 15 → 1 (`knowledge/`) |
| Fichiers restant à la racine | 4 (CLAUDE.md, README.md, LICENSE, .gitignore) |
| JSONs d'exécution séparés | 43 (notes/ → knowledge/state/sessions/) |
| Temps de migration satellite | Une seule commande, un seul commit |
| Bris | Zéro |

## Le résultat

```
repo/
├── CLAUDE.md
├── README.md
├── LICENSE
├── .claude/skills/
└── knowledge/
    ├── engine/        # scripts, live, config
    ├── methodology/   # 40+ docs, leçons, patterns
    ├── data/          # notes, projets, minds, publications
    ├── web/           # docs, assets, profil
    └── state/         # sessions d'exécution
```

## Ce qui a fait fonctionner

**Mode safe-boot** — Le script de restructuration a un flag `--safe-boot` qui déplace tout *sauf* CLAUDE.md et `.claude/`. Les fichiers de boot dont Claude Code dépend restent intouchés pendant la première passe. Le recartographiage des chemins se fait comme une étape séparée. Migration en deux phases, chacune vérifiable indépendamment.

**Le toggle** — Le satellite valide avant que le core ne commette. Si le satellite casse, le core est intouché. Si ça fonctionne, vous savez que la migration est sûre. Le satellite est le canari.

**Piège #25** — Nous avons publié l'URL de téléchargement avant de fusionner vers main. Le satellite a eu un 404. Maintenant documenté : toujours PR+fusion avant de partager des URLs GitHub brutes. Contrainte de séquencement, pas optionnelle.

**Recartographiage mécanique** — Pas de rechercher-remplacer manuel à travers 28 fichiers. Le script `remap_paths.py` a des règles déterministes : `scripts/` → `knowledge/engine/scripts/`, `methodology/` → `knowledge/methodology/`, etc. Exécutez-le deux fois, obtenez le même résultat. Idempotent.

</div>

---

> *La meilleure migration est celle où vous pouvez prouver qu'elle fonctionne avant de vous y engager.*
