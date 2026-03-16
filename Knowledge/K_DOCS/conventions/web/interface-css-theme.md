# Interface CSS Theme Convention

## Context

All interface pages (I2 Session Review, I3 Task Workflow, I4 Project Viewer, I5 Live Mindmap) render inside a `srcdoc` iframe created by the viewer (`docs/index.html`). The viewer injects a `<style>` block into the iframe `<head>` that defines theme-aware CSS custom properties for all 4 themes. Interface CSS files must use these **wrapper variables** for core colors and only define their own prefixed variables for interface-specific colors.

## Wrapper Variables (never redefine)

The viewer injects these into every interface iframe `<head>`, already themed per `data-theme` attribute:

| Variable | Light default | Dark default | Purpose |
|----------|--------------|-------------|---------|
| `--fg` | `#1a1a2e` | `#e8e4f0` | Primary text color |
| `--bg` | `#faf6f1` | `#1a1a2e` | Background color |
| `--muted` | `#5c5c78` | `#9494aa` | Secondary/muted text |
| `--accent` | `#0055b3` | `#5599dd` | Links, active elements |
| `--border` | `#d48a3c` | `#cc8833` | Borders, dividers |
| `--code-bg` | `#eee8df` | `#28283e` | Code blocks, secondary bg, toolbars |
| `--col-alt` | `rgba(0,85,179,0.05)` | `rgba(85,153,221,0.07)` | Alternating row background |

The wrapper also sets `body { background: var(--bg); color: var(--fg); }`.

**Rule: never redefine these variables in interface CSS.** The viewer handles all 4 themes + auto dark mode detection.

## Interface-Specific Variables

For colors not covered by the wrapper (success, warning, danger, badges, hover, etc.), use a prefixed namespace:

- Session Review: `--sv-*`
- Task Workflow: `--tw-*`
- Project Viewer: `--pv-*`

Define light defaults in `:root` and dark overrides in the standard dark theme selector block.

## File Structure

Every interface CSS file follows this order:

```css
/* 1. Dark theme overrides — interface-specific variables only */
[data-theme="midnight"],
[data-theme="daltonism-dark"],
[data-color-mode="dark"],
.theme-dark {
  --xx-success: #3fb950;
  --xx-warning: #d29922;
  /* ... only interface-specific vars ... */
}

/* 2. Scrollbars — always use wrapper vars */
*, *::before, *::after {
  scrollbar-width: thin;
  scrollbar-color: var(--border, #c0c0c0) transparent;
}

/* 3. Interface-specific variable defaults (light) */
:root {
  --xx-success: #28a745;
  --xx-warning: #f9a825;
  /* ... only interface-specific vars ... */
}

/* 4. Component styles using wrapper + interface vars */
#xx-viewer {
  color: var(--fg, #24292e);
  /* ... */
}
```

## Rules

1. **Always use fallback values**: `var(--fg, #1f2328)` — never bare `var(--fg)`. If the wrapper CSS fails to load, the interface must still render.

2. **No `:root` or light theme blocks for wrapper variables**: The wrapper handles `--fg`, `--bg`, `--muted`, `--accent`, `--border`, `--code-bg` for all themes. Do not redefine them.

3. **No `@media (prefers-color-scheme: dark)` for wrapper variables**: The viewer's wrapper CSS already handles auto dark mode detection. Only use `@media` for interface-specific overrides if needed.

4. **Dark theme selector**: Always use the full selector set:
   ```css
   [data-theme="midnight"],
   [data-theme="daltonism-dark"],
   [data-color-mode="dark"],
   .theme-dark { ... }
   ```

5. **Scrollbars**: Always `scrollbar-color: var(--border) transparent` and `var(--muted)` for hover.

6. **Print styles**: Use hardcoded corporate colors (`#111`, `#333`, `#444`, `#ccc`). CSS variables don't apply in print context.

7. **Hardcoded semantic colors** (badges with fixed meaning like `passed`=green, `failed`=red) are acceptable. Use dark theme overrides via `[data-theme]` selectors if needed.

## Variable Mapping Reference

When migrating from prefixed to wrapper variables:

| Old pattern | New pattern |
|-------------|-------------|
| `var(--xx-text)` | `var(--fg, #fallback)` |
| `var(--xx-bg)` | `var(--bg, #fallback)` |
| `var(--xx-muted)` | `var(--muted, #fallback)` |
| `var(--xx-accent)` | `var(--accent, #fallback)` |
| `var(--xx-border)` | `var(--border, #fallback)` |
| `var(--xx-card-bg)` / `var(--xx-bg-secondary)` | `var(--code-bg, #fallback)` |
