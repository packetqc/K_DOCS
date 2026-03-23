# Interactive Diagnostic — Convention

> Adapted from `packetqc/knowledge:knowledge/methodology/interactive-diagnostic.md`

Structured methodology for diagnosing rendering, integration, or behavioral problems. Every step documented in real-time on GitHub issue for complete audit trail.

## When to Use

- Web page rendering problems (Mermaid, CSS, layout, JavaScript)
- Cross-language discrepancies (EN works, FR doesn't)
- Build pipeline issues (Jekyll, kramdown, GitHub Pages)
- Any problem requiring iterative hypothesis elimination

## Core Principles

1. **Real-time documentation** — every exchange posted as issue comment
2. **Comparative analysis** — always compare working vs broken version
3. **Iterative elimination** — systematically eliminate hypotheses, document each
4. **User-driven pivots** — user sees rendered output, follow their redirects immediately
5. **Gradual isolation** — progressively add/remove components to isolate breaking change

## Protocol

1. **Create diagnostic task** — GitHub issue before first file examined
2. **Document initial context** — URLs, observations, suspected causes
3. **Comparative analysis** — section by section, working vs broken
4. **Systematic elimination** — one hypothesis at a time
5. **User pivot** — when user redirects, follow immediately
6. **Isolation** — if unclear, progressively isolate components
7. **Resolution** — apply fix, verify, close issue
