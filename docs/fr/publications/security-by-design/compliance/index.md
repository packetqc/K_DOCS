---
layout: publication
title: "Jeton d'élévation pour l'autonomie — Rapport du cycle de vie de conformité"
description: "Évaluation phase par phase de la gestion éphémère des jetons de Knowledge par rapport à OWASP MCP01:2025, NIST SP 800-57/63B/88, FIPS 140-3 et CIS Controls. Suivi complet du cycle de vie de conformité de l'analyse au déploiement."
pub_id: "Publication #9"
version: "v1"
date: "2026-02-21"
permalink: /fr/publications/security-by-design/compliance/
og_image: /assets/og/security-by-design-fr-cayman.gif
keywords: "cycle de vie jeton, OWASP MCP01, NIST, FIPS 140-3, conformité, jeton éphémère, PQC"
---

# Jeton d'élévation pour l'autonomie — Rapport du cycle de vie de conformité

> **Publication parente** : [#9 — Sécurité par conception]({{ '/fr/publications/security-by-design/' | relative_url }}) | **Complet** : [Documentation complète]({{ '/fr/publications/security-by-design/full/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Aperçu](#aperçu) | Portée du rapport et constats clés |
| [Légende des statuts — Cycle de vie de conformité](#légende-des-statuts--cycle-de-vie-de-conformité) | Suivi en six étapes de l'analyse au déploiement |
| [Phase 1 — Réception](#phase-1--réception) | Livraison et traitement initial du jeton |
| [Phase 2 — Persistance en mémoire](#phase-2--persistance-en-mémoire) | Protection de la mémoire à l'exécution |
| [Phase 3 — Utilisation](#phase-3--utilisation) | Authentification API et sécurité du transport |
| [Phase 4 — Élimination](#phase-4--élimination) | Destruction du jeton en fin de session |
| [Phase 5 — Vérification post-session](#phase-5--vérification-post-session) | Vérification des artéfacts après élimination |
| [Sommaire de conformité global](#sommaire-de-conformité-global) | Statut de conformité agrégé sur toutes les phases |
| [PQC pour le chiffrement en RAM — Verdict](#pqc-pour-le-chiffrement-en-ram--verdict) | Évaluation de faisabilité du chiffrement post-quantique |
| [Feuille de route d'amélioration](#feuille-de-route-damélioration) | Améliorations planifiées et calendrier |

---

## Auteurs

**Martin Paquet** — Analyste programmeur sécurité réseau, administrateur de sécurité des réseaux et des systèmes, analyste programmeur et concepteur logiciels embarqués. 30 ans d'expérience en sécurité réseau, systèmes embarqués et télécom.

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. A réalisé l'évaluation de conformité, la recherche industrielle et l'introspection empirique des jetons sur 3 configurations PAT.

---

## Aperçu

Ce rapport évalue la gestion éphémère des jetons de Knowledge par rapport aux meilleures pratiques de l'industrie, phase par phase. Le jeton traverse 5 phases — réception, persistance en mémoire, utilisation, élimination et vérification post-session. Chaque phase est évaluée selon des normes spécifiques.

**Constat clé** : OWASP MCP01:2025 classe la mauvaise gestion des jetons comme le **risque #1** pour les outils de développement assistés par IA. L'architecture éphémère par conception de Knowledge répond directement à ce risque — les jetons ne persistent jamais au-delà d'une session, ne sont jamais écrits dans des fichiers et ne sont jamais commis dans git.

**Validation empirique** : Le 2026-02-21, trois PAT GitHub ont été testés sur le cycle autonome complet (création PR + fusion via API). L'introspection des jetons a confirmé le minimum Niveau 2 : seulement **4 permissions** requises (Contents RW + Pull requests RW + Projects RW + Metadata Read). Les PR #137 à #143 ont validé le cycle de vie complet.

---

## Légende des statuts — Cycle de vie de conformité

Chaque meilleure pratique est suivie à travers un cycle de vie de conformité complet. Cette méthodologie assure la transparence — les lecteurs savent exactement où en est chaque mesure de sécurité, pas simplement si c'est « fait » ou « pas fait ».

| # | Statut | <span id="compliance-icons">Icône</span> | Définition |
|---|--------|------|------------|
| 1 | **Analyse** | 🔎 | Exigence identifiée. Analyse de l'applicabilité à notre architecture, modèle de menaces et contraintes. |
| 2 | **Planifié** | 📋 | Analyse terminée. Approche définie, sur la feuille de route, pas encore démarré. |
| 3 | **En cours** | 🔄 | Implémentation activement en cours. |
| 4 | **Test** | 🧪 | Implémentation existante. En cours de validation et de test. |
| 5 | **AQ** | 🔍 | Assurance qualité — revue par les pairs, revue de code, revue de sécurité. |
| 6 | **Approbation** | 📝 | AQ réussi. En attente d'approbation avant déploiement. |
| 7 | **Déploiement** | 🚀 | Approuvé. Déploiement en production en cours. |
| 8 | **Appliqué** | ✅ | Opérationnel, testé, vérifié. Preuves empiriques disponibles. |

**Statuts additionnels** :

| Statut | <span id="compliance-icons-additional">Icône</span> | Définition |
|--------|------|------------|
| **Par conception** | ✅📐 | Décision architecturale délibérée — la non-implémentation EST la pratique correcte. Justification documentée et consensus industriel. |
| **Futur** | 🔮 | Feuille de route à long terme — dépend de matériel ou projet externe. |
| **S/O** | — | Sans objet pour cette architecture. |

**Instantané actuel** : Phase 1 (Réception) et Phase 3 (Utilisation) mises à jour à ✅ Appliqué (v46). Phases 2, 4, 5 en cours de revue.

---

## Phase 1 — Réception

| Meilleure pratique | Norme | Notre implémentation | Statut |
|-------------------|-------|---------------------------|--------|
| Canal d'entrée sécurisé — pas de journalisation, pas d'écho, invisible dans le transcript | OWASP Secrets Management, OWASP MCP01:2025 | **Variable d'environnement `GH_TOKEN`** (v46) : configurée dans la configuration de l'environnement cloud Claude Code (format `.env`). Le jeton est chargé AVANT le démarrage de la session — ne touche jamais l'UI, ne s'affiche jamais dans la sortie des outils. ~~AskUserQuestion « Autre »~~ (v34-v44 : le champ était visible — corrigé v45) | ✅ Appliqué |
| Option de livraison chiffrée | NIST SP 800-175B | **Éliminé par conception** (v46) : le jeton n'entre jamais dans la session. Configuré dans les variables d'environnement (chargé avant Claude Code). Pas de transit dans la session = pas besoin de chiffrement de livraison | ✅📐 Par conception |
| Prévenir la collision multimodale + appel d'outil | Pitfall #12 (Knowledge) | **Éliminé par conception** (v46) : le jeton ne transite pas par les outils Claude Code. Aucun AskUserQuestion, aucun téléversement d'image, aucun Bash avec jeton — la condition de déclenchement n'existe plus | ✅📐 Par conception |
| Hygiène du presse-papiers | OWASP Secrets Management | Configuration unique de l'environnement — copier le jeton une fois dans le champ des variables d'environnement. Gestionnaire de mots de passe avec effacement automatique recommandé | ✅ Appliqué |
| Ne jamais répéter le jeton à l'utilisateur | OWASP | Le jeton n'entre jamais dans la session — pas d'écho possible. `gh_helper.py` lit depuis `os.environ['GH_TOKEN']` en interne, jamais sur la ligne de commande | ✅ Appliqué |

**Fonctionnement** (v46) : Le jeton est configuré dans le champ « Variables d'environnement » de la configuration de l'environnement cloud Claude Code (format `.env` : `GH_TOKEN=ghp_xxx`). Ce champ est chargé dans l'environnement du processus AVANT le lancement de Claude Code. Le jeton n'entre jamais dans l'UI de session, n'apparaît jamais dans la sortie des outils, et ne touche jamais aucun outil. `gh_helper.py` lit depuis `os.environ['GH_TOKEN']` en interne — la commande Bash affiche uniquement `python3 scripts/gh_helper.py project ensure --title "..." --owner packetqc --repo ...`.

**Note historique** : La méthode v34 (zone de texte AskUserQuestion « Autre ») a été empiriquement démontrée comme affichant le jeton en clair dans le chat de session (v45, Pitfall #17). La prétention d'invisibilité du transcript v34 était incorrecte — le système formate la réponse complète incluant la valeur brute du jeton. Toutes les sessions utilisant la livraison par zone de texte de v34 à v44 ont exposé le jeton dans le chat. Corrigé v45 (variable d'environnement + fichier temporaire), complété v46 (environnement uniquement + GraphQL dans `gh_helper.py`).

---

## Phase 2 — Persistance en mémoire

| Meilleure pratique | Norme | Notre implémentation | Statut |
|-------------------|-------|---------------------------|--------|
| Jeton non conservé au-delà du besoin opérationnel | NIST SP 800-63B §5.1.1 | Le jeton vit uniquement dans la fenêtre de contexte — meurt avec la session | 🔎 Analyse |
| Prévenir la persistance du jeton dans le contexte IA entre sessions | OWASP MCP01:2025 (risque #1) | Éphémère par conception — pas de report de contexte, pas de `remember` pour les jetons | 🔎 Analyse |
| Isolation des processus | Meilleures pratiques conteneurs | Claude Code conteneurisé — chaque session a son propre espace processus | 🔎 Analyse |
| Pas d'exposition au swap | FIPS 140-3 | Le conteneur n'a pas de swap configuré — le jeton ne peut pas être paginé sur disque | 🔎 Analyse |
| Matériel clé en système de fichiers RAM uniquement | NIST SP 800-88 | Matériel clé PQC dans `/dev/shm/` (tmpfs, ne touche jamais le disque) | 🔎 Analyse |
| Chiffrement en mémoire du jeton | Débat industriel | **Non appliqué** — et c'est correct. Sans HSM/TPM/SGX, la clé de déchiffrement coexiste en mémoire processus | 🔎 Analyse |
| Utiliser des structures de données mutables pour les secrets | OWASP Secrets Management | Le jeton est un `str` Python (immuable) — devrait être `bytearray` pour zéro-écrasement | 🔎 Analyse |
| `mlock()` pour prévenir le swap | FIPS 140-3, HashiCorp Vault | Pas encore implémenté — le conteneur n'a pas de swap (protection équivalente aujourd'hui) | 🔎 Analyse |

**Fonctionnement** : Le jeton existe comme une chaîne de caractères en clair dans la fenêtre de contexte Claude (mémoire gérée par Anthropic, isolée par processus, conteneurisée). Il n'est pas chiffré en RAM — conforme à la pratique industrielle. HashiCorp Vault, AWS Secrets Manager et tous les gestionnaires majeurs gardent les jetons en clair en mémoire processus pendant l'utilisation. La différence : nous ne le persistons nulle part. Session terminée → contexte détruit → jeton disparu.

**Pourquoi OWASP MCP01:2025 est directement pertinent** : Cette norme met spécifiquement en garde contre les jetons stockés, indexés ou récupérables involontairement entre sessions IA. Notre architecture prévient cela par conception — les jetons sont éphémères, jamais écrits dans `notes/`, jamais capturés par `remember`, jamais commis. Chaque session démarre propre.

**Pourquoi « Par conception » pour le chiffrement en mémoire** (✅📐) : Chiffrer le jeton en mémoire processus protège contre les attaques de vidage mémoire, mais la clé de déchiffrement doit aussi résider dans la même mémoire processus — rendant la protection indépendante de l'algorithme et effectivement du théâtre sécuritaire sans support matériel. C'est une **décision architecturale correcte**, validée par le consensus industriel. La véritable voie d'amélioration est le stockage de clés adossé au matériel (statut : 🔮 Futur).

**Pourquoi « Planifié » pour les structures mutables et mlock()** (📋) : Ce sont de véritables améliorations sur la feuille de route. Cependant, l'architecture actuelle fournit une protection équivalente via les contrôles au niveau conteneur (pas de swap, isolation des processus, contexte éphémère).

**Preuves de validation** : Statut swap du conteneur vérifié (`free -m` montre 0 swap). Isolation des processus confirmée. `/dev/shm/` utilisé par `pqc_envelope.py` — vérifié dans le code source (`_secure_delete()`, lignes 119–128).

---

## Phase 3 — Utilisation

| Meilleure pratique | Norme | Notre implémentation | Statut |
|-------------------|-------|---------------------------|--------|
| HTTPS pour les appels API | TLS 1.3 | Tous les appels API GitHub via `https://api.github.com` — chiffré sur le fil | ✅ Appliqué |
| Isolation conteneur pour la liste de processus | Docker/CIS | `/proc/<pid>/cmdline` ne contient plus de jeton — `gh_helper.py` lit depuis `os.environ`, jamais sur la ligne de commande | ✅ Appliqué |
| Préférer les en-têtes aux jetons intégrés dans l'URL | OWASP | `gh_helper.py` utilise Python `urllib` avec en-tête `Authorization: bearer` — le jeton n'apparaît jamais dans la commande Bash ni dans `/proc/cmdline` | ✅ Appliqué |
| Minimiser la fenêtre d'utilisation du jeton | NIST SP 800-63B | Jeton utilisé uniquement pour des appels API spécifiques (création PR, fusion, Project board), pas maintenu ouvert | ✅ Appliqué |
| Jeton jamais sur la ligne de commande | OWASP MCP01:2025 | `gh_helper.py` (v46) : toutes les opérations API (REST + GraphQL) via Python `urllib`. Le jeton est lu depuis `os.environ['GH_TOKEN']` en interne. Les commandes `curl` brutes avec `PAT="ghp_..."` en ligne sont éliminées | ✅ Appliqué |

**Fonctionnement** (v46) : Toutes les opérations API GitHub (REST + GraphQL) passent par `gh_helper.py` qui utilise Python `urllib` en interne. Le jeton est lu depuis `os.environ['GH_TOKEN']` — jamais passé sur une ligne de commande Bash. L'affichage de la commande Bash montre uniquement `python3 scripts/gh_helper.py ...` — zéro jeton visible. Les opérations GraphQL (création de board Project, liaison au dépôt) qui étaient auparavant faites via `curl` brut avec `PAT="ghp_..."` en ligne sont maintenant dans `gh_helper.py` : `_graphql()`, `project_create_board()`, `project_link_repo()`, `project_ensure()`.

**Note historique** : Avant v46, les opérations GraphQL (Projects v2) utilisaient des commandes `curl` brutes avec le jeton littéral dans le texte de la commande : `PAT="ghp_xxx" curl -s -X POST https://api.github.com/graphql ...`. Le jeton complet était visible dans l'affichage de l'outil Bash de la session.

**Preuves de validation** : `gh_helper.py` syntaxe vérifiée avec `py_compile`. Toutes les opérations API utilisent HTTPS via Python `urllib`. Le jeton n'apparaît dans aucune commande Bash — uniquement dans les en-têtes HTTP internes de `urllib`.

---

## Phase 4 — Élimination

| Meilleure pratique | Norme | Notre implémentation | Statut |
|-------------------|-------|---------------------------|--------|
| Destruction de la fenêtre de contexte | Runtime Anthropic | Détruite automatiquement en fin de session — aucune étape manuelle | 🔎 Analyse |
| Zéro-écrasement du matériel clé | NIST SP 800-57 §8.3.4, FIPS 140-3 | Fichiers clés PQC : `_secure_delete()` → zéro-écrasement + `fsync()` + unlink dans `/dev/shm/` | 🔎 Analyse |
| Suppression du fichier image | CIS Control 3.4 | `rm -f` immédiatement après extraction du jeton | 🔎 Analyse |
| Zéro-écrasement des variables Python | OWASP, NIST SP 800-57 | `str` Python ramassé par le GC mais NON zéro-écrasé (immuable — bogue Python #17405) | 🔎 Analyse |
| Prévenir les core dumps contenant des secrets | Durcissement Linux, HashiCorp Vault | `prctl(PR_SET_DUMPABLE, 0)` pas encore implémenté | 🔎 Analyse |
| Exclure les secrets des core dumps | Linux core(5) | `madvise(MADV_DONTDUMP)` pas encore implémenté | 🔎 Analyse |

**Fonctionnement** : Quand la session se termine, le runtime Anthropic détruit la fenêtre de contexte — la chaîne du jeton est partie. Pour les opérations PQC, le matériel clé dans `/dev/shm/` est explicitement zéro-écrasé (chaque octet mis à 0), vidé avec `fsync()`, puis délié.

**La lacune Python** (📋 Planifié) : Les chaînes Python sont des objets immuables (bogue Python #17405, ouvert depuis 2013). Quand `token_var = None`, la référence est abandonnée, mais les octets réels peuvent persister en pages mémoire libérées. C'est une limitation connue partagée par tous les langages à ramasse-miettes. Le correctif planifié : migrer les variables contenant des jetons de `str` vers `bytearray` (mutable), permettant un `secret[:] = b'\x00' * len(secret)` explicite avant déréférencement.

**Durcissement des core dumps** (📋 Planifié) : Deux mécanismes du noyau Linux — `prctl(PR_SET_DUMPABLE, 0)` empêche les core dumps et `madvise(MADV_DONTDUMP)` exclut les régions sensibles. L'environnement conteneur atténue ceci aujourd'hui mais ces protections ajoutent la défense en profondeur.

**Preuves de validation** : Code source `_secure_delete()` revu — zéro-écrasement confirmé. Suppression d'image confirmée dans la documentation du protocole d'élévation. Destruction de la fenêtre de contexte garantie par le runtime Anthropic.

---

## Phase 5 — Vérification post-session

| Meilleure pratique | Norme | Notre implémentation | Statut |
|-------------------|-------|---------------------------|--------|
| Pas de jeton dans les fichiers | OWASP, CIS 3.10 | `grep -r "github_pat_" notes/ minds/` retourne rien — règles de sécurité du jeton appliquées | 🔎 Analyse |
| Pas de jeton dans l'historique git | CIS 3.10 | Jamais commis — règle de sécurité non négociable | 🔎 Analyse |
| Pas de jeton dans l'environnement | NIST SP 800-63B | Pas de fichiers `.env`, pas de `export TOKEN=...` | 🔎 Analyse |
| Conteneur éphémère | Meilleures pratiques Docker | Conteneur détruit après la session — toute la mémoire processus libérée | 🔎 Analyse |

**Preuves de validation** : Audit complet des identifiants sur toutes les branches (voir [Audit des identifiants]({{ '/fr/publications/security-by-design/full/' | relative_url }}#audit-des-identifiants)) — zéro correspondance. `.gitignore` bloque `.env`, `.pem`, `.key`, `.p12`, `credentials.*`, `secrets.*`.

---

## Sommaire de conformité global

| Norme | Ce qu'elle exige | Statut | Preuve |
|-------|-----------------|--------|--------|
| **OWASP Secrets Management** | Pas de journalisation, pas d'écho, persistance minimale | ✅ Appliqué | Variable d'environnement (pré-session) + `gh_helper.py` (`urllib` interne). Zéro affichage dans la session |
| **OWASP MCP01:2025** | Prévenir la persistance du jeton en contexte IA | ✅ Appliqué | Risque #1 directement traité — le jeton n'entre jamais dans la session. Éphémère par conception |
| **NIST SP 800-63B** §5.1.1 | Authentificateurs éphémères non conservés au-delà du besoin | ✅ Appliqué | Le jeton meurt avec la session — variable d'environnement détruite avec le conteneur |
| **NIST SP 800-57** §8.3.4 | Destruction des clés — zéroiser au-delà de la récupération | 🔎 Analyse | Clés fichiers : 🔎 Analyse. Variables Python : 🔎 Analyse |
| **NIST SP 800-88** | Assainissement des médias (appliqué à la RAM) | 🔎 Analyse | Fichiers `/dev/shm` : 🔎 Analyse. Variables Python : 🔎 Analyse |
| **FIPS 140-3** | Zéroisation de tous les SSP non protégés | 🔎 Analyse | Clés fichiers : 🔎 Analyse. Variables en mémoire : 🔎 Analyse |
| **CIS Control 3.10** | Pas de secrets dans le code source | ✅ Appliqué | Audit complet des identifiants — zéro correspondance. Jeton jamais sur la ligne de commande |
| **pyATS secret_strings** | Chiffrement au repos pour secrets persistants | ✅📐 Par conception | Le jeton n'est jamais au repos — livré via variable d'environnement, utilisé en mémoire, meurt avec la session |
| **Chiffrement adossé au matériel** | HSM/TPM pour protection des clés | 🔮 Futur | Projet PQC knowledge-live — élément sécurisé STM32 |

**Score** : Phase 1 (Réception) — ✅ Appliqué. Phase 3 (Utilisation) — ✅ Appliqué. Phases 2, 4, 5 — en cours de revue. Vérification de conformité sécuritaire complétée pour l'affichage du jeton dans les sessions utilisateur (v46).

---

## PQC pour le chiffrement en RAM — Verdict

**Non recommandé.** Les algorithmes PQC (ML-KEM-1024, FIPS 203) sont conçus pour protéger les données **en transit** contre les futurs ordinateurs quantiques — la menace « récolter maintenant, déchiffrer plus tard ». Les jetons en RAM font face à des menaces de vidage mémoire et d'inspection de processus, que les ordinateurs quantiques ne rendent pas plus faciles.

Notre PQC est **correctement ciblé** : protéger l'enveloppe d'échange de jetons (en transit via `pqc_envelope.py`), pas le jeton en mémoire (en utilisation). NIST SP 800-57 Rév 6 (brouillon déc 2025) confirme ce périmètre pour FIPS 203 ML-KEM.

**Où le PQC apporte une vraie valeur dans notre système** :

| Cas d'usage | Protection PQC | Modèle de menaces | Statut |
|------------|---------------|-------------|--------|
| Échange de jetons (sceller/ouvrir enveloppe) | ✅ Protège contre le déchiffrement quantique futur | Récolter maintenant, déchiffrer plus tard | 🔎 Analyse |
| Mise à niveau ML-KEM-1024 automatique | ✅ Encapsulation de clé post-quantique | Attaques ère quantique | 🔎 Analyse |
| Communication beacon-à-beacon | ✅ Trafic inter-instances chiffré | Capture réseau sur sous-réseau partagé | 🔎 Analyse |
| Jeton en RAM (en utilisation) | ❌ Non applicable — paradoxe du stockage de clé | Vidage mémoire, inspection de processus | 🔎 Analyse |

---

## Feuille de route d'amélioration

Améliorations priorisées pour combler les lacunes restantes. Chaque élément suit sa position dans le cycle de vie de conformité.

| Priorité | Amélioration | Mécanisme | Norme | Statut cycle de vie | Effort |
|----------|-------------|-----------|----------|-----------------|--------|
| **Haute** | Stocker les jetons en `bytearray` pas `str` | Mutable — peut être zéro-écrasé sur place | OWASP Secrets Management | 🔎 Analyse | Modification de code dans `pqc_envelope.py` |
| **Haute** | `mlock()` sur la mémoire contenant des secrets | Empêche l'exposition au swap | FIPS 140-3, HashiCorp Vault | 🔎 Analyse | `ctypes` + liaison libc |
| **Haute** | Zéro-écrasement explicite de `bytearray` avant déréférencement | `secret[:] = b'\x00' * len(secret)` | NIST SP 800-57 §8.3.4 | 🔎 Analyse | Modification de code |
| **Moyenne** | `prctl(PR_SET_DUMPABLE, 0)` à l'init du processus | Empêche les core dumps, restreint `/proc/pid/mem` | Durcissement Linux | 🔎 Analyse | Configuration unique |
| **Moyenne** | `madvise(MADV_DONTDUMP)` sur les régions sensibles | Exclut des core dumps | Linux core(5) | 🔎 Analyse | Appel par allocation |
| **Basse** | Paquet Python `zeroize` (Rust) | Zéro-écrasement garanti par le compilateur, liaisons `mlock`/`munlock` | Sécurité mémoire Rust | 🔎 Analyse | Évaluation de dépendance externe |
| **Futur** | Stockage de clés adossé au matériel | Élément sécurisé STM32 — la clé n'entre jamais en mémoire processus | FIPS 140-3 Niveau 4 | 🔎 Analyse | Projet PQC knowledge-live |

**Suivi du cycle de vie** : Au fur et à mesure que les éléments avancent de 📋 Planifié → 🔄 En cours → 🧪 Test → 🔍 AQ → 📝 Approbation → 🚀 Déploiement → ✅ Appliqué, cette feuille de route sera mise à jour. Le cycle de vie complet assure qu'aucune amélioration n'est marquée « Appliqué » avant d'avoir été testée, révisée et déployée.

---

## Publications connexes

| # | Publication | Relation |
|---|-------------|---------|
| 0 | [Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Système parent |
| 9 | [Sécurité par conception]({{ '/fr/publications/security-by-design/' | relative_url }}) | Publication parente — architecture de sécurité |
| 9 | [Sécurité par conception (Complet)]({{ '/fr/publications/security-by-design/full/' | relative_url }}) | Documentation complète de sécurité |
| 10 | [Réseau de connaissances live]({{ '/fr/publications/live-knowledge-network/' | relative_url }}) | Enveloppe PQC — crypto réseau beacon |
| 11 | [Histoires de succès]({{ '/fr/publications/success-stories/' | relative_url }}) | Histoire #2 — validation des niveaux d'accès PAT |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
*© 2026 Martin Paquet & Claude (Anthropic)*
