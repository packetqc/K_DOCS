---
layout: publication
title: "Live Mindmap — K_MIND Knowledge Graph"
description: "Interactive live rendering of the K_MIND memory mindmap. Reads mind_memory.md and renders with MindElixir in real-time."
permalink: /interfaces/live-mindmap/
permalink_fr: /fr/interfaces/live-mindmap/
lang: en
header_title: "Live Mindmap"
tagline: "K_MIND Knowledge Graph — Real-Time"
pub_meta: "Interface | K_DOCS"
pub_version: "v3"
pub_date: "March 2026"
page_type: interface
og_image: /assets/og/live-mindmap-en-daltonism-light.gif
---

{::nomarkdown}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/mind-elixir@5.9.3/dist/MindElixir.css">
<style>
/* Theme CSS variables — synced with viewer */
:root, html, html[data-theme="daltonism-light"] {
  --bg: #faf6f1; --fg: #1a1a2e; --accent: #0055b3; --muted: #5c5c78;
  --border: #d48a3c; --code-bg: #eee8df;
}
@media (prefers-color-scheme: dark) {
  html:not([data-theme]), html[data-theme="auto"] {
    --bg: #1a1a2e; --fg: #e8e4f0; --accent: #5599dd; --muted: #9494aa;
    --border: #cc8833; --code-bg: #28283e;
  }
}
html[data-theme="cayman"] {
  --bg: #eff6ff; --fg: #0f172a; --accent: #1d4ed8; --muted: #475569;
  --border: #93c5fd; --code-bg: #dbeafe;
}
html[data-theme="midnight"] {
  --bg: #0f172a; --fg: #e2e8f0; --accent: #60a5fa; --muted: #94a3b8;
  --border: #334155; --code-bg: #1e293b;
}
html[data-theme="daltonism-dark"] {
  --bg: #1a1a2e; --fg: #e8e4f0; --accent: #5599dd; --muted: #9494aa;
  --border: #cc8833; --code-bg: #28283e;
}
html, body {
  height: 100%; margin: 0; overflow: hidden;
  background: var(--bg); color: var(--fg);
}
/* Prevent MindElixir text editing on nodes */
me-tpc { user-select: none !important; -webkit-user-select: none !important; }
me-tpc:focus { outline: none !important; box-shadow: none !important; }
/* Discrete thin scrollbars */
*, *::before, *::after { scrollbar-width: thin; scrollbar-color: var(--border, #c0c0c0) transparent; }
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border, #c0c0c0); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--muted, #888); }
body > .container {
  display: flex; flex-direction: column;
  height: 100%; overflow: hidden;
  padding-left: 1rem;
  padding-right: 1rem;
  box-sizing: border-box;
}
.mindmap-controls {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  flex-wrap: wrap;
  align-items: center;
}
.mindmap-controls button,
.mindmap-controls select {
  background: var(--accent, #0055b3);
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.35rem 0.8rem;
  font-size: 0.82rem;
  cursor: pointer;
  font-weight: 500;
}
.mindmap-controls select { appearance: auto; }
.mindmap-controls button:hover,
.mindmap-controls select:hover { opacity: 0.85; }
.mindmap-controls .sep {
  width: 1px; height: 1.2rem; background: var(--border, #d48a3c); margin: 0 0.2rem;
}
.mindmap-controls .mindmap-status {
  font-size: 0.8rem;
  color: var(--muted, #5c5c78);
  margin-left: auto;
}
/* Main area: mindmap + help panel side by side */
.mindmap-area {
  display: flex; flex: 1; min-height: 0; gap: 0;
  margin-bottom: 1.5rem;
}
#mindmap-container {
  flex: 1;
  overflow: hidden;
  border: 1px solid var(--border, #d48a3c);
  border-radius: 8px;
  position: relative;
  min-width: 0;
}
.mindmap-error {
  color: #dc2626;
  padding: 1rem;
  text-align: center;
}
/* Help button — round ? */
.help-btn {
  width: 1.6rem; height: 1.6rem;
  border-radius: 50%;
  background: var(--accent, #0055b3);
  color: white;
  border: none;
  font-size: 0.9rem; font-weight: 700;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  padding: 0;
  flex-shrink: 0;
}
.help-btn:hover { opacity: 0.85; }
.help-btn.active { background: var(--muted, #5c5c78); }
/* Help panel — right side */
.help-panel {
  width: 0; overflow: hidden;
  border: none;
  border-radius: 0 8px 8px 0;
  background: var(--code-bg, #eee8df);
  transition: width 0.25s ease, border-width 0.25s ease, padding 0.25s ease;
  padding: 0;
  font-size: 0.82rem;
  line-height: 1.5;
  color: var(--fg, #1a1a2e);
}
.help-panel.open {
  width: 280px;
  border: 1px solid var(--border, #d48a3c);
  border-left: none;
  padding: 1rem;
  overflow-y: auto;
}
.help-panel h3 {
  margin: 0 0 0.6rem; font-size: 0.95rem; color: var(--accent, #0055b3);
}
.help-panel h4 {
  margin: 0.8rem 0 0.3rem; font-size: 0.85rem; color: var(--accent, #0055b3);
}
.help-panel p { margin: 0 0 0.5rem; }
.help-panel kbd {
  display: inline-block; background: var(--bg, #faf6f1); border: 1px solid var(--border, #d48a3c);
  border-radius: 3px; padding: 0.05rem 0.35rem; font-size: 0.78rem; font-family: monospace;
}
</style>

<h2>K_MIND — Live Knowledge Graph</h2>

<div class="mindmap-controls">
  <select id="mindmap-view" onchange="loadMindmap()">
    <option value="normal">Normal</option>
    <option value="full">Full</option>
  </select>
  <select id="mindmap-theme" onchange="applyMindTheme()">
    <option value="auto">Theme: Auto</option>
    <option value="cayman">Cayman</option>
    <option value="midnight">Midnight</option>
    <option value="daltonism-light">Daltonism Light</option>
    <option value="daltonism-dark">Daltonism Dark</option>
  </select>
  <button id="btn-reload" onclick="loadMindmap()">Reload</button>
  <span class="sep"></span>
  <button id="btn-center" onclick="if(mindInstance)mindInstance.toCenter()">Center</button>
  <button id="btn-fit" onclick="if(mindInstance)mindInstance.scaleFit()">Fit</button>
  <span class="sep"></span>
  <button id="btn-fullscreen" onclick="toggleFullscreen()">Fullscreen</button>
  <span class="mindmap-status" id="mindmap-status">Loading...</span>
  <button class="help-btn" id="help-toggle" onclick="toggleHelp()" title="Help">?</button>
</div>

<div class="mindmap-area">
  <div id="mindmap-container">
    <div class="loading" style="padding:2rem;text-align:center;">Loading mindmap...</div>
  </div>
  <div class="help-panel" id="help-panel"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/mind-elixir@5.9.3/dist/MindElixir.iife.js"></script>
<script>
(function() {
  var RAW_BASE = 'https://raw.githubusercontent.com/packetqc/knowledge/main/Knowledge/K_MIND/';
  var MIND_URL = RAW_BASE + 'mind/mind_memory.md';
  var CONFIG_URL = RAW_BASE + 'conventions/depth_config.json';

  var cachedMermaid = null;
  var cachedConfig = null;
  window.mindInstance = null;

  // === Theme definitions matching viewer themes ===
  var MIND_THEMES = {
    cayman: {
      name: 'Cayman', type: 'light',
      palette: ['#1d4ed8','#2563eb','#3b82f6','#60a5fa','#0ea5e9','#0284c7','#7c3aed','#8b5cf6','#06b6d4','#14b8a6'],
      cssVar: {
        '--bgcolor': '#eff6ff',
        '--root-color': '#ffffff', '--root-bgcolor': '#1d4ed8', '--root-border-color': '#1e40af',
        '--main-color': '#0f172a', '--main-bgcolor': '#dbeafe',
        '--color': '#334155', '--selected': '#3b82f6',
        '--root-radius': '30px', '--main-radius': '8px',
        '--panel-color': '#0f172a', '--panel-bgcolor': '#eff6ff', '--panel-border-color': '#93c5fd'
      }
    },
    midnight: {
      name: 'Midnight', type: 'dark',
      palette: ['#60a5fa','#818cf8','#a78bfa','#38bdf8','#22d3ee','#34d399','#fb923c','#f472b6','#c084fc','#facc15'],
      cssVar: {
        '--bgcolor': '#0f172a',
        '--root-color': '#e2e8f0', '--root-bgcolor': '#1e40af', '--root-border-color': '#3b82f6',
        '--main-color': '#e2e8f0', '--main-bgcolor': '#1e293b',
        '--color': '#94a3b8', '--selected': '#60a5fa',
        '--root-radius': '30px', '--main-radius': '8px',
        '--panel-color': '#e2e8f0', '--panel-bgcolor': '#1e293b', '--panel-border-color': '#334155'
      }
    },
    'daltonism-light': {
      name: 'Daltonism Light', type: 'light',
      palette: ['#0055b3','#d48a3c','#6b21a8','#0369a1','#b45309','#047857','#be185d','#4338ca','#0e7490','#a16207'],
      cssVar: {
        '--bgcolor': '#faf6f1',
        '--root-color': '#ffffff', '--root-bgcolor': '#0055b3', '--root-border-color': '#003d80',
        '--main-color': '#1a1a2e', '--main-bgcolor': '#eee8df',
        '--color': '#5c5c78', '--selected': '#0055b3',
        '--root-radius': '30px', '--main-radius': '8px',
        '--panel-color': '#1a1a2e', '--panel-bgcolor': '#faf6f1', '--panel-border-color': '#d48a3c'
      }
    },
    'daltonism-dark': {
      name: 'Daltonism Dark', type: 'dark',
      palette: ['#5599dd','#cc8833','#a78bfa','#38bdf8','#fbbf24','#34d399','#f472b6','#818cf8','#22d3ee','#fb923c'],
      cssVar: {
        '--bgcolor': '#1a1a2e',
        '--root-color': '#e8e4f0', '--root-bgcolor': '#2a4a7a', '--root-border-color': '#5599dd',
        '--main-color': '#e8e4f0', '--main-bgcolor': '#28283e',
        '--color': '#9494aa', '--selected': '#5599dd',
        '--root-radius': '30px', '--main-radius': '8px',
        '--panel-color': '#e8e4f0', '--panel-bgcolor': '#28283e', '--panel-border-color': '#cc8833'
      }
    }
  };

  function detectTheme() {
    // Check viewer theme from parent or localStorage
    var saved = localStorage.getItem('kdocs-theme');
    if (saved && saved !== 'auto' && MIND_THEMES[saved]) return saved;
    // Auto: check prefers-color-scheme
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) return 'daltonism-dark';
    return 'daltonism-light';
  }

  function getCurrentTheme() {
    var sel = document.getElementById('mindmap-theme');
    var val = sel ? sel.value : 'auto';
    if (val === 'auto') return detectTheme();
    return val;
  }

  window.applyMindTheme = function() {
    var themeKey = getCurrentTheme();
    // Apply page theme via data-theme attribute
    document.documentElement.setAttribute('data-theme', themeKey);
    // Apply MindElixir canvas theme
    if (!window.mindInstance) return;
    var theme = MIND_THEMES[themeKey];
    if (theme) window.mindInstance.changeTheme(theme);
  };

  // === Fetch helpers ===
  function fetchMindmap() {
    if (cachedMermaid) return Promise.resolve(cachedMermaid);
    return fetch(MIND_URL)
      .then(function(r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.text(); })
      .then(function(text) {
        var match = text.match(/```mermaid\s*\n([\s\S]*?)```/);
        if (!match) throw new Error('No mermaid block found');
        cachedMermaid = match[1].trim();
        return cachedMermaid;
      });
  }

  function fetchConfig() {
    if (cachedConfig) return Promise.resolve(cachedConfig);
    return fetch(CONFIG_URL)
      .then(function(r) { if (!r.ok) throw new Error('Config HTTP ' + r.status); return r.json(); })
      .then(function(cfg) { cachedConfig = cfg; return cfg; })
      .catch(function() {
        cachedConfig = { default_depth: 3, omit: ['architecture', 'constraints'], overrides: {} };
        return cachedConfig;
      });
  }

  // === Depth filter (JS port of mindmap_filter.py) ===
  function filterMindmap(mermaidCode, config) {
    var lines = mermaidCode.split('\n');
    var headerLines = [], bodyLines = [], inHeader = true;
    for (var i = 0; i < lines.length; i++) {
      var s = lines[i].trim();
      if (inHeader && (s.indexOf('%%{') === 0 || s === 'mindmap' || s.indexOf('root(') !== -1)) headerLines.push(lines[i]);
      else { inHeader = false; bodyLines.push(lines[i]); }
    }
    var nodes = [];
    for (var i = 0; i < bodyLines.length; i++) {
      if (!bodyLines[i].trim()) continue;
      var content = bodyLines[i].replace(/^\s+/, '');
      var indent = bodyLines[i].length - content.length;
      nodes.push({ level: Math.floor(indent / 2), text: content, lineIdx: i });
    }
    if (!nodes.length) return headerLines.join('\n');
    var rootIndent = nodes[0].level;
    var omit = config.omit || [], overrides = config.overrides || {}, def = config.default_depth || 3;
    var out = [];
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i], parts = [], tgt = n.level;
      for (var j = i; j >= 0; j--) {
        if (nodes[j].level < tgt) { parts.unshift(nodes[j].text); tgt = nodes[j].level; }
        else if (j === i) parts.push(nodes[j].text);
      }
      var path = parts.join('/'), top = parts[0] || n.text;
      var depth = n.level - rootIndent + 1;
      var skip = false;
      for (var k = 0; k < omit.length; k++) if (top === omit[k]) { skip = true; break; }
      if (skip) continue;
      var max = def, best = 0;
      for (var op in overrides) {
        if ((path === op || path.indexOf(op + '/') === 0) && op.length > best) { best = op.length; max = overrides[op]; }
      }
      if (depth <= max) out.push(bodyLines[n.lineIdx]);
    }
    return headerLines.join('\n') + '\n' + out.join('\n');
  }

  // === Omit-only filter: remove omitted branches, keep all other nodes ===
  function filterMindmapOmitOnly(mermaidCode, config) {
    var lines = mermaidCode.split('\n');
    var headerLines = [], bodyLines = [], inHeader = true;
    for (var i = 0; i < lines.length; i++) {
      var s = lines[i].trim();
      if (inHeader && (s.indexOf('%%{') === 0 || s === 'mindmap' || s.indexOf('root(') !== -1)) headerLines.push(lines[i]);
      else { inHeader = false; bodyLines.push(lines[i]); }
    }
    var omit = (config && config.omit) || [];
    if (!omit.length) return mermaidCode;
    var nodes = [];
    for (var i = 0; i < bodyLines.length; i++) {
      if (!bodyLines[i].trim()) continue;
      var content = bodyLines[i].replace(/^\s+/, '');
      var indent = bodyLines[i].length - content.length;
      nodes.push({ level: Math.floor(indent / 2), text: content, line: bodyLines[i] });
    }
    var rootIndent = nodes.length ? nodes[0].level : 0;
    var out = [], skipLevel = -1;
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i], depth = n.level - rootIndent + 1;
      if (skipLevel >= 0) {
        if (n.level > skipLevel) continue;
        skipLevel = -1;
      }
      if (depth === 1) {
        var skip = false;
        for (var k = 0; k < omit.length; k++) if (n.text === omit[k]) { skip = true; break; }
        if (skip) { skipLevel = n.level; continue; }
      }
      out.push(n.line);
    }
    return headerLines.join('\n') + '\n' + out.join('\n');
  }

  // === Mermaid → MindElixir data converter ===
  function mermaidToMindElixir(mermaidCode) {
    var lines = mermaidCode.split('\n');
    var bodyLines = [];
    var inHeader = true;
    for (var i = 0; i < lines.length; i++) {
      var s = lines[i].trim();
      if (inHeader && (s.indexOf('%%{') === 0 || s === 'mindmap' || s.indexOf('root(') !== -1)) continue;
      inHeader = false;
      if (s) bodyLines.push({ raw: lines[i], text: s });
    }

    // Parse into flat node list with levels
    var flatNodes = [];
    for (var i = 0; i < bodyLines.length; i++) {
      var line = bodyLines[i].raw;
      var content = line.replace(/^\s+/, '');
      var indent = line.length - content.length;
      var level = Math.floor(indent / 2);
      // Clean mermaid syntax: root((text)), ((text)), (text), [text]
      var clean = content
        .replace(/^root\(\(/, '').replace(/\)\)$/, '')
        .replace(/^\(\(/, '').replace(/\)\)$/, '')
        .replace(/^\(/, '').replace(/\)$/, '')
        .replace(/^\[/, '').replace(/\]$/, '')
        .replace(/^\{/, '').replace(/\}$/, '');
      flatNodes.push({ level: level, topic: clean, id: 'me-' + i });
    }

    if (!flatNodes.length) {
      return { nodeData: { topic: 'knowledge', id: 'me-root', children: [] }, direction: 2 };
    }

    // Build tree recursively
    function buildChildren(startIdx, parentLevel) {
      var children = [];
      var i = startIdx;
      while (i < flatNodes.length) {
        var node = flatNodes[i];
        if (node.level <= parentLevel) break;
        if (node.level === parentLevel + 1) {
          var child = { topic: node.topic, id: node.id, children: [] };
          // Collect sub-children
          var sub = buildChildren(i + 1, node.level);
          child.children = sub.children;
          children.push(child);
          i = sub.nextIdx;
        } else {
          i++;
        }
      }
      return { children: children, nextIdx: i };
    }

    var root = { topic: 'knowledge', id: 'me-root', children: [] };
    var result = buildChildren(0, flatNodes[0].level - 1);
    root.children = result.children;

    // If first node is also "knowledge" (the root), use its children directly
    if (root.children.length === 0 && flatNodes.length > 0) {
      root.topic = flatNodes[0].topic;
    }

    return {
      nodeData: root,
      direction: 2
    };
  }

  // === Load ===
  window.loadMindmap = function() {
    var container = document.getElementById('mindmap-container');
    var status = document.getElementById('mindmap-status');
    var viewSelect = document.getElementById('mindmap-view');
    var mode = viewSelect ? viewSelect.value : 'normal';

    container.innerHTML = '<div class="loading" style="padding:2rem;text-align:center;">' + il.loadingMsg + '</div>';
    status.textContent = il.fetching;

    // Destroy previous instance
    if (window.mindInstance) {
      try { window.mindInstance.destroy(); } catch(e) {}
      window.mindInstance = null;
    }

    Promise.all([fetchMindmap(), fetchConfig()])
      .then(function(results) {
        var mermaidCode = results[0];
        var config = results[1];
        // Normal mode: load ALL nodes but collapse per config. Full mode: same data, deeper initial expand.
        // filterMindmap only used for omit list (architecture/constraints hidden in normal mode)
        var displayCode = (mode === 'full') ? mermaidCode : filterMindmapOmitOnly(mermaidCode, config);

        // Convert to MindElixir data
        var data = mermaidToMindElixir(displayCode);

        // Count nodes
        function countNodes(node) {
          var c = 1;
          if (node.children) for (var i = 0; i < node.children.length; i++) c += countNodes(node.children[i]);
          return c;
        }
        var nodeCount = countNodes(data.nodeData) - 1; // exclude root

        // Clear container
        container.innerHTML = '';

        // Get theme
        var themeKey = getCurrentTheme();
        var theme = MIND_THEMES[themeKey] || MIND_THEMES['daltonism-light'];

        // Initialize MindElixir
        var mind = new MindElixir.default({
          el: container,
          direction: MindElixir.SIDE,
          editable: false,
          keypress: false,
          toolBar: false,
          theme: theme,
          contextMenu: false,
          allowUndo: false
        });

        mind.init(data);
        window.mindInstance = mind;

        // Collapse children of top-level groups using MindElixir API (both views)
        (function collapseDeep(node, depth) {
          if (!node.children || !node.children.length) return;
          for (var i = 0; i < node.children.length; i++) {
            var child = node.children[i];
            if (child.children && child.children.length > 0 && depth >= 1) {
              var el = mind.findEle(child.id);
              if (el) mind.expandNode(el, false);
            } else {
              collapseDeep(child, depth + 1);
            }
          }
        })(mind.nodeData, 0);
        document.documentElement.setAttribute('data-theme', themeKey);

        // Fix Ctrl+click expand all: reset descendant state before MindElixir handles it
        container.addEventListener('click', function(e) {
          if (e.target.tagName !== 'ME-EPD') return;
          if (!e.ctrlKey && !e.metaKey) return;
          var tpc = e.target.previousSibling;
          if (!tpc || !tpc.nodeObj) return;
          (function resetAll(obj) {
            if (obj.children) obj.children.forEach(function(c) { c.expanded = false; resetAll(c); });
          })(tpc.nodeObj);
        }, true);

        // Fit after render
        setTimeout(function() { mind.scaleFit(); }, 200);

        var modeLabel = (mode === 'full') ? il.full : 'Normal';
        status.textContent = modeLabel + ' — ' +
          nodeCount + ' ' + il.nodes + ' — ' + new Date().toLocaleTimeString();
      })
      .catch(function(err) {
        container.innerHTML = '<div class="mindmap-error"><p>' + il.error + ': ' + err.message + '</p></div>';
        status.textContent = il.error;
      });
  };

  window.toggleFullscreen = function() {
    var container = document.getElementById('mindmap-container');
    if (document.fullscreenElement) document.exitFullscreen();
    else container.requestFullscreen();
  };

  // Fit mindmap on fullscreen change and window resize
  document.addEventListener('fullscreenchange', function() {
    if (window.mindInstance) setTimeout(function() { window.mindInstance.scaleFit(); }, 200);
  });
  window.addEventListener('resize', function() {
    if (window.mindInstance) window.mindInstance.scaleFit();
  });

  // Sync theme on page load
  var themeSelect = document.getElementById('mindmap-theme');
  if (themeSelect) {
    var saved = localStorage.getItem('kdocs-theme');
    if (saved && saved !== 'auto') themeSelect.value = saved;
  }

  // Listen for theme changes from viewer (master)
  if (typeof BroadcastChannel !== 'undefined') {
    var themeChannel = new BroadcastChannel('kdocs-theme-sync');
    themeChannel.onmessage = function(ev) {
      var val = ev.data;
      localStorage.setItem('kdocs-theme', val);
      if (val === 'auto') document.documentElement.removeAttribute('data-theme');
      else document.documentElement.setAttribute('data-theme', val);
      // Sync dropdown
      if (themeSelect) themeSelect.value = val;
      // Apply MindElixir canvas theme
      window.applyMindTheme();
    };
  }

  // === Bilingual i18n ===
  var LANG = (document.documentElement.lang === 'fr' || window.location.pathname.indexOf('/fr/') >= 0) ? 'fr' : 'en';
  var I = {
    en: { title: 'K_MIND — Live Knowledge Graph', full: 'Full', themeAuto: 'Theme: Auto',
      dalLight: 'Daltonism Light', dalDark: 'Daltonism Dark', reload: 'Reload',
      center: 'Center', fit: 'Fit', fullscreen: 'Fullscreen', loading: 'Loading...',
      loadingMsg: 'Loading mindmap...', fetching: 'Fetching from GitHub...', error: 'Error',
      helpTitle: 'Help', nodes: 'nodes' },
    fr: { title: 'K_MIND \u2014 Graphe de connaissances vivant', full: 'Complet', themeAuto: 'Th\u00e8me : Auto',
      dalLight: 'Daltonisme clair', dalDark: 'Daltonisme sombre', reload: 'Recharger',
      center: 'Centrer', fit: 'Ajuster', fullscreen: 'Plein \u00e9cran', loading: 'Chargement...',
      loadingMsg: 'Chargement du mindmap...', fetching: 'R\u00e9cup\u00e9ration depuis GitHub...', error: 'Erreur',
      helpTitle: 'Aide', nodes: 'n\u0153uds' }
  };
  var il = I[LANG];
  // Translate static HTML controls
  (function() {
    var h2 = document.querySelector('h2'); if (h2) h2.textContent = il.title;
    var vs = document.getElementById('mindmap-view');
    if (vs) { var opts = vs.querySelectorAll('option'); for (var i = 0; i < opts.length; i++) { if (opts[i].value === 'full') opts[i].textContent = il.full; } }
    var ts = document.getElementById('mindmap-theme');
    if (ts) { var to = ts.querySelectorAll('option'); var tm = { auto: il.themeAuto, 'daltonism-light': il.dalLight, 'daltonism-dark': il.dalDark }; for (var i = 0; i < to.length; i++) { if (tm[to[i].value]) to[i].textContent = tm[to[i].value]; } }
    var bm = {'btn-reload': il.reload, 'btn-center': il.center, 'btn-fit': il.fit, 'btn-fullscreen': il.fullscreen};
    Object.keys(bm).forEach(function(id) { var b = document.getElementById(id); if (b) b.textContent = bm[id]; });
    var st = document.getElementById('mindmap-status'); if (st) st.textContent = il.loading;
    var ht = document.getElementById('help-toggle'); if (ht) ht.title = il.helpTitle;
    var ld = document.querySelector('#mindmap-container .loading'); if (ld) ld.textContent = il.loadingMsg;
  })();
  var helpContent = {
    en: '<h3>Live Mindmap Help</h3>' +
      '<h4>Navigation</h4>' +
      '<p><kbd>Scroll</kbd> to zoom in/out<br>' +
      '<kbd>Click + Drag</kbd> on background to pan</p>' +
      '<h4>Expand / Collapse</h4>' +
      '<p><kbd>+</kbd> / <kbd>-</kbd> — expand or collapse <b>one level</b> at a time<br>' +
      '<kbd>Ctrl + Click</kbd> on <kbd>+</kbd> — expand <b>all</b> levels at once</p>' +
      '<h4>Toolbar</h4>' +
      '<p><b>Normal</b> — all nodes, architecture/constraints hidden, collapsed at level 2<br>' +
      '<b>Full</b> — all nodes including architecture/constraints, collapsed at level 2<br>' +
      '<b>Reload</b> — re-fetch from GitHub<br>' +
      '<b>Center</b> — center the map without scaling<br>' +
      '<b>Fit</b> — fit entire map in view<br>' +
      '<b>Fullscreen</b> — toggle fullscreen mode</p>' +
      '<h4>What is this?</h4>' +
      '<p>This mindmap is the <b>K_MIND memory grid</b> — the live knowledge graph of the system. ' +
      'Every node represents a directive: architecture rules, conventions, work state, or session context. ' +
      'It updates in real-time as conversations progress.</p>',
    fr: '<h3>Aide — Mindmap vivant</h3>' +
      '<h4>Navigation</h4>' +
      '<p><kbd>Molette</kbd> pour zoomer<br>' +
      '<kbd>Clic + Glisser</kbd> sur le fond pour se deplacer</p>' +
      '<h4>Deplier / Replier</h4>' +
      '<p><kbd>+</kbd> / <kbd>-</kbd> — deplier ou replier <b>un niveau</b> a la fois<br>' +
      '<kbd>Ctrl + Clic</kbd> sur <kbd>+</kbd> — deplier <b>tous</b> les niveaux d\'un coup</p>' +
      '<h4>Barre d\'outils</h4>' +
      '<p><b>Normal</b> — tous les noeuds, architecture/contraintes masquees, replie au niveau 2<br>' +
      '<b>Full</b> — tous les noeuds y compris architecture/contraintes, replie au niveau 2<br>' +
      '<b>Reload</b> — re-charger depuis GitHub<br>' +
      '<b>Center</b> — centrer sans redimensionner<br>' +
      '<b>Fit</b> — ajuster la carte a la vue<br>' +
      '<b>Fullscreen</b> — basculer en plein ecran</p>' +
      '<h4>Qu\'est-ce que c\'est ?</h4>' +
      '<p>Ce mindmap est la <b>grille memoire K_MIND</b> — le graphe de connaissances vivant du systeme. ' +
      'Chaque noeud represente une directive : regles d\'architecture, conventions, etat du travail ou contexte de session. ' +
      'Il se met a jour en temps reel au fil des conversations.</p>'
  };

  var helpPanel = document.getElementById('help-panel');
  var helpBtn = document.getElementById('help-toggle');
  var HELP_KEY = 'mindmap-help-open';
  helpPanel.innerHTML = helpContent[LANG];

  window.toggleHelp = function() {
    var open = helpPanel.classList.toggle('open');
    helpBtn.classList.toggle('active', open);
    localStorage.setItem(HELP_KEY, open ? '1' : '0');
  };

  // Restore state
  if (localStorage.getItem(HELP_KEY) === '1') {
    helpPanel.classList.add('open');
    helpBtn.classList.add('active');
  }

  // Init
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadMindmap);
  } else {
    loadMindmap();
  }
})();
</script>
{:/nomarkdown}
