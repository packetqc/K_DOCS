#!/usr/bin/env python3
"""
compile_sessions.py — Parse session notes and generate docs/data/sessions.json

Reads all notes/session-*.md files, extracts metadata (date, title, branch,
PRs, type, summary), and writes a structured JSON for the Session Viewer
web page.

Usage:
    python3 scripts/compile_sessions.py
    python3 scripts/compile_sessions.py --output docs/data/sessions.json
"""

import os
import re
import json
import glob
import sys
from datetime import datetime


def extract_title(content, filename):
    """Extract session title from first heading."""
    match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        # Clean up common prefixes
        title = re.sub(r'^Session\s+(Notes\s+)?[—–-]\s*', '', title)
        title = re.sub(r'^\d{4}-\d{2}-\d{2}\s*[—–-]?\s*', '', title)
        return title.strip() if title.strip() else os.path.basename(filename)
    return os.path.basename(filename)


def extract_date(filename):
    """Extract date from filename pattern session-YYYY-MM-DD*.md"""
    match = re.search(r'session-(\d{4}-\d{2}-\d{2})', filename)
    return match.group(1) if match else None


def extract_branch(content):
    """Extract branch name from content."""
    patterns = [
        r'[Bb]ranch:\s*`?([^\s`\n]+)`?',
        r'`(claude/[^\s`]+)`',
    ]
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            return match.group(1)
    return None


def extract_prs(content):
    """Extract PR numbers and titles from content."""
    prs = []
    # Pattern: ### PR #NNN — Title
    for match in re.finditer(r'###\s+PR\s+#(\d+)\s*[—–-]\s*(.+)', content):
        prs.append({
            "number": int(match.group(1)),
            "title": match.group(2).strip()
        })
    # Pattern: PR #NNN: title or PR #NNN created/merged
    if not prs:
        for match in re.finditer(r'PR\s+#(\d+)\s*[—–:]\s*([^\n]+)', content):
            num = int(match.group(1))
            title = match.group(2).strip()
            # Avoid duplicates
            if not any(p["number"] == num for p in prs):
                prs.append({"number": num, "title": title})
    # Simple PR #NNN mentions
    if not prs:
        for match in re.finditer(r'PR\s+#(\d+)', content):
            num = int(match.group(1))
            if not any(p["number"] == num for p in prs):
                prs.append({"number": num, "title": ""})
    return prs


def extract_issues(content):
    """Extract issue numbers mentioned."""
    issues = set()
    for match in re.finditer(r'[Ii]ssue\s+#(\d+)', content):
        issues.add(int(match.group(1)))
    return sorted(list(issues))


def classify_session(content, title):
    """Classify session type based on content analysis."""
    title_lower = (title or "").lower()
    content_lower = content.lower()

    if any(w in title_lower for w in ["fix", "bug", "diagnostic", "rendering", "recovery"]):
        return "🔍 Diagnostic"
    if any(w in title_lower for w in ["deploy", "staging", "bootstrap"]):
        return "⚙️ Collateral"
    if any(w in title_lower for w in ["publication", "documentation", "doc review"]):
        return "📝 Documentation"
    if any(w in title_lower for w in ["design", "architecture", "conception"]):
        return "💡 Conception"

    # Content-based classification
    if "diagnostic" in content_lower or "root cause" in content_lower:
        return "🔍 Diagnostic"
    if "publication" in content_lower and "created" in content_lower:
        return "📝 Documentation"
    if "deploy" in content_lower or "bootstrap" in content_lower:
        return "⚙️ Collateral"

    return "📝 Documentation"


def extract_summary(content):
    """Extract a brief summary from the session notes."""
    # Look for ## Summary, ## Work Done, ## Objective sections
    for header in ["Summary", "Objective", "Work Done", "Context", "Résumé"]:
        pattern = rf'##\s+{header}\s*\n((?:(?!^##\s).)+)'
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if match:
            text = match.group(1).strip()
            # Take first 2 lines
            lines = [l.strip() for l in text.split('\n') if l.strip() and not l.strip().startswith('#')]
            summary = ' '.join(lines[:2])
            # Clean markdown
            summary = re.sub(r'\*\*([^*]+)\*\*', r'\1', summary)
            summary = re.sub(r'`([^`]+)`', r'\1', summary)
            summary = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', summary)
            summary = re.sub(r'^[-*]\s+', '', summary)
            if len(summary) > 200:
                summary = summary[:197] + "..."
            return summary
    return ""


