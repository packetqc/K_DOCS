# Security by Design — Owner-Scoped AI Knowledge Architecture

**Publication #9 — Security Model for Public AI Knowledge Repositories**

*By Martin Paquet & Claude (Anthropic, Opus 4.6)*
*v1 — February 2026*

---

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. 30 years of experience spanning network security, embedded systems, and telecom. Designed the owner-scoped security model ensuring Knowledge remains safe as a public repository.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Performed comprehensive security audits of the repository, scanning all branches, git history, and file content for credentials, tokens, and sensitive data.

---

## Abstract

AI-assisted development systems that persist knowledge across sessions and projects face a fundamental security question: **what happens when the repository goes public?** Session notes, harvested satellite data, configuration files, and automation scripts — can any of this compromise the owner's accounts?

**Knowledge** (`packetqc/knowledge`) is designed from the ground up to be **public-safe and owner-scoped**. Every component — from session persistence to distributed harvest to automated deployment — operates within security boundaries that make the repository safe to fork, clone, and publish:

1. **Zero credentials stored** — No API keys, tokens, passwords, SSH keys, or certificates anywhere in files or git history across all branches
2. **Proxy-scoped push access** — Claude Code sessions can only push to their assigned task branch in their assigned repo. No cross-branch, no cross-repo writes
3. **Owner-namespaced operations** — All harvest, wakeup, and sync URLs reference the owner's GitHub namespace. A forker gets methodology (intentionally public), not account access
4. **Environmentally isolated** — Session notes, satellite references, and `minds/` data are per-owner. A fork starts clean
5. **PR-gated delivery** — No direct writes to shared branches. Every change goes through a pull request requiring owner approval

This publication documents the security model, the audit methodology, the threat analysis, and the fork/clone safety guarantees that make Knowledge safe as a public, forkable repository.

---

## Table of Contents

