#!/usr/bin/env python3
"""Knowledge imbriqué avec architecture Skills.

Chaque composant du knowledge est un Skill enregistré dans un registre.
Les skills peuvent s'appeler entre eux par nom via le registre.
Charge la configuration depuis methodology/methodology-knowledge.md.
"""
import subprocess
import sys
import os
import json
import glob
from datetime import datetime

_script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _script_dir)
sys.path.insert(0, os.path.dirname(_script_dir))  # knowledge/engine/ for knowledge_config
from knowledge_config import charger_methodologie


# =============================================================================
# Registre de Skills
# =============================================================================

class SkillRegistry:
    """Registre central de tous les skills disponibles."""

    def __init__(self):
        self._skills = {}
        self._resultats = {}

    def enregistrer(self, nom, skill):
        """Enregistre un skill dans le registre."""
        self._skills[nom] = skill
        skill.registre = self

    def executer(self, nom, **kwargs):
        """Exécute un skill par son nom."""
        if nom not in self._skills:
            print(f"  Skill '{nom}' non trouvé.")
            return None
        return self._skills[nom].executer(**kwargs)

    def lister(self):
        """Liste tous les skills enregistrés."""
        return list(self._skills.keys())

    def stocker_resultat(self, knowledge, question, reponse):
        """Stocke un résultat."""
        if knowledge not in self._resultats:
            self._resultats[knowledge] = {}
        self._resultats[knowledge][question] = reponse

    def get_resultats(self):
        """Retourne tous les résultats."""
        return self._resultats


# =============================================================================
# Classe de base Skill
# =============================================================================

class Skill:
    """Classe de base pour tous les skills."""

    def __init__(self, nom, description=""):
        self.nom = nom
        self.description = description
        self.registre = None

    def executer(self, **kwargs):
        raise NotImplementedError


# =============================================================================
# Skill : Lire un choix
# =============================================================================

class LireChoixSkill(Skill):
    def executer(self, prompt="Votre choix : ", max_choix=2):
        while True:
            choix = input(prompt).strip()
            if choix.isdigit() and 1 <= int(choix) <= max_choix:
                return int(choix)
            print(f"Choix invalide. Veuillez entrer un nombre entre 1 et {max_choix}.")


# =============================================================================
# Skills : Actions (fonctions et programmes)
# =============================================================================

class FonctionSkill(Skill):
    """Skill qui exécute une fonction interne."""
    def executer(self, question="", message=""):
        if message:
            print(f"      {message}")
        else:
            print(f"      >>> Je suis la fonction {question}.")


class ProgrammeSkill(Skill):
    """Skill qui exécute un programme externe."""
    def executer(self, question="", message=""):
        script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "action_externe.py")
        subprocess.run([sys.executable, script, question])


# =============================================================================
# Skill : Sous-knowledge (Vrai / Faux / Passer)
# =============================================================================

class SousKnowledgeSkill(Skill):
    """Skill du sous-knowledge avec Vrai, Faux, Passer."""

    def __init__(self, nom, action_vrai_skill=None, message_vrai="", choix_labels=None):
        super().__init__(nom, f"Sous-knowledge pour {nom}")
        self.action_vrai_skill = action_vrai_skill
        self.message_vrai = message_vrai
        self.choix_labels = choix_labels or ["Vrai", "Faux", "Passer"]

    def executer(self, knowledge_parent="", **kwargs):
        print(f"\n      --- Sous-knowledge pour {self.nom} ---")
        for i, label in enumerate(self.choix_labels, start=1):
            print(f"      {i}. {label}")

        choix = self.registre.executer("lire_choix",
                                       prompt=f"      Votre réponse pour {self.nom} (1/2/3) : ",
                                       max_choix=len(self.choix_labels))
        reponse = self.choix_labels[choix - 1]
        print(f"      Vous avez choisi : {reponse}")

        if choix == 1 and self.action_vrai_skill:
            self.registre.executer(self.action_vrai_skill, question=self.nom,
                                   message=self.message_vrai)

        self.registre.stocker_resultat(knowledge_parent, self.nom, reponse)
        return reponse


# =============================================================================
# Skill : Knowledge Secondaire
# =============================================================================

