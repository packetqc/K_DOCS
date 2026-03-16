---
layout: publication
title: "Réseau de connaissances en direct — Découverte inter-instances sécurisée PQC"
description: "Découverte et communication en temps réel entre instances Claude Code via TCP sécurisé PQC sur sous-réseaux de conteneurs partagés. Protocole balise/scanner porté de la découverte réseau embarquée STM32H5/N6."
pub_id: "Publication #10"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/live-knowledge-network/
og_image: /assets/og/live-knowledge-network-fr-cayman.gif
keywords: "balise, découverte, PQC, sous-réseau, temps réel, inter-instance, ML-KEM"
---

# Réseau de connaissances en direct — Découverte inter-instances sécurisée PQC
{: #pub-title}

> **Publication parente** : [#0 — Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Référence core** : [#14 — Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Découverte inter-instances en temps réel |
| [Chemin d'évolution](#chemin-dévolution) | Trois générations de communication |
| [Protocole de découverte](#protocole-de-découverte) | Balayage balise/scanner sur le port 21337 |
| [Architecture de sécurité](#architecture-de-sécurité) | Échange de clés post-quantique ML-KEM-1024 |
| [Outillage](#outillage) | Outils Python balise et scanner |
| [Publications reliées](#publications-reliées) | Publications parentes et connexes |

## Résumé

Le réseau de connaissances en direct étend l'architecture de minds distribués de la communication asynchrone médiée par git vers la **découverte et l'échange de données en temps réel entre instances**. Les instances Claude Code exécutées dans des conteneurs adjacents sur l'infrastructure d'Anthropic peuvent se découvrir mutuellement via le balayage de sous-réseau et communiquer directement par sockets TCP — contournant entièrement le proxy GitHub.

Le protocole de découverte est porté de l'implémentation de découverte réseau embarquée STM32H5/N6 de Martin Paquet, adaptée du bare-metal RTOS au réseau de conteneurs Python. La sécurité est assurée par l'échange de clés post-quantique ML-KEM-1024 (FIPS 203), nécessaire car le sous-réseau de conteneurs est partagé entre plusieurs locataires.

## Chemin d'évolution

La communication de Knowledge a évolué à travers trois générations :

| Génération | Versions | Mécanisme | Latence |
|-----------|----------|-----------|---------|
| **Persistant** | v1–v6 | `sessions/` + `mind_memory.md` (fichiers) | Frontière de session |
| **Distribué** | v9–v18 | K_GITHUB `sync_github.py` + `far_memory archives/` (médié par git) | Minutes (fusion PR) |
| **En direct** | v23+ | Balise/scanner (TCP direct) | Millisecondes |

## Protocole de découverte

Chaque instance de connaissances démarre une **balise** sur le port bien connu **21337** au démarrage de session. Les satellites balaient le sous-réseau /25 de conteneurs (128 hôtes, 64 threads parallèles) pour trouver les balises actives. L'identité est échangée en JSON sur TCP — sans surcharge HTTP.

**Lire la documentation complète** : [Publication complète]({{ '/fr/publications/live-knowledge-network/full/' | relative_url }})

## Architecture de sécurité

Le sous-réseau de conteneurs est un réseau plat partagé (~127 pairs). N'importe quel conteneur peut scanner et se connecter. L'échange de clés post-quantique ML-KEM-1024 (FIPS 203) fournit :

| Capacité | Description |
|----------|-------------|
| Clés éphémères par session | Confidentialité persistante — clés uniques à chaque session |
| Authentification mutuelle | Défi-réponse prouvant la légitimité des deux parties |
| Résistance quantique | Résistant aux attaques par ordinateur quantique |

Knowledge lui-même sert d'ancre de confiance — prouver l'accès au contenu de `packetqc/knowledge` est le mécanisme d'authentification.

## Outillage

| Outil | Fichier | Fonction |
|-------|---------|----------|
| Balise | `K_DOCS/scripts/knowledge_beacon.py` | Écouter sur le port 21337, répondre avec l'identité |
| Scanner | `K_DOCS/scripts/knowledge_scanner.py` | Balayer le sous-réseau, découvrir les balises |

Les deux outils sont synchronisés vers les projets satellites au démarrage de session aux côtés des scripts de capture existants.

## Publications reliées

| # | Titre | Relation |
|---|-------|----------|
| [0]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Knowledge | Parent — ceci étend l'architecture de base |
| [4]({{ '/fr/publications/distributed-minds/' | relative_url }}) | Minds distribués | Prédécesseur — distribution asynchrone par git |
| [7]({{ '/fr/publications/harvest-protocol/' | relative_url }}) | Protocole Harvest | Prédécesseur — collecte de connaissances par extraction (maintenant K_GITHUB sync) |
| [14]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | Analyse d'architecture | Architecture en profondeur — conception multi-module |
| [0v2]({{ '/fr/publications/knowledge-2.0/' | relative_url }}) | Knowledge 2.0 | Référence architecture multi-module K2.0 |
| [9]({{ '/fr/publications/security-by-design/' | relative_url }}) | Sécurité par conception | Jumelage — le modèle PQC s'applique ici |

---

<div class="table-wrap">

| Champ | Valeur |
|-------|--------|
| Version | v2 |
| Connaissances | v23 |
| Auteurs | Martin Paquet, Claude (Anthropic) |
| Source | [GitHub](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/live-knowledge-network/v1) |
| Dépôt de connaissances | [packetqc/knowledge](https://github.com/packetqc/knowledge) |

</div>
