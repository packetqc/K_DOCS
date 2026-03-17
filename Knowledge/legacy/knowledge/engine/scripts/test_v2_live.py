#!/usr/bin/env python3
"""test_v2_live.py — Live integration test for v2.0 session system.

Simulates two scenarios without user interaction:
  1. Single user request: creates session issue, posts progression,
     generates a collateral task with linked GitHub issue
  2. Interactive user request: creates session issue, posts multiple
     steps with ⏳→✅ lifecycle, generates 2 collateral tasks,
     publishes knowledge grid, demonstrates the full pipeline

All artifacts are created in GitHub (issues, comments, cross-refs)
and compiled into sessions.json for the viewer.

Usage:
    python3 scripts/test_v2_live.py

Authors: Martin Paquet, Claude (Anthropic)
License: MIT
"""

import json
import os
import sys
import time
import hashlib
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gh_helper import GitHubHelper
from session_issue_sync import SessionSync
from collateral_sync import CollateralSync, _find_project_root

REPO = "packetqc/knowledge"


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _usid():
    """Generate a user_session_id."""
    h = hashlib.md5(str(time.time()).encode()).hexdigest()[:6]
    d = datetime.now(timezone.utc).strftime("%Y%m%d")
    return f"us-{d}-{h}"


def print_step(n, msg):
    print(f"\n{'='*60}")
    print(f"  STEP {n}: {msg}")
    print(f"{'='*60}")


def run_test_single_request(gh):
    """Test 1: Single user request with 1 collateral task."""
    print_step("1A", "Creating session issue — single request")

    result = gh.issue_create(
        repo=REPO,
        title="[TEST-v2.0] Ajouter validation email au formulaire d'inscription",
        body=(
            "**Test v2.0 session system — demande unique**\n\n"
            "Ajouter la validation d'email (format + domaine) au formulaire "
            "d'inscription utilisateur.\n\n"
            f"- `user_session_id`: sera généré\n"
            f"- Date: {_now()}\n"
            f"- Type: `fix`\n\n"
            "*Issue créée automatiquement par test_v2_live.py*"
        ),
        labels=["SESSION", "test-v2"],
    )

    if not result.get("created"):
        print(f"  ERROR: Issue creation failed: {result}")
        return None

    issue_num = result["number"]
    print(f"  Issue #{issue_num} created: {result['html_url']}")

    # Initialize session sync
    sync = SessionSync(REPO, issue_number=issue_num)
    usid = _usid()

    # Post user message
    print_step("1B", "Posting user message")
    sync.post_user(
        "Ajouter validation email au formulaire d'inscription",
        "Demande initiale"
    )
    time.sleep(1)

    # Start step
    print_step("1C", "Starting implementation step (⏳)")
    cid = sync.start_step(
        "Implémenter la validation email",
        "Ajout regex validation + vérification DNS du domaine"
    )
    time.sleep(1)

    # Complete step
    print_step("1D", "Completing step (✅)")
    sync.complete_step(
        cid, "Implémenter la validation email",
        "Regex validation ajoutée + DNS check du domaine.\n"
        "Fichiers modifiés: `src/validators/email.py`, `tests/test_email.py`"
    )
    time.sleep(1)

    # Create collateral task
    print_step("1E", "Creating collateral task — auto-detected fix")
    ct_result = gh.issue_create(
        repo=REPO,
        title="[collateral] Fix regex edge case pour emails avec '+' ",
        body=(
            f"**Parent session issue:** #{issue_num}\n"
            f"**Collateral task ID:** `ct-001`\n"
            f"**Type:** `fix`\n\n"
            "Découvert pendant l'implémentation: la regex ne gère pas "
            "les emails avec `+` (ex: user+tag@example.com).\n\n"
            f"*Auto-generated collateral task — {_now()}*"
        ),
        labels=["task", "collateral", "test-v2"],
    )

    ct_issue = ct_result.get("number", 0)
    print(f"  Collateral issue #{ct_issue} created")

    # Link collateral to parent
    if ct_issue:
        gh.issue_comment_post(
            REPO, issue_num,
            f"**Collateral task created:** #{ct_issue}\n"
            f"> Fix regex edge case pour emails avec '+'\n\n"
            f"*Auto-linked by session system v2.0*"
        )
        # Notify on parent via sync
        sync.post_collateral_created(
            "Fix regex edge case pour emails avec '+'",
            "fix",
            issue_number=ct_issue
        )
    time.sleep(1)

    # Post knowledge grid
    print_step("1F", "Publishing knowledge validation grid")
    grid = (
        "| # | Question | Résultat |\n"
        "|---|----------|----------|\n"
        "| 1 | Démarrage session | ✅ Vrai |\n"
        "| 2 | Méthodologie | ✅ Vrai |\n"
        "| 3 | Grille publiée | ✅ Vrai |\n"
    )
    sync.post_knowledge_grid(grid, usid)
    time.sleep(1)

    # Post summary
    print_step("1G", "Posting session summary")
    sync.post_summary(
        "### Résumé de session\n"
        "- **Demande:** Validation email au formulaire d'inscription\n"
        "- **Résultat:** Implémenté avec regex + DNS check\n"
        f"- **Tâche collatérale:** #{ct_issue} (fix regex edge case)\n"
        f"- **user_session_id:** `{usid}`\n"
        "- **Temps actif:** ~25 min\n"
    )
    time.sleep(1)

    # Close issue
    print_step("1H", "Closing session issue with report")
    deliveries = [
        (f"Issue #{issue_num}", "✅ complétée"),
    ]
    if ct_issue:
        deliveries.append((f"Collateral #{ct_issue}", "✅ créée & liée"))
    sync.close_with_report(deliveries)

    # Close collateral too
    if ct_issue:
        gh.issue_close(REPO, ct_issue)

    print(f"\n  ✅ Test 1 COMPLETE — Issue #{issue_num} closed")
    return {
        "issue_number": issue_num,
        "collateral_issue": ct_issue,
        "user_session_id": usid,
        "type": "single",
    }


