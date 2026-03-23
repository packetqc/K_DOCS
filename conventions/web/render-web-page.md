# Web Page Rendering — Convention

> Adapted from legacy `render_web_page.py`

Production rendering using Playwright + Chromium for web pages and Mermaid diagrams. Zero external services.

## Stack

| Tool | Role |
|------|------|
| **Playwright** | Browser automation (Chromium headless) |
| **npm mermaid** | Local Mermaid CLI for diagram rendering |
| **Python** | Orchestration and output management |

## Capabilities

- Render web pages as PNG/SVG screenshots
- Render Mermaid diagrams as PNG/SVG (local, no cloud)
- Full-page captures with configurable viewport
- CSS theme application before capture

## Usage Pattern

```bash
# Render a web page
python3 render_web_page.py --url "file:///path/to/page.html" --output screenshot.png

# Render Mermaid diagram
python3 render_web_page.py --mermaid diagram.mmd --output diagram.svg
```

## Design Constraint

All rendering is local — no external rendering services, no cloud APIs. Playwright + local Chromium ensures consistent output across environments.
