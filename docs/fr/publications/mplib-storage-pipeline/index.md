---
layout: publication
title: "MPLIB Storage — Ingestion SQLite haute performance sur Cortex-M55"
description: "Pipeline 5 étapes atteignant ~2 650 logs/sec soutenus sur ARM Cortex-M55 bare-metal (STM32N6570-DK). Double tampon PSRAM, SQLite mode WAL, interface GUI zéro-SQL, ThreadX RTOS."
pub_id: "Publication #1"
version: "v1"
date: "2026-02-19"
permalink: /fr/publications/mplib-storage-pipeline/
og_image: /assets/og/mplib-pipeline-fr-cayman.gif
keywords: "embarqué, SQLite, RTOS, ThreadX, pipeline, double tampon, PSRAM"
---

# MPLIB Storage — Ingestion SQLite haute performance sur Cortex-M55
{: #pub-title}

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Vue d'ensemble et résumé du pipeline |
| [Métriques clés](#métriques-clés) | Débit, mémoire et chiffres de cache |
| [Architecture](#architecture) | Pipeline 5 étapes et séparation frontend/backend |
| [Pile technologique](#pile-technologique) | MCU, RTOS, base de données et stockage |

## Résumé

MPLIB Storage est un pipeline d'ingestion de logs SQLite haute performance conçu pour les systèmes ARM Cortex-M55 bare-metal. Fonctionnant sur le STM32N6570-DK (800 MHz), il atteint **~2 650 logs/sec soutenus** sur plus de 400 000 lignes grâce à une architecture pipeline 5 étapes avec double tampon PSRAM, SQLite en mode WAL, et une interface GUI zéro-SQL.

## Métriques clés

| Métrique | Valeur |
|----------|--------|
| Débit d'écriture soutenu | ~2 650 logs/sec |
| Total de lignes testées | 400 000+ |
| Taille struct log | 224 octets, aligné 32 octets |
| Mémoire paire de tampons | 7,2 Mo (PSRAM) |
| Tas SQLite | 512 Ko (memsys5) |
| Cache de pages | 4 Mo (~965 pages) |

## Architecture

**Pipeline 5 étapes** : Génération → DoubleTampon (PSRAM) → Ingestion (SQLite) → Moteur WAL → Carte SD

**Séparation frontend/backend** : Le thread GUI n'exécute jamais de SQL — il lit depuis un tampon PSRAM peuplé par le thread backend. Cache de prélecture à 4 emplacements (suivant/précédent/premier/dernier) masquant la latence des requêtes.

## Pile technologique

| Composant | Technologie |
|-----------|------------|
| MCU | STM32N6570-DK (Cortex-M55 @ 800 MHz) |
| RTOS | ThreadX |
| Interface | TouchGFX |
| Base de données | SQLite 3 (mode WAL, allocateur memsys5) |
| Stockage | Carte SD via SDMMC2 / FileX |

---

[**Lire la documentation complète →**]({{ '/fr/publications/mplib-storage-pipeline/full/' | relative_url }})

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