def run_test_interactive_request(gh):
    """Test 2: Interactive user request with multiple steps + 2 collateral."""
    print_step("2A", "Creating session issue — interactive request")

    result = gh.issue_create(
        repo=REPO,
        title="[TEST-v2.0] Refactoring du module de cache distribué",
        body=(
            "**Test v2.0 session system — demande interactive**\n\n"
            "Refactoring complet du module de cache distribué:\n"
            "1. Analyse de l'architecture actuelle\n"
            "2. Design nouveau pattern (Strategy)\n"
            "3. Implémentation Redis + Memcached providers\n"
            "4. Tests de performance\n"
            "5. Documentation API\n\n"
            f"- Date: {_now()}\n"
            f"- Type: `enhancement`\n\n"
            "*Issue créée automatiquement par test_v2_live.py*"
        ),
        labels=["SESSION", "test-v2"],
    )

    if not result.get("created"):
        print(f"  ERROR: Issue creation failed: {result}")
        return None

    issue_num = result["number"]
    print(f"  Issue #{issue_num} created: {result['html_url']}")

    sync = SessionSync(REPO, issue_number=issue_num)
    usid = _usid()

    # User message
    print_step("2B", "Posting user message")
    sync.post_user(
        "Refactoring du module de cache distribué — session interactive",
        "Demande interactive"
    )
    time.sleep(1)

    # Step 1: Analysis
    print_step("2C", "Step 1 — Analysis (⏳→✅)")
    cid1 = sync.start_step(
        "Analyser l'architecture du cache actuel",
        "Audit des patterns, dépendances, et points de contention"
    )
    time.sleep(1)
    sync.complete_step(
        cid1, "Analyser l'architecture du cache actuel",
        "Architecture auditée: singleton pattern, couplage fort avec Redis.\n"
        "Recommandation: Strategy pattern pour supporter multi-provider."
    )
    time.sleep(1)

    # Step 2: Design
    print_step("2D", "Step 2 — Design (⏳→✅)")
    cid2 = sync.start_step(
        "Concevoir le pattern Strategy pour le cache",
        "Interface CacheProvider + adapters Redis/Memcached/InMemory"
    )
    time.sleep(1)
    sync.complete_step(
        cid2, "Concevoir le pattern Strategy pour le cache",
        "Design complété:\n"
        "- `CacheProvider` interface abstraite\n"
        "- `RedisCacheProvider` adapter\n"
        "- `MemcachedCacheProvider` adapter\n"
        "- `InMemoryCacheProvider` pour tests\n"
        "- Factory pattern pour l'instanciation"
    )
    time.sleep(1)

    # Collateral 1: discovered during design
    print_step("2E", "Collateral task 1 — config migration")
    ct1_result = gh.issue_create(
        repo=REPO,
        title="[collateral] Migrer la config cache de .env vers YAML",
        body=(
            f"**Parent session issue:** #{issue_num}\n"
            f"**Collateral task ID:** `ct-001`\n"
            f"**Type:** `chore`\n\n"
            "Découvert pendant le design: la config cache est en .env "
            "(flat), incompatible avec le multi-provider.\n"
            "Migrer vers `config/cache.yaml` avec structure hiérarchique.\n\n"
            f"*Auto-generated collateral task — {_now()}*"
        ),
        labels=["task", "collateral", "test-v2"],
    )
    ct1_num = ct1_result.get("number", 0)
    if ct1_num:
        gh.issue_comment_post(
            REPO, issue_num,
            f"**Collateral task created:** #{ct1_num}\n"
            f"> Migrer la config cache de .env vers YAML\n\n"
            f"*Auto-linked by session system v2.0*"
        )
        sync.post_collateral_created(
            "Migrer la config cache de .env vers YAML",
            "chore", issue_number=ct1_num
        )
    time.sleep(1)

    # Step 3: Implementation
    print_step("2F", "Step 3 — Implementation (⏳→✅)")
    cid3 = sync.start_step(
        "Implémenter les providers Redis et Memcached",
        "Code des adapters + factory + intégration"
    )
    time.sleep(1)
    sync.complete_step(
        cid3, "Implémenter les providers Redis et Memcached",
        "3 providers implémentés:\n"
        "- `RedisCacheProvider`: 280 lignes, connection pooling\n"
        "- `MemcachedCacheProvider`: 195 lignes, consistent hashing\n"
        "- `InMemoryCacheProvider`: 85 lignes, LRU eviction\n"
        "- Factory: auto-detection depuis config"
    )
    time.sleep(1)

    # Step 4: Testing
    print_step("2G", "Step 4 — Testing (⏳→✅)")
    cid4 = sync.start_step(
        "Tests de performance et intégration",
        "Benchmarks comparatifs Redis vs Memcached + tests unitaires"
    )
    time.sleep(1)

    # Collateral 2: discovered during testing
    print_step("2H", "Collateral task 2 — connection leak fix")
    ct2_result = gh.issue_create(
        repo=REPO,
        title="[collateral] Fix connection leak dans MemcachedProvider",
        body=(
            f"**Parent session issue:** #{issue_num}\n"
            f"**Collateral task ID:** `ct-002`\n"
            f"**Type:** `fix`\n\n"
            "Découvert pendant les tests de charge: le MemcachedProvider "
            "ne ferme pas les connexions sur timeout, causant un leak "
            "après ~500 requêtes.\n\n"
            f"*Auto-generated collateral task — {_now()}*"
        ),
        labels=["task", "collateral", "test-v2"],
    )
    ct2_num = ct2_result.get("number", 0)
    if ct2_num:
        gh.issue_comment_post(
            REPO, issue_num,
            f"**Collateral task created:** #{ct2_num}\n"
            f"> Fix connection leak dans MemcachedProvider\n\n"
            f"*Auto-linked by session system v2.0*"
        )
        sync.post_collateral_created(
            "Fix connection leak dans MemcachedProvider",
            "fix", issue_number=ct2_num
        )
    time.sleep(1)

    # Complete testing step
    sync.complete_step(
        cid4, "Tests de performance et intégration",
        "Tests complétés:\n"
        "- 42 tests unitaires: ✅ all passing\n"
        "- Benchmark Redis: 12,500 ops/sec\n"
        "- Benchmark Memcached: 15,200 ops/sec\n"
        f"- Connection leak fix: #{ct2_num}"
    )
    time.sleep(1)

    # Knowledge grid
    print_step("2I", "Publishing knowledge validation grid")
    grid = (
        "| # | Question | Résultat |\n"
        "|---|----------|----------|\n"
        "| 1 | Démarrage session | ✅ Vrai |\n"
        "| 2 | Méthodologie | ✅ Vrai |\n"
        "| 3 | Architecture auditée | ✅ Vrai |\n"
        "| 4 | Design validé | ✅ Vrai |\n"
        "| 5 | Tests passants | ✅ Vrai |\n"
        "| 6 | Documentation | ⏳ En cours |\n"
        "| 7 | Grille publiée | ✅ Vrai |\n"
    )
    sync.post_knowledge_grid(grid, usid)
    time.sleep(1)

    # Integrity check
    print_step("2J", "Running integrity check")
    report = sync.integrity_check(
        todos_completed=[
            "Analyser l'architecture du cache actuel",
            "Concevoir le pattern Strategy pour le cache",
            "Implémenter les providers Redis et Memcached",
            "Tests de performance et intégration",
        ],
        todos_pending=["Documentation API"]
    )
    print(f"  Integrity: {report['report_line']}")
    time.sleep(1)

    # Summary
    print_step("2K", "Posting session summary")
    sync.post_summary(
        "### Résumé de session interactive\n"
        "- **Demande:** Refactoring module de cache distribué\n"
        "- **Type:** Enhancement (session interactive)\n"
        "- **Étapes complétées:** 4/5\n"
        "  1. ✅ Analyse architecture\n"
        "  2. ✅ Design Strategy pattern\n"
        "  3. ✅ Implémentation 3 providers\n"
        "  4. ✅ Tests performance\n"
        "  5. ⏳ Documentation API (en cours)\n"
        f"- **Tâches collatérales:** #{ct1_num} (config), #{ct2_num} (leak fix)\n"
        f"- **user_session_id:** `{usid}`\n"
        "- **Temps actif:** ~45 min\n"
    )
    time.sleep(1)

    # Close with report
    print_step("2L", "Closing session issue with full report")
    deliveries = [
        (f"Issue #{issue_num}", "✅ complétée"),
        (f"Collateral #{ct1_num}", "✅ config migration"),
        (f"Collateral #{ct2_num}", "✅ connection leak fix"),
    ]
    sync.close_with_report(deliveries)

    # Close collaterals
    if ct1_num:
        gh.issue_close(REPO, ct1_num)
    if ct2_num:
        gh.issue_close(REPO, ct2_num)

    print(f"\n  ✅ Test 2 COMPLETE — Issue #{issue_num} closed")
    return {
        "issue_number": issue_num,
        "collateral_issues": [ct1_num, ct2_num],
        "user_session_id": usid,
        "type": "interactive",
    }


