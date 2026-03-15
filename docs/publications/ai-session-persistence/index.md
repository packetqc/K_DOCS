---
layout: publication
title: "AI Session Persistence — Cross-Session Knowledge Continuity for AI-Assisted Engineering"
description: "Methodology giving AI coding assistants durable cross-session memory using CLAUDE.md + notes/ + lifecycle protocol. 30-second context recovery vs 15 minutes manual re-explain. Inspired by RTOS thread architecture."
pub_id: "Publication #3"
version: "v1"
date: "2026-02-19"
permalink: /publications/ai-session-persistence/
og_image: /assets/og/ai-persistence-en-cayman.gif
keywords: "session persistence, Free Guy, NPC, awareness, notes, wakeup, sunglasses"
---

# AI Session Persistence — Cross-Session Knowledge Continuity for AI-Assisted Software Engineering
{: #pub-title}

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Session persistence methodology overview |
| [The Three Components](#the-three-components) | CLAUDE.md, notes/, and lifecycle protocol |
| [Measured Results](#measured-results) | 30-second recovery vs 15-minute re-explain |
| [The RTOS Analogy](#the-rtos-analogy) | Sessions as threads, notes as shared memory |
| [Portable — And Self-Demonstrating](#portable--and-self-demonstrating) | One-line bootstrap for any project |

## Abstract

AI coding assistants operate in stateless sessions — each conversation starts from zero. For sustained engineering projects spanning days or weeks, this is a critical limitation.

This publication documents a **session persistence methodology** that gives AI coding assistants durable cross-session memory using three components: a project instruction file (`CLAUDE.md`), a session notes directory (`notes/`), and a lifecycle protocol (init → work → save).

**This repository is itself the proof.** The knowledge you are reading was distilled across multiple sessions, persisted to files, and is now readable by any Claude instance — anywhere, anytime.

## The Three Components

| Component | Role | Analogy |
|-----------|------|---------|
| **CLAUDE.md** | Project identity, conventions, rules | Constitution |
| **notes/** | Decisions, discoveries, status per session | Journal |
| **Lifecycle** | init (read) → work (append) → save (persist) | RTOS thread lifecycle |

## Measured Results

| Method | Time to full context | Quality |
|--------|---------------------|---------|
| No persistence (re-explain manually) | 10–15 minutes | Partial |
| **Full methodology (CLAUDE.md + notes/)** | **~30 seconds** | **Complete** |

## The RTOS Analogy

The methodology was designed by a developer who recognized that AI sessions are structurally identical to **RTOS threads**: they need isolated context, shared memory regions (notes/), and explicit lifecycle management (init/cleanup).

| RTOS Concept | AI Session Equivalent |
|--------------|----------------------|
| Thread | Single Claude Code session |
| Shared memory (PSRAM) | `notes/` directory |
| Thread init | `wakeup` command |
| Thread cleanup | `save` command |

## Portable — And Self-Demonstrating

The `knowledge` repo is the portable brain. Any new project references it:

```markdown
## Knowledge Base
Read https://github.com/packetqc/knowledge for methodology, commands, and patterns.
```

One sentence. Full bootstrap. Every Claude instance gets the playbook.

---

[**Read the full documentation →**]({{ '/publications/ai-session-persistence/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
