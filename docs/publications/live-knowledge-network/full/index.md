---
layout: publication
title: "Live Knowledge Network — Complete Documentation"
description: "Complete documentation of the PQC-secured inter-instance discovery and communication protocol for Claude Code containers. Protocol design, reconnaissance findings, beacon/scanner implementation, security architecture."
pub_id: "Publication #10"
version: "v2"
date: "2026-03-16"
permalink: /publications/live-knowledge-network/full/
og_image: /assets/og/live-knowledge-network-en-cayman.gif
keywords: "beacon, discovery, PQC, subnet, real-time, inter-instance, ML-KEM"
---

# Live Knowledge Network — Complete Documentation
{: #pub-title}

> **Summary page**: [Publication #10 — Live Knowledge Network]({{ '/publications/live-knowledge-network/' | relative_url }}) | **Core reference**: [#14 — Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }}) | [#0v2 — Knowledge 2.0]({{ '/publications/knowledge-2.0/' | relative_url }})

**PQC-Secured Inter-Instance Discovery and Communication Protocol**

| Field | Value |
|-------|-------|
| Publication | #10 |
| Version | v2 |
| Date | 2026-03-16 |
| Authors | Martin Paquet, Claude (Anthropic) |
| Status | Draft |
| Knowledge version | v23→K2.0 |
| Related | #0 Knowledge System, #4 Distributed Minds, #7 Harvest Protocol, #9 Security by Design |

---

## Abstract

The Live Knowledge Network extends the distributed minds architecture from asynchronous git-mediated communication to real-time inter-instance discovery and data exchange. Claude Code instances running in adjacent containers on Anthropic's infrastructure can discover each other via subnet scanning and communicate directly over TCP sockets — bypassing the GitHub proxy entirely.

The discovery protocol is ported from Martin Paquet's STM32H5/N6 embedded network discovery implementation, adapted from bare-metal RTOS to Python container networking. Security is provided by ML-KEM-1024 (FIPS 203) post-quantum key exchange, necessary because the container subnet is shared across multiple tenants.

This publication documents the protocol design, container network reconnaissance findings, beacon/scanner implementation, and the evolution path from stateless to live.

---

## Evolution Path

```
v1-v6:   stateless → persistent    (sessions/, mind_memory.md)
v9-v18:  isolated  → distributed   (K_GITHUB sync, far_memory archives, git-mediated)
v23+:    async     → live          (PQC-secured direct instance network)
```

---

## Container Network Reconnaissance

### Environment

Claude Code instances run in isolated containers on a shared flat network:

| Finding | Value |
|---------|-------|
| IP range | 21.0.0.x (varies per session) |
| Subnet | /25 (128 addresses) |
| Interface | Virtual (name varies) |
| Peers | ~127 containers on same subnet |
| Port 15004 | Open on all peers (egress proxy sidecar) |
| Socket bind/listen | Works — server sockets can be opened on 0.0.0.0 |
| Proxy scope | Per-repo, per-branch git push only |

### Key Discovery

Containers **can** open listening sockets. This means:

| Capability | Implication |
|------------|-------------|
| TCP server (beacon) | Any instance can run a listening server |
| Subnet connectivity | Other instances on the subnet can connect to it |
| Non-git TCP allowed | The git proxy does not block non-git TCP traffic between containers |
| Direct communication | Inter-instance communication is possible without GitHub as intermediary |

### Limitations

| Limitation | Impact |
|-----------|--------|
| Ephemeral IPs | Container IPs change every session — no static addressing |
| Multi-tenant | Subnet shared with other users' containers — authentication required |
| Temporal overlap | Both sessions must run simultaneously |
| No DNS | No service discovery mechanism (Docker Swarm DNS in no_proxy but unused) |

---

## Protocol Design

### Discovery — Well-Known Port 21337

Every knowledge instance starts a beacon on port 21337 on session start. Satellites scan the /25 subnet (128 hosts, 64 parallel threads, 300ms timeout per host) to find active beacons.

```
Satellite                          Core (or any beacon)
    |                                   |
    |--- TCP connect :21337 ----------->|
    |<-- JSON identity -----------------| (beacon sends first)
    |--- JSON identity ---------------->| (scanner responds)
    |--- close -------------------------|
```

### Identity Payload

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

### Roles

| Role | Behavior |
|------|----------|
| `core` | Auto-detected when running in `packetqc/knowledge`. Listens + responds. |
| `satellite` | Auto-detected in any other repo. Scans first, then listens. |

Role detection reads the local mind_memory.md — if it contains the knowledge core directive grid and `packetqc/knowledge`, it's the core.

### Watchdog

The beacon runs under a watchdog that auto-restarts on crash (2s delay, 50 max restarts). Started on session start, runs for the session's lifetime.

---

## Security Architecture (Planned)

### Why PQC

The container subnet is a shared flat network. Any container on the /25 can potentially:

| Threat | Difficulty |
|--------|------------|
| Scan for open ports | Trivial — as we demonstrated |
| Connect to beacons | Trivial — same TCP connect |
| Eavesdrop on traffic | Trivial if traffic is unencrypted |

ML-KEM-1024 (FIPS 203) provides:

| Capability | Description |
|------------|-------------|
| Post-quantum key encapsulation | Resistant to quantum computers |
| Per-session ephemeral keys | Forward secrecy |
| Mutual authentication | Challenge-response verification |

### Authentication Challenge

The knowledge network must distinguish its own instances from other users' containers on the same subnet. Planned approach:

| Component | Mechanism |
|-----------|-----------|
| Shared secret | Derived from repo-specific knowledge (e.g., knowledge-version hash + repo signature) |
| Key exchange | ML-KEM-1024 encapsulated key exchange |
| Authentication | Challenge-response proving access to `packetqc/knowledge` content |
| Trust anchor | No external key distribution — Knowledge IS the trust anchor |

### Origin

The PQC transport design draws from Martin Paquet's embedded implementations:

| Platform | Implementation |
|----------|---------------|
| STM32H5 | Secure boot with ML-KEM key exchange |
| STM32N6 | Network device discovery protocol |
| ThreadX RTOS | Secure communication patterns |

The same protocol concepts (discover --> authenticate --> exchange) apply at both embedded and cloud container layers.

---

## Tooling

### Knowledge Assets

| Tool | File | Synced to satellites |
|------|------|---------------------|
| Beacon | `K_DOCS/scripts/knowledge_beacon.py` | Yes (synced on session start) |
| Scanner | `K_DOCS/scripts/knowledge_scanner.py` | Yes (synced on session start) |

### Beacon Usage

```bash
python3 knowledge_beacon.py                    # auto-detect role
python3 knowledge_beacon.py --role core        # force core role
python3 knowledge_beacon.py --role satellite   # force satellite role
python3 knowledge_beacon.py --scan             # scan subnet then listen
python3 knowledge_beacon.py --watchdog         # run with auto-restart
python3 knowledge_beacon.py --scan --watchdog  # full session start mode
```

### Scanner Usage

```bash
python3 knowledge_scanner.py                   # scan local subnet
python3 knowledge_scanner.py --connect 21.0.0.38  # direct connect
python3 knowledge_scanner.py --json            # JSON output for piping
python3 knowledge_scanner.py --subnet 21.0.0.0/25  # explicit subnet
```

### Session Start Integration

On session start, the beacon is started automatically:
```bash
python3 K_DOCS/scripts/knowledge_beacon.py --scan --watchdog &
```

Peers discovered during scan are saved to `/tmp/knowledge_peers.json` and reported in the session start summary.

---

## Open Questions

| Question | Status |
|----------|--------|
| Can container A connect to container B's custom port? | Untested — needs two simultaneous sessions |
| Does Docker Swarm DNS resolve between containers? | Unknown — `*.svc.cluster.local` in no_proxy list suggests possible |
| Can UDP broadcast/multicast reach the subnet? | Untested — would simplify discovery |
| What's the container lifecycle vs session lifecycle? | Unknown — does the container persist between tool calls? |
| Rate limiting on inter-container TCP? | Unknown — no evidence of throttling so far |

---

## Related Publications

| # | Title | Relationship |
|---|-------|-------------|
| 0 | [Knowledge]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — this extends the core architecture |
| 4 | [Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }}) | Predecessor — async git-mediated distribution |
| 7 | [Harvest Protocol]({{ '/publications/harvest-protocol/' | relative_url }}) | Predecessor — pull-based knowledge collection (now K_GITHUB sync) |
| 9 | [Security by Design]({{ '/publications/security-by-design/' | relative_url }}) | Sibling — PQC security model applies here |
| 14 | [Architecture Analysis]({{ '/publications/architecture-analysis/' | relative_url }}) | Multi-module architecture design |
| 0v2 | [Knowledge 2.0]({{ '/publications/knowledge-2.0/' | relative_url }}) | K2.0 multi-module architecture reference |

---

## Version History

| Version | Date | Knowledge | Changes |
|---------|------|-----------|---------|
| v1 | 2026-02-20 | v23 | Initial publication — protocol design, reconnaissance, beacon/scanner tooling |
| v2 | 2026-03-16 | K2.0 | K2.0 terminology update — inlined content, wakeup → session start, notes/ → sessions/, CLAUDE.md → mind_memory.md, live/ → K_DOCS/scripts/ |

---

<div class="table-wrap">

| Field | Value |
|-------|-------|
| Version | v2 |
| Knowledge | K2.0 |
| Authors | Martin Paquet, Claude (Anthropic) |
| Source | [GitHub](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/live-knowledge-network/v1) |
| Back to summary | [Publication #10]({{ '/publications/live-knowledge-network/' | relative_url }}) |

</div>
