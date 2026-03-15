---
name: docs-create
user_invocable: true
description: "Load K_DOCS documentation methodology chain before creating publications. Usage: /docs-create (load chain), /docs-create <slug> (create new publication)."
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

## K_DOCS — Documentation Creation

Arguments: $ARGUMENTS

### Methodology Chain — Mandatory Pre-Load

Before creating any documentation content, the following methodology files MUST be loaded and internalized. Read them in order:

!`python3 -c "
import os
R = 'Knowledge/K_DOCS' if os.path.isdir('Knowledge/K_DOCS/methodology') else '.'
chain = [
    ('documentation-generation.md', 'Standards: publication structure, writing style, quality checklist, front matter contract'),
    ('interactive-documentation.md', 'Workflow: gather → structure → expand → web pages → deliver'),
    ('documentation-audience.md', 'Audience: 19 segments, content voice guidelines, rewrite principle'),
    ('webcard-generation.md', 'Webcards: specs, themes, naming, live webcard alternative'),
    ('web-production-pipeline.md', 'Pipeline: viewer architecture, Liquid resolver, .nojekyll'),
    ('web-pagination-export.md', 'Export: PDF (CSS Paged Media) + DOCX (MSO elements)'),
]
print('| # | Methodology | Role |')
print('|---|---|---|')
for i, (f, desc) in enumerate(chain, 1):
    path = os.path.join(R, 'methodology', f)
    exists = '✅' if os.path.exists(path) else '❌'
    size = f'{os.path.getsize(path) // 1024}KB' if os.path.exists(path) else '—'
    print(f'| {i} | {exists} \`{f}\` ({size}) | {desc} |')
print()
print('All methodologies loaded from: \`Knowledge/K_DOCS/methodology/\`')
"
`

### Quality Checklist (from documentation-generation.md)

Before publishing or delivering a publication:

- [ ] All front matter fields present (title, description, pub_id, version, pub_date, permalink, og_image, keywords)
- [ ] Abstract answers "why" + "what" + context (200–400 words)
- [ ] Mind map diagram present after abstract (in ALL tiers)
- [ ] Diagrams support the narrative (not decorative)
- [ ] Tables use consistent format (markdown pipes, bold headers)
- [ ] Three tiers created: source + summary + full
- [ ] Bilingual mirrors exist (EN + FR) for all web pages
- [ ] Webcard generated (or placeholder) and `og_image` set
- [ ] Related publications linked
- [ ] Audience framing applied (lead with "why does this matter?")

### Publication Phase Pattern

| Phase | Output |
|-------|--------|
| **Gather** | User provides raw intelligence |
| **Structure** | Methodology file if applicable |
| **Expand** | Source: `publications/<slug>/v1/README.md` |
| **Web pages** | 4 files: EN/FR summary + full |
| **Deliver** | Commit and push |

### Front Matter Template

```yaml
---
title: "<Title — Descriptive Subtitle>"
description: "<One sentence, SEO-optimized>"
permalink: /publications/<slug>/
lang: en
permalink_fr: /fr/publications/<slug>/
header_title: "<Short Title>"
tagline: "<Tagline>"
pub_id: "Publication #N"
pub_meta: "Publication #N v1 | Month YYYY"
pub_version: "v1"
pub_number: N
pub_date: "Month YYYY"
og_image: /assets/og/<slug>-en-cayman.gif
keywords: "keyword1, keyword2, keyword3"
---
```

### Instructions

After loading, follow the methodology chain strictly:
1. Read the methodologies (they are now loaded above)
2. Create/review documentation following the quality checklist
3. Always create all 4 web pages in one pass (EN/FR summary + full)
4. Include mind map after abstract in ALL tiers
5. Apply audience framing: lead with "why does this matter?" before "what"
6. Use the front matter template — adapt fields per tier (summary vs full, EN vs FR)