class KnowledgeSecondaireSkill(Skill):
    """Skill du knowledge secondaire avec 3 sous-options + Passer."""

    def __init__(self, nom, lettre, sous_knowledge_skills):
        super().__init__(nom, f"Knowledge secondaire {nom}")
        self.lettre = lettre
        self.sous_knowledge_skills = sous_knowledge_skills

    def _ordonner_affichage(self):
        """Réordonne les questions pour l'affichage.

        Règle : les questions avec action 'tous' sont affichées en premier.
        Pour Approbation (E) : 'Approuver' (E4) en premier, 'Tous' (E3) en deuxième.
        Les IDs restent inchangés — seul l'ordre de présentation change.
        """
        tous = []
        approuver = []
        autres = []
        for sq in self.sous_knowledge_skills:
            skill = self.registre._skills.get(sq)
            if skill and hasattr(skill, 'action_vrai_skill') and skill.action_vrai_skill == 'tous':
                # Distinguer "Approuver" de "Tous" par le label
                if 'approuver' in sq.lower() or (hasattr(skill, 'nom') and 'E4' in skill.nom):
                    approuver.append(sq)
                else:
                    tous.append(sq)
            else:
                autres.append(sq)

        if self.lettre == 'E':
            # Approbation : Approuver d'abord, Tous ensuite, puis le reste
            return approuver + tous + autres
        else:
            # Autres sections : Tous d'abord, puis le reste
            return tous + autres

    def executer(self, **kwargs):
        while True:
            print(f"\n  == Knowledge Secondaire ({self.nom}) ==")
            affichage = self._ordonner_affichage()
            for i, sq in enumerate(affichage, start=1):
                print(f"  {i}. {sq}?")
            print(f"  {len(affichage) + 1}. Passer")

            choix = self.registre.executer("lire_choix",
                                           prompt=f"  Votre choix (1-{len(affichage) + 1}) : ",
                                           max_choix=len(affichage) + 1)

            if choix == len(affichage) + 1:
                print(f"  Vous passez le knowledge {self.nom}.")
                break

            skill_nom = affichage[choix - 1]
            self.registre.executer(skill_nom, knowledge_parent=self.nom)


# =============================================================================
# Skill : Knowledge Principal
# =============================================================================

class KnowledgePrincipalSkill(Skill):
    """Skill du knowledge principal."""

    def __init__(self, nom, knowledge_secondaires):
        super().__init__(nom, "Knowledge principal")
        self.knowledge_secondaires = knowledge_secondaires

    def executer(self, **kwargs):
        while True:
            print(f"\n=== Knowledge Principal ===")
            for i, (label, _) in enumerate(self.knowledge_secondaires, start=1):
                print(f"{i}. {label}")
            print(f"{len(self.knowledge_secondaires) + 1}. Terminer")

            choix = self.registre.executer("lire_choix",
                                           prompt=f"Votre choix (1-{len(self.knowledge_secondaires) + 1}) : ",
                                           max_choix=len(self.knowledge_secondaires) + 1)

            if choix == len(self.knowledge_secondaires) + 1:
                print("\nVous avez choisi de terminer.")
                break

            _, skill_nom = self.knowledge_secondaires[choix - 1]
            self.registre.executer(skill_nom)

        self.registre.executer("afficher_grille")


# =============================================================================
# Skill : Afficher la grille
# =============================================================================

class AfficherGrilleSkill(Skill):
    """Skill pour afficher la grille de résultats."""

    def __init__(self, nom, knowledge_config, message_fin_complet="", message_fin_incomplet=""):
        super().__init__(nom, "Affichage grille")
        self.knowledge_config = knowledge_config
        self.message_fin_complet = message_fin_complet
        self.message_fin_incomplet = message_fin_incomplet

    def executer(self, **kwargs):
        resultats = self.registre.get_resultats()
        idx = 7
        col = 10
        max_questions = max(len(qs) for _, _, qs in self.knowledge_config)
        sep = "+" + "-" * idx + ("+" + "-" * col) * max_questions + "+"
        sep_header = "+" + "=" * idx + ("+" + "=" * col) * max_questions + "+"

        print("\n        GRILLE DE RÉSULTATS")
        print(sep)
        header = f"|{'':^{idx}}"
        for n in range(1, max_questions + 1):
            header += f"|{n:^{col}}"
        header += "|"
        print(header)
        print(sep_header)

        complet = True
        for label, lettre, questions in self.knowledge_config:
            row = f"|{('Knw ' + lettre):^{idx}}"
            for n in range(1, max_questions + 1):
                sous_option = f"{lettre}{n}"
                if n <= len(questions) and label in resultats and sous_option in resultats[label]:
                    val = resultats[label][sous_option]
                elif n <= len(questions):
                    val = "--"
                    complet = False
                else:
                    val = ""
                row += f"|{val:^{col}}"
            row += "|"
            print(row)
            print(sep)

        message = self.message_fin_complet if complet else self.message_fin_incomplet
        print(f"\n{message}")


