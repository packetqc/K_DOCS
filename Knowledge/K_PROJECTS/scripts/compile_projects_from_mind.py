#!/usr/bin/env python3
"""
Compile project data from K_MIND + tasks.json for the project-viewer interface.

Reads project metadata + tasks.json and produces projects.json
compatible with the project-viewer interface.

Usage:
  python3 Knowledge/K_PROJECTS/scripts/compile_projects_from_mind.py
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
K_PROJECTS = PROJECT_ROOT / "Knowledge" / "K_PROJECTS"
TASKS_PATH = PROJECT_ROOT / "docs" / "data" / "tasks.json"
SESSIONS_PATH = PROJECT_ROOT / "docs" / "data" / "sessions.json"
MODULES_PATH = PROJECT_ROOT / "Knowledge" / "modules.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "docs" / "data" / "projects.json"


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def compile_projects(output_path=None):
    # Load tasks
    tasks = []
    if TASKS_PATH.exists():
        tasks = load_json(TASKS_PATH).get("tasks", [])

    # Load sessions
    sessions = []
    if SESSIONS_PATH.exists():
        sessions = load_json(SESSIONS_PATH).get("sessions", [])

    # Load modules
    modules = []
    if MODULES_PATH.exists():
        modules = load_json(MODULES_PATH).get("modules", [])

    # Load project metadata
    project_md = K_PROJECTS / "data" / "projects" / "knowledge.md"
    project_title = "Knowledge"
    if project_md.exists():
        with open(project_md, encoding="utf-8") as f:
            for line in f:
                if line.startswith("# Project:"):
                    project_title = line.replace("# Project:", "").strip()
                    break

    # Stage distribution from tasks
    stage_dist = {
        "initial": 0, "plan": 0, "analyze": 0, "implement": 0,
        "validation": 0, "documentation": 0, "approval": 0, "completion": 0,
    }
    for t in tasks:
        stage = t.get("current_stage", "initial")
        if stage in stage_dist:
            stage_dist[stage] += 1

    completed = stage_dist.get("completion", 0)
    total = len(tasks)
    completion_pct = round(completed / total * 100) if total else 0

    # Git metrics from session
    metrics = {"prs": 0, "additions": 0, "deletions": 0, "files_changed": 0}
    session_ids = []
    branches = []
    for s in sessions:
        metrics["additions"] += s.get("total_additions", 0)
        metrics["deletions"] += s.get("total_deletions", 0)
        metrics["files_changed"] += s.get("total_files_changed", 0)
        session_ids.append(s.get("id", ""))
        if s.get("branch"):
            branches.append(s["branch"])

    # Module summary
    module_summary = []
    for m in modules:
        module_summary.append({
            "id": m["id"],
            "name": m["name"],
            "status": m["status"],
            "has": m.get("has", []),
        })

    project = {
        "id": "project-knowledge",
        "title": project_title,
        "repo": "packetqc/K_DOCS",
        "board_number": 39,
        "board_url": "https://github.com/users/packetqc/projects/39",
        "task_count": total,
        "completed_tasks": completed,
        "completion_pct": completion_pct,
        "stage_distribution": stage_dist,
        "metrics": metrics,
        "branches": list(set(branches)),
        "session_ids": session_ids,
        "modules": module_summary,
        "tasks": [
            {
                "id": t["id"],
                "title": t["title"],
                "stage": t["current_stage"],
                "children_count": len(t.get("children", [])),
                "message_count": t.get("message_count", 0),
            }
            for t in tasks
        ],
    }

    output = {
        "meta": {
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "total_projects": 1,
            "source": "K_PROJECTS data + tasks.json + sessions.json + modules.json",
        },
        "projects": [project],
    }

    out = Path(output_path) if output_path else DEFAULT_OUTPUT
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Compiled 1 project → {out}")
    print(f"  tasks: {total} ({completed} completed, {completion_pct}%)")
    print(f"  modules: {len(module_summary)}")
    print(f"  sessions: {len(session_ids)}")
    print(f"  stage distribution: {stage_dist}")


if __name__ == "__main__":
    out = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            out = sys.argv[idx + 1]
    compile_projects(out)
