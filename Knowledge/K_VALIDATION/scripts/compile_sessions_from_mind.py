#!/usr/bin/env python3
"""
Compile session data from K_MIND memory for the session-review interface.

Reads near_memory + far_memory + tasks.json and produces sessions.json
compatible with the session-review interface.

Usage:
  python3 Knowledge/K_VALIDATION/scripts/compile_sessions_from_mind.py
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
K_MIND = PROJECT_ROOT / "Knowledge" / "K_MIND"
TASKS_PATH = PROJECT_ROOT / "docs" / "data" / "tasks.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "docs" / "data" / "sessions.json"


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def compile_sessions(output_path=None):
    near = load_json(K_MIND / "sessions" / "near_memory.json")
    far = load_json(K_MIND / "sessions" / "far_memory.json")

    # Load tasks if available
    tasks = []
    if TASKS_PATH.exists():
        tasks_data = load_json(TASKS_PATH)
        tasks = tasks_data.get("tasks", [])

    session_id = near.get("session_id", "unknown")
    summaries = near.get("summaries", [])
    messages = far.get("messages", [])
    archives = far.get("archives", [])

    # Count archived topics
    archive_files = list((K_MIND / "sessions" / "archives").glob("*.json"))

    # Compute metrics from tasks
    task_stages = {}
    for t in tasks:
        stage = t.get("current_stage", "unknown")
        task_stages[stage] = task_stages.get(stage, 0) + 1

    # Git metrics from this branch
    total_additions = 0
    total_deletions = 0
    total_files_changed = 0
    total_commits = 0

    # Try git log for metrics
    import subprocess
    prs = []
    try:
        result = subprocess.run(
            ["git", "log", "--shortstat", "--oneline"],
            capture_output=True, text=True, cwd=str(PROJECT_ROOT)
        )
        for line in result.stdout.split("\n"):
            line = line.strip()
            if "insertion" in line or "deletion" in line:
                total_commits += 1
                parts = line.split(",")
                for part in parts:
                    part = part.strip()
                    if "file" in part:
                        total_files_changed += int(part.split()[0])
                    elif "insertion" in part:
                        total_additions += int(part.split()[0])
                    elif "deletion" in part:
                        total_deletions += int(part.split()[0])
    except Exception:
        pass

    # Count merged PRs from git log
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", "--merges", "--grep=Merge pull request"],
            capture_output=True, text=True, cwd=str(PROJECT_ROOT)
        )
        for line in result.stdout.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            # Extract PR number from "Merge pull request #N from ..."
            import re
            m = re.search(r"Merge pull request #(\d+)", line)
            if m:
                pr_num = int(m.group(1))
                prs.append({
                    "number": pr_num,
                    "title": line.split(" ", 1)[1] if " " in line else line,
                    "url": f"https://github.com/packetqc/K_DOCS/pull/{pr_num}",
                })
    except Exception:
        pass

    # Build session entry
    session = {
        "id": session_id,
        "user_session_id": session_id,
        "date": summaries[0]["timestamp"][:10] if summaries else None,
        "title": "Knowledge Module System",
        "branch": "main",
        "type": "Feature",
        "request_type": "feature",
        "summary": "Multi-module knowledge system — K_MIND memory, K_DOCS documentation, K_VALIDATION QA, K_PROJECTS management, K_GITHUB integration",
        "repo": "packetqc/K_DOCS",
        "project": "Knowledge",
        "prs": prs,
        "total_prs": len(prs),
        "has_notes": True,
        "has_issue": False,
        "total_additions": total_additions,
        "total_deletions": total_deletions,
        "total_files_changed": total_files_changed,
        "total_commits": total_commits,
        "issue_number": None,
        "issue_labels": [],
        "first_activity_time": summaries[0]["timestamp"] if summaries else None,
        "last_activity_time": summaries[-1]["timestamp"] if summaries else None,
        "message_count": len(messages),
        "summary_count": len(summaries),
        "archive_count": len(archive_files),
        "task_count": len(tasks),
        "stage_distribution": task_stages,
        "engineering_stage": "implement",
        "work_summary": {
            "title": "Knowledge Module System",
            "tasks_completed": task_stages.get("completion", 0),
            "tasks_in_progress": task_stages.get("implement", 0),
            "tasks_in_validation": task_stages.get("validation", 0),
            "files_changed": total_files_changed,
            "additions": total_additions,
            "deletions": total_deletions,
            "deliverables": [t["title"] for t in tasks],
        },
        "metrics": {
            "categories": [
                {
                    "name": "Documentation",
                    "prs": len(prs),
                    "additions": total_additions,
                    "deletions": total_deletions,
                    "files": total_files_changed,
                    "commits": total_commits,
                    "issues": 0,
                    "lessons": 0,
                },
            ],
            "totals": {
                "prs": 0,
                "additions": total_additions,
                "deletions": total_deletions,
                "files": total_files_changed,
                "commits": total_commits,
            },
        },
        "tasks": [
            {
                "id": t["id"],
                "title": t["title"],
                "stage": t["current_stage"],
                "description": t["description"],
            }
            for t in tasks
        ],
        "lessons": [],
    }

    # Also include last_session summaries if available
    last_session = near.get("last_session", {})
    sessions_list = [session]

    output = {
        "meta": {
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "total_sessions": 1,
            "source": "K_MIND near_memory + far_memory + tasks.json",
        },
        "sessions": sessions_list,
    }

    out = Path(output_path) if output_path else DEFAULT_OUTPUT
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Compiled 1 session → {out}")
    print(f"  messages: {len(messages)}, summaries: {len(summaries)}")
    print(f"  tasks: {len(tasks)}, archives: {len(archive_files)}")
    print(f"  git: +{total_additions}/-{total_deletions}, {total_files_changed} files, {total_commits} commits")


if __name__ == "__main__":
    out = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            out = sys.argv[idx + 1]
    compile_sessions(out)
