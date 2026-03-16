---
layout: publication
title: "Analyse d'architecture de Knowledge — Documentation complete"
description: "Analyse architecturale complete : couches de connaissances, architecture des composants, 13 qualites fondamentales, cycle de vie des sessions, topologie maitre-satellite distribuee, modele de securite, architecture de publication web et niveaux de deploiement production/developpement."
pub_id: "Publication #14 — Complete"
version: "v1"
date: "2026-02-26"
permalink: /fr/publications/architecture-analysis/full/
og_image: /assets/og/knowledge-system-fr-cayman.gif
keywords: "architecture, connaissances, distribue, securite, qualite, session, harvest"
---

# Analyse d'architecture de Knowledge — Documentation complete
{: #pub-title}

**Table des matieres**

| | |
|---|---|
| [Auteurs](#auteurs) | Auteurs de la publication |
| [Resume](#resume) | Vue d'ensemble de l'architecture du systeme |
| [Vue d'ensemble du systeme](#vue-densemble-du-systeme) | Intelligence d'ingenierie IA auto-evolutive |
| [Couches de connaissances](#couches-de-connaissances) | Core, Prouve, Recolte, Session — quatre niveaux de stabilite |
| &nbsp;&nbsp;[Couche Core — CLAUDE.md](#couche-core--claudemd) | Le cerveau — configuration systeme et methodologie |
| &nbsp;&nbsp;[Couche Prouve](#couche-prouve--patterns-lessons-methodology) | Patrons et pieges eprouves |
| &nbsp;&nbsp;[Couche Recolte — minds/](#couche-recolte--minds) | Incubateur de decouvertes satellites |
| &nbsp;&nbsp;[Couche Session — notes/](#couche-session--notes) | Memoire de travail ephemere par session |
| &nbsp;&nbsp;[Modele d'interaction entre couches](#modele-dinteraction-entre-couches) | Transitions du cycle de vie des connaissances |
| [Architecture des composants](#architecture-des-composants) | 13 composants majeurs avec interfaces |
| &nbsp;&nbsp;[CLAUDE.md — Le cerveau](#claudemd--le-cerveau) | Double role : configuration IA et documentation humaine |
| &nbsp;&nbsp;[gh_helper.py — Passerelle API](#scriptsgh_helperpy--passerelle-api-github) | Acces API GitHub contournant le proxy |
| &nbsp;&nbsp;[generate_og_gifs.py — Identite visuelle](#scriptsgenerate_og_gifspy--moteur-didentite-visuelle) | Webcards animees double theme |
| &nbsp;&nbsp;[publications/ — Documents source](#publications--documents-source) | Contenu canonique versionne |
| &nbsp;&nbsp;[docs/ — Publication web](#docs--couche-de-publication-web) | Site bilingue GitHub Pages |
| &nbsp;&nbsp;[minds/ — Intelligence recoltee](#minds--intelligence-recoltee) | Pont entre session et core |
| &nbsp;&nbsp;[live/ — Outillage temps reel](#live--outillage-temps-reel) | Capture, beacon, scanner |
| &nbsp;&nbsp;[projects/ — Registre de projets](#projects--registre-de-projets) | Indexation hierarchique P# |
| [Architecture des qualites](#architecture-des-qualites) | 13 qualites fondamentales |
| &nbsp;&nbsp;[Graphe de dependance des qualites](#graphe-de-dependance-des-qualites) | Comment les qualites se renforcent mutuellement |
| &nbsp;&nbsp;[Mecanismes d'application des qualites](#mecanismes-dapplication-des-qualites) | Commandes qui appliquent chaque qualite |
| [Architecture du cycle de vie des sessions](#architecture-du-cycle-de-vie-des-sessions) | Le mecanisme de persistance |
| &nbsp;&nbsp;[Le protocole Wakeup](#le-protocole-wakeup) | 12 etapes de PNJ a CONSCIENT |
| &nbsp;&nbsp;[Protocole Save](#protocole-save) | Livraison semi-automatique et autonome |
| &nbsp;&nbsp;[Checkpoint et Resume](#checkpoint-et-resume) | Recuperation apres crash avec etat de protocole |
| &nbsp;&nbsp;[Recall](#recall--recuperation-par-branches) | Recuperation de travail basee sur les branches |
| &nbsp;&nbsp;[Perte de contexte et Refresh](#perte-de-contexte-et-refresh) | Recuperation apres compaction |
| [Architecture distribuee](#architecture-distribuee) | Reseau maitre-satellite |
| &nbsp;&nbsp;[Topologie maitre-satellite](#topologie-maitre-satellite) | Etoile avec flux bidirectionnel |
| &nbsp;&nbsp;[Flux Push — Wakeup](#flux-push--wakeup) | Methodologie du core vers les satellites |
| &nbsp;&nbsp;[Flux Pull — Harvest](#flux-pull--harvest) | Insights des satellites vers le core |
| &nbsp;&nbsp;[Mecanisme d'auto-guerison](#mecanisme-dauto-guerison) | Bootstrap, auto-reparation, remediation pull |
| &nbsp;&nbsp;[Suivi de version et derive](#suivi-de-version-et-derive) | Comparaison des versions de connaissances |
| [Architecture de securite](#architecture-de-securite) | Controle d'acces et modele de jetons |
| &nbsp;&nbsp;[Modele proxy](#modele-proxy) | Frontieres du proxy conteneur |
| &nbsp;&nbsp;[Protocole de jetons ephemeres](#protocole-de-jetons-ephemeres) | Cycle de vie PAT zero-stocke-au-repos |
| &nbsp;&nbsp;[Modele a deux canaux](#modele-a-deux-canaux) | Proxy git vs API direct |
| [Architecture web](#architecture-web) | Publication et presentation |
| &nbsp;&nbsp;[Systeme double theme](#systeme-double-theme) | Cayman clair et Midnight sombre |
| &nbsp;&nbsp;[Architecture des layouts](#architecture-des-layouts) | default.html vs publication.html |
| &nbsp;&nbsp;[Pipeline de publication](#pipeline-de-publication) | Source, resume, complet |
| &nbsp;&nbsp;[Systeme miroir bilingue](#systeme-miroir-bilingue) | Concordance EN/FR |
| &nbsp;&nbsp;[Architecture d'exportation](#architecture-dexportation) | Generation PDF et DOCX |
| [Modele de deploiement](#modele-de-deploiement) | Niveaux production/developpement |
| &nbsp;&nbsp;[Cycle de vie des satellites](#cycle-de-vie-des-satellites) | Progression en 4 etapes |
| &nbsp;&nbsp;[Topologie du reseau](#topologie-du-reseau) | Registre de projets actuel |
| [Analyse structurelle — Noyau core](#analyse-structurelle--noyau-core) | Analyse de poids au niveau fichier et fosse d'autorite |
| &nbsp;&nbsp;[Poids du noyau par role](#poids-du-noyau-par-role) | Cerveau, connaissances, intelligence, outils, infrastructure |
| &nbsp;&nbsp;[Decomposition detaillee des composants](#decomposition-detaillee-des-composants) | 11 composants avec tailles et roles |
| &nbsp;&nbsp;[Priorite de lecture pour les instances Claude](#priorite-de-lecture-pour-les-instances-claude) | Table de priorite P0-P10 |
| &nbsp;&nbsp;[Le fosse d'autorite](#le-fosse-dautorite) | Autorite systeme vs conversation |
| [Analyse de la structure Publication](#analyse-de-la-structure-publication) | Anatomie d'une publication |
| &nbsp;&nbsp;[Anatomie d'une publication — Les 9 branches](#anatomie-dune-publication--les-9-branches) | Source, web, front matter, webcards, layout, integration |
| &nbsp;&nbsp;[Cycle de vie d'une publication](#cycle-de-vie-dune-publication) | De pub new a normalize |
| &nbsp;&nbsp;[Commandes de validation](#commandes-de-validation) | Boucle qualite a 5 commandes |
| [Publications connexes](#publications-connexes) | Publications soeurs et parente |

## Auteurs

**Martin Paquet** — Analyste programmeur en securite des reseaux, administrateur de securite des reseaux et des systemes, et concepteur programmeur de logiciels embarques. 30 ans d'experience couvrant les systemes embarques, la securite reseau, les telecoms et le developpement logiciel. Architecte du systeme Knowledge — une intelligence d'ingenierie IA auto-evolutive construite sur des fichiers Markdown simples dans Git.

**Claude** (Anthropic, Opus 4.6) — Partenaire de developpement IA. Co-architecte et executeur principal du systeme Knowledge. Opere au sein de l'architecture decrite ici — chaque session s'amorce depuis ces structures, chaque commande suit ces patrons.

---

## Resume

Le systeme Knowledge (P0) est une intelligence d'ingenierie IA auto-evolutive qui transforme des sessions de codage IA sans etat en un reseau persistant, distribue et auto-reparateur de conscience. Construit entierement sur des fichiers Markdown simples dans des depots Git, il ne necessite aucun service externe, aucune base de donnees et aucune infrastructure cloud. Un seul `git clone` demarre tout.

Cette publication fournit une analyse architecturale complete du systeme : ses quatre couches de connaissances (Core, Prouve, Recolte, Session), ses 13+ composants majeurs, ses 13 qualites fondamentales, son cycle de vie des sessions, sa topologie distribuee maitre-satellite, son modele de securite, son architecture de publication web et ses niveaux de deploiement production/developpement. L'analyse couvre a la fois la conception structurelle et les proprietes emergentes issues de l'interaction de ces composants.

L'architecture est distinctive en ce que le systeme se documente en consommant sa propre production — la publication #0 a ete construite en recoltant ses enfants. Le tableau de bord se met a jour a chaque recolte. Le journal d'evolution grandit a mesure que le systeme grandit. Cette conscience de soi recursive n'est pas un objectif de conception mais une propriete emergente de l'architecture.

**Source** : Session de documentation d'architecture 2026-02-26 depuis knowledge (P0). Ferme [#316](https://github.com/packetqc/knowledge/issues/316).

---

## Audience ciblee

Cette publication est destinee aux equipes de travail impliquees dans l'ecosysteme du systeme Knowledge :

| Audience | Quoi privilegier |
|----------|-----------------|
| **Administrateurs reseau** | Architecture distribuee, modele de securite, frontieres proxy, niveaux de deploiement |
| **Administrateurs systeme** | Modele de deploiement, configuration GitHub Pages, gestion des assets, niveaux production/developpement |
| **Programmeurs et programmeuses** | Architecture des composants, cycle de vie des sessions, couches de connaissances, architecture des qualites, scripts Python |
| **Gestionnaires** | Vue d'ensemble du systeme, qualites fondamentales, niveaux de deploiement, le ratio de productivite 100x documente dans les success stories |

Le document progresse d'une vue d'ensemble de haut niveau vers une analyse technique detaillee. Les gestionnaires et architectes peuvent se concentrer sur les premieres sections (Vue d'ensemble, Couches de connaissances, Architecture des qualites), tandis que les implementeurs trouveront les sections ulterieures (Cycle de vie des sessions, Architecture de securite, Modele de deploiement) les plus actionnables.

## Conventions du document

Cette publication utilise les conventions suivantes :

| Convention | Utilisation |
|------------|-------------|
| **Tableaux** | Donnees structurees, comparaisons, inventaires — format compact (cle-valeur ou multi-colonnes) |
| **Diagrammes Mermaid** | Visualisations d'architecture integrees en ligne — rendues par GitHub et GitHub Pages |
| **Blocs de code** | Chemins de fichiers, exemples de commandes, extraits de configuration |
| **Texte en gras** | Termes cles a la premiere introduction, emphase sur les concepts critiques |
| **References aux qualites** (`#N`) | References croisees aux 13 qualites fondamentales par leur numero (ex. : *Autonome* #2, *Concordant* #3) |
| **References aux publications** (`#N`) | References croisees aux publications soeurs par numero (ex. : Publication #15 pour les diagrammes) |
| **References de version** (`vN`) | Numeros de version d'evolution des connaissances suivant les decouvertes architecturales |
| **Fleches dans le texte** (`→`) | Flux de processus ou transformation (ex. : source → EN/FR → references croisees) |

---

## Vue d'ensemble du systeme

Le systeme Knowledge est une **intelligence d'ingenierie IA auto-evolutive** — un reseau de depots Git, de fichiers Markdown et de scripts Python qui donne aux assistants de codage IA une memoire persistante, une conscience distribuee et des capacites d'auto-guerison. A son coeur, il resout un probleme fondamental : les sessions de codage IA sont sans etat. Sans structure externe, chaque nouvelle session demarre vierge — un PNJ sans memoire d'hier.

L'architecture du systeme peut etre comprise a travers trois prismes :

1. **Comme mecanisme de persistance** : CLAUDE.md + notes/ + le cycle wakeup/save transforment des sessions ephemeres en collaboration continue
2. **Comme reseau distribue** : Un esprit maitre (depot knowledge) pousse la methodologie vers les satellites et recolte les insights en retour, creant un flux d'intelligence bidirectionnel
3. **Comme systeme auto-documentant** : Le systeme enregistre sa propre evolution, publie sa propre documentation et grandit en consommant sa propre production

L'ensemble du systeme fonctionne sur du texte brut. Aucune base de donnees, aucun service cloud, aucune dependance externe au-dela de Git et GitHub. C'est la qualite **autosuffisant** — le systeme se sustente de sa propre structure.

---

## Couches de connaissances

Le systeme organise les connaissances en quatre couches, ordonnees par stabilite et niveau de validation. Chaque couche a un cycle de vie distinct, un emplacement de stockage et un objectif propre.

### Couche Core — CLAUDE.md

**Emplacement** : `CLAUDE.md` (racine de chaque depot)
**Stabilite** : La plus haute — les changements ici se propagent a tout le reseau
**Taille** : 3000+ lignes dans le depot maitre ; ~180 lignes (sous-ensemble critique) dans les satellites

CLAUDE.md est le cerveau du systeme. Dans le depot knowledge maitre, il contient la methodologie complete : identite, cycle de vie des sessions, definitions de commandes, patrons eprouves, pieges connus, journal d'evolution des connaissances, inventaire des publications et le protocole distribue complet. Il est charge comme **instructions de projet au niveau systeme** par Claude Code, lui conferant le plus haut niveau d'autorite — survivant a la compaction du contexte qui elimine les donnees au niveau conversation.

Dans les depots satellites, CLAUDE.md porte un **sous-ensemble critique** (~180 lignes) : un pointeur vers le depot maitre, l'ADN comportemental essentiel (protocole de session, protocole save, protocole de branche, principe du pont humain) et la reference complete des commandes en 7 groupes. Ce sous-ensemble survit a la compaction — le satellite conserve un comportement correct meme quand le contexte conversationnel est perdu.

**Propriete architecturale cle** : CLAUDE.md est a la fois configuration et documentation. Il configure le comportement de Claude Code ET documente l'architecture du systeme pour les lecteurs humains. Ce double role est intentionnel — le systeme est concu pour etre lisible par l'IA et les humains.

### Couche Prouve — patterns/, lessons/, methodology/

**Emplacement** : Repertoires `patterns/`, `lessons/`, `methodology/`
**Stabilite** : Haute — contenu valide sur plusieurs projets
**Contenu** : Patrons eprouves (debogage embarque, integration RTOS, SQLite sur embarque), pieges connus (20 modes de defaillance documentes) et methodologie de processus (bootstrap satellite, gestion de projet, pagination web)

Cette couche represente les **connaissances validees** — des insights prouves corrects sur au moins deux projets. Les patrons decrivent les approches qui fonctionnent. Les lecons decrivent les approches qui ont echoue. La methodologie decrit les processus affines par la pratique.

La couche prouvee est la cible de promotion pour les insights recoltes. Quand un insight de `minds/` est valide sur plusieurs projets, il est promu vers `patterns/` ou `lessons/` via la commande `harvest --promote`.

### Couche Recolte — minds/

**Emplacement** : Repertoire `minds/`
**Stabilite** : Moyenne — plus recente, moins validee que les connaissances prouvees
**Contenu** : Fichiers d'esprit par satellite avec insights extraits, suivi de version, curseurs de branches et candidats a la promotion

Le dossier `minds/` est l'**incubateur** — ou les decouvertes specifiques aux projets murissent avant de devenir des connaissances universelles. Chaque projet satellite a un fichier `minds/<slug-projet>.md` correspondant contenant :

- Patrons et pieges extraits du travail du satellite
- Curseurs de branches (SHA de commit + date) pour le suivi incrementiel
- Statut de derive de version par rapport au core
- Candidats a la promotion marques pour revision

`minds/` se situe entre les connaissances prouvees et la memoire de session. Plus durable que les notes (persiste entre les sessions), moins etabli que les patrons du core (pas encore valide sur plusieurs projets).

### Couche Session — notes/

**Emplacement** : Repertoire `notes/` dans chaque depot
**Stabilite** : La plus basse — donnees ephemeres par session
**Contenu** : Notes de session (`session-AAAA-MM-JJ.md`), fichiers de checkpoint (`checkpoint.json`), caches d'etat de board, donnees de healthcheck

La couche session est la **memoire de travail**. Chaque session ecrit ses conclusions, decisions et prochaines etapes dans `notes/`. La session suivante les lit au wakeup, atteignant une recuperation de contexte en ~30 secondes au lieu de ~15 minutes de re-explication manuelle.

Les notes de session suivent un format structure : Done (ce qui a ete accompli), Remember (directives pour les futures sessions), Next (travail prevu). Le marqueur `remember harvest:` signale les insights pour collecte par le protocole de recolte.

### Modele d'interaction entre couches

Les quatre couches forment un cycle de vie des connaissances :

| Transition | Mecanisme | Declencheur |
|-----------|-----------|-------------|
| Session → Recolte | `harvest <projet>` | Commande explicite |
| Recolte → Prouve | `harvest --promote <N>` | Promotion validee par humain |
| Prouve → Core | Mise a jour manuelle de CLAUDE.md | Cristallisation architecturale |
| Core → Session | `wakeup` (auto au demarrage) | Chaque debut de session |
| Session → Session | Persistance `notes/` | Save → prochain wakeup |

Le cycle est continu : les sessions generent des insights, harvest les collecte, la promotion les valide et le core les absorbe. La session suivante herite du core enrichi. C'est la qualite **recursif** — le systeme grandit en consommant sa propre production.

---

## Architecture des composants

Le systeme Knowledge comprend 13 composants majeurs, chacun avec un role distinct. Ils interagissent via des interfaces bien definies — principalement des fichiers Markdown, des operations git et des scripts Python.

### CLAUDE.md — Le cerveau

**Role** : Configuration systeme, documentation de methodologie, definitions de commandes
**Interfaces** : Lu par Claude Code comme instructions de projet au niveau systeme ; lu par le protocole wakeup ; lu par harvest pour comparaison de version

CLAUDE.md est le fichier le plus volumineux et le plus important du systeme. Dans le depot maitre, il depasse 3000 lignes et contient :

| Section | Contenu | Lignes (~) |
|---------|---------|-----------|
| Identite | Qui est Martin, comment nous travaillons ensemble | ~100 |
| Qualites fondamentales | 13 qualites avec descriptions | ~50 |
| Cycle de vie des sessions | Wakeup, travail, save, checkpoint, resume, recall | ~200 |
| Commandes | 7 groupes, 49+ commandes avec specifications completes | ~1500 |
| Patrons | Patrons eprouves de debogage embarque, RTOS, SQLite | ~50 |
| Pieges | 20 modes de defaillance documentes avec correctifs | ~200 |
| Evolution des connaissances | 48 entrees versionnees documentant les changements du systeme | ~500 |
| Publications | 13+ publications avec liens | ~50 |
| Protocoles | Branche, acces, jeton, deploiement | ~300 |

### scripts/gh_helper.py — Passerelle API GitHub

**Role** : Remplacement Python portable du CLI `gh`
**Technologie** : Python `urllib` pur (aucune dependance externe)
**Propriete cle** : Contourne le proxy conteneur qui bloque `curl` et `gh`

`gh_helper.py` est la passerelle du systeme vers l'API GitHub. Il a ete cree parce que :
1. Le CLI `gh` n'est pas installe dans les conteneurs Claude Code
2. `curl` vers `api.github.com` est bloque par le proxy conteneur (en-tetes d'authentification supprimes)
3. Python `urllib` ouvre des connexions socket directes, contournant entierement le proxy

Il couvre : les operations PR (creer, lister, voir, fusionner, assurer), GitHub Projects v2 (creer un board, lier un depot, lister les items, synchroniser, champs, ajout/mise a jour d'items), les labels TAG (configuration, deploiement par lot) et la gestion des issues (creer avec labels). Il lit `GH_TOKEN` depuis `os.environ` en interne — le jeton n'apparait jamais sur aucune ligne de commande.

### scripts/generate_og_gifs.py — Moteur d'identite visuelle

**Role** : Generer des GIF animes d'apercu social OG pour toutes les pages web
**Technologie** : PIL/Pillow, Python
**Sortie** : 40+ GIF animes (1200x630, 256 couleurs, double theme)

Le generateur de webcards cree des images d'apercu social animees uniques pour chaque page web. Six types d'animation (corporate, diagramme, panneau divise, cartoon, index) avec mouvement specifique au contenu. Double theme : Cayman (clair) et Midnight (sombre). Pilote par les donnees — la webcard du tableau de bord lit le statut reel des satellites depuis le README source.

### publications/ — Documents source

**Role** : Source canonique de toutes les publications
**Structure** : `publications/<slug>/v1/README.md` par publication
**Propriete cle** : Source de verite — les pages web (`docs/`) en derivent

Chaque publication existe sous forme de document Markdown versionne. Le repertoire `v1/` permet de futures montees de version sans perte d'historique. Les sous-repertoires d'assets et de media (`assets/`, `media/`) contiennent les ressources specifiques a la publication.

### docs/ — Couche de publication web

**Role** : Site web GitHub Pages servant tout le contenu web
**Technologie** : Jekyll avec layouts personnalises, aucune dependance de theme distant
**Structure** : Bilingue (EN a la racine, FR a `/fr/`), publications a trois niveaux (resume, complet, source)

Le dossier `docs/` est la vitrine publique du systeme. Il contient :
- Pages d'accueil (EN + FR)
- Pages de profil (hub, CV, complet — EN + FR)
- Publications (resume + complet pour chacune — EN + FR)
- Pages hub de projets (EN + FR)
- Assets (webcards, apercu social, CSS, JS)

### minds/ — Intelligence recoltee

**Role** : Incubateur d'insights decouverts par les satellites
**Structure** : Un fichier `<slug-projet>.md` par satellite avec donnees d'insights structurees
**Propriete cle** : Pont entre les donnees ephemeres au niveau session et les connaissances permanentes au niveau core

### live/ — Outillage temps reel

**Role** : Outils de capture en direct et de communication inter-instances
**Contenu** : `stream_capture.py` (capture OBS/RTSP), `knowledge_beacon.py` (decouverte de pairs sur port 21337), `knowledge_scanner.py` (sondage de sous-reseau)
**Propriete cle** : Synchronise vers chaque satellite comme asset de connaissances

### projects/ — Registre de projets

**Role** : Registre central de tous les projets avec indexation hierarchique P#
**Structure** : Fichiers de metadonnees plats `<slug>.md` (jamais de sous-dossiers)
**Contenu** : Identite du projet, type (core/enfant/gere), statut, depots associes, liens de board

---

## Architecture des qualites

### Les 13 qualites fondamentales

Le systeme Knowledge incarne 13 qualites — chacune decouverte par la pratique, chacune renforcant les autres. Elles sont nommees en francais (le systeme a ete concu en francais) et forment une hierarchie de dependance.

| # | Qualite | Essence | Mecanisme |
|---|---------|---------|-----------|
| 1 | **Autosuffisant** | Aucun service externe, aucune base de donnees, aucun cloud. Markdown simple dans Git. | CLAUDE.md + notes/ + patterns/ + lessons/ — tout en texte brut dans un depot |
| 2 | **Autonome** | Auto-propagation, auto-guerison, auto-documentation. | Wakeup etape 0, normalize --fix, harvest --fix, scaffold bootstrap |
| 3 | **Concordant** | Integrite structurelle activement appliquee. | normalize, pub check, docs check — detecter et reparer les ecarts |
| 4 | **Concis** | Sous-ensemble critique, pas des copies. Signal maximum, bruit minimum. | Principe du sous-ensemble critique, couches de connaissances |
| 5 | **Interactif** | Operable, pas seulement lisible. Clic-pour-copier sur le tableau de bord. | JS du tableau de bord, harvest --review/--stage/--promote |
| 6 | **Evolutif** | Le systeme grandit en travaillant. 48 versions en 10 jours. | Table d'Evolution des connaissances, pipeline de promotion |
| 7 | **Distribue** | L'intelligence circule dans les deux sens. Push et harvest. | wakeup (push), harvest (pull), minds/ (incubateur) |
| 8 | **Persistant** | Les sessions sont ephemeres, les connaissances sont permanentes. | notes/ + protocole save, checkpoint/resume |
| 9 | **Recursif** | Le systeme se documente en consommant sa propre production. | harvest alimente minds/, minds/ alimente les publications, les publications alimentent le core |
| 10 | **Securitaire** | Securite par architecture, pas par obscurite. | Delimitation par proxy, regles .gitignore, URLs espace de noms proprietaire |
| 11 | **Resilient** | Chaque mode de defaillance a un chemin de recuperation correspondant. | resume, recall, refresh, echelle de recuperation |
| 12 | **Structure** | Organise autour des projets, pas seulement des publications. | Metadonnees projects/, indexation P#/S#/D#, badges de lien double origine |
| 13 | **Integre** | S'etend aux plateformes externes. | gh_helper.py, GitHub Projects v2, convention TAG:, sync_roadmap.py |

### Graphe de dependance des qualites

**Ordre de lecture** : Autosuffisant active tout — si le systeme depend de services externes, rien d'autre ne fonctionne. Autonome et concordant le maintiennent. Concis le garde gerable. Interactif et evolutif le rendent utilisable et vivant. Distribue le fait monter en echelle. Persistant l'ancre. Recursif le rend auto-conscient. Securitaire le rend publiable. Resilient le rend survivable. Structure l'organise autour des projets. Integre l'etend aux plateformes externes.

Les qualites forment un reseau de renforcement :

- **Autosuffisant** active **distribue** (aucune dependance externe a propager)
- **Autonome** active **resilient** (l'auto-guerison inclut la recuperation apres crash)
- **Concordant** active **structure** (integrite structurelle a travers les projets)
- **Persistant** active **evolutif** (les connaissances s'accumulent entre les sessions)
- **Recursif** active **autosuffisant** (le systeme construit sa propre documentation)

### Mecanismes d'application des qualites

Chaque qualite est appliquee par des commandes et protocoles specifiques :

| Qualite | Mecanisme d'application |
|---------|------------------------|
| Autosuffisant | Aucune dependance externe dans aucun composant ; outillage Python pur |
| Autonome | `wakeup` auto au demarrage ; `normalize --fix` auto-guerit ; bootstrap auto-cree |
| Concordant | `normalize` audite la structure ; `pub check` valide les publications |
| Concis | Template sous-ensemble critique (~180 lignes vs 3000+ dans le core) |
| Interactif | JS clic-pour-copier sur le tableau de bord ; workflow de promotion via la page web |
| Evolutif | Table d'Evolution des connaissances avec 48 entrees versionnees |
| Distribue | Protocole `harvest` avec curseurs de branches ; `wakeup` etape 0 |
| Persistant | `notes/` + protocole `save` ; `checkpoint.json` |
| Recursif | `harvest` alimente `minds/`, `minds/` alimente les publications, les publications alimentent le core |
| Securitaire | Delimitation par proxy ; jetons ephemeres ; blocs `.gitignore` ; espace de noms proprietaire |
| Resilient | `resume` (checkpoint), `recover` (branches), `recall` (memoire profonde), `refresh` (compaction), `wakeup` (profond) |
| Structure | Registre `projects/` ; indexation P# ; liens double origine |
| Integre | `gh_helper.py` ; GitHub Projects v2 ; convention TAG: ; `sync_roadmap.py` |

---

## Architecture du cycle de vie des sessions

Chaque session IA suit le meme cycle de vie. C'est le mecanisme de persistance qui transforme des PNJ sans etat en collaborateurs continus.

```
[auto-wakeup] → verifier checkpoint → lire notes/ → resumer l'etat → travailler → [auto-checkpoint] → save → commit & push
```

### Le protocole Wakeup

Wakeup est le « moment des lunettes » — la transition de PNJ a CONSCIENT. Il s'execute automatiquement a chaque debut de session.

**12 etapes** (0 a 11) :

| Etape | Action | Objectif |
|-------|--------|---------|
| 0 | Cloner `packetqc/knowledge` | Mettre les lunettes — lire le cerveau |
| 0.3 | Detecter/acquerir GH_TOKEN | Elevation pour le mode autonome |
| 0.5 | Scaffold bootstrap | Creer les fichiers essentiels manquants sur les depots vierges |
| 0.55 | Auto-guerir le CLAUDE.md satellite | Remediation automatique de derive |
| 0.56 | Fusionner le PR d'auto-guerison | Activation des commandes dans la meme session |
| 0.6 | Beacon de connaissances (desactive) | Disponible pour demarrage manuel |
| 0.7 | Synchroniser l'amont | Fetch et merge de la branche par defaut |
| 0.8 | Relire les connaissances | Synchronisation mi-session pour mises a jour concurrentes |
| 0.9 | Detection de reprise | Verifier `notes/checkpoint.json` |
| 1-8 | Lire l'etat | Evolution, minds/, notes/, plans, assets, git log, branches |
| 9 | Afficher l'aide | Intelligence + table complete des commandes |
| 10 | Invite harvest | Depot core uniquement, sur accord |
| 11 | Traiter le message de l'utilisateur | Commencer a travailler |

**Adaptation** : Wakeup s'adapte a l'environnement. En mode plan (Bash bloque), il bascule l'etape 0 de `git clone` vers WebFetch. Dans les satellites, il ajoute les etapes de bootstrap et d'auto-guerison. Le protocole a la meme structure partout, mais l'implementation s'adapte.

### Protocole Save

La commande save persiste le travail et le livre a la branche par defaut. Elle s'adapte a l'etat d'elevation de la session :

| Mode | Jeton | Flux | Action utilisateur |
|------|-------|------|--------------------|
| Autonome complet | PAT classique | Creation PR + fusion via API + sync | Aucune |
| Semi-automatique | Aucun | Creation PR + bloc pause | Fusionner le PR (un clic) |

**Protocole (6 etapes)** : Ecrire les notes → commit → push → detecter la branche par defaut → creer le PR → fusionner (eleve) ou l'utilisateur fusionne (semi-auto).

Le PR est le pont entre la branche de tache autorisee par le proxy et le point de convergence (branche par defaut). Sans la fusion, le travail est echoue.

### Checkpoint et Resume

Les protocoles multi-etapes (save, harvest, normalize, bootstrap) ecrivent des checkpoints aux limites d'etapes dans `notes/checkpoint.json`. Si une session plante en cours de protocole, la session suivante detecte le checkpoint a l'etape wakeup 0.9 et propose la reprise.

La commande resume redemarre depuis la derniere etape completee — aucune re-explication manuelle necessaire. Les checkpoints sont auto-supprimes a la fin reussie. Les checkpoints de plus de 24 heures sont marques comme perimes ; ceux de plus de 7 jours sont auto-supprimes.

### Recover — Recuperation par branches

Quand une session plante sans ecrire de checkpoint, `recover` recherche dans les branches `claude/*` le travail committe qui n'a jamais ete fusionne :

1. Enumerer toutes les branches `claude/*` triees par date
2. Filtrer les branches avec des commits non fusionnes
3. Proposer une recuperation par cherry-pick ou diff-apply
4. Appliquer la methode choisie a la branche courante

`recover` capture les crashs au niveau git, complementant `resume` qui les capture au niveau protocole.

### Perte de contexte et Refresh

Quand le contexte est compacte en cours de session, `refresh` restaure le contexte CLAUDE.md sans la charge d'un wakeup complet :

| Commande | Cas d'usage | Vitesse |
|----------|-------------|---------|
| `refresh` | Apres compaction — mise en forme perdue | ~5s |
| `wakeup` | Apres fusion de PRs par d'autres sessions | ~30-60s |
| `resume` | Apres crash avec checkpoint | ~10s |
| `recover` | Apres crash sans checkpoint | ~15s |
| `recall` | Recherche de memoire profonde | ~10s |

L'echelle de recuperation — du plus leger au plus lourd : rafraichir le navigateur → PR manuel → `resume` → `recover` → `recall` → `refresh` → `wakeup` → nouvelle session.

---

## Architecture distribuee

### Topologie maitre-satellite

Le systeme Knowledge opere comme un reseau en etoile avec flux d'intelligence bidirectionnel :

**Esprit maitre** (P0 — `packetqc/knowledge`) : Contient le CLAUDE.md canonique, toutes les connaissances prouvees, les minds/ recoltes, la bibliotheque complete de publications et la presence web. C'est le niveau PRODUCTION du reseau.

**Projets satellites** (P1-P9) : Chaque satellite a son propre CLAUDE.md (sous-ensemble critique), ses propres notes/, son propre outillage `live/` et potentiellement ses propres GitHub Pages et publications. Les satellites sont simultanement :
- **Developpement** par rapport au core — terrain d'essai pour de nouvelles capacites
- **Production** a leur propre niveau de depot — faisant autorite de maniere independante pour leur domaine

### Flux Push — Wakeup

A chaque debut de session dans un satellite, le protocole wakeup lit le CLAUDE.md de `packetqc/knowledge` en premier (etape 0). Cela pousse la derniere methodologie, les commandes, les patrons et les protocoles vers le satellite. Le satellite recoit aussi :

- Les assets de connaissances (outillage `live/`, helpers `scripts/`)
- Le scaffold bootstrap (fichiers essentiels pour les depots vierges)
- Les mises a jour d'auto-guerison (section commandes rafraichie a la derniere version du core)

Le push est **base sur la lecture, pas sur l'ecriture** — le satellite lit depuis le core, le core ne pousse pas vers les satellites. Cela fonctionne car tout l'acces utilise des URLs HTTPS publiques.

### Flux Pull — Harvest

La commande `harvest` tire les connaissances evoluees des satellites vers le centre :

1. **Enumerer les branches** — `git ls-remote` pour lister toutes les branches distantes
2. **Verifier les curseurs** — Comparer les HEAD de branches aux SHA derniers recoltes
3. **Scanner le nouveau contenu** — Lire CLAUDE.md, notes/, publications/, drapeaux harvest
4. **Extraire les insights** — Patrons, pieges, ameliorations methodologiques
5. **Mettre a jour minds/** — Ecrire dans `minds/<slug-projet>.md` avec les curseurs
6. **Mettre a jour le tableau de bord** — Rafraichir les 5 fichiers du tableau de bord (source + resume/complet EN/FR)
7. **Regenerer les webcards** — La webcard du tableau de bord pilotee par les donnees reflete le nouveau statut
8. **Nettoyer** — Supprimer les clones temporaires de `/tmp/`

Le harvest est **incrementiel** — les curseurs de branches tracent le dernier commit traite. Seul le nouveau contenu est scanne lors des executions suivantes.

### Mecanisme d'auto-guerison

Les satellites s'auto-guerissent via trois mecanismes :

1. **Scaffold bootstrap** (wakeup etape 0.5) : Cree les fichiers essentiels manquants sur les depots vierges
2. **Auto-guerison du CLAUDE.md** (wakeup etape 0.55) : Detecte la derive de version, met a jour la section commandes depuis le template du core
3. **Remediation basee sur le pull** : Au prochain wakeup, le satellite lit le core mis a jour — tout correctif applique au core se propage automatiquement

L'auto-guerison est consciente de la version : les tags `<!-- knowledge-version: vN -->` tracent la version du core avec laquelle chaque satellite s'est synchronise.

### Suivi de version et derive

Chaque entree d'evolution porte un numero de version (v1 a v48 au moment de cette redaction). La derive est l'ecart entre la derniere version synchronisee du satellite et la version actuelle du core :

| Derive | Severite | Icone tableau de bord |
|--------|----------|----------------------|
| 0 | A jour | 🟢 |
| 1-3 | Mineure | 🟡 |
| 4-7 | Moderee | 🟠 |
| 8+ | Critique | 🔴 |

`harvest --fix <projet>` prepare la remediation pour les satellites avec une derive significative.

---

## Architecture de securite

### Modele proxy

Les sessions Claude Code s'executent derriere un proxy conteneur qui applique des frontieres d'acces strictes :

| Operation | Comportement |
|-----------|-------------|
| `git clone` (depots publics) | Autorise — lecture seule initiale |
| `git fetch` (apres clone, cross-repo) | Bloque — « No such device or address » |
| `git push` (branche de tache assignee) | Autorise — autorise par le proxy |
| `git push` (toute autre branche) | Bloque — HTTP 403 |
| `curl` vers `api.github.com` | Bloque — le proxy supprime les en-tetes d'authentification |
| Python `urllib` vers `api.github.com` | Autorise — contourne le proxy |

### Protocole de jetons ephemeres

Quand un acces API autonome est necessaire, le systeme utilise des PAT GitHub classiques avec les portees `repo` + `project`. Les jetons sont **ephemeres par conception** :

| Propriete | Implementation |
|-----------|---------------|
| Livraison | Variable d'env `GH_TOKEN` (pre-session) ou `/tmp/.gh_token` (lu+supprime) |
| Stockage | Variable d'environnement uniquement — meurt avec la session/le conteneur |
| Visibilite | Jamais affiche dans l'UI de session, jamais ecrit dans les fichiers |
| Persistance | Aucune — zero-stocke-au-repos |
| Utilisation | Via `gh_helper.py` Python `urllib` — jeton jamais sur la ligne de commande |

**Contrainte critique** (decouverte v45) : le champ texte « Autre » de `AskUserQuestion` n'est PAS invisible — la valeur EST affichee dans le chat de session. La livraison de jeton se fait exclusivement via variable d'environnement ou fichier temporaire.

### Modele a deux canaux

Le systeme opere a travers deux canaux paralleles :

| Canal | Protocole | Restriction | Utilise pour |
|-------|----------|-------------|--------------|
| Proxy Git | HTTPS via proxy conteneur | Par depot, par branche | Clone, fetch, push (branche de tache uniquement) |
| API direct | Python `urllib` vers `api.github.com` | Authentifie par jeton, sans restriction | Creation/fusion PR, Projects v2, gestion des issues |

**Sans jeton** : Lecture seule cross-repo + push vers la branche assignee uniquement.
**Avec jeton via `gh_helper.py`** : Operations API cross-repo completes sur tout depot auquel le jeton a acces.

---

## Architecture web

### Systeme double theme

Toutes les pages web supportent deux themes visuels :

| Theme | Declencheur | Arriere-plan | Texte | Accents |
|-------|-------------|--------------|-------|---------|
| **Cayman** (clair) | `prefers-color-scheme: light` | Degrade sarcelle/emeraude (#ecfdf5 → #ccfbf1) | Ardoise sombre (#0f172a) | Sarcelle, Cyan, Emeraude |
| **Midnight** (sombre) | `prefers-color-scheme: dark` | Degrade marine/indigo (#0f172a → #1e1b4b) | Ardoise claire (#e2e8f0) | Bleu, Violet, Cyan |

La detection de theme utilise des elements `<picture>` avec des requetes `media` pour les en-tetes webcard, et le CSS `@media (prefers-color-scheme: dark)` pour le style des pages. Le partage social (`og:image`) utilise toujours la variante Cayman (claire).

### Architecture des layouts

Deux layouts gerent toutes les pages web :

| Layout | Portee | Fonctionnalites |
|--------|--------|-----------------|
| `default.html` | Pages de profil, pages d'accueil, hubs | CSS Cayman/Midnight, tags OG, rendu mermaid |
| `publication.html` | Toutes les pages de publication | Tout default + banniere de version, mots-cles, refs croisees, barre d'export, barre de langue, CSS Paged Media |

Le layout `publication.html` ajoute :
- **Banniere de version** : ID de publication, version, date, horodatage de generation, auteurs — auto-rendu depuis le front matter
- **Barre de langue** : Auto-generee depuis le permalink via Liquid — les pages EN montrent le lien francais, les pages FR montrent le lien anglais
- **Barre d'export** : Boutons PDF (Letter/Legal) et DOCX
- **CSS Paged Media** : Regles `@page` pour en-tetes courants, pieds de page, page de couverture, saut de page TDM intelligent

### Pipeline de publication

Chaque publication suit un pipeline a trois niveaux :

```
publications/<slug>/v1/README.md           ← Source de verite (EN)
    ↓ (pub sync)
docs/publications/<slug>/index.md          ← Resume EN (web)
docs/publications/<slug>/full/index.md     ← Complet EN (web)
    ↓ (traduction)
docs/fr/publications/<slug>/index.md       ← Resume FR (web)
docs/fr/publications/<slug>/full/index.md  ← Complet FR (web)
```

### Systeme miroir bilingue

Chaque page web existe en anglais et en francais. La commande `normalize` applique cette structure miroir. Les barres de langue dans le layout `publication.html` generent automatiquement les liens entre les miroirs.

### Architecture d'exportation

Les publications peuvent etre exportees en PDF et DOCX :

| Mode | Mecanisme | Dependances |
|------|-----------|-------------|
| **Web** (cote client) | `window.print()` + CSS Paged Media | Aucune — le navigateur EST le moteur PDF |
| **CLI** (console) | `pub export #N --pdf` via pandoc | Necessite pandoc |

Le mode web utilise : la fonction `printAs()` avec selection Letter/Legal, en-tete courant (boite unique `@top-left`), pied de page trois colonnes, page de couverture, saut de page TDM intelligent et assainissement du nom de fichier PDF.

---

## Modele de deploiement

### Cycle de vie des satellites

Un satellite progresse a travers 4 etapes :

| Etape | Action | Resultat |
|-------|--------|---------|
| 1. Bootstrap | `wakeup` sur depot vierge | CLAUDE.md, README, LICENSE, .gitignore, notes/ |
| 2. Normalize | `normalize --fix` | Concordance structurelle verifiee |
| 3. Healthcheck | `harvest --healthcheck` | Tableau de bord mis a jour, statut suivi |
| 4. Presence web | `project create` | Scaffold docs/ complet, GitHub Pages, hub publications |

### Topologie du reseau

Le reseau actuel :

| ID | Projet | Type | Statut | Role |
|----|--------|------|--------|------|
| P0 | Knowledge System | core | actif | Esprit maitre — canonique a l'echelle du systeme |
| P1 | MPLIB | enfant | actif | Bibliotheque embarquee — preuve de concept originale |
| P2 | STM32 PoC | enfant | actif | Preuve de concept materiel |
| P3 | knowledge-live | enfant | actif | Developpement d'outillage live |
| P4 | MPLIB Dev Staging | enfant (de P1) | actif | Staging de developpement pour MPLIB |
| P5 | PQC | enfant | pre-bootstrap | Projet de cryptographie post-quantique |
| P6 | Export Documentation | gere (dans P3) | actif | Documentation des fonctionnalites d'export |
| P8 | Documentation System | gere (dans P0) | actif | Methodologie de gestion documentaire |
| P9 | Knowledge Compliancy Report | gere (dans P0) | actif | Suivi de conformite securitaire |

Le cycle de vie : idee → test satellite (dev) → pages satellite (production-depot) → harvest vers core → promouvoir → pages core (production-systeme) → tous les satellites heritent au prochain wakeup.

---

## Analyse structurelle — Noyau core

Le systeme Knowledge tient dans moins de 1 Mo de Markdown et Python. Cette section fournit une analyse de poids au niveau fichier, la priorite de lecture, et la decouverte du fosse d'autorite qui gouverne l'architecture du sous-ensemble critique.

### Poids du noyau par role

| Role | Composants | Poids | Proportion |
|------|-----------|-------|------------|
| **Cerveau** | CLAUDE.md | 293 Ko | 31% |
| **Connaissances** | methodology + patterns + lessons | 218 Ko | 23% |
| **Intelligence** | minds + projects | 121 Ko | 13% |
| **Outils** | scripts | 242 Ko | 26% |
| **Infrastructure** | live | 53 Ko | 6% |
| **Ephemere** | docs + notes + publications | Variable | — |
| **Total noyau** | **~930 Ko** | **100%** | |

### Decomposition detaillee des composants

| Composant | Fichiers | Taille | Role |
|-----------|----------|--------|------|
| `CLAUDE.md` | 1 fichier | 293 Ko (3218 lignes) | Le cerveau — identite, methodologie, 49 commandes, 48 evolutions, 20 pieges, protocole proxy/branches |
| `methodology/` | 15 fichiers | 194 Ko | Plans d'implementation — satellite-bootstrap (34 Ko), web-pagination-export (31 Ko), project-management (36 Ko), project-create (17 Ko), checkpoint-resume (11 Ko), satellite-commands (8 Ko), 9 autres (57 Ko) |
| `patterns/` | 4 fichiers | 14 Ko | Approches eprouvees — embedded-debugging, rtos-integration, sqlite-embedded, ui-backend-separation |
| `lessons/` | 2 fichiers | 10 Ko | Erreurs a eviter — pitfalls (20 entrees), performance insights |
| `minds/` | 7 fichiers | 71 Ko | Intelligence satellite recoltee — knowledge-live (22 Ko), stm32n6570-dk-sqlite (15 Ko), mplib-dev-staging (10 Ko), mplib (6 Ko), pqc (5 Ko) |
| `projects/` | 10 fichiers | 50 Ko | Registre d'entites P0-P9 avec metadonnees d'indexation hierarchique |
| `scripts/` | 7 scripts | 242 Ko | Outils deployes — gh_helper (57 Ko), generate_og_gifs (90 Ko), pqc_envelope (23 Ko), 4 autres (72 Ko) |
| `live/` | 5 fichiers | 53 Ko | Infrastructure temps reel — stream_capture (26 Ko), knowledge_beacon (12 Ko), knowledge_scanner (8 Ko) |
| `publications/` | 15 sources | Variable | Contenu canonique des publications — versionne, source de verite pour les pages web |
| `docs/` | 100+ pages | Variable | Presence web — 2 layouts HTML, bilingue EN/FR, 40 webcards GIF animees |
| `notes/` | ~20 fichiers | 80 Ko | Memoire de session ephemere — checkpoint.json, healthcheck.json, board-state.json |

### Priorite de lecture pour les instances Claude

| Priorite | Dossier / Fichier | Taille | Autorite | Survit a la compaction ? | Role |
|----------|-------------------|--------|----------|--------------------------|------|
| **P0** | `CLAUDE.md` | 293 Ko | Systeme (instructions projet) | Oui | **Le noyau** — identite, methodologie, commandes, evolution, pieges |
| **P1** | `methodology/` | 194 Ko | Conversation (lu au wakeup) | Non | Plans d'implementation — bootstrap, checkpoint, projets, export |
| **P2** | `patterns/` | 14 Ko | Conversation | Non | Savoir eprouve — debugging embarque, RTOS, SQLite, UI/backend |
| **P3** | `lessons/` | 10 Ko | Conversation | Non | Erreurs a eviter — 20 pieges documentes |
| **P4** | `minds/` | 71 Ko | Conversation | Non | Intelligence recoltee des satellites — plus recent, moins valide |
| **P5** | `notes/` | 80 Ko (3 derniers) | Conversation | Non | Memoire ephemere — contexte session precedente |
| **P6** | `projects/` | 50 Ko | Conversation | Non | Registre d'entites P0-P9 avec metadonnees |
| **P7** | `scripts/` | 242 Ko | Executable | N/A | Outils deployes — non lus, executes (gh_helper, webcards, beacon) |
| **P8** | `publications/` | Variable | Conversation | Non | Source pour 15 publications — lu a la demande, pas au wakeup |
| **P9** | `docs/` | 100+ pages | Web | N/A | Presence web — GitHub Pages, pas lu par Claude |
| **P10** | `live/` | 53 Ko | Executable | N/A | Infrastructure live — beacon, scanner, capture |

### Le fosse d'autorite

La decouverte architecturale la plus critique : CLAUDE.md (293 Ko) a l'**autorite systeme** — il survit a la compaction de contexte car il est charge comme « instructions projet » par la plateforme Claude Code. Tout le reste (~640 Ko de methodology, patterns, lessons, minds, projects) a l'**autorite conversation** — lu au wakeup etape 0, mais perdu a la premiere compaction.

Ce fosse d'autorite est la raison d'etre du principe du **sous-ensemble critique** (v31). Le CLAUDE.md satellite (~180 lignes) porte assez d'ADN comportemental (protocole de session, protocole save, protocole de branches, 49 commandes) pour survivre post-compaction. Sans lui, une session satellite compactee perd toute conscience et retourne au comportement NPC.

L'ordre de lecture (`CLAUDE.md → methodology/ → patterns/ → lessons/ → minds/`) reflete une autorite decroissante et une recence croissante. Le cerveau est stable et autoritaire ; les minds recoltes sont frais mais non valides.

---

## Analyse de la structure Publication

Chaque publication dans le systeme Knowledge suit une structure rigoureuse a 9 branches. Cette section documente l'anatomie d'une publication — ses composants, son cycle de vie et ses points d'integration.

### Anatomie d'une publication — Les 9 branches

| Branche | Role | Fichiers |
|---------|------|----------|
| **Source** | Verite canonique, versionnee | `publications/<slug>/v1/README.md` + `assets/` + `media/` |
| **Pages web EN** | Presence web anglaise, 2 niveaux | Resume (`index.md`) + Complet (`full/index.md`) |
| **Pages web FR** | Miroir francais | Meme structure sous `docs/fr/` |
| **Front matter** | Metadonnees Jekyll | 8 champs requis par page (layout, title, description, pub_id, version, date, permalink, og_image) |
| **Webcards OG** | Apercu social anime | 4 GIFs par publication (2 langues × 2 themes) |
| **Layout** | Moteur de rendu | Banniere version, barre langue, barre export, CSS Paged Media, mots-cles references croisees |
| **Integration systeme** | Points de connexion | Index publications (EN/FR), 6 pages profil, table CLAUDE.md, tableau de bord #4a |
| **Identifiants** | Systeme de nommage | #N, slug URL-friendly, 3 niveaux, double-origine (core/satellite), inter-projet (→P#) |
| **Validation** | Controle qualite | `pub check`, `pub sync`, `doc review`, `docs check`, `normalize` |

### Cycle de vie d'une publication

```
pub new → Source creee → Pages EN/FR scaffoldees → Webcards generees
    → Contenu ecrit dans Source
    → pub sync → Pages web mises a jour
    → doc review → Fraicheur verifiee
    → pub check → Structure validee
    → normalize → Concordance globale
```

### Commandes de validation

| Commande | Focus | Modifie des fichiers ? |
|----------|-------|------------------------|
| `pub check` | Structure — front matter, liens, miroirs, assets | Non (rapport seulement) |
| `pub sync` | Sync — concordance source→docs, copie assets | Assets seulement |
| `doc review` | Fraicheur du contenu — etat connaissances vs contenu publication | Avec `--apply` |
| `docs check` | Validation de page — integrite page doc individuelle | Non (rapport seulement) |
| `normalize` | Concordance globale — miroirs EN/FR, liens, assets | Avec `--fix` |

Ensemble, ces 5 commandes forment une boucle qualite complete : la structure est correcte (`pub check`), source et docs concordent (`pub sync`), le contenu reflete les connaissances actuelles (`doc review`), les pages sont individuellement valides (`docs check`), et la structure globale est concordante (`normalize`).

**Source** : [Issue #317](https://github.com/packetqc/knowledge/issues/317), [Issue #318](https://github.com/packetqc/knowledge/issues/318) — Sessions d'exploration architecturale.

---

## Publications connexes

| # | Publication | Relation |
|---|-------------|----------|
| 0 | [Systeme de connaissances]({{ '/fr/publications/knowledge-system/' | relative_url }}) | Parente — la publication maitre documentant le systeme |
| 3 | [Persistance de session IA]({{ '/fr/publications/ai-session-persistence/' | relative_url }}) | Fondation — la methodologie qui a tout demarre |
| 4 | [Connaissances distribuees]({{ '/fr/publications/distributed-minds/' | relative_url }}) | Architecture — le flux d'intelligence distribuee |
| 9 | [Securite par conception]({{ '/fr/publications/security-by-design/' | relative_url }}) | Securite — le controle d'acces et le modele de jetons |
| 12 | [Gestion de projet]({{ '/fr/publications/project-management/' | relative_url }}) | Structure — modele d'entite projet et cycle de vie |

---

*Auteurs : Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Connaissances : [packetqc/knowledge](https://github.com/packetqc/knowledge)*
