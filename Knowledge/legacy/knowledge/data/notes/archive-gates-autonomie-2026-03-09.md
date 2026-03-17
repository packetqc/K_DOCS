# Archive — Système de Gates d'Autonomie (retiré 2026-03-09)

Ce système a été retiré car le concept d'autonomie causait des déviations.
Remplacé par des étapes obligatoires programmées dans le flow.

## Ancien contenu de CLAUDE.md — section "Gates d'autonomie"

### Liste des gates

| Gate | S'ouvrait quand | Permettait UNIQUEMENT | Se refermait quand |
|------|----------------|----------------------|-------------------|
| **G1** | L'utilisateur clique "Exécuter la demande" (A4) | Lancer le programme via `executer_demande.py` — RIEN d'autre | Programme terminé (preuve lue) |
| **G2** | Programme A4 terminé avec preuve valide (code_retour=0) | commit + push des résultats sur la branche de travail | push complété |
| **G3** | "Tous" complété dans un knowledge secondaire | commit + push des résultats sur la branche de travail | push complété |
| **G4** | Chaque réponse de l'utilisateur au quiz | Sauvegarder `knowledge_resultats.json` + commit + push | push complété |
| **G5** | "terminé"/"done" en session interactive | Finaliser la session interactive (bannière + sauvegarde + commit + push) — puis RETOUR OBLIGATOIRE au Knowledge Principal | push complété |
| **G6** | Skip au Knowledge Principal (fin du quiz) | PR + merge vers main via `gh_helper.py` (`pr_create_and_merge`) | merge complété |
| **G7** | Issue GitHub existante + résultat à poster | Poster un commentaire sur l'issue (succès ou échec) | commentaire posté |

### Raison du retrait

L'autonomie, même sous forme de gates temporaires, donnait trop de latitude à Claude.
Le concept même d'"autonomie" encourageait des déviations (issues supplémentaires,
reformulations de titres, initiatives non demandées).

### Remplacement

Des **étapes obligatoires programmées** dans le flow :
- Après exécution → commit + push (étape programmée, pas de choix)
- Après Skip au principal → PR + merge (étape programmée, pas de choix)
- Chaque réponse → sauvegarde + commit + push (étape programmée)

Aucune "autonomie" n'est nécessaire. Ce sont des commandes dans le programme.
