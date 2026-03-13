#!/usr/bin/env python3
"""
session_init.py — Initialize a new K_MIND session.

Creates fresh session files while preserving archives and mind_memory.
Called by Claude on new session start (bootstrap phase).

Usage:
    python3 scripts/session_init.py --session-id "Ka00B"
    python3 scripts/session_init.py --session-id "Ka00B" --preserve-active

Options:
    --preserve-active   Keep active messages in far_memory (for resume, not new session)
"""

import argparse
import json
import os
from datetime import datetime, timezone

SESSIONS_DIR = os.path.join(os.path.dirname(__file__), '..', 'sessions')
ARCHIVES_DIR = os.path.join(SESSIONS_DIR, 'archives')
FAR_MEMORY = os.path.join(SESSIONS_DIR, 'far_memory.json')
NEAR_MEMORY = os.path.join(SESSIONS_DIR, 'near_memory.json')


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  written: {path}")


def main():
    parser = argparse.ArgumentParser(description='Initialize K_MIND session')
    parser.add_argument('--session-id', required=True, help='New session identifier')
    parser.add_argument('--preserve-active', action='store_true',
                        help='Keep active messages (for resume)')
    args = parser.parse_args()

    os.makedirs(ARCHIVES_DIR, exist_ok=True)

    # Preserve existing archives index
    existing_archives = []
    if os.path.exists(FAR_MEMORY):
        try:
            old_far = load_json(FAR_MEMORY)
            existing_archives = old_far.get('archives', [])

            if args.preserve_active:
                # Keep active messages, just update session_id
                old_far['session_id'] = args.session_id
                save_json(FAR_MEMORY, old_far)
                print(f"OK: resumed session {args.session_id} (active messages preserved)")

                # Update near_memory session_id
                if os.path.exists(NEAR_MEMORY):
                    near = load_json(NEAR_MEMORY)
                    near['session_id'] = args.session_id
                    save_json(NEAR_MEMORY, near)
                return
        except (json.JSONDecodeError, KeyError):
            pass

    # New session: fresh files with archive index preserved
    far_data = {
        'session_id': args.session_id,
        'messages': [],
        'archives': existing_archives
    }
    save_json(FAR_MEMORY, far_data)

    near_data = {
        'session_id': args.session_id,
        'summaries': []
    }
    save_json(NEAR_MEMORY, near_data)

    print(f"OK: initialized session {args.session_id}")
    print(f"    archives preserved: {len(existing_archives)}")
    print(f"    far_memory: empty (fresh)")
    print(f"    near_memory: empty (fresh)")


if __name__ == '__main__':
    main()
