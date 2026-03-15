---
layout: publication
page_type: interface
title: "Main Navigator"
description: "Knowledge system main navigation interface: three-panel browser with widget directory, extensible content viewer, and full command reference."
pub_id: "Main Navigator · I2"
version: "v4"
date: "2026-03-01"
permalink: /interfaces/main-navigator/
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

  <!-- LEFT — Widget Directory -->
  <div class="nav-panel" id="left-panel"></div>

  <!-- LEFT DIVIDER — open/close toggle -->
  <div class="nav-divider-left" id="left-toggle"><span>◀</span></div>

  <!-- CENTER — Content Viewer (left panel links load here) -->
  <div class="nav-center" id="center-panel">
    <iframe name="center-frame" src="{{ '/interfaces/task-workflow/' | relative_url }}"></iframe>
  </div>

  <!-- RIGHT DIVIDER — bidirectional arrows -->
  <div class="nav-divider-right" id="right-toggle">
    <span class="r-arrow" data-dir="extend" title="Extend viewer">◀</span>
    <span class="r-arrow hidden" data-dir="collapse" title="Collapse viewer">▶</span>
  </div>

  <!-- RIGHT — Content Viewer -->
  <div class="nav-viewer">
    <iframe name="content-frame" src="{{ '/' | relative_url }}"></iframe>
  </div>

</div>

