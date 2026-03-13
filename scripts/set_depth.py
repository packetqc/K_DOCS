#!/usr/bin/env python3
"""Set depth overrides for mindmap branches in depth_config.json.

Usage:
    python3 scripts/set_depth.py --path "session/near memory" --depth 4
    python3 scripts/set_depth.py --path "architecture" --depth 0       # omit branch
    python3 scripts/set_depth.py --path "architecture" --depth -1      # remove override (use default)
    python3 scripts/set_depth.py --default 3                           # set default depth
    python3 scripts/set_depth.py --list                                # show current config
"""
import argparse
import json
import os
import sys

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'conventions', 'depth_config.json')

def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=2)
        f.write('\n')

def main():
    parser = argparse.ArgumentParser(description='Manage mindmap depth config')
    parser.add_argument('--path', help='Branch path (e.g. "session/near memory")')
    parser.add_argument('--depth', type=int, help='Depth level (0=omit, -1=remove override)')
    parser.add_argument('--default', type=int, help='Set default depth for all branches')
    parser.add_argument('--list', action='store_true', help='Show current config')
    args = parser.parse_args()

    config = load_config()

    if args.list:
        print(f"Default depth: {config['default_depth']}")
        print(f"Omitted branches: {', '.join(config.get('omit', []))}")
        print("Overrides:")
        for path, depth in config.get('overrides', {}).items():
            print(f"  {path}: {depth}")
        return

    if args.default is not None:
        config['default_depth'] = args.default
        save_config(config)
        print(f"OK: default depth set to {args.default}")
        return

    if not args.path or args.depth is None:
        parser.error('--path and --depth are required (or use --list / --default)')

    if args.depth == 0:
        # Omit this branch
        omit = config.get('omit', [])
        if args.path not in omit:
            omit.append(args.path)
            config['omit'] = omit
        # Remove from overrides if present
        config.get('overrides', {}).pop(args.path, None)
        save_config(config)
        print(f"OK: {args.path} will be omitted in normal mode")
    elif args.depth == -1:
        # Remove override, use default
        config.get('overrides', {}).pop(args.path, None)
        # Remove from omit if present
        omit = config.get('omit', [])
        if args.path in omit:
            omit.remove(args.path)
            config['omit'] = omit
        save_config(config)
        print(f"OK: {args.path} reset to default depth {config['default_depth']}")
    else:
        # Set override
        if 'overrides' not in config:
            config['overrides'] = {}
        config['overrides'][args.path] = args.depth
        # Remove from omit if present
        omit = config.get('omit', [])
        if args.path in omit:
            omit.remove(args.path)
            config['omit'] = omit
        save_config(config)
        print(f"OK: {args.path} depth set to {args.depth}")

if __name__ == '__main__':
    main()
