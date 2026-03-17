---
name: documentation
description: Skill de documentation. Lit la methodology documentation avant d'exécuter les tâches de documentation système ou utilisateur.
---

## Skill Documentation

Ce skill est invoqué automatiquement par le knowledge-validation quand l'utilisateur sélectionne une option du Knowledge Documentation (D1, D2, ou D3/Tous).

### Pré-exécution — Chargement dynamique des méthodologies

Avant d'exécuter toute tâche de documentation, charger les méthodologies pertinentes via l'outil Read.

**IMPORTANT — Déduplication des lectures** : Avant de lire un fichier de méthodologie, vérifier s'il a déjà été lu dans cette session via `filter_unread_methodologies()` (task_workflow.py). Ne lire que les fichiers **non encore lus**. Après lecture, appeler `mark_methodologies_read()` pour enregistrer. Cela évite de gonfler le contexte et de provoquer une compaction prématurée.

```python
from knowledge.engine.scripts.session_agent.task_workflow import filter_unread_methodologies, mark_methodologies_read

# methodologies = liste résolue par detect_command()["methodologies"]
to_read = filter_unread_methodologies(methodologies)
# Lire seulement to_read via Read tool
# Puis enregistrer :
mark_methodologies_read(to_read)
```

**Principe** : Le répertoire `knowledge/methodology/` utilise une nomenclature par famille. Le chargement est **contextuel** — les commandes de gestion (listing, vérification) ne chargent que la méthodologie primaire, tandis que les commandes de travail réel chargent la famille complète + les standards de méthode de travail.

#### Distinction gestion vs travail

| Type | Exemples | Chargement |
|------|----------|------------|
| **Gestion** | `pub list`, `pub check`, `docs check`, `weblinks` | Méthodologie primaire seulement |
| **Travail** | `pub new`, `pub sync`, `pub export`, `doc review`, `webcard`, `visual` | Famille complète + standards |

Les commandes de gestion n'ont pas besoin de spécialisation — elles listent ou valident. Les commandes de travail créent, modifient, ou analysent — elles nécessitent le contexte complet.

#### Logique de chargement par type (Knowledge D)

**D1 — Documentation système** :
1. Lire `knowledge/methodology/methodology-documentation.md` (base)
2. Lire les fichiers pertinents à la documentation système :
   - `methodology-documentation-generation.md` — workflows de génération
   - `methodology-documentation-engineering.md` — pratiques d'ingénierie
   - `methodology-documentation-web.md` — si la documentation système touche au web
3. Standards de méthode de travail :
   - `methodology-working-style.md` — style de collaboration
   - `methodology-task-workflow.md` — cycle de travail
   - `methodology-engineer.md` — pratiques d'ingénierie

**D2 — Documentation utilisateur** :
1. Lire `knowledge/methodology/methodology-documentation.md` (base)
2. Lire les fichiers pertinents à la documentation utilisateur :
   - `methodology-documentation-audience.md` — ciblage d'audience
   - `methodology-documentation-generation.md` — workflows de génération
   - `methodology-documentation-web.md` — si export web nécessaire
3. Standards de méthode de travail (même liste que D1)

**D3 — Tous** : Charger toute la famille + standards, puis exécuter D1 et D2 en séquence.

### Détection automatique par commande

Quand le skill est invoqué via une commande détectée dans le `COMMAND_REGISTRY` (task_workflow.py), le champ `methodologies` du résultat de `detect_command()` contient déjà la liste résolue. Claude doit lire **tous** les fichiers de cette liste.

**Commandes de travail (famille chargée + standards)** :

| Commande | Méthodologie primaire | Fichiers résolus |
|----------|-----------------------|-----------------|
| `pub new` | methodology-documentation.md | 6 doc + 3 standards = 9 fichiers |
| `pub sync` | methodology-documentation.md | 9 fichiers |
| `pub export` | methodology-system-web-export.md | 10 fichiers |
| `doc review` | methodology-documentation.md | 9 fichiers |
| `webcard` | methodology-documentation-web.md | 9 fichiers |
| `visual *` / `deep` / `analyze` | methodology-documentation-visual.md | 9 fichiers |

**Commandes de gestion (primaire seulement)** :

| Commande | Méthodologie | Fichiers résolus |
|----------|-------------|-----------------|
| `pub list` | methodology-documentation.md | 1 fichier |
| `pub check` | methodology-documentation.md | 1 fichier |
| `docs check` | methodology-documentation.md | 1 fichier |
| `weblinks` / `weblinks --admin` | methodology-documentation-web.md | 1 fichier |

