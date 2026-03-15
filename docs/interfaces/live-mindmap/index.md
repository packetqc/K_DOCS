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
.mindmap-controls button {
  background: var(--accent, #0055b3);
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.35rem 0.8rem;
  font-size: 0.82rem;
  cursor: pointer;
  font-weight: 500;
}
.mindmap-controls button:hover { opacity: 0.85; }
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
  <button onclick="loadMindmap()">Reload</button>
  <button onclick="toggleFullscreen()">Fullscreen</button>
  <span class="mindmap-status" id="mindmap-status">Loading...</span>
</div>

<div class="mindmap-container" id="mindmap-container">
  <div class="loading">Loading mindmap...</div>
</div>

<script>
(function() {
  // mind_memory.md is outside docs/ — fetch from GitHub raw (works in srcdoc iframes too)
  var RAW_URL = 'https://raw.githubusercontent.com/packetqc/K_DOCS/main/Knowledge/K_MIND/mind/mind_memory.md';

  window.loadMindmap = function() {
    var container = document.getElementById('mindmap-container');
    var status = document.getElementById('mindmap-status');
    container.innerHTML = '<div class="loading">Loading mindmap...</div>';
    status.textContent = 'Fetching from GitHub...';

    fetch(RAW_URL)
      .then(function(r) {
        if (!r.ok) throw new Error('HTTP ' + r.status + ' — cannot load mind_memory.md');
        return r.text();
      })
      .then(function(text) {
        // Extract mermaid code from markdown fences
        var match = text.match(/```mermaid\s*\n([\s\S]*?)```/);
        if (!match) throw new Error('No mermaid block found in mind_memory.md');
        var mermaidCode = match[1].trim();

        container.innerHTML = '<div class="mermaid">' + mermaidCode + '</div>';
        status.textContent = 'Rendering...';

        // Render with mermaid
        if (window.mermaid) {
          mermaid.run({ nodes: container.querySelectorAll('.mermaid') }).then(function() {
            status.textContent = 'Live — ' + new Date().toLocaleTimeString();
          });
        } else {
          // Load mermaid if not already loaded
          var script = document.createElement('script');
          script.src = 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js';
          script.onload = function() {
            mermaid.initialize({ startOnLoad: false, theme: 'default', mindmap: { useMaxWidth: true } });
            mermaid.run({ nodes: container.querySelectorAll('.mermaid') }).then(function() {
              status.textContent = 'Live — ' + new Date().toLocaleTimeString();
            });
          };
          document.head.appendChild(script);
        }
      })
      .catch(function(err) {
        container.innerHTML = '<div class="mindmap-error"><p>Error: ' + err.message + '</p>' +
          '<p>Serve via HTTP server: <code>python3 -m http.server 8000</code></p></div>';
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
