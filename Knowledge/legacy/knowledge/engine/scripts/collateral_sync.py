#!/usr/bin/env python3
"""collateral_sync.py — Bridge for collateral tasks ↔ GitHub issues.

Manages the lifecycle of collateral tasks:
  - Create GitHub issues for new collateral tasks
  - Link collateral issues to parent session issue
  - Sync locally-persisted tasks when GitHub becomes available
  - Update task status based on GitHub issue/PR state

Usage (as module):
    from scripts.collateral_sync import CollateralSync
    sync = CollateralSync("packetqc/knowledge")
    sync.sync_all()  # reads knowledge_resultats.json, syncs to GitHub

Usage (CLI):
    python3 scripts/collateral_sync.py
    python3 scripts/collateral_sync.py --status
    python3 scripts/collateral_sync.py --dry-run

Authors: Martin Paquet, Claude (Anthropic)
License: MIT
Knowledge version: v2.0
"""

import json
import os
import sys
from datetime import datetime, timezone
from typing import Optional

# Import GitHubHelper
try:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from gh_helper import GitHubHelper
except ImportError:
    GitHubHelper = None


def _find_project_root():
    """Find project root by looking for CLAUDE.md."""
    d = os.path.dirname(os.path.abspath(__file__))
    while d != '/':
        if os.path.exists(os.path.join(d, 'CLAUDE.md')):
            return d
        d = os.path.dirname(d)
    return os.getcwd()


def _load_knowledge_results(root=None):
    """Load knowledge_resultats.json."""
    if not root:
        root = _find_project_root()
    path = os.path.join(root, '.claude', 'knowledge_resultats.json')
    if not os.path.exists(path):
        return None, path
    try:
        with open(path, 'r') as f:
            return json.load(f), path
    except (json.JSONDecodeError, OSError):
        return None, path