# =============================================================================
# État interne post-grille
# =============================================================================

# Flag interne : documentation requise suite à des changements détectés.
# - Remis à False quand l'exécution DÉMARRE (A3) — ardoise propre.
# - Mis à True par les compilations si elles détectent des changements.
# - Consulté par confirmation_documentation qui le compare avec le résultat
#   de l'étape Documentation (dernière rangée du quiz) pour décider si un
#   rappel est nécessaire.
_documentation_requise = False


def set_documentation_requise():
    """Met le flag à True. Appelée par les compilations quand elles
    détectent des changements qui nécessitent documentation."""
    global _documentation_requise
    _documentation_requise = True


def reset_documentation_requise():
    """Remet le flag à False. Appelée quand l'exécution de la demande
    DÉMARRE (A3) — on repart à zéro avant de savoir s'il y aura
    des changements."""
    global _documentation_requise
    _documentation_requise = False


# =============================================================================
# Fonctions post-grille
# =============================================================================

def _find_project_root():
    """Find project root by looking for CLAUDE.md."""
    d = os.path.dirname(os.path.abspath(__file__))
    while d != '/':
        if os.path.exists(os.path.join(d, 'CLAUDE.md')):
            return d
        d = os.path.dirname(d)
    return os.getcwd()


def _load_latest_cache():
    """Load the most recent session runtime cache."""
    root = _find_project_root()
    pattern = os.path.join(root, "notes", "session-runtime-*.json")
    files = sorted(glob.glob(pattern), key=os.path.getmtime, reverse=True)
    if not files:
        return None
    try:
        with open(files[0], 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def _parse_iso(ts):
    """Parse ISO timestamp string to datetime, returning None on failure."""
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts.replace('Z', '+00:00'))
    except (ValueError, AttributeError):
        return None


# Categories from methodology-compilation-metrics.md / methodology-compilation-times.md
CATEGORY_ICONS = {
    'diagnostic': '🔍',
    'conception': '💡',
    'documentation': '📝',
    'doc_management': '📋',
    'collateral': '⚙️',
}


def _load_previous_compilation(compilation_type):
    """Load previous compilation results from knowledge_resultats.json.

    Returns the previous compilation dict for the given type ('metriques' or 'temps'),
    or None if no previous compilation exists.
    """
    root = _find_project_root()
    resultats_path = os.path.join(root, ".claude", "knowledge_resultats.json")
    try:
        with open(resultats_path, 'r') as f:
            data = json.load(f)
        compilations = data.get("compilations_post_execution") or {}
        return compilations.get(compilation_type)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return None


def compilation_metriques(resultats, incremental=False):
    """Compile les métriques du knowledge.

    Called in two contexts:
    1. Post-execution (incremental=True): first pass after demand execution,
       before returning to quiz. Compiles metrics of the work just executed.
    2. Post-quiz (incremental=True): second pass after quiz completion.
       Only compiles the delta since the post-execution compilation.

    When incremental=True and a previous compilation exists, the git diff
    range starts from the last compiled commit instead of HEAD~5.

    Collects PR stats, file counts, line changes from the session cache.
    Detects if metrics changed; if so, sets _documentation_requise flag.
    Returns compiled metrics dict.
    """
    global _documentation_requise
    cache = _load_latest_cache()
    if not cache:
        return {}

    sd = cache.get("session_data", {})
    workflow = sd.get("task_workflow", {})

    # Collect PR data from cache exchanges
    exchanges = sd.get("exchanges", [])
    pr_numbers = set()
    for ex in exchanges:
        pr = ex.get("pr_number")
        if pr:
            pr_numbers.add(pr)

    # Collect from work summary if available
    work_summary = sd.get("work_summary", {})
    if isinstance(work_summary, str):
        work_summary = {}
    prs_merged = work_summary.get("prs_merged", [])
    for pr_info in prs_merged:
        if isinstance(pr_info, dict):
            pr_numbers.add(pr_info.get("number", 0))
        elif isinstance(pr_info, int):
            pr_numbers.add(pr_info)

    # Determine git diff range based on incremental mode
    root = _find_project_root()
    previous = _load_previous_compilation('metriques') if incremental else None
    if previous and previous.get("last_commit_sha"):
        diff_range = f"{previous['last_commit_sha']}..HEAD"
    else:
        diff_range = "HEAD~5..HEAD"

    # Get current HEAD SHA for tracking
    current_sha = None
    try:
        result = subprocess.run(
            ['git', 'rev-parse', 'HEAD'],
            capture_output=True, text=True, cwd=root, timeout=5
        )
        current_sha = result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # Collect file/line stats from git
    total_files = 0
    total_additions = 0
    total_deletions = 0
    try:
        result = subprocess.run(
            ['git', 'diff', '--numstat', diff_range],
            capture_output=True, text=True, cwd=root, timeout=10
        )
        for line in result.stdout.strip().split('\n'):
            parts = line.split('\t')
            if len(parts) >= 3:
                try:
                    additions = int(parts[0]) if parts[0] != '-' else 0
                    deletions = int(parts[1]) if parts[1] != '-' else 0
                    total_additions += additions
                    total_deletions += deletions
                    total_files += 1
                except ValueError:
                    pass
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # Collect deliverables from cache
    deliverables = work_summary.get("deliverables", [])

    # Accumulate with previous compilation if incremental
    if previous:
        total_additions += previous.get("additions", 0)
        total_deletions += previous.get("deletions", 0)
        total_files += previous.get("files_changed", 0)
        # Merge PR numbers
        for pr in previous.get("pr_numbers", []):
            pr_numbers.add(pr)

    metrics = {
        "prs": len(pr_numbers),
        "pr_numbers": sorted(pr_numbers),
        "files_changed": total_files,
        "additions": total_additions,
        "deletions": total_deletions,
        "deliverables": deliverables,
        "todos_count": len(sd.get("todos_snapshot", [])),
        "compiled_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "last_commit_sha": current_sha,
        "incremental": incremental,
    }

    # Detect changes — if any non-zero metric, documentation may be needed
    if total_files > 0 or len(pr_numbers) > 0:
        set_documentation_requise()

    return metrics


