---
layout: default
title: "Interfaces"
description: "Interfaces web interactives du système de connaissances — outils dynamiques pour la révision de sessions, la navigation et la gestion du système."
permalink: /fr/interfaces/
og_image: /assets/og/interfaces-hub-fr-cayman.gif
---

# Interfaces

Applications web interactives construites sur l'infrastructure de publication Knowledge. Les interfaces partagent le même pipeline d'exportation que les publications (PDF/DOCX) mais sont des outils dynamiques en JavaScript plutôt que de la documentation statique.

---

## Interfaces disponibles

| ID | Interface | Description |
|----|-----------|-------------|
| I1 | [Révision de sessions]({{ '/fr/interfaces/session-review/' | relative_url }}) | Visualiseur interactif de sessions — sélectionnez une session et explorez son résumé, métriques, compilation temporelle, livraisons et leçons apprises. |
| I2 | [Navigateur principal]({{ '/fr/interfaces/main-navigator/' | relative_url }}) | Interface de navigation à trois panneaux — parcourez toutes les publications, profils et commandes avec visualiseur de contenu intégré. |
| I3 | [Flux de travail des tâches]({{ '/fr/interfaces/task-workflow/' | relative_url }}) | Visualiseur de flux de travail — suivez la progression des tâches à travers 8 étapes, résultats de validation et tests unitaires. |
| I4 | [Visualiseur de projets]({{ '/fr/interfaces/project-viewer/' | relative_url }}) | Visualiseur de projets — parcourez les projets, suivez la complétion des tâches, agrégez métriques et scores de grille Knowledge. |

---

## Interface vs Publication

| Aspect | Publication | Interface |
|--------|-------------|-----------|
| Contenu | Documentation markdown statique | Application JavaScript dynamique |
| Interactivité | Minimale (thème, table des matières) | Riche (visualiseurs de données, graphiques, navigation) |
| Webcard | GIF OG animé par page | GIF OG animé — partage social uniquement (non affiché sur la page) |
| Barre de langue | Bascule EN/FR auto-générée | Aucune — bilingue géré en interne |
| Exportation | PDF/DOCX via CSS Paged Media | Même pipeline d'exportation |
| Layout | `publication` | `publication` avec `page_type: interface` |
| Chemin URL | `/publications/<slug>/` | `/interfaces/<slug>/` |
| Numérotation | `#<n>` | `I<n>` |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
