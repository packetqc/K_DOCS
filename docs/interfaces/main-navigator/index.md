---
layout: publication
page_type: interface
title: "Main Navigator"
description: "Knowledge system main navigation interface: three-panel browser with widget directory, extensible content viewer, and full command reference."
pub_id: "Main Navigator · I2"
version: "v5"
date: "2026-03-15"
permalink: /interfaces/main-navigator/
permalink_fr: /fr/interfaces/main-navigator/
keywords: "interface, navigation, browser, knowledge, dashboard, commands"
og_image: /assets/og/main-navigator-en-cayman.gif
dev_banner: "Interface in development — features and layout may change between sessions."

---

# Main Navigator

{::nomarkdown}
<style>
/* ═══ Hide gradient header + footer only — keep layout chrome ═══ */
.page-header, .site-footer, .pub-crossrefs { display: none !important; }
html { margin: 0; padding: 0; height: 100%; }
body { margin: 0; padding: 0; overflow: hidden; height: 100vh; display: flex; flex-direction: column; }

/* ═══ Discrete thin scrollbars ═══ */
*, *::before, *::after {
  scrollbar-width: thin;
  scrollbar-color: var(--border, #c0c0c0) transparent;
}
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border, #c0c0c0); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--muted, #888); }

/* ═══ Fill viewport as flex column ═══ */
.container {
  padding: 0 !important; margin: 0 !important; max-width: 100% !important;
  flex: 1 !important;
  display: flex !important; flex-direction: column !important;
  min-height: 0 !important;
  overflow: hidden !important;
}

/* Layout chrome keeps natural height at top */
.pub-lang-bar, .dev-banner, .pub-topbar,
.pub-version-banner, .pub-export-toolbar {
  flex-shrink: 0 !important;
  padding-left: 0.75rem !important;
  padding-right: 0.75rem !important;
  transition: max-height 0.25s ease, opacity 0.2s ease, padding 0.25s ease, margin 0.25s ease;
  overflow: hidden !important;
}

/* Page title heading — compact */
.container > h1 {
  flex-shrink: 0 !important;
  margin: 0.3rem 0.75rem !important;
  font-size: 1.4rem !important;
  padding-bottom: 0.2rem !important;
  border-bottom: 1px solid var(--border, #d0d7de) !important;
  transition: max-height 0.25s ease, opacity 0.2s ease, padding 0.25s ease, margin 0.25s ease;
  overflow: hidden !important;
}

/* ═══ Main grid — 5 columns: left(overlay) | div-L | center | div-R | right ═══ */
.nav-grid {
  flex: 1; min-height: 0; display: grid; overflow: hidden;
  position: relative;
  grid-template-columns: 220px 14px 1fr 14px 0px;
  grid-template-rows: 1fr;
  margin: 0.3rem 0.4rem 0.25rem;
  border: 1px solid var(--border, #d0d7de);
  border-radius: 10px;
  background: var(--bg, #fff);
}
.nav-grid.dragging { transition: none; }
.nav-grid:not(.dragging) { transition: grid-template-columns 0.25s ease; }

/* Left nav panel */
.nav-panel {
  grid-column: 1;
  z-index: 20;
  background: var(--code-bg, #f6f8fa);
  overflow-y: auto; overflow-x: hidden;
  border-right: 1px solid var(--border, #d0d7de);
  border-radius: 10px 0 0 10px;
  min-width: 0;
}

/* Divider shared styles — thin draggable bar with grip dots */
.nav-divider-left, .nav-divider-right {
  background: var(--code-bg, #f6f8fa);
  border-left: 1px solid var(--border, #d0d7de);
  border-right: 1px solid var(--border, #d0d7de);
  display: flex; align-items: center; justify-content: center;
  cursor: col-resize; user-select: none;
  transition: background 0.15s ease;
  position: relative;
  min-width: 14px;
  z-index: 10;
}
.nav-divider-left { grid-column: 2; }
.nav-divider-left::before, .nav-divider-right::before {
  content: '·\A·\A·\A·\A·'; white-space: pre; position: absolute; top: 50%; transform: translateY(-50%);
  font-size: 0.75rem; line-height: 0.5; color: var(--muted, #656d76);
}
.nav-divider-left:hover, .nav-divider-right:hover {
  background: var(--col-alt, #e0e8f0);
}

/* Center panel — content viewer (deepest layer) */
.nav-center {
  grid-column: 3;
  background: var(--bg, #fff);
  display: flex; flex-direction: column; min-width: 0;
  overflow: hidden; transition: opacity 0.2s ease;
  z-index: 1;
}
/* Center panel hidden when right takes nearly all space — handled dynamically */
.nav-center iframe { flex: 1; width: 100%; border: none; background: var(--bg, #fff); }

.nav-divider-right { grid-column: 4; z-index: 40; }

/* Right content viewer */
.nav-viewer { grid-column: 5; display: flex; flex-direction: column; min-width: 0; overflow: hidden; z-index: 40; }
.nav-viewer iframe { flex: 1; width: 100%; border: none; background: var(--bg, #fff); }

/* ═══ Widget cards ═══ */
.nav-widget {
  margin: 0.4rem 0.3rem;
  border: 1px solid var(--border, #d0d7de);
  border-radius: 6px; overflow: hidden;
  background: var(--bg, #fff);
}
.nav-widget summary {
  cursor: pointer; padding: 0.35rem 0.5rem;
  font-size: 0.76rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.04em;
  color: var(--fg, #24292f);
  background: var(--code-bg, #f6f8fa);
  border-bottom: 1px solid var(--border, #d0d7de);
  list-style: none;
  display: flex; align-items: center; gap: 0.35rem;
  user-select: none;
}
.nav-widget summary::-webkit-details-marker { display: none; }
.nav-widget summary::before {
  content: '▸'; font-size: 0.7rem;
  transition: transform 0.15s; color: var(--muted, #656d76);
}
.nav-widget[open] > summary::before { transform: rotate(90deg); }
.nav-widget[open] > summary { border-bottom-color: var(--accent, #1d4ed8); }
.nav-widget .widget-body { padding: 0.25rem 0.3rem; display: flex; flex-direction: column; gap: 0.15rem; }
.nav-widget .widget-body a {
  display: block; font-size: 0.72rem; font-weight: 500;
  padding: 0.3rem 0.5rem;
  color: var(--fg, #24292f);
  text-decoration: none; border-radius: 4px;
  text-transform: uppercase; letter-spacing: 0.02em;
  background: var(--code-bg, #f6f8fa);
  border-left: 2px solid transparent;
  transition: background 0.15s, border-color 0.15s, color 0.15s, transform 0.12s, box-shadow 0.15s;
}
.nav-widget .widget-body a:hover {
  background: var(--col-alt, #e8eef4);
  color: var(--accent, #1d4ed8);
  border-left-color: var(--accent, #1d4ed8);
  transform: translateX(3px);
  box-shadow: -2px 0 0 var(--accent, #1d4ed8);
}
.nav-widget .widget-body a.active {
  background: var(--accent, #1d4ed8); color: var(--bg, #fff);
  border-left-color: var(--bg, #fff);
}

/* Sub-groups */
.nav-widget .pub-group {
  margin: 0.1rem 0; padding: 0;
  background: var(--code-bg, #f6f8fa);
  border-radius: 4px; border: 1px solid var(--border, #d0d7de);
}
.nav-widget .pub-group summary {
  font-size: 0.72rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.02em;
  padding: 0.3rem 0.5rem;
  background: none; border-bottom: none;
  color: var(--fg, #24292f);
  border-radius: 4px;
  transition: background 0.15s;
}
.nav-widget .pub-group summary:hover { background: var(--col-alt, #e8eef4); transform: translateX(2px); }
.nav-widget .pub-group summary::before { content: '›'; font-size: 0.8rem; }
.nav-widget .pub-group[open] > summary::before { content: '⌄'; }
.nav-widget .pub-group[open] > summary { border-bottom: 1px solid var(--border, #d0d7de); border-radius: 4px 4px 0 0; }
.nav-widget .pub-group a {
  padding-left: 1.1rem; font-size: 0.7rem;
  background: transparent; border-left: none;
}
.nav-widget .pub-group a:hover { background: var(--col-alt, #e8eef4); border-left: none; transform: translateX(2px); box-shadow: none; }
.cmd-link { font-family: monospace; font-size: 0.68rem; color: var(--muted, #656d76); letter-spacing: 0; }

/* ═══ Tab bar — horizontal strip above content-frame ═══ */
.tab-bar {
  flex-shrink: 0;
  display: flex; align-items: stretch;
  overflow-x: auto; overflow-y: hidden;
  background: var(--code-bg, #f6f8fa);
  border-bottom: 1px solid var(--border, #d0d7de);
  scrollbar-width: thin;
}
.tab-bar:empty { display: none; }
.tab-item {
  display: flex; align-items: center; gap: 0.15rem;
  padding: 0.2rem 0.25rem 0.2rem 0.5rem;
  font-size: 0.72rem; white-space: nowrap;
  border-right: 1px solid var(--border, #d0d7de);
  cursor: pointer; user-select: none;
  color: var(--muted, #656d76);
  max-width: 180px;
  transition: background 0.15s;
}
.tab-item:hover { background: var(--col-alt, #f0f0f0); color: var(--fg, #24292f); }
.tab-item.tab-active {
  background: var(--bg, #fff); color: var(--fg, #24292f);
  font-weight: 600;
  border-bottom: 2px solid var(--accent, #1d4ed8);
}
.tab-label {
  overflow: hidden; text-overflow: ellipsis;
  max-width: 140px; display: inline-block;
}
.tab-close {
  font-size: 0.6rem; padding: 0.1rem 0.25rem;
  color: var(--muted, #656d76); border-radius: 3px;
  line-height: 1; cursor: pointer;
}
.tab-close:hover { background: #e5534b; color: #fff; }

/* ═══ Interface row — link + ℹ button ═══ */
.iface-row {
  display: flex; align-items: center;
  background: var(--code-bg, #f6f8fa);
  border-radius: 4px;
  border-left: 2px solid transparent;
  transition: background 0.15s, border-color 0.15s, transform 0.12s, box-shadow 0.15s;
}
.iface-row:hover {
  background: var(--col-alt, #e8eef4);
  border-left-color: var(--accent, #1d4ed8);
  transform: translateX(3px);
  box-shadow: -2px 0 0 var(--accent, #1d4ed8);
}
.iface-row > a:first-child {
  flex: 1; background: transparent !important;
  border-left: none !important; border-radius: 0 !important;
}
.iface-row > a:first-child:hover { background: transparent !important; border-left: none !important; }
.iface-pub-btn {
  flex-shrink: 0; padding: 0.2rem 0.4rem;
  font-size: 0.7rem; text-decoration: none;
  color: var(--muted, #656d76); border-radius: 3px;
  cursor: pointer; opacity: 0.4;
  transition: opacity 0.15s, color 0.15s;
}
.iface-pub-btn:hover {
  opacity: 1; color: var(--accent, #1d4ed8);
}

/* ═══ Dark theme overrides for widgets ═══ */
[data-theme="midnight"],
[data-theme="daltonism-dark"],
[data-color-mode="dark"],
.theme-dark {
  --fg: #c9d1d9;
  --bg: #0d1117;
  --code-bg: #161b22;
  --border: #30363d;
  --muted: #8b949e;
  --accent: #58a6ff;
  --col-alt: #1c2128;
}
@media (prefers-color-scheme: dark) {
  :root {
    --fg: #c9d1d9;
    --bg: #0d1117;
    --code-bg: #161b22;
    --border: #30363d;
    --muted: #8b949e;
    --accent: #58a6ff;
    --col-alt: #1c2128;
  }
}

/* ═══ Mobile — shrink dividers for touch screens ═══ */
@media (max-width: 768px) {
  .nav-divider-left, .nav-divider-right { min-width: 8px; }
  .nav-divider-left::before, .nav-divider-right::before { font-size: 0.55rem; }
  .nav-grid { grid-template-columns: 0px 8px 1fr 8px 0px; }
}

/* ═══ Print / PDF export — center panel content after cover page ═══ */
@media print {
  html, body { height: auto !important; overflow: visible !important; }
  body { display: block !important; }
  .container { display: block !important; overflow: visible !important; max-width: 100% !important; }
  /* Hide interactive chrome — left panel, dividers, right panel, chrome bar */
  .nav-panel, .nav-divider-left, .nav-divider-right,
  .nav-viewer, .page-url-link { display: none !important; }
  /* Un-lock the grid for flow layout */
  .nav-grid {
    display: block !important; overflow: visible !important;
    border: none !important; margin: 0 !important;
    height: auto !important; min-height: 0 !important;
  }
  /* Center panel — show full width, iframe stretches to content */
  .nav-center {
    display: block !important; width: 100% !important;
    overflow: visible !important; opacity: 1 !important;
  }
  .nav-center iframe {
    width: 100% !important; height: auto !important;
    min-height: 80vh; border: none !important;
  }
}
</style>

<!-- MAIN GRID -->
<div class="nav-grid" id="nav-grid">
  <div class="nav-panel" id="left-panel"></div>
  <div class="nav-divider-left" id="left-toggle"></div>
  <div class="nav-center" id="center-panel">
    <iframe name="center-frame" id="center-frame-el"></iframe>
  </div>
  <div class="nav-divider-right" id="right-toggle"></div>
  <div class="nav-viewer" id="right-viewer">
    <div class="tab-bar" id="tab-bar"></div>
    <iframe name="content-frame" id="right-frame-el"></iframe>
  </div>
</div>

<script>
(function() {
  /* ─── Language auto-detection from URL path ─── */
  var LANG = (document.documentElement.lang === 'fr' || window.location.pathname.indexOf('/fr/') >= 0) ? 'fr' : 'en';
  var LP = LANG === 'fr' ? '/fr' : '';  // language path prefix
  // localStorage keys are language-neutral (shared across EN/FR)

  /* All translations are now in docs/data/<section>.json — no hardcoded T block needed */

  var BASE = '{{ "" | relative_url }}';
  var CENTER_KEY  = 'navigator-center-url';
  var WIDGET_KEY  = 'navigator-widgets';
  var LPANEL_KEY  = 'navigator-left-state';
  var RPANEL_KEY  = 'navigator-right-state';
  var RCONTENT_KEY = 'navigator-right-url';
  var ACTIVE_KEY  = 'navigator-active-href';
  var SUBDET_KEY  = 'navigator-subdetails';

  /* Set default iframe sources based on language */
  var centerIframe = document.getElementById('center-frame-el');
  var rightIframe  = document.getElementById('right-frame-el');
  centerIframe.src = BASE + LP + '/interfaces/task-workflow/';
  rightIframe.src  = BASE + LP + '/';

  var panel  = document.getElementById('left-panel');
  var grid   = document.getElementById('nav-grid');
  var lToggle = document.getElementById('left-toggle');
  var rToggle = document.getElementById('right-toggle');
  if (!panel || !grid) return;

  /* ─── Panel sizes — draggable + click-to-step ─── */
  var DIVIDER_W = (window.innerWidth <= 768) ? 8 : 14;
  var LEFT_STEPS = [0, 220, 320];
  var savedLeft = parseInt(localStorage.getItem(LPANEL_KEY) || '220');
  var savedRight = parseInt(localStorage.getItem(RPANEL_KEY) || '0');
  var leftW = savedLeft;
  var rightW = savedRight;

  function applyGrid(animate) {
    if (!animate) grid.classList.add('dragging');
    else grid.classList.remove('dragging');
    grid.style.gridTemplateColumns = leftW + 'px ' + DIVIDER_W + 'px 1fr ' + DIVIDER_W + 'px ' + rightW + 'px';
    localStorage.setItem(LPANEL_KEY, String(leftW));
    localStorage.setItem(RPANEL_KEY, String(rightW));
  }
  applyGrid(false);
  requestAnimationFrame(function() { grid.classList.remove('dragging'); });

  /* ─── Drag logic (shared) ─── */
  function makeDraggable(divider, getSetter) {
    var startX, dragged;
    divider.addEventListener('mousedown', function(e) {
      e.preventDefault();
      startX = e.clientX;
      dragged = false;
      var setter = getSetter();
      var overlay = document.createElement('div');
      overlay.style.cssText = 'position:fixed;inset:0;z-index:9999;cursor:col-resize;';
      document.body.appendChild(overlay);
      grid.classList.add('dragging');

      function onMove(ev) {
        var dx = ev.clientX - startX;
        if (Math.abs(dx) > 3) dragged = true;
        setter(dx);
        applyGrid(false);
      }
      function onUp() {
        document.removeEventListener('mousemove', onMove);
        document.removeEventListener('mouseup', onUp);
        overlay.remove();
        grid.classList.remove('dragging');
        if (!dragged) {
          setter('step');
          applyGrid(true);
        }
      }
      document.addEventListener('mousemove', onMove);
      document.addEventListener('mouseup', onUp);
    });
  }

  /* Left divider: drag resizes left panel, click cycles steps */
  var leftStepIdx = LEFT_STEPS.indexOf(leftW) >= 0 ? LEFT_STEPS.indexOf(leftW) : 1;
  makeDraggable(lToggle, function() {
    var startW = leftW;
    return function(dx) {
      if (dx === 'step') {
        leftStepIdx = (leftStepIdx + 1) % LEFT_STEPS.length;
        leftW = LEFT_STEPS[leftStepIdx];
      } else {
        leftW = Math.max(0, Math.min(startW + dx, grid.offsetWidth * 0.5));
      }
    };
  });

  /* Right divider: drag resizes right panel, click cycles 0 → 50% → full → 0 */
  makeDraggable(rToggle, function() {
    var startW = rightW;
    return function(dx) {
      if (dx === 'step') {
        var gw = grid.offsetWidth;
        if (rightW < gw * 0.25) rightW = Math.round(gw * 0.5);
        else if (rightW < gw * 0.75) rightW = gw - leftW - DIVIDER_W * 2;
        else rightW = 0;
      } else {
        rightW = Math.max(0, Math.min(startW - dx, grid.offsetWidth - leftW - DIVIDER_W * 2 - 50));
      }
    };
  });

  /* ─── Widget definitions — bilingual, driven by LANG ─── */
  /* Section registry — fetched from Knowledge/sections.json (priority descending: higher = first).
     Fallback to hardcoded list if fetch fails.
     See Knowledge/K_DOCS/conventions/web/json-driven-panels.md */
  var SECTIONS_URL = 'https://raw.githubusercontent.com/packetqc/knowledge/main/Knowledge/sections.json';
  var FALLBACK_WIDGETS = [
    { id:'interfaces',json:'data/interfaces.json',priority:1 },
    { id:'documentation',json:'data/documentation.json',priority:2 },
    { id:'essentials',json:'data/essentials.json',priority:3 },
    { id:'commands',json:'data/commands.json',priority:4 },
    { id:'methodologies',json:'data/methodologies.json',priority:5 },
    { id:'hubs',json:'data/hubs.json',priority:6 },
    { id:'profile',json:'data/profile.json',priority:7 },
    { id:'publications',json:'data/publications.json',priority:8 },
    { id:'stories',json:'data/stories.json',priority:9 },
    { id:'configurations',json:'data/configurations.json',priority:10 }
  ];

  /* ─── Restore + build widgets ─── */
  var savedState = {};
  try { savedState = JSON.parse(localStorage.getItem(WIDGET_KEY) || '{}'); } catch(e) {}

  function saveWidgetState() {
    var st = {};
    panel.querySelectorAll('.nav-widget').forEach(function(w) { st[w.dataset.wid] = w.open; });
    localStorage.setItem(WIDGET_KEY, JSON.stringify(st));
  }
  /* Sub-details (pub-group) state */
  var savedSubDet = {};
  try { savedSubDet = JSON.parse(localStorage.getItem(SUBDET_KEY) || '{}'); } catch(e) {}
  function saveSubDetState() {
    var st = {};
    panel.querySelectorAll('.pub-group').forEach(function(d,i) { st[i] = d.open; });
    localStorage.setItem(SUBDET_KEY, JSON.stringify(st));
  }
  var subDetIndex = 0;
  var navLinkId = 0;

  /* JSON-driven panel sections — see Knowledge/K_DOCS/conventions/web/json-driven-panels.md
     All widgets are fetched from docs/data/<section>.json at runtime. */
  var vru = (typeof viewerRewriteUrl === 'function') ? viewerRewriteUrl : function(u) { return u; };

  function label(item) { return (LANG === 'fr' && item.title_fr) ? item.title_fr : item.title; }

  function makeSubDet(summaryText) {
    var idx = subDetIndex++;
    var pg = document.createElement('details'); pg.className = 'pub-group';
    if (savedSubDet[idx] !== undefined) pg.open = savedSubDet[idx];
    pg.addEventListener('toggle', saveSubDetState);
    var pgsm = document.createElement('summary'); pgsm.textContent = summaryText; pg.appendChild(pgsm);
    return pg;
  }

  function makeLink(text, href, target) {
    var a = document.createElement('a');
    a.href = href; a.dataset.navId = 'nav-' + (navLinkId++);
    a.target = target || 'content-frame'; a.textContent = text;
    return a;
  }

  function buildWidgets(widgets) {
    /* Sort by priority ascending (lower = first) */
    widgets.sort(function(a, b) { return (a.priority || 99) - (b.priority || 99); });
    widgets.forEach(function(w) {
    var det = document.createElement('details');
    det.className = 'nav-widget'; det.dataset.wid = w.id;
    det.open = (savedState[w.id] !== undefined) ? savedState[w.id] : false;
    det.addEventListener('toggle', saveWidgetState);
    var sm = document.createElement('summary'); sm.textContent = w.id; det.appendChild(sm);
    var body = document.createElement('div'); body.className = 'widget-body';
    det.appendChild(body); panel.appendChild(det);

    fetch(vru(BASE + '/' + w.json))
      .then(function(r) { return r.json(); })
      .then(function(data) {
        /* Section-level metadata */
        sm.textContent = (LANG === 'fr' && data.title_fr) ? data.title_fr : data.title;
        if (data.open && savedState[w.id] === undefined) det.open = true;

        var items = (data.items || []).slice().sort(function(a, b) { return (a.priority || 99) - (b.priority || 99); });
        var section = data.section;

        /* ── Interfaces: links with target routing + ℹ guide button ── */
        if (section === 'interfaces') {
          items.forEach(function(item) {
            var target = item.target === 'top' ? '_top' : (item.target === 'center' ? 'center-frame' : 'content-frame');
            var href = item.target === 'top' ? vru(BASE + LP + item.href, false) : vru(BASE + LP + item.href);
            if (item.pub) {
              var row = document.createElement('div'); row.className = 'iface-row';
              row.appendChild(makeLink(label(item), href, target));
              var ib = document.createElement('a'); ib.className = 'iface-pub-btn';
              ib.textContent = 'ℹ'; ib.title = LANG === 'fr' ? 'Guide utilisateur' : 'User Guide';
              ib.href = BASE + LP + '/publications/' + item.pub + '/full/';
              ib.target = 'content-frame';
              row.appendChild(ib);
              body.appendChild(row);
            } else {
              body.appendChild(makeLink(label(item), href, target));
            }
          });
        }

        /* ── Documentation: groups with summary+full sub-links ── */
        else if (section === 'documentation') {
          var dSumLabel = LANG === 'fr' ? 'Résumé' : 'Summary';
          var dFullLabel = LANG === 'fr' ? 'Complet' : 'Full';
          var dComingSoon = LANG === 'fr' ? '(à venir)' : '(coming soon)';
          (data.groups || []).forEach(function(g) {
            var gLabel = (LANG === 'fr' && g.group_fr) ? g.group_fr : g.group;
            var pg = makeSubDet(gLabel);
            if (g.items && g.items.length > 0) {
              g.items.slice().sort(function(a, b) { return (a.priority || 99) - (b.priority || 99); }).forEach(function(item) {
                var ipg = makeSubDet(label(item));
                ipg.appendChild(makeLink(dSumLabel, vru(BASE + LP + '/publications/' + item.slug + '/'), 'content-frame'));
                ipg.appendChild(makeLink(dFullLabel, vru(BASE + LP + '/publications/' + item.slug + '/full/'), 'content-frame'));
                pg.appendChild(ipg);
              });
            } else {
              var ph = document.createElement('span');
              ph.style.cssText = 'display:block;padding:0.2rem 0.55rem;font-size:0.72rem;color:var(--muted,#656d76);font-style:italic;';
              ph.textContent = dComingSoon;
              pg.appendChild(ph);
            }
            body.appendChild(pg);
          });
        }

        /* ── Simple link lists: essentials, hubs, profile, stories ── */
        else if (section === 'essentials' || section === 'hubs' || section === 'profile' || section === 'stories') {
          items.forEach(function(item) {
            body.appendChild(makeLink(label(item), vru(BASE + LP + item.href), 'content-frame'));
          });
        }

        /* ── Commands: grouped with pub link + cmd spans ── */
        else if (section === 'commands') {
          items.forEach(function(cg) {
            var gLabel = (LANG === 'fr' && cg.group_fr) ? cg.group_fr : cg.group;
            var pg = makeSubDet(gLabel);
            cg.cmds.forEach(function(cmd) {
              var a = makeLink('', vru(BASE + LP + cg.pub), 'content-frame');
              var sp = document.createElement('span'); sp.className = 'cmd-link'; sp.textContent = cmd;
              a.appendChild(sp); pg.appendChild(a);
            });
            body.appendChild(pg);
          });
        }

        /* ── Publications: summary + full sub-links ── */
        else if (section === 'publications') {
          var sumLabel = (LANG === 'fr' && data.summary_label_fr) ? data.summary_label_fr : (data.summary_label || 'Summary');
          var fullLabel = (LANG === 'fr' && data.full_label_fr) ? data.full_label_fr : (data.full_label || 'Full');
          items.forEach(function(p) {
            var pg = makeSubDet(p.number + ' ' + label(p));
            pg.appendChild(makeLink(sumLabel, vru(BASE + LP + '/publications/' + p.slug + '/'), 'content-frame'));
            pg.appendChild(makeLink(fullLabel, vru(BASE + LP + '/publications/' + p.slug + '/full/'), 'content-frame'));
            if (p.extra) { p.extra.forEach(function(e) {
              var eLabel = (LANG === 'fr' && e.title_fr) ? e.title_fr : e.title;
              pg.appendChild(makeLink(eLabel, vru(BASE + LP + e.href), 'content-frame'));
            }); }
            body.appendChild(pg);
          });
        }

        /* ── Module-grouped sections (methodologies, configurations, etc.) ── */
        else if (section === 'methodologies' || section === 'configurations' || (items[0] && items[0].module)) {
          var groups = {};
          items.forEach(function(item) {
            var mod = item.module || 'General';
            if (!groups[mod]) groups[mod] = [];
            groups[mod].push(item);
          });
          Object.keys(groups).forEach(function(mod) {
            var pg = makeSubDet(mod);
            /* "View All" composite link — loads all group items as one page */
            var jsonItems = groups[mod].filter(function(i) { return i.path && i.path.match(/\.json([?#]|$)/i); });
            if (jsonItems.length > 1) {
              var docsParam = jsonItems.map(function(i) { return encodeURIComponent(i.path); }).join('|');
              pg.appendChild(makeLink(LANG === 'fr' ? '▸ Tout voir' : '▸ View All', vru(BASE + '/index.html?docs=' + docsParam + '&embed'), 'content-frame'));
            }
            groups[mod].forEach(function(item) {
              pg.appendChild(makeLink(label(item), vru(BASE + '/index.html?doc=' + encodeURIComponent(item.path) + '&embed'), 'content-frame'));
            });
            body.appendChild(pg);
          });
        }

        /* ── Fallback: flat link list ── */
        else {
          items.forEach(function(item) {
            var href = item.href ? vru(BASE + LP + item.href) : (item.path ? vru(BASE + '/index.html?doc=' + encodeURIComponent(item.path) + '&embed') : '#');
            body.appendChild(makeLink(label(item), href, 'content-frame'));
          });
        }
      })
      .catch(function(e) { console.warn('Failed to load ' + w.json, e); });
    });
  }

  /* Fetch sections.json then build, fallback to hardcoded */
  fetch(SECTIONS_URL)
    .then(function(r) { return r.json(); })
    .then(function(data) { buildWidgets(data.sections || []); })
    .catch(function() { buildWidgets(FALLBACK_WIDGETS); });

  /* ─── Language-neutral URL helpers ─── */
  function stripLang(url) {
    if (!url) return url;
    // Viewer embed URLs: strip &lang=fr parameter
    if (url.indexOf('index.html?doc=') !== -1) {
      return url.replace(/[&?]lang=fr/g, '').replace(/\?&/, '?').replace(/\?$/, '');
    }
    // Direct page URLs: strip /fr/ prefix
    return url.replace(BASE + '/fr/', BASE + '/').replace(/\/fr\//, '/');
  }
  function applyLang(url) {
    if (!url || LANG === 'en') return url;
    // Viewer embed URLs: add &lang=fr parameter
    if (url.indexOf('index.html?doc=') !== -1) {
      return url + (url.indexOf('?') !== -1 ? '&' : '?') + 'lang=fr';
    }
    // Direct page URLs: add /fr/ prefix
    return url.replace(BASE + '/', BASE + '/fr/');
  }

  /* ─── Tab bar manager ─── */
  var TAB_KEY = 'navigator-tabs';
  var TAB_MAX = 12;
  var tabBar = document.getElementById('tab-bar');
  var tabs = [];
  var activeTabId = null;
  var tabCounter = 0;
  var tabNavigating = false; /* flag to suppress iframe-load tab creation during programmatic nav */

  function normUrl(u) {
    try { var p = new URL(u, location.origin); return p.origin + p.pathname.replace(/\/+$/, ''); }
    catch(e) { return u.split('#')[0].replace(/\/+$/, ''); }
  }

  function renderTabs() {
    if (!tabBar) return;
    tabBar.innerHTML = '';
    tabs.forEach(function(t) {
      var el = document.createElement('span');
      el.className = 'tab-item' + (t.id === activeTabId ? ' tab-active' : '');
      el.dataset.tabId = t.id;
      var lbl = document.createElement('span');
      lbl.className = 'tab-label'; lbl.textContent = t.title || 'Document';
      lbl.title = t.title || '';
      el.appendChild(lbl);
      var cls = document.createElement('span');
      cls.className = 'tab-close'; cls.textContent = '×'; cls.dataset.tabId = t.id;
      el.appendChild(cls);
      tabBar.appendChild(el);
    });
  }

  function saveTabState() {
    try {
      localStorage.setItem(TAB_KEY, JSON.stringify({ tabs: tabs, activeTabId: activeTabId, counter: tabCounter }));
    } catch(e) {}
  }

  function activateTab(id) {
    var t = tabs.find(function(x) { return x.id === id; });
    if (!t) return;
    activeTabId = id;
    tabNavigating = true;
    if (rightIframe) rightIframe.src = applyLang(t.url);
    localStorage.setItem(RCONTENT_KEY, stripLang(t.url));
    /* Auto-extend right panel if collapsed */
    if (rightW < 100) { rightW = Math.round(grid.offsetWidth * 0.5); applyGrid(true); }
    renderTabs();
    saveTabState();
  }

  function addTab(url, title) {
    var norm = normUrl(url);
    var existing = tabs.find(function(t) { return normUrl(t.url) === norm; });
    if (existing) {
      if (title && title !== 'Document') existing.title = title;
      activateTab(existing.id);
      return;
    }
    /* Soft cap — close oldest non-active */
    if (tabs.length >= TAB_MAX) {
      var oldest = tabs.find(function(t) { return t.id !== activeTabId; });
      if (oldest) tabs = tabs.filter(function(t) { return t.id !== oldest.id; });
    }
    var id = 'tab-' + (++tabCounter);
    tabs.push({ id: id, title: title || 'Document', url: stripLang(url) });
    activateTab(id);
  }

  function closeTab(id) {
    var idx = tabs.findIndex(function(t) { return t.id === id; });
    if (idx < 0) return;
    tabs.splice(idx, 1);
    if (activeTabId === id) {
      if (tabs.length > 0) {
        var next = tabs[Math.min(idx, tabs.length - 1)];
        activateTab(next.id);
      } else {
        activeTabId = null;
        renderTabs();
        saveTabState();
      }
    } else {
      renderTabs();
      saveTabState();
    }
  }

  /* Tab bar click delegation */
  if (tabBar) {
    tabBar.addEventListener('click', function(e) {
      var cls = e.target.closest('.tab-close');
      if (cls) { closeTab(cls.dataset.tabId); return; }
      var item = e.target.closest('.tab-item');
      if (item) activateTab(item.dataset.tabId);
    });
  }

  /* ─── Restore last viewed pages ─── */
  var vruFn = (typeof viewerRewriteUrl === 'function') ? viewerRewriteUrl : function(u) { return u; };
  var savedCenter = localStorage.getItem(CENTER_KEY);
  var defaultCenter = vruFn(BASE + LP + '/interfaces/task-workflow/');
  if (centerIframe) { centerIframe.src = savedCenter ? applyLang(savedCenter) : defaultCenter; }

  /* Restore tabs or fall back to single URL */
  try {
    var tabData = JSON.parse(localStorage.getItem(TAB_KEY) || 'null');
    if (tabData && tabData.tabs && tabData.tabs.length > 0) {
      tabs = tabData.tabs;
      tabCounter = tabData.counter || tabs.length;
      activeTabId = tabData.activeTabId;
      var activeTab = tabs.find(function(t) { return t.id === activeTabId; });
      if (activeTab && rightIframe) {
        tabNavigating = true;
        rightIframe.src = applyLang(activeTab.url);
        localStorage.setItem(RCONTENT_KEY, stripLang(activeTab.url));
      }
      renderTabs();
    } else {
      /* No tabs saved — load default and create first tab on iframe load */
      var savedRight = localStorage.getItem(RCONTENT_KEY);
      if (savedRight) { savedRight = stripLang(savedRight); localStorage.setItem(RCONTENT_KEY, savedRight); }
      var defaultRight = vruFn(BASE + LP + '/');
      if (rightIframe) { rightIframe.src = savedRight ? applyLang(savedRight) : defaultRight; }
    }
  } catch(e) {
    var savedRight2 = localStorage.getItem(RCONTENT_KEY);
    var defaultRight2 = vruFn(BASE + LP + '/');
    if (rightIframe) { rightIframe.src = savedRight2 ? applyLang(savedRight2) : defaultRight2; }
  }

  /* ─── Restore active link highlight ─── */
  var savedActive = localStorage.getItem(ACTIVE_KEY);
  if (savedActive) {
    var found = panel.querySelector('a[data-nav-id="' + savedActive + '"]');
    if (found) found.classList.add('active');
  }

  /* ─── Active link highlight + save URLs + tab creation ─── */
  panel.addEventListener('click', function(e) {
    var a = e.target.closest('a[target="content-frame"]') || e.target.closest('a[target="center-frame"]');
    if (!a) return;
    panel.querySelectorAll('a.active').forEach(function(el) { el.classList.remove('active'); });
    a.classList.add('active');
    localStorage.setItem(ACTIVE_KEY, a.dataset.navId || a.href);
    /* Save center URL if targeting center (language-neutral) */
    if (a.target === 'center-frame') { localStorage.setItem(CENTER_KEY, stripLang(a.href)); }
    /* Content-frame: create tab + extend panel */
    if (a.target === 'content-frame') {
      e.preventDefault();
      var tabTitle = a.textContent.trim() || 'Document';
      addTab(a.href, tabTitle);
    }
  });

  /* ─── postMessage from center-frame interfaces (ℹ button) ─── */
  window.addEventListener('message', function(e) {
    if (e.data && e.data.type === 'open-pub') {
      addTab(e.data.url, e.data.title || 'Guide');
    }
  });

  /* ─── Theme propagation to both iframes ─── */
  function syncThemeToIframes() {
    var theme = document.documentElement.getAttribute('data-theme');
    [centerIframe, rightIframe].forEach(function(f) {
      if (!f) return;
      try {
        var iDoc = f.contentDocument.documentElement;
        if (theme) iDoc.setAttribute('data-theme', theme);
        else iDoc.removeAttribute('data-theme');
      } catch(e) {}
    });
  }
  new MutationObserver(function(muts) {
    muts.forEach(function(m) { if (m.attributeName === 'data-theme') syncThemeToIframes(); });
  }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });

  if (centerIframe) {
    centerIframe.addEventListener('load', function() {
      try {
        var loc = centerIframe.contentWindow.location.href;
        if (loc && loc !== 'about:blank') localStorage.setItem(CENTER_KEY, stripLang(loc));
      } catch(e) {}
      syncThemeToIframes();
    });
  }
  if (rightIframe) {
    rightIframe.addEventListener('load', function() {
      try {
        var loc = rightIframe.contentWindow.location.href;
        if (loc && loc !== 'about:blank') {
          localStorage.setItem(RCONTENT_KEY, stripLang(loc));
          var title = 'Document';
          try { title = rightIframe.contentDocument.title || title; } catch(e2) {}
          /* If navigating programmatically (tab click), just update title */
          if (tabNavigating) {
            tabNavigating = false;
            if (activeTabId) {
              var at = tabs.find(function(t) { return t.id === activeTabId; });
              if (at && title !== 'Document') { at.title = title; at.url = stripLang(loc); renderTabs(); saveTabState(); }
            }
          } else {
            /* In-iframe navigation — create or update tab */
            addTab(loc, title);
          }
        }
      } catch(e) {}
      syncThemeToIframes();
    });
  }

})();
</script>
{:/nomarkdown}
