# Session 2026-03-09 — Projet jetable + Découverte help

## Travail effectué
- `project create Projet jetable` — Board #77, Issue #885/#886, PR #887/#888 mergés
- Knowledge validation complète (19/19 Vrai)

## Découverte majeure : le help volumineux existe toujours

### Contexte
L'utilisateur a tapé `help` après le knowledge. Claude a répondu avec un résumé ad hoc de ~20 lignes au lieu du vrai output.

### Ce qui existe
- `scripts/help_command.py` → lit `methodology/commands.md` (392 lignes)
- `commands.md` contient **7 groupes**, **42+ commandes**, tables formatées, détails Live/Visuals, Part 2 projet, Asset Sync, Command Registry v100
- Avant la migration 2.0, tout ce contenu était inline dans CLAUDE.md (~965 lignes)
- Le contenu a survécu à la migration dans `commands.md` mais le **chemin d'accès** s'est cassé

### Problèmes identifiés
1. **Help hors-knowledge** : quand `en_cours: false`, `help` n'a pas de chemin d'exécution (pas de route A4). Claude improvise un résumé au lieu de lire `commands.md`
2. **Rendu** : `help_command.py` sort en texte brut via Bash. Le markdown n'est pas rendu. Il faut que Claude lise le fichier et l'affiche directement pour avoir le rendu enrichi (tables, gras, code blocks)
3. **`<cmd> ?` contextuel** : chaque section mentionne `<cmd> ?` pour l'aide par commande (usage, exemples, lien publication). À vérifier si c'est câblé

### Action requise
- Implémenter le flow `help` comme commande directe (lire `commands.md` + afficher en rendu riche)
- Implémenter `<cmd> ?` contextuel
- Ces deux fonctions doivent marcher à tout moment, pas seulement pendant le knowledge

### Archéologie git
- Ancien CLAUDE.md complet : `git show 5a71b93^:CLAUDE.md` (965 lignes, 10 sections help inline)
- Migration 2.0 : commit `5a71b93` — contenu extrait vers `commands.md`
- Route help ajoutée post-migration : commit `1b11f7a`
