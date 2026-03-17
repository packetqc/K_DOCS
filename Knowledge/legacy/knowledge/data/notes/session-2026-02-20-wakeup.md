# Session 2026-02-20 — Wakeup Resilience & Mobile Fixes

## Context
- Branch: `claude/wakeup-functionality-6Drqy`
- Core repo session — knowledge system improvements

## Changes Made

### 1. Mid-session wakeup (CLAUDE.md)
- `wakeup` is now explicitly re-runnable mid-session
- After context compaction, typing `wakeup` re-reads CLAUDE.md, syncs upstream, and restores all formatting rules
- Session Lifecycle updated: mid-session bullet added
- Context Loss Recovery updated: `wakeup` recommended over git recovery line after compaction
- Wakeup section: added "Mid-session re-run" paragraph with distinct `🔄` message

### 2. Help compaction resilience (CLAUDE.md)
- Added rule: if `help` is called after compaction, re-read CLAUDE.md formatting rules first
- Root cause: compaction strips specific formatting instructions → plain text output instead of markdown tables

### 3. Keyword mobile layout fix (publication.html)
- Keywords in version banner now wrap properly on narrow viewports
- Added `min-width: 0; flex: 1 1 0; line-height: 1.8` to `.pub-version-kw`
- Added `@media (max-width: 600px)` that stacks label above keywords

### 4. Webcard animation speed — ~3x slower
- All animation durations roughly tripled from original:
  - profile-hub: 150ms → 650ms
  - resume/full/ai-persistence: 300ms → 900ms
  - pipeline/distributed-minds/knowledge-system/publications: 250ms → 800ms
  - live-session/dashboard: 200ms → 750ms
- All 40 GIFs regenerated (10 cards × 2 themes × 2 langs)
- CLAUDE.md timing tables updated in both locations

### 5. FR terminology fix — esprits → connaissances
- Replaced "esprits distribués" with "connaissances distribuées" across:
  - publication.html keyword map
  - FR knowledge-system summary + full
  - FR distributed-minds summary + full
  - FR session-management full
- Zero occurrences of "esprits" remaining in docs/

## Status
- All changes complete, ready for commit + push + PR

## v24 Lesson — refresh formatting recovery is context-dependent

**Discovery**: `refresh` (and mid-session `wakeup`) formatting recovery depends on the session's pre-compaction context. Not a binary pass/fail — it's a spectrum.

**Test 1 — core session (THIS session)**: Mid-session wakeup restored help formatting correctly. The session was actively editing CLAUDE.md and producing markdown tables before compaction. The compacted summary preserved strong formatting signals. Wakeup reinforced what was already dominant. **Result: formatting restored.**

**Test 2 — satellite session (knowledge-live)**: Ran wakeup (v23), then wakeup again (v24 with refresh), then standalone refresh. Help output remained broken in all cases. The session started with v23, did installation work (not formatting-heavy), compacted, then tried to upgrade. **Result: formatting NOT restored.**

**Root cause**: Compaction creates a behavioral summary that shapes the model. If the pre-compaction context was rich in formatting (markdown tables, structured output), the compacted summary preserves those patterns and refresh reinforces them. If the pre-compaction context was plain-text-heavy (installation work, git operations), the compacted summary anchors plain-text behavior and refresh can't override it.

**Conclusion**: `refresh` works for formatting recovery when the session was already formatting-correct before compaction. It fails when the compacted summary never had strong formatting signals. For satellite sessions doing non-formatting work that hit compaction, a fresh session remains the reliable fix. Don't oversell, but don't undersell either — it works in the right conditions.
