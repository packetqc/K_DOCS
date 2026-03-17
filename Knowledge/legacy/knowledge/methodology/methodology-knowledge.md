# Knowledge de validation des travaux | Work Validation Knowledge

## Message de fin complet

FR: Merci d'avoir complété l'étape de validation des travaux.
EN: Thank you for completing the work validation step.

## Message de fin incomplet

FR: Votre validation n'est pas complète. Recommencez dès que vous le pourrez.
EN: Your validation is not complete. Please try again as soon as you can.

## Choix du sous-knowledge

FR: Vrai, Faux, Passer
EN: True, False, Skip

## Knowledge Principal

### Validation de la demande | Request validation (lettre: A)

| ID | Choix FR                 | Choix EN                 | Action           | Message FR                                                 | Message EN                                                  |
|----|--------------------------|--------------------------|------------------|------------------------------------------------------------|-------------------------------------------------------------|
| A1 | Confirmez le titre       | Confirm the title        | fonction         | >>> Je suis la fonction A1.                                | >>> I am function A1.                                       |
| A2 | Confirmez la description | Confirm the description  | programme        | >>> Je suis le programme A2.                               | >>> I am program A2.                                        |
| A3 | Confirmez le projet      | Confirm the project      | fonction         | >>> Je suis la fonction A3.                                | >>> I am function A3.                                       |
| A4 | Exécuter la demande      | Execute request          | executer_demande | (programmatique - exécute la commande initiale de session) | (programmatic - executes the initial session command)       |

### Qualité du travail | Work quality (lettre: B)

| ID | Choix FR                 | Choix EN                 | Action    | Message FR                                          | Message EN                                          |
|----|--------------------------|--------------------------|-----------|-----------------------------------------------------|-----------------------------------------------------|
| B1 | Tests et build           | Tests and build          | programme | >>> Tests et build exécutés avec succès.             | >>> Tests and build executed successfully.           |
| B2 | Revue de code            | Code review              | fonction  | >>> Revue de code complétée.                         | >>> Code review completed.                           |
| B3 | Métriques                | Metrics                  | programme | >>> Métriques de session compilées.                  | >>> Session metrics compiled.                        |
| B4 | Tous                     | All                      | tous      | >>> Toute la qualité du travail validée.             | >>> All work quality validated.                      |

### Intégrité de session | Session integrity (lettre: C)

| ID | Choix FR                 | Choix EN                 | Action    | Message FR                                          | Message EN                                          |
|----|--------------------------|--------------------------|-----------|-----------------------------------------------------|-----------------------------------------------------|
| C1 | Commits progressifs      | Progressive commits      | fonction  | >>> Commits progressifs vérifiés.                    | >>> Progressive commits verified.                    |
| C2 | Cache à jour             | Cache up to date         | programme | >>> Cache de session mis à jour.                     | >>> Session cache updated.                           |
| C3 | Issue commentée          | Issue commented          | fonction  | >>> Commentaires d'issue vérifiés.                   | >>> Issue comments verified.                         |
| C4 | Tous                     | All                      | tous      | >>> Toute l'intégrité de session validée.            | >>> All session integrity validated.                 |

### Documentation | Documentation (lettre: D, methodology: methodology-documentation)

| ID | Choix FR                      | Choix EN                     | Action   | Message FR                               | Message EN                            |
|----|-------------------------------|------------------------------|----------|------------------------------------------|---------------------------------------|
| D1 | Documentation système         | System documentation         | fonction:documentation_systeme | >>> Documentation système complétée. (documentation_systeme)     | >>> System documentation completed. (documentation_systeme)   |
| D2 | Documentation utilisateur     | User documentation           | fonction:documentation_utilisateur | >>> Documentation utilisateur complétée. (documentation_utilisateur) | >>> User documentation completed. (documentation_utilisateur)     |
| D3 | Tous                          | All                          | tous     | >>> Toute la documentation complétée.    | >>> All documentation completed.      |

### Registre des fonctions | Function Registry

FR: Ce registre documente le comportement de chaque fonction référencée dans les tableaux ci-dessus. L'utilisateur peut **consulter** ce registre mais ne peut pas modifier le comportement des fonctions — elles sont programmatiques. Le nom de la fonction (colonne Action) sert de clé de référence.

EN: This registry documents the behavior of each function referenced in the tables above. The user can **view** this registry but cannot modify function behavior — they are programmatic. The function name (Action column) serves as the reference key.

| Fonction | Knowledge | Source | Comportement FR | Behavior EN |
|----------|-----------|--------|-----------------|-------------|
| `documentation_systeme` | D1 | `methodology/methodology-documentation.md` § Documentation système | Consulte `compilations_post_execution` pour identifier les fichiers changés, puis évalue les fichiers essentiels (README, NEWS, PLAN, LINKS, VERSION, CLAUDE, CHANGELOG, STORIES) pour mise à jour | Consults `compilations_post_execution` to identify changed files, then evaluates essential files (README, NEWS, PLAN, LINKS, VERSION, CLAUDE, CHANGELOG, STORIES) for update |
| `documentation_utilisateur` | D2 | `methodology/methodology-documentation.md` § Documentation utilisateur | Consulte `compilations_post_execution` pour évaluer l'ampleur des changements, puis vérifie les guides, tutoriels et publications utilisateur à créer ou mettre à jour | Consults `compilations_post_execution` to evaluate change scope, then checks user guides, tutorials and publications to create or update |

### Approbation | Approval (lettre: E)

| ID | Choix FR                      | Choix EN                     | Action   | Message FR                               | Message EN                            |
|----|-------------------------------|------------------------------|----------|------------------------------------------|---------------------------------------|
| E1 | Résumé pré-sauvegarde         | Pre-save summary             | fonction | >>> Résumé pré-sauvegarde compilé.       | >>> Pre-save summary compiled.        |
| E2 | Sauvegarde finale             | Final save                   | programme | >>> Sauvegarde finale exécutée.         | >>> Final save executed.              |
| E3 | Tous                          | All                          | tous     | >>> Approbation complète — session prête à fermer. | >>> Approval complete — session ready to close. |
| E4 | Approuver                     | Approve                      | tous     | >>> Travaux approuvés officiellement.    | >>> Work officially approved.         |
