---
layout: publication
title: "Analyse de session en direct — Débogage temps réel assisté par IA pour systèmes embarqués"
description: "Méthodologie de QA en temps réel : capture vidéo en direct de la carte STM32 → analyse de trames par IA → détection d'anomalies → investigation forensique. 4 modes : direct, statique, multi-direct, hybride profond."
pub_id: "Publication #2"
version: "v1"
date: "2026-02-19"
permalink: /fr/publications/live-session-analysis/
og_image: /assets/og/live-session-fr-cayman.gif
keywords: "session en direct, analyse vidéo, UART, extraction d'images, OBS, temps réel"
---

# Analyse de session en direct — Débogage et QA temps réel assistés par IA pour systèmes embarqués
{: #pub-title}

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Vue d'ensemble du mécanisme de débogage en direct |
| [Le pipeline](#le-pipeline) | Flux de capture et d'analyse bout en bout |
| [Quatre modes d'analyse](#quatre-modes-danalyse) | Direct, statique, multi-direct et hybride profond |
| [Résultats prouvés](#résultats-prouvés) | Bugs trouvés et compression de vitesse 3x |

## Résumé

Un mécanisme d'analyse de session en direct pour le débogage et l'assurance qualité temps réel des systèmes embarqués. Capture la sortie écran d'une carte de développement en fonctionnement via streaming RTSP, encode des clips H.264 roulants, et les livre via Git à un agent IA pour analyse multimodale des trames.

L'ingénieur pilote la carte en temps réel pendant que l'IA surveille continuellement la sortie visuelle, rapporte les changements d'état, détecte les anomalies et escalade vers une analyse forensique trame par trame lorsque quelque chose d'inattendu apparaît. **~6 secondes de latence** entre le changement d'état de la carte et le retour IA.

## Le pipeline

```
Carte STM32 → OBS/RTSP → Encodage H.264 → Push Git auto → Claude pull → Analyse de trames → Rapport d'état
   (5-8 secondes bout en bout)
```

## Quatre modes d'analyse

| Mode | Déclencheur | Action |
|------|-------------|--------|
| **Direct** | `I'm live` | Pull du dernier clip, extraction dernière trame, rapport d'état UI |
| **Statique** | `analyze <chemin>` | Échantillonnage de trames clés, chronologie de progression d'état |
| **Multi-direct** | `multi-live` | Validation croisée : UI + UART + caméra simultanément |
| **Hybride profond** | `deep <description>` | Forensique trame par trame sur anomalie détectée |

## Cycle de vie des clips et agent de session

Au-delà des 4 modes d'analyse, le mécanisme inclut la **gestion du cycle de vie des clips** (modes discard vs capture avec `clip_discard.py`) et un **SessionAgent** pour la synchronisation temps réel des billets GitHub avec les avatars Vicky Viking (NPC = Martin, AWARE avec lunettes de soleil = Claude).

## Résultats prouvés

| Résultat | Détail |
|----------|--------|
| 2 bugs dépendants du timing | Trouvés et corrigés en une seule session d'1 heure |
| Condition de course persistance config | Détectée en comparant les trames pré/post-redémarrage |
| Corruption de rendu de caractères | Détectée par l'IA lisant du texte altéré dans les clips en direct |
| Compression de vitesse 3x | Mesurée vs débogage traditionnel |

---

[**Lire la documentation complète →**]({{ '/fr/publications/live-session-analysis/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
