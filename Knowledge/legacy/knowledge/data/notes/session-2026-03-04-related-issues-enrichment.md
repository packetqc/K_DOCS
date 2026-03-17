# Related Issues Enrichment & Protocol Updates

## Branch
`claude/update-related-issues-table-hKLpN`

## Summary
Full session: multi-request detection protocol (v56), Gate G8 (README.md enforcement), README.md overhaul (v39→v55), related issues enrichment in Session Viewer (titles, PR filtering, bidirectional parent-child linking), issue number in dropdown.

## Deliveries

| Delivery | Reference | Status |
|----------|-----------|--------|
| PR | #666 → main | ✅ merged |
| PR | #667 → main | ✅ merged |
| PR | #668 → main | ✅ merged |
| PR | #669 → main | ✅ merged |
| PR | #670 → main | ✅ merged |
| Issue | #664 | created |
| Issue | #665 | created |

## Metrics
- 5 PRs merged, 5 commits
- 10 files changed, +3,217 −2,129 lines

## Changes

### Multi-request detection (v56) — PR #666
- CLAUDE.md: updated On Task Received protocol to scan for multiple distinct requests
- session-protocol.md: expanded task received steps 1-6 with multi-request parsing

### Gate G8 — README.md enforcement — PR #666
- session-protocol.md: added G8 to enforcement gates table and self-assessment
- CLAUDE.md: added G8 to save protocol rules and todo delivery steps

### README.md overhaul — PR #666
- Updated from v39 to v55
- 13 → 24 publications with full web links
- Added Interfaces section (I1, I2), CHANGELOG.md to essentials
- Updated structure tree

### Related issues enrichment — PR #667
- generate_sessions.py: new fetch_issue_detail() function
- Builds related_issues array with title/state/labels per session
- Session Viewer: displays related issue titles (was showing "—")
- Issues table: sum row footer when 2+ issues
- Time compilation: totals row always displayed

### Issue number in dropdown — PR #669
- Format: "21:06 #617 Title 📦📋🎫"

### PR filtering + bidirectional linking — PR #670
- Filter PR numbers from related_issues (PRs are not issues)
- fetch_issue_detail skips pull requests (pull_request key)
- Bidirectional: child issues show parent session as related
- Example: #649 → related #664, #665 / #664 → parent #649

## Lessons
- README.md was severely outdated (v39 vs v55) — Gate G8 now prevents drift
- Related issues were just integer arrays with no enrichment — now fetched from API
- PRs were incorrectly appearing as related issues — filtered via all_pr_numbers set
- Bidirectional linking gives child issues context about their parent session
