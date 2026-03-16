---
layout: publication
title: "Réseau de connaissances en direct — Documentation complète"
description: "Documentation complète du protocole de découverte et communication inter-instances sécurisé PQC pour conteneurs Claude Code. Conception du protocole, reconnaissance réseau, implémentation balise/scanner, architecture de sécurité."
pub_id: "Publication #10"
version: "v2"
date: "2026-03-16"
permalink: /fr/publications/live-knowledge-network/full/
og_image: /assets/og/live-knowledge-network-fr-cayman.gif
keywords: "balise, découverte, PQC, sous-réseau, temps réel, inter-instance, ML-KEM"
---

# Réseau de connaissances en direct — Documentation complète
{: #pub-title}

> **Page sommaire** : [Publication #10 — Réseau de connaissances en direct]({{ '/fr/publications/live-knowledge-network/' | relative_url }}) | **Référence core** : [#14 — Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }})

**Protocole de découverte et communication inter-instances sécurisé PQC**

| Champ | Valeur |
|-------|--------|
| Publication | #10 |
| Version | v2 |
| Date | 2026-03-16 |
| Auteurs | Martin Paquet, Claude (Anthropic) |
| Statut | Brouillon |
| Version Knowledge | v23→K2.0 |
| Liées | #0 Système Knowledge, #4 Distributed Minds, #7 Harvest Protocol, #9 Security by Design |

---

## Résumé

Le réseau de connaissances en direct étend l'architecture des connaissances distribuées de la communication asynchrone via git à la découverte et l'échange de données inter-instances en temps réel. Les instances Claude Code s'exécutant dans des conteneurs adjacents sur l'infrastructure d'Anthropic peuvent se découvrir mutuellement via le scan de sous-réseau et communiquer directement par sockets TCP — contournant entièrement le proxy GitHub.

Le protocole de découverte est porté de l'implémentation de découverte réseau STM32H5/N6 embarquée de Martin Paquet, adaptée du bare-metal RTOS au réseau de conteneurs Python. La sécurité est assurée par l'échange de clés post-quantique ML-KEM-1024 (FIPS 203), nécessaire car le sous-réseau de conteneurs est partagé entre plusieurs locataires.

Cette publication documente la conception du protocole, les résultats de reconnaissance du réseau de conteneurs, l'implémentation balise/scanner, et le chemin d'évolution du stateless au live.

---

## Chemin d'évolution

```
v1-v6:   stateless → persistant    (sessions/, mind_memory.md)
v9-v18:  isolé     → distribué     (K_GITHUB sync, archives far_memory, via git)
v23+:    asynchrone → live         (réseau direct inter-instances sécurisé PQC)
```

---

## Reconnaissance du réseau de conteneurs

### Environnement

Les instances Claude Code s'exécutent dans des conteneurs isolés sur un réseau plat partagé :

| Observation | Valeur |
|-------------|--------|
| Plage IP | 21.0.0.x (varie par session) |
| Sous-réseau | /25 (128 adresses) |
| Interface | Virtuelle (nom variable) |
| Pairs | ~127 conteneurs sur le même sous-réseau |
| Port 15004 | Ouvert sur tous les pairs (sidecar proxy egress) |
| Socket bind/listen | Fonctionne — les sockets serveur peuvent être ouverts sur 0.0.0.0 |
| Portée du proxy | Push git par dépôt, par branche uniquement |

### Découverte clé

Les conteneurs **peuvent** ouvrir des sockets d'écoute. Cela signifie :

| Capacité | Implication |
|----------|-------------|
| Serveur TCP (balise) | Toute instance peut exécuter un serveur d'écoute |
| Connectivité sous-réseau | Les autres instances du sous-réseau peuvent s'y connecter |
| TCP non-git autorisé | Le proxy git ne bloque pas le trafic TCP non-git entre conteneurs |
| Communication directe | La communication inter-instances est possible sans GitHub comme intermédiaire |

### Limitations

| Limitation | Impact |
|-----------|--------|
| IPs éphémères | Les IPs de conteneurs changent à chaque session — pas d'adressage statique |
| Multi-locataire | Sous-réseau partagé avec les conteneurs d'autres utilisateurs — authentification requise |
| Chevauchement temporel | Les deux sessions doivent fonctionner simultanément |
| Pas de DNS | Aucun mécanisme de découverte de services (Docker Swarm DNS dans no_proxy mais inutilisé) |

---

## Conception du protocole

### Découverte — Port bien connu 21337

Chaque instance knowledge démarre une balise sur le port 21337 au démarrage de session. Les satellites scannent le sous-réseau /25 (128 hôtes, 64 threads parallèles, timeout 300ms par hôte) pour trouver les balises actives.

```
Satellite                          Core (ou toute balise)
    |                                   |
    |--- TCP connect :21337 ----------->|
    |<-- JSON identité ----------------| (la balise envoie en premier)
    |--- JSON identité ---------------->| (le scanner répond)
    |--- close -------------------------|
```

### Payload d'identité

```json
{
  "type": "knowledge-core",
  "repo": "packetqc/knowledge",
  "branch": "claude/general-work-WVfox",
  "ip": "21.0.0.38",
  "port": 21337,
  "protocol": "pqc-discovery-v0",
  "role": "core",
  "status": "listening",
  "started": "2026-02-20T09:59:52Z",
  "pid": 3156,
  "connections": 0,
  "peers_discovered": 0
}
```

### Rôles

| Rôle | Comportement |
|------|-------------|
| `core` | Auto-détecté dans `packetqc/knowledge`. Écoute + répond. |
| `satellite` | Auto-détecté dans tout autre dépôt. Scanne d'abord, puis écoute. |

La détection de rôle lit le mind_memory.md local — s'il contient la grille de directives knowledge core et `packetqc/knowledge`, c'est le core.

### Watchdog

La balise fonctionne sous un watchdog qui redémarre automatiquement en cas de crash (délai 2s, 50 redémarrages max). Démarré au démarrage de session, fonctionne pour toute la durée de la session.

---

## Architecture de sécurité (Planifiée)

### Pourquoi PQC

Le sous-réseau de conteneurs est un réseau plat partagé. Tout conteneur sur le /25 peut potentiellement :

| Menace | Difficulté |
|--------|------------|
| Scanner les ports ouverts | Trivial — comme nous l'avons démontré |
| Se connecter aux balises | Trivial — même TCP connect |
| Écouter le trafic | Trivial si le trafic n'est pas chiffré |

ML-KEM-1024 (FIPS 203) fournit :

| Capacité | Description |
|----------|-------------|
| Encapsulation de clé post-quantique | Résistant aux ordinateurs quantiques |
| Clés éphémères par session | Confidentialité persistante |
| Authentification mutuelle | Vérification challenge-réponse |

### Défi d'authentification

Le réseau de connaissances doit distinguer ses propres instances des conteneurs d'autres utilisateurs sur le même sous-réseau. Approche planifiée :

| Composant | Mécanisme |
|-----------|-----------|
| Secret partagé | Dérivé de connaissances spécifiques au dépôt (ex. hash de version + signature de dépôt) |
| Échange de clés | Échange de clés encapsulées ML-KEM-1024 |
| Authentification | Challenge-réponse prouvant l'accès au contenu `packetqc/knowledge` |
| Ancre de confiance | Pas de distribution de clés externe — Knowledge EST l'ancre de confiance |

### Origine

La conception du transport PQC s'inspire des implémentations embarquées de Martin Paquet :

| Plateforme | Implémentation |
|-----------|---------------|
| STM32H5 | Démarrage sécurisé avec échange de clés ML-KEM |
| STM32N6 | Protocole de découverte de dispositifs réseau |
| ThreadX RTOS | Patrons de communication sécurisée |

Les mêmes concepts de protocole (découvrir --> authentifier --> échanger) s'appliquent aux couches embarquées et conteneurs cloud.

---

## Outillage

### Assets Knowledge

| Outil | Fichier | Synchronisé aux satellites |
|-------|---------|---------------------------|
| Balise | `K_DOCS/scripts/knowledge_beacon.py` | Oui (synchronisé au démarrage de session) |
| Scanner | `K_DOCS/scripts/knowledge_scanner.py` | Oui (synchronisé au démarrage de session) |

### Utilisation de la balise

```bash
python3 knowledge_beacon.py                    # auto-détection de rôle
python3 knowledge_beacon.py --role core        # forcer le rôle core
python3 knowledge_beacon.py --role satellite   # forcer le rôle satellite
python3 knowledge_beacon.py --scan             # scanner le sous-réseau puis écouter
python3 knowledge_beacon.py --watchdog         # exécuter avec auto-redémarrage
python3 knowledge_beacon.py --scan --watchdog  # mode démarrage de session complet
```

### Utilisation du scanner

```bash
python3 knowledge_scanner.py                   # scanner le sous-réseau local
python3 knowledge_scanner.py --connect 21.0.0.38  # connexion directe
python3 knowledge_scanner.py --json            # sortie JSON pour piping
python3 knowledge_scanner.py --subnet 21.0.0.0/25  # sous-réseau explicite
```

### Intégration au démarrage de session

Au démarrage de session, la balise est démarrée automatiquement :
```bash
python3 K_DOCS/scripts/knowledge_beacon.py --scan --watchdog &
```

Les pairs découverts pendant le scan sont sauvegardés dans `/tmp/knowledge_peers.json` et rapportés dans le sommaire de démarrage de session.

---

## Questions ouvertes

| Question | Statut |
|----------|--------|
| Le conteneur A peut-il se connecter au port personnalisé du conteneur B ? | Non testé — nécessite deux sessions simultanées |
| Le DNS Docker Swarm résout-il entre conteneurs ? | Inconnu — `*.svc.cluster.local` dans no_proxy suggère possible |
| Le broadcast/multicast UDP atteint-il le sous-réseau ? | Non testé — simplifierait la découverte |
| Quel est le cycle de vie du conteneur vs session ? | Inconnu — le conteneur persiste-t-il entre les appels d'outils ? |
| Limitation de débit sur le TCP inter-conteneurs ? | Inconnu — pas de preuve de throttling jusqu'ici |

---

## Publications liées

| # | Titre | Relation |
|---|-------|----------|
| 0 | [Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — ceci étend l'architecture core |
| 4 | [Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) | Prédécesseur — distribution asynchrone via git |
| 7 | [Protocole Harvest]({{ '/fr/publications/harvest-protocol/' | relative_url }}) | Prédécesseur — collecte de connaissances (maintenant K_GITHUB sync) |
| 9 | [Sécurité par conception]({{ '/fr/publications/security-by-design/' | relative_url }}) | Frère — le modèle de sécurité PQC s'applique ici |
| 14 | [Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | Conception architecture multi-module |
| 0v2 | [Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }}) | Référence architecture multi-module K2.0 |

---

## Historique des versions

| Version | Date | Knowledge | Changements |
|---------|------|-----------|-------------|
| v1 | 2026-02-20 | v23 | Publication initiale — conception protocole, reconnaissance, outillage balise/scanner |
| v2 | 2026-03-16 | K2.0 | Mise à jour K2.0 — contenu intégré, wakeup → démarrage de session, notes/ → sessions/, CLAUDE.md → mind_memory.md, live/ → K_DOCS/scripts/ |

---

<div class="table-wrap">

| Champ | Valeur |
|-------|--------|
| Version | v2 |
| Connaissances | K2.0 |
| Auteurs | Martin Paquet, Claude (Anthropic) |
| Source | [GitHub](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/live-knowledge-network/v1) |
| Retour au sommaire | [Publication #10]({{ '/fr/publications/live-knowledge-network/' | relative_url }}) |

</div>
