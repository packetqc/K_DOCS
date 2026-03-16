// ═══ Session Review — Core (session-core.js) ═══
// Shared state, i18n, utilities, init, dropdown, and session selection.
// Other modules attach to window.SV namespace.

// Landscape default — per-page key only
(function() {
  var KEY = 'knowledge-orient:' + location.pathname.replace(/\/+$/, '');
  if (!localStorage.getItem(KEY)) localStorage.setItem(KEY, 'landscape');
})();

(function() {
  'use strict';

  // ── Shared namespace ──
  var SV = window.SV = {};

  // ── Config ──
  var viewerEl = document.getElementById('session-viewer');
  SV.lang = (document.documentElement.lang === 'fr' || window.location.pathname.indexOf('/fr/') !== -1) ? 'fr' : 'en';
  SV.baseurl = viewerEl.getAttribute('data-baseurl') || '';
  SV.REPO = viewerEl.getAttribute('data-repo') || 'packetqc/knowledge';
  SV.dataUrl = SV.baseurl + '/data/sessions.json';
  SV.sessionsData = null;
  SV.currentSession = null;

  // ── i18n ──
  var L = {
    en: {
      selectSession: '\u2014 Select a session \u2014',
      sessionsAvailable: 'sessions available',
      selectPrompt: 'Select a session from the dropdown above to view its full report.',
      prCount: 'Pull Requests',
      taskCount: 'Tasks',
      lessonCount: 'Lessons',
      noPRs: 'No pull requests recorded.',
      noLessons: 'No lessons recorded for this session.',
      timeNote: 'Time data compiled from commit timestamps and task creation times.',
      view: 'View',
      totals: 'Totals',
      error: 'Failed to load sessions data.',
      noTitle: '(untitled)',
      category: 'Category',
      allSections: 'All sections',
      source: 'Source file',
      srcPR: 'PRs',
      srcNotes: 'Notes',
      srcTask: 'Task',
      noCompilation: 'This session predates the compilation feature (v50). Only PR delivery data is available \u2014 no detailed metrics or time blocks.',
      prOnly: 'This session was reconstructed from Pull Request data. No session notes or GitHub task were created at the time.',
      generated: 'Generated from',
      start: 'Start',
      end: 'End',
      duration: 'Duration',
      task: 'Task (PR)',
      morning: 'Morning',
      afternoon: 'Afternoon',
      evening: 'Evening',
      calendarTime: 'Calendar time',
      calendar: 'Calendar',
      inactive: 'Inactive',
      tasks: 'tasks',
      noTimeData: 'No time data available for this session.',
      status: 'Status',
      additions: 'Additions',
      deletions: 'Deletions',
      linesChanged: 'Lines changed',
      filesChanged: 'Files changed',
      commits: 'Commits',
      linesPerHour: 'Lines/hour',
      commitsPerHour: 'Commits/hour',
      filesPerHour: 'Files/hour',
      velocity: 'Velocity',
      deliverables: 'Deliverables',
      activeTime: 'Active time',
      timeBlock: 'Time block',
      velocityTitle: 'Velocity & Code Impact',
      codeImpact: 'Code Impact by PR',
      additionsLabel: 'Additions',
      deletionsLabel: 'Deletions',
      avgPerPR: 'avg/PR',
      subFeat: 'Feature',
      subFix: 'Fix',
      subDoc: 'Documentation',
      subTest: 'Test / QA',
      subRefactor: 'Refactor',
      subChore: 'Chore',
      reqType: 'Request type',
      engStage: 'Eng. stage',
      rtFix: 'Fix', rtFeature: 'Feature', rtInvestigation: 'Investigation',
      rtEnhancement: 'Enhancement', rtTesting: 'Testing', rtValidation: 'Validation',
      rtDocumentation: 'Documentation', rtDeployment: 'Deployment', rtConception: 'Design',
      rtReview: 'Review', rtChore: 'Chore',
      stAnalysis: 'Analysis', stPlanning: 'Planning', stDesign: 'Design',
      stImplementation: 'Implementation', stTesting: 'Testing', stValidation: 'Validation',
      stReview: 'Review', stDeployment: 'Deployment', stOperations: 'Operations',
      stImprovement: 'Improvement',
      taskCol: 'Task',
      typeCol: 'Type',
      titleCol: 'Title',
      taskTypeSession: 'Session',
      taskTypeRelated: 'Related',
      sessionCol: 'Session',
      openSession: 'Open',
      openTab: 'New tab',
      scopeTitle: 'Session Scope',
      scopeChildren: 'Child Sessions',
      scopeRelated: 'Related Tasks',
      userSession: 'User Session',
      systemSessions: 'System Sessions',
      collateralTasks: 'Collateral Tasks',
      mainTask: 'Main Task',
      subTask: 'Sub-task',
      sessionIdentity: 'Session Identity',
      internalId: 'Internal ID',
      noCollateral: 'No collateral tasks recorded.',
      taskProgression: 'Task Progression',
      openTaskViewer: 'Open in Task Viewer',
      progressStage: 'Current Stage',
      progressCompleted: 'Completed',
      progressInProgress: 'In Progress',
      progressPending: 'Pending',
      noProgression: 'No progression data available.'
    },
    fr: {
      selectSession: '\u2014 Choisir une session \u2014',
      sessionsAvailable: 'sessions disponibles',
      selectPrompt: 'S\u00e9lectionnez une session ci-dessus pour afficher son rapport complet.',
      prCount: 'Pull Requests',
      taskCount: 'T\u00e2ches',
      lessonCount: 'Le\u00e7ons',
      noPRs: 'Aucun pull request enregistr\u00e9.',
      noLessons: 'Aucune le\u00e7on enregistr\u00e9e pour cette session.',
      timeNote: 'Donn\u00e9es de temps compil\u00e9es \u00e0 partir des timestamps de commits et de cr\u00e9ation des t\u00e2ches.',
      view: 'Voir',
      totals: 'Totaux',
      error: 'Erreur de chargement des donn\u00e9es de sessions.',
      noTitle: '(sans titre)',
      category: 'Cat\u00e9gorie',
      allSections: 'Toutes les sections',
      source: 'Fichier source',
      srcPR: 'PRs',
      srcNotes: 'Notes',
      srcTask: 'T\u00e2che',
      noCompilation: 'Cette session pr\u00e9c\u00e8de la fonctionnalit\u00e9 de compilation (v50). Seules les donn\u00e9es de livraison PR sont disponibles \u2014 pas de m\u00e9triques ni de blocs temporels d\u00e9taill\u00e9s.',
      prOnly: 'Cette session a \u00e9t\u00e9 reconstruite \u00e0 partir des donn\u00e9es de Pull Requests. Aucune note de session ni t\u00e2che GitHub n\u2019a \u00e9t\u00e9 cr\u00e9\u00e9e \u00e0 l\u2019\u00e9poque.',
      generated: 'G\u00e9n\u00e9r\u00e9 \u00e0 partir de',
      start: 'D\u00e9but',
      end: 'Fin',
      duration: 'Dur\u00e9e',
      task: 'T\u00e2che (PR)',
      morning: 'Matin',
      afternoon: 'Apr\u00e8s-midi',
      evening: 'Soir',
      calendarTime: 'Temps calendrier',
      calendar: 'Calendrier',
      inactive: 'Inactif',
      tasks: 't\u00e2ches',
      noTimeData: 'Aucune donn\u00e9e de temps disponible pour cette session.',
      status: 'Statut',
      additions: 'Ajouts',
      deletions: 'Suppressions',
      linesChanged: 'Lignes modifi\u00e9es',
      filesChanged: 'Fichiers modifi\u00e9s',
      commits: 'Commits',
      linesPerHour: 'Lignes/heure',
      commitsPerHour: 'Commits/heure',
      filesPerHour: 'Fichiers/heure',
      velocity: 'V\u00e9locit\u00e9',
      deliverables: 'Livrables',
      activeTime: 'Temps actif',
      timeBlock: 'Bloc horaire',
      velocityTitle: 'V\u00e9locit\u00e9 & Impact du code',
      codeImpact: 'Impact du code par PR',
      additionsLabel: 'Ajouts',
      deletionsLabel: 'Suppressions',
      avgPerPR: 'moy/PR',
      subFeat: 'Fonctionnalit\u00e9',
      subFix: 'Correctif',
      subDoc: 'Documentation',
      subTest: 'Test / QA',
      subRefactor: 'Refactorisation',
      subChore: 'Maintenance',
      reqType: 'Type de demande',
      engStage: 'Phase ing.',
      rtFix: 'Correctif', rtFeature: 'Fonctionnalit\u00e9', rtInvestigation: 'Investigation',
      rtEnhancement: 'Am\u00e9lioration', rtTesting: 'Test', rtValidation: 'Validation',
      rtDocumentation: 'Documentation', rtDeployment: 'D\u00e9ploiement', rtConception: 'Conception',
      rtReview: 'R\u00e9vision', rtChore: 'Maintenance',
      stAnalysis: 'Analyse', stPlanning: 'Planification', stDesign: 'Conception',
      stImplementation: 'Impl\u00e9mentation', stTesting: 'Test', stValidation: 'Validation',
      stReview: 'R\u00e9vision', stDeployment: 'D\u00e9ploiement', stOperations: 'Op\u00e9rations',
      stImprovement: 'Am\u00e9lioration',
      taskCol: 'T\u00e2che',
      typeCol: 'Type',
      titleCol: 'Titre',
      taskTypeSession: 'Session',
      taskTypeRelated: 'Li\u00e9e',
      sessionCol: 'Session',
      openSession: 'Ouvrir',
      openTab: 'Nouvel onglet',
      scopeTitle: 'Port\u00e9e de la session',
      scopeChildren: 'Sessions enfants',
      scopeRelated: 'T\u00e2ches li\u00e9es',
      userSession: 'Session utilisateur',
      systemSessions: 'Sessions syst\u00e8me',
      collateralTasks: 'T\u00e2ches collat\u00e9rales',
      mainTask: 'T\u00e2che principale',
      subTask: 'Sous-t\u00e2che',
      sessionIdentity: 'Identit\u00e9 de session',
      internalId: 'ID interne',
      noCollateral: 'Aucune t\u00e2che collat\u00e9rale enregistr\u00e9e.',
      taskProgression: 'Progression de la t\u00e2che',
      openTaskViewer: 'Ouvrir dans le Task Viewer',
      progressStage: '\u00c9tape courante',
      progressCompleted: 'Termin\u00e9',
      progressInProgress: 'En cours',
      progressPending: 'En attente',
      noProgression: 'Aucune donn\u00e9e de progression disponible.'
    }
  };
  SV.t = L[SV.lang] || L.en;

  // ── Engineering Taxonomy ──
  var t = SV.t;
  SV.reqTypeMap = {
    fix:            { emoji: '\ud83d\udd27', label: t.rtFix },
    feature:        { emoji: '\ud83d\ude80', label: t.rtFeature },
    investigation:  { emoji: '\ud83d\udd0d', label: t.rtInvestigation },
    enhancement:    { emoji: '\ud83d\udd04', label: t.rtEnhancement },
    testing:        { emoji: '\ud83e\uddea', label: t.rtTesting },
    validation:     { emoji: '\u2705',       label: t.rtValidation },
    documentation:  { emoji: '\ud83d\udcdd', label: t.rtDocumentation },
    deployment:     { emoji: '\ud83d\udce6', label: t.rtDeployment },
    conception:     { emoji: '\ud83d\udca1', label: t.rtConception },
    review:         { emoji: '\ud83d\udc41\ufe0f', label: t.rtReview },
    chore:          { emoji: '\u2699\ufe0f', label: t.rtChore }
  };
  SV.engStageMap = {
    analysis:       { emoji: '\ud83d\udd0d', label: t.stAnalysis },
    planning:       { emoji: '\ud83d\udccb', label: t.stPlanning },
    design:         { emoji: '\ud83c\udfa8', label: t.stDesign },
    implementation: { emoji: '\ud83d\udee0\ufe0f', label: t.stImplementation },
    testing:        { emoji: '\ud83e\uddea', label: t.stTesting },
    validation:     { emoji: '\u2705',       label: t.stValidation },
    review:         { emoji: '\ud83d\udc41\ufe0f', label: t.stReview },
    deployment:     { emoji: '\ud83d\ude80', label: t.stDeployment },
    operations:     { emoji: '\u2699\ufe0f', label: t.stOperations },
    improvement:    { emoji: '\ud83d\udcc8', label: t.stImprovement }
  };

  // ── Utility functions ──
  SV.reqTypeBadge = function(rt) {
    if (!rt) return '';
    var info = SV.reqTypeMap[rt] || { emoji: '\u2022', label: rt };
    return info.emoji + ' ' + info.label;
  };
  SV.engStageBadge = function(st) {
    if (!st) return '';
    var info = SV.engStageMap[st] || { emoji: '\u2022', label: st };
    return info.emoji + ' ' + info.label;
  };
  SV.esc = function(str) {
    var d = document.createElement('div');
    d.appendChild(document.createTextNode(str));
    return d.innerHTML;
  };
  SV.formatTime = function(isoStr) {
    if (!isoStr) return '\u2014';
    var d = new Date(isoStr);
    return ('0'+d.getHours()).slice(-2) + ':' + ('0'+d.getMinutes()).slice(-2);
  };
  SV.calcDuration = function(startIso, endIso) {
    if (!startIso || !endIso) return null;
    var ms = new Date(endIso) - new Date(startIso);
    return Math.round(ms / 60000);
  };
  SV.formatDuration = function(minutes) {
    if (minutes == null || minutes < 0) return '\u2014';
    if (minutes === 0) return '<1min';
    if (minutes < 60) return '~' + minutes + 'min';
    var h = Math.floor(minutes / 60);
    var m = minutes % 60;
    return '~' + h + 'h' + (m > 0 ? ('0'+m).slice(-2) : '');
  };
  SV.timeBlock = function(isoStr) {
    if (!isoStr) return '\u2014';
    var h = new Date(isoStr).getHours();
    if (h >= 5 && h < 12) return t.morning;
    if (h >= 12 && h < 18) return t.afternoon;
    return t.evening;
  };
  SV.localDate = function(isoStr) {
    if (!isoStr) return null;
    var d = new Date(isoStr);
    return d.getFullYear() + '-' + ('0'+(d.getMonth()+1)).slice(-2) + '-' + ('0'+d.getDate()).slice(-2);
  };
  SV.effectiveTime = function(s) {
    return (s.aggregated ? s.aggregated.last_activity_time : null)
      || s.last_activity_time || s.last_pr_time || s.first_activity_time;
  };
  SV.findSession = function(id) {
    if (!SV.sessionsData) return null;
    for (var i = 0; i < SV.sessionsData.sessions.length; i++) {
      if (SV.sessionsData.sessions[i].id === id) return SV.sessionsData.sessions[i];
    }
    return null;
  };
  SV.taskLabel = function(num) {
    var map = (SV.sessionsData && SV.sessionsData.task_labels) || {};
    var info = map[String(num)];
    return info ? info.label : null;
  };
  SV.taskLabelBadge = function(num, fallback) {
    var lbl = SV.taskLabel(num);
    if (!lbl) return '<span class="sv-task-type sv-task-type-related">' + SV.esc(fallback) + '</span>';
    var cls = 'sv-task-label-' + lbl.toLowerCase().replace(/[^a-z]/g, '');
    return '<span class="sv-task-type ' + cls + '">' + SV.esc(lbl) + '</span>';
  };
  SV.isDarkTheme = function() {
    var dt = document.documentElement.getAttribute('data-theme') || '';
    return (dt === 'midnight' || dt === 'daltonism-dark') ||
      (!dt || dt === 'auto') && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  };

  // ── DOM refs ──
  var selectEl = document.getElementById('sv-session-select');
  var emptyEl = document.getElementById('sv-empty-state');
  var contentEl = document.getElementById('sv-content');
  var countEl = document.getElementById('sv-session-count');

  // ── All Sessions label ──
  var allSessionsLabel = SV.lang === 'fr' ? '\u2014 Toutes les sessions \u2014' : '\u2014 All Sessions \u2014';
  var overviewEl = document.getElementById('sv-view-overview');

  // ── Dropdown population ──
  function populateDropdown(sessions) {
    selectEl.innerHTML = '<option value="">' + allSessionsLabel + '</option>';
    var supported = sessions;
    var byDate = {};
    supported.forEach(function(s) {
      var refTime = SV.effectiveTime(s);
      var d = (refTime ? SV.localDate(refTime) : s.date) || 'unknown';
      if (!byDate[d]) byDate[d] = [];
      byDate[d].push(s);
    });
    Object.keys(byDate).sort().reverse().forEach(function(date) {
      var group = document.createElement('optgroup');
      group.label = date;
      byDate[date].sort(function(a, b) {
        var ta = SV.effectiveTime(a) || '';
        var tb = SV.effectiveTime(b) || '';
        return ta < tb ? -1 : ta > tb ? 1 : 0;
      });
      byDate[date].forEach(function(s) {
        var opt = document.createElement('option');
        opt.value = s.id;
        var suffix = '';
        var rtInfo = s.request_type ? SV.reqTypeMap[s.request_type] : null;
        if (rtInfo) suffix += rtInfo.emoji;
        if (s.pr_count > 0) suffix += '\ud83d\udce6';
        if (s.has_notes) suffix += '\ud83d\udccb';
        if (s.has_task) suffix += '\ud83c\udfab';
        var timePrefix = SV.effectiveTime(s) ? SV.formatTime(SV.effectiveTime(s)) + ' ' : '';
        var label = s.title || t.noTitle;
        if (label.length > 50) label = label.substring(0, 47) + '...';
        var taskTag = s.task_number ? '#' + s.task_number + ' ' : '';
        var kindEmoji = s.session_kind === 'continuation' ? '\ud83d\udd01 ' : '\ud83d\udcac ';
        opt.textContent = timePrefix + taskTag + kindEmoji + label + (suffix ? ' ' + suffix : '');
        group.appendChild(opt);
      });
      selectEl.appendChild(group);
    });
    countEl.textContent = supported.length;
  }

  // ── Show session ──
  SV.showSession = function(id) {
    // "All Sessions" overview mode
    if (!id) {
      SV.currentSession = null;
      if (SV.destroyCharts) SV.destroyCharts();
      emptyEl.style.display = 'none';
      contentEl.style.display = 'none';
      if (overviewEl) {
        overviewEl.style.display = '';
        renderSessionOverview();
      }
      localStorage.removeItem('sv-selected-session');
      return;
    }
    // Hide overview when viewing a single session
    if (overviewEl) overviewEl.style.display = 'none';

    var s = SV.findSession(id);
    if (!s) {
      SV.currentSession = null;
      if (SV.destroyCharts) SV.destroyCharts();
      emptyEl.style.display = '';
      contentEl.style.display = 'none';
      return;
    }
    SV.currentSession = s;
    emptyEl.style.display = 'none';
    contentEl.style.display = '';
    localStorage.setItem('sv-selected-session', id);

    // Delegate to render modules
    if (SV.renderSummary) SV.renderSummary(s);
    if (SV.renderMetrics) SV.renderMetrics(s);
    if (SV.renderTime) SV.renderTime(s);
    if (SV.renderDeliveries) SV.renderDeliveries(s);
    if (SV.renderTasks) SV.renderTasks(s);
    if (SV.renderLessons) SV.renderLessons(s);
    if (SV.renderCollateral) SV.renderCollateral(s);
    if (SV.renderTasks) SV.renderTasks(s);
    if (SV.renderProgression) SV.renderProgression(s);
    if (SV.renderVelocity) SV.renderVelocity(s);
    if (SV.renderAllCharts) SV.renderAllCharts(s);
  };

  // ── Overview rendering (All Sessions) ──
  function renderSessionOverview() {
    if (!SV.sessionsData || !overviewEl) return;
    var sessions = SV.sessionsData.sessions || [];

    // Aggregate stats
    var totalSessions = sessions.length;
    var totalPRs = 0;
    var totalAdds = 0;
    var totalDels = 0;
    var totalActive = 0;
    sessions.forEach(function(s) {
      var d = SV.effectiveData(s);
      totalPRs += d.prCount;
      totalAdds += d.additions;
      totalDels += d.deletions;
      totalActive += d.active;
    });

    var statsEl = document.getElementById('sv-overview-stats');
    if (statsEl) {
      var activeFmt = totalActive >= 60
        ? Math.floor(totalActive / 60) + 'h ' + (totalActive % 60) + 'm'
        : totalActive + 'm';
      statsEl.innerHTML =
        '<div class="sv-stat-card"><div class="sv-stat-value">' + totalSessions + '</div><div class="sv-stat-label">Sessions</div></div>' +
        '<div class="sv-stat-card"><div class="sv-stat-value">' + totalPRs + '</div><div class="sv-stat-label">' + t.prCount + '</div></div>' +
        '<div class="sv-stat-card"><div class="sv-stat-value">+' + totalAdds.toLocaleString() + '</div><div class="sv-stat-label">' + t.additions + '</div></div>' +
        '<div class="sv-stat-card"><div class="sv-stat-value">-' + totalDels.toLocaleString() + '</div><div class="sv-stat-label">' + t.deletions + '</div></div>' +
        '<div class="sv-stat-card"><div class="sv-stat-value">' + activeFmt + '</div><div class="sv-stat-label">' + t.activeTime + '</div></div>';
    }

    // Session cards
    var cardsEl = document.getElementById('sv-session-cards');
    if (!cardsEl) return;

    // Sort by date descending
    var sorted = sessions.slice().sort(function(a, b) {
      var ta = SV.effectiveTime(a) || a.date || '';
      var tb = SV.effectiveTime(b) || b.date || '';
      return tb.localeCompare(ta);
    });

    var html = '';
    sorted.forEach(function(s) {
      var d = SV.effectiveData(s);
      var title = SV.esc(s.title || t.noTitle);
      if (title.length > 60) title = title.substring(0, 57) + '...';
      var date = SV.localDate(SV.effectiveTime(s)) || s.date || '';
      var time = SV.effectiveTime(s) ? SV.formatTime(SV.effectiveTime(s)) : '';
      var taskTag = s.task_number ? '#' + s.task_number + ' ' : '';
      var rtBadge = s.request_type ? SV.reqTypeBadge(s.request_type) + ' ' : '';

      html += '<div class="sv-card" data-session-id="' + SV.esc(s.id) + '">';
      html += '<div class="sv-card-title">' + taskTag + title + '</div>';
      html += '<div class="sv-card-meta">';
      html += '<span>' + date + (time ? ' ' + time : '') + '</span>';
      html += '<span>' + d.prCount + ' PRs</span>';
      html += '<span>+' + d.additions.toLocaleString() + '/-' + d.deletions.toLocaleString() + '</span>';
      if (s.request_type) html += '<span>' + rtBadge + '</span>';
      html += '</div>';
      html += '</div>';
    });
    cardsEl.innerHTML = html;

    // Click handlers on cards
    cardsEl.querySelectorAll('.sv-card').forEach(function(card) {
      card.addEventListener('click', function() {
        var id = card.getAttribute('data-session-id');
        selectEl.value = id;
        SV.showSession(id);
      });
    });
  }

  // ── Data loading ──
  fetch(SV.dataUrl)
    .then(function(r) { return r.json(); })
    .then(function(data) {
      SV.sessionsData = data;
      populateDropdown(data.sessions);
      var urlParams = new URLSearchParams(window.location.search);
      var urlSession = urlParams.get('session');
      var autoId = urlSession ? 'task-' + urlSession : null;
      if (autoId && selectEl.querySelector('option[value="' + autoId + '"]')) {
        selectEl.value = autoId;
        SV.showSession(autoId);
      } else if (urlSession && selectEl.querySelector('option[value="' + urlSession + '"]')) {
        selectEl.value = urlSession;
        SV.showSession(urlSession);
      } else {
        var saved = localStorage.getItem('sv-selected-session');
        if (saved && selectEl.querySelector('option[value="' + saved + '"]')) {
          selectEl.value = saved;
          SV.showSession(saved);
        } else {
          // Default: show all sessions overview
          SV.showSession('');
        }
      }
    })
    .catch(function(err) {
      console.error('Session data load error:', err);
      emptyEl.querySelector('p').textContent = t.error;
    });

  selectEl.addEventListener('change', function() { SV.showSession(this.value); });

  // ── Refine view filtering ──
  var refineEl = document.getElementById('sv-refine-select');

  // Section visibility map per refine view
  var refineViews = {
    all: null, // null = show all (default behavior)
    tasks: ['sv-section-summary', 'sv-section-tasks', 'sv-section-progression'],
    metrics: ['sv-section-summary', 'sv-section-metrics', 'sv-section-pies', 'sv-section-deliveries', 'sv-section-velocity'],
    timeline: ['sv-section-summary', 'sv-section-time', 'sv-section-progression']
  };

  var allSectionIds = [
    'sv-section-summary', 'sv-section-metrics', 'sv-section-pies',
    'sv-section-time', 'sv-section-deliveries', 'sv-section-related-tasks',
    'sv-section-lessons', 'sv-section-collateral', 'sv-section-tasks',
    'sv-section-progression', 'sv-section-velocity'
  ];

  SV.applyRefineView = function(view) {
    var visible = refineViews[view];
    if (!visible) {
      // "all" mode — restore default visibility (show all, let renderers handle display)
      allSectionIds.forEach(function(sid) {
        var el = document.getElementById(sid);
        if (el) el.removeAttribute('data-refine-hidden');
      });
    } else {
      // Show only specified sections
      allSectionIds.forEach(function(sid) {
        var el = document.getElementById(sid);
        if (!el) return;
        if (visible.indexOf(sid) !== -1) {
          el.removeAttribute('data-refine-hidden');
        } else {
          el.setAttribute('data-refine-hidden', 'true');
        }
      });
    }
  };

  if (refineEl) {
    refineEl.addEventListener('change', function() {
      SV.applyRefineView(this.value);
    });
  }

  // ── Effective data helper (aggregated sessions) ──
  SV.effectiveData = function(s) {
    var agg = s.aggregated || null;
    return {
      agg: agg,
      additions: agg ? agg.total_additions : (s.total_additions || 0),
      deletions: agg ? agg.total_deletions : (s.total_deletions || 0),
      files: agg ? agg.total_files_changed : (s.total_files_changed || 0),
      commits: agg ? agg.total_commits : (s.total_commits || 0),
      prCount: agg ? agg.pr_count : (s.pr_count || 0),
      active: agg ? agg.active_minutes : (s.active_minutes || 0),
      firstTime: agg ? agg.first_activity_time : s.first_pr_time,
      lastTime: agg ? agg.last_activity_time : s.last_pr_time,
      prs: agg ? agg.prs : (s.prs || []),
      collateralTasks: agg ? (agg.collateral_tasks || []) : (s.collateral_tasks || []),
      systemSessions: agg ? (agg.system_sessions || []) : (s.branch ? [s.branch] : [])
    };
  };

  // ── v2.0: user session identity ──
  SV.userSessionId = function(s) {
    return s.user_session_id || null;
  };
  SV.isUserSessionRoot = function(s) {
    return s.session_kind === 'original' && (s.children_tasks || []).length > 0;
  };
  SV.systemSessionCount = function(s) {
    var d = SV.effectiveData(s);
    return d.systemSessions.length;
  };
})();
