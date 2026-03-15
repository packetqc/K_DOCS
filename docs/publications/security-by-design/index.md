---
layout: publication
title: "Security by Design — Owner-Scoped AI Knowledge Architecture"
description: "Security model for public AI knowledge repositories: zero credentials stored, proxy-scoped push access, owner-namespaced operations, environmental isolation, and PR-gated delivery. Comprehensive threat model and audit methodology for Knowledge."
pub_id: "Publication #9"
version: "v2"
date: "2026-02-21"
permalink: /publications/security-by-design/
og_image: /assets/og/security-by-design-en-cayman.gif
keywords: "security, PQC, access control, fork safety, privacy, owner-scoped"
---

# Security by Design — Owner-Scoped AI Knowledge Architecture
{: #pub-title}

> **Parent publication**: [#0 — Knowledge]({{ '/publications/knowledge-system/' | relative_url }})

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | System overview and public-safe architecture |
| [The Security Question](#the-security-question) | Why public repos need architectural security |
| [Threat Model](#threat-model) | Threats addressed and protections in place |
| [Security Layers](#security-layers) | Seven-layer defense architecture |
| [Credential Audit](#credential-audit) | Comprehensive scan results across all branches |
| [Fork & Clone Safety](#fork--clone-safety) | Guarantees for public forking and cloning |
| [PAT Access Levels](#pat-access-levels) | Token configuration tiers and scope mapping |
| [Token Lifecycle Security](#token-lifecycle-security) | Ephemeral token handling from reception to disposal |
| [Design Principles](#design-principles) | Core security design principles |

## Abstract

AI-assisted development systems that persist knowledge across sessions and projects face a fundamental security question: **what happens when the repository goes public?**

Knowledge is designed from the ground up to be **public-safe and owner-scoped**. Every component operates within security boundaries that make the repository safe to fork, clone, and publish:

| Protection | Description |
|------------|-------------|
| **Zero credentials stored** | No API keys, tokens, passwords, or certificates anywhere in files or git history |
| **Proxy-scoped push access** | Sessions can only push to their assigned branch in their assigned repo |
| **Owner-namespaced operations** | All URLs reference the owner's GitHub namespace, not hardcoded tokens |
| **Environmentally isolated** | Session notes, satellite references, and `minds/` data are per-owner |
| **PR-gated delivery** | No direct writes to shared branches |

## The Security Question

When an AI-assisted development system persists knowledge and that system lives in a git repository, making the repository public raises legitimate concerns: credential leakage, account compromise, cross-contamination between forker and owner, data exposure, and privilege escalation.

Knowledge addresses each by **architectural design** — not by post-hoc scrubbing, but by decisions that make credential storage unnecessary and cross-owner operations impossible.

## Threat Model

| Threat | Protection |
|--------|-----------|
| **Credential theft** | No credentials ever stored — `.gitignore` blocks sensitive patterns, audit confirms zero matches |
| **Session hijacking** | Session URLs expire; only in commit metadata, never in file content |
| **Repo takeover** | Proxy scopes push to assigned branch only — cross-repo returns 403 |
| **Satellite infiltration** | Harvest uses public HTTPS only — private repos return 403/404 |
| **Data exfiltration** | `minds/` contains only metadata — no source code, no credentials |

## Security Layers

Seven independent layers of protection:

| Layer | Protection | Description |
|-------|------------|-------------|
| 1 | **`.gitignore`** | Blocks `.env`, `.pem`, `.key`, `.p12`, `credentials.*`, `secrets.*` |
| 2 | **Zero-credential architecture** | Public HTTPS for reads, proxy for auth — no tokens needed in repo |
| 3 | **Proxy scoping** | Push to assigned `claude/<task-id>` branch only, current repo only |
| 4 | **PR-gated delivery** | All changes to `main` require owner approval |
| 5 | **Owner-namespacing** | URLs use `packetqc/<repo>` — forker changes namespace to use their own |
| 6 | **Environmental isolation** | `notes/`, `minds/`, dashboard are per-owner |
| 7 | **Continuous audit** | `normalize` and `harvest` include security-adjacent checks |

## Credential Audit

Comprehensive scan across all branches:

| Category | Patterns | Result |
|----------|----------|--------|
| GitHub tokens | `ghp_`, `gho_`, `github_pat_` | **None found** |
| API keys | `sk-`, `sk-ant-`, `AKIA` | **None found** |
| Private keys | `BEGIN PRIVATE KEY`, `BEGIN RSA` | **None found** |
| Passwords | `password=`, `secret=` with values | **None found** |
| Auth headers | `Bearer`, `Basic` with values | **None found** |
| URLs with credentials | `://user:pass@host` | **None found** |

## Fork & Clone Safety

**What a forker gets**: methodology, publications, tooling, published profile data — all intentionally public. No account access, no credentials, no attack surface.

**What a forker cannot do**: push to original repo, access private repos, compromise accounts, modify satellites.

**What a forker changes**: replace `packetqc` with their GitHub username in CLAUDE.md. Everything else adapts automatically.

## PAT Access Levels

4 progressive levels of GitHub PAT configuration, from least to most privileged:

| Level | Configuration | Enables | Mode |
|-------|--------------|---------|------|
| **0** | No PAT (proxy only) | Public repos, assigned branch push, manual PRs | Semi-automatic |
| **1** | Fine-grained Read-only | + private repo clone/fetch for harvest | Semi-auto + private visibility |
| **2** | Fine-grained Read-Write | + API PR create/merge + GitHub Project boards (full autonomous) | **Recommended** |
| **3** | Classic PAT `repo` | Everything — but violates least privilege | Not recommended |

**Level 2 confirmed minimum** (validated 2026-02-21 — PR #137 full cycle): Only **4 permissions** required: `Contents: RW` + `Pull requests: RW` + `Projects: RW` + `Metadata: Read` (mandatory, auto-included). Issues, Actions, Webhooks, Pages, Administration — none needed for autonomy.

Each level maps to an architecture discovery: L0=v17 proxy, L1=v27 ephemeral token, L2=v28 API bypass, L3=classic overreach.

## Token Lifecycle Security

The token moves through 5 phases — reception, in-memory persistence, usage, disposal, post-session verification. Each phase maps to industry standards (OWASP Secrets Management, OWASP MCP01:2025, NIST SP 800-63B, FIPS 140-3, CIS Controls). OWASP MCP01:2025 ranks Token Mismanagement as the **#1 risk** for AI tools — our ephemeral-by-design architecture directly addresses this.

**Reception**: Paste (recommended, no file I/O) or PQC Envelope (encrypted in transit) or image upload (fallback, temp file deleted immediately).

**In-memory**: Token is NOT encrypted in RAM — consistent with industry practice. In-memory encryption without hardware backing (HSM/TPM) is security theater. **Future**: knowledge-live PQC project targets hardware-backed key storage (STM32 secure element).

**Disposal**: Context window destroyed on session end. Key material zero-overwritten. **Gap**: Python strings not zero-overwritten before GC — planned fix via `ctypes.memset()`.

**Compliance**: OWASP ✅ | NIST SP 800-63B ✅ | NIST SP 800-88 ⚠️ (keys yes, token pending) | CIS 3.10 ✅

## Design Principles

| Principle | Description |
|-----------|-------------|
| **Credentials are unnecessary, not scrubbed** | The architecture never requires storing credentials |
| **The namespace is the boundary** | Security comes from owner-scoping, not secrets |
| **Public by default** | Private data stays in local environment, never in the repo |
| **Defense in depth** | Seven independent layers |
| **Audit-friendly** | Verifiable with standard git tools and regex scanning |
| **Fork-friendly** | Designed to be forked. Methodology and tooling, not access |

---

[**Read the full documentation →**]({{ '/publications/security-by-design/full/' | relative_url }}) | [**Compliance report →**]({{ '/publications/security-by-design/compliance/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
