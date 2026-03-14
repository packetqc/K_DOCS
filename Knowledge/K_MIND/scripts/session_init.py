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
import re
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


def topic_to_slug(topic):
    slug = topic.lower().strip()
    slug = re.sub(r'[^a-z0-9]+', '_', slug)
    slug = slug.strip('_')
    return slug


def auto_archive_previous_session(far_data, near_data):
    """Auto-archive any existing messages before wiping for a new session."""
    messages = far_data.get('messages', [])
    if not messages:
        return far_data, 0

    old_session_id = far_data.get('session_id', 'unknown')
    timestamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')
    topic = f"session-{old_session_id}"
    slug = topic_to_slug(topic)
    archive_filename = f"far_memory_{slug}_{timestamp}.json"
    archive_path = os.path.join(ARCHIVES_DIR, archive_filename)

    msg_ids = [m['id'] for m in messages]
    start_msg, end_msg = min(msg_ids), max(msg_ids)

    summaries = near_data.get('summaries', [])
    if summaries:
        near_ids = [s['id'] for s in summaries]
        start_near, end_near = min(near_ids), max(near_ids)
    else:
        start_near, end_near = 0, 0

    archive_data = {
        'topic': topic,
        'session_id': old_session_id,
        'message_range': [start_msg, end_msg],
        'near_memory_range': [start_near, end_near],
        'messages': messages,
        'summaries': summaries
    }
    save_json(archive_path, archive_data)

    # Update archives index in far_data
    if 'archives' not in far_data:
        far_data['archives'] = []

    far_data['archives'].append({
        'file': f"archives/{archive_filename}",
        'topic': topic,
        'message_range': [start_msg, end_msg],
        'near_memory_range': [start_near, end_near]
    })

    print(f"  auto-archived: {len(messages)} messages, {len(summaries)} summaries -> {archive_filename}")
    return far_data, len(messages)


def main():
    parser = argparse.ArgumentParser(description='Initialize K_MIND session')
    parser.add_argument('--session-id', required=True, help='New session identifier')
    parser.add_argument('--preserve-active', action='store_true',
                        help='Keep active messages (for resume)')
    args = parser.parse_args()

    os.makedirs(ARCHIVES_DIR, exist_ok=True)

    # Load existing files if present
    old_far = {'messages': [], 'archives': []}
    old_near = {'summaries': []}
    if os.path.exists(FAR_MEMORY):
        try:
            old_far = load_json(FAR_MEMORY)
        except (json.JSONDecodeError, KeyError):
            pass
    if os.path.exists(NEAR_MEMORY):
        try:
            old_near = load_json(NEAR_MEMORY)
        except (json.JSONDecodeError, KeyError):
            pass

    # Resume mode: keep active messages, just update session_id
    if args.preserve_active:
        old_far['session_id'] = args.session_id
        save_json(FAR_MEMORY, old_far)
        old_near['session_id'] = args.session_id
        save_json(NEAR_MEMORY, old_near)
        print(f"OK: resumed session {args.session_id} (active messages preserved)")
        return

    # Fresh session: auto-archive previous conversation before wiping
    archived_count = 0
    old_far, archived_count = auto_archive_previous_session(old_far, old_near)
    existing_archives = old_far.get('archives', [])

    # Capture last session summaries for continuity
    last_session_summaries = old_near.get('summaries', [])
    last_session_id = old_near.get('session_id', None)

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
    # Carry forward last session context for continuity on start
    if last_session_summaries:
        near_data['last_session'] = {
            'session_id': last_session_id,
            'summaries': last_session_summaries
        }
    save_json(NEAR_MEMORY, near_data)

    print(f"OK: initialized session {args.session_id}")
    print(f"    archives preserved: {len(existing_archives)}")
    if archived_count > 0:
        print(f"    auto-archived previous session: {archived_count} messages")
    print(f"    far_memory: empty (fresh)")
    print(f"    near_memory: empty (fresh)")
    if last_session_summaries:
        print(f"    last_session: {len(last_session_summaries)} summaries carried forward from {last_session_id}")


if __name__ == '__main__':
    main()
