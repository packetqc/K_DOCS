#!/usr/bin/env python3
"""Generate demo session entries that align with the 5 demo tasks.

Creates sessions.json entries with v2.0 features:
- user_session_id (internal session identity)
- collateral_tasks (auto-generated sub-tasks)
- system_sessions (N system sessions = 1 user session)
- Aggregation of multi-system-session user sessions

Usage:
    python3 scripts/generate_demo_sessions.py
    python3 scripts/generate_demo_sessions.py --inject  # inject into existing sessions.json
"""

import json
import os
import sys
from datetime import datetime, timezone


def create_demo_sessions():
    """Create 5 demo sessions aligned with the 5 demo task runtime caches."""

    sessions = []

    # ─── Demo 1: OAuth2 Authentication (demo-001) ───
    # Completed session, 1 user session = 1 system session
    sessions.append({
        "id": "2026-03-07_oauth2-auth-YC3EK",
        "user_session_id": "us-20260307-a1b2c3",
        "date": "2026-03-07",
        "title": "Implémenter le système d'authentification OAuth2",
        "branch": "claude/oauth2-auth-YC3EK",
        "type": "🚀 Feature",
        "request_type": "feature",
        "engineering_stage": "implementation",
        "summary": "OAuth2 avec Google et GitHub providers, refresh token, gestion des sessions.",
        "prs": [
            {
                "number": 38, "title": "feat: OAuth2 core module + Google provider",
                "created_at": "2026-03-07T10:30:00Z", "merged_at": "2026-03-07T12:15:00Z",
                "additions": 850, "deletions": 12, "changed_files": 8, "commits": 4, "sub_type": "feat"
            },
            {
                "number": 39, "title": "feat: GitHub OAuth2 provider + callback handlers",
                "created_at": "2026-03-07T12:30:00Z", "merged_at": "2026-03-07T13:45:00Z",
                "additions": 420, "deletions": 35, "changed_files": 5, "commits": 3, "sub_type": "feat"
            },
            {
                "number": 40, "title": "fix: token refresh flow + session middleware",
                "created_at": "2026-03-07T15:00:00Z", "merged_at": "2026-03-07T16:00:00Z",
                "additions": 310, "deletions": 85, "changed_files": 4, "commits": 2, "sub_type": "fix"
            }
        ],
        "issues": [42],
        "lessons": [
            "Token refresh needs dedicated retry logic — single-attempt refresh causes race conditions",
            "OAuth2 state parameter must be cryptographically random, not predictable UUID"
        ],
        "comments": [
            {"author": "claude-bot", "created_at": "2026-03-07T09:20:00Z", "type": "bot", "status": "completed",
             "step_name": "Task received — OAuth2 implementation", "preview": "Implementing OAuth2 with Google and GitHub providers",
             "body_lines": ["Implementing OAuth2 with Google and GitHub providers", "Includes refresh token and session management"]},
            {"author": "martin-paquet", "created_at": "2026-03-07T09:35:00Z", "type": "user", "status": None,
             "step_name": "", "preview": "Approuvé. Commencer par Google provider.",
             "body_lines": ["Approuvé. Commencer par Google provider.", "Ensuite GitHub, puis le refresh token."]},
            {"author": "claude-bot", "created_at": "2026-03-07T16:30:00Z", "type": "bot", "status": "completed",
             "step_name": "Completion — all tests passing", "preview": "OAuth2 implementation complete",
             "body_lines": ["All 7 tests passing", "3 PRs merged", "Documentation updated"]}
        ],
        "collateral_tasks": [],
        "pr_count": 3,
        "has_notes": True,
        "has_issue": True,
        "sync_score": 1.0,
        "source_file": "session-runtime-demo-001.json",
        "issue_number": 42,
        "issue_created_at": "2026-03-07T09:15:00Z",
        "first_activity_time": "2026-03-07T09:15:00Z",
        "last_activity_time": "2026-03-07T16:42:00Z",
        "first_pr_time": "2026-03-07T10:30:00Z",
        "last_pr_time": "2026-03-07T16:00:00Z",
        "active_minutes": 330,
        "calendar_minutes": 447,
        "time_block": "morning",
        "total_additions": 1580,
        "total_deletions": 132,
        "total_lines": 1712,
        "total_files_changed": 17,
        "total_commits": 9,
        "lines_per_hour": 311,
        "commits_per_hour": 1.6,
        "files_per_hour": 3.1,
        "session_kind": "original",
        "tree_depth": 0,
        "parent_issues": [],
        "children_issues": [],
        "related_issues": []
    })

    # ─── Demo 2: Pagination Bug Fix (demo-002) ───
    # In-progress session with 1 collateral task auto-generated
    sessions.append({
        "id": "2026-03-06_pagination-fix-BV2K6",
        "user_session_id": "us-20260306-d4e5f6",
        "date": "2026-03-06",
        "title": "Fix pagination cursor reset on filter change",
        "branch": "claude/pagination-fix-BV2K6",
        "type": "🔧 Fix",
        "request_type": "fix",
        "engineering_stage": "implementation",
        "summary": "Le curseur de pagination ne se réinitialise pas quand l'utilisateur change de filtre.",
        "prs": [
            {
                "number": 50, "title": "fix: reset pagination cursor on filter change",
                "created_at": "2026-03-06T14:00:00Z", "merged_at": "2026-03-06T15:30:00Z",
                "additions": 145, "deletions": 23, "changed_files": 3, "commits": 2, "sub_type": "fix"
            },
            {
                "number": 51, "title": "test: add regression tests for pagination reset",
                "created_at": "2026-03-06T15:45:00Z", "merged_at": None,
                "additions": 89, "deletions": 0, "changed_files": 2, "commits": 1, "sub_type": "test"
            }
        ],
        "issues": [55, 56],
        "lessons": [],
        "comments": [
            {"author": "claude-bot", "created_at": "2026-03-06T13:30:00Z", "type": "bot", "status": "in_progress",
             "step_name": "Implementing pagination fix", "preview": "Fixing cursor reset logic",
             "body_lines": ["Fixing pagination cursor that doesn't reset on filter change", "Root cause: state not clearing in useEffect cleanup"]}
        ],
        "collateral_tasks": [
            {
                "id": "ct-001",
                "title": "Fix stale cache on filter change",
                "type": "fix",
                "status": "completed",
                "issue_number": 56,
                "created_at": "2026-03-06T14:45:00Z",
                "pr_numbers": [51]
            }
        ],
        "pr_count": 2,
        "has_notes": False,
        "has_issue": True,
        "sync_score": 0.5,
        "source_file": "session-runtime-demo-002.json",
        "issue_number": 55,
        "issue_created_at": "2026-03-06T13:30:00Z",
        "first_activity_time": "2026-03-06T13:30:00Z",
        "last_activity_time": "2026-03-06T16:00:00Z",
        "first_pr_time": "2026-03-06T14:00:00Z",
        "last_pr_time": "2026-03-06T15:45:00Z",
        "active_minutes": 120,
        "calendar_minutes": 150,
        "time_block": "afternoon",
        "total_additions": 234,
        "total_deletions": 23,
        "total_lines": 257,
        "total_files_changed": 5,
        "total_commits": 3,
        "lines_per_hour": 129,
        "commits_per_hour": 1.5,
        "files_per_hour": 2.5,
        "session_kind": "original",
        "tree_depth": 0,
        "parent_issues": [],
        "children_issues": [],
        "related_issues": [
            {"number": 56, "title": "Fix stale cache on filter change", "state": "closed", "labels": ["task"]}
        ]
    })

    # ─── Demo 3: Dark Mode (demo-003) ───
    # Session with 2 system sessions (compaction happened) → user_session_id links them
    # Parent session
    sessions.append({
        "id": "2026-03-05_dark-mode-R7X3P",
        "user_session_id": "us-20260305-g7h8i9",
        "date": "2026-03-05",
        "title": "Ajouter le support dark mode complet",
        "branch": "claude/dark-mode-R7X3P",
        "type": "🚀 Feature",
        "request_type": "feature",
        "engineering_stage": "implementation",
        "summary": "Support dark mode avec détection automatique OS + toggle manuel. CSS variables et thèmes personnalisés.",
        "prs": [
            {
                "number": 58, "title": "feat: CSS custom properties for theming",
                "created_at": "2026-03-05T09:00:00Z", "merged_at": "2026-03-05T10:30:00Z",
                "additions": 520, "deletions": 180, "changed_files": 12, "commits": 3, "sub_type": "feat"
            },
            {
                "number": 59, "title": "feat: dark mode toggle component",
                "created_at": "2026-03-05T10:45:00Z", "merged_at": "2026-03-05T12:00:00Z",
                "additions": 280, "deletions": 15, "changed_files": 4, "commits": 2, "sub_type": "feat"
            }
        ],
        "issues": [63],
        "lessons": ["CSS custom properties propagate to Shadow DOM — no extra effort needed"],
        "comments": [],
        "collateral_tasks": [
            {
                "id": "ct-002",
                "title": "Ajuster les couleurs du header en dark mode",
                "type": "fix",
                "status": "completed",
                "issue_number": 64,
                "created_at": "2026-03-05T11:30:00Z",
                "pr_numbers": [60]
            },
            {
                "id": "ct-003",
                "title": "Mettre à jour les screenshots documentation",
                "type": "doc",
                "status": "pending",
                "issue_number": None,
                "created_at": "2026-03-05T14:00:00Z",
                "pr_numbers": []
            }
        ],
        "pr_count": 2,
        "has_notes": True,
        "has_issue": True,
        "sync_score": 0.75,
        "source_file": "session-runtime-demo-003.json",
        "issue_number": 63,
        "issue_created_at": "2026-03-05T08:45:00Z",
        "first_activity_time": "2026-03-05T08:45:00Z",
        "last_activity_time": "2026-03-05T12:00:00Z",
        "first_pr_time": "2026-03-05T09:00:00Z",
        "last_pr_time": "2026-03-05T12:00:00Z",
        "active_minutes": 165,
        "calendar_minutes": 195,
        "time_block": "morning",
        "total_additions": 800,
        "total_deletions": 195,
        "total_lines": 995,
        "total_files_changed": 16,
        "total_commits": 5,
        "lines_per_hour": 362,
        "commits_per_hour": 1.8,
        "files_per_hour": 5.8,
        "session_kind": "original",
        "tree_depth": 0,
        "parent_issues": [],
        "children_issues": [65],
        "related_issues": [
            {"number": 64, "title": "Ajuster couleurs header dark mode", "state": "closed", "labels": ["task"]},
            {"number": 65, "title": "Dark mode — suite après compaction", "state": "closed", "labels": ["SESSION"]}
        ],
        # Aggregated: parent collects child session data
        "aggregated": {
            "prs": [
                {"number": 58, "title": "feat: CSS custom properties for theming",
                 "created_at": "2026-03-05T09:00:00Z", "merged_at": "2026-03-05T10:30:00Z",
                 "additions": 520, "deletions": 180, "changed_files": 12, "commits": 3, "sub_type": "feat"},
                {"number": 59, "title": "feat: dark mode toggle component",
                 "created_at": "2026-03-05T10:45:00Z", "merged_at": "2026-03-05T12:00:00Z",
                 "additions": 280, "deletions": 15, "changed_files": 4, "commits": 2, "sub_type": "feat"},
                {"number": 60, "title": "fix: header dark mode colors",
                 "created_at": "2026-03-05T13:30:00Z", "merged_at": "2026-03-05T14:15:00Z",
                 "additions": 95, "deletions": 42, "changed_files": 3, "commits": 1, "sub_type": "fix"},
                {"number": 61, "title": "feat: OS dark mode auto-detection",
                 "created_at": "2026-03-05T14:30:00Z", "merged_at": "2026-03-05T15:45:00Z",
                 "additions": 180, "deletions": 20, "changed_files": 3, "commits": 2, "sub_type": "feat"}
            ],
            "collateral_tasks": [
                {"id": "ct-002", "title": "Ajuster les couleurs du header en dark mode", "type": "fix", "status": "completed",
                 "issue_number": 64, "created_at": "2026-03-05T11:30:00Z", "pr_numbers": [60]},
                {"id": "ct-003", "title": "Mettre à jour les screenshots documentation", "type": "doc", "status": "pending",
                 "issue_number": None, "created_at": "2026-03-05T14:00:00Z", "pr_numbers": []}
            ],
            "system_sessions": ["claude/dark-mode-R7X3P", "claude/dark-mode-cont-M2N4Q"],
            "total_additions": 1075,
            "total_deletions": 257,
            "total_files_changed": 22,
            "total_commits": 8,
            "total_lines": 1332,
            "active_minutes": 285,
            "calendar_minutes": 420,
            "pr_count": 4,
            "first_activity_time": "2026-03-05T08:45:00Z",
            "last_activity_time": "2026-03-05T15:45:00Z",
            "children_count": 1,
            "children_issue_numbers": [65]
        }
    })

    # Child session (continuation after compaction)
    sessions.append({
        "id": "2026-03-05_dark-mode-cont-M2N4Q",
        "user_session_id": "us-20260305-g7h8i9",  # Same user_session_id!
        "date": "2026-03-05",
        "title": "Dark mode — suite après compaction",
        "branch": "claude/dark-mode-cont-M2N4Q",
        "type": "🚀 Feature",
        "request_type": "feature",
        "engineering_stage": "implementation",
        "summary": "Continuation après compaction système — OS auto-detection et corrections header.",
        "prs": [
            {
                "number": 60, "title": "fix: header dark mode colors",
                "created_at": "2026-03-05T13:30:00Z", "merged_at": "2026-03-05T14:15:00Z",
                "additions": 95, "deletions": 42, "changed_files": 3, "commits": 1, "sub_type": "fix"
            },
            {
                "number": 61, "title": "feat: OS dark mode auto-detection",
                "created_at": "2026-03-05T14:30:00Z", "merged_at": "2026-03-05T15:45:00Z",
                "additions": 180, "deletions": 20, "changed_files": 3, "commits": 2, "sub_type": "feat"
            }
        ],
        "issues": [65, 63],
        "lessons": [],
        "comments": [],
        "collateral_tasks": [],
        "pr_count": 2,
        "has_notes": False,
        "has_issue": True,
        "sync_score": 1.0,
        "source_file": None,
        "issue_number": 65,
        "issue_created_at": "2026-03-05T13:15:00Z",
        "first_activity_time": "2026-03-05T13:15:00Z",
        "last_activity_time": "2026-03-05T15:45:00Z",
        "first_pr_time": "2026-03-05T13:30:00Z",
        "last_pr_time": "2026-03-05T15:45:00Z",
        "active_minutes": 120,
        "calendar_minutes": 150,
        "time_block": "afternoon",
        "total_additions": 275,
        "total_deletions": 62,
        "total_lines": 337,
        "total_files_changed": 6,
        "total_commits": 3,
        "lines_per_hour": 135,
        "commits_per_hour": 1.2,
        "files_per_hour": 2.4,
        "session_kind": "continuation",
        "tree_depth": 1,
        "parent_issues": [63],
        "children_issues": [],
        "related_issues": [
            {"number": 63, "title": "Ajouter le support dark mode complet", "state": "closed", "labels": ["SESSION"]}
        ]
    })

    # ─── Demo 4: SQLite → PostgreSQL Migration (demo-004) ───
    # Complex session: 3 system sessions (crash + recovery), multiple collateral tasks
    sessions.append({
        "id": "2026-03-04_sqlite-postgres-K9L2M",
        "user_session_id": "us-20260304-j1k2l3",
        "date": "2026-03-04",
        "title": "Migration SQLite vers PostgreSQL",
        "branch": "claude/sqlite-postgres-K9L2M",
        "type": "🔄 Enhancement",
        "request_type": "enhancement",
        "engineering_stage": "implementation",
        "summary": "Migration complète de la base SQLite vers PostgreSQL. Schéma, ORM, queries, tests de performance.",
        "prs": [
            {
                "number": 66, "title": "feat: PostgreSQL schema + migration scripts",
                "created_at": "2026-03-04T08:30:00Z", "merged_at": "2026-03-04T10:00:00Z",
                "additions": 1200, "deletions": 45, "changed_files": 15, "commits": 5, "sub_type": "feat"
            },
            {
                "number": 67, "title": "refactor: ORM queries SQLite → PostgreSQL",
                "created_at": "2026-03-04T10:15:00Z", "merged_at": "2026-03-04T12:30:00Z",
                "additions": 890, "deletions": 720, "changed_files": 22, "commits": 8, "sub_type": "refactor"
            },
            {
                "number": 68, "title": "fix: performance regression in bulk insert",
                "created_at": "2026-03-04T14:00:00Z", "merged_at": "2026-03-04T15:00:00Z",
                "additions": 150, "deletions": 85, "changed_files": 3, "commits": 2, "sub_type": "fix"
            },
            {
                "number": 69, "title": "test: PostgreSQL integration tests",
                "created_at": "2026-03-04T15:15:00Z", "merged_at": "2026-03-04T16:30:00Z",
                "additions": 480, "deletions": 120, "changed_files": 8, "commits": 3, "sub_type": "test"
            },
            {
                "number": 70, "title": "doc: migration guide and connection config",
                "created_at": "2026-03-04T16:45:00Z", "merged_at": "2026-03-04T17:15:00Z",
                "additions": 210, "deletions": 0, "changed_files": 3, "commits": 1, "sub_type": "doc"
            }
        ],
        "issues": [71, 72, 73],
        "lessons": [
            "PostgreSQL COPY is 10x faster than individual INSERTs for bulk data",
            "Always benchmark with production-sized dataset, not test fixtures",
            "Connection pooling config must match expected concurrent load"
        ],
        "comments": [
            {"author": "claude-bot", "created_at": "2026-03-04T08:15:00Z", "type": "bot", "status": "completed",
             "step_name": "Migration plan approved", "preview": "Starting SQLite to PostgreSQL migration",
             "body_lines": ["Migration plan: schema → ORM → queries → tests → docs", "Estimated: 1 day"]},
            {"author": "martin-paquet", "created_at": "2026-03-04T13:00:00Z", "type": "user", "status": None,
             "step_name": "", "preview": "Attention au performance regression",
             "body_lines": ["Le bulk insert doit rester performant", "Tester avec le dataset de production"]},
            {"author": "claude-bot", "created_at": "2026-03-04T15:00:00Z", "type": "bot", "status": "completed",
             "step_name": "Performance fix — COPY command", "preview": "Bulk insert performance restored with COPY",
             "body_lines": ["Replaced individual INSERTs with COPY command", "Performance: 10x improvement", "All integration tests passing"]}
        ],
        "collateral_tasks": [
            {
                "id": "ct-004",
                "title": "Fix connection pool exhaustion under load",
                "type": "fix",
                "status": "completed",
                "issue_number": 72,
                "created_at": "2026-03-04T12:45:00Z",
                "pr_numbers": [68]
            },
            {
                "id": "ct-005",
                "title": "Add database health check endpoint",
                "type": "feature",
                "status": "completed",
                "issue_number": 73,
                "created_at": "2026-03-04T15:30:00Z",
                "pr_numbers": [69]
            }
        ],
        "pr_count": 5,
        "has_notes": True,
        "has_issue": True,
        "sync_score": 0.9,
        "source_file": "session-runtime-demo-004.json",
        "issue_number": 71,
        "issue_created_at": "2026-03-04T08:00:00Z",
        "first_activity_time": "2026-03-04T08:00:00Z",
        "last_activity_time": "2026-03-04T17:15:00Z",
        "first_pr_time": "2026-03-04T08:30:00Z",
        "last_pr_time": "2026-03-04T17:15:00Z",
        "active_minutes": 450,
        "calendar_minutes": 555,
        "time_block": "morning",
        "total_additions": 2930,
        "total_deletions": 970,
        "total_lines": 3900,
        "total_files_changed": 51,
        "total_commits": 19,
        "lines_per_hour": 520,
        "commits_per_hour": 2.5,
        "files_per_hour": 6.8,
        "session_kind": "original",
        "tree_depth": 0,
        "parent_issues": [],
        "children_issues": [],
        "related_issues": [
            {"number": 72, "title": "Fix connection pool exhaustion", "state": "closed", "labels": ["task"]},
            {"number": 73, "title": "Database health check endpoint", "state": "closed", "labels": ["task"]}
        ]
    })

    # ─── Demo 5: REST API User Management (demo-005) ───
    # Fresh session, just started — no PRs yet
    sessions.append({
        "id": "2026-03-08_user-api-BV2K6",
        "user_session_id": "us-20260308-m4n5o6",
        "date": "2026-03-08",
        "title": "REST API pour la gestion des utilisateurs",
        "branch": "claude/user-api-BV2K6",
        "type": "🚀 Feature",
        "request_type": "feature",
        "engineering_stage": "analysis",
        "summary": "API REST complète pour le CRUD utilisateurs avec validation, rôles et permissions.",
        "prs": [],
        "issues": [78],
        "lessons": [],
        "comments": [
            {"author": "claude-bot", "created_at": "2026-03-08T10:00:00Z", "type": "bot", "status": "in_progress",
             "step_name": "Task received — REST API user management", "preview": "Analysing requirements for user management API",
             "body_lines": ["Received request for REST API user management", "Currently in analysis phase"]}
        ],
        "collateral_tasks": [],
        "pr_count": 0,
        "has_notes": False,
        "has_issue": True,
        "sync_score": 0.0,
        "source_file": "session-runtime-demo-005.json",
        "issue_number": 78,
        "issue_created_at": "2026-03-08T10:00:00Z",
        "first_activity_time": "2026-03-08T10:00:00Z",
        "last_activity_time": "2026-03-08T10:15:00Z",
        "first_pr_time": None,
        "last_pr_time": None,
        "active_minutes": 15,
        "calendar_minutes": 15,
        "time_block": "morning",
        "total_additions": 0,
        "total_deletions": 0,
        "total_lines": 0,
        "total_files_changed": 0,
        "total_commits": 0,
        "lines_per_hour": None,
        "commits_per_hour": None,
        "files_per_hour": None,
        "session_kind": "original",
        "tree_depth": 0,
        "parent_issues": [],
        "children_issues": [],
        "related_issues": []
    })

    return sessions


