#!/usr/bin/env python3
"""
compile_tasks.py — Parse session runtime caches and generate docs/data/tasks.json

Scans all notes/session-runtime-*.json files for task_workflow data,
enriches with validation results and unit test data, and writes a
structured JSON for the Tasks Workflow Viewer web interface (I3).

Usage:
    python3 scripts/compile_tasks.py
    python3 scripts/compile_tasks.py --output docs/data/tasks.json
"""

import os
import json
import glob
import sys
from datetime import datetime


def _parse_iso(ts):
    """Parse ISO timestamp string to datetime, returning None on failure."""
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts.replace('Z', '+00:00'))
    except (ValueError, AttributeError):
        return None


def _normalize_grid(kg):
    """Normalize knowledge_grid to current format (remove legacy 'labels' key)."""
    if not kg or not isinstance(kg, dict):
        return kg
    return {
        "resultats": kg.get("resultats", {}),
        "en_cours": kg.get("en_cours", False),
        "valeurs_detectees": kg.get("valeurs_detectees", {}),
    }


def _synthesize_grid(workflow, cache, stages_visited, current_stage, metrics_compilation):
    """Synthesize a conforming knowledge_grid for tasks that don't have one.

    Uses available task data (stage progression, validation, PRs, etc.)
    to infer grid values. Marks synthesized grids with 'synthesized': True.
    """
    issue_number = workflow.get("issue_number") or cache.get("issue_number", 0)
    issue_title = workflow.get("title") or cache.get("issue_title", "")
    branch = cache.get("branch", "")
    sd = cache.get("session_data", {})
    work_summary = sd.get("work_summary", {})
    if not isinstance(work_summary, dict):
        work_summary = {}
    validation_results = workflow.get("validation_results", {})

    all_stages = [
        "initial", "plan", "analyze", "implement",
        "validation", "documentation", "approval", "completion",
    ]
    stage_idx = all_stages.index(current_stage) if current_stage in all_stages else 0

    # Evidence of actual execution (PRs, commits, file changes)
    mc = metrics_compilation or {}
    has_pr_evidence = (mc.get("prs", 0) > 0 or mc.get("files_changed", 0) > 0
                       or mc.get("additions", 0) > 0)
    has_commit_evidence = bool(work_summary.get("prs_merged"))

    # --- Section A: Validation de la demande ---
    a1 = "Vrai" if issue_title else "--"
    a2 = "Vrai" if workflow.get("description") else "--"
    a3 = "Vrai" if workflow.get("project") or issue_number else "--"
    # A4: request executed only if stage >= implement AND evidence of work
    # Tasks with just comments stay in initial phases
    a4 = "Vrai" if (stage_idx >= 3 and (has_pr_evidence or has_commit_evidence)) else "--"

    # --- Section B: Qualité du travail ---
    has_validation = bool(validation_results)
    has_tests = bool(workflow.get("unit_tests"))
    mc = metrics_compilation or {}
    has_metrics = mc.get("prs", 0) > 0 or mc.get("files_changed", 0) > 0
    b1 = "Vrai" if has_tests or has_validation else "--"
    b2 = "Vrai" if mc.get("prs", 0) > 0 else "--"  # PR = code review
    b3 = "Vrai" if has_metrics else "--"
    b4 = "Vrai" if b1 == "Vrai" and b2 == "Vrai" and b3 == "Vrai" else "--"

    # --- Section C: Intégrité de session ---
    has_commits = bool(work_summary.get("prs_merged")) or mc.get("prs", 0) > 0
    c1 = "Vrai" if has_commits else "--"
    c2 = "Vrai" if cache.get("updated") else "--"  # cache was updated
    c3 = "Vrai" if issue_number else "--"  # has issue = commented
    c4 = "Vrai" if c1 == "Vrai" and c2 == "Vrai" and c3 == "Vrai" else "--"

    # --- Section D: Documentation ---
    d1 = "Vrai" if stage_idx >= 5 else "--"  # past documentation stage
    d2 = "--"  # user doc — can't infer
    d3 = "Vrai" if d1 == "Vrai" and d2 == "Vrai" else "--"

    # --- Section E: Approbation ---
    e1 = "Vrai" if stage_idx >= 6 else "--"  # past approval
    e2 = "Vrai" if current_stage == "completion" else "--"
    e3 = "Vrai" if e1 == "Vrai" and e2 == "Vrai" else "--"
    e4 = "Vrai" if current_stage == "completion" else "--"

    # Build valeurs_detectees from non-"--" values
    vals = {}
    grid_vals = {"A1": a1, "A2": a2, "A3": a3, "A4": a4,
                 "B1": b1, "B2": b2, "B3": b3, "B4": b4,
                 "C1": c1, "C2": c2, "C3": c3, "C4": c4,
                 "D1": d1, "D2": d2, "D3": d3,
                 "E1": e1, "E2": e2, "E3": e3, "E4": e4}
    for k, v in grid_vals.items():
        if v == "Vrai":
            vals[k] = v

    return {
        "resultats": {
            "Validation de la demande": {"A1": a1, "A2": a2, "A3": a3, "A4": a4},
            "Qualité du travail": {"B1": b1, "B2": b2, "B3": b3, "B4": b4},
            "Intégrité de session": {"C1": c1, "C2": c2, "C3": c3, "C4": c4},
            "Documentation": {"D1": d1, "D2": d2, "D3": d3},
            "Approbation": {"E1": e1, "E2": e2, "E3": e3, "E4": e4},
        },
        "en_cours": False,
        "valeurs_detectees": vals,
        "synthesized": True,
    }


