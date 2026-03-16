---
layout: publication
title: "Sécurité par conception — Architecture de connaissances IA limitée au propriétaire (Complet)"
description: "Documentation complète du modèle de sécurité pour les dépôts publics de connaissances IA : défense à sept couches, modèle de menaces, résultats d'audit, architecture proxy, opérations limitées au propriétaire, garanties fork/clone et méthodologie d'audit."
pub_id: "Publication #9"
version: "v3"
date: "2026-03-16"
permalink: /fr/publications/security-by-design/full/
og_image: /assets/og/security-by-design-fr-cayman.gif
keywords: "sécurité, PQC, contrôle d'accès, fork sûr, confidentialité, portée propriétaire"
---

# Sécurité par conception — Architecture de connaissances IA limitée au propriétaire
{: #pub-title}

> **Publication parente** : [#0 — Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | **Résumé** : [#9 — Sécurité par conception]({{ '/fr/publications/security-by-design/' | relative_url }})

**Table des matières**

| | |
|---|---|
| [Résumé](#résumé) | Vue d'ensemble et architecture sûre publiquement |
| [La question de sécurité](#la-question-de-sécurité) | Pourquoi les dépôts publics nécessitent une sécurité architecturale |
| [Modèle de menaces](#modèle-de-menaces) | Menaces traitées et protections en place |
| [Couches de sécurité](#couches-de-sécurité) | Architecture de défense à sept couches |
| [Audit des identifiants](#audit-des-identifiants) | Résultats de scan complet sur toutes les branches |
| [Sécurité : Fork & Clone](#sécurité--fork--clone) | Garanties pour le fork et clone publics |
| [Architecture proxy](#architecture-proxy) | Frontières proxy de conteneur et contrôle d'accès |
| [Opérations limitées au propriétaire](#opérations-limitées-au-propriétaire) | Isolation par espace de noms pour toutes les opérations |
| [Méthodologie d'audit](#méthodologie-daudit) | Comment les audits de sécurité sont réalisés |
| [Niveaux d'accès PAT](#niveaux-daccès-pat) | Niveaux de configuration des jetons et portées |
| [Sécurité du cycle de vie du jeton](#sécurité-du-cycle-de-vie-du-jeton) | Gestion éphémère du jeton de la réception à l'élimination |
| [Principes de conception](#principes-de-conception) | Principes fondamentaux de conception sécuritaire |
| [Publications connexes](#publications-connexes) | Publications parentes et connexes |

---

## Auteurs

**Martin Paquet** — Analyste programmeur sécurité réseau, administrateur de sécurité des réseaux et des systèmes, analyste programmeur et concepteur logiciels embarqués. 30 ans d'expérience en sécurité réseau, systèmes embarqués et télécom. Concepteur du modèle de sécurité limité au propriétaire assurant que Knowledge reste sûr en tant que dépôt public.

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. A réalisé des audits de sécurité complets du dépôt, scannant toutes les branches, l'historique git et le contenu des fichiers pour les identifiants, jetons et données sensibles.

---

## Résumé

Les systèmes de développement assistés par IA qui persistent les connaissances entre sessions et projets font face à une question de sécurité fondamentale : **que se passe-t-il quand le dépôt devient public ?**

**Knowledge** (`packetqc/knowledge`) est conçu dès le départ pour être **sûr publiquement et limité au propriétaire** :

| Protection | Description |
|------------|-------------|
| **Zéro identifiants stockés** | Aucune clé API, jeton, mot de passe, clé SSH ou certificat dans les fichiers ou l'historique git |
| **Accès en écriture limité par proxy** | Les sessions ne peuvent pousser que vers leur branche assignée dans leur dépôt assigné |
| **Opérations limitées à l'espace de noms** | Toutes les URLs référencent l'espace de noms GitHub du propriétaire |
| **Isolation environnementale** | Fichiers de session, références satellites et `far_memory archives/` sont par propriétaire |
| **Livraison via PR** | Aucune écriture directe aux branches partagées |

---

## La question de sécurité

Quand un système de développement assisté par IA persiste les connaissances et que ce système vit dans un dépôt git, le rendre public soulève des préoccupations légitimes :

| Préoccupation | Risque |
|---------|------|
| **Fuite d'identifiants** | Clés API, jetons ou mots de passe commis accidentellement dans l'historique git |
| **Compromission de compte** | URLs de session, jetons OAuth ou en-têtes d'auth exposant l'accès aux comptes |
| **Contamination croisée** | Les opérations d'un forkeur affectant les dépôts ou comptes du propriétaire original |
| **Exposition de données** | Détails de projets privés, IPs internes ou informations personnelles |
| **Escalade de privilèges** | Un forkeur obtenant un accès en écriture aux branches du propriétaire |

Knowledge répond à chacune par **conception architecturale** — pas par nettoyage après coup.

---

## Modèle de menaces

### Ce contre quoi nous protégeons

| Menace | Vecteur d'attaque | Protection |
|--------|--------------|------------|
| **Vol d'identifiants** | Scanner l'historique git pour les jetons | Aucun identifiant stocké — `.gitignore` bloque les patrons sensibles, audit confirme zéro correspondance |
| **Détournement de session** | Extraire les URLs de session Claude des commits | Les URLs de session expirent ; seulement dans les métadonnées de commit, jamais dans le contenu |
| **Prise de contrôle du dépôt** | Forkeur poussant vers les branches du propriétaire | Le proxy limite le push à la branche assignée — cross-repo retourne 403 |
| **Infiltration satellite** | Harvest du forkeur accédant aux dépôts privés | La synchronisation K_GITHUB utilise le HTTPS public uniquement — dépôts privés retournent 403/404 |
| **Exfiltration de données** | Extraction de détails privés de `far_memory archives/` | `far_memory archives/` ne contient que des métadonnées — aucun code source, aucun identifiant |

### Hors portée

| Hors portée | Pourquoi |
|-------------|-----|
| **Compromission du compte GitHub** | Orthogonal au système — utilisez 2FA, mots de passe forts |
| **Vol de clé API Claude** | Les clés API ne sont jamais dans le dépôt — elles résident dans l'environnement local |
| **Modifications malveillantes du fork** | Un forkeur peut modifier son propre fork — cela n'affecte pas l'original |
| **Attaques supply chain** | Aucune dépendance — que du markdown, git et un script Python |

---

## Couches de sécurité

```
Couche 1: .gitignore          — Empêche les fichiers sensibles d'être commis
Couche 2: Zéro-identifiant     — Aucun identifiant nécessaire (HTTPS public, auth proxy)
Couche 3: Portée du proxy      — Push limité à la branche assignée dans le dépôt assigné
Couche 4: Livraison via PR    — Aucune écriture directe aux branches partagées
Couche 5: Espace de noms      — Les URLs référencent l'espace de noms du propriétaire
Couche 6: Isolation            — Données de session, far_memory archives/, sessions/ par propriétaire
Couche 7: Audit continu       — Vérifications sécurité à chaque synchronisation K_GITHUB et K_VALIDATION /normalize
```

### Couche 2 : Architecture zéro-identifiant

Le système n'a jamais besoin d'identifiants car :

| Composant | Pourquoi aucun identifiant nécessaire |
|-----------|--------------------------------------|
| **Opérations git** | Utilisent des URLs HTTPS publiques — pas de clés SSH, pas de jetons dans les URLs |
| **Authentification Claude Code** | Gérée par le proxy — le dépôt ne voit jamais les jetons |
| **Accès API GitHub** | Utilise `gh` CLI qui s'authentifie via la config locale |
| **Aucun service externe** | Pas de clés API, pas de secrets webhook, pas d'identifiants de base de données |

**L'absence d'identifiants est un choix de conception, pas un effort de nettoyage.**

### Couche 3 : Architecture proxy

| Frontière | Application |
|----------|------------|
| **Portée de branche** | Push uniquement vers la branche `claude/<task-id>` assignée |
| **Portée de dépôt** | Push uniquement vers le dépôt courant — cross-repo retourne 403 |
| **Direction** | Les écritures sont proxyées ; les lectures utilisent le HTTPS public |

### Couche 5 : Espace de noms du propriétaire

```
https://github.com/packetqc/knowledge          ← dépôt core
https://github.com/packetqc/<satellite-name>    ← dépôts satellites
```

Un forkeur hérite de ces URLs, mais les écritures échouent car le proxy limite au dépôt du forkeur. **L'espace de noms est la frontière de sécurité** — pas les jetons, pas les clés.

---

## Audit des identifiants

Scan complet à travers toutes les branches :

| Catégorie | Patrons | Résultat |
|----------|----------|--------|
| Jetons GitHub | `ghp_`, `gho_`, `github_pat_` | **Aucun trouvé** |
| Clés Anthropic/OpenAI | `sk-`, `sk-ant-`, `sk-live_` | **Aucun trouvé** |
| Clés AWS | `AKIA`, `ASIA` | **Aucun trouvé** |
| Clés privées | `BEGIN PRIVATE KEY`, `BEGIN RSA` | **Aucun trouvé** |
| Mots de passe | `password=`, `secret=` avec valeurs | **Aucun trouvé** |
| En-têtes d'auth | `Bearer`, `Basic` avec valeurs | **Aucun trouvé** |
| URLs avec identifiants | `://user:pass@host` | **Aucun trouvé** |
| Jetons JWT | `eyJ[A-Za-z0-9_-]+\.eyJ` | **Aucun trouvé** |

**Résultat : zéro identifiant** trouvé dans les fichiers, l'historique git ou sur aucune branche.

---

## Sécurité : Fork & Clone

### Ce qu'un forkeur obtient

| Composant | Ce qu'il reçoit | Impact sécurité |
|-----------|------------------|----------------|
| **Méthodologie** | Persistance de session, protocole, commandes | Intentionnellement public |
| **Publications** | Articles techniques complets | Intentionnellement public |
| **Outillage** | Scripts de capture, générateur de webcards | Intentionnellement public |
| **Profil** | Nom, email, LinkedIn, GitHub | Intentionnellement public |
| **Historique git** | Commits avec URLs de session | URLs expirent ; aucun identifiant |
| **`far_memory archives/`** | Noms de dépôts, versions, statut | Métadonnées uniquement |
| **`sessions/`** | Historique de session, résumés | Métadonnées uniquement |

### Ce qu'un forkeur ne peut pas faire

| Action | Pourquoi c'est bloqué |
|--------|-----------------|
| Pousser vers le dépôt original | Le proxy limite au dépôt du forkeur |
| Accéder aux dépôts privés | Harvest utilise le HTTPS public — 403/404 |
| Compromettre le compte GitHub | Aucun jeton stocké |
| Compromettre le compte Claude | Aucune clé API ; URLs expirent |
| Modifier les satellites | Cross-repo impossible (proxy) |

### Ce qu'un forkeur doit changer

| Étape | Action |
|-------|--------|
| **Remplacer `packetqc` par son nom d'utilisateur GitHub** | Dans CLAUDE.md — redirige la synchronisation K_GITHUB et le démarrage de session vers son espace de noms |
| **Créer ses propres dépôts satellites** | Le système knowledge du forkeur se bootstrap depuis ses propres projets |
| **Mettre à jour les données de profil** | Remplacer les informations de l'auteur par les siennes |

Le reste s'adapte automatiquement. Le système est conçu pour être portable par espace de noms.

---

## Architecture proxy

```
Session Claude Code
    ↓
Proxy (authentification + autorisation)
    ↓ autorisé : push vers claude/<task-id> assignée dans le dépôt courant
    ✗ bloqué : push vers main, autres branches, autres dépôts
    ↓
API GitHub
```

| Règle | Effet |
|------|--------|
| **Restriction de branche** | Seule la branche `claude/<task-id>` assignée peut recevoir des pushs |
| **Restriction de dépôt** | Seul le dépôt de la session courante |
| **Restriction de direction** | Les écritures sont proxyées ; les lectures utilisent le HTTPS public |

---

## Opérations limitées au propriétaire

| Commande | Accès | Portée |
|---------|-----------------|-------|
| démarrage session | `https://github.com/<propriétaire>/knowledge` | Lecture seule, HTTPS public |
| K_GITHUB `sync_github.py` | `https://github.com/<propriétaire>/<projet>` | Lecture seule, HTTPS public |
| K_GITHUB sync (fix) | Branche de tâche locale | Écriture limitée à la branche assignée |
| git commit + push | Branche de tâche → PR vers `main` | Écriture limitée à la branche assignée |
| `normalize` | Fichiers locaux uniquement | Aucun accès réseau |
| `webcard` | Fichiers locaux uniquement | Aucun accès réseau |

---

## Méthodologie d'audit

| Étape | Vérification |
|-------|-------------|
| **Scanner toutes les branches** | `git branch -a` + `git log --all --name-only` |
| **Scanner l'historique pour les identifiants** | Patrons regex pour jetons, clés, mots de passe |
| **Vérifier le `.gitignore`** | `.env`, `.pem`, `.key`, `.p12`, `credentials.*` |
| **Vérifier le contenu** | URLs de session, IPs internes, emails, webhooks |
| **Vérifier la portée du proxy** | Push vers `main` retourne 403, cross-repo retourne 403 |

---

## Principes de conception

| Principe | Description |
|----------|-------------|
| **Les identifiants sont inutiles, pas nettoyés** | L'architecture ne requiert jamais de stocker des identifiants |
| **L'espace de noms est la frontière** | La sécurité vient du confinement au propriétaire |
| **Public par défaut** | Les données privées restent dans l'environnement local |
| **Défense en profondeur** | Sept couches indépendantes |
| **Audit-friendly** | Vérifiable avec les outils git standard |
| **Fork-friendly** | Conçu pour être forké |

---

## Niveaux d'accès PAT

Knowledge définit 4 niveaux progressifs de configuration PAT (Personal Access Token) GitHub. Chaque niveau active des opérations spécifiques et correspond à une couche architecturale découverte :

| Niveau | Configuration PAT | Portée GitHub | Ce qu'il active | Mode opérationnel |
|--------|------------------|-------------|-----------------|-----------------|
| **0** | **Sans PAT** | Proxy seul | Dépôts publics : clone (initial seul), push branche assignée, création PR manuelle | Semi-automatique — l'utilisateur crée les PRs manuellement |
| **1** | **Fine-grained lecture seule** | `Contents: Read` sur dépôts spécifiques | Niveau 0 + clone/fetch dépôts satellites privés pour la synchronisation K_GITHUB et le démarrage de session | Semi-automatique + visibilité privée |
| **2** | **Fine-grained lecture-écriture** | `Contents: Read-Write` + `Pull requests: Read-Write` + `Projects: Read-Write` | Niveau 1 + création/fusion PR et gestion de tableaux GitHub Project via API `api.github.com` | **Autonome complet** — recommandé |
| **3** | **PAT classique `repo`** | Portée `repo` complète | Tout — mais accorde bien plus d'accès que nécessaire | Autonome complet — **non recommandé** |

### Guide de sélection de niveau

| Scénario | Niveau recommandé | Pourquoi |
|----------|------------------|---------|
| Dépôts tous publics, usage occasionnel | **0** | Aucun jeton nécessaire |
| Satellites privés, synchronisation K_GITHUB en lecture seule | **1** | Minimum pour voir les dépôts privés |
| Opération autonome complète (usage quotidien) | **2** | Création/fusion PR via API, limité aux dépôts spécifiques |
| Test rapide, session jetable | **3** | Pratique mais trop large — à éviter en usage régulier |

### Correspondance architecturale

| Niveau | Découverte architecturale |
|--------|--------------------------|
| **Niveau 0** | Réalité du proxy (v17) — le proxy limite le push à la branche assignée |
| **Niveau 1** | Protocole de jeton éphémère (v27) — PAT fine-grained lecture seule pour cloner les dépôts privés |
| **Niveau 2** | Contournement API (v28) — le modèle à deux canaux : git via proxy (restreint), API REST GitHub directe (illimitée avec jeton). Minimum confirmé : `Contents: RW` + `Pull requests: RW` + `Projects: RW` + `Metadata: Read` (obligatoire) — 4 permissions au total |
| **Niveau 3** | PAT classique portée `repo` — inutilement large, viole le moindre privilège |

### Niveau 2 — Permissions minimales confirmées

Validé le 2026-02-21 via cycle autonome complet (création PR #137 + fusion via API) :

| Permission fine-grained | Requise | Ce qu'elle active |
|-------------------------|---------|-------------------|
| **Contents: Read and write** | **OUI** | Cloner les dépôts, opérations de branches via API |
| **Pull requests: Read and write** | **OUI** | Créer PR + fusionner PR via `api.github.com` |
| **Projects: Read and write** | **OUI** | Créer et gérer les tableaux GitHub Project |
| **Metadata: Read-only** | **OUI** (obligatoire) | Auto-incluse par GitHub — ne peut pas être décochée |
| Issues | Non | Non utilisé par le cycle d'autonomie |
| Actions | Non | Non utilisé par le cycle d'autonomie |
| Webhooks | Non | Non utilisé par le cycle d'autonomie |
| Pages | Non | Non utilisé par le cycle d'autonomie |
| Administration | Non | Non nécessaire |

Seulement **4 permissions** requises (3 sélectionnées + 1 obligatoire) pour l'autonomie complète de Knowledge.

### Principe du moindre privilège

Toujours utiliser le niveau le plus bas qui répond aux besoins de la session :

| Pratique | Recommandation |
|----------|---------------|
| **Limiter aux dépôts spécifiques** | Les jetons fine-grained (Niveaux 1-2) se limitent aux dépôts du système |
| **Limiter aux permissions minimales** | Lecture seule (Niveau 1) pour la visibilité K_GITHUB sync, Lecture-écriture (Niveau 2) pour les opérations PR autonomes |
| **Expiration courte** | 7-30 jours recommandés |
| **Usage limité à la session** | Le jeton vit uniquement en mémoire contextuelle, jamais écrit dans un fichier |

---

## Sécurité du cycle de vie du jeton — Réception à élimination

Le jeton éphémère traverse 5 phases. Chaque phase possède des propriétés de sécurité spécifiques alignées sur les standards industriels. **OWASP MCP01:2025** classe la mauvaise gestion des jetons comme le **risque #1** pour les outils de développement IA — notre architecture éphémère par conception répond directement à ce risque.

### Phase 1 — Réception

| Méthode | Canal | Propriété de sécurité |
|--------|-------|-------------------|
| **Coller (recommandé)** | Texte dans le chat | Aucune E/S fichier, aucun fichier temporaire. Le jeton entre directement en mémoire contextuelle |
| **Enveloppe PQC** | Blob chiffré | Chiffré en transit (X25519 ou ML-KEM-1024), déchiffré en session |
| **Téléversement d'image (repli)** | Capture d'écran | Fichier temporaire dans `/tmp/` — supprimé immédiatement après extraction |

**Alignement industriel** : OWASP Secrets Management — canaux de saisie sécurisés, pas de journalisation, pas d'écho. L'enveloppe PQC ajoute le chiffrement en transit NIST SP 800-175B.

### Phase 2 — Persistance en mémoire

| Emplacement | Contenu | Protection | Durée de vie |
|-------------|---------|------------|----------|
| **Fenêtre de contexte Claude** | Chaîne du jeton | Isolation de processus, conteneurisé (pas de swap) | Durée de la session |
| **Variable Python** (chemin PQC) | Chaîne déchiffrée | En clair dans la mémoire du processus | Jusqu'à la sortie de portée |
| **`/dev/shm/`** | Matériel de clé uniquement | Zéro-écrasé sur `destroy()` | Jusqu'à `PQCEnvelope.__exit__()` |

Le jeton **n'est pas chiffré en mémoire** après la réception. Le chiffrement en mémoire sans support matériel (HSM/TPM/SGX) est du théâtre sécuritaire — la clé de déchiffrement coexiste dans la même mémoire de processus.

**Futur** : le projet knowledge-live PQC vise le stockage de clés supporté par matériel (STM32 élément sécurisé). Avec une clé conservée par le matériel, le jeton pourrait être chiffré en RAM avec une protection véritable — la clé n'entre jamais dans la mémoire du processus.

### Phase 3 — Utilisation

| Opération | Exposition | Atténuation |
|-----------|----------|------------|
| `curl -H "Authorization: token <T>"` | `/proc/<pid>/cmdline` | Isolation de conteneur |
| `git clone https://<T>@github.com/...` | Liste de processus | Isolation de conteneur + préférer les en-têtes |
| API REST GitHub via HTTPS | Aucune | Chiffrement TLS 1.3 en transit |

### Phase 4 — Élimination

| Matériel | Méthode d'élimination | Quand |
|----------|----------------|------|
| Fenêtre de contexte | Détruite par le runtime Anthropic | Fin de session |
| Variable Python | Ramassée par le GC (non zéro-écrasée) | Sortie de portée |
| Matériel de clé (`/dev/shm/`) | Zéro-écrasement + unlink | `destroy()` |
| Fichier image | `rm -f` immédiatement | Après extraction |

**Lacune connue** : Les chaînes Python sont immutables — le GC ne zéro-écrase pas la mémoire avant libération (bogue Python #17405, ouvert depuis 2013). Le jeton peut persister dans les pages libérées. **Améliorations prévues** : stocker les jetons en `bytearray` (mutable, zéro-écrasable sur place), ajouter `mlock()` pour empêcher le swap (FIPS 140-3, patron HashiCorp Vault), `prctl(PR_SET_DUMPABLE, 0)` pour empêcher les core dumps, zéro-écrasement explicite avant déréférencement (NIST SP 800-57 §8.3.4).

### Phase 5 — Vérification post-session

Vérifier l'absence de résidu de jeton : aucun fichier ne contient `github_pat_`, aucun historique git ne le contient, aucune variable d'environnement. Le démontage du conteneur détruit toute la mémoire du processus.

### Résumé de conformité

| Standard | Exigence | Statut |
|----------|----------|--------|
| **OWASP Secrets Management** | Pas de journalisation, pas d'écho, persistance minimale | ✅ Conforme |
| **OWASP MCP01:2025** | Empêcher la persistance des jetons dans le contexte/mémoire IA | ✅ Conforme — éphémère par conception |
| **NIST SP 800-63B** §5.1.1 | Authentifiants éphémères non stockés au-delà du besoin | ✅ Conforme |
| **NIST SP 800-57** §8.3.4 | Destruction de clé — zéro-écrasement irréversible | ⚠️ Partiel — clés oui, jeton en attente |
| **NIST SP 800-88** | Assainissement des médias (appliqué à la RAM) | ⚠️ Partiel — clés oui, jeton en attente |
| **FIPS 140-3** | Zéro-écrasement de tous les SSP non protégés | ⚠️ Partiel — `/dev/shm` oui, variables Python en attente |
| **CIS Control 3.10** | Pas de secrets dans le code source | ✅ Conforme |
| **Patron pyATS secret_strings** | Chiffrement au repos pour secrets persistants | N/A — jeton jamais au repos |
| **Chiffrement supporté par matériel** | HSM/TPM pour protection des clés | 🔮 Prévu — projet knowledge-live PQC |

---

## Publications connexes

| # | Publication | Relation |
|---|-------------|-------------|
| 0 | [Knowledge]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parent — le système que cette publication sécurise |
| 3 | [Persistance de session IA]({{ '/fr/publications/ai-session-persistence/' | relative_url }}) | Modèle de sécurité des notes de session |
| 4 | [Connaissances distribuées]({{ '/fr/publications/distributed-minds/' | relative_url }}) | Portée de sécurité de harvest |
| 4a | [Tableau de bord]({{ '/fr/publications/distributed-knowledge-dashboard/' | relative_url }}) | Modèle d'exposition des données |
| 7 | [Protocole Harvest]({{ '/fr/publications/harvest-protocol/' | relative_url }}) | Contrôles d'accès harvest |
| 8 | [Gestion de session]({{ '/fr/publications/session-management/' | relative_url }}) | Contraintes proxy du protocole save |
| 9 | [Rapport de conformité]({{ '/fr/publications/security-by-design/compliance/' | relative_url }}) | Évaluation phase par phase avec suivi du cycle de vie |
| 14 | [Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | Architecture en profondeur — conception multi-module |
| 0v2 | [Knowledge 2.0]({{ '/fr/publications/knowledge-2.0/' | relative_url }}) | Référence architecture multi-module K2.0 |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
*© 2026 Martin Paquet & Claude (Anthropic)*
