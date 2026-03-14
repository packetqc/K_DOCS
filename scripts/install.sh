#!/bin/bash
# K_MIND Bootstrap — Install K_MIND capabilities into a host project
# Run from the host project root: bash Knowledge/K_MIND/scripts/install.sh
#
# This script configures the host project's .claude/ directory to use
# K_MIND skills and hooks from Knowledge/K_MIND/.

set -euo pipefail

# Detect K_MIND path relative to the current directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
K_MIND_ABS="$(cd "$SCRIPT_DIR/.." && pwd)"
PROJECT_ROOT="$(pwd)"

# Compute relative path from project root to K_MIND
K_MIND_REL=$(python3 -c "import os; print(os.path.relpath('$K_MIND_ABS', '$PROJECT_ROOT'))")

# Verify we're not running from within K_MIND itself (standalone)
if [ "$K_MIND_REL" = "." ]; then
    echo "K_MIND is already at project root (standalone mode). No install needed."
    exit 0
fi

echo "Installing K_MIND from: $K_MIND_REL"

# --- 1. Create .claude directories ---
mkdir -p .claude/hooks
mkdir -p .claude/skills/mind-context
mkdir -p .claude/skills/mind-depth
mkdir -p .claude/skills/mind-stats

# --- 2. Generate .claude/settings.json ---
if [ -f .claude/settings.json ]; then
    echo "  .claude/settings.json already exists — skipping (check hooks manually)"
else
    cat > .claude/settings.json << 'SETTINGSEOF'
{
    "$schema": "https://json-schema.store/claude-code-settings.json",
    "hooks": {
        "SessionStart": [
            {
                "matcher": "",
                "hooks": [
                    {
                        "type": "command",
                        "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/session-start.sh"
                    }
                ]
            }
        ]
    }
}
SETTINGSEOF
    echo "  Created .claude/settings.json"
fi

# --- 3. Generate .claude/hooks/session-start.sh ---
cp "$K_MIND_ABS/.claude/hooks/session-start.sh" .claude/hooks/session-start.sh
chmod +x .claude/hooks/session-start.sh
echo "  Installed .claude/hooks/session-start.sh"

# --- 4. Copy skills (they auto-detect K_MIND_ROOT) ---
for skill in mind-context mind-depth mind-stats; do
    cp "$K_MIND_ABS/.claude/skills/$skill/SKILL.md" ".claude/skills/$skill/SKILL.md"
    echo "  Installed skill: $skill"
done

# --- 5. Install/update CLAUDE.md ---
K_MIND_INCLUDE="# K_MIND Integration
Read and apply Knowledge/K_MIND/CLAUDE.md as base instructions for the K_MIND memory system."

if [ -f CLAUDE.md ]; then
    if ! grep -q "Knowledge/K_MIND/CLAUDE.md" CLAUDE.md; then
        echo "" >> CLAUDE.md
        echo "$K_MIND_INCLUDE" >> CLAUDE.md
        echo "  Appended K_MIND reference to existing CLAUDE.md"
    else
        echo "  CLAUDE.md already references K_MIND — skipping"
    fi
else
    echo "$K_MIND_INCLUDE" > CLAUDE.md
    echo "  Created CLAUDE.md with K_MIND reference"
fi

# --- 6. Copy memory files if present ---
if [ -d "$K_MIND_ABS/.claude/memory" ]; then
    mkdir -p .claude/memory
    for src in "$K_MIND_ABS/.claude/memory"/*.md; do
        [ -f "$src" ] || continue
        filename=$(basename "$src")
        if [ ! -f ".claude/memory/$filename" ] || [ "$src" -nt ".claude/memory/$filename" ]; then
            cp "$src" ".claude/memory/$filename"
        fi
    done
    echo "  Synced memory files"
fi

echo ""
echo "K_MIND bootstrap complete."
echo "K_MIND location: $K_MIND_REL"
echo "Open Claude Code in this project to start using K_MIND capabilities."
