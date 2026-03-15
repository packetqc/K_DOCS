#!/usr/bin/env node
/**
 * Capture MindElixir rendering as progressive PNG frames.
 * Uses headless Chrome to render the actual MindElixir library,
 * then captures screenshots as branches expand.
 *
 * Usage: node capture_mindmap.js [daltonism-light|daltonism-dark|cayman|midnight] [--full]
 * Output: /tmp/mindmap-frames/frame-*.png
 */

const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

const PROJECT_ROOT = path.resolve(__dirname, '..', '..', '..');
const MIND_PATH = path.join(PROJECT_ROOT, 'Knowledge', 'K_MIND', 'mind', 'mind_memory.md');
const FRAME_DIR = '/tmp/mindmap-frames';

const THEME_MAP = {
  'daltonism-light': {
    bg: '#faf6f1', root: '#0055b3', rootFg: '#fff',
    palette: ['#0055b3','#b35900','#6b21a8','#b91c1c','#0e7490','#15803d'],
    cssVars: { '--fg':'#1a1a2e', '--main-color':'#0055b3' },
  },
  'daltonism-dark': {
    bg: '#1a1a2e', root: '#2a4a7a', rootFg: '#e8e0d4',
    palette: ['#5b9bd5','#f0a050','#b088d0','#e87070','#50b8d0','#60c080'],
    cssVars: { '--fg':'#e8e0d4', '--main-color':'#5b9bd5' },
  },
  'cayman': {
    bg: '#eff6ff', root: '#1d4ed8', rootFg: '#fff',
    palette: ['#2563eb','#0d9488','#7c3aed','#dc2626','#ea580c','#0284c7'],
    cssVars: { '--fg':'#0f172a', '--main-color':'#1d4ed8' },
  },
  'midnight': {
    bg: '#0f172a', root: '#1e40af', rootFg: '#e2e8f0',
    palette: ['#60a5fa','#34d399','#a78bfa','#fb7185','#fb923c','#38bdf8'],
    cssVars: { '--fg':'#e2e8f0', '--main-color':'#60a5fa' },
  },
};

function readMindmap() {
  const text = fs.readFileSync(MIND_PATH, 'utf8');
  const match = text.match(/```mermaid\s*\n([\s\S]*?)```/);
  if (!match) throw new Error('No mermaid block found');
  return match[1].trim();
}

function parseMermaidToMindElixir(code) {
  const lines = code.split('\n');
  let root = null;
  const stack = [];

  for (const line of lines) {
    const stripped = line.trim();
    if (!stripped || stripped.startsWith('%%') || stripped === 'mindmap') continue;

    const indent = line.length - line.trimStart().length;
    let text = stripped;

    // Strip decorators
    let m;
    if ((m = text.match(/^root\(\((.*)\)\)$/))) text = m[1];
    else if ((m = text.match(/^\(\((.*)\)\)$/))) text = m[1];
    else if ((m = text.match(/^\((.*)\)$/))) text = m[1];
    else if ((m = text.match(/^\[(.*)\]$/))) text = m[1];
    else if ((m = text.match(/^\{(.*)\}$/))) text = m[1];

    const node = {
      topic: text,
      id: 'n' + Math.random().toString(36).substr(2, 8),
      children: [],
      _indent: indent,
    };

    if (!root) {
      node.id = 'root';
      root = node;
      stack.push({ indent, node });
      continue;
    }

    while (stack.length && stack[stack.length - 1].indent >= indent) {
      stack.pop();
    }
    if (stack.length) {
      stack[stack.length - 1].node.children.push(node);
    }
    stack.push({ indent, node });
  }

  return root;
}

function filterByDepth(node, maxDepth, currentDepth = 0) {
  // Limit tree depth for readability at 1200x630
  const filtered = { topic: node.topic, id: node.id, children: [] };
  if (currentDepth < maxDepth && node.children) {
    for (const child of node.children) {
      filtered.children.push(filterByDepth(child, maxDepth, currentDepth + 1));
    }
  }
  return filtered;
}

function buildProgressiveData(root, fullMode = false) {
  // Three short movies:
  //
  // MOVIE 1 — "The Emergence": Progressive build from root to full overview
  //   root only → depth 1 → depth 2 → depth 3 (hold)
  //
  // MOVIE 2 — "The Collapse": Retract back to skeleton
  //   depth 3 → depth 2 → depth 1 (hold)
  //
  // MOVIE 3 — "The Exploration": Each branch opens progressively, closes before next
  //   For each branch: depth 1 → 2 → 3 → 4 → (5 in full) → hold → collapse back to 1
  //
  // Normal mode: overview max=2, explore max=3
  // Full mode:   overview max=3, explore max=5
  const overviewMax = fullMode ? 3 : 2;
  const exploreMax = fullMode ? 5 : 3;

  const topChildren = root.children || [];
  const frames = [];

  // ── MOVIE 1: The Emergence ──
  // Build up from nothing to full overview, one depth at a time
  for (let d = 0; d <= overviewMax; d++) {
    frames.push({ nodeData: filterByDepth(root, d), direction: 2 });
  }
  // Hold the full overview for an extra beat
  frames.push({ nodeData: filterByDepth(root, overviewMax), direction: 2 });

  // ── MOVIE 2: The Collapse ──
  // Retract back down to just branch names
  for (let d = overviewMax - 1; d >= 1; d--) {
    frames.push({ nodeData: filterByDepth(root, d), direction: 2 });
  }
  // Hold the collapsed view
  frames.push({ nodeData: filterByDepth(root, 1), direction: 2 });

  // ── MOVIE 3: The Exploration ──
  // Each branch opens progressively depth by depth, then closes before next
  for (let i = 0; i < topChildren.length; i++) {
    // Progressive open: depth 2 → 3 → ... → exploreMax
    for (let d = 2; d <= exploreMax; d++) {
      const frameRoot = { topic: root.topic, id: root.id, children: [] };
      for (let j = 0; j < topChildren.length; j++) {
        if (j === i) {
          frameRoot.children.push(filterByDepth(topChildren[j], d, 0));
        } else {
          frameRoot.children.push(filterByDepth(topChildren[j], 1, 0));
        }
      }
      frames.push({ nodeData: frameRoot, direction: 2 });
    }
    // Hold the fully expanded branch for an extra beat
    const holdRoot = { topic: root.topic, id: root.id, children: [] };
    for (let j = 0; j < topChildren.length; j++) {
      if (j === i) {
        holdRoot.children.push(filterByDepth(topChildren[j], exploreMax, 0));
      } else {
        holdRoot.children.push(filterByDepth(topChildren[j], 1, 0));
      }
    }
    frames.push({ nodeData: holdRoot, direction: 2 });

    // Collapse back (only if not the last branch — last one holds as finale)
    if (i < topChildren.length - 1) {
      frames.push({ nodeData: filterByDepth(root, 1), direction: 2 });
    }
  }

  return frames;
}