def inject_test_sessions(results):
    """Inject test session entries into sessions.json."""
    root = _find_project_root()
    output = os.path.join(root, "docs", "data", "sessions.json")

    existing = {"meta": {}, "sessions": [], "issue_labels": {}}
    if os.path.exists(output):
        with open(output, "r", encoding="utf-8") as f:
            existing = json.load(f)

    now = _now()

    for r in results:
        if not r:
            continue

        is_interactive = r["type"] == "interactive"
        inum = r["issue_number"]
        usid = r["user_session_id"]

        session = {
            "id": f"issue-{inum}",
            "user_session_id": usid,
            "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "title": (
                "Refactoring du module de cache distribué"
                if is_interactive else
                "Validation email au formulaire d'inscription"
            ),
            "branch": f"claude/test-v2-{inum}",
            "type": "🔄 Enhancement" if is_interactive else "🔧 Fix",
            "request_type": "enhancement" if is_interactive else "fix",
            "engineering_stage": "testing" if is_interactive else "validation",
            "summary": (
                "Refactoring complet: Strategy pattern, 3 providers, "
                "benchmarks, 2 collateral tasks auto-générées."
                if is_interactive else
                "Validation email avec regex + DNS check. "
                "1 collateral task auto-générée (edge case regex)."
            ),
            "prs": [],
            "issues": [inum] + (
                r.get("collateral_issues", [])
                if is_interactive else
                ([r["collateral_issue"]] if r.get("collateral_issue") else [])
            ),
            "lessons": (
                [
                    "Strategy pattern permet d'ajouter des providers sans modifier le code existant",
                    "Toujours tester avec charge pour détecter les connection leaks",
                ]
                if is_interactive else
                ["Tester les edge cases d'email dès le début ('+', dots, unicode)"]
            ),
            "comments": [],
            "collateral_tasks": (
                [
                    {"id": "ct-001", "title": "Migrer config cache .env → YAML",
                     "type": "chore", "status": "completed",
                     "issue_number": r["collateral_issues"][0],
                     "created_at": now, "pr_numbers": []},
                    {"id": "ct-002", "title": "Fix connection leak MemcachedProvider",
                     "type": "fix", "status": "completed",
                     "issue_number": r["collateral_issues"][1],
                     "created_at": now, "pr_numbers": []},
                ]
                if is_interactive else
                [
                    {"id": "ct-001", "title": "Fix regex edge case emails avec '+'",
                     "type": "fix", "status": "completed",
                     "issue_number": r.get("collateral_issue"),
                     "created_at": now, "pr_numbers": []},
                ]
            ),
            "pr_count": 0,
            "has_notes": True,
            "has_issue": True,
            "sync_score": 1.0,
            "source_file": f"test-v2-{inum}",
            "issue_number": inum,
            "issue_created_at": now,
            "first_activity_time": now,
            "last_activity_time": now,
            "first_pr_time": None,
            "last_pr_time": None,
            "active_minutes": 45 if is_interactive else 25,
            "calendar_minutes": 50 if is_interactive else 30,
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
            "related_issues": [],
        }

        # Add related issues for collaterals
        if is_interactive:
            for ci in r.get("collateral_issues", []):
                if ci:
                    session["related_issues"].append({
                        "number": ci,
                        "title": "Collateral task",
                        "state": "closed",
                        "labels": ["task", "collateral"],
                    })
        elif r.get("collateral_issue"):
            session["related_issues"].append({
                "number": r["collateral_issue"],
                "title": "Fix regex edge case",
                "state": "closed",
                "labels": ["task", "collateral"],
            })

        # Insert at top
        existing["sessions"].insert(0, session)

    # Update meta
    existing["meta"]["generated_at"] = now
    existing["meta"]["total_sessions"] = len(existing["sessions"])

    with open(output, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

    print(f"\n  Sessions injected into {output}")
    print(f"  Total sessions: {len(existing['sessions'])}")


def main():
    print("\n" + "═" * 60)
    print("  v2.0 SESSION SYSTEM — LIVE INTEGRATION TEST")
    print("═" * 60)
    print(f"  Repo: {REPO}")
    print(f"  Time: {_now()}")
    print("═" * 60)

    # Verify GitHub access
    gh = GitHubHelper()
    auth = gh.auth_status()
    if not auth.get("authenticated"):
        print("ERROR: GitHub authentication failed")
        sys.exit(1)
    print(f"  GitHub: authenticated ✅")

    results = []

    # Test 1: Single request
    print("\n\n" + "━" * 60)
    print("  TEST 1: SINGLE USER REQUEST")
    print("━" * 60)
    r1 = run_test_single_request(gh)
    results.append(r1)

    time.sleep(2)

    # Test 2: Interactive request
    print("\n\n" + "━" * 60)
    print("  TEST 2: INTERACTIVE USER REQUEST")
    print("━" * 60)
    r2 = run_test_interactive_request(gh)
    results.append(r2)

    # Inject into sessions.json
    print("\n\n" + "━" * 60)
    print("  INJECTING TEST SESSIONS INTO VIEWER DATA")
    print("━" * 60)
    inject_test_sessions(results)

    # Final report
    print("\n\n" + "═" * 60)
    print("  LIVE TEST COMPLETE — RESULTS")
    print("═" * 60)
    for r in results:
        if not r:
            continue
        print(f"\n  {r['type'].upper()} REQUEST:")
        print(f"    Session issue: #{r['issue_number']}")
        print(f"    user_session_id: {r['user_session_id']}")
        if r["type"] == "interactive":
            print(f"    Collateral issues: {r['collateral_issues']}")
        else:
            print(f"    Collateral issue: #{r.get('collateral_issue', 'none')}")
        print(f"    GitHub URL: https://github.com/{REPO}/issues/{r['issue_number']}")
    print("\n  Check the Session Viewer to see these sessions rendered!")
    print("═" * 60)


if __name__ == "__main__":
    main()
