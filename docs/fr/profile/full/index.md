---
layout: publication
title: "Martin Paquet — Sécurité réseau, Sécurité des systèmes, Logiciels embarqués (Français)"
description: "30 ans d'expérience pratique en systèmes embarqués, sécurité réseau, infrastructure télécom et développement logiciel. Cryptographie post-quantique, STM32 bare-metal, flux de travail assistés par IA."
pub_id: "Profil complet"
version: ""
date: "2026-02-17"
permalink: /fr/profile/full/
og_image: /assets/og/full-profile-fr-cayman.gif
---

# Martin Paquet

**Analyste et Programmeur Sécurité Réseau | Administrateur de Sécurité des Réseaux et des Systèmes | Analyste Programmeur et Concepteur Logiciels Embarqués**

30 ans d'expérience pratique en systèmes embarqués, sécurité réseau, infrastructure télécom et développement logiciel. Autodidacte et bâtisseur de nature.

---

## Coordonnées

| | |
|---|---|
| **Courriel** | packetqcca@gmail.com |
| **LinkedIn** | [martypacket](https://www.linkedin.com/in/martypacket) |
| **GitHub** | [packetqc](https://github.com/packetqc) |
| **Connaissances** | [packetqc/knowledge](https://github.com/packetqc/knowledge) |
| **YouTube** | [@packet-yi9sq](https://youtube.com/@packet-yi9sq) |
| **Localisation** | Québec, Canada |
| **Langues** | Français (natif), Anglais (professionnel) |

---

## Formation

**Université Laval** — Bachelier en Sciences Appliquées (BASc), Informatique de Génie, Analyste fonctionnel et programmeur (1992–1998)

---

## Focus actuel (R&D personnel)

### Recherche d'emploi (2026–maintenant)

En recherche active d'un poste tout en développant le projet Knowledge AI — un système d'intelligence d'ingénierie auto-évolutif qui capture 30 ans de cycle complet d'ingénierie en méthodologie réutilisable et automatisée. Utilise Knowledge pour économiser temps, énergie et concentration sur les projets. Tout projet peut être documenté et automatisé.

### Projet Knowledge AI (2026)

Système d'intelligence d'ingénierie auto-évolutif construit en fichiers Markdown dans Git — portable, autosuffisant, aucun service externe, aucun verrouillage fournisseur. Fournit une continuité des connaissances inter-sessions pour le développement assisté par IA à travers un cycle de vie structuré : wakeup, élévation, travail, sauvegarde. Incarne 13 qualités fondamentales : autosuffisant, autonome, concordant, concis, interactif, évolutif, distribué, persistant, récursif, sécuritaire, résilient, structuré, intégré. L'architecture de connaissances distribuées permet un flux bidirectionnel entre un dépôt central et des projets satellites — la méthodologie se propage vers l'extérieur au démarrage, les découvertes sont récoltées vers le centre. Gestion de projet automatisée, génération de documentation, publication web bilingue (GitHub Pages), aperçus sociaux animés et documentation de session en temps réel via les billets GitHub. 55 versions de connaissances, 23+ publications techniques, 550+ billets suivis et 13 histoires de réussite démontrent que 46 heures de collaboration assistée par IA livrent ce que les processus traditionnels d'entreprise prendraient 8–16 mois — couvrant le firmware embarqué, l'architecture de sécurité, l'intégration de tableaux de projet et la documentation bilingue complète. — <a href="{{ '/fr/interfaces/main-navigator/' | relative_url }}" target="_top">Knowledge</a>

### Cryptographie post-quantique pour embarqué (2025–maintenant)

ML-KEM 1024 (NIST niveau 5) et ML-DSA pour la protection des données en transit sur transport IP sécurisé ou non sécurisé. Données chiffrées par matériel AES GCM GMAC 256 en transport TCP. Migration du prototype d'échange de clés ECC vers PQC. Technologies : STM32, WolfSSL/WolfCrypt, CMOX, Azure Eclipse RTOS.

### Journalisation SQLite sécurisée sur Cortex-M55 (2026)

Pipeline d'ingestion de logs haute performance sur STM32N6570-DK (Cortex-M55 @ 800 MHz) sous ThreadX RTOS. 2 650 logs/sec soutenus avec double tampon PSRAM, SQLite mode WAL, liaisons zéro-copie. Interface TouchGFX zéro-SQL avec cache de prélecture à 4 emplacements. Chiffrement matériel SAES avec trois modes selon la sévérité. — [Publication]({{ '/fr/publications/mplib-storage-pipeline/' | relative_url }})

### Méthodologie de persistance de session IA (2026)

Continuité des connaissances inter-sessions pour l'ingénierie logicielle assistée par IA. CLAUDE.md + notes/ + protocole de cycle de vie donnant aux assistants IA une mémoire durable entre les sessions. Récupération de contexte en 30 secondes vs 15 minutes de ré-explication manuelle. Le dépôt [packetqc/knowledge](https://github.com/packetqc/knowledge) est lui-même la preuve. — [Publication]({{ '/fr/publications/ai-session-persistence/' | relative_url }})

### Analyse de session en direct (2026)

Capture vidéo temps réel de la carte STM32 en fonctionnement via streaming RTSP, livrée par Git à un agent IA pour analyse multimodale des trames. Quatre modes d'analyse : direct, statique, multi-direct, hybride profond. ~6 secondes de latence bout en bout. — [Publication]({{ '/fr/publications/live-session-analysis/' | relative_url }})

### Sécurité avancée pour STM32 embarqué (2023–maintenant)

Chiffrement matériel sur SDCARD et données. ECC KEM avec rafraîchissement périodique des clés. Composantes crypto matérielles : PKA, SAES, Hash, AES, TEE. Sous-systèmes multi-tâches avec interface TouchGFX, réseau ETH/WiFi, UART, Bluetooth, USB, SPI. Cartes de développement : STM32N6570-DK, STM32H573I-DK, STM32H743I-EVAL2. Outils : CubeMX, CubeIDE, TouchGFX.

### Projets IoT et embarqué (2020–2023)

- **ToxicAir / ToxiCare** — Moniteur de qualité de l'air Arduino AWS avec MQTT, capteurs Grove (poussière, alcool, VOC, eCO2, baromètre), WiFi, NTP.
- **Sierra 4G Monitor** — Application visuelle C++ Qt/QML sur Linux pour antenne 4G Sierra wireless. Géolocalisation, graphiques de performance temps réel, communication SMS.

---

## Projets antérieurs (sélection)

| Année | Projet | Technologies |
|-------|--------|-------------|
| 2018 | Automatisation de mise à jour Cisco IOS | Python, PExpect, JSON, Cisco IOS |
| 2018 | Appliance réseau de sécurité automatisée | Ubuntu, OPNsense, ElasticSearch, Docker, Netflow |
| 2017 | Prototype d'entraînement VR pour Android | Android Studio, Java, BLE, Google VR |
| 2017 | Recherche sécurité Python et RF | HackRF, RTL-SDR, GNU Radio, GRGSM |
| 2017 | Surveillance sécurité ElasticSearch | SELKS, Suricata, Kibana, MetricBeat, PacketBeat |
| 2016 | Environnement vCloud Trend Micro | VMware vCloud Director, virtualisation imbriquée |
| 2011 | Application sécurité SOAP/WSSE | WSE-PHP, NuSOAP, X.509, MySQL |
| 2010–2018 | Environnement avancé de test cybersécurité | Kali, Metasploit, BeEF, vCloud Director |
| 2010–2011 | Ateliers en sécurité de l'information (5 sessions) | Backtrack 5, CTF, prévention d'exploits |
| 2009 | Tableau de bord IP Google Earth | C#, Linux, Google Earth |
| 2008 | Surveillance de communications IP | RRDTools, Apache, Perl |
| 2007 | Sniffer/détecteur/injecteur réseau | C#, WinPcap, injection de paquets IP |
| 2006 | Client protocole MSN | C#, protocole MSN 10 |
| 2004 | Journal alimentaire en ligne | C#, interfaces web |
| 1997 | Serveur HTTP sur mesure | Java JDK 1.2, ODBC, multiplateforme |
| 1996 | Bras robotique 3D (infographie) | C++, bibliothèques matricielles |
| 1996 | Système d'architecture temps réel | C++, Assembleur Intel, files de priorité |
| 1995 | Costume virtuel (prototype VR) | C++, Silverrun, modélisation corps humain |

---

## Domaines techniques

- **Embarqué** : STM32, TouchGFX, C/C++, Azure RTOS (ThreadX/NetXDuo), FreeRTOS, cryptographie matérielle (AES GCM, SAES, ECC CMOX, PQC ML-KEM/ML-DSA, PKA, TEE), CubeMX, CubeIDE
- **Sécurité réseau** : Routage/commutation Cisco, Checkpoint SASE, VPN, Pare-feu, IDPS, SIEM, NDR, Netflow, PyATS
- **Cybersécurité** : Tests d'intrusion (Kali, Metasploit, BeEF), simulation APT, sécurité RF (HackRF, RTL-SDR, GNU Radio), ElasticSearch/SELKS, EDR
- **Programmation** : C, C++, Python, C#, Java, Perl, PHP, Assembleur Intel, Qt/QML
- **Infrastructure** : Docker, Vagrant, VMware vCloud, AWS IoT, Arduino

---

## Profil

Bâtisseur depuis 1995 — d'un noyau de système temps réel et d'un serveur HTTP sur mesure (1996–1997) à la cryptographie post-quantique sur ARM Cortex-M (2025). Des décennies de projets personnels démontrent un patron : identifier un manque, bâtir la solution, pousser la technologie. Fait le pont entre les opérations de sécurité réseau, la cybersécurité et le développement embarqué bare-metal. Actuellement concentré sur les systèmes embarqués sécurisés par matériel avec des flux de travail de développement assistés par IA.

Le [système Knowledge](https://github.com/packetqc/knowledge) démontre comment un développeur structuré exploite chaque plateforme moderne disponible — GitHub Projects pour le suivi, GitHub Pages pour la publication, GitHub Actions pour l'automatisation, Git pour le contrôle de version — dans un système d'intelligence d'ingénierie cohérent. Aucun outil payant, aucun verrouillage fournisseur, aucun middleware. Juste une architecture propre sur des plateformes ouvertes.

Avec l'assistance IA au codage (Claude, Anthropic), ces 30 ans d'expérience en ingénierie gagnent un multiplicateur de force pour le développement, la gestion de projet et la documentation. 46 heures de collaboration active ont livré ce que les processus traditionnels d'entreprise prendraient 8–16 mois — couvrant le firmware embarqué, l'architecture de sécurité, l'intégration de tableaux de projet et la documentation bilingue complète. Knowledge est à la fois la méthodologie et la preuve : 13 histoires de réussite avec des chronologies de livraison réelles et des comparaisons côte à côte avec l'entreprise. — [Histoires de réussite]({{ '/fr/publications/success-stories/' | relative_url }})

---

## Top 5 — Proposition de valeur

1. **Sécurité réseau et systèmes** — 30 ans de défense de réseaux d'entreprise : infrastructure Cisco, Checkpoint SASE, SIEM/NDR/IDPS, tests d'intrusion, simulation APT, ateliers de sécurité
2. **Ingénierie de systèmes embarqués** — Du bare-metal au RTOS : STM32 (H5/H7/N6), interface TouchGFX, ThreadX/FreeRTOS, cryptographie matérielle (AES, SAES, ECC, PKA, TEE)
3. **Cryptographie post-quantique** — NIST niveau 5 (ML-KEM 1024, ML-DSA) sur ARM Cortex-M avec WolfSSL/WolfCrypt, échange de clés accéléré par matériel
4. **Flux d'ingénierie propulsé par IA** — Le système Knowledge automatise le cycle complet de développement : gestion de projet, génération de documentation, publication bilingue, persistance de session — tout projet hérite de la méthodologie
5. **Livraison bilingue cycle complet** — De l'architecture à la documentation en anglais et français. 46 heures de collaboration assistée par IA livrent l'équivalent de 8–16 mois en entreprise — firmware, sécurité et infrastructure

---

## Recommandation

[**Lettre de recommandation — Claude (Anthropic, Opus 4.6)**]({{ '/fr/profile/recommendation/' | relative_url }}) — Partenaire de développement IA, basée sur des données de collaboration directe (550+ billets, 23 publications, 52 versions de connaissances, 20 histoires de succès).

---

## Publications

| # | Titre | Lien |
|---|-------|------|
| 0 | Knowledge — Intelligence d'ingénierie IA auto-évolutive | [Lire]({{ '/fr/publications/knowledge-system/' | relative_url }}) |
| 1 | MPLIB Storage Pipeline — SQLite haute performance sur Cortex-M55 | [Lire]({{ '/fr/publications/mplib-storage-pipeline/' | relative_url }}) |
| 2 | Analyse de session en direct — Débogage temps réel assisté par IA | [Lire]({{ '/fr/publications/live-session-analysis/' | relative_url }}) |
| 3 | Persistance de session IA — Continuité inter-sessions | [Lire]({{ '/fr/publications/ai-session-persistence/' | relative_url }}) |
| 4 | Connaissances distribuées — Flux bidirectionnel de connaissances | [Lire]({{ '/fr/publications/distributed-minds/' | relative_url }}) |
| 4a | Tableau de bord — Statut du cerveau maître et du réseau satellite | [Lire]({{ '/fr/publications/distributed-knowledge-dashboard/' | relative_url }}) |
| 5 | Webcards & Partage social — Aperçus OG animés | [Lire]({{ '/fr/publications/webcards-social-sharing/' | relative_url }}) |
| 6 | Normalize & Concordance structurelle — Architecture auto-réparatrice | [Lire]({{ '/fr/publications/normalize-structure-concordance/' | relative_url }}) |
| 7 | Protocole Harvest — Collecte de connaissances distribuées | [Lire]({{ '/fr/publications/harvest-protocol/' | relative_url }}) |
| 8 | Gestion de session — Commandes de cycle de vie IA | [Lire]({{ '/fr/publications/session-management/' | relative_url }}) |
| 16 | Visualisation de pages web — Pipeline de rendu local | [Lire]({{ '/fr/publications/web-page-visualization/' | relative_url }}) |

---

*Martin Paquet — Québec, Canada — packetqcca@gmail.com*