def find_project_root():
    """Find the project root by looking for CLAUDE.md."""
    d = os.path.dirname(os.path.abspath(__file__))
    while d != '/':
        if os.path.exists(os.path.join(d, 'CLAUDE.md')):
            return d
        d = os.path.dirname(d)
    return os.getcwd()


def load_runtime_caches(notes_dir):
    """Load all session runtime cache files.

    Returns:
        List of (filename, cache_data) tuples.
    """
    pattern = os.path.join(notes_dir, "session-runtime-*.json")
    caches = []
    for path in sorted(glob.glob(pattern)):
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            caches.append((os.path.basename(path), data))
        except (json.JSONDecodeError, OSError):
            continue
    return caches


def extract_task_from_cache(filename, cache):
    """Extract task workflow data from a session runtime cache.

    Args:
        filename: Cache filename for reference.
        cache: Parsed cache dict.

    Returns:
        Task dict if task_workflow exists, None otherwise.
    """
    sd = cache.get("session_data", {})
    workflow = sd.get("task_workflow")
    if not workflow:
        return None

    # Extract session metadata
    session_id = cache.get("session_id", "")
    issue_number = workflow.get("issue_number") or cache.get("issue_number", 0)
    issue_title = workflow.get("title") or cache.get("issue_title", "")
    branch = cache.get("branch", "")
    repo = cache.get("repo", "")
    created = cache.get("created", "")
    updated = cache.get("updated", "")
    user_session_id = sd.get("user_session_id")

    # Validation results
    validation_results = workflow.get("validation_results", {})
    validation_skipped = workflow.get("validation_skipped_entirely", False)

    # Unit tests
    unit_tests = workflow.get("unit_tests", [])

    # Stage history
    stage_history = workflow.get("stage_history", [])
    step_history = workflow.get("step_history", [])

    # Compute stage progression
    stages_visited = []
    seen = set()
    for entry in stage_history:
        s = entry.get("stage")
        if s and s not in seen:
            stages_visited.append(s)
            seen.add(s)

    # Coherence fix: if stage_history is empty but current_stage_index > 0,
    # reconstruct stages_visited from the known stage sequence
    all_stages = [
        "initial", "plan", "analyze", "implement",
        "validation", "documentation", "approval", "completion",
    ]
    current_stage = workflow.get("current_stage", "unknown")
    current_stage_index = workflow.get("current_stage_index", 0)

    if current_stage_index > 0 and (not stages_visited or current_stage not in stages_visited):
        # Reconstruct: ensure all stages up to current are marked visited
        stages_visited = all_stages[:current_stage_index + 1]

    # Coherence fix: ensure current_step matches current_stage
    current_step = workflow.get("current_step")
    step_stage_map = {
        "close_issue": "completion",
        "closed": "completion",
        "mark_modifications": "implement",
        "analyze_prompt": "initial",
        "extract_title": "initial",
        "create_plan": "plan",
    }
    if current_step and current_step in step_stage_map:
        expected_stage = step_stage_map[current_step]
        if current_stage != expected_stage:
            # Fix: use the step's stage as the real current stage
            current_stage = expected_stage
            current_stage_index = all_stages.index(expected_stage) if expected_stage in all_stages else current_stage_index
            stages_visited = all_stages[:current_stage_index + 1]

    # Compute validation summary per stage
    validation_summary = {}
    for stage_name, stage_val in validation_results.items():
        checks = stage_val.get("checks", [])
        validation_summary[stage_name] = {
            "status": stage_val.get("overall_status", "pending"),
            "skipped": stage_val.get("skipped", False),
            "total_checks": len(checks),
            "passed": sum(1 for c in checks if c.get("result") == "passed"),
            "failed": sum(1 for c in checks if c.get("result") == "failed"),
            "validated_at": stage_val.get("validated_at"),
        }

    # Compute unit test summary
    test_summary = {
        "total": len(unit_tests),
        "passed": sum(1 for t in unit_tests if t.get("result") == "passed"),
        "failed": sum(1 for t in unit_tests if t.get("result") == "failed"),
        "pending": sum(1 for t in unit_tests if t.get("result") is None),
        "by_source": {},
    }
    for t in unit_tests:
        src = t.get("source", "unknown")
        test_summary["by_source"].setdefault(src, 0)
        test_summary["by_source"][src] += 1

    # Compute timing
    started_at = workflow.get("started_at") or created
    updated_at = workflow.get("updated_at") or updated

    # Knowledge grid results — use cache's own grid, normalize format,
    # or synthesize from available data. Never fallback to global file.
    knowledge_grid = None
    cache_kg = sd.get("knowledge_grid")
    if cache_kg and cache_kg.get("resultats"):
        knowledge_grid = _normalize_grid(cache_kg)
    # Synthesis happens after metrics_compilation is computed (see below)

    # Time compilation — calculate stage durations
    time_compilation = None
    # Fallback: use compilations_post_execution from knowledge-validation cache
    cpe = sd.get("compilations_post_execution") or {}
    cpe_temps = cpe.get("temps", {})

    if stage_history:
        stage_durations = []
        total_active_sec = 0
        for entry in stage_history:
            entered = _parse_iso(entry.get("entered_at"))
            exited = _parse_iso(entry.get("exited_at"))
            dur_sec = 0
            if entered and exited:
                dur_sec = (exited - entered).total_seconds()
            total_active_sec += dur_sec
            stage_durations.append({
                "stage": entry.get("stage", "unknown"),
                "duration_seconds": dur_sec,
            })

        calendar_sec = 0
        s = _parse_iso(started_at)
        u = _parse_iso(updated_at)
        if s and u:
            calendar_sec = (u - s).total_seconds()

        time_compilation = {
            "calendar_seconds": calendar_sec,
            "active_seconds": total_active_sec,
            "inactive_seconds": max(0, calendar_sec - total_active_sec),
            "stage_durations": stage_durations,
        }
    elif cpe_temps:
        # Fallback from knowledge-validation compilations
        time_compilation = {
            "calendar_seconds": cpe_temps.get("calendar_seconds", 0),
            "active_seconds": cpe_temps.get("active_seconds", 0),
            "inactive_seconds": cpe_temps.get("inactive_seconds", 0),
            "stage_durations": cpe_temps.get("stage_durations", []),
        }

    # Metrics compilation — collect from cache work_summary
    metrics_compilation = None
    work_summary = sd.get("work_summary", {})
    if not isinstance(work_summary, dict):
        work_summary = {}
    prs_merged = work_summary.get("prs_merged", [])
    if prs_merged or work_summary.get("deliverables") or work_summary.get("files_changed"):
        pr_nums = []
        for pr_info in prs_merged:
            if isinstance(pr_info, dict):
                pr_nums.append(pr_info.get("number", 0))
            elif isinstance(pr_info, int):
                pr_nums.append(pr_info)
        metrics_compilation = {
            "prs": len(pr_nums),
            "pr_numbers": sorted(set(pr_nums)),
            "files_changed": work_summary.get("files_changed", 0),
            "additions": work_summary.get("additions", 0),
            "deletions": work_summary.get("deletions", 0),
            "deliverables": work_summary.get("deliverables", []),
            "todos_count": len(sd.get("todos_snapshot", [])),
        }
    elif cpe.get("metriques"):
        # Fallback from knowledge-validation compilations
        cpe_m = cpe["metriques"]
        metrics_compilation = {
            "prs": cpe_m.get("prs", 0),
            "pr_numbers": cpe_m.get("pr_numbers", []),
            "files_changed": cpe_m.get("files_changed", 0),
            "additions": cpe_m.get("additions", 0),
            "deletions": cpe_m.get("deletions", 0),
            "deliverables": cpe_m.get("deliverables", []),
            "todos_count": cpe_m.get("todos_count", 0),
        }

    # Synthesize knowledge_grid if cache didn't have one
    if not knowledge_grid:
        knowledge_grid = _synthesize_grid(
            workflow, cache, stages_visited, current_stage, metrics_compilation
        )

    task = {
        "id": f"task-{issue_number}" if issue_number else f"task-{session_id}",
        "user_session_id": user_session_id,
        "task_number": issue_number,
        "title": issue_title,
        "description": workflow.get("description", ""),
        "branch": branch,
        "repo": repo,
        "session_id": session_id,
        "source_file": filename,
        "current_stage": current_stage,
        "current_stage_index": current_stage_index,
        "current_step": current_step,
        "project": workflow.get("project"),
        "stages_visited": stages_visited,
        "stage_count": len(stages_visited),
        "total_transitions": len(stage_history) if stage_history else len(stages_visited),
        "started_at": started_at,
        "updated_at": updated_at,
        "modifications_occurred": workflow.get("modifications_occurred", False),
        "validation_skipped_entirely": validation_skipped,
        "validation_summary": validation_summary,
        "unit_test_summary": test_summary,
        "stage_history": stage_history,
        "step_history": step_history,
        "validation_results": validation_results,
        "unit_tests": unit_tests,
        "knowledge_grid": knowledge_grid,
        "time_compilation": time_compilation,
        "metrics_compilation": metrics_compilation,
    }

    return task


