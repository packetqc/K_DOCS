---
layout: publication
title: "Session Review — User Guide (Full)"
description: "Complete user guide for the Session Review interface: detailed walkthrough of every section, metrics interpretation, chart reading, timeline analysis, and export tips."
pub_id: "Guide — Session Review — Full"
version: "v1"
date: "2026-03-16"
permalink: /publications/guide-session-review/full/
og_image: /assets/og/session-review-en-cayman.gif
keywords: "guide, session, review, metrics, charts, timeline, user guide, complete, walkthrough"
---

# Session Review — User Guide (Full)
{: #pub-title}

> **Summary**: [Session Review — User Guide]({{ '/publications/guide-session-review/' | relative_url }})

**Contents**

| | |
|---|---|
| [Overview](#overview) | What Session Review does |
| [Opening the Interface](#opening-the-interface) | Where to find it and how to launch |
| [The Toolbar](#the-toolbar) | Session selector and view filter |
| [All Sessions View](#all-sessions-view) | Overview cards when no session is selected |
| [Session Report Sections](#session-report-sections) | Detailed guide to each section |
| [Reading the Charts](#reading-the-charts) | How to interpret pie charts and gauges |
| [Understanding the Dropdown](#understanding-the-dropdown) | Date grouping, time prefix, emoji indicators |
| [Data Source Modes](#data-source-modes) | Static vs. real-time data |
| [Tips and Best Practices](#tips-and-best-practices) | Getting the most from the interface |

---

## Overview

Session Review (I1) is the primary interface for reviewing knowledge system work sessions. It transforms structured session data into an interactive, multi-section report. Each session captures:

- **What** was accomplished (summary, tasks, deliveries)
- **How much** was produced (metrics: PRs, files, lines, commits)
- **How long** it took (time compilation with category breakdowns)
- **What was learned** (lessons, decisions, methodology insights)

The interface is read-only — it displays session data but does not modify it.

---

## Opening the Interface

You can access Session Review in two ways:

1. **Direct URL** — navigate to the Session Review page on the published site
2. **From Main Navigator (I2)** — click the Session Review link in the left panel; it loads inside the center frame

When embedded in the Main Navigator, the info button (blue circle with "i") opens this guide in a new panel.

---

## The Toolbar

The toolbar at the top of the interface contains two controls:

### Session Selector

The first dropdown lists all available sessions. Selecting a session loads its full report. Selecting "All Sessions" shows the overview with summary cards.

### View Filter

The second dropdown filters which sections are displayed:

| View | Sections Shown |
|------|----------------|
| **All sections** | Every section in sequence |
| **Tasks Overview** | Tasks, related tasks, collateral tasks, and task progression |
| **Metrics Dashboard** | Metrics table and pie charts |
| **Timeline** | Time compilation with time-block breakdown |

Use the view filter to focus on what matters to you without scrolling past unrelated sections.

---

## All Sessions View

When no individual session is selected, the interface displays:

- **Aggregate statistics** — total sessions, total PRs, total active time across all sessions
- **Session cards** — one card per session showing title, date, type, and key metrics

This is useful for getting a quick sense of recent activity or finding a specific session to drill into.

---

## Session Report Sections

Each session report contains the following sections, displayed in order:

### 1. Summary

The top section shows the session header:

- **Title** — what the session was about
- **Badges** — session type (work, fix, exploration), request type, engineering stage
- **Date and branch** — when the session happened and which Git branch was used
- **Description** — a brief summary of what was accomplished
- **Stat cards** — 8 metric blocks showing key numbers at a glance (PRs, files, lines added, lines removed, commits, tasks, lessons, active time)

### 2. Metrics Compilation

A detailed table breaking down the session's quantified output by category:

| Column | Meaning |
|--------|---------|
| **Category** | The area of work (e.g., knowledge, interface, scripts) |
| **Pull Requests** | Number of PRs in this category |
| **+/-** | Lines added and removed |
| **Files** | Number of files modified |
| **Commits** | Number of commits |
| **Tasks** | Related tasks |
| **Lessons** | Lessons recorded in this category |

A totals line above the table summarizes the session's overall output.

### 3. Pie Charts

Visual breakdowns displayed as pie charts:

- **Scope** — distribution of work across categories
- **Metrics** — proportional view of PRs, files, commits
- **Lines** — additions vs. removals
- **Time** — allocation across time categories

Charts appear only when the session has enough data to make them meaningful.

### 4. Time Compilation

The time section shows:

- **Total active time** and **total calendar time**
- **Time blocks** — individual work periods with start/end times and category labels
- **Three-slice breakdown**: Machine time (AI working), Human time (user interaction), and Inactive time (pauses, context switches)

This section is valuable for understanding how time was actually spent during a session, not just the wall-clock duration.

### 5. Deliveries

A table listing every pull request created during the session:

| Column | Meaning |
|--------|---------|
| **Pull Request** | PR title |
| **+/-** | Lines added and removed |
| **Files** | Number of files in the PR |
| **Commits** | Number of commits |
| **Link** | Direct link to the PR on GitHub |

### 6. Related Tasks

If the session is linked to tasks (from the task workflow system), they appear here with their type and title.

### 7. Lessons & Decisions

A list of insights captured during the session: methodology compliance observations, discovered patterns, pitfalls encountered, and decisions made. If no lessons were recorded, a placeholder message is shown.

### 8. Additional Sections

Depending on the session, you may also see:

- **Collateral Tasks** — unplanned tasks that emerged during the session
- **Session Tasks** — tasks tracked within the session with progress indicators
- **Task Progression** — visual timeline of how tasks advanced
- **Velocity & Code Impact** — gauges and charts showing coding speed and impact metrics

---

## Reading the Charts

### Pie Charts

Each pie chart shows proportional distribution. Hover over a slice to see the exact value and percentage. The legend below the chart identifies each slice by color and label.

### Velocity Gauges

When available, velocity gauges show coding speed metrics as dial indicators. These compare the session's output rate against historical baselines.

### Code Impact Chart

The impact chart (when available) shows additions vs. removals as a bar chart, giving a visual sense of whether the session was additive (new features) or subtractive (cleanup, refactoring).

---

## Understanding the Dropdown

The session dropdown has several features designed to help you find sessions quickly:

### Date Grouping

Sessions are grouped by **local date** (your browser's timezone). This means a session you worked on in the evening will appear under today's date, even if the UTC timestamp crosses into the next day.

### Time Prefix

Each entry starts with the session's **start time** — the time of the first PR. This makes it natural to identify sessions: "the one I started at 10:30 AM."

### Emoji Indicators

Small emoji suffixes tell you what data is available before you even select a session:

| Emoji | Meaning |
|-------|---------|
| Deliveries | Has pull request data |
| Notes | Has session notes |
| Issue | Has a linked GitHub issue |

---

## Data Source Modes

The interface supports two data modes, indicated by a banner at the top:

- **Static mode** (default) — data is loaded from a pre-generated JSON file, refreshed at the end of each work session. This is the standard mode on GitHub Pages.
- **Real-time mode** — when connected via GitHub OAuth2, session data is fetched live from the GitHub API. This mode shows the most current data but requires authentication.

---

## Tips and Best Practices

- **Use the view filter** to jump directly to the section you care about — especially useful on mobile where scrolling through all sections takes time
- **Check the emoji indicators** in the dropdown before selecting a session to know what data is available
- **Compare sessions** by opening multiple browser tabs, each with a different session selected
- **Time compilation** is the best section for understanding productivity — it shows actual active time, not just when the session started and ended
- **Lessons Learned** is valuable for teams — review it to capture institutional knowledge from each session
- Sessions before **v52** (2026-02-27) are not displayed because they lack the structured data protocol this viewer requires

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