def compilation_temps(resultats, incremental=False):
    """Compile les données de temps du knowledge.

    Called in two contexts:
    1. Post-execution (incremental=True): first pass after demand execution,
       before returning to quiz. Compiles time data of the work just executed.
    2. Post-quiz (incremental=True): second pass after quiz completion.
       Only compiles the delta since the post-execution compilation.

    When incremental=True and a previous compilation exists, only stage_history
    entries after the last compiled timestamp are included in the delta.

    Calculates durations from time_markers and stage_history.
    Detects if time was accumulated; if so, sets _documentation_requise flag.
    Returns compiled time dict.
    """
    global _documentation_requise
    cache = _load_latest_cache()
    if not cache:
        return {}

    sd = cache.get("session_data", {})
    workflow = sd.get("task_workflow", {})
    time_markers = sd.get("time_markers", [])
    stage_history = workflow.get("stage_history", [])

    # Filter stage_history for incremental mode
    previous_temps = _load_previous_compilation('temps') if incremental else None
    if previous_temps and previous_temps.get("compiled_at"):
        last_compiled = _parse_iso(previous_temps["compiled_at"])
        if last_compiled:
            # Only include entries entered after the last compilation
            stage_history = [
                e for e in stage_history
                if not _parse_iso(e.get("entered_at")) or
                _parse_iso(e.get("entered_at")) > last_compiled
            ]

    # Calculate stage durations
    stage_durations = []
    for entry in stage_history:
        entered = _parse_iso(entry.get("entered_at"))
        exited = _parse_iso(entry.get("exited_at"))
        duration_sec = 0
        if entered and exited:
            duration_sec = (exited - entered).total_seconds()
        stage_durations.append({
            "stage": entry.get("stage", "unknown"),
            "entered_at": entry.get("entered_at"),
            "exited_at": entry.get("exited_at"),
            "duration_seconds": duration_sec,
            "direction": entry.get("direction", ""),
            "reason": entry.get("reason", ""),
        })

    # Calculate total session time
    started_at = _parse_iso(workflow.get("started_at"))
    updated_at = _parse_iso(workflow.get("updated_at"))
    calendar_seconds = 0
    if started_at and updated_at:
        calendar_seconds = (updated_at - started_at).total_seconds()

    # Calculate active time (sum of stage durations)
    active_seconds = sum(d["duration_seconds"] for d in stage_durations)

    # Accumulate with previous compilation if incremental
    if previous_temps:
        active_seconds += previous_temps.get("active_seconds", 0)

    # Calculate inactive time
    inactive_seconds = max(0, calendar_seconds - active_seconds)

    # Time blocks (morning/afternoon/evening)
    blocks = set()
    for entry in stage_history:
        entered = _parse_iso(entry.get("entered_at"))
        if entered:
            hour = entered.hour
            if 5 <= hour < 12:
                blocks.add("morning")
            elif 12 <= hour < 18:
                blocks.add("afternoon")
            elif 18 <= hour < 23:
                blocks.add("evening")

    # Format durations
    def fmt_duration(secs):
        if secs < 60:
            return f"~{int(secs)}s"
        hours = int(secs // 3600)
        mins = int((secs % 3600) // 60)
        if hours > 0:
            return f"{hours}h{mins:02d}"
        return f"~{mins}min"

    time_data = {
        "calendar_seconds": calendar_seconds,
        "active_seconds": active_seconds,
        "inactive_seconds": inactive_seconds,
        "calendar_formatted": fmt_duration(calendar_seconds),
        "active_formatted": fmt_duration(active_seconds),
        "inactive_formatted": fmt_duration(inactive_seconds),
        "stage_durations": stage_durations,
        "blocks": sorted(blocks),
        "block_count": len(blocks),
        "time_markers_count": len(time_markers),
        "started_at": workflow.get("started_at"),
        "updated_at": workflow.get("updated_at"),
        "compiled_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "incremental": incremental,
    }

    # Detect changes — if any time accumulated
    if active_seconds > 0:
        set_documentation_requise()

    return time_data


# =============================================================================
# Pré-sauvegarde (étape 9)
# =============================================================================
# L'étape pré-sauvegarde regroupe les sous-fonctions de conformité
# exécutées avant la sauvegarde. confirmation_documentation est la
# première règle. D'autres suivront.

def confirmation_documentation(resultats):
    """Sous-fonction pré-sauvegarde #1 : rappel de documentation.

    Compare deux valeurs :
    1. Le flag interne _documentation_requise (mis à True par les compilations
       si des changements ont été détectés)
    2. Le résultat de l'étape Documentation dans le quiz (dernière rangée
       du tableau des résultats — le dernier knowledge au niveau principal)

    Logique de comparaison :
    - Flag False → passe (rien à documenter, pas de changements)
    - Flag True + résultat doc "Vrai" → passe (l'utilisateur a documenté)
    - Flag True + résultat doc "--"/"Faux"/"Passer" → suggérer via
      AskUserQuestion (rappel de discipline, pas un bloqueur)

    Retourne True si pas de rappel nécessaire ou si l'utilisateur a documenté,
    False si l'utilisateur n'a pas documenté et passe le rappel.
    """
    if not _documentation_requise:
        return True

    # Chercher le dernier knowledge (étape Documentation) dans les résultats
    knowledge_names = list(resultats.keys()) if resultats else []
    if not knowledge_names:
        return True

    dernier_knowledge = knowledge_names[-1]
    resultats_doc = resultats.get(dernier_knowledge, {})

    # Vérifier si au moins une question du dernier knowledge a "Vrai"
    # (l'utilisateur a complété l'étape de documentation)
    documentation_faite = any(v == "Vrai" for v in resultats_doc.values())

    if documentation_faite:
        return True

    # Flag True + documentation non faite → rappel nécessaire
    # TODO: AskUserQuestion pour suggérer la documentation
    # L'utilisateur peut Skip — c'est un rappel, pas un bloqueur
    return False


def pre_sauvegarde(resultats):
    """Étape 9 : exécute toutes les règles de conformité pré-sauvegarde.

    Regroupe les sous-fonctions de conformité qui doivent s'exécuter
    avant la sauvegarde. Actuellement :
    1. confirmation_documentation — rappel si documentation manquante

    D'autres règles de conformité seront ajoutées ici.
    """
    confirmation_documentation(resultats)


# =============================================================================
# Sauvegarde (étape 10)
# =============================================================================

def _find_current_cache(root):
    """Find the current session's runtime cache file.

    Looks for the cache matching the current git branch, or falls back
    to the most recently modified cache.
    """
    notes_dir = os.path.join(root, "notes")
    try:
        branch_result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True, timeout=5, cwd=root,
        )
        branch = branch_result.stdout.strip()
    except (subprocess.TimeoutExpired, OSError):
        branch = ""

    # Try branch-specific cache (same suffix logic as session_agent)
    if branch:
        suffix = _branch_to_suffix(branch)
        candidate = os.path.join(notes_dir, f"session-runtime-{suffix}.json")
        if os.path.exists(candidate):
            return candidate

    # Fallback: most recent cache by mtime (exclude demo files)
    pattern = os.path.join(notes_dir, "session-runtime-*.json")
    caches = sorted(glob.glob(pattern), key=os.path.getmtime, reverse=True)
    # Prefer non-demo caches
    non_demo = [c for c in caches if "demo" not in os.path.basename(c)]
    return (non_demo[0] if non_demo else caches[0]) if caches else None


def _branch_to_suffix(branch):
    """Extract the short unique suffix from a branch name.

    Mirrors session_agent.cache._session_id_to_suffix() logic:
    claude/create-project-test-G93uA → G93uA
    """
    if not branch:
        return ""
    parts = branch.rstrip('/').split('-')
    if len(parts) > 1:
        suffix = parts[-1]
        suffix = ''.join(c for c in suffix if c.isalnum())
        if suffix:
            return suffix
    # Fallback: sanitize full branch
    return ''.join(c for c in branch if c.isalnum())[:20]


def _ensure_runtime_cache(root):
    """Create a minimal runtime cache from knowledge_resultats.json if none exists.

    The knowledge-validation flow does not go through session_agent, so no
    runtime cache is created automatically. Without a cache, sauvegarde()
    cannot feed incremental_update() for sessions.json/tasks.json.

    This bridge reads knowledge_resultats.json and creates a cache file
    that the compilation pipeline can consume. Uses the same suffix logic
    as session_agent.cache._session_id_to_suffix() so that both
    _find_current_cache() and session_agent.read_runtime_cache() find it.

    Returns the path to the cache file (existing or newly created), or None.
    """
    notes_dir = os.path.join(root, "notes")
    try:
        branch_result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True, timeout=5, cwd=root,
        )
        branch = branch_result.stdout.strip()
    except (subprocess.TimeoutExpired, OSError):
        return None

    if not branch:
        return None

    # Use the same suffix logic as session_agent
    suffix = _branch_to_suffix(branch)
    cache_path = os.path.join(notes_dir, f"session-runtime-{suffix}.json")
    if os.path.exists(cache_path):
        # Check if existing cache matches current session — if not, update it
        try:
            with open(cache_path, "r") as ef:
                existing = json.load(ef)
            kr_path = os.path.join(root, ".claude", "knowledge_resultats.json")
            if os.path.exists(kr_path):
                with open(kr_path, "r") as kf:
                    kr_current = json.load(kf)
                current_sid = kr_current.get("user_session_id", "")
                cached_sid = existing.get("session_id", "")
                if current_sid and cached_sid == current_sid:
                    return cache_path  # Same session, cache is valid
                # Different session on same branch — fall through to rebuild
            else:
                return cache_path
        except (json.JSONDecodeError, OSError):
            pass  # Fall through to rebuild

    # Read knowledge_resultats.json
    kr_path = os.path.join(root, ".claude", "knowledge_resultats.json")
    if not os.path.exists(kr_path):
        return None

    try:
        with open(kr_path, "r") as f:
            kr = json.load(f)
    except (json.JSONDecodeError, OSError):
        return None

    issue_github = kr.get("issue_github") or {}
    issue_number = issue_github.get("numero")
    issue_repo = issue_github.get("repo", "")
    valeurs = kr.get("valeurs_detectees", {})
    a1 = valeurs.get("A1", {})
    a2 = valeurs.get("A2", {})
    user_session_id = kr.get("user_session_id", "")
    started_at = kr.get("started_at", "")
    resultats = kr.get("resultats", {})
    compilations = kr.get("compilations_post_execution") or {}

    # Build title from issue or A1
    title = a1.get("valeur", "")
    description = a2.get("original") or a2.get("valeur", "")
    a3 = valeurs.get("A3", {})
    project_name = a3.get("valeur", "")
    now_iso = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Determine execution result from A4
    a4_result = resultats.get("Validation de la demande", {}).get("A4", "--")
    demande_executee = kr.get("demande_executee", False)

    # PR numbers from compilations
    pr_numbers = compilations.get("metriques", {}).get("pr_numbers", [])

    # Build task_workflow so compile_tasks.py can extract a task entry.
    # This mirrors session_agent's task_workflow structure with the fields
    # that extract_task_from_cache() actually reads.
    #
    # Map knowledge grid completion to task workflow stage:
    #   A (Validation) done  → implement (3)
    #   B (Qualité) done     → validation (4)
    #   C (Intégrité) done   → documentation (5)  (skip to next)
    #   D (Documentation) done → approval (6)
    #   E (Approbation) done → completion (7)
    # "done" = all questions answered (no "--" left)
    def _knowledge_done(name):
        vals = resultats.get(name, {})
        return vals and all(v != "--" for v in vals.values())

    if _knowledge_done("Approbation"):
        _stage, _idx = "completion", 7
    elif _knowledge_done("Documentation"):
        _stage, _idx = "approval", 6
    elif _knowledge_done("Intégrité de session"):
        _stage, _idx = "documentation", 5
    elif _knowledge_done("Qualité du travail"):
        _stage, _idx = "validation", 4
    elif demande_executee:
        _stage, _idx = "implement", 3
    else:
        _stage, _idx = "initial", 0

    task_workflow = {
        "issue_number": issue_number,
        "title": title,
        "description": description,
        "current_stage": _stage,
        "current_stage_index": _idx,
        "current_step": "close_issue" if demande_executee else "classify_request",
        "project": project_name or None,
        "started_at": started_at,
        "updated_at": now_iso,
        "modifications_occurred": demande_executee,
        "validation_skipped_entirely": False,
        "validation_results": {},
        "unit_tests": [],
        "stage_history": [],
        "step_history": [],
    }

    # Build knowledge_grid for the task
    knowledge_grid = {
        "resultats": resultats,
        "en_cours": kr.get("en_cours", False),
        "valeurs_detectees": valeurs,
    }

    # Extract metrics from compilations for work_summary enrichment
    metriques = compilations.get("metriques", {})
    temps = compilations.get("temps", {})

    # Build minimal runtime cache compatible with compile pipeline
    cache_data = {
        "session_id": user_session_id,
        "issue_number": issue_number,
        "issue_title": title,
        "branch": branch,
        "repo": issue_repo,
        "created": started_at,
        "updated": now_iso,
        "session_data": {
            "user_session_id": user_session_id,
            "session_phase": "completed" if demande_executee else "active",
            "request_description": description,
            "todo_snapshot": [],
            "files_modified": [],
            "work_summary": {
                "title": title,
                "prs_merged": [p for p in pr_numbers],
                "files_changed": metriques.get("files_changed", 0),
                "additions": metriques.get("additions", 0),
                "deletions": metriques.get("deletions", 0),
                "deliverables": metriques.get("deliverables", []),
            },
            "pr_numbers": [p for p in pr_numbers],
            "knowledge_grid": knowledge_grid,
            "task_workflow": task_workflow,
            "compilations_post_execution": compilations if compilations else None,
        },
    }

    # Write the cache
    os.makedirs(notes_dir, exist_ok=True)
    with open(cache_path, "w") as f:
        json.dump(cache_data, f, indent=2, ensure_ascii=False)

    return cache_path


