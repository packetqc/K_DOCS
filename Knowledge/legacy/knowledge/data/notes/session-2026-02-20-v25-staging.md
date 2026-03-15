# v25 Staging Road Test — Monitoring Notes
**Date**: 2026-02-20
**Core session**: claude/wakeup-functionality-6Drqy (knowledge)
**Satellite session**: TBD (waiting for satellite to wakeup)

---

## Pre-Test State

- Core: 4 commits on task branch (v25 — Core Qualities + iterative staging)
- Main: v25 live (PRs #91, #92 merged)
- Satellite: wakeup running now

## Staging Timeline

| Time | Event | Status |
|------|-------|--------|
| — | v25 PRs #91, #92 merged to main | done |
| — | Satellite wakeup reads v25 | in progress |
| — | Satellite Round 1 (bootstrap) | pending |
| — | Round 1 PR merge | pending |
| — | Satellite verify Stage 1 | pending |
| — | Satellite Round 2 (normalize) | pending |
| — | Round 2 PR merge | pending |
| — | Satellite verify Stage 2 | pending |
| — | Installation complete | pending |

## Observations / Fixes Needed

1. **Human bridge missing after compaction** — Yesterday's session naturally guided user through PR creation/merge steps. Today after compaction, the guidance disappeared. Console guidance must be codified, not dependent on session memory. Added "The Human Bridge" principle to CLAUDE.md and "Console Guidance — Assisted Staging" section to satellite-bootstrap.md.

2. **Satellite default branch is `master`** — Confirms the $DEFAULT fix was necessary. Hardcoded `origin/main` would have broken verification.

3. **No staging guidance after wakeup scaffold** — Satellite completed wakeup, created scaffold files, started beacon — but did NOT print the `⏸` human bridge block to guide user through commit → push → PR → merge. The wakeup step 0.5 description said "commit and push immediately" but didn't explicitly require the console guidance block. **Fix**: Updated step 0.5 to say "immediately enter the guided staging flow" with mandatory `⏸` block. The staging pause must happen BEFORE continuing wakeup steps.

4. **Beacon deployed before scaffold merged** — Step 0.6 (beacon) ran before step 0.5 staging completed. The beacon and `live/` assets were deployed to the working tree but the scaffold files (CLAUDE.md, README, etc.) hadn't been merged to `master` yet. **Fix**: Step 0.5 now explicitly **BLOCKS** — wakeup does not continue to 0.6+ until all staging rounds are complete. Step 0.6 note added: "On fresh repos, runs only after step 0.5 staging is complete."

5. **Satellite save found "nothing to commit"** — After wakeup, user typed `save` but satellite reported "Working tree is clean." Wakeup created/modified files but either they were already committed from a previous session or the detection didn't trigger. **Fix**: Added "Autonomous Change Detection" — after each wakeup step that creates files, run `git status -s` and if changes exist, automatically enter the staging flow (commit → push → PR → `⏸`). Don't wait for user to type `save`.