### Standards de méthode de travail (WORKING_STYLE_STANDARDS)

Les 3 fichiers standards sont ajoutés automatiquement par `resolve_methodologies()` pour toute famille de type travail (`methodology-documentation` ou `methodology-interactive`) :

1. **`methodology-working-style.md`** — Comment l'utilisateur travaille, ses attentes, ses patterns
2. **`methodology-task-workflow.md`** — Le cycle de travail structuré (8 étapes)
3. **`methodology-engineer.md`** — Les pratiques d'ingénierie

Ces standards assurent que Claude opère selon la méthode de travail établie, peu importe le type de commande.

### Exécution concrète — Flow D1/D2

Quand l'utilisateur sélectionne D1 ou D2 (ou D3/Tous qui les lance en séquence), voici le flow **complet** :

#### Étape 1 — Détection des changements

Exécuter le script de détection :

```bash
python3 knowledge/engine/scripts/documentation_validation.py d1 --json   # Pour D1
python3 knowledge/engine/scripts/documentation_validation.py d2 --json   # Pour D2
python3 knowledge/engine/scripts/documentation_validation.py both --json  # Pour D3/Tous
```

Le script retourne un JSON structuré avec :
- `has_changes` : booléen — s'il y a eu des changements dans la session
- `action_items` : liste d'actions concrètes à réaliser
- `action_items_count` : nombre d'actions requises

#### Étape 2 — Exécution des mises à jour (par Claude)

**D1 — Documentation système** :
Si `action_items_count > 0`, Claude exécute les mises à jour suivantes selon les `action_items` détectés :

| Type d'action | Ce que Claude fait |
|---|---|
| `essential_file` (NEWS.md) | Lire NEWS.md, ajouter une entrée sous la date courante résumant les changements de la session |
| `essential_file` (CHANGELOG.md) | Lire CHANGELOG.md, ajouter les PRs/issues de la session |
| `essential_file` (PLAN.md) | Lire PLAN.md, mettre à jour What's New si nouvelle fonctionnalité |
| `essential_file` (LINKS.md) | Lire LINKS.md, ajouter toute nouvelle URL web créée |
| `methodology` | Vérifier la cohérence des fichiers methodology modifiés |
| `claude_md` | Vérifier si CLAUDE.md reflète les changements d'infrastructure |
| `session_cache` | Mettre à jour le work_summary dans le cache de session |

Si `has_changes` est `false` (aucun changement dans la session) :
- Résultat = **Vrai** — rien à documenter, tout est à jour.

Si `action_items_count == 0` mais `has_changes` est `true` :
- Les fichiers essentiels sont déjà à jour — Résultat = **Vrai**.

**D2 — Documentation utilisateur** :
Si `action_items_count > 0`, Claude exécute les mises à jour suivantes :

| Type d'action | Ce que Claude fait |
|---|---|
| `publication_update` | Lire la publication affectée, vérifier si le contenu reflète les changements, mettre à jour si nécessaire |
| `pub_sync` | Synchroniser la source (`knowledge/data/publications/`) vers le web (`docs/knowledge/data/publications/`) |
| `web_pages` | Vérifier la cohérence des pages web modifiées |
| `success_story` | Évaluer si la session mérite une success story et en créer une si approprié |
| `bilingual_mirror` | Créer ou mettre à jour les pages FR/EN manquantes |

#### Étape 3 — Résultat

- **Vrai** : si toutes les actions ont été complétées avec succès, OU s'il n'y avait aucune action nécessaire
- **Faux** : si au moins une action a échoué ou n'a pas pu être complétée

Le résultat est enregistré dans `knowledge_resultats.json` pour la grille.

#### D3 — Tous (pipeline complet)

Quand D3 est sélectionné :
1. Exécuter D1 (documentation système) → enregistrer résultat D1
2. Exécuter D2 (documentation utilisateur) → enregistrer résultat D2
3. D3 = Vrai si D1 ET D2 sont Vrai, sinon Faux
4. **Si tout Vrai → retour au Knowledge Principal**
5. **Si échec → rester au Knowledge Secondaire** (l'utilisateur peut relancer individuellement)

### Résultat

Retourne "Vrai" si la documentation a été complétée avec succès, "Faux" sinon.
