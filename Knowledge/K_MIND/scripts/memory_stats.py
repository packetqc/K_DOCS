#!/usr/bin/env python3
"""Output K_MIND memory stats table with context availability.

Usage:
    python3 scripts/memory_stats.py
"""
import json
import os
import glob

BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
MODEL_CONTEXT_LIMIT = 200_000  # Opus context window
AUTOCOMPACT_BUFFER = 33_000   # Reserved by Claude for compaction
SYSTEM_OVERHEAD = 34_000      # System prompt + tools + MCP tools (relatively constant)

def main():
    os.chdir(BASE_DIR)

    with open('sessions/far_memory.json') as f:
        fm = json.load(f)
    fm_msgs = len(fm.get('messages', []))
    fm_size = os.path.getsize('sessions/far_memory.json')

    with open('sessions/near_memory.json') as f:
        nm = json.load(f)
    nm_summaries = len(nm.get('summaries', []))
    nm_size = os.path.getsize('sessions/near_memory.json')

    archive_files = glob.glob('sessions/archives/far_memory_*.json')
    archive_count = len(archive_files)
    arc_size = sum(os.path.getsize(f) for f in archive_files)

    mm_size = os.path.getsize('mind/mind_memory.md')
    with open('mind/mind_memory.md') as f:
        lines = f.readlines()
    bt = chr(96) * 3
    node_count = sum(1 for l in lines if l.strip() and not l.strip().startswith(bt)
                     and not l.strip().startswith('%%') and 'mindmap' not in l.strip()
                     and 'root(' not in l.strip())

    domain_files = [f for f in glob.glob('*/**/**.json', recursive=True)
                    if not f.startswith('sessions/') and not f.startswith('node_modules/')]
    domain_size = sum(os.path.getsize(f) for f in domain_files)
    domain_count = len(domain_files)

    claude_md = os.path.getsize('CLAUDE.md') if os.path.exists('CLAUDE.md') else 0
    conv_size = os.path.getsize('conventions/conventions.json') if os.path.exists('conventions/conventions.json') else 0

    def kb(b):
        return f'{b / 1024:.1f} KB'

    def tk(b):
        return f'~{b // 4:,}'

    def tk_raw(b):
        return b // 4

    disk_total = fm_size + nm_size + mm_size + arc_size + domain_size + claude_md
    loaded_total = mm_size + nm_size + claude_md + conv_size
    loaded_tokens = tk_raw(loaded_total)
    # Estimate conversation tokens: far_memory tracks the full conversation,
    # so its size approximates the conversation history occupying the context window.
    conversation_tokens = tk_raw(fm_size)
    total_context_used = SYSTEM_OVERHEAD + loaded_tokens + conversation_tokens
    usable_limit = MODEL_CONTEXT_LIMIT - AUTOCOMPACT_BUFFER
    available = usable_limit - total_context_used

    print('| Store | Count | Size | ~Tokens | Loaded |')
    print('|:------|:------|:-----|:--------|:-------|')
    print(f'| far_memory | {fm_msgs} msgs | {kb(fm_size)} | {tk(fm_size)} | 0 |')
    print(f'| near_memory | {nm_summaries} summaries | {kb(nm_size)} | {tk(nm_size)} | {tk(nm_size)} |')
    print(f'| archives | {archive_count} topics | {kb(arc_size)} | {tk(arc_size)} | 0 |')
    print(f'| mind_memory | {node_count} nodes | {kb(mm_size)} | {tk(mm_size)} | {tk(mm_size)} |')
    print(f'| domain JSONs | {domain_count} refs | {kb(domain_size)} | {tk(domain_size)} | {tk(conv_size)} |')
    print(f'| CLAUDE.md | 1 file | {kb(claude_md)} | {tk(claude_md)} | {tk(claude_md)} |')
    print(f'| **Subtotal (K_MIND)** | | **{kb(disk_total)}** | **{tk(disk_total)}** | **~{loaded_tokens:,}** |')
    print(f'| **System overhead** | tools+MCP | | | **~{SYSTEM_OVERHEAD:,}** |')
    print(f'| **Conversation** | {fm_msgs} msgs | {kb(fm_size)} | | **~{conversation_tokens:,}** |')
    print(f'| **Context used** | | | | **~{total_context_used:,}** |')
    print(f'| **Usable limit** | 200k - 33k buffer | | | **~{usable_limit:,}** |')
    print(f'| **Available** | | | | **~{available:,}** |')

if __name__ == '__main__':
    main()
