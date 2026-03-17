# Session Notes — 2026-03-03 — Remove NEWS.md and PLAN.md from wakeup reads

## Context
Branch: `claude/read-knowledge-files-G8a5z`
Issue: #612

## Summary
Removed NEWS.md, PLAN.md, and LINKS.md from mandatory wakeup startup reads to reduce context load. These files are available on-demand. Fixed startup hook accordingly.

## Work Done

### PR #616 — Remove NEWS.md and PLAN.md from wakeup startup reads
- Removed from wakeup steps 1-8 context load
- Files remain available via on-demand read

### PR #618 — Also remove LINKS from wakeup context load + fix startup hook
- Extended removal to LINKS.md
- Updated startup hook
