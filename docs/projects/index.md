---
layout: default
title: "Projects"
description: "Project-centric view of the knowledge ecosystem. Core project, child projects, satellite repositories, and their publications — organized by project hierarchy with dual-origin links."
permalink: /projects/
og_image: /assets/og/knowledge-system-en-cayman.gif
project_boards: true
---

# Projects

The knowledge ecosystem organized by **project hierarchy**. Each project is a first-class entity with its own identity, publications, satellites, evolution, and stories.

*By Martin Paquet & Claude (Anthropic, Opus 4.6)*

**Navigation**: [Publications (flat list)]({{ '/publications/' | relative_url }}) | **Projects (by hierarchy)** | [Profile]({{ '/profile/' | relative_url }})

**Contents**

- [Project Registry](#project-registry)
- [Link Origin Convention](#link-origin-convention)
- [P0 — Knowledge](#p0--knowledge)
- [P1 — MPLIB](#p1--mplib)
- [P2 — STM32 PoC](#p2--stm32-poc)
- [P3 — knowledge-live](#p3--knowledge-live)
- [P4 — MPLIB Dev Staging](#p4--mplib-dev-staging)
- [P5 — PQC](#p5--pqc)
- [P6 — Export Documentation](#p6--export-documentation)
- [P8 — Documentation System](#p8--documentation-system)
- [P9 — Knowledge Compliancy Report](#p9--knowledge-compliancy-report)
- [P13 — Studio 54](#p13--studio-54)

---

## Project Registry

| ID | Project | Type | Status | Satellites | Publications |
|----|---------|------|--------|------------|--------------|
| P0 | [Knowledge](#p0--knowledge) | core | 🟢 active | 5 | 15 |
| P1 | [MPLIB](#p1--mplib) | child | 🟢 active | 2 | 1 |
| P2 | [STM32 PoC](#p2--stm32-poc) | child | 🟢 active | 1 | 1 |
| P3 | [knowledge-live](#p3--knowledge-live) | child | 🟢 active | 1 | 1 |
| P4 | [MPLIB Dev Staging](#p4--mplib-dev-staging) | child | 🟢 active | 1 | 0 |
| P5 | [PQC](#p5--pqc) | child | 🔴 pre-bootstrap | 1 | 0 |
| P6 | [Export Documentation](#p6--export-documentation) | managed | 🟢 active | 0 | 0 |
| P8 | [Documentation System](#p8--documentation-system) | managed | 🟢 active | 0 | 0 |
| P9 | [Knowledge Compliancy Report](#p9--knowledge-compliancy-report) | managed | 🟢 active | 0 | 1 |
| P13 | [Studio 54](#p13--studio-54) | managed | 🟢 active | 0 | 0 |

---

## Link Origin Convention

Publications and documentation exist across multiple repositories, each with its own GitHub Pages site. The link origin indicates provenance:

| Origin | Meaning | Base URL | Badge |
|--------|---------|----------|-------|
| **Core** | Reviewed, published, canonical | `{{ site.url }}{{ site.baseurl }}/` | **core** |
| **Satellite** | Development, staging, local docs | `packetqc.github.io/<repo>/` | *satellite* |

Core publications are the approved, reviewed versions. Satellite publications are working documents that may evolve independently. Both are accessible via GitHub Pages — different origin, same technology.

---

## P0 — Knowledge

**Type**: core | **Status**: 🟢 active | **Repository**: [packetqc/knowledge](https://github.com/packetqc/knowledge) | **Board**: [#4](https://github.com/users/packetqc/projects/4)

The master project — methodology, publications, distributed network, self-evolving intelligence.

### Project Board

[GitHub Project Board #4 →](https://github.com/users/packetqc/projects/4) — Roadmap, ongoing work, planned features, and forecasts.

See also: [General Plan]({{ '/plan/' | relative_url }}) (live board widgets with status filters)

<div class="project-board-widget" data-board-number="4"></div>

### Core Publications (P0)

| Index | # | Title | Origin | Link |
|-------|---|-------|--------|------|
| P0/#0 | 0 | Knowledge | **core** | [Read →]({{ '/publications/knowledge-system/' | relative_url }}) |
| P0/#1 | 1 | MPLIB Storage Pipeline | **core** →P1 | [Read →]({{ '/publications/mplib-storage-pipeline/' | relative_url }}) |
| P0/#2 | 2 | Live Session Analysis | **core** | [Read →]({{ '/publications/live-session-analysis/' | relative_url }}) |
| P0/#3 | 3 | AI Session Persistence | **core** | [Read →]({{ '/publications/ai-session-persistence/' | relative_url }}) |
| P0/#4 | 4 | Distributed Minds | **core** | [Read →]({{ '/publications/distributed-minds/' | relative_url }}) |
| P0/#4a | 4a | Knowledge Dashboard | **core** | [Read →]({{ '/publications/distributed-knowledge-dashboard/' | relative_url }}) |
| P0/#5 | 5 | Webcards & Social Sharing | **core** | [Read →]({{ '/publications/webcards-social-sharing/' | relative_url }}) |
| P0/#6 | 6 | Normalize & Structure Concordance | **core** | [Read →]({{ '/publications/normalize-structure-concordance/' | relative_url }}) |
| P0/#7 | 7 | Harvest Protocol | **core** | [Read →]({{ '/publications/harvest-protocol/' | relative_url }}) |
| P0/#8 | 8 | Session Management | **core** | [Read →]({{ '/publications/session-management/' | relative_url }}) |
| P0/#9 | 9 | Security by Design | **core** | [Read →]({{ '/publications/security-by-design/' | relative_url }}) |
| P0/#9a | 9a | Token Lifecycle Compliance | **core** | [Read →]({{ '/publications/security-by-design/compliance/' | relative_url }}) |
| P0/#10 | 10 | Live Knowledge Network | **core** →P3 | [Read →]({{ '/publications/live-knowledge-network/' | relative_url }}) |
| P0/#11 | 11 | Success Stories | **core** | [Read →]({{ '/publications/success-stories/' | relative_url }}) |
| P0/#12 | 12 | Project Management | **core** | [Read →]({{ '/publications/project-management/' | relative_url }}) |

### Child Projects

| ID | Project | Status | Satellites |
|----|---------|--------|------------|
| P1 | [MPLIB](#p1--mplib) | 🟢 active | 2 repos |
| P2 | [STM32 PoC](#p2--stm32-poc) | 🟢 active | 1 repo |
| P3 | [knowledge-live](#p3--knowledge-live) | 🟢 active | 1 repo |
| P4 | [MPLIB Dev Staging](#p4--mplib-dev-staging) | 🟢 active | 1 repo |
| P5 | [PQC](#p5--pqc) | 🔴 pre-bootstrap | 1 repo |

---

## P1 — MPLIB

**Type**: child of P0 | **Status**: 🟢 active | **Repository**: [packetqc/MPLIB](https://github.com/packetqc/MPLIB) | **Board**: [#5](https://github.com/users/packetqc/projects/5)

High-throughput embedded systems library — SQLite log ingestion on ARM Cortex-M55, ThreadX RTOS, TouchGFX UI. The original proof-of-concept that validated Knowledge.

### Project Board

[GitHub Project Board #5 →](https://github.com/users/packetqc/projects/5)

<div class="project-board-widget" data-board-number="5"></div>

### Publications

| Index | Title | Origin | Link |
|-------|-------|--------|------|
| P0/#1 | MPLIB Storage Pipeline | **core** | [Read →]({{ '/publications/mplib-storage-pipeline/' | relative_url }}) |
| P1/S1/D1 | X | *satellite* | X |

### Satellites

| Index | Repository | Version | Health |
|-------|------------|---------|--------|
| P1/S1 | [packetqc/MPLIB](https://github.com/packetqc/MPLIB) | v31 | 🟢 |
| P1/S2 | [packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE](https://github.com/packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE) | v31 | 🟢 |

---

## P2 — STM32 PoC

**Type**: child of P0 | **Status**: 🟢 active | **Repository**: [packetqc/STM32N6570-DK_SQLITE](https://github.com/packetqc/STM32N6570-DK_SQLITE) | **Board**: [#6](https://github.com/users/packetqc/projects/6)

Hardware proof-of-concept for the MPLIB library on STM32N6570-DK (Cortex-M55 @ 800 MHz).

### Project Board

[GitHub Project Board #6 →](https://github.com/users/packetqc/projects/6)

<div class="project-board-widget" data-board-number="6"></div>

### Publications

| Index | Title | Origin | Link |
|-------|-------|--------|------|
| P0/#1 | MPLIB Storage Pipeline | **core** (shared with P1) | [Read →]({{ '/publications/mplib-storage-pipeline/' | relative_url }}) |
| P2/S1/D1 | doc/readme.md | *satellite* | X |

### Satellites

| Index | Repository | Version | Health |
|-------|------------|---------|--------|
| P2/S1 | [packetqc/STM32N6570-DK_SQLITE](https://github.com/packetqc/STM32N6570-DK_SQLITE) | v31 | 🟢 |

---

## P3 — knowledge-live

**Type**: child of P0 | **Status**: 🟢 active | **Repository**: [packetqc/knowledge-live](https://github.com/packetqc/knowledge-live) | **Board**: [#37](https://github.com/users/packetqc/projects/37)

PQC-secured inter-instance discovery and communication. First satellite bootstrapped with autonomous scaffold (v23). Beacon/scanner protocol ported from STM32H5/N6 embedded network discovery.

### Project Board

[GitHub Project Board #37 →](https://github.com/users/packetqc/projects/37)

<div class="project-board-widget" data-board-number="37"></div>

### Publications

| Index | Title | Origin | Link |
|-------|-------|--------|------|
| P0/#10 | Live Knowledge Network | **core** | [Read →]({{ '/publications/live-knowledge-network/' | relative_url }}) |

### Satellites

| Index | Repository | Version | Health |
|-------|------------|---------|--------|
| P3/S1 | [packetqc/knowledge-live](https://github.com/packetqc/knowledge-live) | v31 | 🟢 |

---

## P4 — MPLIB Dev Staging

**Type**: child of P1 | **Status**: 🟢 active | **Repository**: [packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE](https://github.com/packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE) | **Board**: [#8](https://github.com/users/packetqc/projects/8)

Development staging environment for MPLIB. Where the iterative staging protocol (v25) was first validated. Most active satellite by session count.

### Project Board

[GitHub Project Board #8 →](https://github.com/users/packetqc/projects/8)

<div class="project-board-widget" data-board-number="8"></div>

### Satellites

| Index | Repository | Version | Health |
|-------|------------|---------|--------|
| P4/S1 | [packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE](https://github.com/packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE) | v31 | 🟢 |

---

## P5 — PQC

**Type**: child of P0 | **Status**: 🔴 pre-bootstrap | **Repository**: [packetqc/PQC](https://github.com/packetqc/PQC) | **Board**: [#9](https://github.com/users/packetqc/projects/9)

Post-Quantum Cryptography reference repository. Not yet bootstrapped into Knowledge.

### Project Board

[GitHub Project Board #9 →](https://github.com/users/packetqc/projects/9)

<div class="project-board-widget" data-board-number="9"></div>

### Satellites

| Index | Repository | Version | Health |
|-------|------------|---------|--------|
| P5/S1 | [packetqc/PQC](https://github.com/packetqc/PQC) | v0 | 🔴 47 versions behind |

### Remediation

Open a Claude Code session in the PQC repo → `wakeup` → bootstrap scaffold activates → merge PR.

---

## P6 — Export Documentation

**Type**: managed (in P3) | **Status**: 🟢 active | **Host repo**: [packetqc/knowledge-live](https://github.com/packetqc/knowledge-live) | **Board**: [#10](https://github.com/users/packetqc/projects/10)

Multi-purpose documentation and publication management project hosted within knowledge-live.

<div class="project-board-widget" data-board-number="10"></div>

---

## P8 — Documentation System

**Type**: managed (in P0) | **Status**: 🟢 active | **Host repo**: [packetqc/knowledge](https://github.com/packetqc/knowledge) | **Board**: [#38](https://github.com/users/packetqc/projects/38)

Knowledge documentation system — publication pipeline, doc review, and content management.

<div class="project-board-widget" data-board-number="38"></div>

---

## P9 — Knowledge Compliancy Report

**Type**: managed (in P0) | **Status**: 🟢 active | **Host repo**: [packetqc/knowledge](https://github.com/packetqc/knowledge) | **Board**: [#43](https://github.com/users/packetqc/projects/43)

Compliance assessment of Knowledge's ephemeral token handling against OWASP MCP01:2025, NIST SP 800-63B, FIPS 140-3, and CIS Controls v8. Tracks 28 compliance checkpoints and 7 roadmap items across 5 lifecycle phases.

<div class="project-board-widget" data-board-number="43"></div>

### Publications

| Index | Title | Origin | Link |
|-------|-------|--------|------|
| P0/#9a | Token Lifecycle Compliance | **core** | [Read →]({{ '/publications/security-by-design/compliance/' | relative_url }}) |

---

## P13 — Studio 54

**Type**: managed (in P0) | **Status**: 🟢 active | **Host repo**: [packetqc/knowledge](https://github.com/packetqc/knowledge) | **Board**: [#50](https://github.com/users/packetqc/projects/50)

Studio 54 project. Managed within the knowledge core repository.

<div class="project-board-widget" data-board-number="50"></div>

---

## About

This page provides a **project-centric navigation** overlay on top of the existing [publications index]({{ '/publications/' | relative_url }}). No existing URLs were changed — this is an additive view.

| | |
|---|---|
| **Repository** | [{{ site.github_repo }}](https://github.com/{{ site.github_repo }}) |
| **Publications (flat list)** | [All publications →]({{ '/publications/' | relative_url }}) |
| **Author** | [Martin Paquet →]({{ '/profile/' | relative_url }}) |
| **Contact** | packetqcca@gmail.com |

---

*Project entity model introduced in Knowledge v35 (February 2026).*
*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
