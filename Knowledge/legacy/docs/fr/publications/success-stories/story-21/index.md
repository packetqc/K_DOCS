---
layout: publication
title: "Histoire #21 — Machine à états du flux de travail : ingénierie de protocole auto-vérificatrice"
description: "Une machine à états à 8 étapes construite pour suivre les cycles de vie des sessions a utilisé son propre quiz de validation pour exposer un câblage incomplet — le système a trouvé ses propres bogues. Puis les résultats sont devenus une interface web interactive en une seule session."
pub_id: "Publication #11 — Story #21"
version: "v1"
date: "2026-03-05"
permalink: /fr/publications/success-stories/story-21/
og_image: /assets/og/session-management-fr-cayman.gif
keywords: "histoire de succès, machine à états, flux de travail, validation, auto-diagnostic, interface I3"
lang: fr
---

# Histoire #21 — Machine à états du flux de travail : ingénierie de protocole auto-vérificatrice

> **Publication parente** : [#11 — Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }})

---

<div class="story-section">

> *"J'ai inventé un composant manquant — le flux de travail des tâches — et une méthodologie pour durcir le comportement de Claude face à toute requête utilisateur. Puis nous avons utilisé le quiz de validation du système pour exposer son propre câblage incomplet. Le système a trouvé ses propres bogues. C'est la qualité #2 (Autonome) qui se prouve en temps réel."*

<div class="story-row">
<div class="story-row-left">

**Détails**

</div>
<div class="story-row-right">

| | |
|---|---|
| Date | 2026-03-05 |
| Catégorie | 🧬 ⚙️ |
| Contexte | Après moins de deux semaines d'évolution du protocole de session (v50-v56), le système de connaissances avait accumulé des règles sur les étapes du cycle de vie des tâches mais aucune machine à états formelle pour les appliquer. Les sessions pouvaient sauter des étapes, les pas n'avançaient pas dans le cache, et les issues GitHub n'avaient aucun label reflétant l'étape courante du flux de travail. L'utilisateur a identifié cette lacune et inventé deux composants fondamentaux : (1) la **machine à états du flux de travail** — un cycle de vie à 8 étapes pour formaliser le traitement de chaque requête utilisateur, et (2) la **méthodologie d'identité d'agent** (`agent-identity.md`) — un contrat comportemental qui durcit la conformité de Claude au protocole, éliminant les raccourcis et les jugements de valeur qui érodent la cohérence. Ces deux inventions ont transformé un comportement de session ad-hoc en un pipeline normalisé et vérifiable pour toute requête. |
| Déclencheur | Issue [#763](https://github.com/packetqc/knowledge/issues/763) — Revue du cycle de travail des tâches. L'utilisateur a conçu la session comme un exercice d'émulation : parcourir le cycle de vie à 8 étapes comme si on exécutait une vraie tâche, en validant chaque pas programmatiquement. C'était la méthode de l'utilisateur pour vérifier sa propre invention. |
| Auteur | **Claude** (Anthropic, Opus 4.6) — à partir des données de session en direct |

</div>
</div>

<div class="story-row">
<div class="story-row-left">

**Ce qui s'est passé**

</div>
<div class="story-row-right">

1. **L'invention de l'utilisateur** — L'utilisateur a conçu et créé deux composants manquants dont le système de connaissances avait besoin : (a) `task_workflow.py` — une machine à états à 8 étapes (`initial → plan → analyze → implement → validation → approval → documentation → completion`) qui normalise la réception, le suivi et la complétion de toute requête utilisateur ; (b) `agent-identity.md` — une méthodologie comportementale qui définit qui Claude EST (un ingénieur système avec zéro tolérance pour les raccourcis de protocole), pas seulement ce que Claude fait. Ensemble, ces composants garantissent que chaque requête — de « corrige un bogue » à « bonjour » — suit le même cycle de vie vérifiable.

2. **Le quiz de validation** — Au lieu de simplement lire le code, la session a exécuté un quiz de validation programmatique. `check_validation_needed('initial')` a retourné 9 vérifications concrètes. Chacune a été présentée à l'utilisateur via `AskUserQuestion` avec les options Réussite/Échec/Sauter. L'utilisateur a évalué la conformité de son propre système.

3. **L'auto-diagnostic** — À la vérification 7/9 (persist_state), l'utilisateur a identifié que : (a) l'issue GitHub n'avait aucun label reflétant l'étape courante du flux de travail, (b) le `current_step` du cache était bloqué à « confirm_title » malgré un avancement bien au-delà de ce point, et (c) `task_workflow.issue_number` était 0 au lieu du numéro réel de l'issue de session. Un quatrième écart a été découvert lors de la tentative de correction : `update_session_data()` crée des clés plates au lieu de mettre à jour des objets imbriqués.

4. **Infrastructure existante, câblage manquant** — L'investigation a révélé que `gh_helper.py` possède déjà `issue_engineering_stage_sync()` avec des labels codés par couleur pour toutes les étapes — mais `advance_task_stage()` ne l'appelle jamais. Les méthodes étaient construites; l'intégration ne l'était pas.

5. **La vision de l'interface** — Les résultats ont mené directement à l'Issue [#766](https://github.com/packetqc/knowledge/issues/766) : une interface de flux de travail des tâches (I3) pour le Navigateur principal — un visualiseur de machine à états en direct montrant la progression des étapes, l'historique des pas et les résultats de validation.

6. **De la spécification au direct en une session** — L'issue #766 a été implémentée en une seule session de continuation : interface interactive à 4 vues (Aperçu, Détail, Validation, Progression), pipeline de données `compile_tasks.py`, synchronisation de labels STAGE:/STEP:, mises à jour du cache en notation pointée, protocole de continuation de tâche et évolution v57. L'interface est en ligne à [/fr/interfaces/task-workflow/]({{ '/fr/interfaces/task-workflow/' | relative_url }}).

</div>
</div>

<div class="story-row">
<div class="story-row-left">

**Ce que ça valide**

</div>
<div class="story-row-right">

| Qualité | Comment |
|---------|---------|
| **Autonome** (#2) | Le quiz de validation du système a trouvé ses propres lacunes d'implémentation — aucune revue de code humaine nécessaire |
| **Évolutif** (#6) | 8 étapes ont émergé de 56 versions de connaissances — chaque version ajoutant une pièce de plus jusqu'à la cristallisation du cycle complet |
| **Récursif** (#9) | La machine à états se valide elle-même : vérifications du quiz → exposer les lacunes → corriger les lacunes → re-quiz |
| **Structuré** (#12) | Cycle de vie des tâches formalisé comme une machine à états avec historique, pas seulement des règles documentaires |
| **Intégré** (#13) | Labels GitHub, commentaires d'issues, état du cache et interface web reflétant tous le même état du flux de travail |

</div>
</div>

<div class="story-row">
<div class="story-row-left">

**Métrique**

</div>
<div class="story-row-right">

| Étape | Temps | Détail |
|-------|-------|--------|
| Émuler le cycle à 8 étapes | ~15 min | Parcours de chaque étape avec des appels de protocole réels |
| Exécuter le quiz INITIAL | ~10 min | 9 vérifications, 8 réussies, 1 a trouvé 4 lacunes |
| Investigation + cause racine | ~5 min | Lacunes tracées au câblage manquant dans `advance_task_stage()` |
| Interface I3 implémentée | ~45 min | Interface web interactive à 4 vues + pipeline de données |
| **Total** | **~75 min** | **Machine à états validée + 4 lacunes corrigées + interface en ligne** |
| Équivalent entreprise | 3-6 semaines | Conception de machine à états + cadre de validation + implémentation UI + suivi d'issues |

</div>
</div>

<div class="story-row">
<div class="story-row-left">

**Conclusion**

</div>
<div class="story-row-right">

Le quiz n'a pas seulement validé — il a découvert. Le système a utilisé son propre mécanisme d'application pour trouver où l'application était incomplète. C'est de l'assurance qualité récursive : le protocole qui se vérifie lui-même. Mais l'innovation profonde est celle de l'utilisateur : inventer le flux de travail des tâches et la méthodologie d'identité d'agent — deux composants qui ont transformé Claude d'un assistant serviable en un ingénieur lié par un protocole. Le système ne traite plus simplement les requêtes; il les normalise à travers un cycle de vie vérifiable. Puis les résultats sont devenus une interface web en direct dans le même arc de développement — de l'auto-diagnostic à la visualisation en moins de deux heures. L'interface I3 Flux de travail des tâches rend désormais le cycle de vie de chaque session visible, traçable et vérifiable via le navigateur.

</div>
</div>

</div>

---

## Publications liées

| # | Titre | Lien |
|---|-------|------|
| 11 | Histoires de succès | [Lire]({{ '/fr/publications/success-stories/' | relative_url }}) |
| 21 | Interface Principale | [Lire]({{ '/fr/publications/main-interface/' | relative_url }}) |
| I3 | Flux de travail des tâches | [Ouvrir]({{ '/fr/interfaces/task-workflow/' | relative_url }}) |