- [The Security Question](#the-security-question)
- [Threat Model](#threat-model)
- [Security Layers](#security-layers)
- [Credential Audit](#credential-audit)
- [Fork & Clone Safety](#fork--clone-safety)
- [Proxy Architecture](#proxy-architecture)
- [Owner-Scoped Operations](#owner-scoped-operations)
- [What a Forker Gets](#what-a-forker-gets)
- [What a Forker Must Change](#what-a-forker-must-change)
- [Audit Methodology](#audit-methodology)
- [Design Principles](#design-principles)
- [Related Publications](#related-publications)

---

## The Security Question

When an AI-assisted development system persists knowledge — session notes, project decisions, harvested satellite data, automation scripts — and that system lives in a git repository, making the repository public raises legitimate concerns:

| Concern | Risk |
|---------|------|
| **Credential leakage** | API keys, tokens, or passwords accidentally committed to git history |
| **Account compromise** | Session URLs, OAuth tokens, or auth headers exposing account access |
| **Cross-contamination** | A forker's operations affecting the original owner's repos or accounts |
| **Data exposure** | Private project details, internal IPs, or personal information beyond published content |
| **Privilege escalation** | A forker gaining write access to the original owner's branches or repos |

Knowledge addresses each of these by design — not by post-hoc scrubbing, but by architectural decisions that make credential storage unnecessary and cross-owner operations impossible.

---

## Threat Model

### What We Protect Against

| Threat | Attack vector | Protection |
|--------|--------------|------------|
| **Credential theft** | Scanning git history for leaked tokens | No credentials are ever stored — `.gitignore` blocks sensitive file patterns, audit confirms zero matches across all branches |
| **Session hijacking** | Extracting Claude session URLs from commits | Session URLs expire after use; only appear in commit metadata (auto-appended by protocol), never in file content |
| **Repo takeover** | Forker pushing to original owner's branches | Proxy architecture scopes push to assigned branch only — cross-repo push returns 403 |
| **Satellite infiltration** | Forker's harvest accessing original owner's private repos | Harvest uses public HTTPS only — private repos return 403/404, marked `unreachable` |
| **Data exfiltration** | Extracting private project details from `minds/` | `minds/` contains only metadata (repo names, version numbers, status) — no source code, no credentials |
| **Social engineering** | Using published contact info to compromise accounts | Only intentionally published info (email, LinkedIn, GitHub handle) — no private data |

### What We Don't Protect Against

| Out of scope | Why |
|-------------|-----|
| **GitHub account compromise** | Orthogonal to Knowledge — use 2FA, strong passwords |
| **Claude API key theft** | API keys are never stored in the repo — they live in the user's local environment |
| **Malicious fork modifications** | A forker can modify their own fork freely — this doesn't affect the original |
| **Supply chain attacks** | Knowledge has no dependencies — it's pure markdown, git, and one Python script |

---

## Security Layers

The system's security is layered — each layer provides independent protection:

```
Layer 1: .gitignore          — Prevents sensitive files from being committed
Layer 2: Zero-credential     — No credentials needed by design (public HTTPS, proxy auth)
Layer 3: Proxy scoping       — Push access limited to assigned branch in assigned repo
Layer 4: PR-gated delivery   — No direct writes to shared branches
Layer 5: Owner-namespacing   — All URLs reference owner's namespace, not hardcoded tokens
Layer 6: Environmental isolation — Session data, minds/, notes/ are per-owner
Layer 7: Continuous audit    — Security checks on every harvest and normalize
```

### Layer 1: .gitignore

The repository's `.gitignore` includes a dedicated secrets section:

```
# Secrets / credentials
.env
.env.*
*.pem
*.key
*.p12
credentials.*
secrets.*
```

This is the first line of defense — preventing common sensitive file patterns from being committed. Present on all branches.

### Layer 2: Zero-Credential Architecture

Knowledge never needs credentials in its repository because:

- **Git operations** use public HTTPS URLs — no SSH keys, no tokens in URLs
- **Claude Code authentication** is handled by the proxy — the repo never sees auth tokens
- **GitHub API** access uses `gh` CLI which authenticates via the user's local config, not stored tokens
- **No external services** are called — no API keys, no webhook secrets, no database credentials

This is the most important layer: **the absence of credentials is a design choice, not a cleanup effort**.

### Layer 3: Proxy Architecture

Claude Code sessions run behind a proxy that enforces strict access boundaries:

| Boundary | Enforcement |
|----------|------------|
| **Branch scope** | Push access to the exact assigned `claude/<task-id>` branch only |
| **Repo scope** | Push access to the current repo only — cross-repo push returns 403 |
| **Direction** | Write operations are proxied; read operations use public HTTPS directly |

A forker's Claude Code sessions get their own proxy-assigned branches in their own fork. They cannot push to the original repo's branches — the proxy doesn't authorize it.

### Layer 4: PR-Gated Delivery

No Claude Code session can write directly to `main` (or `master`). Every change follows:

```
work on claude/<task-id> → commit → push to task branch → create PR → owner approves → merge to main
```

The owner's PR approval is the gate. This prevents both accidental and intentional writes to shared branches.

### Layer 5: Owner-Namespacing

All repository URLs in Knowledge use the owner's namespace:

```
https://github.com/packetqc/knowledge          ← core knowledge repo
https://github.com/packetqc/<satellite-name>    ← satellite repos
```

A forker's clone inherits these URLs, but:
- **Read operations** access the original owner's public repos (read-only — intentional)
- **Write operations** fail because the proxy scopes push to the forker's own repos
- To use the system for their own projects, the forker replaces `packetqc` with their username

The namespace is the security boundary — not tokens, not keys.

### Layer 6: Environmental Isolation

Per-owner data that starts blank in a fork:

| Component | Content | In a fork |
|-----------|---------|-----------|
| `notes/` | Session memory | Empty — each user builds their own |
| `minds/` | Harvested satellite data | References original owner's repos — meaningless for forker |
| Dashboard | Network status table | Reflects original owner's network — static until forker runs own harvests |
| Git history | Commit messages with session URLs | Session URLs expire; no credentials |

### Layer 7: Continuous Audit

The `normalize` and `harvest` commands include security-adjacent checks:

- **`normalize`** verifies no hardcoded paths, validates asset references, checks link integrity
- **`harvest`** verifies repo accessibility, reports unreachable satellites, validates version tags
- **Manual audit** — periodic full-history scan using regex patterns for credential patterns (see Audit Methodology)

---

## Credential Audit

A comprehensive audit was performed across all branches, scanning git history and file content for sensitive patterns:

### Patterns Scanned

| Category | Patterns | Result |
|----------|----------|--------|
| GitHub tokens | `ghp_`, `gho_`, `github_pat_` | **None found** |
| Anthropic/OpenAI keys | `sk-`, `sk-ant-`, `sk-live_`, `sk-proj_` | **None found** |
| AWS keys | `AKIA`, `ASIA` | **None found** |
| Slack tokens | `xoxb-`, `xoxp-` | **None found** |
| Private keys | `-----BEGIN PRIVATE KEY`, `-----BEGIN RSA` | **None found** |
| Passwords in code | `password\s*=\s*["']`, `secret\s*=\s*["']` | **None found** |
| Auth headers | `Bearer `, `Basic ` with actual values | **None found** |
| URLs with credentials | `://[^@]+@` | **None found** |
| JWT tokens | `eyJ[A-Za-z0-9_-]+\.eyJ` | **None found** |
| Webhook URLs with tokens | `hooks.slack.com`, `discord.com/api/webhooks` | **None found** |

### Branches Scanned

All 7 branches (local + remote) were scanned:
- `claude/implement-save-wxnpG`
- `claude/knowledge`
- `master`
- `remotes/origin/claude/implement-save-wxnpG`
- `remotes/origin/claude/knowledge`
- `remotes/origin/knowledge`
- `remotes/origin/main`

### Finding: Zero Credentials

No credentials, tokens, API keys, or authentication material found anywhere — not in current files, not in git history, not on any branch. The `.gitignore` has appropriate patterns for common sensitive files.

### Intentionally Public Data

The following data is intentionally public:
- `packetqcca@gmail.com` — published contact email
- `packetqc` / `martypacket` — public GitHub/LinkedIn handles
- GitHub repository URLs — public repos by design
- `localhost:8554` RTSP references — local development only, not externally reachable

---

## Fork & Clone Safety

This section answers the central question: **what happens when someone forks or clones this repository?**

### What a Forker Gets

| Component | What they receive | Security impact |
|-----------|------------------|----------------|
| **Methodology** | Session persistence, lifecycle protocol, commands | Intentionally public — the whole point |
| **Publications** | 10 technical papers with full content | Intentionally public — published for sharing |
| **Tooling** | Live capture scripts, webcard generator | Intentionally public — reusable tools |
| **Profile data** | Author name, email, LinkedIn, GitHub | Intentionally public — published contact info |
| **Git history** | Commits with session URLs in messages | Session URLs expire; no credentials |
| **`minds/` data** | Satellite repo names, versions, status | Metadata only — no source code, no secrets |
| **`notes/` files** | Session working memory | Historical context — no sensitive data |

### What a Forker Cannot Do

| Action | Why it's blocked |
|--------|-----------------|
| Push to original repo's branches | Proxy scopes push to forker's own repo only |
| Access original owner's private repos | Harvest uses public HTTPS — private repos return 403/404 |
| Compromise original owner's GitHub account | No tokens or credentials stored anywhere |
| Compromise original owner's Claude account | No API keys stored; session URLs expire |
| Modify original owner's satellites | Cross-repo push is impossible (proxy-scoped) |
| Read original owner's private data | Only publicly published data is in the repo |

### What a Forker Must Change

To use Knowledge for their own projects, a forker needs to:

1. **Replace `packetqc` with their GitHub username** in CLAUDE.md — this redirects all harvest, wakeup, and sync operations to their own namespace
2. **Create their own satellite repos** — the forker's knowledge system bootstraps from their own projects
3. **Update profile data** — replace author information with their own

Everything else adapts automatically. The system is designed to be namespace-portable.

---

## Proxy Architecture

Claude Code sessions — whether the desktop app, VS Code extension, or web interface — all operate behind a proxy that enforces security boundaries.

### How the Proxy Works

```
Claude Code session
    ↓
Proxy (authentication + authorization)
    ↓ allowed: push to assigned claude/<task-id> branch in current repo
    ✗ blocked: push to main, push to other branches, push to other repos
    ↓
GitHub API
```

### What the Proxy Enforces

| Rule | Effect |
|------|--------|
| **Branch restriction** | Only the exact assigned `claude/<task-id>` branch can receive pushes |
| **Repo restriction** | Only the current session's repo can receive pushes |
| **Direction restriction** | Only write operations are proxied; reads use public HTTPS |
| **Identity** | Commits are signed as `Claude <noreply@anthropic.com>` |

### Cross-Repo Implications

- A session in repo A cannot push to repo B — the proxy blocks it with 403
- `harvest --fix` prepares remediation locally but cannot push to satellite repos
- Satellites self-heal on next `wakeup` by reading updated core (pull-based)
- The user can manually push from their terminal for cross-repo operations

This proxy architecture is the foundational security guarantee. Even if credentials were accidentally committed (they aren't), the proxy prevents any Claude Code session from writing outside its authorized scope.

---

## Owner-Scoped Operations

Every command in Knowledge operates within the owner's namespace:

| Command | What it accesses | Scope |
|---------|-----------------|-------|
| `wakeup` | `https://github.com/<owner>/knowledge` | Read-only, public HTTPS |
| `harvest <project>` | `https://github.com/<owner>/<project>` | Read-only, public HTTPS |
| `harvest --fix` | Local task branch only | Write scoped to assigned branch |
| `save` | Local task branch → PR to `main` | Write scoped to assigned branch |
| `normalize` | Local files only | No network access |
| `webcard` | Local files only | No network access |

The `<owner>` is derived from CLAUDE.md — currently `packetqc`. A forker who changes this to their own username gets all operations pointing at their own repos.

---

## Audit Methodology

To verify the security posture of a public knowledge repository, follow this audit procedure:

### Step 1: Scan All Branches

```bash
git branch -a                    # List all branches
git log --all --name-only        # Check for sensitive filenames
```

### Step 2: Scan Git History for Credential Patterns

Search all diffs across all branches for common credential patterns:
- GitHub tokens: `ghp_`, `gho_`, `github_pat_`
- API keys: `sk-`, `AKIA`, `xoxb-`
- Private keys: `BEGIN PRIVATE KEY`, `BEGIN RSA`
- Passwords: `password=`, `secret=` with quoted values
- Auth headers: `Bearer`, `Basic` with actual values
- URLs with credentials: `://user:pass@host`

### Step 3: Verify .gitignore Coverage

Confirm `.gitignore` blocks common sensitive patterns:
- `.env`, `.env.*`
- `*.pem`, `*.key`, `*.p12`
- `credentials.*`, `secrets.*`

### Step 4: Check File Content

Scan current files for:
- Session URLs (should only be in commit messages, not file content)
- Internal IPs or hostnames
- Email addresses beyond published contact info
- Webhook URLs with tokens

### Step 5: Verify Proxy Scoping

Confirm that:
- Push operations only succeed to the assigned task branch
- Push to `main` returns 403
- Cross-repo push returns 403

---

## Design Principles

1. **Credentials are unnecessary, not scrubbed** — The architecture never requires storing credentials. This is stronger than "we deleted the tokens" — there were never tokens to delete.

2. **The namespace is the boundary** — Security comes from owner-scoping, not from secrets. Changing the GitHub username redirects the entire system.

3. **Public by default** — Every component is designed to be safely public. Private data stays in the user's local environment, never in the repo.

4. **Defense in depth** — Seven independent layers. Failure of any single layer doesn't compromise security.

5. **Audit-friendly** — The entire security posture can be verified with standard git tools and regex pattern scanning.

6. **Fork-friendly** — The system is designed to be forked. A forker gets methodology and tooling, not access.

---

## PAT Access Levels

Knowledge defines 4 progressive levels of GitHub Personal Access Token (PAT) configuration. Each level enables specific operations and maps to a discovered architecture layer:

| Level | PAT Configuration | GitHub Scope | What it enables | Operational mode |
|-------|------------------|-------------|-----------------|-----------------|
| **0** | **No PAT** | Proxy only | Public repos: clone (initial only), push to assigned branch, manual PR creation | Semi-automatic — user creates PRs manually from GitHub web UI |
| **1** | **Fine-grained Read-only** | `Contents: Read` on specific repos | Level 0 + clone/fetch private satellite repos for `harvest` and `wakeup` | Semi-automatic + private repo visibility |
| **2** | **Fine-grained Read-Write** | `Contents: Read-Write` + `Pull requests: Read-Write` + `Projects: Read-Write` on specific repos | Level 1 + API-mediated PR create, merge, branch operations, and GitHub Project board management via `curl` to `api.github.com` | **Full autonomous** — recommended |
| **3** | **Classic PAT `repo`** | Full `repo` scope (all repos, all permissions) | Everything — but grants far more access than needed | Full autonomous — **not recommended** (violates least privilege) |

### Level Selection Guide

| Scenario | Recommended level | Why |
|----------|------------------|-----|
| All repos public, occasional use | **0** | No token needed — proxy handles assigned branch |
| Private satellites, read-only harvest | **1** | Minimum needed to see private repos |
| Full autonomous operation (daily use) | **2** | PR create + merge via API, scoped to specific repos |
| Quick testing, throwaway session | **3** | Convenient but overly broad — avoid for regular use |

### Architecture Mapping

Each level corresponds to a specific architecture discovery in the Knowledge Evolution:

- **Level 0** = Proxy reality (v17) — Claude Code sessions run behind a proxy that scopes push access to the assigned task branch only. Without a PAT, all operations go through this proxy. PRs must be created manually by the user from the GitHub web UI.
- **Level 1** = Ephemeral token protocol (v27) — A fine-grained PAT with read-only Contents scope enables `git clone` of private repos. The token is ephemeral (dies with the session, never persisted). This unlocks `harvest` visibility into private satellites.
- **Level 2** = API bypass (v28) — The two-channel model: git operations go through the proxy (restricted), but the GitHub REST API (`api.github.com`) goes direct when authenticated. A PAT with read-write Contents + Pull requests + Projects scope enables full autonomous operation: commit → push (proxy) → create PR (API) → merge PR (API) → manage GitHub Project boards (API). This is the recommended level for daily use.
- **Level 3** = Classic PAT with full `repo` scope — grants access to ALL repositories, including those unrelated to Knowledge. Functionally identical to Level 2 but with unnecessarily broad permissions. Not recommended — violates the principle of least privilege.

### Level 2 — Confirmed Minimum Permissions

Validated on 2026-02-21 via full autonomous cycle (create PR #137 + merge via API). The token was probed against all GitHub API permission areas to identify exactly what is required:

| Fine-grained Permission | Required | What it enables |
|-------------------------|----------|-----------------|
| **Contents: Read and write** | **YES** | Clone repos, branch operations via API |
| **Pull requests: Read and write** | **YES** | Create PR + merge PR via `api.github.com` |
| **Projects: Read and write** | **YES** | Create and manage GitHub Project boards (`project create`, `project register`) |
| **Metadata: Read-only** | **YES** (mandatory) | Auto-included by GitHub on all fine-grained tokens — cannot be unchecked |
| Issues | No | Accessible but not used by autonomy cycle |
| Actions | No | Accessible but not used by autonomy cycle |
| Webhooks | No | Accessible but not used by autonomy cycle |
| Pages | No | Accessible but not used by autonomy cycle |
| Administration | No | Not granted, not needed |

**Result**: Only **4 fine-grained permissions** are required (3 selected + 1 mandatory) for the complete knowledge autonomy cycle. A token with `Contents: RW` + `Pull requests: RW` + `Projects: RW` + `Metadata: Read` (auto-included) scoped to specific repositories achieves the same full cycle as a classic `repo`-scoped PAT — without granting unnecessary access to Issues, Actions, Webhooks, Pages, or Administration.

### Principle of Least Privilege

Always use the lowest level that meets the session's needs. The PAT access levels embody defense in depth:

1. **Scope to specific repos** — Fine-grained tokens (Levels 1–2) can be restricted to only the repos that Knowledge operates on
2. **Scope to minimum permissions** — Read-only (Level 1) when you only need harvest visibility, Read-write (Level 2) when you need autonomous PR operations and GitHub Project board management
3. **Short expiration** — 7–30 days recommended. The token is ephemeral in the session, but the PAT itself persists on GitHub until it expires
4. **Session-scoped usage** — The token lives only in context memory, never written to files, never committed, never echoed back (see Ephemeral Token Protocol)

---

## Token Lifecycle Security — Reception to Disposal

The ephemeral token moves through 5 phases. Each phase has specific security properties mapped to industry standards. **OWASP MCP01:2025** ranks Token Mismanagement as the **#1 risk** for AI-assisted development tools — our ephemeral-by-design architecture directly addresses this.

### Phase 1 — Reception

| Method | Channel | Security property |
|--------|---------|-------------------|
| **Paste (recommended)** | Text in chat | No file I/O, no temp file. Token enters context memory directly |
| **PQC Envelope** | Encrypted blob | Encrypted in transit (X25519 or ML-KEM-1024), decrypted in-session |
| **Image upload (fallback)** | Screenshot | Temp file in `/tmp/` — deleted immediately after extraction |

**Industry alignment**: OWASP Secrets Management — secure input channels, no logging, no echo. PQC Envelope adds NIST SP 800-175B encryption in transit.

### Phase 2 — In-Memory Persistence

| Location | What's stored | Protection | Lifetime |
|----------|---------------|------------|----------|
| **Claude context window** | Token string | Process isolation, containerized (no swap) | Session duration |
| **Python variable** (PQC path) | Decrypted string | Plain in process memory | Until scope exit |
| **`/dev/shm/`** | Key material only | Zero-overwritten on `destroy()` | Until `PQCEnvelope.__exit__()` |

The token is **not encrypted in memory** after reception. This is consistent with industry practice — in-memory encryption requires decrypt-on-every-use and the decryption key must coexist in process memory, making it security theater without hardware backing (HSM/TPM/SGX).

**Future upgrade**: The knowledge-live PQC project targets hardware-backed key storage (STM32 secure element). With a hardware-held key, the token could be encrypted in RAM with genuine protection — the key never enters process memory. This is the real upgrade path, not software-only in-memory encryption.

### Phase 3 — Usage

| Operation | Exposure | Mitigation |
|-----------|----------|------------|
| `curl -H "Authorization: token <T>"` | Process list (`/proc/<pid>/cmdline`) | Container isolation — no cross-user visibility |
| `git clone https://<T>@github.com/...` | Process list (URL-embedded) | Container isolation + prefer header-based auth |
| GitHub REST API over HTTPS | None — TLS 1.3 in transit | Encrypted on wire |

### Phase 4 — Disposal

| Material | Disposal method | When |
|----------|----------------|------|
| Context window | Destroyed by Anthropic runtime | Session end (automatic) |
| Python variable | Garbage collected (not zero-overwritten) | Scope exit |
| Key material (`/dev/shm/`) | `_secure_delete()`: zero-overwrite + unlink | `destroy()` call |
| Image file (if uploaded) | `rm -f` immediately | After extraction |

**Known gap**: Python strings are immutable — garbage collection does not zero memory before freeing (Python bug #17405, open since 2013). Token may persist in freed pages until reuse. **Planned improvements**: store tokens in `bytearray` (mutable, zero-erasable in-place), add `mlock()` to prevent swap exposure (FIPS 140-3, HashiCorp Vault pattern), `prctl(PR_SET_DUMPABLE, 0)` to prevent core dumps, explicit zeroing before dereference (NIST SP 800-57 §8.3.4).

### Phase 5 — Post-Session Verification

Verify no token residue: no files contain `github_pat_`, no git history contains it, no environment variables reference it. Container teardown destroys all process memory.

### Compliance Summary

| Standard | Requirement | Status |
|----------|-------------|--------|
| **OWASP Secrets Management** | No logging, no echo, minimum persistence | ✅ Compliant |
| **OWASP MCP01:2025** | Prevent token persistence in AI context/memory | ✅ Compliant — ephemeral by design |
| **NIST SP 800-63B** §5.1.1 | Ephemeral authenticators not stored beyond need | ✅ Compliant |
| **NIST SP 800-57** §8.3.4 | Key destruction — zeroize beyond recovery | ⚠️ Partial — keys yes, token pending |
| **NIST SP 800-88** | Media sanitization (applied to RAM) | ⚠️ Partial — keys yes, token string pending |
| **FIPS 140-3** | Zeroization of all unprotected SSPs | ⚠️ Partial — `/dev/shm` yes, Python variables pending |
| **CIS Control 3.10** | No secrets in source code | ✅ Compliant |
| **pyATS secret_strings** pattern | Encrypted at-rest for persistent secrets | N/A — token never at rest (by design) |
| **Hardware-backed encryption** | HSM/TPM for key protection | 🔮 Planned — knowledge-live PQC project |

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge](../knowledge-system/v1/README.md) | Parent — the system this publication secures |
| 3 | [AI Session Persistence](../ai-session-persistence/v1/README.md) | Session notes security model |
| 4 | [Distributed Minds](../distributed-minds/v1/README.md) | Harvest security scope |
| 4a | [Knowledge Dashboard](../distributed-knowledge-dashboard/v1/README.md) | Dashboard data exposure model |
| 7 | [Harvest Protocol](../harvest-protocol/v1/README.md) | Harvest access controls |
| 8 | [Session Management](../session-management/v1/README.md) | Save protocol proxy constraints |

---

## Publication Notice

This publication is part of the **MPLIB Knowledge** project — a self-evolving AI engineering intelligence system.

| | |
|---|---|
| **Authors** | Martin Paquet & Claude (Anthropic, Opus 4.6) |
| **Knowledge** | [packetqc/knowledge](https://github.com/packetqc/knowledge) |
| **Contact** | packetqcca@gmail.com |
| **License** | © 2026 Martin Paquet & Claude (Anthropic) |