def _find_current_notes(root):
    """Find the current session's notes file (for compile_sessions --incremental)."""
    notes_dir = os.path.join(root, "notes")
    try:
        branch_result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True, timeout=5, cwd=root,
        )
        branch = branch_result.stdout.strip()
    except (subprocess.TimeoutExpired, OSError):
        branch = ""

    if branch:
        suffix = branch.replace("/", "-")
        candidate = os.path.join(notes_dir, f"session-{suffix}.md")
        if os.path.exists(candidate):
            return candidate

    # Fallback: most recent notes file by mtime
    pattern = os.path.join(notes_dir, "session-*.md")
    # Exclude runtime caches
    notes = [f for f in sorted(glob.glob(pattern), key=os.path.getmtime, reverse=True)
             if "runtime" not in os.path.basename(f)]
    return notes[0] if notes else None


def sauvegarde(resultats):
    """Sauvegarde les résultats du knowledge. Appelée après l'affichage de la grille.

    Uses INCREMENTAL compilation to preserve existing data (v2.0 baseline)
    and only add/update the current session's entry in:
      - docs/data/sessions.json  (via compile_sessions.py --incremental)
      - docs/data/tasks.json     (via compile_tasks.py --incremental)

    This is the bridge between knowledge-validation data production and
    web interface visibility.
    """
    root = _find_project_root()
    compiled = []
    errors = []

    # 0. Ensure a runtime cache exists for the current branch.
    #    knowledge-validation doesn't go through session_agent, so no cache
    #    is created automatically. Without it, incremental_update() skips.
    cache_created = _ensure_runtime_cache(root)
    if cache_created:
        # Check if it was newly created (not pre-existing)
        branch_cache = _find_current_cache(root)
        if branch_cache and branch_cache == cache_created:
            # Git-add so it persists across PR merges
            subprocess.run(
                ["git", "add", cache_created],
                capture_output=True, timeout=10, cwd=root,
            )

    # 1. Incremental sessions.json — try generate_sessions.py first, then compile_sessions.py
    gen_sessions = os.path.join(root, "scripts", "generate_sessions.py")
    compile_sessions = os.path.join(root, "scripts", "compile_sessions.py")
    notes_file = _find_current_notes(root)

    if os.path.exists(gen_sessions):
        # Preferred: generate_sessions.py incremental_update() — GitHub-aware
        try:
            result = subprocess.run(
                ["python3", "-c",
                 "import sys; sys.path.insert(0, 'scripts'); "
                 "from generate_sessions import incremental_update; "
                 "incremental_update()"],
                capture_output=True, text=True, timeout=120,
                cwd=root,
            )
            if result.returncode == 0:
                compiled.append("sessions.json")
            else:
                errors.append(f"incremental sessions: {result.stderr[:200]}")
        except (subprocess.TimeoutExpired, OSError) as e:
            errors.append(f"incremental sessions: {e}")
    elif notes_file and os.path.exists(compile_sessions):
        # Fallback: compile_sessions.py --incremental with current notes file
        try:
            result = subprocess.run(
                ["python3", compile_sessions, "--incremental", notes_file],
                capture_output=True, text=True, timeout=60,
                cwd=root,
            )
            if result.returncode == 0:
                compiled.append("sessions.json")
            else:
                errors.append(f"compile_sessions: {result.stderr[:200]}")
        except (subprocess.TimeoutExpired, OSError) as e:
            errors.append(f"compile_sessions: {e}")

    # 2. Incremental tasks.json — only merge the current session's cache
    compile_tasks = os.path.join(root, "scripts", "compile_tasks.py")
    cache_file = _find_current_cache(root)

    if cache_file and os.path.exists(compile_tasks):
        try:
            result = subprocess.run(
                ["python3", compile_tasks, "--incremental", cache_file],
                capture_output=True, text=True, timeout=60,
                cwd=root,
            )
            if result.returncode == 0:
                compiled.append("tasks.json")
            else:
                errors.append(f"compile_tasks: {result.stderr[:200]}")
        except (subprocess.TimeoutExpired, OSError) as e:
            errors.append(f"compile_tasks: {e}")
    elif not cache_file:
        errors.append("compile_tasks: no runtime cache found for current session")

    # 3. Commit + push compiled JSON if anything changed
    if compiled:
        files_to_add = []
        sessions_json = os.path.join(root, "docs", "data", "sessions.json")
        tasks_json = os.path.join(root, "docs", "data", "tasks.json")
        if os.path.exists(sessions_json):
            files_to_add.append(sessions_json)
        if os.path.exists(tasks_json):
            files_to_add.append(tasks_json)

        if files_to_add:
            try:
                subprocess.run(
                    ["git", "add"] + files_to_add,
                    capture_output=True, timeout=10, cwd=root,
                )
                msg = f"data: incremental compile {' + '.join(compiled)} for web interfaces"
                subprocess.run(
                    ["git", "commit", "-m", msg],
                    capture_output=True, timeout=10, cwd=root,
                )
            except (subprocess.TimeoutExpired, OSError):
                pass

    return {"compiled": compiled, "errors": errors}


