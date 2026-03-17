# Project: Export Documentation

<!-- project-id: P6 -->
<!-- project-type: managed -->
<!-- project-status: active -->
<!-- github-project: https://github.com/users/packetqc/projects/10 -->
<!-- managed-in-repo: packetqc/knowledge-live -->
<!-- path-prefix: projects/export-documentation/ -->

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | P6 |
| **Name** | Export Documentation |
| **Type** | managed (in P3/knowledge-live) |
| **Repository** | [packetqc/knowledge-live](https://github.com/packetqc/knowledge-live) (shared) |
| **Path** | `projects/export-documentation/` |
| **GitHub Project** | [#10](https://github.com/users/packetqc/projects/10) |
| **Status** | 🟢 active |
| **Created** | 2026-02-22 |
| **Knowledge Version** | v48 |
| **Description** | Export and publication pipeline for the knowledge network — PDF export (CSS Paged Media), DOCX export (OOXML ZIP via altChunk), 3 convention layouts, cross-repo dev→prod promotion workflow. First managed project in the knowledge network. |

**Role in ecosystem**: Documentation infrastructure for Knowledge's export and publication workflows. Managed within knowledge-live (P3) — shares repository, tooling, and web presence with no dedicated repo. Board linked to host repo.

---

## Publications

| Index | Title | Status |
|-------|-------|--------|
| [#13](https://packetqc.github.io/knowledge/publications/web-pagination-export/) | Web Pagination & Export | 🟢 published |

---

## Satellites

N/A — managed projects have no satellites. Physical location: `packetqc/knowledge-live/projects/export-documentation/`.

---

## Tasks

| ID | Title | Status | Created | Completed |
|----|-------|--------|---------|-----------|
| T1 | Universal layout pagination for exportation and web pages | Done | 2026-02-24 | 2026-02-25 |
| T2 | PDF export pipeline — header/footer/Mermaid/language bar | Done | 2026-02-24 | 2026-02-25 |
| T3 | DOCX export pipeline — OOXML ZIP, cover page, MSO layout | Done | 2026-02-24 | 2026-02-25 |
| T4 | 3 convention layouts — publication.html / default.html / three-zone @page | Done | 2026-02-25 | 2026-02-25 |
| T5 | Dev→Prod promotion — knowledge-live to knowledge core | Done | 2026-02-25 | 2026-02-25 |

---

## Activity Timeline

### 2026-02-24 (Dev — knowledge-live)

| Time | Activity | PRs | Repo |
|------|----------|-----|------|
| AM | Sync publication.html baseline from core — 4-theme CSS, cross-refs widget, board widget, export toolbar | PR #42 | knowledge-live |
| AM | Publication #0 local copy for export testing | PR #42 | knowledge-live |
| AM | CLAUDE.md updated v39→v47 (8-version drift resolved) | PR #42 | knowledge-live |
| PM | PDF export: clickable links in print, document title as filename | PR #44 | knowledge-live |
| PM | PDF export: methodology notes — print export stack documented | PR #45 | knowledge-live |
| PM | Site footer with Knowledge repo link | PR #46 | knowledge-live |
| PM | PDF footer: Knowledge repo clickable link (@bottom-right) | PR #47 | knowledge-live |
| PM | PDF export overhaul — header/footer/table/Mermaid fixes | PR #48 | knowledge-live |
| PM | T1 task created — Universal layout pagination | — | knowledge-live |
| PM | DOCX export: complete rewrite with 8 fixes | PR #289 | knowledge |
| PM | DOCX export: MSO 3-zone page layout with header/footer | PR #290 | knowledge |

### 2026-02-25 (Dev+QA — knowledge-live, then Prod — knowledge)

| Time | Activity | PRs | Repo |
|------|----------|-----|------|
| AM | PDF export overhaul — language bar redesign, header border, TOC spacing | PR #49 | knowledge-live |
| AM | Success Stories local copy for export testing | PR #51 | knowledge-live |
| AM | Double language bar + TOC table multi-column fix | PR #52 | knowledge-live |
| AM | PDF header title+liner + footer Knowledge alignment | PR #53 | knowledge-live |
| AM | Remove duplicate lang bar + version in publication pages | PR #54 | knowledge-live |
| AM | Header liner full-width, margins, story tables, pie charts | PR #55 | knowledge-live |
| AM | Single header liner + h3 section names + Story Format | PR #56 | knowledge-live |
| AM | Restore readmore links on all 12 stories | PR #57 | knowledge-live |
| AM | Fix stray `</div>` in readmore links | PR #58 | knowledge-live |
| AM | **Final: single full-width header liner** — @top-left width:100% | PR #59 | knowledge-live |
| PM | DOCX export: 6 bugs fixed (MSO display, cover dupe, page breaks, pie, Mermaid, Stories) | PR #291 | knowledge |
| PM | Stranded work recovered (v48 wakeup + TOC fix) | PR #292 | knowledge |
| PM | DOCX: MSO header/footer placement + mso-title-page | PR #294 | knowledge |
| PM | DOCX: async Mermaid PNG, cover page break, MSO div cleanup | PR #295 | knowledge |
| PM | DOCX: inject page-break paragraph after cover | PR #296 | knowledge |
| PM | DOCX: Word-compatible cover page layout | PR #297 | knowledge |
| PM | DOCX: visual fidelity — pie charts, emoji, story-row | PR #298 | knowledge |
| PM | DOCX: story table — no header, consistent borders | PR #299 | knowledge |
| PM | DOCX: html-docx-js OOXML + emoji alignment + borderless inner tables | PR #300 | knowledge |
| PM | DOCX: restore running header/footer via JSZip post-processing | PR #302 | knowledge |
| PM | DOCX: remove invalid style refs, null-check ZIP entries | PR #303 | knowledge |
| PM | **Final: OOXML ZIP from scratch via altChunk** — removes html-docx-js | PR #304 | knowledge |

### Summary

| Metric | Value |
|--------|-------|
| **Total PRs** | 37 (19 knowledge-live + 18 knowledge) |
| **Duration** | 2 days (2026-02-24 to 2026-02-25) |
| **DOCX fixes** | 8 major issues resolved across 10 PRs |
| **PDF fixes** | Single header liner + footer + Mermaid + TOC across 8 PRs |
| **Layouts formalized** | 3 (publication.html, default.html, three-zone @page) |
| **Dev→Prod** | knowledge-live (dev/pre-prod) → knowledge (prod) via harvest issues |
| **Issue #301** | DOCX export: 7 visual fixes — tracking issue (10 sub-fixes) |

---

## Evolution

| Date | Entry |
|------|-------|
| 2026-02-25 | **DOCX export production-ready** — OOXML ZIP from scratch via altChunk, removes html-docx-js dependency |
| 2026-02-25 | **PDF export production-ready** — single full-width header liner, language bar auto-generated |
| 2026-02-25 | **3 convention layouts formalized** — publication.html / default.html / three-zone @page scope boundaries |
| 2026-02-25 | **Dev→Prod promotion complete** — all layouts promoted from knowledge-live to knowledge core |
| 2026-02-25 | All 5 tasks completed (T1–T5) — export documentation QA cycle closed |
| 2026-02-24 | T1 created — Universal layout pagination for exportation and web pages |
| 2026-02-24 | PDF export overhaul — header, footer, Mermaid, clickable links, filename sanitization |
| 2026-02-24 | DOCX export: complete rewrite with 8 fixes — MSO 3-zone, cover page, section properties |
| 2026-02-24 | publication.html baseline synced from core — 4-theme CSS, cross-refs, board widget |
| 2026-02-22 | Registered as managed project in P3 (knowledge-live) — first managed-in instance |
| 2026-02-22 | Subfolder scaffold created: README, docs/, notes/, assets/ |
| 2026-02-22 | Design spec authored: `notes/v39-hosted-project-design.md` |
| 2026-02-22 | Harvested by core — registered in core project registry |

---

## Stories

| Date | Story |
|------|-------|
| 2026-02-22 | First managed project in the knowledge network. Design spec authored in P3 satellite session, promoted via evolution-relay (v39). Validates the managed-in architecture. |

---

## Required Assets Status

| Asset | Status | Notes |
|-------|--------|-------|
| Subfolder scaffold | 🟢 created | `projects/export-documentation/` in P3 satellite |
| README.md | 🟢 present | Project overview with managed markers |
| docs/ | 🟢 created | Empty — ready for documentation |
| notes/ | 🟢 created | Empty — ready for session notes |
| assets/ | 🟢 created | Empty — ready for project assets |
| Core registry | 🟢 registered | `projects/export-documentation.md` in core |
| GitHub Project | 🟢 [#10](https://github.com/users/packetqc/projects/10) | Created 2026-02-22 |
| Host CLAUDE.md | 🟢 updated | P3's CLAUDE.md lists P6 in "Managed Projects" section |

---

## Design Reference

Full design spec: `packetqc/knowledge-live/notes/v39-hosted-project-design.md`

Key decisions:
- Subfolder under `projects/` (consistent with core convention)
- No nested Jekyll site (lightweight — just markdown)
- Own GitHub Project board (platform independence without repo independence)
- AskUserQuestion for managed vs child decision (Human Bridge)
