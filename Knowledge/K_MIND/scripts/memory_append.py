#!/usr/bin/env python3
"""
memory_append.py — Append a message to far_memory and a summary to near_memory.

Called by Claude every turn with intelligent content as arguments.
Handles all mechanical file I/O deterministically.

Usage (args):
    python3 scripts/memory_append.py \
        --role user --content "verbatim message" \
        --role2 assistant --content2 "full assistant output" \
        --summary "one-line summary" \
        --mind-refs "knowledge::session,knowledge::work" \
        [--tools '[{"tool":"Edit","file":"path","action":"desc"},...]']

Usage (stdin for large content — pipe JSON):
    echo '{"role":"user","content":"...","role2":"assistant","content2":"full output with tables etc","summary":"...","mind_refs":"...","tools":[]}' | \
    python3 scripts/memory_append.py --stdin
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone

SESSIONS_DIR = os.path.join(os.path.dirname(__file__), '..', 'sessions')
FAR_MEMORY = os.path.join(SESSIONS_DIR, 'far_memory.json')
NEAR_MEMORY = os.path.join(SESSIONS_DIR, 'near_memory.json')


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  written: {path}")


def next_message_id(far_data):
    if not far_data.get('messages'):
        return 1
    return max(m['id'] for m in far_data['messages']) + 1


def next_summary_id(near_data):
    if not near_data.get('summaries'):
        return 1
    return max(s['id'] for s in near_data['summaries']) + 1


def main():
    parser = argparse.ArgumentParser(description='Append to far_memory and near_memory')
    parser.add_argument('--stdin', action='store_true', help='Read JSON input from stdin (for large content)')
    parser.add_argument('--role', help='Message role (user/assistant)')
    parser.add_argument('--content', help='Verbatim message content')
    parser.add_argument('--role2', help='Second message role (for assistant response)')
    parser.add_argument('--content2', help='Second message content (full output)')
    parser.add_argument('--tools', default='', help='JSON array of tool calls')
    parser.add_argument('--summary', help='Summary for near_memory')
    parser.add_argument('--mind-refs', default='', help='Comma-separated mind_memory refs')
    args = parser.parse_args()

    # Support stdin mode for large content
    if args.stdin:
        data = json.load(sys.stdin)
        role = data['role']
        content = data['content']
        role2 = data.get('role2')
        content2 = data.get('content2')
        tools_list = data.get('tools', [])
        summary = data['summary']
        mind_refs_str = data.get('mind_refs', '')
    else:
        if not args.role or not args.content or not args.summary:
            parser.error('--role, --content, and --summary are required (or use --stdin)')
        role = args.role
        content = args.content
        role2 = args.role2
        content2 = args.content2
        tools_list = []
        if args.tools:
            try:
                tools_list = json.loads(args.tools)
            except json.JSONDecodeError:
                tools_list = []
        summary = args.summary
        mind_refs_str = args.mind_refs

    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Load current state
    far_data = load_json(FAR_MEMORY)
    near_data = load_json(NEAR_MEMORY)

    # Append first message to far_memory
    msg_id_1 = next_message_id(far_data)
    far_data['messages'].append({
        'id': msg_id_1,
        'role': role,
        'content': content,
        'timestamp': now
    })

    far_refs = [msg_id_1]

    # Append second message if provided
    if role2 and content2:
        msg_id_2 = msg_id_1 + 1
        msg2 = {
            'id': msg_id_2,
            'role': role2,
            'content': content2,
            'timestamp': now
        }
        if tools_list:
            msg2['tools'] = tools_list
        far_data['messages'].append(msg2)
        far_refs.append(msg_id_2)

    # Append summary to near_memory
    summary_id = next_summary_id(near_data)
    mind_refs = [r.strip() for r in mind_refs_str.split(',') if r.strip()]
    near_data['summaries'].append({
        'id': summary_id,
        'summary': summary,
        'far_memory_refs': far_refs,
        'mind_memory_refs': mind_refs,
        'timestamp': now
    })

    # Save both files
    save_json(FAR_MEMORY, far_data)
    save_json(NEAR_MEMORY, near_data)

    print(f"OK: far_memory ids={far_refs}, near_memory id={summary_id}")


if __name__ == '__main__':
    main()
