---
layout: publication
title: "Session Review — User Guide (Full)"
description: "Complete user guide for the Session Review interface: navigation, metrics interpretation, export, and advanced usage."
pub_id: "User Guide — I1 (Full)"
version: "v1"
date: "2026-03-16"
permalink: /publications/guide-session-review/full/
keywords: "user guide, session review, interface, tutorial, complete"
---

# Session Review — User Guide
{: #pub-title}

> **Interface**: [Session Review (I1)]({{ '/interfaces/session-review/' | relative_url }}) | [Summary version]({{ '/publications/guide-session-review/' | relative_url }})

## Table of Contents

| | |
|---|---|
| [Getting Started](#getting-started) | Open and orient yourself |
| [Session Selector](#session-selector) | Choose and filter sessions |
| [Summary Section](#summary-section) | Goals, context, outcome |
| [Metrics Dashboard](#metrics-dashboard) | Charts and indicators |
| [Time Compilation](#time-compilation) | Duration and allocation |
| [Deliveries](#deliveries) | Files, commits, artifacts |
| [Lessons Learned](#lessons-learned) | Process improvements |
| [Export & Print](#export--print) | PDF and print options |
| [Troubleshooting](#troubleshooting) | Common issues |

## Getting Started

The Session Review interface (I1) is a read-only viewer for completed work sessions. Each session captures everything that happened during a conversation: what was accomplished, how long it took, what tools were used, and what was learned.

**Opening the interface:**
- From the **Main Navigator** (I2): click *I1 Session Review* in the Interfaces section
- Direct URL: `/interfaces/session-review/`
- The interface loads in the center panel of the navigator

## Session Selector

Two dropdown controls at the top:

**Session dropdown** — Lists all available sessions by date and title (newest first). Select *All Sessions* to see an overview across all sessions.

**View dropdown** — Filter the display:
- *All sections* — complete session report
- *Tasks Overview* — focus on task progression
- *Metrics Dashboard* — charts and numbers only
- *Timeline* — chronological message flow

> **Note**: Only sessions from version 52+ (2026-02-27 onwards) appear. Earlier sessions lack structured protocol data.

## Summary Section

The summary provides a quick overview:
- **Session goals** — what the session set out to accomplish
- **Context** — project, branch, starting state
- **Outcome** — what was achieved, what remains

## Metrics Dashboard

Visual charts showing session productivity:
- **Message counts** — user messages, assistant responses, tool calls
- **Tool usage** — which tools were used and how often
- **Productivity indicators** — tasks completed, files modified, commits created

Charts are interactive — hover for exact values.

## Time Compilation

Detailed time tracking:
- **Total duration** — start to end
- **Active time** — time between messages (excludes idle)
- **Time per task** — how long each task took
- **Time allocation** — pie chart showing time distribution across activities

## Deliveries

Everything the session produced:
- **Files created** — new files added to the repository
- **Files modified** — existing files changed
- **Commits** — git commits with messages
- **Artifacts** — publications, diagrams, scripts, or other outputs

## Lessons Learned

Process insights captured during the session:
- **What worked well** — patterns to repeat
- **What didn't work** — mistakes or blockers
- **Process improvements** — suggestions for future sessions

## Export & Print

The interface supports print-optimized output:
1. Use the browser's print function (Ctrl+P / Cmd+P)
2. A cover page is automatically generated
3. Charts render as static images in print
4. Select *PDF* as destination for digital export

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No sessions listed | Check that `docs/data/sessions.json` exists and is not empty |
| Session shows empty sections | The session may have been interrupted before the pre-save summary |
| Charts don't render | Ensure JavaScript is enabled; try a hard refresh (Ctrl+Shift+R) |
| Data seems outdated | Session data is refreshed at end of each work session, not in real time |

---

**[Launch Session Review (I1) →]({{ '/interfaces/session-review/' | relative_url }})**

*See also: [Session Review — Technical Publication]({{ '/publications/session-review/' | relative_url }})*

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
