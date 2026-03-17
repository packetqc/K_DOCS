# Session 2026-02-21 — Safe Elevation Protocol (v30)

## Status
- Branch: claude/general-work-3hJpU
- Focus: API crash mitigation during elevation flow

## Problem Observed
- Recurring API 400 errors: `tool_use ids must be unique`
- Triggers specifically during `elevate` flow when image upload + AskUserQuestion combine
- Pattern: multimodal input (image) + interactive tool call = conversation history corruption
- Once triggered, session is unrecoverable in-place — every retry hits same corrupted history
- Session dies, comes back as NPC (context lost)
- Observed across multiple sessions on 2026-02-21
- User identified this is NOT random — it's a reproducible pattern at the elevation point

## Root Cause Analysis
- Anthropic API bug: `tool_use ids must be unique` when multimodal + tool calls collide
- Cannot fix from our side — it's in the API layer
- BUT we can eliminate the trigger conditions

## Solution Implemented (v30)
Three mitigations, defense in depth:

1. **Pitfall #12** — Documented the pattern in Known Pitfalls with full description
2. **Pre-elevation checkpoint** — Auto-save state before attempting elevation
3. **Paste-first delivery** — Reversed recommendation: paste > image upload
   - Text paste = no multimodal processing = no collision trigger
   - Image upload demoted to fallback
4. **Turn isolation rule** — Never combine image upload + AskUserQuestion in same turn

## Changes Made
- CLAUDE.md: Added Pitfall #12 (after #11)
- CLAUDE.md: Updated mid-session elevation section with safe elevation protocol table
- CLAUDE.md: Updated token delivery protocol — paste-first ordering
- CLAUDE.md: Updated wakeup step 0.3 guidance — paste first, image fallback
- CLAUDE.md: Updated PAT creation guide step 6
- CLAUDE.md: Added v30 evolution entry
- CLAUDE.md: Updated all version references v29 → v30

## Decisions
- [x] Pitfall #12 documented
- [x] Safe elevation protocol designed and implemented
- [x] Paste-first delivery reversed from image-first
- [x] Turn isolation rule added
- [x] v30 evolution entry added
