#!/usr/bin/env python3
"""Harvest pull — fetch content from a remote knowledge mind.

Pulls publications, methodology, or patterns from a remote knowledge
repository into the local mind. Supports the mesh model where any
knowledge node can pull from any other.

Usage:
  python3 scripts/harvest_pull.py pub <mind> <slug>       # Pull a publication
  python3 scripts/harvest_pull.py pub <mind> --list        # List available pubs
  python3 scripts/harvest_pull.py doc <mind> <slug>        # Pull a docs page
  python3 scripts/harvest_pull.py methodology <mind> <slug> # Pull a methodology
  python3 scripts/harvest_pull.py patterns <mind> <slug>   # Pull a pattern

  <mind> = GitHub repo slug (e.g., "packetqc/knowledge") or known alias

v2.0.1 — Mesh harvest: any mind can pull from any mind.
"""

import json
import os
import re
import subprocess
import sys
import tempfile
import shutil
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.join(SCRIPT_DIR, '..')

# Known mind aliases — extend as network grows
MIND_ALIASES = {
    'core': 'packetqc/knowledge',
    'knowledge': 'packetqc/knowledge',
    'knowledge-live': 'packetqc/knowledge-live',
    'mplib': 'packetqc/MPLIB',
    'stm32': 'packetqc/STM32N6570-DK_SQLITE',
    'pqc': 'packetqc/PQC',
}


def resolve_mind(mind_ref):
    """Resolve a mind reference to owner/repo format."""
    # Check aliases first
    if mind_ref.lower() in MIND_ALIASES:
        return MIND_ALIASES[mind_ref.lower()]
    # Accept direct owner/repo format
    if '/' in mind_ref:
        return mind_ref
    # Try packetqc/<mind_ref> as default owner
    return f'packetqc/{mind_ref}'


def fetch_raw_file(repo, path, branch='main'):
    """Fetch a raw file from a GitHub repo via raw.githubusercontent.com."""
    url = f'https://raw.githubusercontent.com/{repo}/{branch}/{path}'
    try:
        req = Request(url, headers={'User-Agent': 'knowledge-harvest/2.0.1'})
        with urlopen(req, timeout=15) as resp:
            return resp.read().decode('utf-8')
    except HTTPError as e:
        if e.code == 404:
            return None
        raise
    except URLError:
        return None


def fetch_directory_listing(repo, path, branch='main'):
    """Fetch directory listing from GitHub API (public repos only)."""
    url = f'https://api.github.com/repos/{repo}/contents/{path}?ref={branch}'
    token = os.environ.get('GH_TOKEN', '')
    headers = {'User-Agent': 'knowledge-harvest/2.0.1'}
    if token:
        headers['Authorization'] = f'token {token}'
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except (HTTPError, URLError):
        return None


def list_remote_publications(repo, branch='main'):
    """List publications available in a remote mind."""
    listing = fetch_directory_listing(repo, 'publications', branch)
    if not listing:
        return []

    pubs = []
    for item in listing:
        if item.get('type') == 'dir' and item['name'] != 'README.md':
            slug = item['name']
            # Try to fetch the README to get the title
            readme = fetch_raw_file(repo, f'publications/{slug}/v1/README.md', branch)
            if not readme:
                readme = fetch_raw_file(repo, f'publications/{slug}/README.md', branch)
            title = slug
            if readme:
                # Extract title from first # heading
                m = re.search(r'^#\s+(.+)', readme, re.MULTILINE)
                if m:
                    title = m.group(1).strip()
            pubs.append({'slug': slug, 'title': title})

    return pubs


def list_remote_docs(repo, branch='main'):
    """List docs pages available in a remote mind."""
    listing = fetch_directory_listing(repo, 'docs/publications', branch)
    if not listing:
        return []

    docs = []
    for item in listing:
        if item.get('type') == 'dir':
            slug = item['name']
            docs.append({'slug': slug})
    return docs


