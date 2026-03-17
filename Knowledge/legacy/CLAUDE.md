# Instructions de session

## Démarrage obligatoire

**IMPORTANT : Au début de CHAQUE nouvelle session, AVANT de répondre à quoi que ce soit, tu DOIS exécuter le skill `knowledge-validation` en utilisant l'outil Skill.**

- Peu importe ce que l'utilisateur écrit comme premier message, le knowledge doit démarrer en premier.
- L'utilisateur doit compléter le knowledge (choisir "Terminer" au knowledge principal) avant que tu puisses traiter sa demande.
- Après que le knowledge est terminé et la grille affichée :
  - Si `demande_executee` est `true` dans `.claude/knowledge_resultats.json` : la demande initiale a DÉJÀ été exécutée avec succès par le programme pendant le knowledge. NE PAS la re-traiter. Considérer la demande comme complétée — attendre simplement la prochaine instruction de l'utilisateur.
  - Si `demande_executee` est `false` : la demande n'a pas été exécutée (soit ce n'était pas une commande reconnue, soit l'exécution a échoué). Dans ce cas, traiter la demande initiale naturellement comme Claude le ferait normalement.

## Persistance du knowledge

- L'état du knowledge est sauvegardé dans `.claude/knowledge_resultats.json`.
- Si ce fichier existe et que `en_cours` est `true`, le knowledge n'est pas terminé : reprendre au niveau indiqué.
- Si ce fichier existe et que `en_cours` est `false`, le knowledge est déjà complété : ne pas relancer.
- Après un compactage de session, TOUJOURS lire ce fichier pour retrouver l'état avant de continuer.

## Retour obligatoire après session interactive

- Quand l'utilisateur tape "terminé" ou "done" en session interactive, **le quiz N'EST PAS terminé**.
- La session interactive est l'équivalent de A4. Après A4, le flow DOIT retourner au Knowledge Principal en mode complet.
- Séquence obligatoire : bannière fin → A4="Vrai" → `demande_executee=true` → commit → **afficher le menu Knowledge Principal** → l'utilisateur valide B, C, D, E ou fait Skip pour la grille.
- Ne JAMAIS considérer "terminé"/"done" comme la fin du knowledge — c'est seulement la fin de la session interactive.

## Opérations GitHub (OBLIGATOIRE)

- **JAMAIS utiliser `gh` CLI** pour les opérations GitHub (PR, issues, merges). Utiliser TOUJOURS `knowledge/engine/scripts/gh_helper.py`.
- Après compaction, cette règle reste en vigueur — ne pas retomber sur `gh` CLI.

```python
from knowledge.engine.scripts.gh_helper import GitHubHelper
gh = GitHubHelper()  # JAMAIS d'arguments au constructeur

# PR : créer et merger
gh.pr_create_and_merge('packetqc/knowledge', 'branch', 'main', 'Title', body='...')

# Issues
gh.issue_create('packetqc/knowledge', 'Title', body='...', labels=['SESSION'])
gh.issue_comment_post('packetqc/knowledge', issue_num, 'body')

# Depuis Bash (chaque appel est un shell frais) :
export GH_TOKEN="$GH_TOKEN" && python3 -c "
from knowledge.engine.scripts.gh_helper import GitHubHelper
gh = GitHubHelper()
print(gh.pr_create_and_merge('packetqc/knowledge', 'branch', 'main', 'Title', body='...'))
"
```

- Le repo va sur chaque **méthode**, jamais sur le constructeur.
- Le token vient de `GH_TOKEN` env var automatiquement.

## Comportement strict — Zéro autonomie

**Principe** : Claude suit le flow programmé à la lettre. Il n'a AUCUNE autonomie. Chaque action est une **étape obligatoire programmée** dans le flow, pas une initiative de Claude.

**Comportement par défaut = STRICT, TOUJOURS** :
- NE prend AUCUNE initiative (pas de création d'issues supplémentaires, pas de modifications non demandées)
- NE modifie JAMAIS les données de l'utilisateur (titres, descriptions, noms — mot pour mot, sans reformulation)
- Suit le flow programmé du skill exactement comme écrit
- Attend les instructions de l'utilisateur pour toute décision

### Étapes obligatoires post-exécution

Ces étapes sont **programmées dans le flow** — elles s'exécutent automatiquement parce que le programme le dit, pas parce que Claude "décide" de les faire :

1. **Après chaque réponse de l'utilisateur au quiz** → sauvegarder + commit + push (étape programmée)
2. **Après exécution réussie (A4 = Vrai)** → commit + push des résultats (étape programmée)
3. **Après exécution échouée (A4 = Faux)** → rollback + commit + push des résultats (étape programmée)
4. **Après "terminé"/"done" en session interactive** → finaliser + commit + push + retour au principal (étape programmée)
5. **Après Skip au Knowledge Principal (fin du quiz)** → PR + merge vers main via `gh_helper.py` (étape programmée, **OBLIGATOIRE**)
6. **Après "Tous" complété dans un knowledge** → commit + push des résultats (étape programmée)
7. **Quand une issue GitHub existe et qu'un résultat est disponible** → poster un commentaire (étape programmée)

### Règles fermes

- **Les règles programmatiques** : pagination, ordre des questions, structure du quiz, nombre d'options AskUserQuestion, persistance des résultats — **fermes et inviolables**.
- **Les données utilisateur** : titres, descriptions, noms de projets = texte EXACT de l'utilisateur. JAMAIS reformulé, JAMAIS embelli, JAMAIS suffixé.
- **Les choix architecturaux** : si plusieurs options existent, demander avant d'implémenter.
- **Les demandes de confirmation** : si l'utilisateur a dit "attends mon OK", attendre.
- Après compaction, ces règles restent en vigueur.

## Persistance de l'exécution (checkpoint)

- Avant toute exécution de programme, un checkpoint est écrit dans `.claude/checkpoint_execution.json`.
- Après un compactage de session, TOUJOURS vérifier ce fichier via `python3 knowledge/engine/scripts/executer_demande.py --status` :
  - `phase: "termine"` → le programme a fini, lire le résultat sans relancer
  - `phase: "en_cours"` → vérifier si la preuve existe (programme fini entre-temps) sinon relancer
  - `phase: "pre_execution"` → le programme n'a pas démarré, relancer
  - Pas de fichier → rien en cours
