---
layout: publication
title: "Knowledge 2.0 — Interactive Intelligence Framework"
description: "Knowledge 2.0 introduces an Interactive Intelligence Framework — structured questionnaire, command routing, skill architecture, methodology deduplication, and three interactive working modes."
permalink: /publications/knowledge-2.0/full/
lang: en
permalink_fr: /fr/publications/knowledge-2.0/full/
header_title: "Knowledge 2.0"
tagline: "Interactive Intelligence Framework — Structured session onboarding, command routing, methodology deduplication, and three interactive working modes."
pub_meta: "Publication v1 — March 2026 | Martin Paquet & Claude (Opus 4.6)"
pub_version: "v2"
pub_number: 0
pub_date: "March 2026"
source_url: "https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/knowledge-2.0/v1"
og_image: /assets/og/knowledge-2-en-cayman.gif
citation: "Paquet, M. & Claude (2026). Knowledge 2.0: Interactive Intelligence Framework. packetqc/knowledge."
---

# Knowledge 2.0 — Interactive Intelligence Framework
{: #pub-title}

**Contents**

- [Authors](#authors)
- [Abstract](#abstract)
- [What's New in 2.0](#whats-new-in-20-)
- [The Evolution: v1 → v2](#the-evolution-v1--v2)
- [1. The Mindmap Memory](#1-the-mindmap-memory-)
- [2. The Session Questionnaire](#2-the-session-questionnaire)
- [3. The Command Router](#3-the-command-router)
- [4. The Skill Architecture](#4-the-skill-architecture)
- [5. Methodology Resolution](#5-methodology-resolution)
- [6. The Deduplication Engine](#6-the-deduplication-engine)
- [7. Interactive Modes](#7-interactive-modes)
- [8. Complete Architecture](#8-complete-architecture)
- [Legacy References — Knowledge 1.0](#legacy-references--knowledge-10-)

## Authors

**Martin Paquet** — Network security analyst programmer, network and system security administrator, and embedded software designer. Architect of Knowledge. Designed the persistence methodology, the distributed intelligence network, and the self-healing version-aware architecture. The insight behind Knowledge 2.0: session initialization is as critical as session persistence — a structured onboarding protocol replaces unstructured prompting.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Co-architect of the Interactive Intelligence Framework. Implemented the session questionnaire, command router, skill registry, methodology resolution, and deduplication engine. This publication documents a system built collaboratively across 100+ sessions.

---

## Abstract

Knowledge 1.0 solved **statelessness** — AI sessions that forget everything between conversations.

**Knowledge 2.0** solves the next problem: **session initialization chaos**. Even with persistent memory, every session starts with an unstructured prompt. Knowledge 2.0 introduces a structured questionnaire, deterministic command routing, composable skills, and methodology deduplication — so the session *understands what it's about to do* before doing it.

| Feature | Description |
|---------|-------------|
| **Session questionnaire** | Structured onboarding grid (A1–E3) validates context, extracts intent, confirms project scope. State persists on disk |
| **Command router** | `routes.json` maps user intent to programs deterministically — no AI interpretation |
| **Skill architecture** | `SkillRegistry` with composable units — self-contained and testable |
| **Methodology resolution** | Family-based loading — commands declare a family, get all matching files automatically |
| **Deduplication engine** | Session-level tracking — 66% reduction in methodology loading for multi-command sessions |
| **Interactive modes** | Three specialized sessions: Conception, Documentation, Diagnostic |
| **Checkpoint persistence** | Survives context compaction and crashes — automatic state recovery |
| **Work validation** | 5-block validation: Request (A), Quality (B), Integrity (C), Documentation (D), Approval (E) |

---

## What's New in 2.0 <span class="badge badge-new">NEW</span>

<div class="feature-grid">
<div class="feature-card">
<h4>Session Questionnaire</h4>
<p>Structured onboarding grid (A1–E3) validates context, extracts intent, and confirms project scope before work begins. State persists on disk.</p>
</div>
<div class="feature-card">
<h4>Command Router</h4>
<p><code>routes.json</code> maps user intent to programs deterministically. No AI interpretation — keywords trigger exact programs.</p>
</div>
<div class="feature-card">
<h4>Skill Architecture</h4>
<p><code>SkillRegistry</code> with composable units: <code>LireChoixSkill</code>, <code>FonctionSkill</code>, <code>ProgrammeSkill</code>. Self-contained and testable.</p>
</div>
<div class="feature-card">
<h4>Methodology Resolution</h4>
<p><code>resolve_methodologies(family)</code> scans by prefix. Commands declare a family, get all matching files. 6 families, 30 files.</p>
</div>
<div class="feature-card">
<h4>Deduplication Engine</h4>
<p>Session-level tracking: 2nd command in same family reads <strong>0 files</strong> instead of 9. 66% reduction in multi-command sessions.</p>
</div>
<div class="feature-card">
<h4>Interactive Modes</h4>
<p>Three specialized sessions: <strong>Conception</strong> (design), <strong>Documentation</strong> (content), <strong>Diagnostic</strong> (debugging). Each with its own phase pattern.</p>
</div>
</div>

## The Evolution: v1 → v2

```mermaid
flowchart LR
    subgraph V1["Knowledge 1.0"]
        direction TB
        P1["Session Persistence"]
        P2["Distributed Minds"]
        P3["Harvest Protocol"]
        P4["Version Tracking"]
    end

    subgraph V2["Knowledge 2.0"]
        direction TB
        Q1["Session Questionnaire"]
        Q2["Command Router"]
        Q3["Skill Architecture"]
        Q4["Methodology Resolution"]
        Q5["Deduplication Engine"]
        Q6["Interactive Modes"]
    end

    V1 -->|"builds on"| V2
```

<table class="comparison-table">
<thead>
<tr><th>Dimension</th><th>v1 <span class="badge badge-v1">1.0</span></th><th>v2 <span class="badge badge-new">2.0</span></th></tr>
</thead>
<tbody>
<tr><td><strong>Session start</strong></td><td class="v1">Unstructured prompt — AI guesses intent</td><td class="v2">Questionnaire validates context → routes to correct mode</td></tr>
<tr><td><strong>Command execution</strong></td><td class="v1">AI interprets natural language</td><td class="v2"><code>routes.json</code> maps to programs — deterministic</td></tr>
<tr><td><strong>Methodology loading</strong></td><td class="v1">Read everything on wakeup</td><td class="v2">Family-based resolution — load only what's needed</td></tr>
<tr><td><strong>Repeated commands</strong></td><td class="v1">Re-read all methodology files</td><td class="v2">Deduplication — 0 files on 2nd invocation</td></tr>
<tr><td><strong>Working modes</strong></td><td class="v1">One mode (work)</td><td class="v2">Three interactive modes + command mode</td></tr>
<tr><td><strong>Validation</strong></td><td class="v1">Manual</td><td class="v2">Knowledge grid (A1-D3)</td></tr>
<tr><td><strong>Crash recovery</strong></td><td class="v1">Notes + git history</td><td class="v2">Checkpoint files + status queries</td></tr>
</tbody>
</table>

## 1. The Mindmap Memory <span class="badge badge-new">NEW</span>

Knowledge 2.0 introduces a **three-file memory system** where a mermaid mindmap serves as the AI's operating memory — not decoration, but an executable knowledge graph that governs behavior every session.

### The Three-File System

| File | Role | Content |
|------|------|---------|
| `mind_memory.md` | **Core mind** | Mermaid mindmap — the subconscious. Every node is a directive Claude commits to follow. |
| `far_memory.json` | **Full recall** | Verbatim conversation history. Archived by topic when large. |
| `near_memory.json` | **Working memory** | Real-time summaries with pointers to far_memory and mind_memory. |

### Mind-First Strategy

The mindmap is read **first** at every session start, resume, and compaction recovery. One glance shows the entire knowledge state — branches represent behavioral categories:

- **architecture** nodes → System design rules. HOW you work.
- **constraints** nodes → Hard limits. BOUNDARIES you never violate.
- **conventions** nodes → Patterns and standards. HOW you execute.
- **work** nodes → Accomplished/staged results. STATE and continuity anchor.
- **session** nodes → Current context. WHAT you're doing now.

Claude walks the full tree and internalizes each node as a rule before proceeding with any task.

### Programs Over Improvisation

Claude-as-engine is the **bootstrap only** — new session, resume, compaction recovery. All mechanical operations use deterministic scripts:

| Script | Purpose |
|--------|---------|
| `memory_append.py` | Every turn: appends to far_memory + near_memory atomically |
| `far_memory_split.py` | Archives completed topics by subject (not by size) |
| `memory_recall.py` | Searches and loads archived memory by keyword |
| `session_init.py` | Initializes fresh sessions, preserves archives |
| `mindmap_filter.py` | Renders depth-filtered mindmap from config |
| `set_depth.py` | Human-editable depth control per branch |

Claude provides intelligence (summaries, topic names) as arguments to these programs. Architecture changes equal script updates — Claude maintains this coupling automatically.

### Depth-Configurable Display

The mindmap supports **normal** and **full** display modes. A `depth_config.json` file controls:

- **Default depth**: how many levels to show (default: 3)
- **Omit list**: branches hidden in normal mode (architecture, constraints)
- **Overrides**: per-branch depth settings for fine control

This enables a clean, focused view for daily work while preserving the full knowledge graph for deep inspection.

### Live Knowledge Graph

The mindmap below renders the current K_MIND memory in real-time — fetched from the repository and filtered by depth configuration.

<div id="k20-live-mindmap" style="width:100%;min-height:400px;border:1px solid var(--border,#d48a3c);border-radius:8px;background:var(--bg,#faf6f1);padding:1rem;overflow:auto;">
<div class="loading">Loading live mindmap...</div>
</div>
<script>
(function() {
  var RAW_BASE = 'https://raw.githubusercontent.com/packetqc/K_DOCS/main/Knowledge/K_MIND/';
  var container = document.getElementById('k20-live-mindmap');
  Promise.all([
    fetch(RAW_BASE + 'mind/mind_memory.md').then(function(r) { return r.ok ? r.text() : Promise.reject('HTTP ' + r.status); }),
    fetch(RAW_BASE + 'conventions/depth_config.json').then(function(r) { return r.ok ? r.json() : {default_depth:3,omit:['architecture','constraints'],overrides:{}}; }).catch(function() { return {default_depth:3,omit:['architecture','constraints'],overrides:{}}; })
  ]).then(function(res) {
    var match = res[0].match(/```mermaid\s*\n([\s\S]*?)```/);
    if (!match) throw new Error('No mermaid block');
    var code = match[1].trim();
    var lines = code.split('\n'), hdr = [], body = [], inH = true;
    for (var i = 0; i < lines.length; i++) {
      var s = lines[i].trim();
      if (inH && (s.indexOf('%%{') === 0 || s === 'mindmap' || s.indexOf('root(') !== -1)) hdr.push(lines[i]);
      else { inH = false; body.push(lines[i]); }
    }
    var cfg = res[1], nodes = [], out = [];
    for (var i = 0; i < body.length; i++) {
      if (!body[i].trim()) continue;
      var c = body[i].replace(/^\s+/,''), ind = body[i].length - c.length;
      nodes.push({l:Math.floor(ind/2),t:c,li:i});
    }
    if (nodes.length) {
      var ri = nodes[0].l, omit = cfg.omit||[], ov = cfg.overrides||{}, df = cfg.default_depth||3;
      for (var i = 0; i < nodes.length; i++) {
        var n = nodes[i], p = [], tg = n.l;
        for (var j = i; j >= 0; j--) { if (nodes[j].l < tg) { p.unshift(nodes[j].t); tg = nodes[j].l; } else if (j===i) p.push(nodes[j].t); }
        var path = p.join('/'), top = p[0]||n.t, dep = n.l - ri + 1, skip = false;
        for (var k = 0; k < omit.length; k++) if (top === omit[k]) { skip = true; break; }
        if (skip) continue;
        var mx = df, best = 0;
        for (var op in ov) { if ((path===op||path.indexOf(op+'/')===0)&&op.length>best) { best=op.length; mx=ov[op]; } }
        if (dep <= mx) out.push(body[n.li]);
      }
    }
    var filtered = hdr.join('\n') + '\n' + out.join('\n');
    container.innerHTML = '<div class="mermaid">' + filtered + '</div>';
    if (window.mermaid) mermaid.run({nodes:container.querySelectorAll('.mermaid')});
  }).catch(function(e) {
    container.innerHTML = '<p style="color:var(--muted);text-align:center;">Live mindmap unavailable</p>';
  });
})();
</script>

> [Full-screen Live Mindmap &#x2197;]({{ site.baseurl }}/interfaces/live-mindmap/)

### Real-Time Updates

Every conversation turn updates all three files:
1. **far_memory** captures the full verbatim exchange
2. **near_memory** records a one-line summary with pointers
3. **mind_memory** nodes are updated when knowledge structure changes

Topic splitting archives completed conversations by subject. Any memory can be recalled by keyword at any time — the system never forgets.

## 2. The Session Questionnaire

Every session begins with a structured validation grid — replacing unstructured guessing with a deterministic protocol.

| Knowledge | ID | Question | Action Type |
|-----------|----|----------|-------------|
| **A — Request Validation** | A1 | Confirm the title | function |
| | A2 | Confirm the description | program |
| | A3 | Confirm the project | function |
| | A4 | Execute request | executer_demande |
| **B — Work Quality** | B1 | Tests and build | program |
| | B2 | Code review | function |
| | B3 | Metrics | program |
| | B4 | All | all |
| **C — Session Integrity** | C1 | Progressive commits | function |
| | C2 | Cache up to date | program |
| | C3 | Issue commented | function |
| | C4 | All | all |
| **D — Documentation** | D1 | System documentation | function |
| | D2 | User documentation | function |
| | D3 | All | all |
| **E — Approval** | E1 | Pre-save summary | function |
| | E2 | Final save | program |
| | E3 | All | all |

> **Persistence**: State saved in `.claude/knowledge_resultats.json`. Survives compaction and crashes. After recovery: `en_cours: true` → resume, `demande_executee: true` → skip re-execution.

## 3. The Command Router

Commands are **routed**, not interpreted. `routes.json` maps keywords to programs.

```mermaid
flowchart LR
    INPUT["User prompt"] --> MATCH{"Keyword match?"}
    MATCH -->|Yes| ROUTE["Route found"]
    MATCH -->|No| CLAUDE["Claude handles naturally"]
    ROUTE --> PROG{"Has program?"}
    PROG -->|Yes| EXEC["Execute program"]
    PROG -->|No| MODE["Enter mode (interactive)"]
```

| Route | Syntax | Program | Type |
|-------|--------|---------|------|
| `project-create` | `project create [title]` | `scripts/project_create.py` | Command |
| `interactive` | `interactif` | — | Mode switch |

## 4. The Skill Architecture

Knowledge is decomposed into composable **skills** — each a self-contained unit registered in `SkillRegistry`.

| Skill | Role | Used By |
|-------|------|---------|
| `LireChoixSkill` | Read user choice (1-N) | Questionnaire navigation |
| `FonctionSkill` | Execute internal function | A1, A3, B2, C1, C3 |
| `ProgrammeSkill` | Execute external program | A2, B1, B3, C2 |

```
KnowledgeSkill → registre.executer("lire_choix") → LireChoixSkill
               → registre.executer("fonction")   → FonctionSkill
               → registre.executer("programme")  → ProgrammeSkill
```

## 5. Methodology Resolution

Commands declare a **family**, the system resolves all matching methodology files automatically.

| Family Prefix | Files | Used By |
|---------------|-------|---------|
| `documentation` | 6 files | pub new, pub check, docs check |
| `interactive` | 4 files | interactif, live, normalize |
| `system` | 5 files | Infrastructure commands |
| `satellite` | 2 files | bootstrap, satellite commands |
| `project` | 2 files | project create, project manage |
| `compilation` | 2 files | Metrics and time tracking |

## 6. The Deduplication Engine

```mermaid
flowchart LR
    CMD["Command (family: interactive)"] --> RESOLVE["resolve_methodologies() → 4 files"]
    RESOLVE --> FILTER["filter_unread() → check cache"]
    FILTER --> READ["Read only new files"]
    READ --> MARK["mark_read() → update cache"]
```

| Scenario | Without Dedup | With Dedup |
|----------|--------------|------------|
| 1st interactive command | 7 files read | 7 files read |
| 2nd interactive command | 7 files read | **0 files read** |
| 3rd interactive command | 7 files read | **0 files read** |
| **Total for 3 commands** | **21 file reads** | **7 file reads** |

> **66% reduction** in methodology loading for multi-command sessions.

## 7. Interactive Modes

<div class="feature-grid">
<div class="feature-card">
<h4>Conception</h4>
<p>Design new capabilities, explore architectures, prototype features. Phase: Anchor → Ideate → Explore → Propose → Prototype → Validate → Iterate → Formalize → Deliver.</p>
</div>
<div class="feature-card">
<h4>Documentation</h4>
<p>Create publications, methodologies, system docs. Phase: Assess → Structure → Draft → Review → Finalize.</p>
</div>
<div class="feature-card">
<h4>Diagnostic</h4>
<p>Live debugging, real-time analysis, forensic investigation. Phase: Observe → Hypothesize → Test → Fix → Verify.</p>
</div>
</div>

## 8. Complete Architecture

```mermaid
flowchart LR
    BOOT["Boot<br/>CLAUDE.md + checkpoints"] --> Q["Questionnaire<br/>A·B·C·D validation"]
    Q --> ENGINE["Engine<br/>Router → Skills → Executor"]
    ENGINE --> METH["Methodologies<br/>6 families · dedup"]
    METH --> MODES["Modes<br/>Conception · Docs · Diagnostic"]
```

---

<div class="annex-section" markdown="1">

## Legacy References — Knowledge 1.0 <span class="badge badge-legacy">v1</span>

> **[Knowledge v1 — Self-Evolving AI Engineering Intelligence](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/knowledge-system/v1)** — The 825-line master publication. Session persistence, distributed minds, core qualities, memory architecture, satellite network, and 26 versions of evolution in 5 days.

### Child Publications

| # | Publication | Links |
|---|-------------|-------|
| 0 | Knowledge System (Master) | [Source](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/knowledge-system/v1) · [Web]({{ site.baseurl }}/publications/knowledge-system/) |
| 1 | MPLIB Storage Pipeline | [Source](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/mplib-storage-pipeline/v1) · [Web]({{ site.baseurl }}/publications/mplib-storage-pipeline/) |
| 2 | Live Session Analysis | [Source](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/live-session-analysis/v1) · [Web]({{ site.baseurl }}/publications/live-session-analysis/) |
| 3 | AI Session Persistence | [Source](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/ai-session-persistence/v1) · [Web]({{ site.baseurl }}/publications/ai-session-persistence/) |
| 4 | Distributed Minds | [Source](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/distributed-minds/v1) · [Web]({{ site.baseurl }}/publications/distributed-minds/) |
| 4a | Knowledge Dashboard | [Source](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/distributed-knowledge-dashboard/v1) · [Web]({{ site.baseurl }}/publications/distributed-knowledge-dashboard/) |
| 5 | Webcards & Social Sharing | [Source](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/webcards-social-sharing/v1) · [Web]({{ site.baseurl }}/publications/webcards-social-sharing/) |
| 6 | Normalize | [Source](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/normalize-structure-concordance/v1) · [Web]({{ site.baseurl }}/publications/normalize-structure-concordance/) |
| 7 | Harvest Protocol | [Source](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/harvest-protocol/v1) · [Web]({{ site.baseurl }}/publications/harvest-protocol/) |
| 8 | Session Management | [Source](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/session-management/v1) · [Web]({{ site.baseurl }}/publications/session-management/) |
| 9 | Security by Design | [Source](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/security-by-design/v1) · [Web]({{ site.baseurl }}/publications/security-by-design/) |
| 10 | Live Knowledge Network | [Source](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/live-knowledge-network/v1) · [Web]({{ site.baseurl }}/publications/live-knowledge-network/) |

### Key v1 Sections

| Topic | What it covers |
|-------|---------------|
| [Core Qualities](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/knowledge-system/v1#core-qualities) | 11 principles — self-sufficient, autonomous, concordant, concise, interactive, evolutionary, distributed, persistent, recursive, secure, resilient |
| [Knowledge Evolution](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/knowledge-system/v1#knowledge-evolution) | v1→v26 timeline — 26 versions in 5 days |
| [Memory Architecture](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/knowledge-system/v1#memory-architecture) | Auto-memory vs Knowledge, compaction survival, context window mechanics |
| [Satellite Network](https://github.com/packetqc/knowledge/tree/main/knowledge/data/publications/knowledge-system/v1#satellite-harvest--what-the-network-produced) | 6 satellites, harvest results, 12 promotion candidates |

> **Note**: All publications are now unified in `packetqc/knowledge`. Knowledge 2.0 served as the integration test for this migration.

</div>
