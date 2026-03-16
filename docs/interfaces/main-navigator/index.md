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
  <div class="nav-viewer">
    <iframe name="content-frame" id="right-frame-el"></iframe>
  </div>
</div>

<script>
(function() {
  /* ─── Language auto-detection from URL path ─── */
  var LANG = (document.documentElement.lang === 'fr' || window.location.pathname.indexOf('/fr/') >= 0) ? 'fr' : 'en';
  var LP = LANG === 'fr' ? '/fr' : '';  // language path prefix
  // localStorage keys are language-neutral (shared across EN/FR)

  var T = {
    en: {
      interfaces: 'Interfaces',
      i1: 'I1 Session Review', i2: 'I2 Main Navigator', i3: 'I3 Tasks Workflow',
      i4: 'I4 Project Viewer', i5: 'I5 Live Mindmap', i_doc: '#21 Documentation',
      essentials: 'Essentials',
      stories: 'STORIES', readme: 'README', plan: 'PLAN', links: 'LINKS', news: 'NEWS', changelog: 'CHANGELOG',
      commands: 'Commands',
      g_session: 'Session', g_normalize: 'Normalize', g_harvest: 'Harvest',
      g_publications: 'Publications', g_project: 'Project', g_live_session: 'Live Session', g_live_network: 'Live Network',
      hubs: 'Hubs', landing: 'Landing', publications: 'Publications', interfaces_hub: 'Interfaces', projects: 'Projects',
      profile: 'Profile', hub: 'Hub', resume: 'Resume', full: 'Full',
      summary: 'Summary',
      p0: 'Knowledge System', p1: 'Knowledge 2.0', p2: 'Live Session', p3: 'AI Persistence',
      p4: 'Distributed Minds', p4a: 'Dashboard', p5: 'Webcards', p6: 'Normalize',
      p7: 'Harvest', p8: 'Session Mgmt', p9: 'Security', p9a: '#9a Compliance',
      p10: 'Live Network', p11: 'Success Stories', p12: 'Project Mgmt', p13: 'Pagination',
      p14: 'Architecture', p15: 'Diagrams', p16: 'Visualization', p17: 'Pipeline',
      p18: 'Doc Generation', p19: 'Interactive', p20: 'Session Metrics',
      p21: 'Main Interface', p22: 'Session Review', p22b: 'Visual Documentation', p23: 'Web Viewer', p24: 'Live Mindmap',
      stories_title: 'Success Stories',
      s26: '#26 One Viewer to Rule Them All', s25: '#25 Live Mindmap Memory',
      s24: '#24 The Toggle', s23: '#23 Knowledge v2.0 Platform',
      s22: '#22 Visual Documentation Engine', s21: '#21 Task Workflow State Machine',
      s19: '#19 Board-Driven Protocol', s17: '#17 Satellite Bootstrap',
      s16: '#16 Cross-Session Recall'
    },
    fr: {
      interfaces: 'Interfaces',
      i1: 'I1 Revue de session', i2: 'I2 Navigateur principal', i3: 'I3 Flux de travail',
      i4: 'I4 Visualiseur projets', i5: 'I5 Mindmap vivant', i_doc: '#21 Documentation',
      essentials: 'Essentiels',
      stories: 'HISTOIRES', readme: 'README', plan: 'PLAN', links: 'LIENS', news: 'NOUVELLES', changelog: 'CHANGELOG',
      commands: 'Commandes',
      g_session: 'Session', g_normalize: 'Normalize', g_harvest: 'Harvest',
      g_publications: 'Publications', g_project: 'Projet', g_live_session: 'Session live', g_live_network: 'Réseau live',
      hubs: 'Hubs', landing: 'Accueil', publications: 'Publications', interfaces_hub: 'Interfaces', projects: 'Projets',
      profile: 'Profil', hub: 'Hub', resume: 'Résumé', full: 'Complet',
      summary: 'Résumé',
      p0: 'Système de connaissances', p1: 'Knowledge 2.0', p2: 'Session live', p3: 'Persistance IA',
      p4: 'Esprits distribués', p4a: 'Tableau de bord', p5: 'Webcards', p6: 'Normalize',
      p7: 'Harvest', p8: 'Gestion de session', p9: 'Sécurité', p9a: '#9a Conformité',
      p10: 'Réseau live', p11: 'Histoires de succès', p12: 'Gestion de projet', p13: 'Pagination',
      p14: 'Architecture', p15: 'Diagrammes', p16: 'Visualisation', p17: 'Pipeline',
      p18: 'Génération doc', p19: 'Interactif', p20: 'Métriques de session',
      p21: 'Interface principale', p22: 'Revue de session', p22b: 'Documentation visuelle', p23: 'Visualiseur Web', p24: 'Mindmap vivant',
      stories_title: 'Histoires de succès',
      s26: '#26 Un seul visualiseur pour tous', s25: '#25 Mémoire mindmap vivante',
      s24: '#24 Le Toggle', s23: '#23 Plateforme Knowledge v2.0',
      s22: '#22 Moteur de documentation visuelle', s21: '#21 Machine à états',
      s19: '#19 Protocole par tableau', s17: '#17 Bootstrap satellite',
      s16: '#16 Rappel inter-session'
    }
  };
  var t = T[LANG];

  var BASE = '{{ "" | relative_url }}';
  var CENTER_KEY  = 'navigator-center-url';
  var WIDGET_KEY  = 'navigator-widgets';
  var LPANEL_KEY  = 'navigator-left-state';
  var RPANEL_KEY  = 'navigator-right-state';
  var RCONTENT_KEY = 'navigator-right-url';
  var ACTIVE_KEY  = 'navigator-active-href';
  var SUBDET_KEY  = 'navigator-subdetails';

  /* Iframe references — src set ONCE after localStorage check (avoid double-load race) */
  var centerIframe = document.getElementById('center-frame-el');
  var rightIframe  = document.getElementById('right-frame-el');

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
  var widgets = [
    { id:'interfaces', title: t.interfaces, open:true, links:[
      {t: t.i1,  h:BASE+LP+'/interfaces/session-review/', center:true},
      {t: t.i2,  h:BASE+LP+'/interfaces/main-navigator/', top:true},
      {t: t.i3,  h:BASE+LP+'/interfaces/task-workflow/', center:true},
      {t: t.i4,  h:BASE+LP+'/interfaces/project-viewer/', center:true},
      {t: t.i5,  h:BASE+LP+'/interfaces/live-mindmap/', center:true},
      {t: t.i_doc, h:BASE+LP+'/publications/main-interface/'}
    ]},
    { id:'essentials', title: t.essentials, open:false, links:[
      {t: t.stories,   h:BASE+LP+'/publications/success-stories/'},
      {t: t.readme,    h:BASE+LP+'/'},
      {t: t.plan,      h:BASE+LP+'/plan/'},
      {t: t.links,     h:BASE+LP+'/links/'},
      {t: t.news,      h:BASE+LP+'/news/'},
      {t: t.changelog, h:BASE+LP+'/changelog/'}
    ]},
    { id:'commands', title: t.commands, open:false, groups:[
      { g: t.g_session,      pub:LP+'/publications/session-management/full/#pub-title', cmds:['wakeup','refresh','help / aide','status','save','remember','resume','recover','recall','checkpoint','elevate'] },
      { g: t.g_normalize,    pub:LP+'/publications/normalize-structure-concordance/full/#pub-title', cmds:['normalize','normalize --fix','normalize --check'] },
      { g: t.g_harvest,      pub:LP+'/publications/harvest-protocol/full/#pub-title', cmds:['harvest','harvest --list','harvest --procedure','harvest --healthcheck','harvest --review','harvest --stage','harvest --promote','harvest --auto','harvest --fix'] },
      { g: t.g_publications, pub:LP+'/publications/webcards-social-sharing/full/#pub-title', cmds:['pub list','pub check','pub new','pub sync','doc review','docs check','webcard','weblinks','pub export'] },
      { g: t.g_project,      pub:LP+'/publications/knowledge-system/full/#pub-title', cmds:['project list','project info','project create','project register','project review','#N: note','g:board:item'] },
      { g: t.g_live_session, pub:LP+'/publications/live-session-analysis/full/#pub-title', cmds:["I'm live",'multi-live','deep','analyze','recipe'] },
      { g: t.g_live_network, pub:LP+'/publications/live-knowledge-network/full/#pub-title', cmds:['beacon'] }
    ]},
    { id:'hubs', title: t.hubs, open:false, links:[
      {t: t.landing,        h:BASE+LP+'/'},
      {t: t.publications,   h:BASE+LP+'/publications/'},
      {t: t.interfaces_hub, h:BASE+LP+'/interfaces/'},
      {t: t.projects,       h:BASE+LP+'/projects/'}
    ]},
    { id:'profile', title: t.profile, open:false, links:[
      {t: t.hub,    h:BASE+LP+'/profile/'},
      {t: t.resume, h:BASE+LP+'/profile/resume/'},
      {t: t.full,   h:BASE+LP+'/profile/full/'}
    ]},
    { id:'publications', title: t.publications, open:false, pubs:[
      {n:'#24', t: t.p24,  s:'live-mindmap'},
      {n:'#23', t: t.p23,  s:'web-documentation-viewer'},
      {n:'#22', t: t.p22b, s:'visual-documentation'},
      {n:'#22', t: t.p22,  s:'session-review'},
      {n:'#21', t: t.p21,  s:'main-interface'},
      {n:'#20', t: t.p20,  s:'session-metrics-time'},
      {n:'#19', t: t.p19,  s:'interactive-work-sessions'},
      {n:'#18', t: t.p18,  s:'documentation-generation'},
      {n:'#17', t: t.p17,  s:'web-production-pipeline'},
      {n:'#16', t: t.p16,  s:'web-page-visualization'},
      {n:'#15', t: t.p15,  s:'architecture-diagrams'},
      {n:'#14', t: t.p14,  s:'architecture-analysis'},
      {n:'#13', t: t.p13,  s:'web-pagination-export'},
      {n:'#12', t: t.p12,  s:'project-management'},
      {n:'#11', t: t.p11,  s:'success-stories'},
      {n:'#10', t: t.p10,  s:'live-knowledge-network'},
      {n:'#9',  t: t.p9,   s:'security-by-design',
        extra:[{t: t.p9a, p:LP+'/publications/security-by-design/compliance/'}]},
      {n:'#8',  t: t.p8,   s:'session-management'},
      {n:'#7',  t: t.p7,   s:'harvest-protocol'},
      {n:'#6',  t: t.p6,   s:'normalize-structure-concordance'},
      {n:'#5',  t: t.p5,   s:'webcards-social-sharing'},
      {n:'#4a', t: t.p4a,  s:'distributed-knowledge-dashboard'},
      {n:'#4',  t: t.p4,   s:'distributed-minds'},
      {n:'#3',  t: t.p3,   s:'ai-session-persistence'},
      {n:'#2',  t: t.p2,   s:'live-session-analysis'},
      {n:'#1',  t: t.p1,   s:'knowledge-2.0'},
      {n:'#0',  t: t.p0,   s:'knowledge-system'}
    ]},
    { id:'stories', title: t.stories_title, open:false, links:[
      {t: t.s26, h:BASE+LP+'/publications/success-stories/story-26/'},
      {t: t.s25, h:BASE+LP+'/publications/success-stories/story-25/'},
      {t: t.s24, h:BASE+LP+'/publications/success-stories/story-24/'},
      {t: t.s23, h:BASE+LP+'/publications/success-stories/story-23/'},
      {t: t.s22, h:BASE+LP+'/publications/success-stories/story-22/'},
      {t: t.s21, h:BASE+LP+'/publications/success-stories/story-21/'},
      {t: t.s19, h:BASE+LP+'/publications/success-stories/story-19/'},
      {t: t.s17, h:BASE+LP+'/publications/success-stories/story-17/'},
      {t: t.s16, h:BASE+LP+'/publications/success-stories/story-16/'}
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

    // Rewrite link href if viewerRewriteUrl is available (running inside viewer srcdoc)
    var vru = (typeof viewerRewriteUrl === 'function') ? viewerRewriteUrl : function(u) { return u; };

    if (w.links) {
      w.links.forEach(function(lk) {
        var a = document.createElement('a'); a.href = lk.top ? vru(lk.h, false) : vru(lk.h);
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
          var a = document.createElement('a'); a.href = vru(BASE + cg.pub); a.target = 'content-frame';
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
        var a1 = document.createElement('a'); a1.href = vru(BASE+LP+'/publications/'+p.s+'/');
        a1.dataset.navId = 'nav-' + (navLinkId++);
        a1.target = 'content-frame'; a1.textContent = t.summary; pg.appendChild(a1);
        var a2 = document.createElement('a'); a2.href = vru(BASE+LP+'/publications/'+p.s+'/full/');
        a2.dataset.navId = 'nav-' + (navLinkId++);
        a2.target = 'content-frame'; a2.textContent = t.full; pg.appendChild(a2);
        if (p.extra) { p.extra.forEach(function(e) {
          var ax = document.createElement('a'); ax.href = vru(BASE+e.p);
          ax.dataset.navId = 'nav-' + (navLinkId++);
          ax.target = 'content-frame'; ax.textContent = e.t; pg.appendChild(ax);
        }); }
        body.appendChild(pg);
      });
    }
    det.appendChild(body); panel.appendChild(det);
  });

  /* ─── Adapt saved URL to current language ─── */
  function adaptLang(url) {
    if (!url) return url;
    // Viewer URLs (index.html?doc=...): toggle &lang=fr
    if (url.indexOf('index.html?doc=') !== -1) {
      var cleaned = url.replace(/[&?]lang=fr/g, '').replace(/\?&/, '?').replace(/\?$/, '');
      return LANG === 'fr' ? (cleaned + (cleaned.indexOf('?') !== -1 ? '&' : '?') + 'lang=fr') : cleaned;
    }
    // Direct page URLs: toggle /fr/ prefix
    var stripped = url.replace(BASE + '/fr/', BASE + '/');
    return LANG === 'fr' ? stripped.replace(BASE + '/', BASE + '/fr/') : stripped;
  }

  /* ─── Restore last viewed pages (or set defaults) ─── */
  var savedCenter = localStorage.getItem(CENTER_KEY);
  if (centerIframe) { centerIframe.src = savedCenter ? adaptLang(savedCenter) : (BASE + LP + '/interfaces/task-workflow/'); }
  var savedRight = localStorage.getItem(RCONTENT_KEY);
  if (rightIframe) { rightIframe.src = savedRight ? adaptLang(savedRight) : (BASE + LP + '/'); }

  /* ─── Restore active link highlight ─── */
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
    /* Save center URL if targeting center (language-neutral) */
    if (a.target === 'center-frame') { localStorage.setItem(CENTER_KEY, a.href); }
    /* Save right URL + extend panel if collapsed (language-neutral) */
    if (a.target === 'content-frame') {
      localStorage.setItem(RCONTENT_KEY, a.href);
      if (rightW < 100) { rightW = Math.round(grid.offsetWidth * 0.5); applyGrid(true); }
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

})();
</script>
{:/nomarkdown}
