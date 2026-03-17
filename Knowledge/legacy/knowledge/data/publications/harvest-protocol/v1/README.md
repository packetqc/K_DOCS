# Harvest Protocol — Practical Guide

**Publication #7 — Distributed Knowledge Collection How-To**

*By Martin Paquet & Claude (Anthropic, Opus 4.6)*
*v1 — February 2026*

---

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Architect of the harvest protocol — the reverse-flow mechanism that pulls evolved knowledge from satellite projects back to the central master mind.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Executes harvest operations, crawls satellite repos, extracts insights, and manages the promotion pipeline.

---

## Abstract

Publication #4 (Distributed Minds) documents the **architecture** of bidirectional knowledge flow. This publication is the **practical guide** — how to actually use the `harvest` commands day-to-day.

The harvest protocol collects evolved knowledge from satellite projects and brings it to the central `minds/` folder. It tracks version drift, detects publications, promotes insights to core knowledge, and maintains a living dashboard of the entire network.

This guide covers: all harvest commands with examples, the promotion pipeline step-by-step, healthcheck sweeps, satellite remediation, and common workflows.

---

## Table of Contents

- [Quick Reference](#quick-reference)
- [Core Concept](#core-concept)
- [Harvesting a Satellite](#harvesting-a-satellite)
- [The Promotion Pipeline](#the-promotion-pipeline)
  - [Step 1: Harvest](#step-1-harvest)
  - [Step 2: Review](#step-2-review)
  - [Step 3: Stage](#step-3-stage)
  - [Step 4: Promote or Auto-Promote](#step-4-promote-or-auto-promote)
- [Network Healthcheck](#network-healthcheck)
- [Satellite Remediation](#satellite-remediation)
- [Contextual Help](#contextual-help)
- [Error Handling](#error-handling)
- [Common Workflows](#common-workflows)
- [What Gets Harvested](#what-gets-harvested)
- [Knowledge Inventory](#knowledge-inventory)
- [Related Publications](#related-publications)

---

## Quick Reference

| Command | Action |
|---------|--------|
| `harvest <project>` | Pull knowledge from a satellite into `minds/` |
| `harvest --list` | List all harvested projects with version + drift |
| `harvest --procedure` | Guided promotion walkthrough |
| `harvest --healthcheck` | Full network sweep + auto-promote queue |
| `harvest --review <N>` | Mark insight #N as human-reviewed |
| `harvest --stage <N> <type>` | Stage insight for integration |
| `harvest --promote <N>` | Promote to core knowledge now |
| `harvest --auto <N>` | Queue for auto-promote on next healthcheck |
| `harvest --fix <project>` | Update satellite CLAUDE.md to latest version |
| `harvest <cmd> ?` | Contextual help for any subcommand |

---

## Core Concept

Knowledge has **bidirectional flow**:

- **Push (outbound)**: On `wakeup`, satellites read the master mind and inherit methodology. This is the "sunglasses moment."
- **Harvest (inbound)**: The master crawls satellite branches, extracts evolved knowledge, and stages it in `minds/` for review and promotion.

```
Satellite project → harvest → minds/<project>.md → review → promote → core knowledge
```

**Access scope**: Harvest only operates on repositories that the user owns and that Claude Code has been granted access to via its GitHub application configuration. No external or third-party repos are ever crawled. This is a deliberate security and privacy boundary.

All satellite access uses public HTTPS: `https://github.com/packetqc/<project>`. Always targets the `main` branch.

### Fork & Clone Safety

If you fork or clone this repository, the harvest protocol is **owner-scoped** and environmentally isolated:

- **No credentials or tokens** are stored — harvest uses public HTTPS URLs only
- **Satellite URLs** reference the original owner's repos — a forker's harvest reads public data (read-only) or fails gracefully (403/404 → marked `unreachable`)
- **Push access** is proxy-scoped — `harvest --fix` can only push to the current session's assigned branch in the current repo
- **`minds/` data** is specific to the original owner's satellites — starts fresh when you run your own harvests

To use harvest for your own projects: replace `packetqc` with your GitHub username in CLAUDE.md. The protocol adapts — your satellites, your namespace, your data.

---

## Harvesting a Satellite

```
harvest STM32N6570-DK_SQLITE
```

**What happens:**
1. Clone/fetch the satellite via `https://github.com/packetqc/STM32N6570-DK_SQLITE`
2. Read from `main` branch
3. Check cursors — compare branch HEAD against last-harvested SHA
4. Scan: `CLAUDE.md`, `notes/`, `publications/`, `remember harvest:` flags
5. Extract: methodology, patterns, pitfalls, Claude instructions
6. Check version: `<!-- knowledge-version: vN -->` tag in satellite CLAUDE.md
7. Write to `minds/STM32N6570-DK_SQLITE.md` with updated cursors
8. Update dashboard in `publications/distributed-knowledge-dashboard/`
9. Report: what was harvested, version drift, promotion candidates

**Incremental**: Each harvest stores a cursor (commit SHA + date). Next harvest only scans new commits after the cursor. First harvest scans everything.

---

## The Promotion Pipeline

Insights advance through 4 stages:

```
harvested → 🔍 review → 📦 stage → ✅ promote (or 🔄 auto)
```

### Step 1: Harvest

```
harvest STM32N6570-DK_SQLITE
```

New insights enter the pipeline as "harvested". They appear in the Acquired Knowledge section of the dashboard.

### Step 2: Review

```
harvest --review 1
```

Read the insight, validate it makes sense, check it's not a duplicate. Marks as human-reviewed. **This is your quality gate.**

### Step 3: Stage

```
harvest --stage 1 lesson
```

Assign a target type — where this insight belongs in core:

| Type | Target | For what |
|------|--------|----------|
| `lesson` | `lessons/pitfalls.md` | Things that broke |
| `pattern` | `patterns/<topic>.md` | Proven approaches |
| `methodology` | `methodology/` | Workflow improvements |
| `docs` | Publications or docs pages | Documentation |

### Step 4: Promote or Auto-Promote

**Immediate promotion:**
```
harvest --promote 1
```
Writes the insight to its target file in core knowledge right now.

**Queued auto-promotion:**
```
harvest --auto 1
```
Queued for promotion on the next `harvest --healthcheck` run.

---

## Network Healthcheck

```
harvest --healthcheck
```

Full sweep of all known satellites in one pass:

1. Crawl each satellite (incremental — only new commits since last cursor)
2. Update severity icons in the dashboard
3. Process the auto-promote queue
4. Regenerate dashboard webcards if data changed
5. Commit all changes, push to task branch, create PR targeting `main`
6. Report: healthy/stale/unreachable counts, drift distribution, actions taken

**Severity icons in the dashboard:**

| <span id="severity-icons">Icon</span> | Severity | Used for |
|------|----------|----------|
| 🟢 | Current / Healthy | Drift 0, Bootstrap active, Sessions 1+, Live deployed |
| 🟡 | Minor drift | Drift 1-3, Health stale |
| 🟠 | Moderate drift | Drift 4-7 |
| 🔴 | Critical / Missing | Drift 8+, Bootstrap missing, Health unreachable |
| ⚪ | Inactive | Sessions 0, Health pending |

---

## Satellite Remediation

```
harvest --fix STM32N6570-DK_SQLITE
```

When a satellite is behind the core version, `--fix` prepares the remediation:

1. Reads the satellite's current `<!-- knowledge-version: vN -->` tag
2. Generates an updated CLAUDE.md bootstrap section referencing the latest core version
3. Records the remediation in `minds/` on the task branch
4. The fix reaches `main` when the user approves the PR
5. The satellite self-heals on next `wakeup` by reading the updated core

**Why not direct push?** Claude Code's push access is proxy-scoped: per-repo and per-branch. A session in the core repo cannot push to a satellite's branches. The fix is **pull-based** — satellite self-heals by reading core on next wakeup.

---

## Contextual Help

Append `?` to any subcommand:

```
harvest ?                    # All harvest commands with descriptions
harvest --review ?           # Review usage, current reviewable insights, examples
harvest --stage ?            # Stage usage, valid types, currently staged
harvest --promote ?          # Promote usage, what gets written where
harvest --auto ?             # Auto-promote usage, current queue
harvest --fix ?              # Fix usage, current satellite drift
```

---

## Error Handling

Missing or incorrect arguments show contextual help — never fail silently:

```
harvest --stage 3              # Missing type → "Usage: harvest --stage <N> <type>"
harvest --review               # Missing N → "Usage: harvest --review <N>"
harvest --fix                  # Missing project → "Usage: harvest --fix <project>"
harvest --stage 3 foo          # Invalid type → "Unknown type 'foo'. Valid: lesson, pattern, methodology, docs"
```

Every error shows: (1) what's wrong, (2) correct usage, (3) current state context, (4) a working example.

---

## Common Workflows

### Daily check

```
harvest --list                 # See network state
harvest --healthcheck          # Full sweep if needed
```

### New satellite discovered something useful

```
harvest STM32N6570-DK_SQLITE   # Pull latest knowledge
harvest --review 1             # Validate the insight
harvest --stage 1 lesson       # Stage as a lesson
harvest --promote 1            # Write to core
```

### Satellite is behind

```
harvest --list                 # Check drift
harvest --fix STM32N6570-DK_SQLITE  # Prepare remediation
# User approves PR → satellite reads updated core on next wakeup
```

### Guided workflow for newcomers

```
harvest --procedure            # Step-by-step walkthrough with current state
```

---

## What Gets Harvested

| Category | Examples |
|----------|----------|
| **Claude instructions** | Project-specific directives that may generalize |
| **Evolved patterns** | New patterns discovered during the project |
| **New pitfalls** | Things that broke, not yet in master `lessons/` |
| **Methodology progress** | Workflow improvements, new commands |
| **Publications** | Technical writeups in satellite `publications/` or `docs/` |
| **Harvest flags** | Notes marked with `remember harvest: <insight>` |

---

## Knowledge Inventory

Every harvest reports the satellite's knowledge status:

| Check | What it means |
|-------|---------------|
| CLAUDE.md references `packetqc/knowledge` | Knowledge is distributed — sunglasses active |
| `notes/` folder exists | Session persistence is active |
| `live/` folder synced | Live tooling is deployed |
| Own `patterns/` or `methodology/` | Project has evolved its own knowledge layer |
| `publications/` with content | Has publishable material |
| Repo accessible | Harvest can reach the satellite |

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | Knowledge | Parent — harvest is a core subsystem |
| 4 | Distributed Minds | Architecture — the system harvest operates within |
| 4a | Knowledge Dashboard | Output — harvest updates the dashboard |
| 3 | AI Session Persistence | Foundation — session notes are harvest's input data |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
