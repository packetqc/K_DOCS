# Validation Protocol — Convention

Convention for QA validation sessions within the K_DOCS knowledge system.

## Purpose

Validation sessions verify that interfaces, data pipelines, publications, and integrations work correctly after changes. They produce structured validation results tracked in K_VALIDATION.

## When to Use

- After importing or adapting modules
- After interface changes (CSS, JS, data binding)
- After data pipeline modifications (compile scripts)
- Before pushing to production (GitHub Pages)

## Validation Targets

| Target | What to check |
|--------|--------------|
| **Interfaces** | Theme switching, dark/light rendering, data binding, link routing, scrollbars |
| **Data pipeline** | JSON compilation, field mapping, stage progression, aggregation |
| **Publications** | Front matter, content rendering, bilingual mirrors, webcards |
| **Modules** | Structure integrity, script execution, convention adherence |

## Protocol

1. **Identify scope** — what changed, what could break
2. **Create checklist** — specific items to verify per target
3. **Execute checks** — systematically verify each item
4. **Record results** — track pass/fail per item
5. **Fix issues** — address failures immediately
6. **Re-verify** — confirm fixes don't introduce new issues
7. **Update tasks** — reflect validation results in tasks.json

## Integration with K_VALIDATION

- Validation results feed into `docs/data/tasks.json` via compile scripts
- Task stages: `validation` stage maps to this protocol
- Sessions that perform validation are tagged in `sessions.json`

## Common Checks

### Interface QA
- [ ] All 4 themes render correctly
- [ ] Dark theme has light fonts (--fg, --muted variables)
- [ ] Scrollbars are thin and discrete
- [ ] Links route correctly in iframe context
- [ ] Data fields match JSON structure
- [ ] Overview/dashboard shows aggregate stats

### Data Pipeline QA
- [ ] Compile scripts run without errors
- [ ] JSON output has expected fields
- [ ] Stage mapping is correct (en cours → implement, validation → validation)
- [ ] Cross-references between tasks/sessions/projects are valid
