#!/usr/bin/env python3
"""
Bridge: K_MIND memory → K_VALIDATION task JSON

Reads mindmap work nodes + near_memory summaries + far_memory messages
and compiles tasks.json for the session-review and task-workflow interfaces.

Mapping:
  - Mindmap work nodes → task identity + stage
  - Near memory summaries (via mind_memory_refs) → task title, description, timeline
  - Far memory messages (via far_memory_refs) → task content (future GitHub comments)

Stage mapping:
  work/en cours/<item>   → implement (active)
  work/validation/<item> → validation (awaiting review)
  work/approbation/<item> → completion (approved)

Usage:
  python3 Knowledge/K_VALIDATION/scripts/compile_tasks_from_mind.py
  python3 Knowledge/K_VALIDATION/scripts/compile_tasks_from_mind.py --output docs/data/tasks.json
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
K_MIND = PROJECT_ROOT / "Knowledge" / "K_MIND"
DEFAULT_OUTPUT = PROJECT_ROOT / "docs" / "data" / "tasks.json"

STAGE_MAP = {
    "en cours": "implement",
    "validation": "validation",
    "approbation": "completion",
}

STAGE_INDEX = {
    "initial": 0, "plan": 1, "analyze": 2, "implement": 3,
    "validation": 4, "documentation": 5, "approval": 6, "completion": 7,
}


def parse_work_nodes(mindmap_path):
    """Extract work nodes from mind_memory.md mermaid mindmap."""
    text = mindmap_path.read_text(encoding="utf-8")
    match = re.search(r"```mermaid\s*\n([\s\S]*?)```", text)
    if not match:
        return {}

    lines = match.group(1).split("\n")
    tasks = {}  # node_name -> {stage, children, depth}

    in_work = False
    work_indent = None
    current_stage = None
    stage_indent = None
    current_task = None
    task_indent = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        indent = len(line) - len(line.lstrip())

        # Find the top-level "work" node — direct child of root at indent 4
        # Skip "work" nodes nested deeper (e.g. inside session/near memory)
        if stripped == "work" and indent == 4 and not in_work:
            in_work = True
            work_indent = indent
            continue

        if not in_work:
            continue

        # Exit work section (same or less indent = sibling or parent)
        if indent <= work_indent:
            break

        # Stage level: direct children of work (work_indent + 2)
        if indent == work_indent + 2 and stripped in STAGE_MAP:
            current_stage = stripped
            stage_indent = indent
            current_task = None
            continue

        if current_stage is None:
            continue

        # Task level: direct children of stage (stage_indent + 2)
        if indent == stage_indent + 2:
            task_id = stripped.lower().replace(" ", "-")
            current_task = task_id
            task_indent = indent
            tasks[task_id] = {
                "name": stripped,
                "stage": STAGE_MAP[current_stage],
                "children": [],
            }
            continue

        # Sub-task: deeper than task (task_indent + 2 or more)
        if current_task and task_indent and indent > task_indent:
            tasks[current_task]["children"].append(stripped)

    return tasks


def load_near_memory(path):
    """Load near_memory.json summaries."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_far_memory(path):
    """Load far_memory.json messages."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def normalize_ref(ref):
    """Normalize a mind_memory_ref to match work node IDs."""
    # Remove prefixes like "knowledge::"
    ref = re.sub(r"^knowledge::", "", ref)
    # Remove "work::" prefix
    ref = re.sub(r"^work::", "", ref)
    # Remove stage prefix
    for stage in ("en cours::", "en_cours::", "validation::", "approbation::"):
        ref = ref.replace(stage, "")
    return ref.strip().lower().replace(" ", "-")


def match_summaries_to_tasks(tasks, near_data):
    """Map near_memory summaries to tasks via mind_memory_refs."""
    task_summaries = {tid: [] for tid in tasks}

    for summary in near_data.get("summaries", []):
        refs = summary.get("mind_memory_refs", [])
        for ref in refs:
            if "work::" not in ref and "work/" not in ref:
                continue
            normalized = normalize_ref(ref)
            # Try exact match
            if normalized in tasks:
                task_summaries[normalized].append(summary)
                continue
            # Try partial match
            for tid in tasks:
                if normalized in tid or tid in normalized:
                    task_summaries[tid].append(summary)
                    break

    return task_summaries


def compile_tasks(output_path=None):
    """Main compilation: mindmap + near + far → tasks.json."""
    mindmap_path = K_MIND / "mind" / "mind_memory.md"
    near_path = K_MIND / "sessions" / "near_memory.json"
    far_path = K_MIND / "sessions" / "far_memory.json"

    # Parse mindmap work nodes
    work_nodes = parse_work_nodes(mindmap_path)
    print(f"Found {len(work_nodes)} work nodes in mindmap")

    # Load session data
    near_data = load_near_memory(near_path)
    far_data = load_far_memory(far_path)
    session_id = near_data.get("session_id", "unknown")

    # Map summaries to tasks
    task_summaries = match_summaries_to_tasks(work_nodes, near_data)

    # Build task list
    task_list = []
    for i, (tid, node) in enumerate(work_nodes.items(), 1):
        summaries = task_summaries.get(tid, [])

        # Title from node name
        title = node["name"]

        # Description from first summary, or from children
        if summaries:
            description = summaries[0]["summary"]
        elif node["children"]:
            description = " | ".join(node["children"][:3])
        else:
            description = title

        # Timestamps from summaries
        timestamps = [s["timestamp"] for s in summaries if "timestamp" in s]
        started_at = min(timestamps) if timestamps else near_data["summaries"][0]["timestamp"] if near_data["summaries"] else None
        updated_at = max(timestamps) if timestamps else started_at

        # Far memory message IDs linked via summaries
        far_refs = []
        for s in summaries:
            far_refs.extend(s.get("far_memory_refs", []))

        # Far memory messages count (future GitHub comments)
        message_count = len(far_refs)

        task = {
            "id": f"task-{i}",
            "title": title,
            "description": description,
            "current_stage": node["stage"],
            "current_stage_index": STAGE_INDEX.get(node["stage"], 0),
            "project": "Knowledge",
            "session_id": session_id,
            "branch": "main",
            "repo": "packetqc/K_DOCS",
            "issue_number": None,
            "source": "mindmap",
            "children": node["children"],
            "near_memory_ids": [s["id"] for s in summaries],
            "far_memory_ids": sorted(set(far_refs)),
            "message_count": message_count,
            "started_at": started_at,
            "updated_at": updated_at,
            "stages_visited": [node["stage"]],
            "stage_count": 1,
        }
        task_list.append(task)

    # Session summary for session-review interface
    all_summaries = near_data.get("summaries", [])
    all_messages = far_data.get("messages", [])

    session_data = {
        "id": session_id,
        "title": f"Session {session_id[:8]}",
        "project": "Knowledge",
        "branch": "main",
        "repo": "packetqc/K_DOCS",
        "started_at": all_summaries[0]["timestamp"] if all_summaries else None,
        "updated_at": all_summaries[-1]["timestamp"] if all_summaries else None,
        "message_count": len(all_messages),
        "summary_count": len(all_summaries),
        "task_count": len(task_list),
        "stages": {
            "implement": sum(1 for t in task_list if t["current_stage"] == "implement"),
            "validation": sum(1 for t in task_list if t["current_stage"] == "validation"),
            "completion": sum(1 for t in task_list if t["current_stage"] == "completion"),
        },
    }

    # Output
    output = {
        "meta": {
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "total_tasks": len(task_list),
            "source": "K_MIND mindmap + near_memory + far_memory",
            "session_id": session_id,
            "stages": list(STAGE_INDEX.keys()),
        },
        "tasks": task_list,
        "sessions": [session_data],
    }

    out = output_path or DEFAULT_OUTPUT
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Compiled {len(task_list)} tasks, 1 session → {out}")
    print(f"  implement: {session_data['stages']['implement']}")
    print(f"  validation: {session_data['stages']['validation']}")
    print(f"  completion: {session_data['stages']['completion']}")
    print(f"  far_memory messages: {len(all_messages)}")
    print(f"  near_memory summaries: {len(all_summaries)}")

    return output


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != "--output" else None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            out = sys.argv[idx + 1]
    compile_tasks(out)
