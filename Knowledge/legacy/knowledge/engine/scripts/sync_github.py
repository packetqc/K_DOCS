#!/usr/bin/env python3
"""
sync_github.py — Full sync of compiled data with GitHub reality.

Pulls ALL issues and projects from GitHub API, creates task entries
for issues not yet tracked, updates the project registry, and
recompiles all data files (tasks.json, projects.json).

Uses GitHubHelper (never gh CLI) as per project rules.

Usage:
    python3 scripts/sync_github.py              # full sync
    python3 scripts/sync_github.py --dry-run    # preview only
"""

import json
import os
import sys
from datetime import datetime, timezone

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
OWNER = "packetqc"
REPO_NAME = "knowledge"


def fetch_all_issues(gh):
    """Fetch ALL issues from GitHub via GraphQL pagination."""
    query = '''
    query($cursor: String) {
      repository(owner: "packetqc", name: "knowledge") {
        issues(first: 100, after: $cursor, orderBy: {field: CREATED_AT, direction: DESC}) {
          pageInfo { hasNextPage endCursor }
          nodes {
            number
            title
            state
            createdAt
            closedAt
            body
            labels(first: 10) { nodes { name } }
            projectItems(first: 5) {
              nodes {
                project { number title }
              }
            }
          }
        }
      }
    }
    '''
    all_issues = []
    cursor = None
    while True:
        result = gh._graphql(query, {'cursor': cursor})
        issues = result['data']['repository']['issues']
        all_issues.extend(issues['nodes'])
        if not issues['pageInfo']['hasNextPage']:
            break
        cursor = issues['pageInfo']['endCursor']
    return all_issues


def fetch_all_projects(gh):
    """Fetch ALL projects from GitHub via pagination."""
    all_projects = []
    cursor = None
    while True:
        page = gh.project_list_page(per_page=10, cursor=cursor) if cursor else gh.project_list_page(per_page=10)
        all_projects.extend(page['projects'])
        if not page.get('has_next') or not page.get('next_cursor'):
            break
        cursor = page['next_cursor']
    return all_projects


def issue_to_task(issue):
    """Convert a GitHub issue to a task entry."""
    labels = [l['name'] for l in issue['labels']['nodes']]

    # Determine project from board association
    project = None
    board_number = None
    for pi in issue.get('projectItems', {}).get('nodes', []):
        project = pi['project']['title']
        board_number = pi['project']['number']
        break

    # Determine current stage from labels
    stage = "initial"
    stage_index = 0
    all_stages = ["initial", "plan", "analyze", "implement",
                  "validation", "documentation", "approval", "completion"]

    # Check STAGE: labels
    for label in labels:
        if label.startswith("STAGE:"):
            stage_name = label.replace("STAGE:", "")
            if stage_name in all_stages:
                stage = stage_name
                stage_index = all_stages.index(stage_name)

    # Closed issues → completion
    if issue['state'] == 'CLOSED':
        stage = "completion"
        stage_index = 7

    # Determine type/category from labels
    is_session = 'SESSION' in labels
    is_task_label = 'task' in labels
    is_project = 'project' in labels
    is_feature = 'FEATURE' in labels
    is_bug = 'bug' in labels
    is_enhancement = 'enhancement' in labels

    # Build knowledge grid based on available evidence
    has_title = bool(issue['title'])
    has_body = bool(issue.get('body'))
    is_completed = issue['state'] == 'CLOSED'

    a1 = "Vrai" if has_title else "--"
    a2 = "Vrai" if has_body else "--"
    a3 = "Vrai" if project else "--"
    a4 = "Vrai" if stage_index >= 3 else "--"

    b1 = "Vrai" if is_completed else "--"
    b2 = "Vrai" if is_completed else "--"
    b3 = "Vrai" if is_completed else "--"
    b4 = "Vrai" if is_completed else "--"

    c1 = "Vrai" if is_completed else "--"
    c2 = "Vrai" if is_completed else "--"
    c3 = "Vrai" if issue['number'] else "--"
    c4 = "Vrai" if is_completed else "--"

    d1 = "Vrai" if stage_index >= 5 else "--"
    d2 = "--"
    d3 = "Vrai" if d1 == "Vrai" and d2 == "Vrai" else "--"

    e1 = "Vrai" if stage_index >= 6 else "--"
    e2 = "Vrai" if is_completed else "--"
    e3 = "Vrai" if e1 == "Vrai" and e2 == "Vrai" else "--"
    e4 = "Vrai" if is_completed else "--"

    knowledge_grid = {
        "resultats": {
            "Validation de la demande": {"A1": a1, "A2": a2, "A3": a3, "A4": a4},
            "Qualité du travail": {"B1": b1, "B2": b2, "B3": b3, "B4": b4},
            "Intégrité de session": {"C1": c1, "C2": c2, "C3": c3, "C4": c4},
            "Documentation": {"D1": d1, "D2": d2, "D3": d3},
            "Approbation": {"E1": e1, "E2": e2, "E3": e3, "E4": e4},
        },
        "en_cours": False,
        "valeurs_detectees": {},
        "synthesized": True,
        "source": "github_sync",
    }

    task = {
        "id": f"task-{issue['number']}",
        "user_session_id": None,
        "issue_number": issue['number'],
        "title": issue['title'],
        "description": (issue.get('body') or '')[:500],
        "branch": "",
        "repo": REPO,
        "session_id": "",
        "source_file": "github_sync",
        "current_stage": stage,
        "current_stage_index": stage_index,
        "current_step": None,
        "project": project,
        "stages_visited": all_stages[:stage_index + 1],
        "stage_count": stage_index + 1,
        "total_transitions": stage_index + 1,
        "started_at": issue['createdAt'],
        "updated_at": issue.get('closedAt') or issue['createdAt'],
        "modifications_occurred": is_completed,
        "validation_skipped_entirely": False,
        "validation_summary": {},
        "unit_test_summary": {"total": 0, "passed": 0, "failed": 0, "pending": 0, "by_source": {}},
        "stage_history": [],
        "step_history": [],
        "validation_results": {},
        "unit_tests": [],
        "knowledge_grid": knowledge_grid,
        "time_compilation": None,
        "metrics_compilation": None,
        "labels": labels,
        "github_state": issue['state'],
    }

    return task


