---
name: github
description: "MANDATORY before ANY GitHubHelper usage. Constructor: GitHubHelper() NO ARGS. Repo goes on methods, not constructor. Pitfall #23."
user_invocable: true
---

# /github — GitHubHelper Convention (MANDATORY)

## THE RULE — Read This First, Every Time

```python
from scripts.gh_helper import GitHubHelper

# ✅ CORRECT — always, no exceptions:
gh = GitHubHelper()

# ❌ FATAL — causes 401 Bad Credentials:
# gh = GitHubHelper('packetqc/knowledge')   ← repo passed as token!
# gh = GitHubHelper(repo)                   ← same mistake
# gh = GitHubHelper(token='packetqc/...')   ← still wrong
```

**Why**: `__init__(self, token=None)` — first arg is `token`. Passing `'packetqc/knowledge'` authenticates with that string as bearer token → 401. The constructor reads `GH_TOKEN` from env automatically. Never pass anything to it.

**Repo goes on EVERY method call, not the constructor:**

```python
gh = GitHubHelper()  # ← empty parens, always

# Issue ops — repo is first positional arg
gh.issue_create('owner/repo', 'Title', body='...', labels=['SESSION'])
gh.issue_comment_post('owner/repo', issue_num, 'body')
gh.issue_comment_edit('owner/repo', comment_id, 'body')
gh.issue_comments_list('owner/repo', issue_num)
gh.issue_labels_add('owner/repo', issue_num, ['LABEL'])
gh.issue_label_remove('owner/repo', issue_num, 'LABEL')
gh.issue_close('owner/repo', issue_num)

# PR ops — repo is first positional arg
gh.pr_create('owner/repo', head_branch, base_branch, 'Title', body='')
gh.pr_merge('owner/repo', pr_number)
gh.pr_create_and_merge('owner/repo', head_branch, base_branch, 'Title', body='')
gh.pr_list('owner/repo')
gh.pr_view('owner/repo', pr_number)

# Board ops — no repo (project-scoped)
gh.project_item_add(project_number, node_id)
gh.project_items_list(project_number)

# Auth check — no args
gh.auth_status()
```

## Token Setup

`GitHubHelper()` handles this automatically. Token resolution:
1. `GH_TOKEN` env var (primary)
2. `GITHUB_TOKEN` env var (fallback)

