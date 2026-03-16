---
layout: publication
title: "Story #25 — Mémoire Mindmap Vivante : Du diagramme statique au graphe de connaissances interactif"
description: "Comment le mindmap K_MIND a évolué d'un diagramme mermaid statique à un graphe de connaissances interactif MindElixir avec filtrage de profondeur, synchronisation de thèmes et récupération en temps réel depuis GitHub."
pub_id: "Publication #11 — Story #25"
version: "v1"
date: "2026-03-15"
permalink: /fr/publications/success-stories/story-25/
og_image: /assets/og/knowledge-system-en-cayman.gif
keywords: "histoire de succès, mindmap, MindElixir, interactif, graphe de connaissances, filtrage de profondeur, thèmes"
---

# Story #25 — Mémoire Mindmap Vivante : Du diagramme statique au graphe de connaissances interactif

> **Publication parente** : [#11 — Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }})

---

<div class="story-section">

> *« Le mindmap a commencé comme un fichier texte rendu par mermaid. Maintenant c'est un graphe de connaissances vivant et interactif qu'on peut déplacer, zoomer et explorer — récupéré en temps réel du dépôt, filtré par profondeur selon la configuration, et thématisé pour correspondre au visualiseur. L'esprit est devenu visible. »*

<div class="story-row">
<div class="story-row-left">

**Détails**

</div>
<div class="story-row-right">

| | |
|---|---|
| Date | 2026-03-15 |
| Catégorie | 🧠 🎨 ⚙️ |
| Contexte | K_MIND stocke sa mémoire opérationnelle sous forme d'un mindmap mermaid dans `mind_memory.md`. Ce fichier est le subconscient du système — chaque nœud est une directive. Mais le visualiser nécessitait le rendu de diagrammes mermaid statiques. L'objectif : rendre le graphe de connaissances explorable, interactif et toujours à jour. |
| Déclenché par | La construction de la section K2.0 sur « La Mémoire Mindmap » — le rendu mermaid statique semblait inadéquat pour expliquer un système vivant. Le mindmap devait *être* vivant. |
| Rédigé par | **Claude** (Anthropic, Opus 4.6) — à partir des données de session en direct |

</div>
</div>

## L'évolution — Trois phases

### Phase 1 : Mermaid statique (référence)

Le mindmap n'existait que comme bloc de code mermaid dans `mind_memory.md`. Claude le rendait via la sortie du skill `/mind-context`. Les utilisateurs pouvaient le voir mais pas interagir avec. Pas de zoom, pas de déplacement, pas d'exploration.

### Phase 2 : Mermaid interactif personnalisé (v2)

Construction d'une interface I5 autonome qui :
- Récupère `mind_memory.md` depuis GitHub en temps réel
- Applique le filtrage de profondeur (portage JS de `mindmap_filter.py`)
- Rend via mermaid.js avec des gestionnaires personnalisés de déplacement/zoom/clic
- Ajoute un menu déroulant Normal/Complet
- Clic sur un nœud → affichage du chemin en fil d'Ariane

**La limitation** : Toute l'interactivité était construite à la main — glisser pour déplacer, molette pour zoomer, pincement tactile, superpositions SVG rect pour les surlignages. Des centaines de lignes de code de gestion d'événements personnalisé. Fragile. Pas de glisser-déposer. Pas d'animations fluides.

### Phase 3 : MindElixir (v3) — Actuel

Remplacement de toute l'implémentation personnalisée par **MindElixir v5.9.3** — une bibliothèque dédiée au mind mapping :

| Fonctionnalité | Personnalisé v2 | MindElixir v3 |
|---------|-----------|---------------|
| Déplacement | Gestionnaires mousedown/move personnalisés | Intégré |
| Zoom | Gestionnaires molette + pincement personnalisés | Intégré avec animation fluide |
| Interaction nœuds | Superpositions SVG rect personnalisées | Sélection + focus intégrés |
| Support tactile | touchstart/move/end personnalisés | Intégré |
| Support thèmes | Aucun | 4 thèmes synchronisés avec le visualiseur |
| Complexité du code | ~400 lignes JS personnalisées | ~50 lignes de configuration |
| Glisser-déposer | Impossible | Intégré (désactivé pour le visualiseur) |

## Le pipeline de filtrage de profondeur

Le mindmap contient 140+ nœuds répartis sur 6 groupes. Tout afficher surcharge. Le système de filtrage de profondeur contrôle la visibilité :

```
mind_memory.md → depth_config.json → filterMindmap() → données MindElixir → rendu
```

- `default_depth: 3` — afficher 3 niveaux de profondeur par défaut
- `omit: ["architecture", "constraints"]` — masquer les détails d'implémentation en mode normal
- `overrides: {"session/near memory": 4}` — contrôle de profondeur par branche
- **Mode complet** : tous les nœuds développés à la profondeur maximale

Le filtre s'exécute en JavaScript (porté depuis Python `mindmap_filter.py`), convertissant le texte indenté mermaid en arbre JSON MindElixir `{topic, id, children}`.

## Synchronisation de thèmes — 4 thèmes

Les thèmes MindElixir correspondent directement au système de variables CSS du visualiseur :

| Thème visualiseur | Mapping MindElixir | Arrière-plan | Nœud racine |
|---|---|---|---|
| Cayman | Palette bleue, clair | `#eff6ff` | `#1d4ed8` |
| Midnight | Palette bleue, sombre | `#0f172a` | `#1e40af` |
| Daltonisme clair | Palette chaude, clair | `#faf6f1` | `#0055b3` |
| Daltonisme sombre | Palette chaude, sombre | `#1a1a2e` | `#2a4a7a` |

L'interface I5 inclut un menu déroulant de thèmes. Les instances embarquées détectent automatiquement depuis l'attribut `data-theme` du visualiseur ou `prefers-color-scheme`.

## Trois points de déploiement

Le mindmap vivant est rendu à trois endroits depuis la même source de données :

1. **Interface I5** — Page autonome complète avec menu déroulant de thèmes, bascule Normal/Complet, contrôles Centrer/Ajuster/Plein écran
2. **Publication K2.0** — Embarquement en ligne dans la Section 1 « La Mémoire Mindmap » avec thème automatique
3. **Webcard du visualiseur** — Carte de prévisualisation vivante quand `live_webcard: mindmap` est défini dans le front matter

Les trois récupèrent depuis `raw.githubusercontent.com`, appliquent le filtrage de profondeur, convertissent au format MindElixir et rendent avec les couleurs appropriées au thème.

## Ce que cela prouve

- **Mind-first est visible** : La mémoire opérationnelle n'est pas cachée — c'est un élément interactif de première classe
- **Bibliothèque plutôt que personnalisé** : 400 lignes de code personnalisé fragile → 50 lignes de configuration MindElixir avec une meilleure UX
- **Propagation des conventions** : Configuration de profondeur, système de thèmes et logique de filtrage sont partagés entre les trois points de déploiement
- **Temps réel par défaut** : Chaque rendu récupère les données actuelles du dépôt — le mindmap est toujours vivant

</div>

[**Validé**]({{ '/fr/publications/success-stories/story-25/' | relative_url }})

---
