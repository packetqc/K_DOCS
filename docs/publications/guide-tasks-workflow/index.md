---
layout: publication
title: "Tasks Workflow — User Guide"
description: "How to use the Tasks Workflow interface: track task progression through workflow stages, view validation results, and monitor completion."
pub_id: "User Guide — I3"
version: "v1"
date: "2026-03-16"
permalink: /publications/guide-tasks-workflow/
keywords: "user guide, tasks workflow, interface, stages, validation"
---

# Tasks Workflow — User Guide
{: #pub-title}

> **Interface**: [Tasks Workflow (I3)]({{ '/interfaces/task-workflow/' | relative_url }})

**Contents**

| | |
|---|---|
| [Getting Started](#getting-started) | Open the interface and select a task |
| [Task Selector](#task-selector) | Choose and filter tasks |
| [Workflow Stages](#workflow-stages) | The 8 stages from Initial to Done |
| [Views](#views) | Dashboard, Detail, and Validation |

## Getting Started

The Tasks Workflow interface tracks every task through its lifecycle — from initial receipt to completion. Each task progresses through defined stages with validation gates.

**To open it:**
- From the **Main Navigator**: click *I3 Tasks Workflow* in the left panel
- Direct URL: `/interfaces/task-workflow/`
- It loads as the default interface in the center panel

## Task Selector

Two dropdown controls:

1. **Task** — select a specific task or *All Tasks* for the dashboard overview
2. **View** — switch between Dashboard, Detail, or Validation views

## Workflow Stages

Tasks progress through 8 stages:

| Stage | Description |
|-------|------------|
| **INITIAL** | Task received, not yet classified |
| **CLASSIFIED** | Engineering type determined |
| **PLANNED** | Implementation plan approved |
| **IN_PROGRESS** | Active development |
| **REVIEW** | Code review and validation |
| **VALIDATED** | All checks passed |
| **DELIVERED** | Committed and pushed |
| **DONE** | Task closed, metrics recorded |

Each transition requires specific conditions to be met (validation gates).

## Views

- **Dashboard** — overview of all tasks with stage distribution and progress bars
- **Detail** — full task information: metadata, stage history, related issues
- **Validation** — validation results, test status, and compliance checks

---

**[Launch Tasks Workflow (I3) →]({{ '/interfaces/task-workflow/' | relative_url }})**