def sync_projects(gh, all_projects, all_issues, dry_run=False):
    """Sync .claude/projects.json with all GitHub projects."""
    registry_path = os.path.join(ROOT, ".claude", "projects.json")

    # Load existing registry
    existing = {"projets": []}
    if os.path.exists(registry_path):
        with open(registry_path, 'r', encoding='utf-8') as f:
            existing = json.load(f)

    existing_boards = {p.get("board_number"): p for p in existing["projets"]}

    # Build issue → project mapping
    issue_project_map = {}
    for issue in all_issues:
        for pi in issue.get('projectItems', {}).get('nodes', []):
            pnum = pi['project']['number']
            if pnum not in issue_project_map:
                issue_project_map[pnum] = []
            issue_project_map[pnum].append(issue['number'])

    added = 0
    updated = 0
    next_id = max((p.get("id", 0) for p in existing["projets"]), default=0) + 1

    for proj in all_projects:
        board_num = proj['number']
        title = proj['title']
        proj_id = proj['id']

        # Find associated PROJECT issue
        project_issue = None
        for issue in all_issues:
            labels = [l['name'] for l in issue['labels']['nodes']]
            if 'project' in labels and title.lower() in issue['title'].lower():
                project_issue = issue
                break

        if board_num in existing_boards:
            # Update existing entry
            entry = existing_boards[board_num]
            entry["titre"] = title
            entry["project_id"] = proj_id
            if project_issue and not entry.get("issue_number"):
                entry["issue_number"] = project_issue['number']
                entry["issue_url"] = f"https://github.com/{REPO}/issues/{project_issue['number']}"
            updated += 1
        else:
            # New project
            entry = {
                "id": next_id,
                "titre": title,
                "repo": REPO,
                "board_number": board_num,
                "board_url": f"https://github.com/users/{OWNER}/projects/{board_num}",
                "project_id": proj_id,
            }
            if project_issue:
                entry["issue_number"] = project_issue['number']
                entry["issue_url"] = f"https://github.com/{REPO}/issues/{project_issue['number']}"

            existing["projets"].append(entry)
            existing_boards[board_num] = entry
            next_id += 1
            added += 1

    # Sort by board_number
    existing["projets"].sort(key=lambda p: p.get("board_number", 0))

    if not dry_run:
        with open(registry_path, 'w', encoding='utf-8') as f:
            json.dump(existing, f, indent=2, ensure_ascii=False)

    print(f"  Projects registry: {added} added, {updated} updated, {len(existing['projets'])} total")
    return existing


