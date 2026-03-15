# NEWS

## 2026-03-09

### Fix — executer_demande env dict serialization

- **Fix `executer_demande.py`** : les valeurs de contexte structurées (dict) sont maintenant sérialisées en JSON avant d'être passées comme variables d'environnement. Corrige le crash `TypeError: expected str, bytes or os.PathLike object, not dict` lors de l'exécution de routes avec `--context` enrichi.

### Knowledge Validation — Compilation & Corrections

- **Compilation incrémentale** : deux passes — post-exécution (avant retour au quiz) + post-quiz (delta uniquement). Compilation dans tous les cas (Vrai ET Faux) pour traçabilité complète
- **Fonctions D1/D2** : noms inscrits dans `methodology-knowledge.md` (`documentation_systeme`, `documentation_utilisateur`) avec registre visible
- **Fix A1** : titre exact conservé sans reformulation par Claude
- **Fix A3** : présélection automatique du dernier projet créé au lieu du repo local
- **Session interactive** : affichage de la demande originale + synthèse au démarrage
- **Méthodologie documentation** : section compilations post-exécution ajoutée pour que D1/D2 consomment les données de compilation

## 2026-03-08

### Knowledge 2.0 — Interactive Intelligence Framework

- **Publication**: Knowledge 2.0 created as Publication #0 v2 — master publication with 8 sections covering the interactive intelligence framework
- **Methodology**: `methodology-webcard.md` — new methodology extracted from `generate_og_gifs.py` (spec, dual-theme palettes, 6 animation types, 8-frame pattern)
- **Webcards**: 4 animated OG GIFs generated for Knowledge 2.0 (EN+FR x Cayman+Midnight)
- **Structure**: Full normalize pass — summary pages EN+FR, complete FR mirror, OG tags, language bars
- **Essential files**: README.md, VERSION.md, NEWS.md, PLAN.md, LINKS.md, CHANGELOG.md created

### v2.0 Platform Evolution

- **GitHub Project board**: `project_ensure()` integrated as non-blocking precondition at A4 execution launch
- **Non-blocking persistence**: All GitHub operations persist locally when unavailable — sync at next opportunity
- **Task Progression viewer**: Persistent stage bar in Task Workflow (I3) — first visual after static mode
- **Session Viewer v2**: Modular JS, knowledge validation grid, bilingual labels, pastel blue headers
- **Landscape interfaces**: All interface pages (I1, I2, I3) default to landscape in standalone mode
- **Session identity**: `user_session_id` with system session aggregation, collateral tasks
- **Success Story #23**: Knowledge v2.0 Platform — from questionnaire to living engineering platform

### Infrastructure

- Methodology read registry to prevent duplicate reads
- Methodology family auto-loading for contextual specialization
- Working-style standards for documentation and interactive families
- `project_create.py`: GitHub Project board creation + issue + linking
- Demo sessions generator + quarterly archive mechanism
