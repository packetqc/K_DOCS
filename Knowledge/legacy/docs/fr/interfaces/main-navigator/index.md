---
layout: publication
page_type: interface
title: "Navigateur principal"
description: "Interface de navigation principale du système Knowledge : navigateur trois panneaux avec répertoire de widgets, visualiseur extensible et référence des commandes."
pub_id: "Navigateur principal · I2"
version: "v4"
date: "2026-03-01"
permalink: /fr/interfaces/main-navigator/
keywords: "interface, navigation, navigateur, connaissances, tableau de bord, commandes"
og_image: /assets/og/main-navigator-fr-cayman.gif
dev_banner: "Interface en developpement — les fonctionnalites et la mise en page peuvent changer entre les sessions."
lang: fr
---

# Navigateur principal

{::nomarkdown}
<style>
/* ═══ Hide gradient header + footer only — keep layout chrome ═══ */
.page-header, .site-footer, .pub-crossrefs { display: none !important; }
html { margin: 0; padding: 0; height: 100%; }
body { margin: 0; padding: 0; overflow: hidden; height: 100vh; display: flex; flex-direction: column; }

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
/* Collapsed state — hide all chrome + title */
.container.chrome-collapsed .pub-lang-bar,
.container.chrome-collapsed .dev-banner,
.container.chrome-collapsed .pub-topbar,
.container.chrome-collapsed .pub-version-banner,
.container.chrome-collapsed .pub-export-toolbar,
.container.chrome-collapsed > h1 {
  max-height: 0 !important; opacity: 0 !important;
  padding-top: 0 !important; padding-bottom: 0 !important;
  margin-top: 0 !important; margin-bottom: 0 !important;
  border: none !important;
}

