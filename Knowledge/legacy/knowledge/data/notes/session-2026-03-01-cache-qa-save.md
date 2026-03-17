# Session Notes — 2026-03-01 — Session Cache QA (Save Segment)

## Context
Branch: `claude/session-cache-qa-0o1sQ`
Issue: #521

## Summary
Final segment of multi-compaction session. Delivered:
- Publications index: Interface prefix + hyperlinks on I1/I2 news (PRs #534, #535)
- Remove #23 from publications news (PR #536)
- Left panel links route to right panel with auto-extend (PR #537)
- Chrome/top panel collapsed by default (PR #538)
- Command links route to full publication doc pages (PR #539)

## Decisions
- All left panel links route to right panel (content-frame), not center
- Main Navigator is the single entry point link for interface news
- Chrome/top panel collapsed by default for maximum viewport
- Command links point to /full/ documentation pages
- Right panel auto-extends to first step (50vw) when collapsed and a link is clicked

## Deferred
- Title anchor on command links — /full/ routing done, anchors next session

## PRs (this segment)
- #534 — Publications index: Interface prefix + links
- #535 — Fix: both interface news link to Main Navigator
- #536 — Remove #23 from publications news
- #537 — Main Navigator: left panel links route to right panel
- #538 — Main Navigator: default chrome collapsed
- #539 — Command links route to full publication doc pages

## PRs (full session)
#524 through #539 — 16 PRs total, all merged to main
