#!/usr/bin/env python3
"""
enrich_from_github.py — Reconstruct historical metrics from GitHub API

Fetches merged PRs from the last N days, extracts metrics (additions,
deletions, files, commits), and enriches tasks.json and sessions.json
with real data from GitHub.

Uses GitHubHelper (never gh CLI) as per project rules.

Usage:
    python3 scripts/enrich_from_github.py              # last 7 days
    python3 scripts/enrich_from_github.py --days 30     # last 30 days
    python3 scripts/enrich_from_github.py --dry-run     # preview only
"""

import json
import os
import sys
from datetime import datetime, timezone, timedelta


def find_project_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != '/':
        if os.path.exists(os.path.join(d, 'CLAUDE.md')):
            return d
        d = os.path.dirname(d)
    return os.getcwd()


ROOT = find_project_root()
sys.path.insert(0, ROOT)

from scripts.gh_helper import GitHubHelper

REPO = "packetqc/knowledge"


def fetch_recent_prs(gh, days=7):
    """Fetch all merged PRs from the last N days with full metrics."""
    # GitHub API: list closed PRs, filter merged ones by date
    prs_raw = gh._request("GET", f"/repos/{REPO}/pulls?state=closed&sort=updated&direction=desc&per_page=100")
    if not isinstance(prs_raw, list):
        print(f"Error: unexpected response: {type(prs_raw)}")
        return []

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    merged_prs = []

    for pr in prs_raw:
        merged_at = pr.get("merged_at")
        if not merged_at:
            continue
        merged_dt = datetime.fromisoformat(merged_at.replace('Z', '+00:00'))
        if merged_dt < cutoff:
            continue

        # Fetch full PR details for metrics
        detail = gh._request("GET", f"/repos/{REPO}/pulls/{pr['number']}")

        merged_prs.append({
            "number": pr["number"],
            "title": pr["title"],
            "branch": pr["head"]["ref"],
            "base": pr["base"]["ref"],
            "merged_at": merged_at,
            "additions": detail.get("additions", 0),
            "deletions": detail.get("deletions", 0),
            "changed_files": detail.get("changed_files", 0),
            "commits": detail.get("commits", 0),
        })

    return merged_prs


def group_prs_by_branch(prs):
    """Group PRs by their head branch."""
    by_branch = {}
    for pr in prs:
        branch = pr["branch"]
        if branch not in by_branch:
            by_branch[branch] = []
        by_branch[branch].append(pr)
    return by_branch


def enrich_tasks(tasks_path, prs_by_branch, dry_run=False):
    """Enrich tasks.json with GitHub PR metrics."""
    with open(tasks_path, 'r') as f:
        data = json.load(f)

    enriched = 0
    for task in data["tasks"]:
        branch = task.get("branch", "")
        if not branch or branch not in prs_by_branch:
            continue

        prs = prs_by_branch[branch]
        total_additions = sum(p["additions"] for p in prs)
        total_deletions = sum(p["deletions"] for p in prs)
        total_files = sum(p["changed_files"] for p in prs)
        pr_numbers = sorted(set(p["number"] for p in prs))

        new_metrics = {
            "prs": len(prs),
            "pr_numbers": pr_numbers,
            "files_changed": total_files,
            "additions": total_additions,
            "deletions": total_deletions,
            "deliverables": [],
            "todos_count": 0,
        }

        old_metrics = task.get("metrics_compilation")
        if old_metrics and old_metrics.get("prs", 0) >= len(prs):
            # Already has equal or better data
            continue

        task["metrics_compilation"] = new_metrics
        enriched += 1

        issue = task.get("task_number", "?")
        print(f"  Task #{issue} ({branch}): {len(prs)} PRs, +{total_additions}/-{total_deletions}, {total_files} files")

    if not dry_run and enriched > 0:
        data["meta"]["enriched_at"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        data["meta"]["enriched_from"] = "github_api"
        with open(tasks_path, 'w') as f:
            json.dump(data, f, indent=2)

    return enriched


def enrich_sessions(sessions_path, prs_by_branch, dry_run=False):
    """Enrich sessions.json — update task metrics within sessions."""
    with open(sessions_path, 'r') as f:
        data = json.load(f)

    enriched = 0
    for session in data["sessions"]:
        branch = session.get("branch", "")
        if not branch or branch not in prs_by_branch:
            continue

        prs = prs_by_branch[branch]

        # Update session-level PR data if missing
        if session.get("pr_count", 0) == 0 and prs:
            session["pr_count"] = len(prs)
            session["prs"] = [{
                "number": p["number"],
                "title": p["title"],
                "additions": p["additions"],
                "deletions": p["deletions"],
                "changed_files": p["changed_files"],
                "commits": p["commits"],
            } for p in prs]
            session["total_additions"] = sum(p["additions"] for p in prs)
            session["total_deletions"] = sum(p["deletions"] for p in prs)
            session["total_files_changed"] = sum(p["changed_files"] for p in prs)
            session["total_commits"] = sum(p["commits"] for p in prs)
            enriched += 1
            print(f"  Session \"{session['title'][:40]}\" ({branch}): {len(prs)} PRs added")

    if not dry_run and enriched > 0:
        data["meta"]["enriched_at"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        with open(sessions_path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    return enriched


def main():
    days = 7
    dry_run = False

    if "--days" in sys.argv:
        idx = sys.argv.index("--days")
        if idx + 1 < len(sys.argv):
            days = int(sys.argv[idx + 1])

    if "--dry-run" in sys.argv:
        dry_run = True

    tasks_path = os.path.join(ROOT, "docs", "data", "tasks.json")
    sessions_path = os.path.join(ROOT, "docs", "data", "sessions.json")

    print(f"Enriching from GitHub API (last {days} days)...")
    if dry_run:
        print("  [DRY RUN — no files will be modified]")

    gh = GitHubHelper()

    # Fetch merged PRs
    print(f"\nFetching merged PRs from {REPO}...")
    prs = fetch_recent_prs(gh, days=days)
    print(f"  Found {len(prs)} merged PRs")

    if not prs:
        print("No PRs to process.")
        return

    # Group by branch
    prs_by_branch = group_prs_by_branch(prs)
    print(f"  Across {len(prs_by_branch)} branches")
    for branch, branch_prs in prs_by_branch.items():
        pr_nums = [p["number"] for p in branch_prs]
        print(f"    {branch}: PRs {pr_nums}")

    # Enrich tasks
    print(f"\nEnriching tasks...")
    task_count = enrich_tasks(tasks_path, prs_by_branch, dry_run)
    print(f"  {task_count} tasks enriched")

    # Enrich sessions
    print(f"\nEnriching sessions...")
    session_count = enrich_sessions(sessions_path, prs_by_branch, dry_run)
    print(f"  {session_count} sessions enriched")

    print(f"\nDone! {task_count} tasks + {session_count} sessions enriched from GitHub.")


if __name__ == "__main__":
    main()