def pull_publication(repo, slug, branch='main', target_dir=None):
    """Pull a publication from a remote mind into local publications/.

    Copies:
      - publications/<slug>/v1/README.md (source content)
      - docs/publications/<slug>/index.md (web page, if exists)
      - docs/publications/<slug>/full/index.html (full export, if exists)
      - docs/fr/publications/<slug>/index.md (FR mirror, if exists)

    Returns dict with results.
    """
    if target_dir is None:
        target_dir = REPO_ROOT

    results = {
        'repo': repo,
        'slug': slug,
        'branch': branch,
        'pulled': [],
        'skipped': [],
        'errors': [],
    }

    # 1. Pull publication source
    pub_paths = [
        f'publications/{slug}/v1/README.md',
        f'publications/{slug}/README.md',
    ]
    pub_content = None
    pub_path_used = None
    for p in pub_paths:
        content = fetch_raw_file(repo, p, branch)
        if content:
            pub_content = content
            pub_path_used = p
            break

    if not pub_content:
        results['errors'].append(f'Publication {slug} not found in {repo}')
        return results

    # Write publication source
    local_pub_dir = os.path.join(target_dir, 'publications', slug, 'v1')
    os.makedirs(local_pub_dir, exist_ok=True)
    local_pub_path = os.path.join(local_pub_dir, 'README.md')

    if os.path.exists(local_pub_path):
        results['skipped'].append(f'publications/{slug}/v1/README.md (already exists)')
    else:
        # Add provenance header
        provenance = (
            f'<!-- harvest-pull: {repo} | branch: {branch} '
            f'| date: {datetime.now(timezone.utc).strftime("%Y-%m-%d")} -->\n'
        )
        with open(local_pub_path, 'w', encoding='utf-8') as f:
            f.write(provenance + pub_content)
        results['pulled'].append(f'publications/{slug}/v1/README.md')

    # 2. Pull docs page (EN)
    docs_paths = [
        f'docs/publications/{slug}/index.md',
    ]
    for dp in docs_paths:
        content = fetch_raw_file(repo, dp, branch)
        if content:
            local_docs_dir = os.path.join(target_dir, 'docs', 'publications', slug)
            os.makedirs(local_docs_dir, exist_ok=True)
            local_docs_path = os.path.join(local_docs_dir, 'index.md')
            if os.path.exists(local_docs_path):
                results['skipped'].append(f'{dp} (already exists)')
            else:
                # Update relative paths if needed
                content = _rewrite_provenance(content, repo, branch)
                with open(local_docs_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                results['pulled'].append(dp)

    # 3. Pull full export HTML (if exists)
    full_html = fetch_raw_file(repo, f'docs/publications/{slug}/full/index.html', branch)
    if full_html:
        local_full_dir = os.path.join(target_dir, 'docs', 'publications', slug, 'full')
        os.makedirs(local_full_dir, exist_ok=True)
        local_full_path = os.path.join(local_full_dir, 'index.html')
        if os.path.exists(local_full_path):
            results['skipped'].append(f'docs/publications/{slug}/full/index.html (already exists)')
        else:
            with open(local_full_path, 'w', encoding='utf-8') as f:
                f.write(full_html)
            results['pulled'].append(f'docs/publications/{slug}/full/index.html')

    # 4. Pull FR mirror (if exists)
    fr_content = fetch_raw_file(repo, f'docs/fr/publications/{slug}/index.md', branch)
    if fr_content:
        local_fr_dir = os.path.join(target_dir, 'docs', 'fr', 'publications', slug)
        os.makedirs(local_fr_dir, exist_ok=True)
        local_fr_path = os.path.join(local_fr_dir, 'index.md')
        if os.path.exists(local_fr_path):
            results['skipped'].append(f'docs/fr/publications/{slug}/index.md (already exists)')
        else:
            content = _rewrite_provenance(fr_content, repo, branch)
            with open(local_fr_path, 'w', encoding='utf-8') as f:
                f.write(content)
            results['pulled'].append(f'docs/fr/publications/{slug}/index.md')

    return results


def pull_methodology(repo, slug, branch='main', target_dir=None):
    """Pull a methodology file from a remote mind."""
    if target_dir is None:
        target_dir = REPO_ROOT

    content = fetch_raw_file(repo, f'methodology/{slug}.md', branch)
    if not content:
        return {'errors': [f'Methodology {slug} not found in {repo}']}

    local_path = os.path.join(target_dir, 'methodology', f'{slug}.md')
    if os.path.exists(local_path):
        return {'skipped': [f'methodology/{slug}.md (already exists)']}

    provenance = (
        f'<!-- harvest-pull: {repo} | branch: {branch} '
        f'| date: {datetime.now(timezone.utc).strftime("%Y-%m-%d")} -->\n'
    )
    with open(local_path, 'w', encoding='utf-8') as f:
        f.write(provenance + content)
    return {'pulled': [f'methodology/{slug}.md']}


def pull_pattern(repo, slug, branch='main', target_dir=None):
    """Pull a pattern file from a remote mind."""
    if target_dir is None:
        target_dir = REPO_ROOT

    content = fetch_raw_file(repo, f'patterns/{slug}.md', branch)
    if not content:
        return {'errors': [f'Pattern {slug} not found in {repo}']}

    local_path = os.path.join(target_dir, 'patterns', f'{slug}.md')
    if os.path.exists(local_path):
        return {'skipped': [f'patterns/{slug}.md (already exists)']}

    provenance = (
        f'<!-- harvest-pull: {repo} | branch: {branch} '
        f'| date: {datetime.now(timezone.utc).strftime("%Y-%m-%d")} -->\n'
    )
    with open(local_path, 'w', encoding='utf-8') as f:
        f.write(provenance + content)
    return {'pulled': [f'patterns/{slug}.md']}


def _rewrite_provenance(content, repo, branch):
    """Add provenance comment to docs content."""
    date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    provenance = f'<!-- harvest-pull: {repo} | branch: {branch} | date: {date} -->\n'

    # Insert after front matter if present
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return f'---{parts[1]}---\n{provenance}{parts[2]}'

    return provenance + content


def print_results(results):
    """Pretty print pull results."""
    if results.get('pulled'):
        print(f"\n  Pulled from {results.get('repo', '?')}:")
        for p in results['pulled']:
            print(f"    + {p}")

    if results.get('skipped'):
        print(f"\n  Skipped (already exist):")
        for s in results['skipped']:
            print(f"    ~ {s}")

    if results.get('errors'):
        print(f"\n  Errors:")
        for e in results['errors']:
            print(f"    ! {e}")

    total = len(results.get('pulled', []))
    print(f"\n  Total: {total} file(s) pulled")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    mind_ref = sys.argv[2]
    repo = resolve_mind(mind_ref)

    branch = 'main'
    # Check for --branch flag
    for i, arg in enumerate(sys.argv):
        if arg == '--branch' and i + 1 < len(sys.argv):
            branch = sys.argv[i + 1]

    if cmd == 'pub':
        if len(sys.argv) > 3 and sys.argv[3] == '--list':
            print(f"\nPublications in {repo} ({branch}):\n")
            pubs = list_remote_publications(repo, branch)
            if not pubs:
                print("  (none found or repo not accessible)")
            for p in pubs:
                print(f"  - {p['slug']:40s}  {p['title']}")
            print(f"\n  Total: {len(pubs)} publication(s)")
        elif len(sys.argv) > 3:
            slug = sys.argv[3]
            print(f"\nPulling publication '{slug}' from {repo} ({branch})...")
            results = pull_publication(repo, slug, branch)
            print_results(results)
        else:
            print("Usage: harvest_pull.py pub <mind> <slug>")
            print("       harvest_pull.py pub <mind> --list")
            sys.exit(1)

    elif cmd == 'doc':
        if len(sys.argv) > 3 and sys.argv[3] == '--list':
            print(f"\nDocs pages in {repo} ({branch}):\n")
            docs = list_remote_docs(repo, branch)
            if not docs:
                print("  (none found or repo not accessible)")
            for d in docs:
                print(f"  - {d['slug']}")
            print(f"\n  Total: {len(docs)} doc page(s)")
        elif len(sys.argv) > 3:
            slug = sys.argv[3]
            print(f"\nPulling doc '{slug}' from {repo} ({branch})...")
            # Pull just the docs page (not the full publication)
            results = {
                'repo': repo, 'slug': slug, 'branch': branch,
                'pulled': [], 'skipped': [], 'errors': [],
            }
            content = fetch_raw_file(repo, f'docs/publications/{slug}/index.md', branch)
            if content:
                local_dir = os.path.join(REPO_ROOT, 'docs', 'publications', slug)
                os.makedirs(local_dir, exist_ok=True)
                local_path = os.path.join(local_dir, 'index.md')
                if os.path.exists(local_path):
                    results['skipped'].append(f'docs/publications/{slug}/index.md (exists)')
                else:
                    content = _rewrite_provenance(content, repo, branch)
                    with open(local_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    results['pulled'].append(f'docs/publications/{slug}/index.md')
            else:
                results['errors'].append(f'Doc page {slug} not found in {repo}')
            print_results(results)
        else:
            print("Usage: harvest_pull.py doc <mind> <slug>")
            sys.exit(1)

    elif cmd == 'methodology':
        if len(sys.argv) > 3:
            slug = sys.argv[3]
            print(f"\nPulling methodology '{slug}' from {repo} ({branch})...")
            results = pull_methodology(repo, slug, branch)
            results['repo'] = repo
            print_results(results)
        else:
            print("Usage: harvest_pull.py methodology <mind> <slug>")
            sys.exit(1)

    elif cmd == 'patterns':
        if len(sys.argv) > 3:
            slug = sys.argv[3]
            print(f"\nPulling pattern '{slug}' from {repo} ({branch})...")
            results = pull_pattern(repo, slug, branch)
            results['repo'] = repo
            print_results(results)
        else:
            print("Usage: harvest_pull.py patterns <mind> <slug>")
            sys.exit(1)

    else:
        print(f"Unknown command: {cmd}")
        print("Available: pub, doc, methodology, patterns")
        sys.exit(1)


if __name__ == '__main__':
    main()
