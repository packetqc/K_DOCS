#!/bin/bash
# =============================================================================
# Migration Script: CC (v2.0) → packetqc/knowledge (unified)
#
# This script is meant to be run FROM the packetqc/knowledge repo.
# Copy it there first, then execute.
#
# Strategy:
#   1. Add CC as remote, fetch v2.0 content
#   2. Delete ONLY conflicting v1 files (flat skills, hooks, commands)
#   3. Overlay v2.0 on top (preserving v1 content that doesn't exist in CC)
#   4. Result: unified repo with v2.0 boot + v1 publications/data intact
# =============================================================================

set -euo pipefail

echo "============================================"
echo " Knowledge Migration: v1 + v2.0 Unification"
echo "============================================"
echo ""

# Safety check: must be in knowledge repo
if [ ! -d ".git" ]; then
    echo "ERROR: Not a git repository. Run this from packetqc/knowledge root."
    exit 1
fi

REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "")
if [[ "$REMOTE_URL" != *"knowledge"* ]]; then
    echo "WARNING: Origin doesn't look like packetqc/knowledge: $REMOTE_URL"
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    [[ $REPLY =~ ^[Yy]$ ]] || exit 1
fi

echo "Step 1/5: Adding CC as remote and fetching..."
git remote add cc https://github.com/packetqc/CC.git 2>/dev/null || echo "  (remote 'cc' already exists)"
git fetch cc

echo ""
echo "Step 2/5: Removing conflicting v1 files..."
# These v1 flat skills would coexist with v2 directory skills = chaos
V1_CONFLICTS=(
    ".claude/skills/github.md"
    ".claude/skills/harvest.md"
    ".claude/skills/healthcheck.md"
    ".claude/skills/integrity-check.md"
    ".claude/skills/live-session.md"
    ".claude/skills/normalize.md"
    ".claude/skills/plan-review.md"
    ".claude/skills/profile-update.md"
    ".claude/skills/project-create.md"
    ".claude/skills/project-manage.md"
    ".claude/skills/pub-export.md"
    ".claude/skills/pub.md"
    ".claude/skills/recall.md"
    ".claude/skills/resume.md"
    ".claude/skills/save-protocol.md"
    ".claude/skills/tagged-input.md"
    ".claude/skills/task-received.md"
    ".claude/skills/visual.md"
    ".claude/skills/wakeup.md"
    ".claude/skills/webcard.md"
    ".claude/skills/work-cycle.md"
    # v1 hooks that interfere with v2 boot
    ".claude/hooks/require-session-protocol.sh"
    ".claude/hooks/startup-checklist.sh"
    # v1 commands replaced by v2 skills
    ".claude/commands/integrity-gate.md"
    ".claude/commands/resilient-run.md"
    # v1 settings (v2 has its own)
    ".claude/settings.json"
)

for f in "${V1_CONFLICTS[@]}"; do
    if [ -f "$f" ]; then
        git rm -f "$f" 2>/dev/null && echo "  Removed: $f"
    fi
done

echo ""
echo "Step 3/5: Overlaying v2.0 content from CC..."
# This overwrites files that exist in both (v2 wins)
# and adds v2-only files (118 new files)
# but KEEPS v1-only files (publications, notes, data, etc.)
git checkout cc/main -- .

echo ""
echo "Step 4/5: Cleaning runtime state for fresh v2.0 boot..."
# Remove any session-specific state that shouldn't persist
rm -f .claude/knowledge_resultats.json 2>/dev/null
rm -f .claude/checkpoint_execution.json 2>/dev/null
rm -f .claude/preuve_execution.json 2>/dev/null
rm -f .claude/journal_actions.json 2>/dev/null

echo ""
echo "Step 5/5: Committing unified repo..."
git add -A
git status --short | head -20
echo "..."
echo "Total changes: $(git status --short | wc -l) files"

echo ""
echo "============================================"
echo " Migration ready to commit!"
echo "============================================"
echo ""
echo "Review the changes above, then run:"
echo ""
echo '  git commit -m "feat: Knowledge 2.0 — unified v1 + v2 migration"'
echo '  git push origin main'
echo ""
echo "After push, start a new Claude Code session."
echo "CLAUDE.md v2.0 will boot → knowledge-validation → v2.0 running clean."
echo ""
echo "What survives from v1:"
echo "  - 25 publications in publications/ (URLs preserved)"
echo "  - All docs/publications/ web pages (social media URLs intact)"
echo "  - evidence/, lessons/, live/, minds/, patterns/ data"
echo "  - 29 complementary methodologies"
echo "  - notes/, projects/, profile/ session data"
echo "  - docs/data/board-*.json board data"
echo ""
echo "What was replaced by v2:"
echo "  - CLAUDE.md (54-line v2 boot replaces 965-line v1)"
echo "  - .claude/skills/ (directory format replaces flat files)"
echo "  - docs/_config.yml, layouts, index pages"
echo "  - scripts/ (v2 engine replaces v1)"
echo ""
echo "What's recoverable from git history:"
echo '  git show HEAD~1:path/to/old/file'
