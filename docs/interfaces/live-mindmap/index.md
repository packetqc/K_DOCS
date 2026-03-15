---
layout: publication
title: "Live Mindmap — K_MIND Knowledge Graph"
description: "Interactive live rendering of the K_MIND memory mindmap. Reads mind_memory.md and renders the mermaid mindmap in real-time."
permalink: /interfaces/live-mindmap/
lang: en
header_title: "Live Mindmap"
tagline: "K_MIND Knowledge Graph — Real-Time"
pub_meta: "Interface | K_DOCS"
pub_version: "v2"
pub_date: "March 2026"
page_type: interface
og_image: /assets/og/knowledge-system-en-cayman.gif
---

{::nomarkdown}
<style>
html, body {
  height: 100%; margin: 0; overflow: hidden;
}
body > .container {
  display: flex; flex-direction: column;
  height: 100%; overflow: hidden;
}
.mindmap-container {
  width: 100%;
  flex: 1;
  overflow: hidden;
  border: 1px solid var(--border, #d48a3c);
  border-radius: 8px;
  background: var(--bg, #faf6f1);
  position: relative;
  cursor: grab;
}
.mindmap-container.dragging { cursor: grabbing; }
.mindmap-container svg {
  position: absolute;
  transform-origin: 0 0;
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
.mindmap-error {
  color: #dc2626;
  padding: 1rem;
  text-align: center;
}
/* Node path breadcrumb */
.mindmap-breadcrumb {
  position: absolute;
  bottom: 0.5rem; left: 0.5rem; right: 0.5rem;
  background: var(--code-bg, rgba(0,0,0,0.05));
  color: var(--fg, #1a1a2e);
  font-size: 0.78rem;
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
  pointer-events: none;
  z-index: 10;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  opacity: 0;
  transition: opacity 0.2s;
}
.mindmap-breadcrumb.visible { opacity: 1; }
/* Zoom indicator */
.zoom-indicator {
  position: absolute;
  top: 0.5rem; right: 0.5rem;
  background: var(--code-bg, rgba(0,0,0,0.05));
  color: var(--muted, #5c5c78);
  font-size: 0.72rem;
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  z-index: 10;
  pointer-events: none;
}
</style>

<h2>K_MIND — Live Knowledge Graph</h2>

<div class="mindmap-controls">
  <select id="mindmap-view" onchange="loadMindmap()">
    <option value="normal">Normal</option>
    <option value="full">Full</option>
  </select>
  <button onclick="loadMindmap()">Reload</button>
  <span class="sep"></span>
  <button onclick="zoomIn()">+</button>
  <button onclick="zoomOut()">&minus;</button>
  <button onclick="zoomFit()">Fit</button>
  <span class="sep"></span>
  <button onclick="toggleFullscreen()">Fullscreen</button>
  <span class="mindmap-status" id="mindmap-status">Loading...</span>
</div>

<div class="mindmap-container" id="mindmap-container">
  <div class="loading">Loading mindmap...</div>
  <div class="mindmap-breadcrumb" id="mindmap-breadcrumb"></div>
  <div class="zoom-indicator" id="zoom-indicator">100%</div>
</div>

<script>
(function() {
  var RAW_BASE = 'https://raw.githubusercontent.com/packetqc/K_DOCS/main/Knowledge/K_MIND/';
  var MIND_URL = RAW_BASE + 'mind/mind_memory.md';
  var CONFIG_URL = RAW_BASE + 'conventions/depth_config.json';

  var cachedMermaid = null;
  var cachedConfig = null;

  // Pan & zoom state
  var panZoom = { x: 0, y: 0, scale: 1, minScale: 0.1, maxScale: 5 };
  var drag = { active: false, startX: 0, startY: 0, startPanX: 0, startPanY: 0 };

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

  // === Pan & Zoom ===
  function applyTransform() {
    var container = document.getElementById('mindmap-container');
    var svg = container.querySelector('svg');
    if (!svg) return;
    svg.style.transform = 'translate(' + panZoom.x + 'px,' + panZoom.y + 'px) scale(' + panZoom.scale + ')';
    var zi = document.getElementById('zoom-indicator');
    if (zi) zi.textContent = Math.round(panZoom.scale * 100) + '%';
  }

  window.zoomIn = function() {
    panZoom.scale = Math.min(panZoom.maxScale, panZoom.scale * 1.25);
    applyTransform();
  };
  window.zoomOut = function() {
    panZoom.scale = Math.max(panZoom.minScale, panZoom.scale / 1.25);
    applyTransform();
  };
  window.zoomFit = function() {
    var container = document.getElementById('mindmap-container');
    var svg = container.querySelector('svg');
    if (!svg) return;
    var cw = container.clientWidth, ch = container.clientHeight;
    var sw = svg.getAttribute('width') || svg.viewBox.baseVal.width || svg.getBBox().width;
    var sh = svg.getAttribute('height') || svg.viewBox.baseVal.height || svg.getBBox().height;
    sw = parseFloat(sw); sh = parseFloat(sh);
    if (!sw || !sh) { panZoom.scale = 1; panZoom.x = 0; panZoom.y = 0; applyTransform(); return; }
    var scaleX = cw / sw, scaleY = ch / sh;
    panZoom.scale = Math.min(scaleX, scaleY, 2) * 0.95;
    panZoom.x = (cw - sw * panZoom.scale) / 2;
    panZoom.y = (ch - sh * panZoom.scale) / 2;
    applyTransform();
  };

  // Mouse drag to pan
  function onMouseDown(e) {
    if (e.button !== 0) return;
    // Don't drag if clicking a node
    if (e.target.closest('.mindmap-node, text, rect, circle, ellipse, path[class*="edge"]')) return;
    drag.active = true;
    drag.startX = e.clientX; drag.startY = e.clientY;
    drag.startPanX = panZoom.x; drag.startPanY = panZoom.y;
    document.getElementById('mindmap-container').classList.add('dragging');
    e.preventDefault();
  }
  function onMouseMove(e) {
    if (!drag.active) return;
    panZoom.x = drag.startPanX + (e.clientX - drag.startX);
    panZoom.y = drag.startPanY + (e.clientY - drag.startY);
    applyTransform();
  }
  function onMouseUp() {
    if (!drag.active) return;
    drag.active = false;
    document.getElementById('mindmap-container').classList.remove('dragging');
  }

  // Mouse wheel zoom (zoom toward cursor)
  function onWheel(e) {
    e.preventDefault();
    var container = document.getElementById('mindmap-container');
    var rect = container.getBoundingClientRect();
    var mx = e.clientX - rect.left, my = e.clientY - rect.top;
    var oldScale = panZoom.scale;
    var factor = e.deltaY < 0 ? 1.15 : 1 / 1.15;
    panZoom.scale = Math.max(panZoom.minScale, Math.min(panZoom.maxScale, panZoom.scale * factor));
    // Zoom toward cursor
    panZoom.x = mx - (mx - panZoom.x) * (panZoom.scale / oldScale);
    panZoom.y = my - (my - panZoom.y) * (panZoom.scale / oldScale);
    applyTransform();
  }

  // Touch pinch zoom
  var lastTouchDist = 0;
  var lastTouchMid = { x: 0, y: 0 };
  function onTouchStart(e) {
    if (e.touches.length === 2) {
      var dx = e.touches[0].clientX - e.touches[1].clientX;
      var dy = e.touches[0].clientY - e.touches[1].clientY;
      lastTouchDist = Math.sqrt(dx * dx + dy * dy);
      lastTouchMid.x = (e.touches[0].clientX + e.touches[1].clientX) / 2;
      lastTouchMid.y = (e.touches[0].clientY + e.touches[1].clientY) / 2;
      e.preventDefault();
    } else if (e.touches.length === 1) {
      drag.active = true;
      drag.startX = e.touches[0].clientX; drag.startY = e.touches[0].clientY;
      drag.startPanX = panZoom.x; drag.startPanY = panZoom.y;
    }
  }
  function onTouchMove(e) {
    if (e.touches.length === 2 && lastTouchDist) {
      var dx = e.touches[0].clientX - e.touches[1].clientX;
      var dy = e.touches[0].clientY - e.touches[1].clientY;
      var dist = Math.sqrt(dx * dx + dy * dy);
      var factor = dist / lastTouchDist;
      var container = document.getElementById('mindmap-container');
      var rect = container.getBoundingClientRect();
      var mx = (e.touches[0].clientX + e.touches[1].clientX) / 2 - rect.left;
      var my = (e.touches[0].clientY + e.touches[1].clientY) / 2 - rect.top;
      var oldScale = panZoom.scale;
      panZoom.scale = Math.max(panZoom.minScale, Math.min(panZoom.maxScale, panZoom.scale * factor));
      panZoom.x = mx - (mx - panZoom.x) * (panZoom.scale / oldScale);
      panZoom.y = my - (my - panZoom.y) * (panZoom.scale / oldScale);
      lastTouchDist = dist;
      applyTransform();
      e.preventDefault();
    } else if (e.touches.length === 1 && drag.active) {
      panZoom.x = drag.startPanX + (e.touches[0].clientX - drag.startX);
      panZoom.y = drag.startPanY + (e.touches[0].clientY - drag.startY);
      applyTransform();
      e.preventDefault();
    }
  }
  function onTouchEnd(e) {
    if (e.touches.length < 2) lastTouchDist = 0;
    if (e.touches.length === 0) drag.active = false;
  }

  // Double-click to zoom in on area
  function onDblClick(e) {
    var container = document.getElementById('mindmap-container');
    var rect = container.getBoundingClientRect();
    var mx = e.clientX - rect.left, my = e.clientY - rect.top;
    var oldScale = panZoom.scale;
    panZoom.scale = Math.min(panZoom.maxScale, panZoom.scale * 1.5);
    panZoom.x = mx - (mx - panZoom.x) * (panZoom.scale / oldScale);
    panZoom.y = my - (my - panZoom.y) * (panZoom.scale / oldScale);
    applyTransform();
  }

  // === Node click → breadcrumb path ===
  function setupNodeClicks() {
    var container = document.getElementById('mindmap-container');
    var svg = container.querySelector('svg');
    if (!svg) return;
    var breadcrumb = document.getElementById('mindmap-breadcrumb');

    // Find all text elements in the mindmap
    var texts = svg.querySelectorAll('text, .mindmap-node');
    texts.forEach(function(el) {
      el.style.cursor = 'pointer';
      el.addEventListener('click', function(e) {
        e.stopPropagation();
        // Get the text content of the clicked node
        var nodeText = el.textContent.trim();
        if (!nodeText) return;

        // Find path in the mermaid source
        var path = findNodePath(nodeText);
        if (path) {
          breadcrumb.textContent = path;
          breadcrumb.classList.add('visible');
          // Highlight the node
          svg.querySelectorAll('.node-highlight').forEach(function(h) { h.remove(); });
          var bbox = el.getBBox ? el.getBBox() : el.getBoundingClientRect();
          if (el.getBBox) {
            var highlight = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            highlight.setAttribute('x', bbox.x - 4);
            highlight.setAttribute('y', bbox.y - 2);
            highlight.setAttribute('width', bbox.width + 8);
            highlight.setAttribute('height', bbox.height + 4);
            highlight.setAttribute('rx', '3');
            highlight.setAttribute('fill', 'rgba(29,78,216,0.15)');
            highlight.setAttribute('stroke', '#1d4ed8');
            highlight.setAttribute('stroke-width', '1.5');
            highlight.classList.add('node-highlight');
            el.parentNode.insertBefore(highlight, el);
          }
          // Auto-hide after 4s
          clearTimeout(breadcrumb._timer);
          breadcrumb._timer = setTimeout(function() {
            breadcrumb.classList.remove('visible');
            svg.querySelectorAll('.node-highlight').forEach(function(h) { h.remove(); });
          }, 4000);
        }
      });
    });

    // Click background to dismiss breadcrumb
    container.addEventListener('click', function(e) {
      if (!e.target.closest('text, .mindmap-node')) {
        breadcrumb.classList.remove('visible');
        svg.querySelectorAll('.node-highlight').forEach(function(h) { h.remove(); });
      }
    });
  }

  // Find node path from mermaid source
  var currentDisplayCode = '';
  function findNodePath(nodeText) {
    if (!currentDisplayCode) return null;
    var lines = currentDisplayCode.split('\n');
    var bodyLines = [], inH = true;
    for (var i = 0; i < lines.length; i++) {
      var s = lines[i].trim();
      if (inH && (s.indexOf('%%{') === 0 || s === 'mindmap' || s.indexOf('root(') !== -1)) continue;
      inH = false;
      bodyLines.push(lines[i]);
    }
    // Parse to find the node
    var nodes = [];
    for (var i = 0; i < bodyLines.length; i++) {
      if (!bodyLines[i].trim()) continue;
      var content = bodyLines[i].replace(/^\s+/, '');
      var indent = bodyLines[i].length - content.length;
      // Clean mermaid node syntax: root((text)), ((text)), (text), [text], etc.
      var clean = content.replace(/^root\(\(/, '').replace(/\)\)$/, '')
        .replace(/^\(\(/, '').replace(/\)\)$/, '')
        .replace(/^\(/, '').replace(/\)$/, '')
        .replace(/^\[/, '').replace(/\]$/, '')
        .replace(/^\{/, '').replace(/\}$/, '');
      nodes.push({ level: Math.floor(indent / 2), text: clean, raw: content });
    }
    // Find matching node
    var matchIdx = -1;
    for (var i = 0; i < nodes.length; i++) {
      if (nodes[i].text === nodeText || nodes[i].raw.indexOf(nodeText) !== -1) {
        matchIdx = i; break;
      }
    }
    if (matchIdx === -1) return null;
    // Build path from root
    var path = [nodes[matchIdx].text];
    var targetLevel = nodes[matchIdx].level;
    for (var j = matchIdx - 1; j >= 0; j--) {
      if (nodes[j].level < targetLevel) {
        path.unshift(nodes[j].text);
        targetLevel = nodes[j].level;
      }
    }
    return 'knowledge / ' + path.join(' / ');
  }

  // === Bind events ===
  function bindEvents() {
    var container = document.getElementById('mindmap-container');
    container.addEventListener('mousedown', onMouseDown);
    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
    container.addEventListener('wheel', onWheel, { passive: false });
    container.addEventListener('dblclick', onDblClick);
    container.addEventListener('touchstart', onTouchStart, { passive: false });
    container.addEventListener('touchmove', onTouchMove, { passive: false });
    container.addEventListener('touchend', onTouchEnd);
  }

  // === Load ===
  window.loadMindmap = function() {
    var container = document.getElementById('mindmap-container');
    var status = document.getElementById('mindmap-status');
    var viewSelect = document.getElementById('mindmap-view');
    var mode = viewSelect ? viewSelect.value : 'normal';

    container.innerHTML = '<div class="loading">Loading mindmap...</div>' +
      '<div class="mindmap-breadcrumb" id="mindmap-breadcrumb"></div>' +
      '<div class="zoom-indicator" id="zoom-indicator">100%</div>';
    status.textContent = 'Fetching from GitHub...';

    Promise.all([fetchMindmap(), fetchConfig()])
      .then(function(results) {
        var mermaidCode = results[0];
        var config = results[1];
        var displayCode = (mode === 'full') ? mermaidCode : filterMindmap(mermaidCode, config);
        currentDisplayCode = displayCode;

        // Reset pan/zoom
        panZoom.x = 0; panZoom.y = 0; panZoom.scale = 1;

        container.innerHTML = '<div class="mermaid">' + displayCode + '</div>' +
          '<div class="mindmap-breadcrumb" id="mindmap-breadcrumb"></div>' +
          '<div class="zoom-indicator" id="zoom-indicator">100%</div>';
        status.textContent = 'Rendering (' + mode + ')...';

        function tryRender() {
          if (window.mermaid) {
            mermaid.run({ nodes: container.querySelectorAll('.mermaid') }).then(function() {
              // Remove mermaid wrapper, keep SVG directly in container
              var svg = container.querySelector('svg');
              if (svg) {
                svg.style.width = ''; svg.style.height = '';
                svg.removeAttribute('style');
              }
              var nodeCount = displayCode.split('\n').filter(function(l) {
                return l.trim() && !l.trim().match(/^(%%|mindmap$|root\()/);
              }).length;
              status.textContent = mode.charAt(0).toUpperCase() + mode.slice(1) + ' — ' +
                nodeCount + ' nodes — ' + new Date().toLocaleTimeString();
              // Fit after render
              setTimeout(function() { zoomFit(); setupNodeClicks(); }, 100);
            });
          } else {
            var script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js';
            script.onload = function() {
              mermaid.initialize({ startOnLoad: false, theme: 'default', mindmap: { useMaxWidth: true } });
              mermaid.run({ nodes: container.querySelectorAll('.mermaid') }).then(function() {
                var svg = container.querySelector('svg');
                if (svg) { svg.style.width = ''; svg.style.height = ''; svg.removeAttribute('style'); }
                status.textContent = mode.charAt(0).toUpperCase() + mode.slice(1) + ' — ' +
                  new Date().toLocaleTimeString();
                setTimeout(function() { zoomFit(); setupNodeClicks(); }, 100);
              });
            };
            document.head.appendChild(script);
          }
        }
        tryRender();
      })
      .catch(function(err) {
        container.innerHTML = '<div class="mindmap-error"><p>Error: ' + err.message + '</p></div>';
        status.textContent = 'Error';
      });
  };

  window.toggleFullscreen = function() {
    var container = document.getElementById('mindmap-container');
    if (document.fullscreenElement) document.exitFullscreen();
    else container.requestFullscreen();
  };

  // Init
  bindEvents();
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadMindmap);
  } else {
    loadMindmap();
  }
})();
</script>
{:/nomarkdown}