def deduplicate_tasks(tasks):
    """Deduplicate tasks by task_number, keeping the most recent.

    Tasks with task_number=0 are kept as-is (session-only tasks).
    """
    by_task = {}
    no_task = []

    for task in tasks:
        num = task.get("task_number", 0)
        if not num:
            no_task.append(task)
            continue
        existing = by_task.get(num)
        if not existing:
            by_task[num] = task
        else:
            # Keep the one with the most recent updated_at
            if (task.get("updated_at") or "") > (existing.get("updated_at") or ""):
                by_task[num] = task

    return list(by_task.values()) + no_task


def compile_tasks(notes_dir, output_path):
    """Main compilation: scan caches → extract tasks → write JSON.

    Preserves enrichment data (metrics_compilation from enrich_from_github.py)
    that was previously written to tasks.json.

    Args:
        notes_dir: Path to notes/ directory.
        output_path: Path to write tasks.json.

    Returns:
        Number of tasks compiled.
    """
    # Load existing tasks.json to preserve enrichment data
    existing_enriched = {}
    if os.path.exists(output_path):
        try:
            with open(output_path, 'r') as f:
                existing = json.load(f)
            for t in existing.get("tasks", []):
                mc = t.get("metrics_compilation")
                if mc and mc.get("prs", 0) > 0:
                    existing_enriched[t["id"]] = mc
        except (json.JSONDecodeError, OSError):
            pass

    caches = load_runtime_caches(notes_dir)

    tasks = []
    caches_by_filename = {}
    for filename, cache in caches:
        task = extract_task_from_cache(filename, cache)
        if task:
            # Preserve enrichment data if task has no metrics but was enriched before
            task_mc = task.get("metrics_compilation")
            if (not task_mc or task_mc.get("prs", 0) == 0) and task["id"] in existing_enriched:
                task["metrics_compilation"] = existing_enriched[task["id"]]
                # Re-synthesize grid with enriched metrics if grid was synthesized
                kg = task.get("knowledge_grid", {})
                if kg.get("synthesized"):
                    sd = cache.get("session_data", {})
                    workflow = sd.get("task_workflow", {})
                    task["knowledge_grid"] = _synthesize_grid(
                        workflow, cache,
                        task["stages_visited"],
                        task["current_stage"],
                        task["metrics_compilation"],
                    )
            tasks.append(task)

    # Deduplicate by issue number
    tasks = deduplicate_tasks(tasks)

    # Sort by updated_at descending (most recent first)
    tasks.sort(key=lambda t: t.get("updated_at") or "", reverse=True)

    # Compute meta
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    meta = {
        "generated_at": now,
        "total_tasks": len(tasks),
        "with_task": sum(1 for t in tasks if t.get("task_number")),
        "with_validation": sum(1 for t in tasks if t.get("validation_summary")),
        "stages": [
            "initial", "plan", "analyze", "implement",
            "validation", "documentation", "approval", "completion",
        ],
        "sources": [
            "notes/session-runtime-*.json",
        ],
    }

    output = {
        "meta": meta,
        "tasks": tasks,
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)

    return len(tasks)