If no token found, guide user via `AskUserQuestion` (guidance only, NEVER accept token text — pitfall #8).

## Bash Usage

Each Bash call is a fresh shell. Always export token in same command:

```bash
export GH_TOKEN="$GH_TOKEN" && python3 -c "
from scripts.gh_helper import GitHubHelper
gh = GitHubHelper()
result = gh.pr_create_and_merge('owner/repo', 'branch', 'main', 'Title', body='Body')
print(result)
"
```

## Error Diagnosis

| Error | Cause | Fix |
|-------|-------|-----|
| **401 Bad credentials** | Repo string passed to constructor | Use `GitHubHelper()` with no args |
| **403 Forbidden** | Token lacks scope | Need `repo` + `project` scopes |
| **404 Not Found** | Bad repo name or number | Check `owner/repo` format |

## Comment Avatars

```markdown
## <img src="https://raw.githubusercontent.com/packetqc/knowledge/main/knowledge/data/references/Martin/vicky.png" width="20"> Martin — <desc>
> <quoted message>

## <img src="https://raw.githubusercontent.com/packetqc/knowledge/main/knowledge/data/references/Martin/vicky-sunglasses.png" width="20"> Claude — <desc>
<content>
```

## Real-Time Comment Protocol — Bidirectional Technique

### Principle

L'issue GitHub est le canal de persistance temps réel. Chaque échange significatif entre l'utilisateur et Claude DOIT être posté sur l'issue au moment où il se produit — pas en batch à la fin.

### Direction 1 — Utilisateur → Issue

Quand l'utilisateur écrit un message dans la session :

```
Utilisateur écrit → Claude reçoit → Claude poste 🧑 sur l'issue (verbatim) → Claude traite
```

```python
gh = GitHubHelper()
gh.issue_comment_post('owner/repo', issue_num,
    '## <img src="...vicky.png" width="20"> Martin — <desc>\n> <message verbatim>')
```

### Direction 2 — Claude → Issue AVANT affichage

Quand Claude prépare une réponse significative, l'ordre est **post first, display second** :

```
Claude prépare réponse → Claude poste 🤖 sur l'issue → Claude affiche à l'écran
```

```python
gh = GitHubHelper()
gh.issue_comment_post('owner/repo', issue_num,
    '## <img src="...vicky-sunglasses.png" width="20"> Claude — <desc>\n### Section\n<contenu>')
# PUIS afficher la réponse à l'utilisateur
```

**Pourquoi cet ordre** : Si compaction ou crash survient entre la préparation et le post, le commentaire est perdu à jamais. En postant d'abord, le contenu est persisté sur GitHub indépendamment de l'état local.

### Fallback — GitHub non disponible

Si l'API GitHub échoue (réseau, token, rate limit) :

1. **Ne pas bloquer** — la session continue normalement
2. **Persister localement** — écrire le commentaire en attente dans le cache runtime ou un fichier local
3. **Rattraper au prochain appel réussi** — poster les commentaires en attente quand GitHub redevient disponible

### Quand poster

| Échange | Direction | Obligatoire |
|---------|-----------|-------------|
| Demande originale utilisateur | 🧑 → issue | Oui — verbatim, gelé |
| Instructions / ajouts utilisateur | 🧑 → issue | Oui |
| Analyse / plan Claude | 🤖 → issue → écran | Oui |
| Étape todo démarrée | 🤖 ⏳ → issue | Oui |
| Étape todo complétée | 🤖 ✅ → issue | Oui |
| Décisions significatives | 🤖 → issue → écran | Oui |
| Raw tool output (git diff, grep) | — | Non — poster l'analyse, pas le dump |

---

## Subtree Sync — Push Module Changes to Home Repos

When working in a multi-module host project (K_DOCS), each K_* module has its own GitHub repo. The local proxy only authorizes the host repo, so subtree pushes must use token-authenticated URLs directly.

### Setup remote (once per module per session)

```bash
export GH_TOKEN="$GH_TOKEN" && git remote add k_tools "https://x-access-token:${GH_TOKEN}@github.com/packetqc/K_TOOLS.git"
```

### Subtree push (sync local changes to module repo)

```bash
git subtree push --prefix=Knowledge/K_TOOLS k_tools main
```

### Force push (when host is source of truth and remote diverged)

```bash
export GH_TOKEN="$GH_TOKEN" && git push k_tools $(git subtree split --prefix=Knowledge/K_TOOLS):main --force
```

### Check if module repo exists (via GitHubHelper)

```python
import urllib.request, json, sys
sys.path.insert(0, 'Knowledge/legacy/knowledge/engine/scripts')
from gh_helper import GitHubHelper
gh = GitHubHelper()
req = urllib.request.Request('https://api.github.com/repos/packetqc/K_TOOLS')
req.add_header('Authorization', f'Bearer {gh.token}')
req.add_header('Accept', 'application/vnd.github+json')
resp = urllib.request.urlopen(req)
print(json.loads(resp.read())['full_name'])
```

### Key insight

The local proxy (`127.0.0.1:*`) only authorizes the host repo. For module repos, bypass the proxy by using `https://x-access-token:${GH_TOKEN}@github.com/owner/repo.git` as the remote URL. This uses the same GH_TOKEN that GitHubHelper reads from env.

### Module registry

Check `Knowledge/modules.json` for all modules and their upstream repos. After sync, ensure `"imported": true` and `"upstream": "packetqc/K_<NAME>"` are set.

---

## Self-Check

Before writing ANY code with `GitHubHelper`:
1. Constructor has **zero arguments**: `GitHubHelper()`
2. Repo is the **first arg on the method**: `gh.method('owner/repo', ...)`
3. Token comes from **environment**, not from code

If you catch yourself writing `GitHubHelper(anything)` — STOP. That's pitfall #23.
