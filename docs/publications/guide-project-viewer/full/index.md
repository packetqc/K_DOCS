---
layout: publication
title: "Project Viewer — User Guide (Full)"
description: "Complete user guide for the Project Viewer interface: project browsing, board integration, issue tracking, progress metrics, and export."
pub_id: "User Guide — I4 (Full)"
version: "v1"
date: "2026-03-16"
permalink: /publications/guide-project-viewer/full/
keywords: "user guide, project viewer, interface, tutorial, complete"
---

# Project Viewer — User Guide
{: #pub-title}

> **Interface**: [Project Viewer (I4)]({{ '/interfaces/project-viewer/' | relative_url }}) | [Summary version]({{ '/publications/guide-project-viewer/' | relative_url }})

## Table of Contents

| | |
|---|---|
| [Getting Started](#getting-started) | Open and orient yourself |
| [Project List](#project-list) | Browse all projects |
| [Project Detail](#project-detail) | Deep-dive into a project |
| [Board Integration](#board-integration) | GitHub Project boards |
| [Issue Tracking](#issue-tracking) | Linked issues and PRs |
| [Progress Metrics](#progress-metrics) | Completion tracking |
| [Export & Print](#export--print) | Portfolio reports |
| [Troubleshooting](#troubleshooting) | Common issues |

## Getting Started

The Project Viewer (I4) is a read-only portfolio dashboard for all registered Knowledge projects. It displays project metadata, GitHub board links, issue status, and progress indicators.

**Opening the interface:**
- From the **Main Navigator** (I2): click *I4 Project Viewer*
- Direct URL: `/interfaces/project-viewer/`

## Project List

The main dashboard shows all projects in a table or card layout:

| Column | Description |
|--------|------------|
| **P#** | Unique project identifier (e.g., P001) |
| **Title** | Project name |
| **Status** | Active, Completed, Paused, or Archived |
| **Board** | Link to GitHub Project board |
| **Issues** | Open / closed issue count |
| **Progress** | Visual progress bar |

## Project Detail

Click a project row to expand its detail view:
- **Description** — goals, scope, and deliverables
- **Team** — contributors and roles
- **Dates** — creation date, target completion
- **Milestone timeline** — key dates and checkpoints

## Board Integration

Each project can link to a GitHub Project board:
- **Board number** — the GitHub Project board ID
- **Direct link** — opens the board on github.com
- **Item count** — total items tracked on the board

## Issue Tracking

Issues linked to the project show:
- **Title** — issue name
- **State** — open, closed, or in progress
- **Labels** — categorization tags
- **Assignee** — who's working on it

## Progress Metrics

Progress is calculated from issue states:
- **Completion %** = closed issues / total issues
- **Progress bar** — visual indicator
- **Velocity** — issues closed per week (when data available)

## Export & Print

Use the browser's print function for portfolio reports. The interface generates a cover page with project summary.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No projects listed | Check that `docs/data/projects.json` exists |
| Board link broken | The GitHub Project board may have been deleted or made private |
| Progress shows 0% | No issues are linked to the project yet |

---

**[Launch Project Viewer (I4) →]({{ '/interfaces/project-viewer/' | relative_url }})**

*See also: [Project Management — Technical Publication]({{ '/publications/project-management/' | relative_url }})*

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
