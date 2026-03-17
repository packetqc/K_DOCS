---
session_date: "2026-03-04"
issue_number: 724
title: "Fix scope pie: issue type breakdown instead of children vs related"
branch: "claude/review-issue-609-MIeq1"
status: "complete"
related_issues: [609]
---

## Summary
Fixed the lingering "lost related issues count" bug in the Session Scope pie chart (Session Review I1). The old children-vs-related split always produced an empty "Related Issues" slice because date-based grouping in generate_sessions.py makes all same-day sessions children of the earliest root — so children == related → related always empty.

Replaced with issue type breakdown showing bugs, enhancements, features, reviews, etc. Each slice is color-coded and shows count + lines changed. Structurally immune to the date-grouping problem.

## Deliveries
- PR #724 — merged to main
- `docs/interfaces/session-review/session-review.js` — scope pie rewrite

## Metrics
- Files: 1 | Lines: ~102 (+46/-56) | Commits: 1 | PRs: 1
- Active time: ~8 min
