#!/bin/bash
set -euo pipefail

# Read hook input from stdin
INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('session_id','unknown'))" 2>/dev/null || echo "unknown")
SOURCE=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('source','startup'))" 2>/dev/null || echo "startup")

cd "$CLAUDE_PROJECT_DIR"

# Initialize session based on source
if [ "$SOURCE" = "startup" ]; then
    python3 scripts/session_init.py --session-id "$SESSION_ID" 2>&1
elif [ "$SOURCE" = "resume" ] || [ "$SOURCE" = "compact" ]; then
    python3 scripts/session_init.py --session-id "$SESSION_ID" --preserve-active 2>&1
fi

# Instruct Claude to output the mindmap
echo ""
echo "K_MIND session initialized (source: $SOURCE, id: $SESSION_ID)."
echo "MANDATORY: You MUST now invoke /mind-context and output the mindmap and recent summaries as visible text in the conversation. This is not optional. Do it immediately before anything else."
echo "MANDATORY: Then, You MUST invoke /context and output the results to user"