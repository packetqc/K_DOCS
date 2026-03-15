# Project: Documentation System

<!-- project-id: P8 -->
<!-- project-type: managed -->
<!-- project-status: active -->
<!-- github-project: https://github.com/users/packetqc/projects/38 -->
<!-- managed-in-repo: packetqc/knowledge -->

---

## Identity

| Field | Value |
|-------|-------|
| **ID** | P8 |
| **Name** | Documentation System |
| **Type** | managed (in P0/knowledge) |
| **Repository** | [packetqc/knowledge](https://github.com/packetqc/knowledge) (shared) |
| **GitHub Project** | [#38](https://github.com/users/packetqc/projects/38) |
| **Status** | 🟢 active |
| **Created** | 2026-02-24 |
| **Knowledge Version** | v47 |
| **Description** | Core-level documentation tracking and authorship — organizes documentation efforts across all publications, satellites, and the knowledge system itself. |

**Role in ecosystem**: Central documentation governance for the knowledge network. Tracks publication freshness, authorship, cross-satellite documentation convergence, and content lifecycle (draft → review → publish → maintain). Managed within knowledge core (P0) — no dedicated repo needed.

**Relationship to P6 (Export Documentation)**: P6 manages export/publication workflows within knowledge-live (P3). P8 operates at the core level — tracking all documentation across all satellites. P6 is a downstream producer; P8 is the upstream aggregator.

---

## Scope

| Area | Description |
|------|-------------|
| **Publications** | Track freshness, version alignment, and content quality for all 14 publications |
| **Authorship** | Document authorship attribution across Martin + Claude collaborative content |
| **Cross-satellite docs** | Track documentation discovered in satellites via harvest, coordinate promotion |
| **Content lifecycle** | Draft → review → publish → maintain — ensure no publication goes stale |
| **Documentation standards** | Three-tier bilingual structure, front matter requirements, asset conventions |

---

## Publications

| Index | Title | Status |
|-------|-------|--------|
| *(inherits all P0 publications)* | | |

---

## Cross-references

| Reference | Description |
|-----------|-------------|
| P0 | Knowledge System — parent project |
| P6 | Export Documentation — downstream producer in knowledge-live |
| Issue #201 | Origin — TASK: Create documentation project in Knowledge core |

---

## Tasks

| ID | Title | Status | Created | Completed |
|----|-------|--------|---------|-----------|
| T1 | 3 convention layouts — formalize publication.html / default.html / three-zone @page scope | Done | 2026-02-25 | 2026-02-25 |
| T2 | Export documentation QA — verify DOCX+PDF production-readiness across dev and prod | Done | 2026-02-25 | 2026-02-25 |
| T3 | Dev→Prod promotion tracking — knowledge-live layouts to knowledge core | Done | 2026-02-25 | 2026-02-25 |

---

## Activity Timeline

### 2026-02-24 (Documentation governance established)

| Activity | Details |
|----------|---------|
| P8 project registered | From knowledge-live harvest, issue #201 |
| Layout baseline sync tracked | publication.html core→satellite sync (knowledge-live PR #42) |
| Export pipeline development initiated | PDF+DOCX development in knowledge-live (dev tier) |

### 2026-02-25 (Layout convention + QA + promotion)

| Activity | Details |
|----------|---------|
| **3 convention layouts documented** | publication.html (full export: PDF/DOCX, version banner, cross-refs, 4-theme), default.html (profile/landing, no export), three-zone @page (header/content/footer CSS Paged Media) |
| **Export QA tracked** | 37 PRs verified across 2 repos — 19 knowledge-live (dev) + 18 knowledge (prod) |
| **Dev→Prod cycle completed** | Layouts promoted from knowledge-live (dev/pre-prod) to knowledge (prod) via harvest issues (#267, #268, #271) |
| **Layout scope boundaries formalized** | publication.html: print/export, language bar, version banner. default.html: no print/export. Both: 4-theme CSS, webcard header, OG tags |
| **DOCX pipeline tracked to completion** | 8 major issues resolved: MSO display, cover page, page breaks, pie charts, Mermaid, OOXML ZIP, running headers, altChunk |
| **PDF pipeline tracked to completion** | Single header liner, language bar, footer links, filename sanitization, TOC clickability |

---

## 3 Convention Layouts (P8 Reference)

| Layout | File | Scope | Export |
|--------|------|-------|--------|
| **Publication** | `docs/_layouts/publication.html` | Publications, technical docs | PDF (CSS Paged Media), DOCX (OOXML altChunk), language bar, version banner, cross-refs, export toolbar |
| **Default** | `docs/_layouts/default.html` | Profile pages, landing pages, hubs | No export features |
| **Three-zone @page** | CSS within publication.html | PDF print output | @top-left (header liner), content area, @bottom-left/center/right (footer) |

**Key scope boundaries**:
- Export toolbar, `printAs()`, language bar → `publication.html` only
- Both layouts share: 4-theme CSS (Cayman/Midnight/daltonism), webcard header, OG meta tags, Mermaid
- Three-zone model: `@page` CSS with `@top-left { width: 100% }` for single-liner header

---

## Evolution

| Date | Change |
|------|--------|
| 2026-02-25 | 3 convention layouts formalized — publication.html, default.html, three-zone @page |
| 2026-02-25 | Export documentation QA complete — 37 PRs across 2 repos, DOCX+PDF production-ready |
| 2026-02-25 | Dev→Prod promotion cycle tracked — knowledge-live (dev) → knowledge (prod) |
| 2026-02-24 | Project registered as P8 (from knowledge-live harvest, issue #201) |

---

*Created: 2026-02-24 — from harvest of knowledge-live (P3), issue #201*