def _save_knowledge_results(data, path):
    """Save knowledge_resultats.json."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


class CollateralSync:
    """Manages collateral task ↔ GitHub issue synchronization.

    Reads collateral_tasks from knowledge_resultats.json, creates
    GitHub issues for tasks without issue_number, links them to
    the parent session issue, and updates status.
    """

    def __init__(self, repo: str, token: Optional[str] = None,
                 dry_run: bool = False):
        """Initialize sync handler.

        Args:
            repo: owner/repo format (e.g., "packetqc/knowledge")
            token: Optional PAT (defaults to GH_TOKEN env var)
            dry_run: If True, don't make GitHub API calls
        """
        self.repo = repo
        self.dry_run = dry_run
        self.root = _find_project_root()
        self._gh = None
        self._gh_available = False

        if not dry_run and GitHubHelper is not None:
            try:
                self._gh = GitHubHelper(token=token)
                self._gh_available = True
            except (ValueError, Exception):
                self._gh_available = False

    @property
    def enabled(self) -> bool:
        """Whether GitHub sync is available."""
        return self._gh_available and self._gh is not None

    def create_collateral_task(self, title: str, task_type: str = "fix",
                               description: str = "",
                               parent_issue: Optional[int] = None) -> dict:
        """Create a new collateral task entry.

        Creates the task in knowledge_resultats.json and optionally
        creates a GitHub issue if available.

        Args:
            title: Task title
            task_type: One of: fix, feature, doc, test, chore, refactor
            description: Task description
            parent_issue: Parent session issue number

        Returns:
            Dict with task data including id, issue_number (if created).
        """
        kr, kr_path = _load_knowledge_results(self.root)
        if not kr:
            return {"error": "knowledge_resultats.json not found"}

        tasks = kr.get("collateral_tasks", [])
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        # Generate unique task ID
        ct_id = f"ct-{len(tasks) + 1:03d}"

        task = {
            "id": ct_id,
            "title": title,
            "type": task_type,
            "status": "pending",
            "issue_number": None,
            "created_at": now,
            "pr_numbers": [],
            "description": description,
            "parent_issue": parent_issue,
            "local_only": True,
        }

        # Try to create GitHub issue
        if self.enabled and not self.dry_run:
            result = self._create_github_issue(task, parent_issue)
            if result.get("created"):
                task["issue_number"] = result["number"]
                task["local_only"] = False

        tasks.append(task)
        kr["collateral_tasks"] = tasks
        _save_knowledge_results(kr, kr_path)

        return task

    def _create_github_issue(self, task: dict,
                             parent_issue: Optional[int] = None) -> dict:
        """Create a GitHub issue for a collateral task.

        Args:
            task: Collateral task dict
            parent_issue: Parent issue number for linking

        Returns:
            GitHub API result dict.
        """
        if not self._gh:
            return {"error": "GitHub not available"}

        # Build issue body with parent reference
        body_parts = []
        if task.get("description"):
            body_parts.append(task["description"])
        if parent_issue:
            body_parts.append(
                f"\n---\n**Parent session issue:** #{parent_issue}\n"
                f"**Collateral task ID:** `{task.get('id', 'unknown')}`\n"
                f"**Type:** `{task.get('type', 'fix')}`"
            )
        body_parts.append(
            f"\n*Auto-generated collateral task — "
            f"{task.get('created_at', '')}*"
        )

        body = "\n".join(body_parts)
        title = f"[collateral] {task['title']}"

        result = self._gh.issue_create(
            repo=self.repo,
            title=title,
            body=body,
            labels=["task", "collateral"],
        )

        # Add cross-reference comment on parent issue
        if result.get("created") and parent_issue:
            self._link_to_parent(parent_issue, result["number"], task["title"])

        return result

    def _link_to_parent(self, parent_issue: int, child_issue: int,
                        child_title: str):
        """Post a cross-reference comment on the parent issue.

        Args:
            parent_issue: Parent issue number
            child_issue: Child (collateral) issue number
            child_title: Child task title
        """
        if not self._gh:
            return

        body = (
            f"**Collateral task created:** #{child_issue}\n"
            f"> {child_title}\n\n"
            f"*Auto-linked by session system v2.0*"
        )
        self._gh.issue_comment_post(self.repo, parent_issue, body)

    def sync_all(self) -> dict:
        """Sync all pending collateral tasks to GitHub.

        Reads knowledge_resultats.json, finds tasks with local_only=True,
        attempts to create GitHub issues for them.

        Returns:
            Dict with sync results: synced, failed, skipped counts.
        """
        kr, kr_path = _load_knowledge_results(self.root)
        if not kr:
            return {"error": "knowledge_resultats.json not found"}

        tasks = kr.get("collateral_tasks", [])
        parent_issue = None
        issue_gh = kr.get("issue_github", {})
        if isinstance(issue_gh, dict):
            parent_issue = issue_gh.get("numero")

        synced = 0
        failed = 0
        skipped = 0
        already = 0

        for task in tasks:
            # Skip tasks that already have GitHub issues
            if task.get("issue_number") and not task.get("local_only"):
                already += 1
                continue

            if not self.enabled:
                skipped += 1
                continue

            if self.dry_run:
                skipped += 1
                continue

            result = self._create_github_issue(task, parent_issue)
            if result.get("created"):
                task["issue_number"] = result["number"]
                task["local_only"] = False
                synced += 1
            else:
                failed += 1

        # Save updated tasks
        kr["collateral_tasks"] = tasks
        _save_knowledge_results(kr, kr_path)

        return {
            "total": len(tasks),
            "synced": synced,
            "failed": failed,
            "skipped": skipped,
            "already_synced": already,
            "github_available": self.enabled,
        }

    def update_task_status(self, task_id: str, status: str,
                           pr_numbers: Optional[list] = None) -> bool:
        """Update a collateral task's status.

        Args:
            task_id: Task ID (e.g., "ct-001")
            status: New status ("pending", "in_progress", "completed")
            pr_numbers: Optional list of PR numbers to associate

        Returns:
            True if updated, False if task not found.
        """
        kr, kr_path = _load_knowledge_results(self.root)
        if not kr:
            return False

        tasks = kr.get("collateral_tasks", [])
        for task in tasks:
            if task.get("id") == task_id:
                task["status"] = status
                if pr_numbers:
                    existing = task.get("pr_numbers", [])
                    task["pr_numbers"] = sorted(set(existing + pr_numbers))

                # Close GitHub issue if completed
                if status == "completed" and task.get("issue_number"):
                    if self.enabled and not self.dry_run:
                        self._gh.issue_close(
                            self.repo, task["issue_number"]
                        )

                kr["collateral_tasks"] = tasks
                _save_knowledge_results(kr, kr_path)
                return True

        return False

    def get_status(self) -> dict:
        """Get current collateral tasks status summary.

        Returns:
            Dict with task counts by status and sync state.
        """
        kr, _ = _load_knowledge_results(self.root)
        if not kr:
            return {"error": "knowledge_resultats.json not found"}

        tasks = kr.get("collateral_tasks", [])
        return {
            "total": len(tasks),
            "pending": sum(1 for t in tasks if t.get("status") == "pending"),
            "in_progress": sum(
                1 for t in tasks if t.get("status") == "in_progress"
            ),
            "completed": sum(
                1 for t in tasks if t.get("status") == "completed"
            ),
            "local_only": sum(1 for t in tasks if t.get("local_only")),
            "synced": sum(
                1 for t in tasks
                if t.get("issue_number") and not t.get("local_only")
            ),
            "github_available": self.enabled,
            "tasks": tasks,
        }


def main():
    """CLI entry point."""
    import argparse
    parser = argparse.ArgumentParser(
        description="Collateral task ↔ GitHub sync"
    )
    parser.add_argument(
        "--status", action="store_true",
        help="Show current collateral tasks status"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Don't make GitHub API calls"
    )
    parser.add_argument(
        "--repo", default="packetqc/knowledge",
        help="GitHub repo (default: packetqc/knowledge)"
    )
    args = parser.parse_args()

    sync = CollateralSync(args.repo, dry_run=args.dry_run)

    if args.status:
        status = sync.get_status()
        print(json.dumps(status, indent=2))
    else:
        result = sync.sync_all()
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
