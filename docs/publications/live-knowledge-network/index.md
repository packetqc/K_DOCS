---
layout: publication
title: "Live Knowledge Network — PQC-Secured Inter-Instance Discovery"
description: "Real-time discovery and communication between Claude Code instances via PQC-secured TCP on shared container subnets. Beacon/scanner protocol ported from STM32H5/N6 embedded network discovery."
pub_id: "Publication #10"
version: "v2"
date: "2026-03-16"
permalink: /publications/live-knowledge-network/
og_image: /assets/og/live-knowledge-network-en-cayman.gif
keywords: "beacon, discovery, PQC, subnet, real-time, inter-instance, ML-KEM"
---

# Live Knowledge Network — PQC-Secured Inter-Instance Discovery
{: #pub-title}

> **Parent publication**: [#0 — Knowledge]({{ '/publications/knowledge-system/' | relative_url }}) | **Core reference**: [#14 — Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/publications/knowledge-2.0/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Real-time inter-instance discovery overview |
| [Evolution Path](#evolution-path) | Three generations of knowledge communication |
| [Discovery Protocol](#discovery-protocol) | Beacon/scanner subnet scanning on port 21337 |
| [Security Architecture](#security-architecture) | ML-KEM-1024 post-quantum key exchange |
| [Tooling](#tooling) | Beacon and scanner Python tools |
| [Related Publications](#related-publications) | Parent and sibling publications |

## Abstract

The Live Knowledge Network extends the distributed minds architecture from asynchronous git-mediated communication to **real-time inter-instance discovery and data exchange**. Claude Code instances running in adjacent containers on Anthropic's infrastructure can discover each other via subnet scanning and communicate directly over TCP sockets — bypassing the GitHub proxy entirely.

The discovery protocol is ported from Martin Paquet's STM32H5/N6 embedded network discovery implementation, adapted from bare-metal RTOS to Python container networking. Security is provided by ML-KEM-1024 (FIPS 203) post-quantum key exchange, necessary because the container subnet is shared across multiple tenants.

## Evolution Path

Knowledge's communication has evolved through three generations:

| Generation | Versions | Mechanism | Latency |
|-----------|----------|-----------|---------|
| **Persistent** | v1–v6 | `sessions/` + `mind_memory.md` (file-based) | Session boundary |
| **Distributed** | v9–v18 | K_GITHUB `sync_github.py` + `far_memory archives/` (git-mediated) | Minutes (PR merge) |
| **Live** | v23+ | Beacon/scanner (direct TCP) | Milliseconds |

## Discovery Protocol

Every knowledge instance starts a **beacon** on well-known port **21337** on session start. Satellites scan the /25 container subnet (128 hosts, 64 parallel threads) to find active beacons. Identity is exchanged as JSON over TCP — no HTTP overhead.

**Read the complete documentation**: [Full publication]({{ '/publications/live-knowledge-network/full/' | relative_url }})

## Security Architecture

The container subnet is a shared flat network (~127 peers). Any container can scan and connect. ML-KEM-1024 (FIPS 203) post-quantum key exchange provides:

| Capability | Description |
|------------|-------------|
| Per-session ephemeral keys | Forward secrecy — keys are unique to each session |
| Mutual authentication | Challenge-response proves both sides are legitimate |
| Quantum resistance | Resistant to attacks by quantum computers |

Knowledge itself serves as the trust anchor — proving access to `packetqc/knowledge` content is the authentication mechanism.

## Tooling

| Tool | File | Purpose |
|------|------|---------|
| Beacon | `K_DOCS/scripts/knowledge_beacon.py` | Listen on port 21337, respond with identity |
| Scanner | `K_DOCS/scripts/knowledge_scanner.py` | Scan subnet, discover beacons, exchange identity |

Both tools are synced to satellite projects on session start alongside the existing capture scripts.

## Related Publications

| # | Title | Relationship |
|---|-------|-------------|
| [0]({{ '/publications/knowledge-system/' | relative_url }}) | Knowledge | Parent — this extends the core architecture |
| [4]({{ '/publications/distributed-minds/' | relative_url }}) | Distributed Minds | Predecessor — async git-mediated distribution |
| [7]({{ '/publications/harvest-protocol/' | relative_url }}) | Harvest Protocol | Predecessor — pull-based knowledge collection (now K_GITHUB sync) |
| [14]({{ '/publications/architecture-analysis/' | relative_url }}) | Architecture Analysis | Architecture deep dive — multi-module design |
| [0v2]({{ '/publications/knowledge-2.0/' | relative_url }}) | Knowledge 2.0 | K2.0 multi-module architecture reference |
| [9]({{ '/publications/security-by-design/' | relative_url }}) | Security by Design | Sibling — PQC security model applies here |

---

<div class="table-wrap">

| Field | Value |
|-------|-------|
| Version | v2 |
| Knowledge | v23 |
| Authors | Martin Paquet, Claude (Anthropic) |
| Source | [GitHub](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/live-knowledge-network/v1) |
| Knowledge repo | [packetqc/knowledge](https://github.com/packetqc/knowledge) |

</div>
