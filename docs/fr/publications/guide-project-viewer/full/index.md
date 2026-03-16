---
layout: publication
title: "Visualiseur projets — Guide utilisateur (Complet)"
pub_id: "Guide — Project Viewer"
version: "v1"
date: "2026-03-16"
lang: fr
permalink: /fr/publications/guide-project-viewer/full/
og_image: /assets/og/project-management-fr-cayman.gif
keywords: "guide, projets, visualiseur, boards, statut"
---

# Project Viewer — User Guide
{: #pub-title}

> **Interface**: [Project Viewer (I4)]({{ '/interfaces/project-viewer/' | relative_url }}) | [Summary version]({{ '/publications/guide-project-viewer/' | relative_url }})

## Table of Contents

| | |
|---|---|
| [Getting Started](#getting-started) | Open and orient yourself |
| [Overview — All Projects](#overview--all-projects) | Portfolio-level stats and cards |
| [Project Dashboard](#project-dashboard) | Single-project deep dive |
| [Board Integration](#board-integration) | GitHub Project boards |
| [Stage Distribution](#stage-distribution) | 8-stage workflow breakdown |
| [Knowledge Grid](#knowledge-grid) | Section-by-section scores |
| [Tasks Table](#tasks-table) | Browse and navigate tasks |
| [Project Types](#project-types) | Active, completed, paused, archived |
| [Print & Export](#print--export) | Portfolio reports |
| [Troubleshooting](#troubleshooting) | Common issues |

## Getting Started

The Project Viewer (I4) is a read-only portfolio dashboard for all registered Knowledge projects. It consolidates project metadata, task counts, PR metrics, stage distribution, knowledge grid scores, and GitHub board integration into a single interface.

**Opening the interface:**
- From the **Main Navigator** (I2): click *I4 Project Viewer* in the left panel
- Direct URL: `/interfaces/project-viewer/`

The interface loads project data from `docs/data/projects.json` and renders two views: an overview (all projects) and a dashboard (single project).

## Overview — All Projects

When no project is selected, the interface displays a portfolio overview:

**Stats cards** (top row):

| Card | Value |
|------|-------|
| Projects | Total registered projects |
| Tasks | Sum of all tasks across projects |
| PRs | Sum of all pull requests |
| Additions | Total lines added across all PRs |

**Project cards** (grid below stats):

Each card shows:
- Project title
- Task count and PR count
- Completion percentage with color-coded progress bar (blue < 40%, yellow 40–79%, green 80%+)
- Board link (opens GitHub Project board)
- Completion fraction (e.g., 12/15)

Click any card to open that project's dashboard, or use the dropdown selector at the top.

## Project Dashboard

Selecting a project reveals its dedicated dashboard with five sections:

### Header and Meta
- **Project title** as main heading
- **GitHub Board link** — direct link to the board on github.com
- **Task link** — the parent GitHub issue
- **Branch count** — number of branches associated with the project

### Stats Grid

Six metric cards:

| Metric | Description |
|--------|-------------|
| Tasks | Total tasks in the project |
| Completed | Tasks that reached the completion stage |
| PRs | Pull requests merged for this project |
| Additions | Lines of code added |
| Deletions | Lines of code removed |
| Files Changed | Number of files modified |

### Completion Bar

A horizontal progress bar with percentage label. Color coding:
- **Blue** — under 40%
- **Yellow** — 40% to 79%
- **Green** — 80% and above

## Board Integration

Each project can link to a GitHub Project board:

- **Board number** — the numeric ID displayed in the header (e.g., Board #38)
- **Direct link** — clicking opens `github.com` in a new tab
- **Task number** — the parent issue number linking the project to the repository
- Board data is read from the `board_url` and `board_number` fields in `projects.json`

Projects without a board link simply omit the board badge from the header.

## Stage Distribution

The stage distribution bar visualizes how tasks are distributed across the 8-stage workflow:

| Stage | Color | Description |
|-------|-------|-------------|
| Initial | Grey (#8b949e) | Task created, not yet started |
| Plan | Yellow (#bf8700) | Planning phase |
| Analyze | Blue (#0969da) | Analysis in progress |
| Implement | Purple (#8250df) | Implementation underway |
| Validation | Red (#cf222e) | Testing and validation |
| Documentation | Dark blue (#0550ae) | Documentation being written |
| Approval | Green (#1a7f37) | Awaiting or received approval |
| Completion | Bright green (#2da44e) | Task finished |

The bar is proportional — each segment's width represents the fraction of tasks at that stage. Segments wider than 10% display their count inline. A legend below the bar lists each active stage with its count.

## Knowledge Grid

The knowledge grid summary shows section-by-section completion scores for the project. Each section (e.g., architecture, conventions, documentation) contains sub-keys with individual percentage scores.

Color coding:
- **Green (gs-high)** — 75% and above
- **Yellow (gs-mid)** — 25% to 74%
- **Red (gs-low)** — below 25%

The grid is rendered as a CSS grid with section labels on the left and sub-key values across columns.

## Tasks Table

The tasks table lists all tasks belonging to the selected project:

| Column | Content |
|--------|---------|
| **#** | GitHub issue number (clickable link to the issue) |
| **Task** | Task title (truncated to 60 characters) |
| **Stage** | Current stage badge |
| **Progress** | Mini progress bar based on stage index (1–8) |
| **Changes** | Sub-task count |
| **Grid** | Message count |
| **Action** | "View" link — opens the task in the Task Workflow interface (I3) |

Clicking "View" navigates to `/interfaces/task-workflow/?task=<id>`, loading the task directly in I3.

## Project Types

Projects are categorized by status:

| Status | Meaning |
|--------|---------|
| **Active** | Work in progress — tasks being created and completed |
| **Completed** | All tasks finished, project delivered |
| **Paused** | Temporarily suspended, may resume later |
| **Archived** | Closed and preserved for reference |

The project dropdown lists all projects regardless of status. Use the overview cards to visually assess status via completion percentages.

## Print & Export

The interface includes print-optimized styles:

- **Cover page** — auto-generated with project title (or "Project Viewer" for overview), task/PR summary, board number, completion percentage, and generation date
- **Dashboard** — all sections render in print layout with proper page breaks
- **How to print** — Ctrl+P (Windows/Linux) or Cmd+P (macOS)

When a single project is selected, the cover page shows that project's data. When viewing the overview, it shows aggregate totals.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No projects listed | Check that `docs/data/projects.json` exists and is accessible |
| Board link broken | The GitHub Project board may have been deleted or made private |
| Progress shows 0% | No tasks have reached the completion stage yet |
| Stage bar empty | The project has no `stage_distribution` data in projects.json |
| Knowledge grid blank | No `grid_summary` data available for the project |
| Task "View" link fails | Ensure the Task Workflow interface (I3) is deployed at the expected path |

---

**[Launch Project Viewer (I4) →]({{ '/interfaces/project-viewer/' | relative_url }})**

*See also: [Project Management — Technical Publication]({{ '/publications/project-management/' | relative_url }})*

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
