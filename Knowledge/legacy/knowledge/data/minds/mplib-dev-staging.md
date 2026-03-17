# MPLIB_DEV_STAGING_WITH_CLAUDE

## Harvest Metadata
| Field | Value |
|-------|-------|
| Repo | [packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE](https://github.com/packetqc/MPLIB_DEV_STAGING_WITH_CLAUDE) |
| Last harvest | 2026-02-22 |
| Branches scanned | main |

### Branch Cursors
| Branch | Last harvested SHA | Date |
|--------|-------------------|------|
| main | 5009c981d7a3cb0b86163ff5219161104074227b | 2026-02-21 |

---

## Knowledge Version
| Field | Value |
|-------|-------|
| Satellite version | v31 |
| Core version | v35 |
| Drift | 4 🟠 |
| Missing features | v32 recall + contextual help, v33 PAT access levels, v34 secure textarea delivery, v35 project entity model |
| Last remediated | 2026-02-21 (harvest --fix via API — critical-subset deployed, PR #13 merged) |

---

## Knowledge Status
| Check | Status | Detail |
|-------|--------|--------|
| Bootstrap | 🟢 **active** | CLAUDE.md v31 critical-subset (~240 lines) — upgraded from v22 via harvest --fix PR #13 |
| Session persistence | 🟢 **active** | notes/ with 5 session files |
| Live tooling | 🟢 **deployed** | live/ synced (stream_capture.py, dynamic/, static/) — beacon+scanner pending next wakeup |
| Own knowledge | 🟢 **rich** | Project-specific commands (vanilla), architecture, code conventions preserved |
| Publications | ⚪ **scaffold** | docs/ structure created, no publication content yet |
| Health | 🟢 **healthy** | Reachable via token-authenticated API (private repo) |

---

## Bootstrap Event — 2026-02-19

Task: "Set up Knowledge initial installation v22" — completed by a separate Claude Code session in the satellite repo.

Branch `claude/setup-knowledge-v22-kDN01`, commit `15c3eb9`:
- CLAUDE.md updated (95 insertions, 21 deletions):
  1. Knowledge Base section added — `<!-- knowledge-version: v22 -->` tag
  2. Wakeup updated to v22 protocol — Step 0 reads packetqc/knowledge first
  3. `flush` replaced with `save` — Semi-automatic protocol (PR-based delivery)
  4. Commands restructured to multipart help — Part 1 (knowledge) + Part 2 (project: `vanilla`)
  5. Branch Protocol section added — Documents proxy constraints (push limited to assigned task branch, 403 on main)
  6. Session lifecycle updated — `wakeup → work → save` cycle documented
- Created notes/session-2026-02-19.md (bootstrap session notes)

**PR status**: Not yet created — `gh` CLI was not authenticated in the bootstrap session. The user was informed and video-recorded the process. PR needs manual creation or next session in the satellite.

### Bootstrap Over-Sync Analysis

The bootstrap installed ~60% more content than needed. Items 3-6 duplicate core content that should be read dynamically on `wakeup`, not hardcoded in the satellite:

| # | Change | Verdict |
|---|--------|---------|
| 1 | Knowledge Base section (`<!-- knowledge-version: v22 -->`) | **KEEP** — minimal bootstrap pointer |
| 2 | Step 0 wakeup protocol | **KEEP** — brief reference |
| 3 | Full `save` protocol (semi-automatic, PR-based) | **OVER-SYNC** — defined in core |
| 4 | Part 1 knowledge commands in help table | **OVER-SYNC** — read from core on wakeup |
| 5 | Full Branch Protocol section | **OVER-SYNC** — universal, in core |
| 6 | Full Session lifecycle | **OVER-SYNC** — universal, in core |

**Remediation**: The next `wakeup` in the satellite should run `normalize` to trim the CLAUDE.md to thin-wrapper form (~30 lines vs ~120). This requires a second PR merge before the satellite is clean for `harvest --healthcheck`.

### Two-Merge Bootstrap Lifecycle

```
Stage 1: Bootstrap → PR → merge to main     ← install v22 pointer + initial sync
Stage 2: Wakeup + Normalize → PR → merge    ← trim bloat, apply thin-wrapper pattern
Stage 3: harvest --healthcheck               ← scan clean satellite from core
```

The first merge gets the sunglasses on. The second merge gets the satellite lean. Only after Stage 2 is the satellite properly shaped for harvest scanning.

---

## Project Overview

**MPLIB 2.0 development staging** — A collaborative development environment where MPLIB modules are updated and new features integrated with Claude's assistance. This is the active development fork of the MPLIB library, transitioning from MPLIB v1 to v2.

### Purpose
- **Module modernization** — Update existing MPLIB modules (singleton architecture, RTOS integration, GUI backend) for the v2.0 target
- **Feature integration** — Integrate new capabilities (PQC cryptography, enhanced storage pipeline, improved thread architecture)
- **AI-assisted staging** — Claude Code operates as a development partner, reading and understanding modules before modifying them, using printf diagnostics for runtime verification
- **Methodology evolution** — The collaborative development process itself generates insights about AI-assisted embedded development

### Relationship to Other Satellites
| Satellite | Relationship |
|-----------|-------------|
| [MPLIB](https://github.com/packetqc/MPLIB) | **Parent** — MPLIB_DEV_STAGING inherits the library architecture (multi-RTOS, singleton modules, static archive) |
| [STM32N6570-DK_SQLITE](https://github.com/packetqc/STM32N6570-DK_SQLITE) | **Sibling** — SQLite storage pipeline patterns feed back into MPLIB 2.0 storage module |
| [PQC](https://github.com/packetqc/PQC) | **Sibling** — PQC cryptography (ML-KEM, ML-DSA) integrating into MPLIB 2.0 security module |

### Inherited Architecture (from MPLIB)
- **Multi-RTOS abstraction** — FreeRTOS/ThreadX dual support with `#if defined(FREERTOS)` / `#elif defined(AZRTOS)` preprocessor guards
- **Library-as-static-archive** — Compiles to `libMPLIB_STM32_MCU.a`, linked by application frameworks
- **Thread/Singleton architecture** — 7 dedicated threads (default, GUI, Data, System, Display, Secure, SDCard, Network) with LED heartbeats
- **Dual cryptography** — ECC KEM (current) + ML-KEM (post-quantum) coexistence
- **Queue/Mutex communication** — Queues for event/message passing, mutexes for shared state
- **TouchGFX MVP pattern** — C entry → C++ RTOS → Model → Presenter → View

---

## Claude Instructions

CLAUDE.md exists (bootstrapped to v22). Key sections:
- Knowledge Base bootstrap referencing packetqc/knowledge with v22 tag
- Step 0 wakeup protocol — reads core knowledge first
- Semi-automatic save protocol — commit + push to task branch + PR to main
- Multipart help — Part 1 (knowledge) + Part 2 (project-specific: `vanilla` command)
- Branch protocol — documents proxy constraints

---

## Evolved Patterns

### AI-Assisted Module Staging — **PROMOTION CANDIDATE**
Development methodology where Claude Code reads and understands existing embedded modules before proposing modifications. Printf diagnostics validate changes at runtime. The staging environment allows safe experimentation without affecting the production library. This pattern — reading first, understanding fully, modifying incrementally — is the operational model for AI-assisted embedded development.

### `vanilla` Command — Module Generation
Project-specific command `vanilla <NAME> <LED>` generates singleton modules from template. Part 2 of multipart help. Demonstrates the command extensibility pattern where satellites add their own commands atop the knowledge base.

---

## New Pitfalls

### Bootstrap PR Delivery Requires Manual Step
The bootstrap session's `gh` CLI was not authenticated, so the PR for `claude/setup-knowledge-v22-kDN01 → main` was not created automatically. This is a known limitation of new satellite bootstraps — the first PR may need manual creation. Subsequent sessions with `gh` access resolve this naturally.

---

## Methodology Progress

- **Collaborative development with knowledge app** — The user ran Claude Code in the satellite while simultaneously running knowledge in the Claude app. This parallel approach — one instance staging, one instance monitoring the network — is a methodology pattern for bootstrap operations.
- **Video recording of bootstrap** — The user recorded the bootstrap process for verification and documentation. Visual confirmation of AI operations.
- **`flush` → `save` migration** — The satellite had an older command (`flush`) that was renamed to `save` per v17+ semi-automatic protocol. This confirms the update path works for existing projects.

---

## Publications Detected
| Title | Path (in satellite) | Status |
|-------|---------------------|--------|
| (none) | — | No publications/ folder — project in early staging phase |

---

## Promotion Candidates

| # | Insight | Target | Status |
|---|---------|--------|--------|
| 1 | **AI-assisted module staging methodology** — Read-first, understand-fully, modify-incrementally with printf diagnostics validation. Collaborative AI+human embedded development workflow. | methodology/ (new: ai-assisted-development.md) | Ready for review |
| 2 | **Parallel instance operations** — Running knowledge core + satellite development simultaneously across Claude Code instances. Network-aware development. | methodology/ | Ready for review |
| 3 | **Two-merge bootstrap lifecycle** — Bootstrap installs the pointer (merge 1), wakeup+normalize trims to thin-wrapper (merge 2), then satellite is clean for harvest. Over-sync during initial bootstrap is expected — normalization is the cure. | methodology/ | Ready for review |
| 4 | **Satellite thin-wrapper principle** — Satellite CLAUDE.md should be ~30 lines: bootstrap pointer + project overview + project-specific commands. Universal content (protocols, commands, patterns) is read from core on wakeup, never duplicated. | CLAUDE.md (bootstrap template) | Ready for review |
