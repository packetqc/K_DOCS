# Knowledge Audience Definition

> Adapted from `packetqc/knowledge:knowledge/methodology/methodology-documentation-audience.md`

*Formal audience segmentation for the Knowledge system — publications, success stories, web presence, and all outward-facing content.*

---

## Overview

Knowledge serves distinct audience segments across 5 tiers. The tiers reflect proximity to the system's core purpose: Tier 1 audiences are the people the system was built for; Tier 5 audiences discover it through community and open-source channels.

**The rewrite principle**: Technical depth is preserved — dates, metrics, architecture diagrams, code references. What changes is framing: every piece of outward-facing content must answer "why does this matter to someone who wasn't in the session?" before explaining what happened.

---

## Tier 1 — Primary (the system was built for them)

| Audience | What they seek |
|----------|----------------|
| **AI-assisted development practitioners** | How to make AI sessions persistent, productive, and self-healing. Replicable methodology. |
| **Embedded systems engineers** | Real-time debugging with AI, RTOS patterns, hardware-software co-design |
| **Solo developers / indie builders** | Force multiplication — how one engineer with AI matches a team |
| **Claude Code users (power users)** | Replicable patterns for their own Claude Code workflows |

## Tier 2 — Technical professionals

| Audience | What they seek |
|----------|----------------|
| **DevOps / Platform engineers** | Automated GitHub workflows, board management, cross-repo operations |
| **Security professionals** | Token lifecycle best practices, compliance, audit trail methodology |
| **System architects** | Self-sustaining distributed systems, bidirectional knowledge flow |
| **Knowledge management researchers** | Session persistence as organizational memory, AI-native knowledge management |
| **Technical writers** | Automated bilingual documentation pipelines, freshness tracking |
| **Project managers** | AI-augmented project lifecycle management, cross-project tracking |

## Tier 3 — Decision makers

| Audience | What they seek |
|----------|----------------|
| **Technical leaders / CTOs** | Evaluating AI-augmented engineering velocity. ROI evidence. |
| **Enterprise architects** | Governance patterns for AI tool adoption. Risk assessment. |
| **Startup founders** | Velocity multiplication with minimal headcount |

## Tier 4 — Academic / Research

| Audience | What they seek |
|----------|----------------|
| **AI researchers** | Novel patterns for persistent AI agents. Session memory. |
| **AI ethics / governance researchers** | Transparent failure documentation, self-correcting architecture |
| **Conference reviewers** | Novel approach to AI-human collaboration at scale |
| **Educators** | Course material on AI-assisted development |

## Tier 5 — Community

| Audience | What they seek |
|----------|----------------|
| **Open source builders** | Adapting the methodology for their own projects. Fork and go. |
| **Government / regulated industry** | Audit-ready AI tool usage. No cloud dependencies. |

---

## Content Voice Guidelines

### Principles

1. **Lead with why** — Before explaining what happened, tell the reader why it matters
2. **Keep all metrics** — Dates, commit counts, timing data. These are the proof.
3. **Keep all architecture** — Mermaid diagrams, technical details. These are the substance.
4. **Frame for outsiders** — The reader was not in the session. One sentence of context bridges the gap.
5. **Name the quality, explain the implication** — "The system is *persistent*" means nothing to a new reader. "Session notes survived across 3 sessions" tells them what it means.

---

## Application

This audience definition applies to:
- All publication abstracts and introductions
- Web presence (GitHub Pages) — landing pages, publications index
- Social sharing — webcard content, OG descriptions
- README.md — the first thing anyone reads after cloning

---

## Related

- Original: `packetqc/knowledge:knowledge/methodology/methodology-documentation-audience.md`
- `methodology/documentation-generation.md` — Content standards
- `methodology/interactive-documentation.md` — Session workflow