def inject_into_sessions_json(output_path="docs/data/sessions.json"):
    """Inject demo sessions into the existing sessions.json."""

    # Load existing
    existing = {"meta": {}, "sessions": [], "issue_labels": {}}
    if os.path.exists(output_path):
        with open(output_path, "r", encoding="utf-8") as f:
            existing = json.load(f)

    demo_sessions = create_demo_sessions()

    # Remove existing demos (by user_session_id prefix "us-")
    real_sessions = [
        s for s in existing.get("sessions", [])
        if not (s.get("user_session_id") or "").startswith("us-2026030")
        or s.get("user_session_id") is None
    ]

    # Add demos
    all_sessions = demo_sessions + real_sessions

    # Sort by date desc
    all_sessions.sort(
        key=lambda s: (s["date"], s.get("last_activity_time") or "", s.get("pr_count", 0)),
        reverse=True
    )

    # Update meta
    existing["meta"]["total_sessions"] = len(all_sessions)
    existing["meta"]["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    existing["sessions"] = all_sessions

    # Add demo issue labels
    demo_labels = {
        "42": {"label": "SESSION", "color": ""},
        "55": {"label": "SESSION", "color": ""},
        "56": {"label": "task", "color": ""},
        "63": {"label": "SESSION", "color": ""},
        "64": {"label": "task", "color": ""},
        "65": {"label": "SESSION", "color": ""},
        "71": {"label": "SESSION", "color": ""},
        "72": {"label": "task", "color": ""},
        "73": {"label": "task", "color": ""},
        "78": {"label": "SESSION", "color": ""},
    }
    existing.setdefault("issue_labels", {}).update(demo_labels)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

    print(f"Injected {len(demo_sessions)} demo sessions into {output_path}")
    print(f"  Total sessions: {len(all_sessions)}")
    print(f"  Demo sessions with user_session_id: {sum(1 for s in demo_sessions if s.get('user_session_id'))}")
    print(f"  Demo sessions with collateral_tasks: {sum(1 for s in demo_sessions if s.get('collateral_tasks'))}")
    print(f"  Demo multi-system-session example: us-20260305-g7h8i9 (2 system sessions → 1 user session)")


if __name__ == "__main__":
    if "--inject" in sys.argv:
        inject_into_sessions_json()
    else:
        sessions = create_demo_sessions()
        print(json.dumps(sessions, indent=2, ensure_ascii=False))