/* Chrome toggle bar — pinned to top via flex order */
.chrome-bar {
  flex-shrink: 0; order: -1;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.15rem 0.75rem;
  background: var(--code-bg, #f6f8fa);
  border-bottom: 1px solid var(--border, #d0d7de);
  font-size: 0.78rem;
  user-select: none;
}
.chrome-bar .lang-toggle a {
  text-decoration: none; color: var(--muted, #656d76);
  padding: 0.1rem 0.3rem; border-radius: 3px;
}
.chrome-bar .lang-toggle a:hover { color: var(--accent, #1d4ed8); }
.chrome-bar .lang-toggle .lang-active {
  font-weight: 700; color: var(--fg, #24292f);
  background: var(--bg, #fff); border: 1px solid var(--border, #d0d7de);
}
.chrome-bar .orient-toggle a {
  text-decoration: none; color: var(--muted, #656d76);
  padding: 0.1rem 0.3rem; border-radius: 3px; cursor: pointer;
}
.chrome-bar .orient-toggle a:hover { color: var(--accent, #1d4ed8); }
.chrome-bar .orient-toggle .orient-active {
  font-weight: 700; color: var(--fg, #24292f);
  background: var(--bg, #fff); border: 1px solid var(--border, #d0d7de);
}
.chrome-bar .chrome-toggle {
  cursor: pointer; color: var(--muted, #656d76);
  padding: 0.1rem 0.4rem; border-radius: 3px; font-size: 0.7rem;
}
.chrome-bar .chrome-toggle:hover {
  background: var(--col-alt, #f0f0f0); color: var(--accent, #1d4ed8);
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
  --left-w: 220px;
  flex: 1; min-height: 0; display: grid; overflow: hidden;
  position: relative;
  grid-template-columns: var(--left-w) 28px 1fr 28px 0px;
  grid-template-rows: 1fr;
  transition: grid-template-columns 0.25s ease;
  margin: 0.3rem 0.4rem 0.25rem;
  border: 1px solid var(--border, #d0d7de);
  border-radius: 10px;
  background: var(--bg, #fff);
}
.nav-grid.left-closed { --left-w: 0px; }
/* Right at 50vw — center + right */
.nav-grid.right-mid {
  grid-template-columns: var(--left-w) 28px 1fr 28px 50vw;
}
/* Right full — center hidden, viewer glued to right edge */
.nav-grid.right-full {
  grid-template-columns: var(--left-w) 28px 0fr 28px 1fr;
  margin-right: 0;
  border-right: none;
  border-radius: 10px 0 0 10px;
}

/* Left nav panel — overlay, does not take grid space */
.nav-panel {
  grid-column: 1;
  position: absolute; left: 0; top: 0; bottom: 0;
  width: 220px; z-index: 20;
  background: var(--code-bg, #f6f8fa);
  overflow-y: auto; overflow-x: hidden;
  border-right: 1px solid var(--border, #d0d7de);
  box-shadow: 2px 0 8px rgba(0,0,0,0.08);
  transition: transform 0.25s ease, opacity 0.2s ease;
  border-radius: 10px 0 0 10px;
}
.nav-grid.left-closed .nav-panel {
  transform: translateX(-100%); opacity: 0; pointer-events: none;
}

/* Left divider — visible interactive bar */
.nav-divider-left {
  grid-column: 2;
  background: linear-gradient(180deg, var(--accent, #1d4ed8) 0%, var(--code-bg, #f6f8fa) 10%, var(--code-bg, #f6f8fa) 90%, var(--accent, #1d4ed8) 100%);
  border-right: 3px solid var(--accent, #1d4ed8);
  border-left: 3px solid var(--accent, #1d4ed8);
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; user-select: none;
  color: var(--fg, #24292f); font-size: 1rem; font-weight: 700;
  transition: background 0.2s ease, box-shadow 0.2s ease;
  position: relative;
  min-width: 28px;
  z-index: 10;
}
.nav-divider-left::before {
  content: '·\A·\A·'; white-space: pre; position: absolute; top: 50%; transform: translateY(-50%);
  font-size: 0.7rem; line-height: 0.5; color: var(--muted, #656d76); margin-top: -1.5rem;
}
.nav-divider-left:hover {
  background: linear-gradient(180deg, var(--accent, #1d4ed8) 0%, var(--col-alt, #e0e8f0) 15%, var(--col-alt, #e0e8f0) 85%, var(--accent, #1d4ed8) 100%);
  color: var(--accent, #1d4ed8);
  box-shadow: 0 0 6px rgba(29,78,216,0.2);
}

/* Center panel — content viewer (deepest layer) */
.nav-center {
  grid-column: 3;
  background: var(--bg, #fff);
  display: flex; flex-direction: column; min-width: 0;
  overflow: hidden; transition: opacity 0.2s ease;
  z-index: 1;
}
.nav-grid.right-full .nav-center { opacity: 0; pointer-events: none; }
.nav-center iframe { flex: 1; width: 100%; border: none; background: var(--bg, #fff); }

/* Right divider — visible interactive bar with bidirectional arrows */
.nav-divider-right {
  grid-column: 4;
  background: linear-gradient(180deg, var(--accent, #1d4ed8) 0%, var(--code-bg, #f6f8fa) 10%, var(--code-bg, #f6f8fa) 90%, var(--accent, #1d4ed8) 100%);
  border-left: 3px solid var(--accent, #1d4ed8);
  border-right: 3px solid var(--accent, #1d4ed8);
  display: flex; flex-direction: column;
  align-items: center; justify-content: center; gap: 10px;
  cursor: pointer; user-select: none;
  font-size: 0.85rem; color: var(--fg, #24292f);
  transition: background 0.2s ease, box-shadow 0.2s ease;
  position: relative;
  min-width: 28px;
  z-index: 40;
}
.nav-divider-right::before {
  content: '·\A·\A·'; white-space: pre; position: absolute; top: 50%; transform: translateY(-50%);
  font-size: 0.7rem; line-height: 0.5; color: var(--muted, #656d76); margin-top: -1.5rem;
}
.nav-divider-right:hover {
  background: linear-gradient(180deg, var(--accent, #1d4ed8) 0%, var(--col-alt, #e0e8f0) 15%, var(--col-alt, #e0e8f0) 85%, var(--accent, #1d4ed8) 100%);
  box-shadow: 0 0 6px rgba(29,78,216,0.2);
}
.nav-divider-right .r-arrow {
  cursor: pointer; padding: 3px 0; line-height: 1;
  font-size: 0.9rem; font-weight: 700; display: inline-block; width: 1em; text-align: center;
  z-index: 1;
}
.nav-divider-right .r-arrow:hover { color: var(--accent, #1d4ed8); }
.nav-divider-right .r-arrow.hidden { display: none; }

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
.nav-widget .widget-body { padding: 0.2rem 0; }
.nav-widget .widget-body a {
  display: block; font-size: 0.78rem;
  padding: 0.18rem 0.55rem;
  color: var(--fg, #24292f);
  text-decoration: none; border-radius: 3px;
}
.nav-widget .widget-body a:hover {
  background: var(--col-alt, #f0f0f0); color: var(--accent, #1d4ed8);
}
.nav-widget .widget-body a.active {
  background: var(--accent, #1d4ed8); color: var(--bg, #fff);
}

/* Sub-groups */
.nav-widget .pub-group { margin: 0; padding: 0; }
.nav-widget .pub-group summary {
  font-size: 0.76rem; font-weight: 600;
  text-transform: none; letter-spacing: 0;
  padding: 0.2rem 0.55rem;
  background: none; border-bottom: none;
  color: var(--fg, #24292f);
}
.nav-widget .pub-group summary::before { content: '›'; font-size: 0.8rem; }
.nav-widget .pub-group[open] > summary::before { content: '⌄'; }
.nav-widget .pub-group a { padding-left: 1.3rem; font-size: 0.74rem; }
.cmd-link { font-family: monospace; font-size: 0.72rem; color: var(--muted, #656d76); }

/* ═══ Print / PDF export — center panel content after cover page ═══ */
@media print {
  html, body { height: auto !important; overflow: visible !important; }
  body { display: block !important; }
  .container { display: block !important; overflow: visible !important; max-width: 100% !important; }
  /* Hide interactive chrome — left panel, dividers, right panel, chrome bar */
  .chrome-bar, .nav-panel, .nav-divider-left, .nav-divider-right,
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

<!-- BARRE CHROME -->
<div class="chrome-bar" id="chrome-bar">
  <span class="chrome-toggle" id="chrome-toggle" title="Replier/deployer l'en-tete">▲</span>
  <span class="orient-toggle" id="orient-toggle" title="Basculer l'orientation de la page">
    <a data-orient="portrait" class="orient-active">Portrait</a>
    <a data-orient="landscape">Paysage</a>
  </span>
  <span class="lang-toggle">
    <a href="{{ '/interfaces/main-navigator/' | relative_url }}">EN</a>
    <a href="{{ '/fr/interfaces/main-navigator/' | relative_url }}" class="lang-active">FR</a>
  </span>
</div>

<!-- GRILLE PRINCIPALE -->
<div class="nav-grid" id="nav-grid">

  <!-- GAUCHE — Répertoire de widgets -->
  <div class="nav-panel" id="left-panel"></div>

  <!-- DIVISEUR GAUCHE — bascule ouvert/fermé -->
  <div class="nav-divider-left" id="left-toggle"><span>◀</span></div>

  <!-- CENTRE — Visualiseur de contenu (liens du panneau gauche) -->
  <div class="nav-center" id="center-panel">
    <iframe name="center-frame" src="{{ '/fr/interfaces/task-workflow/' | relative_url }}"></iframe>
  </div>

  <!-- DIVISEUR DROIT — flèches bidirectionnelles -->
  <div class="nav-divider-right" id="right-toggle">
    <span class="r-arrow" data-dir="extend" title="Étendre le visualiseur">◀</span>
    <span class="r-arrow hidden" data-dir="collapse" title="Replier le visualiseur">▶</span>
  </div>

  <!-- DROITE — Visualiseur de contenu -->
  <div class="nav-viewer">
    <iframe name="content-frame" src="{{ '/fr/' | relative_url }}"></iframe>
  </div>

</div>

<script>
(function() {
  var BASE = '{{ "" | relative_url }}';
  var CENTER_KEY  = 'navigator-center-url-fr';
  var WIDGET_KEY  = 'navigator-widgets-fr';
  var LPANEL_KEY  = 'navigator-left-state';
  var RPANEL_KEY  = 'navigator-right-state';
  var CHROME_KEY  = 'navigator-chrome-collapsed';
  var RCONTENT_KEY = 'navigator-right-url-fr';
  var ACTIVE_KEY  = 'navigator-active-href-fr';
  var SUBDET_KEY  = 'navigator-subdetails-fr';
  var centerIframe = document.querySelector('iframe[name="center-frame"]');
  var rightIframe  = document.querySelector('iframe[name="content-frame"]');
  var panel  = document.getElementById('left-panel');
  var grid   = document.getElementById('nav-grid');
  var lToggle = document.getElementById('left-toggle');
  var rToggle = document.getElementById('right-toggle');
  if (!panel || !grid) return;

  /* ─── Chrome collapse/expand ─── */
  var container = document.querySelector('.container');
  var chromeToggle = document.getElementById('chrome-toggle');
  var chromeCollapsed = localStorage.getItem(CHROME_KEY) !== '0';

  function applyChromeState() {
    if (chromeCollapsed) {
      container.classList.add('chrome-collapsed');
      chromeToggle.textContent = '▼';
      chromeToggle.title = 'Deployer l\'en-tete';
    } else {
      container.classList.remove('chrome-collapsed');
      chromeToggle.textContent = '▲';
      chromeToggle.title = 'Replier l\'en-tete';
    }
  }
  applyChromeState();
  chromeToggle.addEventListener('click', function() {
    chromeCollapsed = !chromeCollapsed;
    applyChromeState();
    localStorage.setItem(CHROME_KEY, chromeCollapsed ? '1' : '0');
  });

  /* ─── Left divider — 2 states: open / closed ─── */
  var lArrow = lToggle.querySelector('span');
  var leftOpen = localStorage.getItem(LPANEL_KEY) !== '0';

  /* ─── Right divider — 3 states: 0=collapsed, 1=40%, 2=full ─── */
  var rState = parseInt(localStorage.getItem(RPANEL_KEY) || '0');
  var extendBtn = rToggle.querySelector('[data-dir="extend"]');
  var collapseBtn = rToggle.querySelector('[data-dir="collapse"]');

  function applyGridState() {
    var cls = 'nav-grid';
    if (!leftOpen) cls += ' left-closed';
    if (rState === 1) cls += ' right-mid';
    else if (rState === 2) cls += ' right-full';
    grid.className = cls;
    /* Left arrow */
    lArrow.textContent = leftOpen ? '◀' : '▶';
    /* Right arrows visibility */
    extendBtn.classList.toggle('hidden', rState >= 2);
    collapseBtn.classList.toggle('hidden', rState <= 0);
  }
  applyGridState();

  lToggle.addEventListener('click', function() {
    leftOpen = !leftOpen;
    applyGridState();
    localStorage.setItem(LPANEL_KEY, leftOpen ? '1' : '0');
  });

  extendBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    if (rState < 2) { rState++; applyGridState(); localStorage.setItem(RPANEL_KEY, rState); }
  });
  collapseBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    if (rState > 0) { rState--; applyGridState(); localStorage.setItem(RPANEL_KEY, rState); }
  });

  /* ─── Widget definitions (French) ─── */
  var widgets = [
    { id:'interfaces', title:'Interfaces', open:true, links:[
      {t:'I1 Revue de session',     h:BASE+'/fr/interfaces/session-review/', center:true},
      {t:'I2 Navigateur principal',  h:BASE+'/fr/interfaces/main-navigator/', top:true},
      {t:'I3 Flux de travail',      h:BASE+'/fr/interfaces/task-workflow/', center:true},
      {t:'I4 Visualiseur projets',  h:BASE+'/fr/interfaces/project-viewer/', center:true},
      {t:'#21 Documentation',       h:BASE+'/fr/publications/main-interface/'}
    ]},
    { id:'essentials', title:'Essentiels', open:false, links:[
      {t:'HISTOIRES',     h:BASE+'/fr/publications/success-stories/'},
      {t:'README',        h:BASE+'/fr/'},
      {t:'PLAN',          h:BASE+'/fr/plan/'},
      {t:'LIENS',         h:BASE+'/fr/links/'},
      {t:'NOUVELLES',     h:BASE+'/fr/news/'},
      {t:'CHANGELOG',     h:BASE+'/fr/changelog/'}
    ]},
    { id:'commands', title:'Commandes', open:false, groups:[
      { g:'Session', pub:'/fr/publications/session-management/full/#pub-title', cmds:['wakeup','refresh','help / aide','status','save','remember','resume','recall','checkpoint','elevate'] },
      { g:'Normalize', pub:'/fr/publications/normalize-structure-concordance/full/#pub-title', cmds:['normalize','normalize --fix','normalize --check'] },
      { g:'Harvest', pub:'/fr/publications/harvest-protocol/full/#pub-title', cmds:['harvest','harvest --list','harvest --procedure','harvest --healthcheck','harvest --review','harvest --stage','harvest --promote','harvest --auto','harvest --fix'] },
      { g:'Publications', pub:'/fr/publications/webcards-social-sharing/full/#pub-title', cmds:['pub list','pub check','pub new','pub sync','doc review','docs check','webcard','weblinks','pub export'] },
      { g:'Projet', pub:'/fr/publications/knowledge-system/full/#pub-title', cmds:['project list','project info','project create','project register','project review','#N: note','g:board:item'] },
      { g:'Session live', pub:'/fr/publications/live-session-analysis/full/#pub-title', cmds:["I'm live",'multi-live','deep','analyze','recipe'] },
      { g:'Réseau live', pub:'/fr/publications/live-knowledge-network/full/#pub-title', cmds:['beacon'] }
    ]},
    { id:'hubs', title:'Hubs', open:false, links:[
      {t:'Accueil',      h:BASE+'/fr/'},
      {t:'Publications', h:BASE+'/fr/publications/'},
      {t:'Projets',      h:BASE+'/fr/projects/'}
    ]},
    { id:'profile', title:'Profil', open:false, links:[
      {t:'Hub',     h:BASE+'/fr/profile/'},
      {t:'Résumé',  h:BASE+'/fr/profile/resume/'},
      {t:'Complet', h:BASE+'/fr/profile/full/'}
    ]},
    { id:'publications', title:'Publications', open:false, pubs:[
      {n:'#0',  t:'Système de connaissances', s:'knowledge-system'},
      {n:'#1',  t:'Pipeline MPLIB',           s:'mplib-storage-pipeline'},
      {n:'#2',  t:'Session live',             s:'live-session-analysis'},
      {n:'#3',  t:'Persistance IA',           s:'ai-session-persistence'},
      {n:'#4',  t:'Esprits distribués',       s:'distributed-minds'},
      {n:'#4a', t:'Tableau de bord',          s:'distributed-knowledge-dashboard'},
      {n:'#5',  t:'Webcards',                 s:'webcards-social-sharing'},
      {n:'#6',  t:'Normalize',                s:'normalize-structure-concordance'},
      {n:'#7',  t:'Harvest',                  s:'harvest-protocol'},
      {n:'#8',  t:'Gestion de session',       s:'session-management'},
      {n:'#9',  t:'Sécurité',                 s:'security-by-design',
        extra:[{t:'#9a Conformité', p:'/fr/publications/security-by-design/compliance/'}]},
      {n:'#10', t:'Réseau live',              s:'live-knowledge-network'},
      {n:'#11', t:'Histoires de succès',      s:'success-stories'},
      {n:'#12', t:'Gestion de projet',        s:'project-management'},
      {n:'#13', t:'Pagination',               s:'web-pagination-export'},
      {n:'#14', t:'Architecture',             s:'architecture-analysis'},
      {n:'#15', t:'Diagrammes',               s:'architecture-diagrams'},
      {n:'#16', t:'Visualisation',            s:'web-page-visualization'},
      {n:'#17', t:'Pipeline',                 s:'web-production-pipeline'},
      {n:'#18', t:'Génération doc',           s:'documentation-generation'},
      {n:'#19', t:'Interactif',               s:'interactive-work-sessions'},
      {n:'#20', t:'Métriques de session',     s:'session-metrics-time'},
      {n:'#21', t:'Interface principale',     s:'main-interface'},
      {n:'#22', t:'Revue de session',         s:'session-review'}
    ]}
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

  widgets.forEach(function(w) {
    var det = document.createElement('details');
    det.className = 'nav-widget'; det.dataset.wid = w.id;
    det.open = (savedState[w.id] !== undefined) ? savedState[w.id] : w.open;
    det.addEventListener('toggle', saveWidgetState);
    var sm = document.createElement('summary'); sm.textContent = w.title; det.appendChild(sm);
    var body = document.createElement('div'); body.className = 'widget-body';

    if (w.links) {
      w.links.forEach(function(lk) {
        var a = document.createElement('a'); a.href = lk.h;
        a.dataset.navId = 'nav-' + (navLinkId++);
        a.target = lk.top ? '_top' : (lk.center ? 'center-frame' : 'content-frame'); a.textContent = lk.t;
        body.appendChild(a);
      });
    }
    if (w.groups) {
      w.groups.forEach(function(cg) {
        var idx = subDetIndex++;
        var pg = document.createElement('details'); pg.className = 'pub-group';
        if (savedSubDet[idx] !== undefined) pg.open = savedSubDet[idx];
        pg.addEventListener('toggle', saveSubDetState);
        var pgsm = document.createElement('summary'); pgsm.textContent = cg.g; pg.appendChild(pgsm);
        cg.cmds.forEach(function(cmd) {
          var a = document.createElement('a'); a.href = BASE + cg.pub; a.target = 'content-frame';
          a.dataset.navId = 'nav-' + (navLinkId++);
          var sp = document.createElement('span'); sp.className = 'cmd-link'; sp.textContent = cmd;
          a.appendChild(sp); pg.appendChild(a);
        });
        body.appendChild(pg);
      });
    }
    if (w.pubs) {
      w.pubs.forEach(function(p) {
        var idx = subDetIndex++;
        var pg = document.createElement('details'); pg.className = 'pub-group';
        if (savedSubDet[idx] !== undefined) pg.open = savedSubDet[idx];
        pg.addEventListener('toggle', saveSubDetState);
        var pgsm = document.createElement('summary'); pgsm.textContent = p.n + ' ' + p.t; pg.appendChild(pgsm);
        var a1 = document.createElement('a'); a1.href = BASE+'/fr/publications/'+p.s+'/#pub-title';
        a1.dataset.navId = 'nav-' + (navLinkId++);
        a1.target = 'content-frame'; a1.textContent = 'Résumé'; pg.appendChild(a1);
        var a2 = document.createElement('a'); a2.href = BASE+'/fr/publications/'+p.s+'/full/#pub-title';
        a2.dataset.navId = 'nav-' + (navLinkId++);
        a2.target = 'content-frame'; a2.textContent = 'Complet'; pg.appendChild(a2);
        if (p.extra) { p.extra.forEach(function(e) {
          var ax = document.createElement('a'); ax.href = BASE+e.p;
          ax.dataset.navId = 'nav-' + (navLinkId++);
          ax.target = 'content-frame'; ax.textContent = e.t; pg.appendChild(ax);
        }); }
        body.appendChild(pg);
      });
    }
    det.appendChild(body); panel.appendChild(det);
  });

  /* ─── Restore last viewed page in center + right + active link ─── */
  var savedCenter = localStorage.getItem(CENTER_KEY);
  if (savedCenter && centerIframe) { centerIframe.src = savedCenter; }
  var savedRight = localStorage.getItem(RCONTENT_KEY);
  if (savedRight && rightIframe) { rightIframe.src = savedRight; }

  var savedActive = localStorage.getItem(ACTIVE_KEY);
  if (savedActive) {
    var found = panel.querySelector('a[data-nav-id="' + savedActive + '"]');
    if (found) found.classList.add('active');
  }

  /* ─── Active link highlight + save URLs ─── */
  panel.addEventListener('click', function(e) {
    var a = e.target.closest('a[target="content-frame"]') || e.target.closest('a[target="center-frame"]');
    if (!a) return;
    panel.querySelectorAll('a.active').forEach(function(el) { el.classList.remove('active'); });
    a.classList.add('active');
    localStorage.setItem(ACTIVE_KEY, a.dataset.navId || a.href);
    /* Save center URL if targeting center */
    if (a.target === 'center-frame') { localStorage.setItem(CENTER_KEY, a.href); }
    /* Save right URL + extend right panel if collapsed */
    if (a.target === 'content-frame') {
      localStorage.setItem(RCONTENT_KEY, a.href);
      if (rState < 1) { rState = 1; applyGridState(); localStorage.setItem(RPANEL_KEY, String(rState)); }
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
        if (loc && loc !== 'about:blank') localStorage.setItem(CENTER_KEY, loc);
      } catch(e) {}
      syncThemeToIframes();
    });
  }
  if (rightIframe) {
    rightIframe.addEventListener('load', function() {
      try {
        var loc = rightIframe.contentWindow.location.href;
        if (loc && loc !== 'about:blank') localStorage.setItem(RCONTENT_KEY, loc);
      } catch(e) {}
      syncThemeToIframes();
    });
  }

  /* ─── Language propagation — transform center iframe URL on lang switch ─── */
  document.querySelectorAll('.chrome-bar .lang-toggle a:not(.lang-active)').forEach(function(langLink) {
    langLink.addEventListener('click', function() {
      var curPath = '';
      try { curPath = centerIframe.contentWindow.location.pathname; } catch(ex) {}
      if (!curPath) return;
      var afterBase = curPath.substring(BASE.length);
      var targetPath = BASE + afterBase.replace(/^\/fr/, '');
      localStorage.setItem('navigator-center-url', targetPath);
    });
  });

  /* ─── Orientation toggle — controls right panel (3rd panel) only ─── */
  var ORIENT_KEY = 'navigator-orient:';
  var orientLinks = document.querySelectorAll('#orient-toggle a[data-orient]');

  function getPagePath() {
    try { return rightIframe.contentWindow.location.pathname.replace(/\/+$/, ''); } catch(e) { return ''; }
  }

  function applyOrientUI(orient) {
    orientLinks.forEach(function(a) {
      a.classList.toggle('orient-active', a.dataset.orient === orient);
    });
  }

  function sendOrientToRight(orient) {
    try { rightIframe.contentWindow.postMessage({ type: 'set-orientation', orient: orient }, '*'); } catch(e) {}
  }

  /* On right iframe load — restore per-page orientation */
  if (rightIframe) {
    rightIframe.addEventListener('load', function() {
      var path = getPagePath();
      if (!path) return;
      var saved = localStorage.getItem(ORIENT_KEY + path) || 'portrait';
      applyOrientUI(saved);
      sendOrientToRight(saved);
    });
  }

  /* On toggle click — save + send to right iframe */
  orientLinks.forEach(function(a) {
    a.addEventListener('click', function() {
      var orient = this.dataset.orient;
      applyOrientUI(orient);
      var path = getPagePath();
      if (path) localStorage.setItem(ORIENT_KEY + path, orient);
      sendOrientToRight(orient);
    });
  });

})();

/* ═══ Panel selector — inject into layout's export toolbar ═══ */
(function() {
  var PANEL_KEY = 'navigator-export-panel';
  var selectedPanel = localStorage.getItem(PANEL_KEY) || 'center';

  var pdfBtn = document.getElementById('exportPdf');
  if (!pdfBtn) return;
  var toolbarGroup = pdfBtn.parentElement;

  var panelGroup = document.createElement('span');
  panelGroup.className = 'pub-orient-group';
  panelGroup.style.marginRight = '0.5rem';
  panelGroup.innerHTML =
    '<label class="pub-export-radio" title="Exporter le panneau central">' +
      '<input type="radio" name="navPanel" value="center"' + (selectedPanel === 'center' ? ' checked' : '') + '> Central' +
    '</label>' +
    '<label class="pub-export-radio" title="Exporter le panneau de droite">' +
      '<input type="radio" name="navPanel" value="right"' + (selectedPanel === 'right' ? ' checked' : '') + '> Droite' +
    '</label>';

  var sep = document.createElement('span');
  sep.className = 'pub-orient-sep';

  toolbarGroup.insertBefore(sep, pdfBtn);
  toolbarGroup.insertBefore(panelGroup, sep);

  panelGroup.querySelectorAll('input[name="navPanel"]').forEach(function(r) {
    r.addEventListener('change', function() {
      selectedPanel = this.value;
      localStorage.setItem(PANEL_KEY, selectedPanel);
    });
  });

  function getSelectedFrame() {
    return selectedPanel === 'right' ? 'content-frame' : 'center-frame';
  }

  var newPdf = pdfBtn.cloneNode(true);
  pdfBtn.parentNode.replaceChild(newPdf, pdfBtn);
  newPdf.addEventListener('click', function(e) {
    e.preventDefault();
    var frameName = getSelectedFrame();
    var frame = window.frames[frameName];
    if (!frame) return;
    try {
      var fdoc = frame.document;
      if (!fdoc.getElementById('pub-cover-page')) {
        var title = fdoc.title || 'Export';
        var now = new Date();
        var gen = now.getFullYear() + '-' +
          String(now.getMonth()+1).padStart(2,'0') + '-' +
          String(now.getDate()).padStart(2,'0') + '  ' +
          String(now.getHours()).padStart(2,'0') + ':' +
          String(now.getMinutes()).padStart(2,'0');
        var cover = fdoc.createElement('div');
        cover.id = 'pub-cover-page';
        cover.setAttribute('aria-hidden', 'true');
        cover.innerHTML =
          '<div class="cover-body">' +
            '<div class="cover-title">' + title + '</div>' +
            '<hr class="cover-rule">' +
            '<div class="cover-meta">Martin Paquet<br>Claude (Anthropic, Opus 4.6)</div>' +
            '<div class="cover-gen-line">Généré : ' + gen + '</div>' +
          '</div>';
        var style = fdoc.createElement('style');
        style.textContent =
          '@media print { #pub-cover-page { display:flex; align-items:center; justify-content:center; ' +
          'text-align:center; min-height:20cm; page-break-after:always; } ' +
          '.cover-body { max-width:18cm; } ' +
          '.cover-title { font-size:28pt; font-weight:700; color:#111; line-height:1.2; margin-bottom:0.7cm; } ' +
          '.cover-rule { border:none; border-top:1.5pt solid #444; margin:0 auto 0.8cm; width:6cm; } ' +
          '.cover-meta { font-size:10pt; color:#444; line-height:2; } ' +
          '.cover-gen-line { font-size:8.5pt; color:#666; font-family:monospace; margin-top:0.2cm; } }' +
          '@media screen { #pub-cover-page { display:none; } }';
        fdoc.head.appendChild(style);
        fdoc.body.insertBefore(cover, fdoc.body.firstChild);
      }
      frame.focus(); frame.print();
    } catch(err) {
      var url = document.querySelector('iframe[name="' + frameName + '"]').src;
      window.open(url, '_blank');
    }
  });

  var docxBtn = document.getElementById('exportDocx');
  if (docxBtn) {
    var newDocx = docxBtn.cloneNode(true);
    docxBtn.parentNode.replaceChild(newDocx, docxBtn);
    newDocx.addEventListener('click', function(e) {
      e.preventDefault();
      var frameName = getSelectedFrame();
      var frame = window.frames[frameName];
      if (!frame) return;
      try {
        var iframeDocx = frame.document.getElementById('exportDocx');
        if (iframeDocx) { iframeDocx.click(); }
        else { window.open(document.querySelector('iframe[name="' + frameName + '"]').src, '_blank'); }
      } catch(err) {
        window.open(document.querySelector('iframe[name="' + frameName + '"]').src, '_blank');
      }
    });
  }
})();

/* ═══ Propagate theme + page size changes to both iframes ═══ */
(function() {
  var centerIframe = document.querySelector('iframe[name="center-frame"]');
  var rightIframe = document.querySelector('iframe[name="content-frame"]');

  function sendToIframes(msg) {
    try { if (centerIframe) centerIframe.contentWindow.postMessage(msg, '*'); } catch(e) {}
    try { if (rightIframe) rightIframe.contentWindow.postMessage(msg, '*'); } catch(e) {}
  }

  var themeSelect = document.getElementById('themeSelect');
  if (themeSelect) {
    themeSelect.addEventListener('change', function() {
      sendToIframes({ type: 'set-theme', theme: this.value });
    });
  }

  var sizeRadios = document.querySelectorAll('input[name="pubPageSize"]');
  sizeRadios.forEach(function(r) {
    r.addEventListener('change', function() {
      sendToIframes({ type: 'set-page-size', size: this.value });
    });
  });

  var orientRadios = document.querySelectorAll('input[name="pubOrient"]');
  orientRadios.forEach(function(r) {
    r.addEventListener('change', function() {
      sendToIframes({ type: 'set-orientation', orient: this.value });
    });
  });

  function pushCurrentState(iframe) {
    if (!iframe) return;
    iframe.addEventListener('load', function() {
      var theme = (themeSelect && themeSelect.value) || localStorage.getItem('knowledge-theme') || 'auto';
      var size = 'letter';
      sizeRadios.forEach(function(r) { if (r.checked) size = r.value; });
      var orient = 'portrait';
      orientRadios.forEach(function(r) { if (r.checked) orient = r.value; });
      try {
        iframe.contentWindow.postMessage({ type: 'set-theme', theme: theme }, '*');
        iframe.contentWindow.postMessage({ type: 'set-page-size', size: size }, '*');
        iframe.contentWindow.postMessage({ type: 'set-orientation', orient: orient }, '*');
      } catch(e) {}
    });
  }
  pushCurrentState(centerIframe);
  pushCurrentState(rightIframe);
})();
</script>
{:/nomarkdown}
