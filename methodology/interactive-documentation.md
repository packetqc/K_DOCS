# Interactive Documentation — Methodology

> Adapted from `packetqc/knowledge:knowledge/methodology/interactive-documentation.md`

**Creating publications, methodologies, and web pages** through interactive collaboration. The documentation session type for the Knowledge system.

---

## When to Use

- Creating a new publication (source + web pages EN/FR)
- Writing a new methodology file
- Updating existing publications for freshness
- Creating or updating web page content

---

## Core Principles

| Principle | Description |
|-----------|-------------|
| **Three-tier awareness** | Every publication has source → summary → full. All three must be created/updated |
| **Bilingual mirroring** | Every web page has EN + FR. Create both in the same pass |
| **Mind map first** | The visual overview is the reader's entry point. Write it before expanding content |
| **Source is truth** | `docs/publications/<slug>/v1/README.md` drives everything downstream |

---

## Phase Pattern

| Phase | Action | Output |
|-------|--------|--------|
| **Gather** | User provides raw intelligence via conversation | Notes, context |
| **Structure** | Create methodology file if applicable | `methodology/<slug>.md` |
| **Expand** | Write full publication source | `docs/publications/<slug>/v1/README.md` |
| **Web pages** | Create 4 web pages (EN/FR summary + full) | 4 markdown files with front matter |
| **Mirror** | Verify bilingual mirrors are complete | — |
| **Deliver** | Commit and push | All files committed |

---

## Session Protocol

### 1. Gather Raw Intelligence

The user feeds content through conversation. Claude classifies and organizes internally. The user provides raw intelligence; Claude structures it.

### 2. Create Methodology File First

If the publication documents a new methodology:
1. Write `methodology/<slug>.md` — the operational reference
2. Commit immediately — this file has value independent of the publication

**Why methodology first**: The methodology file is the practitioner's guide. The publication wraps it with context, analysis, and narrative. If the session is interrupted after the methodology file but before the publication, the operational knowledge is already captured.

### 3. Write Publication Source

Create `docs/publications/<slug>/v1/README.md` following `documentation-generation.md`:

1. Title block with publication number, version, date
2. Authors with role descriptions
3. Abstract (200–400 words) — "why" before "what"
4. Mind map diagram — visual summary after abstract
5. Problem section — the engineering need
6. Solution section — how it works
7. Impact section — before/after, design principles
8. Related publications — cross-references

### 4. Create Web Pages (Batch)

Create all 4 web pages in one pass:

| # | File | Content |
|---|------|---------|
| 1 | `docs/publications/<slug>/index.md` | EN summary |
| 2 | `docs/publications/<slug>/full/index.md` | EN full |
| 3 | `docs/fr/publications/<slug>/index.md` | FR summary |
| 4 | `docs/fr/publications/<slug>/full/index.md` | FR full |

**Front matter**: `title`, `description`, `pub_id`, `version`, `pub_date`, `permalink`, `og_image`, `keywords`.

### 5. Deliver

Commit all changes together and push.

---

## Context Budget Rules

| Do | Don't |
|----|-------|
| Create all 4 web pages in one pass | Create EN, commit, then FR separately |
| Read source once, adapt for each page | Re-read source for each web page |
| Use mind map from source across all tiers | Rewrite mind map differently per tier |

---

## Anti-Patterns

| Anti-pattern | Fix |
|-------------|-----|
| Creating EN pages but forgetting FR | Create all 4 in one pass |
| Writing the publication without a methodology file | Methodology first |
| Updating summary but not full page | Source drives both — sync from source |
| One giant commit with everything | Progressive commits: methodology → source → web pages |

---

## Completion

When deliverables are ready, follow the **Publication Completion Checklist** in `methodology/documentation-generation.md#publication-completion-checklist` — page creation, HTML redirects, viewer index registration, navigator data, parent index updates, and link registry. This applies to every publication produced by an interactive documentation session.

## Related

- Original: `packetqc/knowledge:knowledge/methodology/interactive-documentation.md`
- `methodology/documentation-generation.md` — Content standards, quality checklist, and publication completion checklist
- `methodology/documentation-audience.md` — 19-segment audience definition
