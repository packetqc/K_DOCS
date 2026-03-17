# Project: PQC

<!-- project-id: P5 -->
<!-- project-type: child -->
<!-- project-status: pre-bootstrap -->
<!-- github-project: https://github.com/users/packetqc/projects/9 -->
<!-- parent-project: P0 -->

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | P5 |
| **Name** | PQC |
| **Type** | child of P0 |
| **Repository** | [packetqc/PQC](https://github.com/packetqc/PQC) |
| **GitHub Project** | [#9](https://github.com/users/packetqc/projects/9) |
| **Status** | 🔴 pre-bootstrap |
| **Created** | X |
| **Knowledge Version** | v0 |
| **Parent Index** | P0/S5 |
| **Description** | Post-Quantum Cryptography reference repository — pure reference, no CLAUDE.md, no knowledge integration yet |

**Role in ecosystem**: Reference repository for PQC algorithms and implementations. Not yet bootstrapped into Knowledge. 35 versions behind core.

---

## Publications

| Index | Title | Status |
|-------|-------|--------|
| P5/D1 | X | X |

---

## Satellites

| Index | Name | Repository | Version | Drift | Health |
|-------|------|------------|---------|-------|--------|
| P5/S1 | PQC | [packetqc/PQC](https://github.com/packetqc/PQC) | v0 | 🔴 35 | 🟢 healthy |


---

## Evolution

| Date | Entry |
|------|-------|
| X | Repository exists as PQC reference |
| 2026-02-21 | Detected by harvest healthcheck — pre-bootstrap, v0 |
| 2026-02-22 | Registered as child project P5 |

---

## Stories

(No stories yet — project is pre-bootstrap)

---

## Required Assets Status

| Asset | Status | Notes |
|-------|--------|-------|
| CLAUDE.md | 🔴 missing | No knowledge pointer |
| notes/ | 🔴 missing | No session persistence |
| live/ | 🔴 missing | No knowledge assets |
| publications/ | X | No publications |
| docs/ | X | No web presence |
| GitHub Project | 🟢 [#9](https://github.com/users/packetqc/projects/9) | Created 2026-02-22 |

---

## Remediation Plan

1. Open a Claude Code session in PQC repository
2. Type `wakeup` — step 0.5 will bootstrap scaffold
3. Merge the bootstrap PR
4. Run `harvest PQC` from core to update dashboard