def compile_tasks_incremental(notes_dir, output_path, cache_files):
    """Incremental compilation: merge only specified caches into existing JSON.

    Preserves existing tasks (e.g. v2.0 demo baseline) and only adds/updates
    tasks from the specified cache files.

    Args:
        notes_dir: Path to notes/ directory.
        output_path: Path to tasks.json (read + write).
        cache_files: List of specific runtime cache file paths to process.

    Returns:
        Number of tasks added or updated.
    """
    # Load existing tasks.json
    existing_data = {"meta": {}, "tasks": []}
    if os.path.exists(output_path):
        try:
            with open(output_path, 'r') as f:
                existing_data = json.load(f)
        except (json.JSONDecodeError, OSError):
            pass

    existing_tasks = existing_data.get("tasks", [])
    # Index existing by id for merge
    by_id = {t["id"]: t for t in existing_tasks if "id" in t}

    updated = 0
    added = 0
    for filepath in cache_files:
        try:
            with open(filepath, 'r') as f:
                cache = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue

        filename = os.path.basename(filepath)
        task = extract_task_from_cache(filename, cache)
        if not task:
            continue

        task_id = task["id"]
        if task_id in by_id:
            by_id[task_id] = task
            updated += 1
        else:
            by_id[task_id] = task
            added += 1

    # Rebuild with deduplication
    all_tasks = deduplicate_tasks(list(by_id.values()))
    all_tasks.sort(key=lambda t: t.get("updated_at") or "", reverse=True)

    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    meta = existing_data.get("meta", {})
    meta["generated_at"] = now
    meta["total_tasks"] = len(all_tasks)
    meta["with_task"] = sum(1 for t in all_tasks if t.get("task_number"))
    meta["with_validation"] = sum(1 for t in all_tasks if t.get("validation_summary"))

    output = {"meta": meta, "tasks": all_tasks}
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"  [incremental] +{added} added, ~{updated} updated, {len(all_tasks)} total")
    return added + updated


def main():
    root = find_project_root()
    notes_dir = os.path.join(root, "notes")

    output = os.path.join(root, "docs", "data", "tasks.json")
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output = sys.argv[idx + 1]

    # --incremental <file1> [file2 ...]: merge only these caches
    if "--incremental" in sys.argv:
        idx = sys.argv.index("--incremental")
        files = sys.argv[idx + 1:]
        files = [os.path.join(root, f) if not os.path.isabs(f) else f for f in files]
        count = compile_tasks_incremental(notes_dir, output, files)
        print(f"Incremental: {count} tasks merged → {output}")
    else:
        count = compile_tasks(notes_dir, output)
        print(f"Compiled {count} tasks → {output}")


if __name__ == "__main__":
    main()