async function main() {
  const args = process.argv.slice(2);
  const fullMode = args.includes('--full');
  const themeName = args.find(a => !a.startsWith('--')) || 'daltonism-light';
  const theme = THEME_MAP[themeName];
  if (!theme) {
    console.error(`Unknown theme: ${themeName}. Use: ${Object.keys(THEME_MAP).join(', ')}`);
    process.exit(1);
  }

  console.log(`Capturing mindmap: ${themeName}${fullMode ? ' (FULL mode)' : ''}`);

  const mermaidCode = readMindmap();
  const root = parseMermaidToMindElixir(mermaidCode);
  const progressiveFrames = buildProgressiveData(root, fullMode);

  console.log(`  ${root.children.length} top-level branches, ${progressiveFrames.length} frames`);

  // Ensure frame directory
  fs.mkdirSync(FRAME_DIR, { recursive: true });
  // Clean old frames
  for (const f of fs.readdirSync(FRAME_DIR)) {
    if (f.startsWith('frame-')) fs.unlinkSync(path.join(FRAME_DIR, f));
  }

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu'],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 630 });

  // Build HTML with MindElixir
  const html = `<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/mind-elixir@5.9.3/dist/MindElixir.css">
<script src="https://cdn.jsdelivr.net/npm/mind-elixir@5.9.3/dist/MindElixir.iife.js"></script>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: ${theme.bg}; overflow: hidden; }
  #map { width: 1200px; height: 630px; }
  .mind-elixir, map-container, .map-container { background: ${theme.bg} !important; }
</style>
</head><body>
<div id="map"></div>
<script>
  window.THEME_BG = '${theme.bg}';
  window.THEME_ROOT = '${theme.root}';
  window.THEME_ROOT_FG = '${theme.rootFg}';
  window.THEME_PALETTE = ${JSON.stringify(theme.palette)};
  window.THEME_CSS = ${JSON.stringify(theme.cssVars)};

  async function renderFrame(data) {
    document.getElementById('map').innerHTML = '';
    const ME = window.MindElixir.default || window.MindElixir;
    const mind = new ME({
      el: '#map',
      direction: 2,
      draggable: false,
      contextMenu: false,
      toolBar: false,
      nodeMenu: false,
      keypress: false,
      allowUndo: false,
    });
    mind.init(data);

    // Apply theme palette via changeTheme
    if (mind.changeTheme) {
      mind.changeTheme({
        name: 'custom',
        palette: window.THEME_PALETTE,
        cssVar: {
          '--main-color': window.THEME_CSS['--main-color'],
          '--main-bgcolor': window.THEME_BG,
          '--color': window.THEME_CSS['--fg'],
        },
      });
    }

    // Apply root node colors
    await new Promise(r => setTimeout(r, 200));
    const rootEl = document.querySelector('me-root tpc');
    if (rootEl) {
      rootEl.style.background = window.THEME_ROOT;
      rootEl.style.color = window.THEME_ROOT_FG;
      rootEl.style.borderRadius = '8px';
      rootEl.style.padding = '8px 20px';
      rootEl.style.fontSize = '18px';
      rootEl.style.fontWeight = 'bold';
    }

    // Scale to fit
    await new Promise(r => setTimeout(r, 300));
    if (mind.scaleFit) mind.scaleFit();
    await new Promise(r => setTimeout(r, 200));
    return mind;
  }

  window.renderFrame = renderFrame;
</script>
</body></html>`;

  await page.setContent(html, { waitUntil: 'domcontentloaded', timeout: 30000 });
  // Wait for CDN resources to load
  await new Promise(r => setTimeout(r, 3000));

  // Capture each progressive frame
  for (let i = 0; i < progressiveFrames.length; i++) {
    const data = progressiveFrames[i];
    await page.evaluate(async (d) => {
      await window.renderFrame(d);
    }, data);

    // Wait for rendering
    await new Promise(r => setTimeout(r, 500));

    const framePath = path.join(FRAME_DIR, `frame-${String(i).padStart(2, '0')}.png`);
    await page.screenshot({ path: framePath, type: 'png' });
    console.log(`  Frame ${i + 1}/${progressiveFrames.length}: ${framePath}`);
  }

  await browser.close();
  console.log(`  Done: ${progressiveFrames.length} frames in ${FRAME_DIR}/`);
}

main().catch(e => { console.error(e); process.exit(1); });