def extract_lessons(content):
    """Extract lessons/decisions from content."""
    lessons = []
    for header in ["Lessons", "Decisions", "Findings", "Key Discovery"]:
        pattern = rf'##\s+{header}.*?\n((?:(?!^##\s).)+)'
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if match:
            text = match.group(1).strip()
            for line in text.split('\n'):
                line = line.strip()
                if line.startswith('- ') or line.startswith('* '):
                    lesson = line[2:].strip()
                    lesson = re.sub(r'\*\*([^*]+)\*\*', r'\1', lesson)
                    if lesson:
                        lessons.append(lesson)
    return lessons[:5]  # Max 5 lessons


def parse_session_file(filepath):
    """Parse a single session notes file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    date = extract_date(filename)
    title = extract_title(content, filename)
    branch = extract_branch(content)
    prs = extract_prs(content)
    issues = extract_issues(content)
    session_type = classify_session(content, title)
    summary = extract_summary(content)
    lessons = extract_lessons(content)

    # Build session ID from filename
    session_id = filename.replace('.md', '')

    return {
        "id": session_id,
        "date": date,
        "title": title,
        "branch": branch,
        "type": session_type,
        "summary": summary,
        "prs": prs,
        "issues": issues,
        "lessons": lessons,
        "pr_count": len(prs),
        "source_file": f"notes/{filename}"
    }


def load_tasks_by_branch(notes_dir):
    """Build a mapping of branch → task summary.

    Scans runtime caches and extracts lightweight task info.
    The branch is the primary key linking sessions to their tasks.
    Returns dict keyed by branch name, values are lists of task summaries.
    """
    import glob as _glob
    pattern = os.path.join(notes_dir, "session-runtime-*.json")
    tasks_by_branch = {}

    for path in sorted(_glob.glob(pattern)):
        try:
            with open(path, 'r') as f:
                cache = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue

        sd = cache.get("session_data", {})
        workflow = sd.get("task_workflow")
        if not workflow:
            continue

        branch = cache.get("branch", "")
        if not branch:
            continue

        issue_number = workflow.get("issue_number") or cache.get("issue_number", 0)
        current_stage = workflow.get("current_stage", "unknown")
        current_step = workflow.get("current_step")

        # Coherence: fix stage if step doesn't match
        step_stage_map = {
            "close_issue": "completion",
            "closed": "completion",
            "mark_modifications": "implement",
        }
        if current_step and current_step in step_stage_map:
            expected = step_stage_map[current_step]
            if current_stage != expected:
                current_stage = expected

        all_stages = [
            "initial", "plan", "analyze", "implement",
            "validation", "documentation", "approval", "completion",
        ]
        stage_index = all_stages.index(current_stage) if current_stage in all_stages else 0

        task_summary = {
            "issue_number": issue_number,
            "title": workflow.get("title") or cache.get("issue_title", ""),
            "current_stage": current_stage,
            "current_stage_index": stage_index,
            "task_id": f"task-{issue_number}" if issue_number else None,
        }

        # Index by branch — deduplicate by issue_number within same branch
        if branch not in tasks_by_branch:
            tasks_by_branch[branch] = []
        existing_issues = {t["issue_number"] for t in tasks_by_branch[branch]}
        if issue_number not in existing_issues:
            tasks_by_branch[branch].append(task_summary)

    return tasks_by_branch


def load_metrics_by_branch(notes_dir):
    """Build a mapping of branch → session metrics from runtime caches.

    Aggregates work_summary data (additions, deletions, files, commits)
    from runtime caches, indexed by branch.
    """
    import glob as _glob
    pattern = os.path.join(notes_dir, "session-runtime-*.json")
    metrics_by_branch = {}

    for path in sorted(_glob.glob(pattern)):
        try:
            with open(path, 'r') as f:
                cache = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue

        branch = cache.get("branch", "")
        if not branch:
            continue

        sd = cache.get("session_data", {})
        ws = sd.get("work_summary", {})
        if not isinstance(ws, dict):
            ws = {}

        # Aggregate metrics from work_summary
        prs_merged = ws.get("prs_merged", [])
        additions = ws.get("additions", 0)
        deletions = ws.get("deletions", 0)
        files_changed = ws.get("files_changed", 0)
        commits = 0
        for pr in prs_merged:
            if isinstance(pr, dict):
                commits += pr.get("commits", 0)

        if not prs_merged and not additions and not files_changed:
            continue

        if branch not in metrics_by_branch:
            metrics_by_branch[branch] = {
                "total_additions": 0,
                "total_deletions": 0,
                "total_files_changed": 0,
                "total_commits": 0,
            }

        m = metrics_by_branch[branch]
        m["total_additions"] += additions
        m["total_deletions"] += deletions
        m["total_files_changed"] += files_changed
        m["total_commits"] += commits

    return metrics_by_branch


def compile_sessions(notes_dir, output_path, incremental_files=None):
    """Compile session notes into a JSON file.

    Args:
        notes_dir: Directory containing session-*.md files.
        output_path: Output JSON path.
        incremental_files: If provided, only process these files and merge
            into the existing JSON. Otherwise, recompile all sessions.
    """
    # Load task summaries and metrics indexed by branch (primary key)
    tasks_by_branch = load_tasks_by_branch(notes_dir)
    metrics_by_branch = load_metrics_by_branch(notes_dir)

    if incremental_files:
        # Incremental mode: merge new/updated sessions into existing data
        existing_data = {"meta": {}, "sessions": []}
        if os.path.exists(output_path):
            try:
                with open(output_path, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                pass

        # Index existing sessions by ID for fast lookup
        existing_by_id = {s["id"]: i for i, s in enumerate(existing_data.get("sessions", []))}

        updated = 0
        added = 0
        for filepath in incremental_files:
            try:
                session = parse_session_file(filepath)
                # Inject tasks for this session based on its branch
                session_branch = session.get("branch", "")
                session["tasks"] = tasks_by_branch.get(session_branch, [])
                # Inject metrics from runtime caches
                branch_metrics = metrics_by_branch.get(session_branch, {})
                for mk, mv in branch_metrics.items():
                    if mk not in session or not session[mk]:
                        session[mk] = mv
                if session["id"] in existing_by_id:
                    # Replace existing entry
                    idx = existing_by_id[session["id"]]
                    existing_data["sessions"][idx] = session
                    updated += 1
                else:
                    # Insert at the beginning (newest first)
                    existing_data["sessions"].insert(0, session)
                    added += 1
            except Exception as e:
                print(f"Warning: Failed to parse {filepath}: {e}", file=sys.stderr)

        existing_data["meta"]["generated_at"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        existing_data["meta"]["total_sessions"] = len(existing_data["sessions"])

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)

        print(f"Incremental: {added} added, {updated} updated → {output_path} ({existing_data['meta']['total_sessions']} total)")
        return existing_data
    else:
        # Full recompile — preserve enrichment data from existing file
        existing_enriched = {}
        if os.path.exists(output_path):
            try:
                with open(output_path, 'r', encoding='utf-8') as f:
                    existing = json.load(f)
                for s in existing.get("sessions", []):
                    if s.get("total_additions") or s.get("prs"):
                        existing_enriched[s["id"]] = {
                            k: s[k] for k in [
                                "total_additions", "total_deletions",
                                "total_files_changed", "total_commits",
                                "pr_count", "prs",
                            ] if k in s and s[k]
                        }
            except (json.JSONDecodeError, OSError):
                pass

        pattern = os.path.join(notes_dir, 'session-*.md')
        files = sorted(glob.glob(pattern), reverse=True)  # Newest first

        sessions = []
        for filepath in files:
            try:
                session = parse_session_file(filepath)
                # Inject tasks based on branch
                session_branch = session.get("branch", "")
                session["tasks"] = tasks_by_branch.get(session_branch, [])
                # Inject metrics from runtime caches
                branch_metrics = metrics_by_branch.get(session_branch, {})
                for mk, mv in branch_metrics.items():
                    if mk not in session or not session[mk]:
                        session[mk] = mv
                # Preserve enrichment data from previous compilation
                if session["id"] in existing_enriched:
                    for ek, ev in existing_enriched[session["id"]].items():
                        if ek not in session or not session[ek]:
                            session[ek] = ev
                sessions.append(session)
            except Exception as e:
                print(f"Warning: Failed to parse {filepath}: {e}", file=sys.stderr)

        data = {
            "meta": {
                "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "total_sessions": len(sessions),
                "source": "notes/session-*.md"
            },
            "sessions": sessions
        }

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Compiled {len(sessions)} sessions → {output_path}")
        return data


if __name__ == "__main__":
    # Resolve paths relative to repo root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)

    notes_dir = os.path.join(repo_root, "notes")
    output_path = os.path.join(repo_root, "docs", "data", "sessions.json")

    # Allow override via --output
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]

    # --incremental <file1> [file2 ...]: merge only these files
    if "--incremental" in sys.argv:
        idx = sys.argv.index("--incremental")
        files = sys.argv[idx + 1:]
        # Resolve relative paths
        files = [os.path.join(repo_root, f) if not os.path.isabs(f) else f for f in files]
        compile_sessions(notes_dir, output_path, incremental_files=files)
    else:
        compile_sessions(notes_dir, output_path)