def sync_tasks(all_issues, dry_run=False):
    """Sync tasks.json with all GitHub issues."""
    tasks_path = os.path.join(ROOT, "docs", "data", "tasks.json")

    # Load existing tasks
    existing_data = {"meta": {}, "tasks": []}
    if os.path.exists(tasks_path):
        with open(tasks_path, 'r') as f:
            existing_data = json.load(f)

    # Index existing by issue number (preserve rich data from runtime caches)
    existing_by_issue = {}
    existing_by_id = {}
    for t in existing_data.get("tasks", []):
        if t.get("issue_number"):
            existing_by_issue[t["issue_number"]] = t
        existing_by_id[t["id"]] = t

    added = 0
    updated = 0

    for issue in all_issues:
        issue_num = issue['number']
        task_id = f"task-{issue_num}"

        if issue_num in existing_by_issue:
            # Already tracked from runtime cache — preserve the richer data
            # Only update state and labels
            existing_task = existing_by_issue[issue_num]
            if issue['state'] == 'CLOSED' and existing_task.get('current_stage') != 'completion':
                existing_task['current_stage'] = 'completion'
                existing_task['current_stage_index'] = 7
                existing_task['github_state'] = 'CLOSED'
                updated += 1
            # Add labels if missing
            labels = [l['name'] for l in issue['labels']['nodes']]
            if labels and not existing_task.get('labels'):
                existing_task['labels'] = labels
            # Add project if missing
            if not existing_task.get('project'):
                for pi in issue.get('projectItems', {}).get('nodes', []):
                    existing_task['project'] = pi['project']['title']
                    break
            continue

        if task_id in existing_by_id:
            continue

        # New issue — create task entry
        task = issue_to_task(issue)
        existing_by_id[task_id] = task
        existing_by_issue[issue_num] = task
        added += 1

    # Rebuild task list
    all_tasks = list(existing_by_id.values())
    all_tasks.sort(key=lambda t: t.get("updated_at") or "", reverse=True)

    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    meta = {
        "generated_at": now,
        "total_tasks": len(all_tasks),
        "with_issue": sum(1 for t in all_tasks if t.get("issue_number")),
        "with_validation": sum(1 for t in all_tasks if t.get("validation_summary")),
        "synced_from": "github_api",
        "synced_at": now,
        "stages": [
            "initial", "plan", "analyze", "implement",
            "validation", "documentation", "approval", "completion",
        ],
        "sources": [
            "notes/session-runtime-*.json",
            "github_api (sync_github.py)",
        ],
    }

    output = {"meta": meta, "tasks": all_tasks}

    if not dry_run:
        os.makedirs(os.path.dirname(tasks_path), exist_ok=True)
        with open(tasks_path, 'w') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"  Tasks: {added} added, {updated} updated, {len(all_tasks)} total")
    return len(all_tasks)


def main():
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("  GitHub → Knowledge System Full Sync")
    print("=" * 60)
    if dry_run:
        print("  [DRY RUN — no files will be modified]")

    gh = GitHubHelper()

    # 1. Fetch all issues
    print(f"\n1. Fetching all issues from {REPO}...")
    all_issues = fetch_all_issues(gh)
    open_count = sum(1 for i in all_issues if i['state'] == 'OPEN')
    closed_count = sum(1 for i in all_issues if i['state'] == 'CLOSED')
    print(f"   Found {len(all_issues)} issues ({open_count} open, {closed_count} closed)")

    # 2. Fetch all projects
    print(f"\n2. Fetching all projects...")
    all_projects = fetch_all_projects(gh)
    print(f"   Found {len(all_projects)} project boards")

    # 3. Sync projects registry
    print(f"\n3. Syncing projects registry (.claude/projects.json)...")
    sync_projects(gh, all_projects, all_issues, dry_run)

    # 4. Sync tasks
    print(f"\n4. Syncing tasks (docs/data/tasks.json)...")
    task_count = sync_tasks(all_issues, dry_run)

    # 5. Recompile projects.json
    if not dry_run:
        print(f"\n5. Recompiling projects.json...")
        from scripts.compile_projects import compile_projects
        proj_count = compile_projects(ROOT, os.path.join(ROOT, "docs", "data", "projects.json"))
        print(f"   Compiled {proj_count} projects → docs/data/projects.json")

    print(f"\n{'=' * 60}")
    print(f"  Sync complete!")
    print(f"  Issues: {len(all_issues)} | Projects: {len(all_projects)} | Tasks: {task_count}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
