---
layout: publication
title: "Story #23 — Knowledge v2.0: From Questionnaire to Living Engineering Platform"
description: "The evolution of Knowledge from a session validation questionnaire to a complete engineering platform with GitHub Project integration, task progression viewers, non-blocking persistence, and landscape-native interfaces."
pub_id: "Publication #11 — Story #23"
version: "v1"
date: "2026-03-08"
permalink: /publications/success-stories/story-23/
og_image: /assets/og/knowledge-2-en-cayman.gif
keywords: "success story, knowledge 2.0, GitHub Project, task progression, session viewer, non-blocking, persistence, landscape"
---

# Story #23 — Knowledge v2.0: From Questionnaire to Living Engineering Platform

> **Parent publication**: [#11 — Success Stories]({{ '/publications/success-stories/' | relative_url }})

---

<div class="story-section">

> *"The knowledge system started as a simple validation quiz. Now it manages GitHub Project boards, creates and links issues, persists everything locally when GitHub is down, shows task progression in real-time, and does it all without ever blocking the developer's flow. That's the v2.0 evolution."*

<div class="story-row">
<div class="story-row-left">

**Details**

</div>
<div class="story-row-right">

| | |
|---|---|
| Date | 2026-03-08 |
| Category | 🚀 ⚙️ 🏗️ |
| Context | Knowledge v2.0 began as a session questionnaire (A1-A4) validating user requests before execution. Over a single intense day, it evolved into a full engineering platform: GitHub Project board creation/validation integrated as a non-blocking precondition, issue creation with automatic board linking, local persistence for GitHub unavailability, a task progression viewer as the primary visual in the Task Workflow interface, modular session viewer with real-time knowledge grids, and landscape-native standalone interfaces. |
| Triggered by | The natural evolution of v2.0 during live integration testing. Each capability emerged from a real need: the user wanted project boards validated before issue creation, but only once execution launched (not during the menu phase where values can still change). The persistence pattern emerged from the principle that external system failures must never block local workflow. |
| Authored by | **Claude** (Anthropic, Opus 4.6) — from live session data |

</div>
</div>

## The Evolution Arc

What makes this story significant is not any single feature, but the **architectural coherence** that emerged across 30+ pull requests in a single day:

### 1. GitHub Project Board Integration

The `project_ensure()` function was created to validate or create GitHub Project boards. The key design decision: it runs as a **precondition at execution launch** (A4), not during the validation menu (A3). This matters because the user can change the project value before launching — running `project_ensure()` prematurely would be wasteful and potentially incorrect.

```
A3 detects repo -> user can modify -> execution launched -> project_ensure() -> issue creation -> project_item_add()
```

### 2. Non-Blocking Persistence Pattern

Every GitHub operation follows the same resilience pattern:

| Operation | Success | GitHub Unavailable |
|-----------|---------|-------------------|
| `project_ensure()` | Store `project_id`, `project_number` | Store `local_only: true`, sync later |
| `issue_create()` | Store `numero`, `url`, `node_id` | Store `titre`, `body` on disk |
| `project_item_add()` | Link created | Store `pending_board_link: true` |

The execution **never stops**. Data is persisted locally and synchronized at the next opportunity. This is the core principle: *the flow of work must not depend on external systems*.

### 3. Task Progression Viewer

The Task Workflow interface (I3) gained a persistent progression bar — visible immediately after selecting a task, above all view-specific content. Eight stages displayed as connected dots (completed/current/pending/skipped), with meta-data showing current stage, completion percentage, issue number, and date.

### 4. Session Viewer Modernization

The Session Review interface (I1) was rebuilt with a modular JavaScript architecture (session-core.js + session-blocks.js + session-print.js), auto-detection of repo context, and a knowledge validation grid with bilingual labels and pastel blue headers.

### 5. Landscape-Native Interfaces

All three interfaces (I1 Session Review, I2 Main Navigator, I3 Task Workflow) now default to landscape orientation in standalone mode. The `publication.html` layout detects `page_type: interface` and sets the default accordingly. Inside the Main Navigator iframe, the center panel always forces landscape on its content.

## Impact

| Metric | Value |
|--------|-------|
| Pull Requests | 30+ merged in a single day |
| New capabilities | 5 major (project board, non-blocking persistence, task progression, session viewer v2, landscape interfaces) |
| Files changed | 15+ across skills, interfaces, layouts, and scripts |
| Principle validated | External system independence — GitHub outages never block workflow |
| Version | v2.0 sub-version 2 |

## Qualities Demonstrated

<div class="story-row">
<div class="story-row-left">

**Validated**

</div>
<div class="story-row-right">

Autosuffisant (#1), Autonome (#2), Intuitif (#3), Concis (#4), Adaptable (#5), Intégré (#13)

</div>
</div>

</div>

## Related Publications

- [#0 — Knowledge 2.0]({{ '/publications/knowledge-2.0/' | relative_url }}) — Master publication
- [#11 — Success Stories]({{ '/publications/success-stories/' | relative_url }}) — Parent hub
- [#21 — Task Workflow State Machine]({{ '/publications/success-stories/story-21/' | relative_url }}) — Earlier task workflow story

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
