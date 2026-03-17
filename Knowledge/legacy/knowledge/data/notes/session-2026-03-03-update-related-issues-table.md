---
session_id: hKLpN
date: 2026-03-03
issue: 649
branch: claude/update-related-issues-table-hKLpN
title: Update Related Issues table in Session Viewer
---

# Session: Update Related Issues table in Session Viewer

## Summary

Added two protocol enhancements to the knowledge system:

1. **Gate G7 enforcement** (PR #660) — Made the GitHub issue the complete session record. All user/Claude exchanges MUST be posted as issue comments. Added Gate G7 to session-protocol.md and CLAUDE.md.

2. **Multi-issue session support** (PR #661) — When sessions work on 2+ issues, metrics and time compilation tables are now grouped per issue with session-level aggregates. Updated metrics-compilation.md, time-compilation.md, interactive-work-sessions.md, and commands.md.

## Metrics

| Metric | Value |
|--------|-------|
| PRs merged | 2 (#660, #661) |
| Files modified | 6 |
| Lines added | +165 |
| Lines removed | -20 |
| Estimated active time | ~15min |

## Deliveries

- PR #660: Gate G7 enforcement — issue as complete session record (merged)
- PR #661: Multi-issue session support to metrics and time compilation (merged)
