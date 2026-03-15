---
layout: publication
title: "Live Mindmap — K_MIND Knowledge Graph"
description: "Interactive live rendering of the K_MIND memory mindmap. Reads mind_memory.md and renders the mermaid mindmap in real-time."
permalink: /interfaces/live-mindmap/
lang: en
header_title: "Live Mindmap"
tagline: "K_MIND Knowledge Graph — Real-Time"
pub_meta: "Interface | K_DOCS"
pub_version: "v1"
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
  overflow: auto;
  border: 1px solid var(--border, #d48a3c);
  border-radius: 8px;
  background: var(--bg, #faf6f1);
  padding: 1rem;
  position: relative;
}
.mindmap-container svg {
  width: 100% !important;
  height: auto !important;
  max-height: 100%;
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
.mindmap-controls select {
  appearance: auto;
}
.mindmap-controls button:hover,
.mindmap-controls select:hover { opacity: 0.85; }
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
</style>

<h2>K_MIND — Live Knowledge Graph</h2>

<div class="mindmap-controls">
  <select id="mindmap-view" onchange="loadMindmap()">
    <option value="normal">Normal</option>
    <option value="full">Full</option>
  </select>
  <button onclick="loadMindmap()">Reload</button>
  <button onclick="toggleFullscreen()">Fullscreen</button>
  <span class="mindmap-status" id="mindmap-status">Loading...</span>
</div>

<div class="mindmap-container" id="mindmap-container">
  <div class="loading">Loading mindmap...</div>
</div>

<script>
(function() {
  var RAW_BASE = 'https://raw.githubusercontent.com/packetqc/K_DOCS/main/Knowledge/K_MIND/';
  var MIND_URL = RAW_BASE + 'mind/mind_memory.md';
  var CONFIG_URL = RAW_BASE + 'conventions/depth_config.json';

  // Cache
  var cachedMermaid = null;
  var cachedConfig = null;

  function fetchMindmap() {
    if (cachedMermaid) return Promise.resolve(cachedMermaid);
    return fetch(MIND_URL)
      .then(function(r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.text();
      })
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
      .then(function(r) {
        if (!r.ok) throw new Error('Config HTTP ' + r.status);
        return r.json();
      })
      .then(function(cfg) {
        cachedConfig = cfg;
        return cfg;
      })
      .catch(function() {
        // Fallback config if fetch fails
        cachedConfig = { default_depth: 3, omit: ['architecture', 'constraints'], overrides: {} };
        return cachedConfig;
      });
  }

  function filterMindmap(mermaidCode, config) {
    var lines = mermaidCode.split('\n');
    var headerLines = [];
    var bodyLines = [];
    var inHeader = true;

    for (var i = 0; i < lines.length; i++) {
      var stripped = lines[i].trim();
      if (inHeader && (stripped.indexOf('%%{') === 0 || stripped === 'mindmap' || stripped.indexOf('root(') !== -1)) {
        headerLines.push(lines[i]);
      } else {
        inHeader = false;
        bodyLines.push(lines[i]);
      }
    }

    // Parse nodes
    var nodes = [];
    for (var i = 0; i < bodyLines.length; i++) {
      var line = bodyLines[i];
      if (!line.trim()) continue;
      var content = line.replace(/^\s+/, '');
      var indent = line.length - content.length;
      var level = Math.floor(indent / 2);
      nodes.push({ level: level, text: content, lineIdx: i });
    }

    if (!nodes.length) return headerLines.join('\n');

    var rootIndent = nodes[0].level;
    var omit = config.omit || [];
    var overrides = config.overrides || {};
    var defaultDepth = config.default_depth || 3;
    var outputLines = [];

    for (var i = 0; i < nodes.length; i++) {
      var node = nodes[i];
      // Build path
      var pathParts = [];
      var target = node.level;
      for (var j = i; j >= 0; j--) {
        if (nodes[j].level < target) {
          pathParts.unshift(nodes[j].text);
          target = nodes[j].level;
        } else if (j === i) {
          pathParts.push(nodes[j].text);
        }
      }
      var nodePath = pathParts.join('/');
      var topLevel = pathParts[0] || node.text;
      var depthFromTop = node.level - rootIndent + 1;

      // Check omit
      var isOmitted = false;
      for (var k = 0; k < omit.length; k++) {
        if (topLevel === omit[k]) { isOmitted = true; break; }
      }
      if (isOmitted) continue;

      // Find depth limit (longest matching override wins)
      var maxDepth = defaultDepth;
      var bestMatchLen = 0;
      for (var opath in overrides) {
        if (nodePath === opath || nodePath.indexOf(opath + '/') === 0) {
          if (opath.length > bestMatchLen) {
            bestMatchLen = opath.length;
            maxDepth = overrides[opath];
          }
        }
      }

      if (depthFromTop <= maxDepth) {
        outputLines.push(bodyLines[node.lineIdx]);
      }
    }

    return headerLines.join('\n') + '\n' + outputLines.join('\n');
  }

  window.loadMindmap = function() {
    var container = document.getElementById('mindmap-container');
    var status = document.getElementById('mindmap-status');
    var viewSelect = document.getElementById('mindmap-view');
    var mode = viewSelect ? viewSelect.value : 'normal';

    container.innerHTML = '<div class="loading">Loading mindmap...</div>';
    status.textContent = 'Fetching from GitHub...';

    Promise.all([fetchMindmap(), fetchConfig()])
      .then(function(results) {
        var mermaidCode = results[0];
        var config = results[1];

        // Apply filter for normal mode
        var displayCode = (mode === 'full') ? mermaidCode : filterMindmap(mermaidCode, config);

        container.innerHTML = '<div class="mermaid">' + displayCode + '</div>';
        status.textContent = 'Rendering (' + mode + ')...';

        // Render with mermaid
        function tryRender() {
          if (window.mermaid) {
            mermaid.run({ nodes: container.querySelectorAll('.mermaid') }).then(function() {
              var nodeCount = displayCode.split('\n').filter(function(l) {
                return l.trim() && !l.trim().match(/^(%%|mindmap$|root\()/);
              }).length;
              status.textContent = mode.charAt(0).toUpperCase() + mode.slice(1) + ' — ' +
                nodeCount + ' nodes — ' + new Date().toLocaleTimeString();
            });
          } else {
            var script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js';
            script.onload = function() {
              mermaid.initialize({ startOnLoad: false, theme: 'default', mindmap: { useMaxWidth: true } });
              mermaid.run({ nodes: container.querySelectorAll('.mermaid') }).then(function() {
                status.textContent = mode.charAt(0).toUpperCase() + mode.slice(1) + ' — ' +
                  new Date().toLocaleTimeString();
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
    if (document.fullscreenElement) {
      document.exitFullscreen();
    } else {
      container.requestFullscreen();
    }
  };

  // Auto-load on page ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadMindmap);
  } else {
    loadMindmap();
  }
})();
</script>
{:/nomarkdown}
