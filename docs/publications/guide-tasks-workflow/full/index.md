---
layout: publication
title: "Tasks Workflow — User Guide (Full)"
description: "Complete user guide for the Tasks Workflow interface: stage progression, validation gates, views, export, and troubleshooting."
pub_id: "User Guide — I3 (Full)"
version: "v1"
date: "2026-03-16"
permalink: /publications/guide-tasks-workflow/full/
keywords: "user guide, tasks workflow, interface, tutorial, complete"
---

# Tasks Workflow — User Guide
{: #pub-title}

> **Interface**: [Tasks Workflow (I3)]({{ '/interfaces/task-workflow/' | relative_url }}) | [Summary version]({{ '/publications/guide-tasks-workflow/' | relative_url }})

## Table of Contents

| | |
|---|---|
| [Getting Started](#getting-started) | Open and orient yourself |
| [Task Selector](#task-selector) | Choose and filter tasks |
| [Dashboard View](#dashboard-view) | Overview of all tasks |
| [Detail View](#detail-view) | Full task information |
| [Validation View](#validation-view) | Compliance and test results |
| [Workflow Stages](#workflow-stages) | The 8-stage lifecycle |
| [Export & Print](#export--print) | PDF output |
| [Troubleshooting](#troubleshooting) | Common issues |

## Getting Started

The Tasks Workflow interface (I3) visualizes task progression through an 8-stage lifecycle. It's the default interface loaded in the center panel of the Main Navigator.

**Opening the interface:**
- From the **Main Navigator** (I2): click *I3 Tasks Workflow* in the Interfaces section
- Direct URL: `/interfaces/task-workflow/`

## Task Selector

**Task dropdown** — Lists all tracked tasks. Select *All Tasks* for the dashboard.

**View dropdown** — Three views:
- *Dashboard* — aggregate overview
- *Detail* — individual task deep-dive
- *Validation* — compliance focus

## Dashboard View

The dashboard shows:
- **Stage distribution** — how many tasks are in each stage
- **Progress bars** — visual progression per task
- **Recent activity** — latest stage transitions
- **Completion rate** — percentage of tasks reaching DONE

## Detail View

Select a specific task to see:
- **Metadata** — task ID, title, creation date, assignee
- **Stage history** — chronological list of stage transitions with timestamps
- **Related issues** — linked GitHub issues and PRs
- **Deliverables** — files, commits, and artifacts produced

## Validation View

Shows compliance and quality data:
- **Validation gates** — which gates passed/failed for each stage transition
- **Test status** — unit test results if applicable
- **Protocol compliance** — adherence to engineering cycle requirements

## Workflow Stages

| # | Stage | Entry Condition | Exit Gate |
|---|-------|----------------|-----------|
| 1 | **INITIAL** | Task received | Classification complete |
| 2 | **CLASSIFIED** | Engineering type set | Plan created |
| 3 | **PLANNED** | Plan approved | Work started |
| 4 | **IN_PROGRESS** | Active development | Implementation complete |
| 5 | **REVIEW** | Code/work review | All checks pass |
| 6 | **VALIDATED** | Validation passed | Commit and push |
| 7 | **DELIVERED** | Pushed to remote | Metrics recorded |
| 8 | **DONE** | Task closed | — |

Tasks can move backward (e.g., REVIEW → IN_PROGRESS if issues found).

## Export & Print

The interface supports print/PDF export:
1. Use Ctrl+P / Cmd+P
2. Cover page auto-generated with task summary
3. Select PDF as destination

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No tasks listed | Check that `docs/data/tasks.json` exists and contains task data |
| Stage shows as unknown | Task may use a legacy stage name from before the 8-stage model |
| Progress bars empty | Ensure tasks have stage transition timestamps |

---

**[Launch Tasks Workflow (I3) →]({{ '/interfaces/task-workflow/' | relative_url }})**

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