<script>
(function() {
  var BASE = '{{ "" | relative_url }}';
  var CENTER_KEY  = 'navigator-center-url';
  var WIDGET_KEY  = 'navigator-widgets';
  var LPANEL_KEY  = 'navigator-left-state';
  var RPANEL_KEY  = 'navigator-right-state';

  var RCONTENT_KEY = 'navigator-right-url';
  var ACTIVE_KEY  = 'navigator-active-href';
  var SUBDET_KEY  = 'navigator-subdetails';
  var centerIframe = document.querySelector('iframe[name="center-frame"]');
  var rightIframe  = document.querySelector('iframe[name="content-frame"]');
  var panel  = document.getElementById('left-panel');
  var grid   = document.getElementById('nav-grid');
  var lToggle = document.getElementById('left-toggle');
  var rToggle = document.getElementById('right-toggle');
  if (!panel || !grid) return;


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

  /* ─── Widget definitions ─── */
  /* Full widget set — pages will be created progressively. */
  var widgets = [
    { id:'interfaces', title:'Interfaces', open:true, links:[
      {t:'I1 Session Review',  h:BASE+'/interfaces/session-review/', center:true},
      {t:'I2 Main Navigator',  h:BASE+'/interfaces/main-navigator/', top:true},
      {t:'I3 Tasks Workflow',  h:BASE+'/interfaces/task-workflow/', center:true},
      {t:'I4 Project Viewer', h:BASE+'/interfaces/project-viewer/', center:true},
      {t:'#21 Documentation',  h:BASE+'/publications/main-interface/'}
    ]},
    { id:'essentials', title:'Essentials', open:false, links:[
      {t:'STORIES',    h:BASE+'/publications/success-stories/'},
      {t:'README',     h:BASE+'/'},
      {t:'PLAN',       h:BASE+'/plan/'},
      {t:'LINKS',      h:BASE+'/links/'},
      {t:'NEWS',       h:BASE+'/news/'},
      {t:'CHANGELOG',  h:BASE+'/changelog/'}
    ]},
    { id:'commands', title:'Commands', open:false, groups:[
      { g:'Session', pub:'/publications/session-management/full/#pub-title', cmds:['wakeup','refresh','help / aide','status','save','remember','resume','recover','recall','checkpoint','elevate'] },
      { g:'Normalize', pub:'/publications/normalize-structure-concordance/full/#pub-title', cmds:['normalize','normalize --fix','normalize --check'] },
      { g:'Harvest', pub:'/publications/harvest-protocol/full/#pub-title', cmds:['harvest','harvest --list','harvest --procedure','harvest --healthcheck','harvest --review','harvest --stage','harvest --promote','harvest --auto','harvest --fix'] },
      { g:'Publications', pub:'/publications/webcards-social-sharing/full/#pub-title', cmds:['pub list','pub check','pub new','pub sync','doc review','docs check','webcard','weblinks','pub export'] },
      { g:'Project', pub:'/publications/knowledge-system/full/#pub-title', cmds:['project list','project info','project create','project register','project review','#N: note','g:board:item'] },
      { g:'Live Session', pub:'/publications/live-session-analysis/full/#pub-title', cmds:["I'm live",'multi-live','deep','analyze','recipe'] },
      { g:'Live Network', pub:'/publications/live-knowledge-network/full/#pub-title', cmds:['beacon'] }
    ]},
    { id:'hubs', title:'Hubs', open:false, links:[
      {t:'Landing',      h:BASE+'/'},
      {t:'Publications', h:BASE+'/publications/'},
      {t:'Interfaces',   h:BASE+'/interfaces/'},
      {t:'Projects',     h:BASE+'/projects/'}
    ]},
    { id:'profile', title:'Profile', open:false, links:[
      {t:'Hub',    h:BASE+'/profile/'},
      {t:'Resume', h:BASE+'/profile/resume/'},
      {t:'Full',   h:BASE+'/profile/full/'}
    ]},
    { id:'publications', title:'Publications', open:false, pubs:[
      {n:'#0',  t:'Knowledge System',  s:'knowledge-system'},
      {n:'#1',  t:'Knowledge 2.0',     s:'knowledge-2.0'},
      {n:'#2',  t:'Live Session',      s:'live-session-analysis'},
      {n:'#3',  t:'AI Persistence',    s:'ai-session-persistence'},
      {n:'#4',  t:'Distributed Minds', s:'distributed-minds'},
      {n:'#4a', t:'Dashboard',         s:'distributed-knowledge-dashboard'},
      {n:'#5',  t:'Webcards',          s:'webcards-social-sharing'},
      {n:'#6',  t:'Normalize',         s:'normalize-structure-concordance'},
      {n:'#7',  t:'Harvest',           s:'harvest-protocol'},
      {n:'#8',  t:'Session Mgmt',      s:'session-management'},
      {n:'#9',  t:'Security',          s:'security-by-design',
        extra:[{t:'#9a Compliance', p:'/publications/security-by-design/compliance/'}]},
      {n:'#10', t:'Live Network',      s:'live-knowledge-network'},
      {n:'#11', t:'Success Stories',   s:'success-stories'},
      {n:'#12', t:'Project Mgmt',      s:'project-management'},
      {n:'#13', t:'Pagination',        s:'web-pagination-export'},
      {n:'#14', t:'Architecture',      s:'architecture-analysis'},
      {n:'#15', t:'Diagrams',          s:'architecture-diagrams'},
      {n:'#16', t:'Visualization',     s:'web-page-visualization'},
      {n:'#17', t:'Pipeline',          s:'web-production-pipeline'},
      {n:'#18', t:'Doc Generation',    s:'documentation-generation'},
      {n:'#19', t:'Interactive',       s:'interactive-work-sessions'},
      {n:'#20', t:'Session Metrics',   s:'session-metrics-time'},
      {n:'#21', t:'Main Interface',    s:'main-interface'},
      {n:'#22', t:'Session Review',    s:'session-review'}
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
        var a1 = document.createElement('a'); a1.href = BASE+'/publications/'+p.s+'/#pub-title';
        a1.dataset.navId = 'nav-' + (navLinkId++);
        a1.target = 'content-frame'; a1.textContent = 'Summary'; pg.appendChild(a1);
        var a2 = document.createElement('a'); a2.href = BASE+'/publications/'+p.s+'/full/#pub-title';
        a2.dataset.navId = 'nav-' + (navLinkId++);
        a2.target = 'content-frame'; a2.textContent = 'Full'; pg.appendChild(a2);
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

  /* ─── Restore last viewed pages ─── */
  var savedCenter = localStorage.getItem(CENTER_KEY);
  if (savedCenter && centerIframe) { centerIframe.src = savedCenter; }
  var savedRight = localStorage.getItem(RCONTENT_KEY);
  if (savedRight && rightIframe) { rightIframe.src = savedRight; }

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
    /* Save center URL if targeting center */
    if (a.target === 'center-frame') { localStorage.setItem(CENTER_KEY, a.href); }
    /* Save right URL + extend panel if collapsed */
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
      /* ─── Right panel routing rules ─── */
      /* Interface links in right panel → center-frame; Main Navigator → _top */
      try {
        var rDoc = rightIframe.contentDocument;
        if (!rDoc) return;
        rDoc.addEventListener('click', function(e) {
          var a = e.target.closest('a');
          if (!a) return;
          var href = a.getAttribute('href') || '';
          /* Resolve internal path via viewer rewriter if available */
          var resolved = (typeof viewerRewriteUrl === 'function') ? viewerRewriteUrl(href, false) : href;
          /* Detect interface paths */
          var isInterface = /\/interfaces\//.test(href) || /\/interfaces\//.test(resolved);
          var isMainNav = /\/interfaces\/main-navigator\//.test(href) || /\/interfaces\/main-navigator\//.test(resolved);
          if (isMainNav) {
            e.preventDefault();
            window.top.location.reload();
          } else if (isInterface && centerIframe) {
            e.preventDefault();
            var embedUrl = (typeof viewerRewriteUrl === 'function') ? viewerRewriteUrl(href) : href;
            centerIframe.src = embedUrl;
            localStorage.setItem(CENTER_KEY, embedUrl);
          }
        });
      } catch(e) {}
    });
  }

  /* Language and orientation are handled by the viewer's top toolbar */

})();

/* Export and theme propagation handled by the viewer */
</script>
{:/nomarkdown}
