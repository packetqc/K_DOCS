# Knowledge System — General Plan

Current roadmap for the knowledge system. Items advance through the lifecycle:
Analysis → Planned → In progress → Testing → QA → Approval → Deploy → Applied.

> **Source of truth**: [GitHub Project Board #4](https://github.com/users/packetqc/projects/4)
> Last sync: 2026-03-01 (legacy board). K2.0 tracking via this file + GitHub issues on packetqc/K_DOCS.

---

## What's New

| Date | Update |
|------|--------|
| 2026-03-16 | **Root essential files restored** — LINKS.md, NEWS.md, PLAN.md, STORIES.md, VERSION.md updated for K_DOCS context. Navigator methodologies widget (16 files, 5 modules). Social sharing URLs migrated to K_DOCS base. |
| 2026-03-15 | **Stories #25 + #26** — Live Mindmap Memory + One Viewer to Rule Them All |
| 2026-03-14 | **K2.0 publication text review complete** — 13 publications, 15 commits, deep K2.0 terminology alignment |
| 2026-03-10 | **Story #24 — The Toggle** — 852 files moved, 158 paths remapped, zero breakage |
| 2026-03-08 | **Story #23 — Knowledge v2.0 Platform** — from questionnaire to living engineering platform |
| 2026-03-07 | **Story #22 — Visual Documentation Engine** — video to evidence with computer vision |
| 2026-03-06 | **v59 — Integrity state machine** — 29-checkpoint instrument panel enforcing agent identity |
| 2026-03-05 | **v57/v58** — STAGE:/STEP: label sync + agent identity |
| 2026-03-04 | **v56 — PreToolUse enforcement** — hook architecture that blocks edits until protocol gates pass |
| 2026-03-03 | **v55 — Session notes → issue + CHANGELOG.md** — session notes posted as issue comment at save |
| 2026-03-02 | **Publication #22 — Visual Documentation** — `visual` command, OpenCV + Pillow + NumPy |
| 2026-03-02 | **#0a Bootstrap Optimization** — CLAUDE.md 3872 → 714 lines (81% reduction) |
| 2026-03-01 | **Main Navigator (I2)** — iframe embed mode, state persistence, arrow alignment, universal anchors |
| 2026-03-01 | **v53/v54** — Autonomous Execution Principle, Strategic Remote Check, four-channel persistence |

[Full changelog → NEWS.md](NEWS.md)

---

## Ongoing

Active work items — started but not yet completed.

### OG URL Migration

**Status**: 🔧 In progress
**Priority**: High

Redirect HTML pages in `docs/` still use `packetqc.github.io/knowledge` in `og:url` meta tags. Need to migrate all 165+ redirect pages (EN+FR) to use `packetqc.github.io/K_DOCS` base URL. Identified in LINKS.md Known Gaps section.

### Hub/Landing Pages K2.0 Review

**Status**: 🔧 In progress
**Priority**: Medium

Publication hub pages, interface hubs, and landing pages need K2.0 terminology review. Text review for 13 publications is complete; hub pages remain.

### Publication Index Ordering

**Status**: 📋 Planned
**Priority**: Low

Reorder publication index to show core docs first instead of chronological order.

### 4-Theme Accessibility System

**Status**: 🔧 In progress
**Priority**: Medium

4-theme selector (Cayman, Midnight, Daltonism Light, Daltonism Dark) implemented in CSS + JS. Awaiting visual QA on GitHub Pages.

---

## Fixes

Known issues to address.

### Publication/Doc Version Numbers

**Status**: 🔴 Open
**Scope**: All publications and docs

Version banner shows `version` front matter field (e.g., "v1") but this is the publication version, not the knowledge version. Pages should reflect the current knowledge version at time of last content update.

### Mindmap Webcard Documentation Gap

**Status**: 🔴 Open
**Scope**: Publication #5

Dynamic webcard generation using MindElixir mindmap is not yet documented in Publication #5 (Webcards & Social Sharing).

---

## Planned

Items analyzed and scheduled but not yet started.

### Publication Freshness Review

**Status**: ✅ Resolved (2026-03-14)

~~Publications #1–#8 need review against current knowledge version.~~ Resolved: 13 publications deep-reviewed for K2.0 terminology in Phase 2 text review (15 commits).

### Complete Publication Full Pages

**Status**: 📋 Planned

Publications #0–#4 have source + summary only. Their summary pages link to GitHub README.md until complete web pages (`/full/`) are created.

---

## Forecast

Future projects and capabilities — known direction, not yet scheduled.

### Knowledge-Live PQC Hardware Security

Post-quantum cryptography with hardware-backed key storage using STM32 secure element. Upgrade from software-only PQC Envelope to hardware-held ML-KEM-1024 keys.

### Beacon Network Encrypted Communications

PQC-secured beacon-to-beacon communication. When both peers support ML-KEM-1024 (OpenSSL 3.5+), connections are quantum-resistant.

### Multi-Satellite Real-Time Sync

Evolve from asynchronous git-mediated sync to real-time inter-instance communication via beacon network.

### `bytearray` + `mlock` Token Hardening

Store tokens in `bytearray` (mutable, zeroing), `mlock()` on secret-holding memory, `prctl(PR_SET_DUMPABLE, 0)`.

---

<details>
<summary>Legacy (v1 — packetqc/knowledge repo)</summary>

### Resolved (Legacy)

| Item | Status | Resolution |
|------|--------|------------|
| CLAUDE.md Size at Download | ✅ Resolved (2026-03-02) | Condensation: 3872 → 714 lines (81% reduction) |
| Webcard Coverage Gaps | ✅ Resolved (PR #150, #162) | 68 GIFs total (17 cards × 2 themes × 2 langs) |
| Conformity Report #9a | ✅ Resolved (2026-02-23) | 16/23 ✅ Applied, 2 By design, 4 Planned, 1 Future |
| Export Documentation | 🔧 In progress | PDF/DOCX implemented, not yet documented in #5 |
| Seamless Evolution Relay | 🔧 In progress | Story #5 captured, web pages need sync |

### Legacy Recalls

| Item | Status |
|------|--------|
| Stranded Branch Intelligence | 🔍 Pending recover |
| Session Note Mining | 🔍 Pending recall |
| Cross-Session Pattern Detection | 🔍 Pending recall |
| Unfinished Protocol Discoveries | 🔍 Pending recall |

### Legacy Forecast

- Hardware-Backed Token Storage (STM32)
- Resiliency Documentation & Implementation
- Satellite Bootstrap Road Test (v25 protocol)

</details>

---

*Last updated: 2026-03-16*
