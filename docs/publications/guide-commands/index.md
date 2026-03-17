---
layout: publication
title: "Commands — User Guide"
description: "Complete reference for all Knowledge platform commands — session management, harvest, publications, projects, live analysis, visuals, and network."
pub_id: "User Guide — Commands"
version: "v1"
date: "2026-03-17"
permalink: /publications/guide-commands/
keywords: "commands, user guide, help, reference, session, harvest, publications, projects, live, visual, network"
---

# Commands — User Guide
{: #pub-title}

> **Module**: K_TOOLS — Command Framework & Utilities

**Contents**

| | |
|---|---|
| [Overview](#overview) | How commands work |
| [Usage Patterns](#usage-patterns) | Three ways to invoke commands |
| [Command Groups](#command-groups) | All 7 command groups at a glance |
| [Getting Help](#getting-help) | Contextual help for any command |
| [Full Reference →](full/) | Complete command tables and details |

## Overview

The Knowledge platform uses **short text commands** to trigger specific actions. Commands are organized by domain group and each maps to a K_* module for execution.

The `help` command displays a **multipart concatenated** table:
- **Part 1**: Knowledge commands (always available — defined in K_TOOLS)
- **Part 2**: Project-specific commands (varies per project — defined in project CLAUDE.md)

## Usage Patterns

Every command works with three entry patterns:

| Pattern | Entry | Best for |
|---------|-------|----------|
| **Direct** | `harvest --healthcheck` | Known commands, one-shot execution |
| **Natural language** | "check the freshness of all publications" | When you know what you want, not the syntax |
| **Interactive** | `interactif` + description | Multi-step sessions, exploratory work |

## Command Groups

| Group | Commands | Module |
|-------|----------|--------|
| **Session** | wakeup, refresh, help, status, save, remember, resume, recover, recall, checkpoint, elevate | K_MIND |
| **Normalize** | normalize, normalize --fix, normalize --check | K_VALIDATION |
| **Harvest** | harvest, harvest --list, --procedure, --healthcheck, --review, --stage, --promote, --auto, --fix | K_MIND |
| **Publications** | pub list/check/new/sync, doc review, docs check, webcard, weblinks, pub export | K_DOCS |
| **Project** | project list/info/create/register/review, #N: notes, g:board:item | K_PROJECTS |
| **Live Session** | I'm live, multi-live, deep, analyze, recipe | K_TOOLS |
| **Live Network** | beacon | K_TOOLS |

## Getting Help

Type any command followed by `?` for contextual help:

```
harvest --healthcheck ?
pub check ?
project create ?
```

---

**[Full Command Reference →](full/)**

*See also: [Main Navigator Guide]({{ '/publications/guide-main-navigator/' | relative_url }})*