# =============================================================================
# Construction et lancement du knowledge
# =============================================================================

def construire_knowledge():
    """Construit et enregistre tous les skills du knowledge depuis la méthodologie."""
    config = charger_methodologie()
    registre = SkillRegistry()

    # Skill utilitaire
    registre.enregistrer("lire_choix", LireChoixSkill("lire_choix"))

    # Skills actions
    registre.enregistrer("fonction", FonctionSkill("fonction"))
    registre.enregistrer("programme", ProgrammeSkill("programme"))

    # Choix du sous-knowledge depuis la config
    choix_labels = config["sous_knowledge"]["choix"]

    # Skills sous-knowledge (depuis la méthodologie)
    knowledge_config = []
    for knowledge in config["knowledge_principal"]["knowledge"]:
        lettre = knowledge["lettre"]
        question_ids = []
        for question in knowledge["questions"]:
            qid = question["id"]
            question_ids.append(qid)
            registre.enregistrer(qid, SousKnowledgeSkill(
                qid,
                action_vrai_skill=question["action_vrai"],
                message_vrai=question["message_vrai"],
                choix_labels=choix_labels
            ))
        knowledge_config.append((knowledge["nom"], lettre, question_ids))

    # Skills knowledge secondaires
    for label, lettre, questions in knowledge_config:
        registre.enregistrer(label, KnowledgeSecondaireSkill(label, lettre, questions))

    # Skill grille
    registre.enregistrer("afficher_grille", AfficherGrilleSkill(
        "afficher_grille", knowledge_config,
        config["message_fin_complet"], config["message_fin_incomplet"]))

    # Skill principal
    knowledge_secondaires = [(label, label) for label, _, _ in knowledge_config]
    registre.enregistrer("knowledge_principal", KnowledgePrincipalSkill("knowledge_principal", knowledge_secondaires))

    return registre


if __name__ == "__main__":
    registre = construire_knowledge()
    print("Skills enregistrés :", ", ".join(registre.lister()))
    print()
    registre.executer("knowledge_principal")
