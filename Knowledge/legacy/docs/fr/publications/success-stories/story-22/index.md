---
layout: publication
title: "Story #22 — Moteur de documentation visuelle : De la vidéo aux évidences en quelques secondes"
description: "Une vision de longue date réalisée — un moteur automatisé qui extrait des cadres d'évidence à partir d'enregistrements vidéo par vision par ordinateur, permettant l'enrichissement de la documentation directement à partir des enregistrements de sessions."
pub_id: "Publication #11 — Story #22"
version: "v1"
date: "2026-03-07"
permalink: /fr/publications/success-stories/story-22/
og_image: /assets/og/visual-documentation-fr-cayman.gif
keywords: "histoire de succès, documentation visuelle, évidences vidéo, OpenCV, extraction de cadres, reconstruction de clips, vision par ordinateur"
---

# Story #22 — Moteur de documentation visuelle : De la vidéo aux évidences en quelques secondes

> **Publication parente** : [#11 — Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }})

---

<div class="story-section">

> *« Je voulais ça depuis longtemps — la capacité de prendre un enregistrement vidéo d'une session de développement et d'en extraire automatiquement les moments clés sous forme d'images et de clips pour enrichir notre documentation. Aujourd'hui ça fonctionne. Chercher dans une vidéo de 2 heures, obtenir 5 cadres d'évidence et leur contexte vidéo, organisés dans un répertoire prêt pour la documentation. »*

<div class="story-row">
<div class="story-row-left">

**Détails**

</div>
<div class="story-row-right">

| | |
|---|---|
| Date | 2026-03-07 |
| Catégorie | 🚀 ⚙️ |
| Contexte | Les flux de développement génèrent des heures d'enregistrements vidéo — captures d'écran, sessions UART, démos, artefacts CI/CD. Extraire des cadres utiles de ces enregistrements était entièrement manuel : parcourir la vidéo, faire pause au bon moment, capturer, organiser, annoter. Pour les longs enregistrements, ce processus était impraticable. L'utilisateur avait envisagé une solution automatisée depuis des mois — un système capable de balayer des fichiers vidéo, de trouver ce qui compte, et de produire des évidences organisées prêtes pour la documentation. |
| Déclenché par | Issue [#556](https://github.com/packetqc/knowledge/issues/556) — L'utilisateur a décrit la vision : recherche multi-critères directement sur les fichiers vidéo, répertoires d'évidences organisés avec découvertes et clips, et l'objectif en aval d'enrichir la documentation avec des évidences visuelles extraites automatiquement. |
| Rédigé par | **Claude** (Anthropic, Opus 4.6) — à partir des données de session en direct |

</div>
</div>

<div class="story-row">
<div class="story-row-left">

**Ce qui s'est passé**

</div>
<div class="story-row-right">

1. **La vision** — L'utilisateur a articulé un besoin accumulé depuis des mois : les enregistrements vidéo contiennent des évidences critiques (états d'interface, écrans d'erreur, sortie UART, changements de configuration), mais extraire ces évidences était entièrement manuel. L'objectif : un moteur qui traite les fichiers vidéo par vision par ordinateur et produit des évidences organisées — sans services cloud, sans outils externes, bibliothèques Python standard uniquement.

2. **Accès vidéo direct** — Au lieu de l'approche naïve d'extraction de tous les cadres sur disque (ce qui consommerait des gigaoctets pour une longue vidéo), l'utilisateur a suggéré de travailler directement sur le fichier vidéo. Le moteur navigue vers des positions spécifiques avec `cv2.VideoCapture.set()` — seuls les cadres correspondants sont sauvegardés.

3. **Architecture de recherche multi-passes** — Le moteur effectue un balayage intelligent en deux passes : Passe 1 (grossière) toutes les ~1 secondes évaluant tous les critères simultanément ; Passe 2 (fine) raffine autour de chaque résultat image par image. Quatre heuristiques combinables : changement de scène, densité de texte, densité de contours et contenu structuré.

4. **Structure d'évidences** — Les résultats sont organisés dans une structure de répertoire dédiée : `discoveries/` pour les cadres, `clips/` pour les segments vidéo, `metadata.json` pour les données machine, et `index.md` pour l'inventaire humain.

5. **Reconstruction de clips** — Au-delà des cadres statiques, le moteur reconstruit des clips `.mp4` autonomes centrés autour des timestamps d'évidences. Avec `cv2.VideoWriter`, il extrait ±N secondes de contexte autour de chaque découverte.

6. **Validation en direct** — Le moteur a été testé sur un vrai enregistrement du système Knowledge (démo du Main Navigator, 1920×1080, 30fps, 65.8s). Le mode recherche a trouvé des cadres d'évidence, la reconstruction de clips a produit des segments MP4 jouables, et la structure d'évidences a été générée avec métadonnées et index.

7. **Découverte de l'affichage en ligne** — Pendant les tests, le défi de montrer les résultats à l'utilisateur a mené à découvrir que les liens d'images markdown via `raw.githubusercontent.com` fonctionnent de manière fiable sur l'application mobile Claude. Ceci est devenu un protocole d'affichage documenté.

</div>
</div>

<div class="story-row">
<div class="story-row-left">

**Ce que ça a validé**

</div>
<div class="story-row-right">

| Qualité | Comment |
|---------|---------|
| **Autosuffisant** (#1) | Zéro dépendance externe — OpenCV + Pillow + NumPy uniquement |
| **Autonome** (#2) | Le moteur auto-organise la sortie — répertoire d'évidences créé automatiquement |
| **Évolutif** (#6) | A grandi de l'extraction de cadres à la détection, puis recherche, clips, analyse d'images |
| **Concis** (#4) | Accès vidéo direct au lieu d'extraction en masse. 5 cadres, pas 216 000 fichiers temporaires |
| **Intégré** (#13) | Les évidences alimentent directement la documentation. Affichage en ligne via GitHub |

</div>
</div>

<div class="story-row">
<div class="story-row-left">

**Métrique**

</div>
<div class="story-row-right">

Un enregistrement 1080p de 65.8 secondes a été recherché avec multi-critères en moins de 30 secondes. Le moteur a extrait des cadres annotés, reconstruit des clips vidéo, et organisé le tout dans un répertoire structuré — un processus qui prendrait 15-20 minutes manuellement.

**Pile technologique** : ~1 200 lignes de Python. Six modes d'opération. Quatre heuristiques de détection. Déduplication par hachage perceptuel. Planches-contact. Rapports d'évidences. Le tout avec trois bibliothèques standard.

</div>
</div>

</div>

---

> **Connexe** : [Publication #22 — Documentation visuelle]({{ '/fr/publications/visual-documentation/' | relative_url }}) · [Publication #2 — Analyse de session en direct]({{ '/fr/publications/live-session-analysis/' | relative_url }}) · [Publication #16 — Visualisation de pages web]({{ '/fr/publications/web-page-visualization/' | relative_url }})

---

*Story #22 — Moteur de documentation visuelle*
*Martin Paquet & Claude (Anthropic, Opus 4.6) — Mars 2026*
