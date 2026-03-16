# NEWS — Knowledge System Changelog

All changes to the knowledge system, organized in 4 views.

**Default**: [By Project](#by-project) | [By Quality](#by-quality) | [By Structure](#by-structure) | [By Type](#by-type)

Current version: **v59** | Last updated: 2026-03-16

---

## By Project

### P0 — Knowledge System (core)

| Date | Change | Version |
|------|--------|---------|
| 2026-03-16 | **Root essential files restored** — LINKS.md, NEWS.md, PLAN.md, STORIES.md, VERSION.md updated for K_DOCS production context. Social sharing URLs migrated to `packetqc.github.io/knowledge`. Legacy sections preserved for gap analysis. Navigator methodologies widget added (16 files across 5 modules). | v59.1 |
| 2026-03-15 | **Story #25 — Live Mindmap Memory** + **Story #26 — One Viewer to Rule Them All** — two new success stories documenting MindElixir knowledge graph and single-file viewer engine | v59 |
| 2026-03-14 | **K2.0 publication text review complete** — 13 publications deep-reviewed for K2.0 terminology (wakeup→session start, harvest→K_GITHUB sync, CLAUDE.md→mind_memory.md, notes/→sessions/). 15 commits across all EN/FR summary+full pages | v59 |
| 2026-03-10 | **Story #24 — The Toggle** — repo restructure migration: 852 files moved, 158 paths remapped, zero breakage | v59 |
| 2026-03-08 | **Story #23 — Knowledge v2.0 Platform** — from questionnaire to living engineering platform | v59 |
| 2026-03-07 | **Story #22 — Visual Documentation Engine** — from video to evidence in seconds, automated extraction with computer vision | v59 |
| 2026-03-06 | **Integrity state machine (v59)** — 29-checkpoint instrument panel enforcing agent identity | v59 |
| 2026-03-05 | **Agent identity (v58)** — the engineer identity model. STAGE:/STEP: label sync + dot-notation + I3 (v57) | v57–v58 |
| 2026-03-04 | **Gold release — Session Viewer v2 + Time Compilation + Memory commands** — Massive Session Viewer improvements: (1) **Session-scoped time compilation** — activities filtered by session date, calendar span recomputed from scoped data. (2) **Tree-based time table** — 3-level hierarchy (issue→comment→PR) with expand/collapse + localStorage persistence. (3) **5 interactive pie charts** — time (active/inactive), scope (child sessions/related issues), metrics (deliverables), lines changed, impact. (4) **Inactive time note** — bilingual explanation under every time table. (5) **CSS/JS extraction** — shared external files for consistent styling. (6) **Native Python recover/recall commands** — `scripts/recover.py` and `scripts/recall.py` with backup-* branch support. (7) **PreToolUse enforcement (v56)** — hook architecture that blocks edits until protocol gates pass. (8) **G7 enforcement** — auto-post all exchanges to session issue. (9) **Multi-issue session notes** — per-issue metrics and time compilation. Issues #675–#722 | v56 |
| 2026-03-03 | **Session notes → issue + CHANGELOG.md (v55)** — Two-part protocol update: (1) session notes posted as issue comment at save time — all user/Claude exchanges in the issue, post-save closing report, post-close final comment as audit trail endpoint. (2) New CHANGELOG.md concept separate from NEWS.md — per-issue/PR chronological audit trail with bilingual web pages (EN/FR). CHANGELOG added to essential files lists across documentation-generation.md, normalize, CLAUDE.md. Issue #610 | v55 |
| 2026-03-02 | **Publication #22 — Visual Documentation** — New `visual` command for automated evidence extraction from video recordings. OpenCV + Pillow + NumPy (no external tools). Two modes: timestamp (seconds/times/dates) and detection (scene change, text density, edge density, structured content). Output: annotated frames, perceptual hash dedup, contact sheets, markdown reports. New **Visuals** command category regroups `visual`, `deep`, `analyze`. Issue #556 | v54 |
| 2026-03-02 | **Interface webcards for social sharing** — animated OG GIFs for interfaces hub, I1 Session Review, I2 Main Navigator (12 files: 3 cards × 2 langs × 2 themes). Social-media-only — served via OG meta tags for LinkedIn/Twitter but not displayed on the page. Layout updated to enable og:image for interfaces. Issue #578 | v54 |
| 2026-03-02 | **#0a Bootstrap Optimization (Annex)** — CLAUDE.md condensation strategy documented: 3872 → 714 lines (81% reduction), full section map, token budget impact (+38K tokens freed), 7 best practices. Bilingual EN/FR pages anchored from #0 source, summary, full docs, and CLAUDE.md. PR #575 | v54 |
| 2026-03-01 | **Main Navigator — arrow alignment fix + interface back-link** — right divider arrows now vertically centered (changed `visibility:hidden` to `display:none`). Layout back-link routes interface pages to `/interfaces/` hub instead of `/publications/`. Both layouts (publication.html, default.html) updated. Issue #521 | v54 |
| 2026-03-01 | **Iframe embed mode — export toolbar hidden** — pages loaded inside iframes (`window.self !== window.top`) hide the export toolbar via `body.in-iframe .pub-export-toolbar { display: none }`. Prevents double-toolbar when publications are viewed inside the Main Navigator. PR #544. Issue #521 | v54 |
| 2026-03-01 | **Universal `{: #pub-title}` anchors** — all 100 publication pages (EN/FR summary + full) now have `{: #pub-title}` kramdown attribute on their `<h1>` title. Enables iframe embed mode to scroll past pre-title chrome. PR #543. Issue #521 | v54 |
| 2026-03-01 | **Iframe embed mode for publications** — `window.self !== window.top` detection adds `body.in-iframe` class, hiding pre-title chrome (back-link, topbar, version banner, language bar, dev banner, webcard header) when viewed inside the Main Navigator center panel. PR #543. Issue #521 | v54 |
| 2026-03-01 | **Navigation state persistence** — Main Navigator preserves right iframe URL, active link highlight, and sub-details open/close state across page refreshes via `sessionStorage`. PR #542. Issue #521 | v54 |
| 2026-03-01 | **Main Navigator (I2) — left panel command links to full pages** — command links in the navigator open full pages in the browser (not in iframe), chrome collapsed by default on load. PR #525–#541. Issue #521 | v54 |
| 2026-03-01 | **Main Navigator (I2) — Session Review in center panel** — clicking Session Review in the left navigation panel now loads it in the center iframe instead of navigating away. Both EN/FR updated. Issue #521 | v54 |
| 2026-03-01 | **Session Review (I1) — engineering taxonomy badges** — new green request_type badge (11 types: fix, feature, investigation, enhancement, testing, validation, documentation, deployment, conception, review, chore) and purple engineering_stage badge (10 stages: analysis through improvement) displayed in session header, dropdown, metrics footer, and time table. Bilingual labels (EN/FR), dark mode support, graceful degradation for legacy sessions. Issue #521 | v54 |
| 2026-03-01 | **Engineering taxonomy — 11 request types + 10 engineering stages** — aligned with SDLC, Agile, DevOps, ITIL, GitHub Flow, ISO 12207. New labels deployed to GitHub repos. Session requalification: 33+ supported sessions re-typed from old 5-type to new 11-type taxonomy via `generate_sessions.py`. Documented in `methodology/engineering-taxonomy.md`. Issue #521 | v54 |
| 2026-03-01 | **Strategic Remote Check (v54)** — Core Methodology #6: `git fetch origin <default>` + `git diff` before modifying files. Wired into work cycle, refresh, and save protocols. | v54 |
| 2026-03-01 | **Autonomous Execution Principle (v53) + Add-on detection protocol** — two-gate flow (title + plan approval) then autonomous execution. Add-on detection: user comments classified as supplements vs new requests. | v53 |
| 2026-03-01 | **Four-channel persistence model + session runtime cache** — session cache (`notes/session-runtime-<suffix>.json`) becomes the fourth persistence channel alongside Git, Notes, and GitHub Issues. 18 typed session_data keys with dedicated helper functions in `session_agent.py`. Cache-first recovery protocol after compaction. Multi-session naming convention prevents conflicts. Updated across [#8 Session Management](https://packetqc.github.io/knowledge/publications/session-management/), [#23 Agent Ticket Sync](https://packetqc.github.io/knowledge/publications/agent-ticket-sync/), methodology files, and all EN/FR web pages. PRs #522–#524, issue #521 | — |
| 2026-02-26 | **Publication #19 — Interactive Work Sessions** — resilient multi-delivery sessions: 5 types (diagnostic, documentation, conception, design, feature dev), 3-channel persistence, progressive commits, per-type methodology files. Closes #355 | — |
| 2026-02-26 | **Publication #18 — Documentation Generation Methodology** — meta-methodology codifying documentation standards, mind map conventions, three-tier structure, universal inheritance of essential files, 13 core qualities alignment. Closes #355 | — |
| 2026-02-26 | **Publication #17 — Web Production Pipeline** — Jekyll processing chain, three-tier structure, kramdown gotchas, front matter contract. Closes #348 | — |
| 2026-02-26 | **`methodology/documentation-generation.md`** — formal meta-methodology: every methodology inherits NEWS/PLAN/LINKS/CLAUDE.md update obligation | — |
| 2026-02-26 | **Publication #14 — Architecture Analysis** — knowledge layers, component architecture, 13 qualities, distributed topology, security model. Closes #316 | — |
| 2026-02-26 | **Publication #15 — Architecture Diagrams** — 11 Mermaid diagrams: system overview, session lifecycle, distributed flow, security boundaries. Closes #317 | — |
| 2026-02-26 | **Success Story #16 — Rencontre de travail productive** — productive architecture documentation session | — |
| 2026-02-24 | **Live board widgets on plan pages** — per-section filtering (ongoing/fixes/planned/forecast/recalls/done), dropdown status filters, Mermaid lifecycle diagram, Completed section | — |
| 2026-02-24 | **Success Story #12 — Human Person Machine Bridge** — Knowledge as Jira+Confluence with zero paid tools | — |
| 2026-02-24 | **Board sync pipeline** — `sync_roadmap.py` with section classification + labels extraction | — |
| 2026-02-23 | **Compliancy security check completed** — token zero-display verified, compliance report Phase 1+3 updated to ✅ Applied | v46 |
| 2026-02-23 | Token zero-display — environment-only delivery + GraphQL in `gh_helper.py` | v46 |
| 2026-02-23 | Token display fix — AskUserQuestion "Other" field is NOT invisible (v34 corrected) | v45 |
| 2026-02-23 | Interactive Input Convention + Tool Call Discipline — API 400 prevention | v44 |
| 2026-02-23 | Wakeup deduplication — root cause of API 400 crashes found and fixed | v43 |
| 2026-02-23 | `gh_helper.py` as sole API method + non-blocking PR creation | v42 |
| 2026-02-23 | GitHub Project repo linking + classic PAT only (fine-grained discarded) | v41 |
| 2026-02-22 | Proxy deep mapping v2 — `curl` blocked, `urllib` bypasses + 7 Project boards | v40 |
| 2026-02-22 | Evolution relay — satellites propose core evolution entries | v39 |
| 2026-02-22 | Self-heal PR merge — same-session command activation (step 0.56) | v38 |
| 2026-02-22 | NEWS.md central changelog with 4 categorization views | v38 |
| 2026-02-22 | 6 bilingual web pages: news, plan, links (EN/FR) | v38 |
| 2026-02-22 | Beacon auto-start disabled — manual only | v38 |
| 2026-02-22 | Self-healing satellite CLAUDE.md — automatic drift remediation | v37 |
| 2026-02-22 | Fix hardcoded branch refs — dynamic default branch detection everywhere | v37 |
| 2026-02-22 | Full-read instruction for core CLAUDE.md in wakeup step 0 | v37 |
| 2026-02-22 | Canonical commands template (`methodology/satellite-commands.md`) | v37 |
| 2026-02-22 | GitHub helper (`scripts/gh_helper.py`) — portable PR management | v36 |
| 2026-02-22 | Publication #12 — Project Management (3-tier bilingual) | v35 |
| 2026-02-22 | Project hub pages EN/FR (`docs/projects/`) | v35 |
| 2026-02-22 | Project as first-class entity — hierarchical indexing P#/S#/D# | v35 |
| 2026-02-22 | Webcard OG GIFs for #12 (4 files) | — |
| 2026-02-22 | What's New / Nouveautés sections on central documents | — |
| 2026-02-22 | LINKS.md — 12 webcards moved from Missing to Deployed | — |
| 2026-02-21 | ~~Secure textarea token delivery — single invisible path~~ (**corrected v45**: textarea IS visible) | v34 |
| 2026-02-21 | PAT Access Levels — 4-tier configuration model | v33 |
| 2026-02-21 | `recall` command + universal contextual help with publication links | v32 |
| 2026-02-21 | Critical-subset satellite CLAUDE.md — behavioral DNA survives compaction | v31 |
| 2026-02-21 | Safe elevation protocol — API crash mitigation | v30 |
| 2026-02-21 | Checkpoint/resume — crash recovery for interrupted sessions | v29 |
| 2026-02-21 | Proxy architecture deep mapping + token-mediated API bypass | v28 |
| 2026-02-21 | Ephemeral token protocol — private repo access | v27 |
| 2026-02-20 | Scoped project notes + 4-theme accessibility | v26 |
| 2026-02-20 | Core Qualities + iterative staging installation | v25 |
| 2026-02-20 | `refresh` command + dashboard field rename | v24 |
| 2026-02-20 | Live knowledge network + bootstrap scaffold | v23 |
| 2026-02-19 | Dual-theme webcards: Cayman (light) + Midnight (dark) | v22 |
| 2026-02-19 | Access scope — user-owned repos only | v21 |
| 2026-02-19 | Semi-automatic delivery documentation + admin routine | v20 |
| 2026-02-19 | Todo list must mirror full save protocol | v19 |
| 2026-02-19 | `main` replaces `claude/knowledge` as convergence branch | v18 |
| 2026-02-19 | Proxy reality — semi-automatic protocol | v17 |
| 2026-02-19 | Save merge protocol + cross-repo push discovery | v16 |
| 2026-02-19 | End-to-end protocol validation | v15 |
| 2026-02-19 | `claude/knowledge` replaces `knowledge` | v14 |
| 2026-02-19 | Public HTTPS repo access + autonomous branch creation | v13 |
| 2026-02-19 | Knowledge branch protocol | v12 |
| 2026-02-18 | Interactive promotion workflow + severity icons + healthcheck | v11 |
| 2026-02-18 | Knowledge versioning and drift remediation | v10 |
| 2026-02-18 | Distributed minds — bidirectional knowledge flow | v9 |
| 2026-02-17 | Profile hub architecture | v8 |
| 2026-02-17 | Normalize command | v7 |
| 2026-02-17 | Chicken-and-egg bootstrap | v6 |
| 2026-02-17 | Step 0: sunglasses first | v5 |
| 2026-02-17 | Multipart help architecture | v4 |
| 2026-02-17 | Knowledge repo as portable bootstrap | v3 |
| 2026-02-16 | Free Guy analogy | v2 |
| 2026-02-16 | Session persistence methodology | v1 |

### P1 — MPLIB

| Date | Change | Version |
|------|--------|---------|
| 2026-02-22 | MPLIB decoupled from core — reclassified as child project P1 | v35 |
| 2026-02-22 | Publication #1 carries `P0/#1 →P1` cross-reference | v35 |
| 2026-02-19 | Semi-automatic delivery admin routine documented | v20 |

### P2 — STM32 PoC

| Date | Change | Version |
|------|--------|---------|
| 2026-02-22 | Registered as child project P2 in core registry | v35 |
| 2026-02-18 | Harvest insights: page cache sizing, printf latency | v9 |

### P3 — Knowledge Live

| Date | Change | Version |
|------|--------|---------|
| 2026-02-22 | CLAUDE.md updated to v37 — full-read instruction added | v37 |
| 2026-02-22 | CLAUDE.md updated to v36 — full 7-group commands | v36 |
| 2026-02-22 | Registered as child project P3 in core registry | v35 |
| 2026-02-20 | Knowledge beacon + scanner created (port 21337) | v23 |
| 2026-02-20 | Bootstrap scaffold protocol established | v23 |

### P4 — MPLIB Dev Staging

| Date | Change | Version |
|------|--------|---------|
| 2026-02-22 | Registered as child project P4 (child of P1) | v35 |
| 2026-02-20 | Iterative staging protocol validated (v25 road test) | v25 |

### P5 — PQC

| Date | Change | Version |
|------|--------|---------|
| 2026-02-22 | Registered as pre-bootstrap project P5 | v35 |
| 2026-02-21 | PQC envelope module (`scripts/pqc_envelope.py`) | v27 |

### P6 — Export Documentation

| Date | Change | Version |
|------|--------|---------|
| 2026-02-25 | **DOCX export: OOXML ZIP from scratch via altChunk** — removes html-docx-js, builds all ZIP parts natively, fixes Word+LibreOffice corruption (PR #304, closes #301 Fix 8) | — |
| 2026-02-25 | **DOCX export: running header/footer via JSZip** — native OOXML section properties, page numbering, 3-zone layout (PRs #302–#303) | — |
| 2026-02-25 | **DOCX export: 6 bug fixes** — MSO display:none, cover page double-clone, h2 page breaks, pie chart selector, Mermaid render guard, Stories #6/#7 (PR #291) | — |
| 2026-02-25 | **PDF export: single full-width header liner** — @top-left width:100%, zeroed center/right boxes, Chrome double-liner fix (knowledge-live PRs #52–#59) | — |
| 2026-02-25 | **Language bar redesign** — auto-generated from permalink via Liquid, above pub-topbar, hidden in print (knowledge-live PR #49) | — |
| 2026-02-25 | **3 convention layouts formalized** — publication.html (full export stack), default.html (no export), three-zone @page model | — |
| 2026-02-25 | **publication.html baseline synced** — 4-theme CSS, cross-refs widget, board widget, export toolbar promoted from knowledge-live to core | — |
| 2026-02-24 | **DOCX export: html-docx-js OOXML** — emoji alignment, borderless inner tables, visual fidelity (PRs #295–#300) | — |
| 2026-02-24 | **DOCX export: complete rewrite with 8 fixes** — MSO 3-zone page layout, cover page, section properties (PRs #288–#290) | — |
| 2026-02-24 | **PDF export: header/footer/table/Mermaid overhaul** — Knowledge repo link in footer, clickable links, filename sanitization (knowledge-live PRs #43–#48) | — |
| 2026-02-24 | T1 created — Universal layout pagination for exportation and web pages | — |
| 2026-02-23 | Registered as hosted project P6 (in P3 knowledge-live) | v44 |

### P8 — Documentation System

| Date | Change | Version |
|------|--------|---------|
| 2026-02-25 | **3 convention layouts documented** — publication.html, default.html, three-zone @page model scope boundaries formalized | — |
| 2026-02-25 | **Export Documentation QA complete** — 19 PRs on knowledge-live (dev) + 18 PRs on knowledge (prod), DOCX+PDF pipelines production-ready | — |
| 2026-02-25 | **Dev→Prod promotion cycle** — knowledge-live layouts/features promoted to knowledge core via harvest issues | — |
| 2026-02-24 | Project registered as P8 — core-level documentation governance (from harvest, issue #201) | v47 |

---

## By Quality

### Self-Sufficient

*The system sustains itself. No external services, no databases, no cloud.*

| Date | Change | Version |
|------|--------|---------|
| 2026-02-24 | Live board widgets — zero paid tools, replaces Jira board views + Confluence roadmaps | — |
| 2026-02-23 | `gh_helper.py` as sole API method — `curl` blocked, `urllib` only path | v42 |
| 2026-02-22 | GitHub helper — portable PR management without `gh` CLI | v36 |
| 2026-02-17 | Knowledge repo as portable bootstrap | v3 |
| 2026-02-16 | Session persistence methodology — plain Markdown in Git | v1 |

### Autonomous

*Self-propagating, self-healing, self-documenting.*

| Date | Change | Version |
|------|--------|---------|
| 2026-02-23 | Wakeup deduplication — prevents double execution on session start | v43 |
| 2026-02-23 | Full autonomous override — elevated sessions never pause for PR ops | v43 |
| 2026-02-22 | Self-heal PR merge — same-session command activation | v38 |
| 2026-02-22 | Self-healing satellite CLAUDE.md — automatic drift remediation | v37 |
| 2026-02-22 | Canonical commands template for satellite injection | v37 |
| 2026-02-20 | Bootstrap scaffold — non-destructive auto-creation | v23 |
| 2026-02-19 | `claude/knowledge` autonomous branch creation | v14 |
| 2026-02-19 | Public HTTPS access + autonomous branch creation | v13 |
| 2026-02-19 | Knowledge branch protocol — autonomous push | v12 |
| 2026-02-19 | End-to-end protocol validation | v15 |
| 2026-02-17 | Step 0: sunglasses first — self-propagating awareness | v5 |
| 2026-02-17 | Chicken-and-egg bootstrap — first manual, then automatic | v6 |

### Concordant

*Structural integrity actively enforced.*

| Date | Change | Version |
|------|--------|---------|
| 2026-02-25 | **3 convention layouts** — publication.html / default.html / three-zone @page scope boundaries enforced | — |
| 2026-02-25 | Export documentation QA — 37 PRs across 2 repos, DOCX+PDF concordance verified | — |
| 2026-02-24 | Per-section board filtering — TAG: prefix → section mapping, single board file → multiple views | — |
| 2026-02-23 | Tool Call Discipline — prevent duplicate tool_use ID collisions | v44 |
| 2026-02-23 | GitHub Project boards linked to repositories (`linkProjectV2ToRepository`) | v41 |
| 2026-02-22 | Fix hardcoded branch refs — dynamic detection everywhere | v37 |
| 2026-02-19 | Todo list must mirror full save protocol | v19 |
| 2026-02-17 | Normalize command — EN/FR mirrors, front matter, links | v7 |

### Concise

*Critical-subset, not copies. Maximum signal, minimum noise.*

| Date | Change | Version |
|------|--------|---------|
| 2026-02-21 | Critical-subset satellite CLAUDE.md — behavioral DNA | v31 |
| 2026-02-19 | `main` replaces `claude/knowledge` — maximum simplification | v18 |
| 2026-02-17 | Multipart help architecture — concatenate, never duplicate | v4 |

### Interactive

*Operable, not just readable.*

| Date | Change | Version |
|------|--------|---------|
| 2026-02-24 | Board widgets with dropdown filters, sortable columns, per-section views | — |
| 2026-02-24 | Mermaid compliance lifecycle diagram on plan pages (EN/FR) | — |
| 2026-02-23 | Interactive Input Convention — gather ALL inputs upfront via single popup | v44 |
| 2026-02-22 | Self-heal PR merge — guided `⏸` pause for same-session activation | v38 |
| 2026-02-22 | What's New / Nouveautés sections on central documents | — |
| 2026-02-20 | Scoped project notes + 4-theme accessibility | v26 |
| 2026-02-19 | Dual-theme webcards: Cayman + Midnight | v22 |
| 2026-02-18 | Interactive promotion workflow + severity icons + healthcheck | v11 |

### Evolutionary

*The system grows as it works.*

| Date | Change | Version |
|------|--------|---------|
| 2026-02-22 | Evolution relay — satellites propose core evolution via harvest pipeline | v39 |
| 2026-02-22 | Project as first-class entity — P#/S#/D# indexing | v35 |
| 2026-02-22 | Publication #12 — Project Management | v35 |
| 2026-02-18 | Knowledge versioning and drift remediation | v10 |

### Distributed

*Intelligence flows both ways. Push methodology to satellites, harvest insights back.*

| Date | Change | Version |
|------|--------|---------|
| 2026-02-22 | Evolution relay — satellites propose core evolution entries | v39 |
| 2026-02-22 | Self-heal PR auto-merge or guided merge for same-session activation | v38 |
| 2026-02-22 | Self-healing satellite CLAUDE.md via canonical template | v37 |
| 2026-02-21 | Critical-subset satellite CLAUDE.md | v31 |
| 2026-02-20 | Live knowledge network + beacon (port 21337) | v23 |
| 2026-02-19 | Save merge protocol + cross-repo push discovery | v16 |
| 2026-02-18 | Distributed minds — bidirectional knowledge flow | v9 |

### Persistent

*Sessions are ephemeral, knowledge is permanent.*

| Date | Change | Version |
|------|--------|---------|
| 2026-03-01 | **Four-channel persistence** — session runtime cache as fourth channel, 18 typed data keys, cache-first recovery. [#8](https://packetqc.github.io/knowledge/publications/session-management/) [#23](https://packetqc.github.io/knowledge/publications/agent-ticket-sync/) | — |
| 2026-02-21 | Critical-subset satellite CLAUDE.md survives compaction | v31 |
| 2026-02-19 | Semi-automatic delivery documentation | v20 |
| 2026-02-16 | Session persistence methodology — wakeup → work → save | v1 |
| 2026-02-16 | Free Guy analogy — NPC → aware | v2 |

### Recursive

*The system documents itself by consuming its own output.*

| Date | Change | Version |
|------|--------|---------|
| 2026-02-22 | Evolution relay — system evolves its own evolution mechanism via itself | v39 |
| 2026-02-22 | NEWS.md — self-categorizing changelog | — |
| 2026-02-22 | Publication #12 documents the project management system | v35 |

### Secure

*Security by architecture, not by obscurity.*

| Date | Change | Version |
|------|--------|---------|
| 2026-02-23 | **Compliancy security check** — compliance report Phase 1+3 updated to ✅ Applied (OWASP MCP01, NIST) | v46 |
| 2026-02-23 | Token zero-display — environment-only delivery + GraphQL in `gh_helper.py` | v46 |
| 2026-02-23 | Token display fix — AskUserQuestion "Other" field NOT invisible (v34 corrected) | v45 |
| 2026-02-23 | Classic PAT only — fine-grained discarded (API 400 + Projects v2 FORBIDDEN) | v41 |
| 2026-02-22 | Proxy deep mapping v2 — `curl` intercepted, `urllib` is true bypass | v40 |
| 2026-02-21 | ~~Secure textarea token delivery — invisible in transcript~~ (corrected v45) | v34 |
| 2026-02-21 | PAT Access Levels — 4-tier least-privilege model | v33 |
| 2026-02-21 | Safe elevation protocol — API crash mitigation | v30 |
| 2026-02-21 | Ephemeral token protocol — private repo access | v27 |
| 2026-02-19 | Access scope — user-owned repos with Claude Code access only | v21 |
| 2026-02-19 | Public HTTPS repo access — no stored credentials | v13 |

### Resilient

*The system survives crashes, compaction, and network failures.*

| Date | Change | Version |
|------|--------|---------|
| 2026-03-01 | **Cache-first compaction recovery** — `read_runtime_cache()` as first action after context loss, 18 session_data keys survive. [#8](https://packetqc.github.io/knowledge/publications/session-management/) [#23](https://packetqc.github.io/knowledge/publications/agent-ticket-sync/) | — |
| 2026-02-23 | API 400 prevention — Tool Call Discipline + deduplication checks | v44 |
| 2026-02-23 | Non-blocking PR creation — protocols continue on PR failure | v42 |
| 2026-02-23 | Wakeup deduplication — root cause of recurring API 400 fixed | v43 |
| 2026-02-22 | Self-heal PR merge — fix activates in same session, not next | v38 |
| 2026-02-22 | Full-read instruction — satellites get complete core context | v37 |
| 2026-02-21 | `recall` command — branch-based work recovery | v32 |
| 2026-02-21 | Checkpoint/resume — crash recovery | v29 |
| 2026-02-21 | Proxy architecture deep mapping — understanding limits | v28 |
| 2026-02-20 | `refresh` command — lightweight mid-session context restore | v24 |
| 2026-02-19 | Proxy reality — semi-automatic protocol adaptation | v17 |

### Structured

*Organized around projects, not just publications.*

| Date | Change | Version |
|------|--------|---------|
| 2026-02-24 | Per-section board widgets on plan pages — hierarchical views matching board sections | — |
| 2026-02-23 | P6 Export Documentation registered as hosted project (in P3) | v44 |
| 2026-02-22 | 7 GitHub Project boards created via GraphQL API (`createProjectV2`) | v40 |
| 2026-02-22 | NEWS.md + 6 web pages (news/plan/links EN/FR) — new reference section | v38 |
| 2026-02-22 | Project as first-class entity — P#/S#/D# indexing | v35 |
| 2026-02-22 | Project hub pages EN/FR | v35 |
| 2026-02-22 | Publication #12 — Project Management | v35 |
| 2026-02-22 | Dual-origin links — core vs satellite badges | v35 |
| 2026-02-20 | Core Qualities crystallized (10 → 12) | v25 |
| 2026-02-17 | Profile hub architecture — hub + subpages | v8 |

### Integrated

*The system extends into external platforms. GitHub Projects, Issues, and PRs become live mirrors.*

| Date | Change | Version |
|------|--------|---------|
| 2026-02-24 | Live board widgets — GitHub Project board rendered directly on plan pages with section filtering | — |
| 2026-02-24 | `sync_roadmap.py` — TAG: convention maps knowledge types to board sections | — |
| 2026-02-23 | 7 GitHub Project boards created + linked to repositories | v40–v41 |

---

## By Structure

### Core (CLAUDE.md)

| Date | Change | Version |
|------|--------|---------|
| 2026-02-23 | Token zero-display — environment-only delivery + GraphQL in `gh_helper.py` | v46 |
| 2026-02-23 | Token display fix — AskUserQuestion "Other" NOT invisible (v34 corrected) | v45 |
| 2026-02-23 | Interactive Input Convention + Tool Call Discipline | v44 |
| 2026-02-23 | Wakeup deduplication — entry message consumed by auto-boot | v43 |
| 2026-02-23 | `gh_helper.py` sole API method, non-blocking PR creation | v42 |
| 2026-02-23 | `linkProjectV2ToRepository` + classic PAT only | v41 |
| 2026-02-22 | Proxy deep mapping v2 — `curl` blocked, `urllib` bypasses | v40 |
| 2026-02-22 | Evolution relay — `harvest --stage N evolution` type | v39 |
| 2026-02-22 | Wakeup step 0.56 — self-heal PR merge (auto or guided) | v38 |
| 2026-02-22 | Beacon auto-start disabled — manual only (step 0.6) | v38 |
| 2026-02-22 | Wakeup step 0.55 — self-heal satellite CLAUDE.md | v37 |
| 2026-02-22 | Wakeup step 0 — full-read instruction (limit: 3500) | v37 |
| 2026-02-22 | Dynamic default branch detection (removed hardcoded `main`) | v37 |
| 2026-02-22 | Project entity model, P# registry, dual-origin links | v35 |
| 2026-02-21 | Secure textarea token delivery | v34 |
| 2026-02-21 | PAT Access Levels — 4-tier model | v33 |
| 2026-02-21 | `recall` command + universal `?` contextual help | v32 |
| 2026-02-21 | Critical-subset satellite template | v31 |
| 2026-02-21 | Safe elevation protocol | v30 |
| 2026-02-21 | Checkpoint/resume mechanism | v29 |
| 2026-02-21 | Proxy architecture mapping + API bypass | v28 |
| 2026-02-21 | Ephemeral token protocol | v27 |
| 2026-02-20 | Scoped project notes `#N:` | v26 |
| 2026-02-20 | Core Qualities + iterative staging | v25 |
| 2026-02-20 | `refresh` command + dashboard rename | v24 |
| 2026-02-19 | Access scope documentation | v21 |
| 2026-02-19 | `main` as convergence branch | v18 |
| 2026-02-19 | Proxy reality — semi-automatic protocol | v17 |
| 2026-02-19 | Branch protocols (v12–v16) | v12–v16 |
| 2026-02-18 | Distributed minds + versioning + healthcheck | v9–v11 |
| 2026-02-17 | Normalize, profile, step 0, multipart help | v4–v8 |
| 2026-02-17 | Knowledge repo as portable bootstrap | v3 |
| 2026-02-16 | Session persistence + Free Guy analogy | v1–v2 |

### Publications

| Date | Change | Version |
|------|--------|---------|
| 2026-03-01 | [#8 Session Management](https://packetqc.github.io/knowledge/publications/session-management/) + [#23 Agent Ticket Sync](https://packetqc.github.io/knowledge/publications/agent-ticket-sync/) — source READMEs, full pages, summary pages updated: four-channel model, cache-first recovery, 18 session_data keys. PRs #522–#524 | — |
| 2026-02-26 | #18 Documentation Generation Methodology — meta-methodology + 3-tier bilingual (source + EN/FR summary + complete). Closes #355 | — |
| 2026-02-26 | #17 Web Production Pipeline — 3-tier bilingual (source + EN/FR summary + complete). Closes #348 | — |
| 2026-02-26 | #14 Architecture Analysis — 3-tier bilingual (source + EN/FR summary + complete) | — |
| 2026-02-26 | #15 Architecture Diagrams — 3-tier bilingual (source + EN/FR summary + complete) with 11 Mermaid diagrams | — |
| 2026-02-26 | #11 Success Stories — Story #16 Rencontre de travail productive | — |
| 2026-02-23 | #11 Success Stories — Story #8 Token Disclosure Deep Investigation | v46 |
| 2026-02-23 | #9a Compliance Report — Phase 1+3 updated to ✅ Applied (compliancy security check) | v46 |
| 2026-02-22 | #12 Project Management — 3-tier bilingual (source + EN/FR summary + complete) | v35 |
| 2026-02-22 | #11 Success Stories — Story #2 PAT promotion | v33 |
| 2026-02-22 | #9 Security by Design — PAT levels section | v33 |
| 2026-02-21 | #8 Session Management — checkpoint/resume docs | v29 |
| 2026-02-19 | #4 Distributed Minds — v20 semi-automatic delivery | v20 |
| 2026-02-19 | #5 Webcards & Social Sharing | v22 |
| 2026-02-19 | #6 Normalize & Structure Concordance | v22 |
| 2026-02-19 | #7 Harvest Protocol | v22 |
| 2026-02-18 | #4a Knowledge Dashboard — live satellite data | v11 |
| 2026-02-17 | #0 Knowledge System — master publication | v3 |
| 2026-02-17 | #1–#3 initial publications | v3 |

### Webcards

| Date | Change | Version |
|------|--------|---------|
| 2026-02-22 | #12 Project Management OG GIFs (4 files: en/fr × cayman/midnight) | — |
| 2026-02-22 | 12 webcards moved from Missing to Deployed in LINKS.md | — |
| 2026-02-19 | Dual-theme system: Cayman (light) + Midnight (dark) | v22 |
| 2026-02-19 | 40 animated GIFs (10 cards × 2 themes × 2 langs) | v22 |

### Dashboard

| Date | Change | Version |
|------|--------|---------|
| 2026-02-20 | Fields renamed: `Live` → `Assets`, `Lives` → `Live` | v24 |
| 2026-02-18 | Interactive promotion workflow + severity icons | v11 |
| 2026-02-18 | Satellite Network Status table | v9 |

### Satellites

| Date | Change | Version |
|------|--------|---------|
| 2026-02-22 | Self-heal PR merge — same-session command activation | v38 |
| 2026-02-22 | Self-healing satellite CLAUDE.md via canonical template | v37 |
| 2026-02-22 | knowledge-live updated to v37 via GitHub API | v37 |
| 2026-02-22 | knowledge-live updated to v36 — full 7-group commands | v36 |
| 2026-02-21 | Critical-subset template (~180 lines) replaces thin-wrapper (~30 lines) | v31 |
| 2026-02-20 | Bootstrap scaffold protocol — non-destructive auto-creation | v23 |
| 2026-02-20 | Iterative staging protocol validated on MPLIB Dev Staging | v25 |

### Methodology

| Date | Change | Version |
|------|--------|---------|
| 2026-03-03 | `methodology/session-protocol.md` + `methodology/interactive-work-sessions.md` + `methodology/documentation-generation.md` — session notes → issue comment, post-close final comment, CHANGELOG.md as essential file. Issue #610 | v55 |
| 2026-03-01 | `methodology/session-protocol.md` + `methodology/interactive-work-sessions.md` — three→four-channel persistence, cache row in tables, cache-first recovery protocol, four-channel recovery matrix. [#8](https://packetqc.github.io/knowledge/publications/session-management/) [#23](https://packetqc.github.io/knowledge/publications/agent-ticket-sync/) | — |
| 2026-02-26 | `methodology/documentation-generation.md` — meta-methodology: universal inheritance, mind map standard, quality checklist | — |
| 2026-02-26 | `methodology/web-production-pipeline.md` — Jekyll processing chain, kramdown gotchas, front matter contract | — |
| 2026-02-23 | `methodology/satellite-bootstrap.md` — removed inline `GH_TOKEN` pattern (3 locations) | v46 |
| 2026-02-23 | `methodology/project-management.md` — raw GraphQL replaced with `gh_helper.py` CLI | v46 |
| 2026-02-23 | `methodology/project-create.md` — steps 8-9 consolidated to `gh_helper.py project ensure` | v46 |
| 2026-02-22 | `methodology/satellite-commands.md` — canonical commands template | v37 |
| 2026-02-22 | `methodology/satellite-bootstrap.md` — self-heal section added | v37 |
| 2026-02-22 | `methodology/project-management.md` — project lifecycle | v35 |
| 2026-02-20 | Iterative staging installation protocol | v25 |

### Scripts

| Date | Change | Version |
|------|--------|---------|
| 2026-03-01 | `scripts/session_agent.py` — 18 session_data keys + 12 dedicated helper functions (append_request_addon, update_todo_snapshot, append_pr_number, etc.). [#23](https://packetqc.github.io/knowledge/publications/agent-ticket-sync/) | — |
| 2026-02-24 | `scripts/sync_roadmap.py` — section classification + labels extraction + Done override | — |
| 2026-02-23 | `scripts/gh_helper.py` — GraphQL + Project board support added (v46) | v46 |
| 2026-02-22 | `scripts/gh_helper.py` — portable PR management (urllib, no deps) | v36 |
| 2026-02-22 | `scripts/generate_og_gifs.py` — #12 webcard generator added | — |
| 2026-02-21 | `scripts/pqc_envelope.py` — PQC crypto module (ML-KEM + X25519) | v27 |
| 2026-02-20 | `live/knowledge_beacon.py` — inter-instance discovery | v23 |
| 2026-02-20 | `live/knowledge_scanner.py` — subnet peer scanner | v23 |

### Docs/Web

| Date | Change | Version |
|------|--------|---------|
| 2026-02-25 | **publication.html** — DOCX: OOXML ZIP from scratch (altChunk), running header/footer, 6 bug fixes | — |
| 2026-02-25 | **publication.html** — PDF: single full-width header liner (@top-left width:100%), language bar redesign | — |
| 2026-02-25 | **publication.html** — baseline synced from knowledge-live: 4-theme CSS, cross-refs, board widget, export toolbar | — |
| 2026-02-25 | **Layout convention** — 3 layouts formalized: publication.html (export), default.html (no export), three-zone @page | — |
| 2026-02-24 | **publication.html** — DOCX complete rewrite: MSO 3-zone, cover page, visual fidelity (8 fixes) | — |
| 2026-02-24 | **publication.html** — PDF overhaul: Knowledge footer link, filename sanitization, clickable TOC | — |
| 2026-02-24 | Plan pages: per-section board widgets + dropdown filters + Mermaid lifecycle diagram + Completed/Terminé section | — |
| 2026-02-24 | Layout widgets: multi-instance board rendering, per-section filtering, localStorage persistence | — |
| 2026-02-22 | NEWS.md central changelog + 6 web pages (news/plan/links EN/FR) | v38 |
| 2026-02-22 | Project hub pages EN/FR (`docs/projects/`) | v35 |
| 2026-02-22 | What's New / Nouveautés sections on central documents | — |
| 2026-02-22 | #12 web pages: EN/FR summary + complete (4 pages) | v35 |
| 2026-02-20 | 4-theme accessibility system (daltonism-safe) | v26 |
| 2026-02-19 | Dual-theme layouts: Cayman + Midnight CSS | v22 |
| 2026-02-17 | Profile hub + resume + full profile (6 bilingual pages) | v8 |

### Projects

| Date | Change | Version |
|------|--------|---------|
| 2026-02-23 | P6 Export Documentation registered (hosted in P3) | v44 |
| 2026-02-22 | 7 GitHub Project boards created (P0 #4 through P6 #10) | v40 |
| 2026-02-23 | Project boards linked to repositories via `linkProjectV2ToRepository` | v41 |
| 2026-02-22 | `projects/` folder with 6 metadata files + README | v35 |
| 2026-02-22 | P0–P5 registry: Knowledge, MPLIB, STM32, knowledge-live, MPLIB Dev, PQC | v35 |
| 2026-02-22 | Hierarchical indexing: P#/S#/D# scheme | v35 |

---

## By Type

### Features

| Date | Change | Version |
|------|--------|---------|
| 2026-03-03 | **Session notes → issue + CHANGELOG.md (v55)** — session notes posted as issue comment at save, post-close final comment, new CHANGELOG.md per-issue/PR audit trail with bilingual web pages. Issue #610 | v55 |
| 2026-03-01 | **Four-channel persistence model** — session runtime cache as fourth channel, 18 typed data keys, 12 helper functions, multi-session naming, cache-first recovery. [#8](https://packetqc.github.io/knowledge/publications/session-management/) [#23](https://packetqc.github.io/knowledge/publications/agent-ticket-sync/) | — |
| 2026-02-25 | **3 convention layouts** — publication.html (export stack), default.html (no export), three-zone @page model (P6/P8) | — |
| 2026-02-25 | **Language bar auto-generation** — Liquid template injection from permalink, above pub-topbar (P6, knowledge-live) | — |
| 2026-02-25 | **publication.html baseline sync** — 4-theme CSS, cross-refs, board widget, export toolbar: dev→prod promotion (P6) | — |
| 2026-02-24 | Live board widgets on plan pages — per-section filtering, dropdown status filters, Mermaid lifecycle | — |
| 2026-02-24 | Board sync pipeline — `sync_roadmap.py` section classification + TAG: prefix mapping | — |
| 2026-02-23 | Interactive Input Convention — upfront multi-question gathering | v44 |
| 2026-02-22 | Evolution relay — satellites propose core evolution entries | v39 |
| 2026-02-22 | 7 GitHub Project boards created via GraphQL API | v40 |
| 2026-02-22 | Self-heal PR merge — same-session command activation (step 0.56) | v38 |
| 2026-02-22 | NEWS.md central changelog with 4 categorization views | v38 |
| 2026-02-22 | 6 bilingual web pages: news, plan, links (EN/FR) | v38 |
| 2026-02-22 | Self-healing satellite CLAUDE.md — automatic drift remediation | v37 |
| 2026-02-22 | GitHub helper (`gh_helper.py`) — portable PR management | v36 |
| 2026-02-22 | Project as first-class entity — P#/S#/D# indexing | v35 |
| 2026-02-22 | Publication #12 — Project Management (3-tier bilingual) | v35 |
| 2026-02-21 | `recall` command — branch-based work recovery | v32 |
| 2026-02-21 | Critical-subset satellite CLAUDE.md | v31 |
| 2026-02-21 | Checkpoint/resume — crash recovery | v29 |
| 2026-02-21 | Ephemeral token protocol — private repo access | v27 |
| 2026-02-20 | Scoped project notes `#N:` | v26 |
| 2026-02-20 | Core Qualities + iterative staging | v25 |
| 2026-02-20 | `refresh` command | v24 |
| 2026-02-20 | Live knowledge network + bootstrap scaffold | v23 |
| 2026-02-19 | Dual-theme webcards: Cayman + Midnight | v22 |
| 2026-02-19 | Knowledge branch protocol | v12 |
| 2026-02-18 | Interactive promotion + severity icons + healthcheck | v11 |
| 2026-02-18 | Knowledge versioning and drift remediation | v10 |
| 2026-02-18 | Distributed minds — bidirectional knowledge flow | v9 |
| 2026-02-17 | Profile hub architecture | v8 |
| 2026-02-17 | Normalize command | v7 |
| 2026-02-17 | Step 0: sunglasses first | v5 |
| 2026-02-17 | Multipart help architecture | v4 |
| 2026-02-17 | Knowledge repo as portable bootstrap | v3 |
| 2026-02-16 | Session persistence methodology | v1 |

### Enhancements

| Date | Change | Version |
|------|--------|---------|
| 2026-02-24 | Dropdown status filters on all per-section board widgets (default: active, done: done) | — |
| 2026-02-24 | Completed/Terminé section on plan pages — shows delivered items | — |
| 2026-02-24 | Success Story #12 — Human Person Machine Bridge: Knowledge as Jira+Confluence | — |
| 2026-02-23 | Tool Call Discipline — self-diagnostic for duplicate tool patterns | v44 |
| 2026-02-23 | GitHub Project boards linked to repositories | v41 |
| 2026-02-23 | Non-blocking PR creation — protocols continue on failure | v42 |
| 2026-02-22 | Beacon auto-start disabled — manual only | v38 |
| 2026-02-22 | Changelog links added to all What's New sections | v38 |
| 2026-02-22 | Full-read instruction for core CLAUDE.md (limit: 3500) | v37 |
| 2026-02-22 | Canonical commands template (`satellite-commands.md`) | v37 |
| 2026-02-22 | Webcard OG GIFs for #12 (4 files) | — |
| 2026-02-22 | LINKS.md — 12 webcards moved from Missing to Deployed | — |
| 2026-02-22 | What's New / Nouveautés sections on central documents | — |
| 2026-02-21 | ~~Secure textarea token delivery — invisible in transcript~~ (corrected v45) | v34 |
| 2026-02-21 | Universal `?` contextual help with publication links | v32 |
| 2026-02-20 | Dashboard fields renamed: `Live` → `Assets`, `Lives` → `Live` | v24 |
| 2026-02-19 | Access scope — user-owned repos only | v21 |
| 2026-02-19 | Todo list must mirror full save protocol | v19 |
| 2026-02-19 | `main` replaces `claude/knowledge` — simplification | v18 |
| 2026-02-19 | `claude/knowledge` replaces `knowledge` | v14 |
| 2026-02-19 | Public HTTPS repo access | v13 |

### Fixes

| Date | Change | Version |
|------|--------|---------|
| 2026-02-25 | **DOCX export: OOXML ZIP from scratch** — removes html-docx-js, altChunk approach, fixes Word+LibreOffice corruption (P6) | — |
| 2026-02-25 | **DOCX export: 6 bugs fixed** — MSO display:none, cover double-clone, page breaks, pie chart, Mermaid guard, Stories (P6) | — |
| 2026-02-25 | **PDF export: single header liner** — @top-left width:100%, Chrome double-liner eliminated (P6, knowledge-live) | — |
| 2026-02-24 | **DOCX export: complete rewrite** — 8 fixes for MSO layout, cover page, section properties, visual fidelity (P6) | — |
| 2026-02-24 | **PDF export: header/footer/Mermaid overhaul** — clickable links, filename sanitization, Knowledge repo footer (P6, knowledge-live) | — |
| 2026-02-23 | Token zero-display — all API calls via `gh_helper.py`, environment-only delivery | v46 |
| 2026-02-23 | Token display fix — AskUserQuestion "Other" field NOT invisible (v34 wrong) | v45 |
| 2026-02-23 | Wakeup deduplication — root cause of recurring API 400 crashes | v43 |
| 2026-02-23 | `curl` to `api.github.com` blocked — `gh_helper.py`/`urllib` is sole path | v40 |
| 2026-02-23 | Classic PAT only — fine-grained discarded (Projects v2 FORBIDDEN) | v41 |
| 2026-02-22 | Hardcoded branch refs — dynamic default branch detection | v37 |
| 2026-02-21 | Safe elevation protocol — API 400 crash mitigation | v30 |
| 2026-02-19 | Proxy reality — protocol adapted to actual proxy limits | v17 |

### Documentation

| Date | Change | Version |
|------|--------|---------|
| 2026-03-01 | **Session cache documentation sync** — [#8 Session Management](https://packetqc.github.io/knowledge/publications/session-management/) and [#23 Agent Ticket Sync](https://packetqc.github.io/knowledge/publications/agent-ticket-sync/) updated across source, full pages, summary pages (EN/FR), methodology files. PRs #522–#524 | — |
| 2026-02-26 | **Publication #14 — Architecture Analysis** — full architecture decomposition, 3-tier bilingual. Closes #316 | — |
| 2026-02-26 | **Publication #15 — Architecture Diagrams** — 11 Mermaid diagrams, 3-tier bilingual. Closes #317 | — |
| 2026-02-26 | **Success Story #16 — Rencontre de travail productive** | — |
| 2026-02-25 | **Export Documentation complete** — 37 PRs (19 knowledge-live + 18 knowledge), DOCX+PDF production-ready, 3 layouts documented (P6/P8) | — |
| 2026-02-25 | **Dev→Prod promotion documented** — knowledge-live (dev) layouts promoted to knowledge (prod) via harvest issues | — |
| 2026-02-24 | Success Story #12 — Human Person Machine Bridge: Knowledge as Jira+Confluence (zero paid tools) | — |
| 2026-02-24 | Knowledge core publication (#0) introduction updated with Human Person Machine Bridge mention | — |
| 2026-02-23 | **Compliancy security check** — Publication #9a compliance report updated to ✅ Applied | v46 |
| 2026-02-23 | Success Story #8 — Token Disclosure Deep Investigation (19-version arc) | v46 |
| 2026-02-23 | Pitfall #17 documented — AskUserQuestion "Other" displays token in session | v45 |
| 2026-02-23 | Pitfalls #13–#16 documented (curl proxy, Projects v2, chained commands, board linking) | v40–v44 |
| 2026-02-23 | `methodology/project-create.md` — interactive input specification | v44 |
| 2026-02-22 | `methodology/satellite-bootstrap.md` — self-heal section | v37 |
| 2026-02-22 | `methodology/project-management.md` — project lifecycle | v35 |
| 2026-02-22 | `projects/` metadata files + README | v35 |
| 2026-02-21 | PAT Access Levels — 4-tier model documented | v33 |
| 2026-02-21 | Proxy architecture deep mapping + API bypass | v28 |
| 2026-02-20 | Iterative staging installation protocol | v25 |
| 2026-02-19 | Semi-automatic delivery documentation + admin routine | v20 |
| 2026-02-19 | End-to-end protocol validation | v15 |
| 2026-02-17 | Chicken-and-egg bootstrap documented | v6 |
| 2026-02-16 | Free Guy analogy — the mental model | v2 |

---

*This file tracks all changes to the knowledge system. Each evolution entry (v#) maps to one or more categories above. Non-versioned changes (webcards, web pages, content updates) are also tracked here.*

*[Publications →](https://packetqc.github.io/knowledge/index.html?doc=publications/index.md) | [Viewer →](https://packetqc.github.io/knowledge/)*
