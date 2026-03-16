# Knowledge System Version

<!-- machine-readable version block — parsed by viewer JS -->
<!-- FORMAT: version|subversion|YYYY-MM-DD HH:MM -->
<!-- version: major knowledge version -->
<!-- subversion: incremental changes between major versions (resets to 0 on new vN) -->
<!-- datetime: creation timestamp of this version (UTC) -->
v59|1|2026-03-16 00:00

## Current

**v59 (1 — 2026-03-16 00:00)** — K2.0 production repo: multi-module architecture, static JS viewer, methodology symlinks, root essential files restored

## Sub-version Convention

Sub-versions track incremental changes between major knowledge versions:

| Field | Meaning | Example |
|-------|---------|---------|
| `version` | Major version — architectural or capability change | `v59` |
| `subversion` | Incremental change counter — resets to 0 on each new major version | `0`, `1`, `2`, to N+ |
| `datetime` | UTC timestamp of the version creation | `2026-03-03 14:00` |

**Display format**: `v59 (2026-03-16 00:00)` — parenthesized creation date/time after the major version tag.

**Context-dependent display**:
- **Interfaces** (`page_type: interface`): show the **current live version** from VERSION.md — interfaces are always up-to-date with the latest knowledge
- **Publications**: show the **knowledge version at publication creation time** — stored in front matter `knowledge_version` field — publications reflect the knowledge state when they were written

**When to increment sub-version**: Any change that doesn't warrant a new major version — methodology tweaks, layout fixes, documentation updates, asset regeneration, root file updates.

**When to increment major version**: Architectural discovery or capability change.

**Reset rule**: When major version advances (e.g., v58 → v59), sub-version resets to 0. Datetime updates to the new version's creation time.

## History

| Version | Sub | Date | Change |
|---------|-----|------|--------|
| v59 | 1 | 2026-03-16 00:00 | K2.0 root essential files + methodology symlinks + navigator methodologies widget |
| v59 | 0 | 2026-03-06 09:00 | Integrity state machine — 29-checkpoint instrument panel |
| v58 | 0 | 2026-03-05 14:00 | Agent identity — the engineer |
| v57 | 0 | 2026-03-05 09:00 | STAGE:/STEP: label sync + dot-notation + continuation + I3 |
| v56 | 0 | 2026-03-04 09:00 | PreToolUse enforcement — hook architecture that blocks |
| v55 | 0 | 2026-03-03 14:00 | Session notes → issue + CHANGELOG.md |
| v54 | 0 | 2026-03-01 10:00 | Initial sub-version system |

<details>
<summary>Legacy history (v1–v53 — packetqc/knowledge repo)</summary>

See [legacy VERSION.md](Knowledge/legacy/knowledge/VERSION.md) for the full v1–v53 history from the original knowledge repository.

</details>
