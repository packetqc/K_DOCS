# Session Notes — 2026-03-02 — Fix session notes not written during save

## Context
Branch: `claude/create-test-routine-zbDuQ`
Issue: #586

Bug fix session. After the session-runtime cache feature (v51-v54), Claude sessions confused the JSON runtime cache with the markdown session notes and stopped writing markdown notes during save. The Session Viewer (I1) depends on markdown notes via generate_sessions.py.

## Work Done

### PR #587 — fix: session notes not written during save — runtime cache confused with notes
- Added `generate_session_notes()` to `scripts/session_agent.py` (~130 lines)
- Updated `methodology/session-protocol.md` with "Two Persistence Systems" section
- Updated `CLAUDE.md` save protocol with guard and Consumer column in five-channel table
- Status: merged

## Key Decisions
- Two systems must coexist: JSON cache (real-time, session continuity) + markdown notes (save-time, web interface)
- Programmatic note generation via `generate_session_notes()` rather than relying on Claude to remember format
- Guard added to save protocol: verify markdown file was produced

## Lessons
- Semantic confusion from reusing the word "cache" for both systems caused the regression
- The `parse_notes_file()` function in `generate_sessions.py` requires the `Branch:` field for PR matching — this is the critical link

## Metrics
- 1 PR, 3 files, +195 -10 lines
- ~30min active time
