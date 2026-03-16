---
layout: publication
title: "Harvest Protocol — Complete Documentation"
description: "Complete documentation for the harvest protocol: all commands with examples, promotion pipeline step-by-step, network healthcheck, satellite remediation, contextual help, error handling, common workflows, and knowledge inventory."
pub_id: "Publication #7 — Full"
version: "v1"
date: "2026-02-19"
permalink: /publications/harvest-protocol/full/
og_image: /assets/og/harvest-protocol-en-cayman.gif
keywords: "harvest, promotion, healthcheck, satellites, insights, version drift"
---

# Harvest Protocol — Complete Documentation
{: #pub-title}

**Contents**

| | |
|---|---|
| [Authors](#authors) | Publication authors |
| [Abstract](#abstract) | Practical guide to distributed knowledge collection |
| [Quick Reference](#quick-reference) | All harvest commands at a glance |
| [Core Concept](#core-concept) | Bidirectional knowledge flow and access scope |
| [Harvesting a Satellite](#harvesting-a-satellite) | 10-step protocol for pulling satellite knowledge |
| [The Promotion Pipeline](#the-promotion-pipeline) | Review, stage, promote, auto-promote workflow |
| [Network Healthcheck](#network-healthcheck) | Full network sweep with severity icons |
| [Satellite Remediation](#satellite-remediation) | Pull-based version drift fix |
| [Contextual Help](#contextual-help) | Appending `?` for inline documentation |
| [Error Handling](#error-handling) | Never-fail-silently error reporting |
| [Common Workflows](#common-workflows) | Daily check, new insight, guided procedures |
| [What Gets Harvested](#what-gets-harvested) | Categories of extracted knowledge |
| [Knowledge Inventory](#knowledge-inventory) | Satellite bootstrap status checks |
| [Related Publications](#related-publications) | Sibling and parent publications |

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer and programmer. Architect of the harvest protocol — the reverse-flow mechanism that pulls evolved knowledge from satellite projects back to the central master mind.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Executes harvest operations, crawls satellite repos, extracts insights, and manages the promotion pipeline.

---

## Abstract

Publication #4 (Distributed Minds) documents the **architecture** of bidirectional knowledge flow. This publication is the **practical guide** — how to use `harvest` commands day-to-day: pulling knowledge from satellites, reviewing and promoting insights, running network sweeps, and fixing version drift.

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

| Direction | Description |
|-----------|-------------|
| **Push (outbound)** | On `wakeup`, satellites read the master mind and inherit methodology. |
| **Harvest (inbound)** | The master crawls satellite branches, extracts evolved knowledge, and stages it in `minds/`. |

```
Satellite project → harvest → minds/<project>.md → review → promote → core knowledge
```

**Access scope**: Harvest only operates on repositories that the user owns and that Claude Code has been granted access to via its GitHub application configuration. No external or third-party repos are ever crawled. This is a deliberate security and privacy boundary.

All satellite access uses public HTTPS: `https://github.com/packetqc/<project>`. Always targets the `main` branch.

### Fork & Clone Safety

If you fork or clone this repository, the harvest protocol is **owner-scoped** and environmentally isolated:

| Concern | Protection |
|---------|------------|
| **No credentials or tokens** | Harvest uses public HTTPS URLs only — nothing stored |
| **Satellite URLs** | Reference the original owner's repos — a forker's harvest reads public data (read-only) or fails gracefully (403/404 → marked `unreachable`) |
| **Push access** | Proxy-scoped — `harvest --fix` can only push to the current session's assigned branch in the current repo |
| **`minds/` data** | Specific to the original owner's satellites — starts fresh when you run your own harvests |

To use harvest for your own projects: replace `packetqc` with your GitHub username in CLAUDE.md. The protocol adapts — your satellites, your namespace, your data.

---

## Harvesting a Satellite

```
harvest STM32N6570-DK_SQLITE
```

**Protocol (10 steps):**

| Step | Action |
|------|--------|
| 1. Enumerate branches | `git ls-remote https://github.com/packetqc/<project>` |
| 2. Check cursors | Compare each branch HEAD against last-harvested SHA in `minds/<project>.md` |
| 3. Scan new content | For changed branches: `CLAUDE.md`, `notes/`, `publications/`, `remember harvest:` flags |
| 4. Knowledge inventory | Does the satellite reference `packetqc/knowledge`? Has `notes/`? Has `live/`? |
| 5. Version check | Read `<!-- knowledge-version: vN -->` from satellite CLAUDE.md |
| 6. Extract | Pull methodology, patterns, pitfalls, Claude instructions, publication references |
| 7. Update | Write to `minds/<project-slug>.md` with updated branch cursors |
| 8. Report | What was harvested, what's new, version drift, promotion candidates |
| 9. Update dashboard | Refresh satellite table in `publications/distributed-knowledge-dashboard/v1/README.md` |
| 10. Regenerate webcards | If dashboard data changed: `python3 scripts/generate_og_gifs.py knowledge-dashboard` |

**Incremental**: Each harvest stores a cursor (commit SHA + date). Next harvest only scans new commits.

---

## The Promotion Pipeline

Insights advance through 4 stages:

| Stage | <span id="promotion-icons">Icon</span> | Command | Effect |
|-------|------|---------|--------|
| Review | 🔍 | `harvest --review N` | Human has read and validated |
| Stage | 📦 | `harvest --stage N <type>` | Staged for integration |
| Promote | ✅ | `harvest --promote N` | Written to core now |
| Auto | 🔄 | `harvest --auto N` | Queued for next healthcheck |

**Step-by-step:**

| Step | Command | Action |
|------|---------|--------|
| 1 | `harvest <project>` | Insights enter as "harvested" |
| 2 | `harvest --review 1` | Read it, validate it's correct, mark as reviewed |
| 3 | `harvest --stage 1 lesson` | Assign target type (see table below) |
| 4 | `harvest --promote 1` | Writes to the target file immediately. Or `harvest --auto 1` to queue |

**Target types:**

| Type | Target file | For what |
|------|------------|----------|
| `lesson` | `lessons/pitfalls.md` | Things that broke |
| `pattern` | `patterns/<topic>.md` | Proven approaches |
| `methodology` | `methodology/` | Workflow improvements |
| `evolution` | CLAUDE.md Knowledge Evolution table | Architectural discoveries about the system itself |
| `docs` | Publications or docs pages | Documentation |

**Guided walkthrough**: `harvest --procedure` shows the full pipeline with current state — what's reviewable, what's staged, what's promoted.

---

## Network Healthcheck

```
harvest --healthcheck
```

Full sweep of all known satellites:

| Step | Action |
|------|--------|
| 1 | Crawl each satellite (incremental — only new commits since last cursor) |
| 2 | Update severity icons in the dashboard |
| 3 | Process auto-promote queue |
| 4 | Regenerate dashboard webcards if data changed |
| 5 | Commit, push to task branch, create PR targeting the default branch |
| 6 | Report: healthy/stale/unreachable counts, drift distribution, actions taken |

**Severity icons:**

| <span id="severity-icons">Icon</span> | Severity | Used for |
|------|----------|----------|
| 🟢 | Current / Healthy | Drift 0, Bootstrap active, Sessions 1+ |
| 🟡 | Minor drift | Drift 1-3, Health stale |
| 🟠 | Moderate drift | Drift 4-7 |
| 🔴 | Critical / Missing | Drift 8+, Bootstrap missing |
| ⚪ | Inactive | Sessions 0, Health pending |

**When to run**: On-demand. Auto-suggested on `wakeup` when the last healthcheck was > 24h ago.

---

## Satellite Remediation

```
harvest --fix STM32N6570-DK_SQLITE
```

| Step | Action |
|------|--------|
| 1 | Read satellite's `<!-- knowledge-version: vN -->` tag |
| 2 | Generate updated CLAUDE.md bootstrap section |
| 3 | Record remediation in `minds/` on the task branch |
| 4 | Fix reaches `main` when user approves the PR |
| 5 | Satellite self-heals on next `wakeup` by reading updated core |

**Why pull-based?** Claude Code's push access is proxy-scoped: per-repo and per-branch. Cannot push to satellite repos. The satellite reads the updated core on its next wakeup — self-healing.

---

## Contextual Help

Append `?` to any subcommand:

```
harvest ?                    # All commands with descriptions
harvest --review ?           # Current reviewable insights, usage, examples
harvest --stage ?            # Valid types, currently staged insights
harvest --promote ?          # What gets written where, examples
harvest --auto ?             # Current queue, next healthcheck schedule
harvest --fix ?              # Current satellite drift, examples
```

---

## Error Handling

Never fail silently. Every incomplete command shows:

| Item | Description |
|------|-------------|
| What's wrong | The specific error or missing parameter |
| Correct usage | The command syntax with required arguments |
| Current state context | Available insights, satellites, etc. |
| Working example | A copy-paste ready command |

```
harvest --stage 3              # → "Missing type. Usage: harvest --stage <N> <type>"
harvest --review               # → "Missing N. Usage: harvest --review <N>"
harvest --fix                  # → "Missing project. Usage: harvest --fix <project>"
harvest --stage 3 foo          # → "Unknown type 'foo'. Valid: lesson, pattern, methodology, evolution, docs"
```

---

## Common Workflows

### Daily check
```
harvest --list                 # See network state at a glance
harvest --healthcheck          # Full sweep if needed
```

### New insight discovered
```
harvest STM32N6570-DK_SQLITE   # Pull latest
harvest --review 1             # Validate
harvest --stage 1 lesson       # Assign type
harvest --promote 1            # Write to core
```

### Satellite behind on version
```
harvest --list                 # Check drift
harvest --fix STM32N6570-DK_SQLITE  # Prepare remediation
# User approves PR → satellite reads updated core on next wakeup
```

### Guided newcomer workflow
```
harvest --procedure            # Full walkthrough with current state
```

---

## What Gets Harvested

| Category | Examples |
|----------|----------|
| **Claude instructions** | Project-specific directives that may generalize |
| **Evolved patterns** | New patterns discovered during the project |
| **New pitfalls** | Things that broke, not yet in master `lessons/` |
| **Methodology progress** | Workflow improvements, new commands |
| **Publications** | Technical writeups in satellite repos |
| **Harvest flags** | Notes marked with `remember harvest: <insight>` |

---

## Knowledge Inventory

Every harvest reports the satellite's knowledge status:

| Check | What it means |
|-------|---------------|
| CLAUDE.md references `packetqc/knowledge` | Sunglasses active |
| `notes/` exists | Session persistence active |
| `live/` synced | Live tooling deployed |
| Own `patterns/` or `methodology/` | Evolved own knowledge layer |
| `publications/` with content | Has publishable material |
| Repo accessible | Harvest can reach the satellite |

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|-------------|
| 0 | [Knowledge]({{ '/publications/knowledge-system/' | relative_url }}) | Parent — harvest is a core subsystem |
| 4 | [Distributed Minds]({{ '/publications/distributed-minds/' | relative_url }}) | Architecture — the system harvest operates within |
| 4a | [Knowledge Dashboard]({{ '/publications/distributed-knowledge-dashboard/' | relative_url }}) | Output — harvest updates the dashboard |
| 3 | [AI Session Persistence]({{ '/publications/ai-session-persistence/' | relative_url }}) | Foundation — session notes are harvest's input data |

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
