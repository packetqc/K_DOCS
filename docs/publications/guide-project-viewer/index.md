---
layout: publication
title: "Project Viewer — User Guide"
pub_id: "Guide — Project Viewer"
version: "v1"
date: "2026-03-16"
permalink: /publications/guide-project-viewer/
og_image: /assets/og/project-management-en-cayman.gif
keywords: "guide, projects, viewer, boards, status"
---

# Project Viewer — User Guide
{: #pub-title}

> **Interface**: [Project Viewer (I4)]({{ '/interfaces/project-viewer/' | relative_url }}) | [Full version]({{ '/publications/guide-project-viewer/full/' | relative_url }})

**Contents**

| | |
|---|---|
| [Getting Started](#getting-started) | Open the interface and orient yourself |
| [Overview — All Projects](#overview--all-projects) | Portfolio-level stats and project cards |
| [Project Dashboard](#project-dashboard) | Single-project deep dive |
| [Board Integration](#board-integration) | GitHub Project boards |
| [Status Tracking](#status-tracking) | Stage distribution and completion |
| [Tips](#tips) | Productivity shortcuts |

## Getting Started

The Project Viewer is a read-only portfolio dashboard for all registered Knowledge projects. It displays project metadata, task counts, PR metrics, stage distribution, knowledge grid scores, and GitHub board links — all from a single dropdown selector.

**To open it:**
- From the **Main Navigator** (I2): click *I4 Project Viewer* in the left panel
- Direct URL: `/interfaces/project-viewer/`

## Overview — All Projects

When no project is selected (default view), the interface shows:

- **Stats cards** — total projects, total tasks, total PRs, total additions
- **Project cards** — one card per project with title, task count, PR count, completion percentage, progress bar, and board link

Click any card to open the project dashboard.

## Project Dashboard

Select a project from the dropdown (or click a card) to see its dedicated dashboard:

| Section | Content |
|---------|---------|
| **Header** | Project title, GitHub board link, task link, branch count |
| **Stats grid** | Tasks, completed tasks, PRs, additions, deletions, files changed |
| **Completion bar** | Visual progress indicator with percentage |
| **Stage distribution** | Color-coded bar showing tasks per stage |
| **Knowledge grid** | Section-by-section completion percentages |
| **Tasks table** | All project tasks with stage, progress, and link to Task Workflow |

## Board Integration

Each project can link to a GitHub Project board:
- **Board number** displayed in the project header
- **Direct link** opens the board on github.com in a new tab
- **Task link** — the parent GitHub issue for the project

## Status Tracking

The stage distribution bar breaks down tasks across the 8-stage workflow:

| Stage | Color |
|-------|-------|
| Initial | Grey |
| Plan | Yellow |
| Analyze | Blue |
| Implement | Purple |
| Validation | Red |
| Documentation | Dark blue |
| Approval | Green |
| Completion | Bright green |

A legend below the bar shows counts per stage.

## Tips

- **Project dropdown** — switch between projects instantly; select "All Projects" to return to the overview
- **Print** — Ctrl+P / Cmd+P generates a cover page with project summary, then the full dashboard
- **Task links** — click "View" in the tasks table to open a task in the Task Workflow (I3)
- **Bilingual** — the interface auto-detects EN/FR from the page URL

---

**[Launch Project Viewer (I4) →]({{ '/interfaces/project-viewer/' | relative_url }})**

*See also: [Project Management — Technical Publication]({{ '/publications/project-management/' | relative_url }})*
