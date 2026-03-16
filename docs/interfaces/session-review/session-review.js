// Session Review defaults to landscape — per-page key only
(function() {
  var KEY = 'knowledge-orient:' + location.pathname.replace(/\/+$/, '');
  if (!localStorage.getItem(KEY)) localStorage.setItem(KEY, 'landscape');
})();

(function() {
  var lang = (document.documentElement.lang === 'fr' || window.location.pathname.indexOf('/fr/') !== -1) ? 'fr' : 'en';
  var baseurl = document.getElementById('session-viewer').getAttribute('data-baseurl') || '';
  var dataUrl = baseurl + '/data/sessions.json';
  var sessionsData = null;
  var chartTime = null;
  var chartScope = null;
  var chartMetrics = null;
  var chartLines = null;
  var chartImpact = null;
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
      timeNote: 'Time data compiled from commit timestamps and issue creation times.',
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
      prOnly: 'This session was reconstructed from Pull Request data. No session notes or GitHub issue were created at the time.',
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
      scopeRelated: 'Related Tasks'
    },
    fr: {
      selectSession: '\u2014 Choisir une session \u2014',
      sessionsAvailable: 'sessions disponibles',
      selectPrompt: 'S\u00e9lectionnez une session ci-dessus pour afficher son rapport complet.',
      prCount: 'Pull Requests',
      taskCount: 'Tasks',
      lessonCount: 'Le\u00e7ons',
      noPRs: 'Aucun pull request enregistr\u00e9.',
      noLessons: 'Aucune le\u00e7on enregistr\u00e9e pour cette session.',
      timeNote: 'Donn\u00e9es de temps compil\u00e9es \u00e0 partir des timestamps de commits et de cr\u00e9ation des issues.',
      view: 'Voir',
      totals: 'Totaux',
      error: 'Erreur de chargement des donn\u00e9es de sessions.',
      noTitle: '(sans titre)',
      category: 'Cat\u00e9gorie',
      allSections: 'Toutes les sections',
      source: 'Fichier source',
      srcPR: 'PRs',
      srcNotes: 'Notes',
      srcTask: 'Task',
      noCompilation: 'Cette session pr\u00e9c\u00e8de la fonctionnalit\u00e9 de compilation (v50). Seules les donn\u00e9es de livraison PR sont disponibles \u2014 pas de m\u00e9triques ni de blocs temporels d\u00e9taill\u00e9s.',
      prOnly: 'Cette session a \u00e9t\u00e9 reconstruite \u00e0 partir des donn\u00e9es de Pull Requests. Aucune note de session ni issue GitHub n\u2019a \u00e9t\u00e9 cr\u00e9\u00e9e \u00e0 l\u2019\u00e9poque.',
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
      velocityTitle: 'Vélocité & Impact du code',
      codeImpact: 'Impact du code par PR',
      additionsLabel: 'Ajouts',
      deletionsLabel: 'Suppressions',
      avgPerPR: 'moy/PR',
      subFeat: 'Fonctionnalité',
      subFix: 'Correctif',
      subDoc: 'Documentation',
      subTest: 'Test / QA',
      subRefactor: 'Refactorisation',
      subChore: 'Maintenance',
      reqType: 'Type de demande',
      engStage: 'Phase ing.',
      rtFix: 'Correctif', rtFeature: 'Fonctionnalité', rtInvestigation: 'Investigation',
      rtEnhancement: 'Amélioration', rtTesting: 'Test', rtValidation: 'Validation',
      rtDocumentation: 'Documentation', rtDeployment: 'Déploiement', rtConception: 'Conception',
      rtReview: 'Révision', rtChore: 'Maintenance',
      stAnalysis: 'Analyse', stPlanning: 'Planification', stDesign: 'Conception',
      stImplementation: 'Implémentation', stTesting: 'Test', stValidation: 'Validation',
      stReview: 'Révision', stDeployment: 'Déploiement', stOperations: 'Opérations',
      stImprovement: 'Amélioration',
      taskCol: 'Task',
      typeCol: 'Type',
      titleCol: 'Titre',
      taskTypeSession: 'Session',
      taskTypeRelated: 'Liée',
      sessionCol: 'Session',
      openSession: 'Ouvrir',
      openTab: 'Nouvel onglet',
      scopeTitle: 'Portée de la session',
      scopeChildren: 'Sessions enfants',
      scopeRelated: 'Tâches liées'
    }
  };
  var t = L[lang] || L.en;

  // === Engineering Taxonomy — request types + stages ===
  var reqTypeMap = {
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
  var engStageMap = {
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
  function reqTypeBadge(rt) {
    if (!rt) return '';
    var info = reqTypeMap[rt] || { emoji: '\u2022', label: rt };
    return info.emoji + ' ' + info.label;
  }
  function engStageBadge(st) {
    if (!st) return '';
    var info = engStageMap[st] || { emoji: '\u2022', label: st };
    return info.emoji + ' ' + info.label;
  }

  var selectEl = document.getElementById('sv-session-select');
  var emptyEl = document.getElementById('sv-empty-state');
  var contentEl = document.getElementById('sv-content');
  var countEl = document.getElementById('sv-session-count');

  fetch(dataUrl)
    .then(function(r) { return r.json(); })
    .then(function(data) {
      sessionsData = data;
      populateDropdown(data.sessions);
      countEl.textContent = data.sessions.length;
      // URL parameter ?session=N → auto-select session
      var urlParams = new URLSearchParams(window.location.search);
      var urlSession = urlParams.get('session');
      var autoId = urlSession ? 'task-' + urlSession : null;
      if (autoId && selectEl.querySelector('option[value="' + autoId + '"]')) {
        selectEl.value = autoId;
        showSession(autoId);
      } else {
        var saved = localStorage.getItem('sv-selected-session');
        if (saved && selectEl.querySelector('option[value="' + saved + '"]')) {
          selectEl.value = saved;
          showSession(saved);
        } else {
          // Default: show all sessions overview
          showSession('');
        }
      }
    })
    .catch(function(err) {
      console.error('Session data load error:', err);
      emptyEl.querySelector('p').textContent = t.error;
    });

  function localDate(isoStr) {
    if (!isoStr) return null;
    var d = new Date(isoStr);
    return d.getFullYear() + '-' + ('0'+(d.getMonth()+1)).slice(-2) + '-' + ('0'+d.getDate()).slice(-2);
  }

  // Effective activity time: aggregated (parent sessions) > own timestamps
  function effectiveTime(s) {
    return (s.aggregated ? s.aggregated.last_activity_time : null)
      || s.last_activity_time || s.last_pr_time || s.first_activity_time;
  }

  function populateDropdown(sessions) {
    selectEl.innerHTML = '<option value="">' + t.selectSession + '</option>';
    var supported = sessions;
    var byDate = {};
    supported.forEach(function(s) {
      // Use local timezone date derived from effective activity timestamp
      var refTime = effectiveTime(s);
      var d = (refTime ? localDate(refTime) : s.date) || 'unknown';
      if (!byDate[d]) byDate[d] = [];
      byDate[d].push(s);
    });
    Object.keys(byDate).sort().reverse().forEach(function(date) {
      var group = document.createElement('optgroup');
      group.label = date;
      // Sort sessions within date group by effective time (earliest first)
      byDate[date].sort(function(a, b) {
        var ta = effectiveTime(a) || '';
        var tb = effectiveTime(b) || '';
        return ta < tb ? -1 : ta > tb ? 1 : 0;
      });
      byDate[date].forEach(function(s) {
        var opt = document.createElement('option');
        opt.value = s.id;
        // All emojis at end: request type + status indicators
        var suffix = '';
        var rtInfo = s.request_type ? reqTypeMap[s.request_type] : null;
        if (rtInfo) suffix += rtInfo.emoji;
        if (s.pr_count > 0) suffix += '\ud83d\udce6';
        if (s.has_notes) suffix += '\ud83d\udccb';
        if (s.has_task) suffix += '\ud83c\udfab';
        var timePrefix = effectiveTime(s) ? formatTime(effectiveTime(s)) + ' ' : '';
        var label = s.title || t.noTitle;
        if (label.length > 50) label = label.substring(0, 47) + '...';
        var taskTag = s.task_number ? '#' + s.task_number + ' ' : '';
        // Session kind emoji: 💬 original, 🔁 continuation (between #issue and title)
        var kindEmoji = s.session_kind === 'continuation' ? '\ud83d\udd01 ' : '\ud83d\udcac ';
        opt.textContent = timePrefix + taskTag + kindEmoji + label + (suffix ? ' ' + suffix : '');
        group.appendChild(opt);
      });
      selectEl.appendChild(group);
    });
  }

  function findSession(id) {
    if (!sessionsData) return null;
    for (var i = 0; i < sessionsData.sessions.length; i++) {
      if (sessionsData.sessions[i].id === id) return sessionsData.sessions[i];
    }
    return null;
  }

  function taskLabel(num) {
    var map = (sessionsData && sessionsData.task_labels) || {};
    var info = map[String(num)];
    return info ? info.label : null;
  }

  function taskLabelBadge(num, fallback) {
    var lbl = taskLabel(num);
    if (!lbl) return '<span class="sv-task-type sv-task-type-related">' + esc(fallback) + '</span>';
    var cls = 'sv-task-type sv-task-label-' + lbl.toLowerCase().replace(/[^a-z]/g, '');
    return '<span class="sv-task-type ' + cls + '">' + esc(lbl) + '</span>';
  }

  function esc(str) {
    var d = document.createElement('div');
    d.appendChild(document.createTextNode(str));
    return d.innerHTML;
  }

  function formatTime(isoStr) {
    if (!isoStr) return '\u2014';
    var d = new Date(isoStr);
    return ('0'+d.getHours()).slice(-2) + ':' + ('0'+d.getMinutes()).slice(-2);
  }

  function calcDuration(startIso, endIso) {
    if (!startIso || !endIso) return null;
    var ms = new Date(endIso) - new Date(startIso);
    return Math.round(ms / 60000);
  }

  function formatDuration(minutes) {
    if (minutes == null || minutes < 0) return '\u2014';
    if (minutes === 0) return '<1min';
    if (minutes < 60) return '~' + minutes + 'min';
    var h = Math.floor(minutes / 60);
    var m = minutes % 60;
    return '~' + h + 'h' + (m > 0 ? ('0'+m).slice(-2) : '');
  }

  function timeBlock(isoStr) {
    if (!isoStr) return '\u2014';
    var h = new Date(isoStr).getHours();
    if (h >= 5 && h < 12) return t.morning;
    if (h >= 12 && h < 18) return t.afternoon;
    return t.evening;
  }

  var currentSession = null;

  // === Chart.js pie chart rendering ===
  var chartColors = {
    active:   { bg: 'rgba(29,78,216,0.75)',  border: '#1d4ed8' },
    inactive: { bg: 'rgba(147,197,253,0.5)', border: '#93c5fd' },
    calendar: { bg: 'rgba(59,130,246,0.6)',  border: '#3b82f6' },
    cats: [
      { bg: 'rgba(29,78,216,0.75)',   border: '#1d4ed8' },
      { bg: 'rgba(59,130,246,0.7)',   border: '#3b82f6' },
      { bg: 'rgba(147,197,253,0.7)',  border: '#93c5fd' },
      { bg: 'rgba(96,165,250,0.7)',   border: '#60a5fa' },
      { bg: 'rgba(37,99,235,0.7)',    border: '#2563eb' },
      { bg: 'rgba(191,219,254,0.7)',  border: '#bfdbfe' }
    ]
  };

  function destroyCharts() {
    if (chartTime) { chartTime.destroy(); chartTime = null; }
    if (chartScope) { chartScope.destroy(); chartScope = null; }
    if (chartMetrics) { chartMetrics.destroy(); chartMetrics = null; }
    if (chartLines) { chartLines.destroy(); chartLines = null; }
    if (chartImpact) { chartImpact.destroy(); chartImpact = null; }
    document.getElementById('sv-chart-time-wrap').style.display = 'none';
    document.getElementById('sv-chart-scope-wrap').style.display = 'none';
    document.getElementById('sv-chart-metrics-wrap').style.display = 'none';
    document.getElementById('sv-chart-lines-wrap').style.display = 'none';
    document.getElementById('sv-chart-impact-wrap').style.display = 'none';
    document.getElementById('sv-section-pies').style.display = 'none';
  }

  function isDarkTheme() {
    var dt = document.documentElement.getAttribute('data-theme') || '';
    return (dt === 'midnight' || dt === 'daltonism-dark') || (!dt || dt === 'auto') && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }

  function renderCharts(s, hasComments, hasPrs) {
    destroyCharts();
    if (typeof Chart === 'undefined') return;

    // --- Time pie chart: Active vs Inactive (gap-based inactive) ---
    var activeMin = 0, inactiveMin = 0, calMin = 0;
    if (hasComments && s.comments && s.comments.length > 0) {
      // Pre-compute end times (same logic as table)
      var chEndTimes = [];
      s.comments.forEach(function(c, i) {
        var endIso = null;
        if (c.updated_at && c.updated_at !== c.created_at) {
          endIso = c.updated_at;
        } else if (i + 1 < s.comments.length) {
          endIso = s.comments[i + 1].created_at;
        } else if (s.last_pr_time) {
          endIso = s.last_pr_time;
        }
        chEndTimes.push(endIso);
      });
      s.comments.forEach(function(c, i) {
        var endIso = chEndTimes[i];
        var cCal = endIso ? calcDuration(c.created_at, endIso) : 0;
        if (cCal == null || cCal < 0) cCal = 0;
        calMin += cCal;
        // Active = sum of child PR durations if any
        var prsByC = [];
        if (hasPrs && s.prs) {
          s.prs.forEach(function(pr) {
            for (var ci = s.comments.length - 1; ci >= 0; ci--) {
              if (s.comments[ci].type === 'bot' && s.comments[ci].created_at <= pr.created_at) {
                if (ci === i) prsByC.push(pr);
                break;
              }
            }
          });
        }
        var cActive = 0;
        if (prsByC.length > 0) {
          prsByC.forEach(function(pr) {
            var d = calcDuration(pr.created_at, pr.merged_at);
            if (d != null && d > 0) cActive += d;
          });
          if (cActive === 0) cActive = cCal;
        } else {
          cActive = cCal;
        }
        activeMin += cActive;
        // Gap-based inactive: gap between previous item's end and current start
        if (i > 0 && chEndTimes[i - 1]) {
          var gap = calcDuration(chEndTimes[i - 1], c.created_at);
          if (gap != null && gap > 0) inactiveMin += gap;
        }
      });
    } else if (hasPrs && s.prs && s.prs.length > 0) {
      s.prs.forEach(function(pr, i) {
        var prDur = calcDuration(pr.created_at, pr.merged_at);
        var nextStart = (i + 1 < s.prs.length) ? s.prs[i + 1].created_at : pr.merged_at;
        var prCal = calcDuration(pr.created_at, nextStart);
        if (prDur != null && prDur > 0) activeMin += prDur;
        if (prCal != null && prCal > 0) calMin += prCal;
        // Gap-based inactive for PR mode
        if (i > 0 && s.prs[i - 1].merged_at) {
          var gap = calcDuration(s.prs[i - 1].merged_at, pr.created_at);
          if (gap != null && gap > 0) inactiveMin += gap;
        }
      });
    }

    if (calMin > 0) {
      var timeWrap = document.getElementById('sv-chart-time-wrap');
      timeWrap.style.display = '';
      document.getElementById('sv-section-pies').style.display = '';
      var timeCtx = document.getElementById('sv-chart-time').getContext('2d');
      var isDark = isDarkTheme();
      var titleColor = isDark ? '#ffffff' : '#0f172a';
      var legendColor = isDark ? '#93c5fd' : '#475569';
      chartTime = new Chart(timeCtx, {
        type: 'doughnut',
        data: {
          labels: [
            (lang === 'fr' ? 'Actif' : 'Active') + ' (' + formatDuration(activeMin) + ')',
            (lang === 'fr' ? 'Inactif' : 'Inactive') + ' (' + formatDuration(inactiveMin) + ')'
          ],
          datasets: [{
            data: [activeMin, inactiveMin],
            backgroundColor: [chartColors.active.bg, chartColors.inactive.bg],
            borderColor: [chartColors.active.border, chartColors.inactive.border],
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: true,
          plugins: {
            legend: {
              position: 'bottom',
              labels: { color: legendColor, font: { size: 12 }, padding: 12 }
            },
            title: {
              display: true,
              text: lang === 'fr' ? 'Proportions temporelles' : 'Time Proportions',
              color: titleColor,
              font: { size: 14, weight: 'bold' }
            }
          }
        }
      });
    }

    // --- Session Scope pie chart: Issue type breakdown across all related/child tasks ---
    // Classify all related_tasks by their secondary label (bug, enhancement, feature, etc.)
    var scopeByType = {};
    var scopeColors = {
      'bug': { bg: 'rgba(239,68,68,0.7)', border: '#ef4444' },
      'enhancement': { bg: 'rgba(59,130,246,0.7)', border: '#3b82f6' },
      'FEATURE': { bg: 'rgba(34,197,94,0.7)', border: '#22c55e' },
      'REVIEW': { bg: 'rgba(168,85,247,0.7)', border: '#a855f7' },
      'DESIGN': { bg: 'rgba(245,158,11,0.7)', border: '#f59e0b' },
      'documentation': { bg: 'rgba(147,197,253,0.7)', border: '#93c5fd' },
      '_default': { bg: 'rgba(100,116,139,0.7)', border: '#64748b' }
    };
    var scopeTypeLabels = {
      'bug': lang === 'fr' ? 'Correctifs' : 'Bug fixes',
      'enhancement': lang === 'fr' ? 'Am\u00e9liorations' : 'Enhancements',
      'FEATURE': lang === 'fr' ? 'Fonctionnalit\u00e9s' : 'Features',
      'REVIEW': lang === 'fr' ? 'Revues' : 'Reviews',
      'DESIGN': 'Design',
      'documentation': 'Documentation'
    };
    (s.related_tasks || []).forEach(function(ri) {
      if (ri.number === s.task_number) return;
      var labels = ri.labels || [];
      // Find the type label (skip SESSION which is just a marker)
      var typeLabel = null;
      for (var li = 0; li < labels.length; li++) {
        if (labels[li] !== 'SESSION') { typeLabel = labels[li]; break; }
      }
      if (!typeLabel) typeLabel = '_other';
      if (!scopeByType[typeLabel]) scopeByType[typeLabel] = { count: 0, lines: 0 };
      scopeByType[typeLabel].count++;
      // Try to get lines from session data
      var cs = findSession('task-' + ri.number);
      if (cs) scopeByType[typeLabel].lines += (cs.total_additions || 0) + (cs.total_deletions || 0);
    });
    var scopeTypeKeys = Object.keys(scopeByType);
    var scopeTotal = scopeTypeKeys.reduce(function(sum, k) { return sum + scopeByType[k].count; }, 0);
    if (scopeTotal > 0) {
      var scLabels = [], scData = [], scBg = [], scBorder = [];
      scopeTypeKeys.forEach(function(k) {
        var entry = scopeByType[k];
        var label = scopeTypeLabels[k] || k;
        var displayLabel = label + ' (' + entry.count + ')';
        if (entry.lines > 0) displayLabel += ' \u2014 ' + entry.lines + ' ' + t.linesChanged;
        scLabels.push(displayLabel);
        scData.push(entry.lines > 0 ? entry.lines : entry.count);
        var color = scopeColors[k] || scopeColors['_default'];
        scBg.push(color.bg);
        scBorder.push(color.border);
      });
      var scopeWrap = document.getElementById('sv-chart-scope-wrap');
      scopeWrap.style.display = '';
      document.getElementById('sv-section-pies').style.display = '';
      var scopeCtx = document.getElementById('sv-chart-scope').getContext('2d');
      var isDarkSc = isDarkTheme();
      var titleColorSc = isDarkSc ? '#ffffff' : '#0f172a';
      var legendColorSc = isDarkSc ? '#93c5fd' : '#475569';
      chartScope = new Chart(scopeCtx, {
        type: 'doughnut',
        data: {
          labels: scLabels,
          datasets: [{
            data: scData,
            backgroundColor: scBg,
            borderColor: scBorder,
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: true,
          plugins: {
            legend: {
              position: 'bottom',
              labels: { color: legendColorSc, font: { size: 12 }, padding: 12 }
            },
            title: {
              display: true,
              text: t.scopeTitle + ' (' + scopeTotal + ' tasks)',
              color: titleColorSc,
              font: { size: 14, weight: 'bold' }
            }
          }
        }
      });
    }

    // --- Deliverables pie chart: PRs / Commits / Files / Issues / Lessons ---
    var mPrs = s.pr_count || 0;
    var mCommits = 0;
    var mFiles = 0;
    if (s.prs && s.prs.length > 0) {
      s.prs.forEach(function(p) { mCommits += (p.commits || 0); mFiles += (p.changed_files || 0); });
    }
    var mTasks = (s.related_tasks && s.related_tasks.length) || 0;
    var mLessons = (s.lessons && s.lessons.length) || 0;
    var mTotal = mPrs + mCommits + mFiles + mTasks + mLessons;
    if (mTotal > 0) {
      var mLabels = [], mData = [], mBg = [], mBorder = [];
      if (mPrs > 0) { mLabels.push(t.prCount + ' (' + mPrs + ')'); mData.push(mPrs); mBg.push(chartColors.cats[0].bg); mBorder.push(chartColors.cats[0].border); }
      if (mCommits > 0) { mLabels.push(t.commits + ' (' + mCommits + ')'); mData.push(mCommits); mBg.push(chartColors.cats[3].bg); mBorder.push(chartColors.cats[3].border); }
      if (mFiles > 0) { mLabels.push(t.filesChanged + ' (' + mFiles + ')'); mData.push(mFiles); mBg.push(chartColors.cats[4].bg); mBorder.push(chartColors.cats[4].border); }
      if (mTasks > 0) { mLabels.push(t.taskCount + ' (' + mTasks + ')'); mData.push(mTasks); mBg.push(chartColors.cats[1].bg); mBorder.push(chartColors.cats[1].border); }
      if (mLessons > 0) { mLabels.push(t.lessonCount + ' (' + mLessons + ')'); mData.push(mLessons); mBg.push(chartColors.cats[2].bg); mBorder.push(chartColors.cats[2].border); }
      var metricsWrap = document.getElementById('sv-chart-metrics-wrap');
      metricsWrap.style.display = '';
      document.getElementById('sv-section-pies').style.display = '';
      var metricsCtx = document.getElementById('sv-chart-metrics').getContext('2d');
      var isDark2 = isDarkTheme();
      var titleColor2 = isDark2 ? '#ffffff' : '#0f172a';
      var legendColor2 = isDark2 ? '#93c5fd' : '#475569';
      chartMetrics = new Chart(metricsCtx, {
        type: 'doughnut',
        data: {
          labels: mLabels,
          datasets: [{
            data: mData,
            backgroundColor: mBg,
            borderColor: mBorder,
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: true,
          plugins: {
            legend: {
              position: 'bottom',
              labels: { color: legendColor2, font: { size: 12 }, padding: 12 }
            },
            title: {
              display: true,
              text: lang === 'fr' ? 'Livrables' : 'Deliverables',
              color: titleColor2,
              font: { size: 14, weight: 'bold' }
            }
          }
        }
      });
    }

    // --- Lines Changed pie chart: Additions vs Deletions ---
    if (hasPrs && s.prs && s.prs.length > 0) {
      var totalAdd = 0, totalDel = 0;
      s.prs.forEach(function(p) {
        totalAdd += (p.additions || 0);
        totalDel += (p.deletions || 0);
      });
      if (totalAdd + totalDel > 0) {
        var linesWrap = document.getElementById('sv-chart-lines-wrap');
        linesWrap.style.display = '';
        document.getElementById('sv-section-pies').style.display = '';
        var linesCtx = document.getElementById('sv-chart-lines').getContext('2d');
        var isDarkL = isDarkTheme();
        var titleColorL = isDarkL ? '#ffffff' : '#0f172a';
        var legendColorL = isDarkL ? '#93c5fd' : '#475569';
        chartLines = new Chart(linesCtx, {
          type: 'doughnut',
          data: {
            labels: [
              t.additionsLabel + ' (+' + totalAdd + ')',
              t.deletionsLabel + ' (-' + totalDel + ')'
            ],
            datasets: [{
              data: [totalAdd, totalDel],
              backgroundColor: ['rgba(22,163,74,0.7)', 'rgba(220,38,38,0.7)'],
              borderColor: ['#16a34a', '#dc2626'],
              borderWidth: 2
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
              legend: {
                position: 'bottom',
                labels: { color: legendColorL, font: { size: 12 }, padding: 12 }
              },
              title: {
                display: true,
                text: t.linesChanged + ' (' + (totalAdd + totalDel) + ')',
                color: titleColorL,
                font: { size: 14, weight: 'bold' }
              }
            }
          }
        });
      }
    }

    // --- Code Impact bar chart: additions/deletions per PR ---
    if (hasPrs && s.prs && s.prs.length > 0) {
      var hasVelocity = s.prs.some(function(p) { return (p.additions || 0) + (p.deletions || 0) > 0; });
      if (hasVelocity) {
        var impactWrap = document.getElementById('sv-chart-impact-wrap');
        impactWrap.style.display = '';
        var impactCtx = document.getElementById('sv-chart-impact').getContext('2d');
        var isDark3 = isDarkTheme();
        var titleColor3 = isDark3 ? '#ffffff' : '#0f172a';
        var legendColor3 = isDark3 ? '#93c5fd' : '#475569';
        var gridColor3 = isDark3 ? 'rgba(148,163,184,0.2)' : 'rgba(0,0,0,0.08)';
        var tickColor3 = isDark3 ? '#94a3b8' : '#64748b';
        var prLabels = s.prs.map(function(p) { return '#' + p.number; });
        var addData = s.prs.map(function(p) { return p.additions || 0; });
        var delData = s.prs.map(function(p) { return -(p.deletions || 0); });
        chartImpact = new Chart(impactCtx, {
          type: 'bar',
          data: {
            labels: prLabels,
            datasets: [
              {
                label: t.additionsLabel,
                data: addData,
                backgroundColor: 'rgba(22,163,74,0.7)',
                borderColor: '#16a34a',
                borderWidth: 1
              },
              {
                label: t.deletionsLabel,
                data: delData,
                backgroundColor: 'rgba(220,38,38,0.7)',
                borderColor: '#dc2626',
                borderWidth: 1
              }
            ]
          },
          options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                position: 'top',
                labels: { color: legendColor3, font: { size: 11 }, padding: 10 }
              },
              title: {
                display: true,
                text: t.codeImpact,
                color: titleColor3,
                font: { size: 13, weight: 'bold' }
              },
              tooltip: {
                callbacks: {
                  label: function(ctx) {
                    var v = Math.abs(ctx.raw);
                    return ctx.dataset.label + ': ' + v;
                  }
                }
              }
            },
            scales: {
              x: {
                grid: { color: gridColor3 },
                ticks: {
                  color: tickColor3,
                  callback: function(v) { return Math.abs(v); }
                }
              },
              y: {
                grid: { display: false },
                ticks: { color: tickColor3, font: { size: 10 } }
              }
            }
          }
        });
        // Dynamic height based on PR count
        var impactCanvas = document.getElementById('sv-chart-impact');
        var minH = Math.max(200, s.prs.length * 28 + 80);
        impactCanvas.parentElement.style.minHeight = minH + 'px';
      }
    }
  }

  // ── Overview rendering (All Sessions) ──
  var overviewEl = document.getElementById('sv-view-overview');

  function renderSessionOverview() {
    if (!overviewEl || !sessionsData) return;
    var sessions = sessionsData.sessions || [];

    // Aggregate stats
    var totalSessions = sessions.length;
    var totalPRs = 0;
    var totalAdds = 0;
    var totalDels = 0;
    var totalFiles = 0;
    sessions.forEach(function(s) {
      totalPRs += s.total_prs || s.pr_count || 0;
      totalAdds += s.total_additions || 0;
      totalDels += s.total_deletions || 0;
      totalFiles += s.total_files_changed || 0;
    });

    var statsEl = document.getElementById('sv-overview-stats');
    if (statsEl) {
      statsEl.innerHTML =
        '<div class="sv-stat-card"><div class="sv-stat-value">' + totalSessions + '</div><div class="sv-stat-label">' + (lang === 'fr' ? 'Sessions' : 'Sessions') + '</div></div>' +
        '<div class="sv-stat-card"><div class="sv-stat-value">' + totalPRs + '</div><div class="sv-stat-label">' + t.prCount + '</div></div>' +
        '<div class="sv-stat-card"><div class="sv-stat-value">+' + totalAdds.toLocaleString() + '</div><div class="sv-stat-label">' + t.additions + '</div></div>' +
        '<div class="sv-stat-card"><div class="sv-stat-value">-' + totalDels.toLocaleString() + '</div><div class="sv-stat-label">' + t.deletions + '</div></div>' +
        '<div class="sv-stat-card"><div class="sv-stat-value">' + totalFiles + '</div><div class="sv-stat-label">' + t.filesChanged + '</div></div>';
    }

    // Session cards
    var cardsEl = document.getElementById('sv-session-cards');
    if (!cardsEl) return;

    var sorted = sessions.slice().sort(function(a, b) {
      var ta = effectiveTime(a) || '';
      var tb = effectiveTime(b) || '';
      return tb.localeCompare(ta);
    });

    var html = '';
    sorted.forEach(function(s) {
      var title = esc(s.title || t.noTitle);
      if (title.length > 60) title = title.substring(0, 57) + '...';
      var date = s.date || '';
      var taskTag = s.task_number ? '#' + s.task_number + ' ' : '';
      var rtInfo = s.request_type ? reqTypeMap[s.request_type] : null;
      var rtEmoji = rtInfo ? rtInfo.emoji + ' ' : '';

      html += '<div class="sv-card" data-session-id="' + esc(s.id) + '">';
      html += '<div class="sv-card-title">' + rtEmoji + taskTag + title + '</div>';
      html += '<div class="sv-card-meta">';
      html += '<span class="sv-badge sv-badge-type">' + esc(s.type || '') + '</span>';
      html += '<span>' + date + '</span>';
      html += '<span>+' + (s.total_additions || 0) + '/-' + (s.total_deletions || 0) + '</span>';
      html += '<span>' + (s.total_prs || s.pr_count || 0) + ' PRs</span>';
      html += '</div>';
      html += '</div>';
    });
    cardsEl.innerHTML = html;

    // Click handlers
    cardsEl.querySelectorAll('.sv-card').forEach(function(card) {
      card.addEventListener('click', function() {
        var id = card.getAttribute('data-session-id');
        selectEl.value = id;
        showSession(id);
      });
    });
  }

  function showSession(id) {
    // "All Sessions" overview mode
    if (!id) {
      currentSession = null;
      destroyCharts();
      emptyEl.style.display = 'none';
      contentEl.style.display = 'none';
      if (overviewEl) {
        overviewEl.style.display = '';
        renderSessionOverview();
      }
      try { localStorage.removeItem('sv-selected-session'); } catch(e) {}
      return;
    }
    // Hide overview when viewing a single session
    if (overviewEl) overviewEl.style.display = 'none';

    var s = findSession(id);
    if (!s) { currentSession = null; destroyCharts(); emptyEl.style.display = ''; contentEl.style.display = 'none'; return; }
    currentSession = s;
    emptyEl.style.display = 'none';
    contentEl.style.display = '';
    localStorage.setItem('sv-selected-session', id);

    // Data source notice
    var noticeEl = document.getElementById('sv-notice');
    var hasPRs = s.pr_count > 0;
    var hasNotes = s.has_notes;
    var hasTask = s.has_task;
    if (!hasNotes && !hasTask) {
      noticeEl.className = 'sv-notice sv-notice-warn';
      noticeEl.innerHTML = '<strong>\u26a0\ufe0f</strong> ' + t.prOnly;
      noticeEl.style.display = '';
    } else if (!hasNotes && hasTask) {
      noticeEl.className = 'sv-notice sv-notice-info';
      noticeEl.innerHTML = '<strong>\u2139\ufe0f</strong> ' + t.noCompilation;
      noticeEl.style.display = '';
    } else {
      noticeEl.style.display = 'none';
    }

    // 1. Summary
    document.getElementById('sv-title').textContent = s.title || t.noTitle;
    document.getElementById('sv-type').textContent = s.type || '';
    document.getElementById('sv-date').textContent = s.date || '';
    // Request type badge (engineering taxonomy)
    var rtEl = document.getElementById('sv-request-type');
    if (s.request_type) {
      rtEl.textContent = reqTypeBadge(s.request_type);
      rtEl.title = t.reqType + ': ' + s.request_type;
      rtEl.style.display = '';
    } else { rtEl.style.display = 'none'; }
    // Engineering stage badge
    var stEl = document.getElementById('sv-eng-stage');
    if (s.engineering_stage) {
      stEl.textContent = engStageBadge(s.engineering_stage);
      stEl.title = t.engStage + ': ' + s.engineering_stage;
      stEl.style.display = '';
    } else { stEl.style.display = 'none'; }
    var brEl = document.getElementById('sv-branch');
    if (s.branch) { brEl.textContent = s.branch; brEl.style.display = ''; }
    else { brEl.style.display = 'none'; }

    // Source badges
    var badgesEl = document.getElementById('sv-source-badges');
    var badges = '';
    if (hasPRs) badges += '<span class="sv-src-badge sv-src-pr">' + t.srcPR + '</span>';
    if (hasNotes) badges += '<span class="sv-src-badge sv-src-notes">' + t.srcNotes + '</span>';
    if (hasTask) badges += '<span class="sv-src-badge sv-src-task">' + t.srcTask + '</span>';
    badgesEl.innerHTML = badges;

    var sumEl = document.getElementById('sv-summary');
    sumEl.textContent = s.summary || '';
    sumEl.style.display = s.summary ? '' : 'none';

    // Use aggregated data when available (parent sessions with children)
    var agg = s.aggregated || null;
    var effAdditions = agg ? agg.total_additions : (s.total_additions || 0);
    var effDeletions = agg ? agg.total_deletions : (s.total_deletions || 0);
    var effFiles = agg ? agg.total_files_changed : (s.total_files_changed || 0);
    var effCommits = agg ? agg.total_commits : (s.total_commits || 0);
    var effPrCount = agg ? agg.pr_count : (s.pr_count || 0);
    var effActive = agg ? agg.active_minutes : (s.active_minutes || 0);
    var effFirstTime = agg ? agg.first_activity_time : s.first_pr_time;
    var effLastTime = agg ? agg.last_activity_time : s.last_pr_time;
    var effPrs = agg ? agg.prs : (s.prs || []);

    var grid = document.getElementById('sv-stats-grid');
    grid.innerHTML = '';
    var calendarMin = calcDuration(effFirstTime, effLastTime);
    var calendarStr = calendarMin != null ? formatDuration(calendarMin) : '\u2014';
    var activeStr = effActive > 0 ? formatDuration(effActive) : '\u2014';
    var totalLines = effAdditions + effDeletions;
    var linesStr = totalLines > 0 ? ('+' + effAdditions + ' \u2212' + effDeletions) : '\u2014';
    var filesStr = effFiles > 0 ? String(effFiles) : '\u2014';
    var commitsStr = effCommits > 0 ? String(effCommits) : '\u2014';
    var velocityStr = s.lines_per_hour ? (s.lines_per_hour + ' ' + t.linesPerHour) : '\u2014';
    [
      { v: effPrCount || 0, l: t.prCount },
      { v: commitsStr, l: t.commits },
      { v: linesStr, l: t.linesChanged },
      { v: filesStr, l: t.filesChanged },
      { v: activeStr, l: t.activeTime },
      { v: calendarStr, l: t.calendarTime },
      { v: (s.related_tasks || []).length, l: t.taskCount },
      { v: (s.lessons || []).length, l: t.lessonCount }
    ].forEach(function(c) {
      var d = document.createElement('div'); d.className = 'sv-stat-card';
      d.innerHTML = '<div class="sv-stat-value">' + c.v + '</div><div class="sv-stat-label">' + c.l + '</div>';
      grid.appendChild(d);
    });

    // 2. Metrics — parent/child collapsible rows grouped by sub_type
    var mTotals = document.getElementById('sv-metrics-totals');
    var mBody = document.getElementById('sv-metrics-body');
    var pc = effPrCount, ic = (s.related_tasks||[]).length, lc = (s.lessons||[]).length;
    var tl = totalLines, tf = effFiles, tc = effCommits;
    mTotals.innerHTML = '<strong>' + t.totals + ':</strong> ' + pc + ' PRs \u00b7 ' + tc + ' commits \u00b7 +' +
      effAdditions + ' \u2212' + effDeletions + ' lines \u00b7 ' + tf + ' files' +
      (s.lines_per_hour ? ' \u00b7 <em>' + s.lines_per_hour + ' ' + t.linesPerHour + '</em>' : '') +
      (agg ? ' \u00b7 <em>' + (agg.children_count || 0) + ' child tasks</em>' : '');
    mBody.innerHTML = '';
    // Sub-type labels and icons
    var subLabels = {
      feat: { icon: '\ud83d\ude80', en: 'Feature', fr: 'Fonctionnalité' },
      fix: { icon: '\ud83d\udd27', en: 'Fix', fr: 'Correctif' },
      doc: { icon: '\ud83d\udcdd', en: 'Documentation', fr: 'Documentation' },
      test: { icon: '\ud83e\uddea', en: 'Test / QA', fr: 'Test / QA' },
      refactor: { icon: '\u267b\ufe0f', en: 'Refactor', fr: 'Refactorisation' },
      chore: { icon: '\u2699\ufe0f', en: 'Chore', fr: 'Maintenance' }
    };
    // Group PRs by sub_type (use aggregated PRs if available)
    var groups = {};
    var groupOrder = ['feat', 'fix', 'test', 'doc', 'refactor', 'chore'];
    effPrs.forEach(function(p) {
      var st = p.sub_type || 'feat';
      if (!groups[st]) groups[st] = [];
      groups[st].push(p);
    });
    // Render parent/child rows per sub_type group
    var groupIdx = 0;
    groupOrder.forEach(function(st) {
      if (!groups[st]) return;
      var prGroup = groups[st];
      groupIdx++;
      var gid = 'mg-' + groupIdx;
      // Aggregate metrics for this group
      var gAdd = 0, gDel = 0, gFiles = 0, gCommits = 0;
      prGroup.forEach(function(p) {
        gAdd += p.additions || 0;
        gDel += p.deletions || 0;
        gFiles += p.changed_files || 0;
        gCommits += p.commits || 0;
      });
      var info = subLabels[st] || { icon: '\u2022', en: st, fr: st };
      var gLabel = info.icon + ' ' + (lang === 'fr' ? info.fr : info.en);
      var gAddDel = (gAdd || gDel) ?
        '<span style="color:#16a34a">+' + gAdd + '</span> <span style="color:#dc2626">\u2212' + gDel + '</span>' : '\u2014';
      // Parent row
      var ptr = document.createElement('tr');
      ptr.className = 'sv-row-parent';
      ptr.setAttribute('data-group', gid);
      ptr.innerHTML = '<td><strong>M' + groupIdx + '</strong></td><td>' + gLabel + '</td><td>' + prGroup.length + '</td><td>' + gAddDel + '</td><td>' + gFiles + '</td><td>' + gCommits + '</td><td></td><td></td>';
      ptr.addEventListener('click', function() {
        var expanded = this.classList.toggle('sv-expanded');
        var children = mBody.querySelectorAll('.sv-child-' + gid);
        for (var i = 0; i < children.length; i++) {
          children[i].classList.toggle('sv-visible', expanded);
        }
      });
      mBody.appendChild(ptr);
      // Child rows (individual PRs)
      prGroup.forEach(function(p) {
        var ctr = document.createElement('tr');
        ctr.className = 'sv-row-child sv-child-' + gid;
        var pAddDel = (p.additions || p.deletions) ?
          '<span style="color:#16a34a">+' + (p.additions || 0) + '</span> <span style="color:#dc2626">\u2212' + (p.deletions || 0) + '</span>' : '\u2014';
        ctr.innerHTML = '<td></td><td>#' + p.number + ' ' + esc(p.title || '').substring(0, 50) + (p.title && p.title.length > 50 ? '\u2026' : '') +
          '</td><td></td><td>' + pAddDel + '</td><td>' + (p.changed_files || 0) + '</td><td>' + (p.commits || 0) + '</td><td></td><td></td>';
        mBody.appendChild(ctr);
      });
    });
    // Totals footer row
    var addDelTotal = (s.total_additions || s.total_deletions) ?
      '<span style="color:#16a34a">+' + (s.total_additions || 0) + '</span> <span style="color:#dc2626">\u2212' + (s.total_deletions || 0) + '</span>' : '\u2014';
    var tfoot = document.createElement('tr');
    tfoot.style.fontWeight = '700';
    tfoot.style.borderTop = '2px solid var(--border, #93c5fd)';
    var footLabel = s.request_type ? reqTypeBadge(s.request_type) : esc(s.type || '\u2014');
    tfoot.innerHTML = '<td colspan="2" style="text-align:right">' + t.totals + '</td><td>' + pc + '</td><td>' + addDelTotal + '</td><td>' + tf + '</td><td>' + tc + '</td><td>' + ic + '</td><td>' + lc + '</td>';
    mBody.appendChild(tfoot);

    // 2b. Velocity & Code Impact
    var velSection = document.getElementById('sv-section-velocity');
    var hasVelocityData = s.lines_per_hour || s.commits_per_hour || s.files_per_hour ||
                          (s.total_additions || 0) + (s.total_deletions || 0) > 0;
    if (hasVelocityData) {
      velSection.style.display = '';
      var gauges = document.getElementById('sv-velocity-gauges');
      gauges.innerHTML = '';
      var avgLines = pc > 0 ? Math.round(tl / pc) : 0;
      var avgFiles = pc > 0 ? Math.round(tf / pc) : 0;
      var avgCommits = pc > 0 ? (tc / pc).toFixed(1) : 0;
      var velData = [
        { label: t.linesPerHour, value: s.lines_per_hour || 0, max: 2000 },
        { label: t.commitsPerHour, value: s.commits_per_hour || 0, max: 40 },
        { label: t.filesPerHour, value: s.files_per_hour || 0, max: 30 },
        { label: t.linesChanged + ' (' + t.avgPerPR + ')', value: avgLines, max: 500 },
        { label: t.filesChanged + ' (' + t.avgPerPR + ')', value: avgFiles, max: 20 },
        { label: t.commits + ' (' + t.avgPerPR + ')', value: avgCommits, max: 5 }
      ];
      velData.forEach(function(g) {
        var pct = Math.min(100, Math.round((g.value / g.max) * 100));
        var el = document.createElement('div'); el.className = 'sv-gauge';
        el.innerHTML = '<div class="sv-gauge-label">' + g.label + '</div>' +
                       '<div class="sv-gauge-value">' + g.value + '</div>' +
                       '<div class="sv-gauge-bar"><div class="sv-gauge-fill" style="width:' + pct + '%"></div></div>';
        gauges.appendChild(el);
      });
    } else {
      velSection.style.display = 'none';
    }

    // 3. Time — 3-level tree: Issue → Comment → PR
    var tTotals = document.getElementById('sv-time-totals');
    var tContent = document.getElementById('sv-time-content');
    var hasComments = s.comments && s.comments.length > 0;
    // For time compilation: use aggregated PRs for root sessions with children, own PRs otherwise
    // Scoped to session date — exclude PRs from child sessions on different dates
    var tcPrs = (agg && agg.prs && agg.prs.length > 0) ? agg.prs : (s.prs || []);
    if (agg && tcPrs.length > 0) {
      var prSessionDate = (s.issue_created_at || s.date || '').substring(0, 10);
      if (prSessionDate) {
        tcPrs = tcPrs.filter(function(pr) {
          var prDate = (pr.created_at || '').substring(0, 10);
          return prDate === prSessionDate;
        });
      }
    }
    var hasPrs = tcPrs.length > 0;
    var hasAggComments = agg && agg.comments_by_task && agg.comments_by_task.length > 0;
    if (hasComments || hasAggComments || hasPrs) {
      // Compute calendar time span — use aggregated times for root sessions, own times otherwise
      var tcFirstTime = (agg ? agg.first_activity_time : null) || s.first_pr_time || s.issue_created_at || effFirstTime;
      var tcLastTime = (agg ? agg.last_activity_time : null) || s.last_pr_time || effLastTime;
      // For sessions with own comments, derive time span from comments + scoped PRs
      if (hasComments && s.comments.length > 0) {
        var ownTimes = [];
        s.comments.forEach(function(c) { if (c.created_at) ownTimes.push(c.created_at); if (c.updated_at) ownTimes.push(c.updated_at); });
        tcPrs.forEach(function(p) { if (p.created_at) ownTimes.push(p.created_at); if (p.merged_at) ownTimes.push(p.merged_at); });
        if (ownTimes.length > 0) { ownTimes.sort(); tcFirstTime = ownTimes[0]; tcLastTime = ownTimes[ownTimes.length - 1]; }
      }
      var calStart = tcFirstTime ? formatTime(tcFirstTime) : '\u2014';
      var calEnd = tcLastTime ? formatTime(tcLastTime) : '\u2014';
      var calDur = calcDuration(tcFirstTime, tcLastTime);
      var block = timeBlock(tcFirstTime);

      // Build the comment groups to render — scoped to session's active time window
      var commentGroups = [];

      // Determine this session's active time window
      // For continuation sessions: [created_at, next_sibling_created_at)
      // For original/root sessions: show all aggregated comments
      var sessionWindowStart = s.issue_created_at || tcFirstTime || null;
      var sessionWindowEnd = null;
      var isScoped = false;

      if (s.session_kind === 'continuation' && s.parent_tasks && s.parent_tasks.length > 0) {
        // Find siblings (all children of the same parent) sorted by creation time
        var parentNum = s.parent_tasks[0];
        var parentSession = null;
        for (var pi = 0; pi < sessionsData.sessions.length; pi++) {
          if (sessionsData.sessions[pi].task_number === parentNum) { parentSession = sessionsData.sessions[pi]; break; }
        }
        if (parentSession && parentSession.children_tasks) {
          var siblings = [];
          parentSession.children_tasks.forEach(function(cNum) {
            var cs = null;
            for (var ci = 0; ci < sessionsData.sessions.length; ci++) {
              if (sessionsData.sessions[ci].task_number === cNum) { cs = sessionsData.sessions[ci]; break; }
            }
            if (cs) siblings.push(cs);
          });
          siblings.sort(function(a, b) { return (a.issue_created_at || '').localeCompare(b.issue_created_at || ''); });
          // Find this session's position and set window end to next sibling's start
          for (var si = 0; si < siblings.length; si++) {
            if (siblings[si].task_number === s.task_number) {
              if (si + 1 < siblings.length) {
                sessionWindowEnd = siblings[si + 1].issue_created_at;
              }
              break;
            }
          }
          isScoped = true;

          // Gather all available comments from parent + all siblings
          var allSources = [parentSession].concat(siblings);
          var sourceMap = {}; // issue_number → {title, comments}
          allSources.forEach(function(src) {
            if (!src || !src.comments || src.comments.length === 0) return;
            var num = src.task_number;
            if (sourceMap[num]) return; // dedup
            sourceMap[num] = { task_number: num, task_title: src.title || '', comments: [] };
            src.comments.forEach(function(c) {
              var ct = c.created_at || '';
              if (ct >= sessionWindowStart && (!sessionWindowEnd || ct < sessionWindowEnd)) {
                sourceMap[num].comments.push(c);
              }
            });
          });
          // Build comment groups (only non-empty)
          Object.keys(sourceMap).forEach(function(k) {
            if (sourceMap[k].comments.length > 0) {
              commentGroups.push(sourceMap[k]);
            }
          });
          // Sort groups: session's own issue first, then by first comment time
          commentGroups.sort(function(a, b) {
            if (a.task_number === s.task_number) return -1;
            if (b.task_number === s.task_number) return 1;
            var aT = a.comments.length > 0 ? a.comments[0].created_at : '';
            var bT = b.comments.length > 0 ? b.comments[0].created_at : '';
            return aT.localeCompare(bT);
          });

          // Also scope PRs to the time window
          if (tcPrs.length > 0) {
            tcPrs = tcPrs.filter(function(pr) {
              var pt = pr.created_at || '';
              return pt >= sessionWindowStart && (!sessionWindowEnd || pt < sessionWindowEnd);
            });
          }
        }
      }

      if (commentGroups.length === 0 && !isScoped) {
        // For root sessions with children: use aggregated comments
        // Session-scoped: include all comments that occurred during the session's active date.
        // For related issues not created during this session, only keep comments
        // that fall within the session date (activities the session interacted with).
        if (hasAggComments) {
          var sessionDate = (s.issue_created_at || s.date || '').substring(0, 10);
          agg.comments_by_task.forEach(function(g) {
            // Always include the session's own issue fully
            if (g.task_number === s.task_number) {
              commentGroups.push({
                task_number: g.task_number,
                task_title: g.task_title || '',
                comments: g.comments
              });
              return;
            }
            // For other issues: only include comments that occurred on the session date
            var scopedComments = g.comments.filter(function(c) {
              var cDate = (c.created_at || '').substring(0, 10);
              return cDate === sessionDate;
            });
            if (scopedComments.length > 0) {
              commentGroups.push({
                task_number: g.task_number,
                task_title: g.task_title || '',
                comments: scopedComments
              });
            }
          });
        } else if (hasComments) {
          // Leaf session or no aggregation — use own comments only
          commentGroups = [{
            task_number: s.task_number,
            task_title: s.title || '',
            comments: s.comments
          }];
        }
      }

      // Count total comments across all groups
      var totalCommentCount = 0;
      commentGroups.forEach(function(g) { totalCommentCount += g.comments.length; });
      var itemCount = totalCommentCount || tcPrs.length;

      // Recompute time span from comment groups (scoped continuations or date-filtered root sessions)
      if ((isScoped || hasAggComments) && commentGroups.length > 0) {
        var allTimes = [];
        commentGroups.forEach(function(g) {
          g.comments.forEach(function(c) { if (c.created_at) allTimes.push(c.created_at); });
        });
        tcPrs.forEach(function(p) {
          if (p.created_at) allTimes.push(p.created_at);
          if (p.merged_at) allTimes.push(p.merged_at);
        });
        if (allTimes.length > 0) {
          allTimes.sort();
          tcFirstTime = allTimes[0];
          tcLastTime = allTimes[allTimes.length - 1];
          calStart = formatTime(tcFirstTime);
          calEnd = formatTime(tcLastTime);
          calDur = calcDuration(tcFirstTime, tcLastTime);
          block = timeBlock(effFirstTime);
        }
      }

      var scopeLabel = isScoped ? ' \u00b7 \ud83d\udd2c ' + (lang === 'fr' ? 'Fen\u00eatre de session' : 'Session window') : '';
      tTotals.textContent = t.totals + ': ' + itemCount + ' ' + t.tasks +
        (commentGroups.length > 1 ? ' \u00b7 ' + commentGroups.length + ' tasks' : '') +
        ' \u00b7 ' + t.calendarTime + ': ' + calStart + '\u2014' + calEnd +
        (calDur != null ? ' (' + formatDuration(calDur) + ')' : '') +
        ' \u00b7 ' + block + scopeLabel;

      if (commentGroups.length > 0) {
        // === Tree-based table: Issue rows → Comment rows → PR rows ===
        var tbl = '<table class="sv-table"><thead><tr>' +
          '<th>#</th><th>' + t.task + '</th><th>' + t.start + '</th><th>' + t.end + '</th>' +
          '<th>' + t.duration + '</th><th>' + t.inactive + '</th><th>' + t.calendar + '</th><th>' + t.status + '</th>' +
          '</tr></thead><tbody>';
        var totalActiveMin = 0;
        var totalInactiveMin = 0;
        var totalCalMin = 0;
        var globalRowIdx = 0;
        var isMultiTask = commentGroups.length > 1;
        // Track which PRs have been assigned to avoid counting a PR in multiple groups
        var assignedPrs = {};

        commentGroups.forEach(function(group, gIdx) {
          var groupComments = group.comments;
          var taskNum = group.task_number;
          var taskTitle = group.task_title || '';

          // Compute group-level time span
          var gFirstTime = groupComments.length > 0 ? groupComments[0].created_at : null;
          var gLastTime = groupComments.length > 0 ? groupComments[groupComments.length - 1].created_at : null;
          var gCalMin = calcDuration(gFirstTime, gLastTime);
          var gGroupActiveMin = 0;

          // Issue header row (level 0) — always rendered for all sessions
          var taskRowId = 'task-' + gIdx;
          var gStart = gFirstTime ? formatTime(gFirstTime) : '\u2014';
          var gEnd = gLastTime ? formatTime(gLastTime) : '\u2014';
          var taskLnk = taskNum ? '<a href="https://github.com/packetqc/knowledge/issues/' + taskNum + '" target="_blank" style="text-decoration:none">#' + taskNum + '</a>' : '';
          var truncTitle = taskTitle.length > 55 ? taskTitle.substring(0, 52) + '...' : taskTitle;
          tbl += '<tr class="sv-row-parent sv-row-task" data-task="' + taskRowId + '" style="background:var(--code-bg, #f0f4ff);font-weight:bold;cursor:pointer">' +
                 '<td></td>' +
                 '<td>' + (taskLnk ? taskLnk + ' ' : '') + '\ud83d\udccc ' + esc(truncTitle) + ' <span style="font-weight:normal;opacity:0.6">(' + groupComments.length + ')</span></td>' +
                 '<td>' + gStart + '</td>' +
                 '<td>' + gEnd + '</td>' +
                 '<td class="sv-task-active-' + gIdx + '"></td>' +
                 '<td></td>' +
                 '<td>' + formatDuration(gCalMin) + '</td>' +
                 '<td></td></tr>';

          // Map PRs to comments within this group by timestamp
          // Each PR is assigned to exactly one group (first best match wins)
          var prsByComment = {};
          if (hasPrs) {
            groupComments.forEach(function(c, ci) {
              prsByComment[ci] = [];
            });
            tcPrs.forEach(function(pr) {
              var prKey = (pr.number || '') + '-' + (pr.created_at || '');
              if (assignedPrs[prKey]) return; // Already assigned to another group
              var bestIdx = -1;
              for (var ci = groupComments.length - 1; ci >= 0; ci--) {
                if (groupComments[ci].created_at <= pr.created_at) {
                  bestIdx = ci;
                  break;
                }
              }
              if (bestIdx >= 0) {
                prsByComment[bestIdx].push(pr);
                assignedPrs[prKey] = true;
              }
            });
          }

          // Pre-compute end times for inactive gap calculation
          // Last comment in a group uses group's last time, not global session time
          var endTimes = [];
          groupComments.forEach(function(c, i) {
            var endIso = null;
            var estimated = false;
            if (c.updated_at && c.updated_at !== c.created_at) {
              endIso = c.updated_at;
            } else if (i + 1 < groupComments.length) {
              endIso = groupComments[i + 1].created_at;
              estimated = true;
            } else if (isMultiTask) {
              // Last comment in a multi-issue group: use group's last known time
              // (don't bleed global session time into this group's duration)
              endIso = gLastTime;
              estimated = true;
            } else if (tcLastTime) {
              endIso = effLastTime;
              estimated = true;
            }
            endTimes.push({ iso: endIso, estimated: estimated });
          });

          // --- Build runs of consecutive same-type comments ---
          var runs = [];
          groupComments.forEach(function(c, i) {
            if (runs.length === 0 || runs[runs.length - 1].type !== c.type) {
              runs.push({ type: c.type, indices: [i] });
            } else {
              runs[runs.length - 1].indices.push(i);
            }
          });

          // Helper to get preview text from a comment
          function getPreview(c) {
            var p = c.step_name || c.preview || '';
            p = p.replace(/<[^>]+>/g, '').replace(/\|/g, ' ').replace(/^#+\s*/g, '').replace(/\*\*/g, '').replace(/\[([^\]]*)\]\([^)]*\)/g, '$1').replace(/\s+/g, ' ').trim();
            if (p.length > 70) p = p.substring(0, 67) + '...';
            return p;
          }

          // Helper to render a single comment row (used for single-item runs and as children)
          function renderCommentRow(c, i, rowId, isChild, parentRowId) {
            var avatarUrl = c.type === 'user'
              ? 'https://raw.githubusercontent.com/packetqc/knowledge/main/references/Martin/vicky.png'
              : 'https://raw.githubusercontent.com/packetqc/knowledge/main/references/Martin/vicky-sunglasses.png';
            var avatarAlt = c.type === 'user' ? 'Martin' : 'Claude';
            var statusIcon = '';
            if (c.status === 'completed') statusIcon = '\u2705';
            else if (c.status === 'in_progress') statusIcon = '\u23f3';
            else if (c.type === 'user') statusIcon = '\ud83d\udcac';
            var cStart = formatTime(c.created_at);
            var endIso = endTimes[i].iso;
            var estimated = endTimes[i].estimated;
            var cEnd = endIso ? (estimated ? '~' + formatTime(endIso) : formatTime(endIso)) : '\u2014';
            var calMin = endIso ? calcDuration(c.created_at, endIso) : null;
            var hasCh = prsByComment[i] && prsByComment[i].length > 0;
            var activeMin = null;
            if (hasCh) {
              activeMin = 0;
              prsByComment[i].forEach(function(pr) {
                var d = calcDuration(pr.created_at, pr.merged_at);
                if (d != null && d > 0) activeMin += d;
              });
              if (activeMin === 0) activeMin = calMin;
            } else {
              activeMin = calMin;
            }
            var inactiveMin = null;
            if (i > 0 && endTimes[i - 1].iso) {
              var gap = calcDuration(endTimes[i - 1].iso, c.created_at);
              if (gap != null && gap > 0) inactiveMin = gap;
            }
            if (activeMin != null && activeMin > 0) { totalActiveMin += activeMin; gGroupActiveMin += activeMin; }
            if (inactiveMin != null && inactiveMin > 0) totalInactiveMin += inactiveMin;
            if (calMin != null && calMin > 0) totalCalMin += calMin;
            var preview = getPreview(c);
            var hasBody = c.body_lines && c.body_lines.length > 0;
            var rowClass = c.type === 'user' ? 'sv-row-user' : 'sv-row-bot';
            if (!isChild && hasBody) rowClass += ' sv-row-parent';
            rowClass += ' sv-row-child sv-task-child-' + gIdx;
            if (isChild) rowClass += ' sv-row-run-child';
            var html = '<tr class="' + rowClass + '" data-idx="' + rowId + '"' +
                   ' data-task="task-' + gIdx + '"' +
                   (isChild ? ' data-parent="' + parentRowId + '"' : '') +
                   ' style="padding-left:' + (isChild ? '1.2rem' : '0.5rem') + '">' +
                   '<td>' + (isChild ? '' : '<img src="' + avatarUrl + '" alt="' + avatarAlt + '" class="sv-avatar">') + '</td>' +
                   '<td>' + esc(preview) + '</td>' +
                   '<td>' + cStart + '</td>' +
                   '<td>' + cEnd + '</td>' +
                   '<td>' + formatDuration(activeMin) + '</td>' +
                   '<td>' + (inactiveMin != null ? formatDuration(inactiveMin) : '\u2014') + '</td>' +
                   '<td>' + formatDuration(calMin) + '</td>' +
                   '<td>' + statusIcon + '</td></tr>';
            // Comment body row
            if (hasBody && !isChild) {
              var bodyHtml = c.body_lines.map(function(line) { return esc(line); }).join('\n');
              html += '<tr class="sv-row-body" data-parent="' + rowId + '"' +
                     ' data-task="task-' + gIdx + '">' +
                     '<td></td><td colspan="7">' + bodyHtml + '</td></tr>';
            }
            return html;
          }

          // Helper to render PR rows at issue-child level (siblings of comment rows)
          function renderPRRows(commentIndices) {
            var html = '';
            commentIndices.forEach(function(ci) {
              if (!prsByComment[ci] || prsByComment[ci].length === 0) return;
              prsByComment[ci].forEach(function(pr) {
                var prStart = formatTime(pr.created_at);
                var prEnd = formatTime(pr.merged_at);
                var prDur = calcDuration(pr.created_at, pr.merged_at);
                html += '<tr class="sv-row-child sv-row-pr sv-task-child-' + gIdx + '"' +
                       ' data-task="task-' + gIdx + '">' +
                       '<td><svg class="sv-avatar" width="20" height="20" viewBox="0 0 16 16" style="vertical-align:middle;border-radius:50%;background:#8b5cf6;padding:2px;box-sizing:border-box" fill="#ffffff"><path fill-rule="evenodd" d="M5 3.254V3.25v.005a.75.75 0 110-.005v.004zm.45 1.9a2.25 2.25 0 10-1.95.218v5.256a2.25 2.25 0 101.5 0V7.123A5.735 5.735 0 009.25 9h1.378a2.251 2.251 0 100-1.5H9.25a4.25 4.25 0 01-3.8-2.346zM12.75 9a.75.75 0 100-1.5.75.75 0 000 1.5zm-8.5 4.5a.75.75 0 100-1.5.75.75 0 000 1.5z"></path></svg></td>' +
                       '<td>PR #' + pr.number + (pr.title ? ' \u2014 ' + esc(pr.title) : '') + '</td>' +
                       '<td>' + prStart + '</td>' +
                       '<td>' + prEnd + '</td>' +
                       '<td>' + formatDuration(prDur) + '</td>' +
                       '<td></td><td></td><td></td></tr>';
              });
            });
            return html;
          }

          // Render runs
          runs.forEach(function(run) {
            if (run.indices.length === 1) {
              // Single comment — render directly as before
              var i = run.indices[0];
              var rowId = globalRowIdx++;
              tbl += renderCommentRow(groupComments[i], i, rowId, false, null);
              // PRs at issue level (siblings, not children)
              tbl += renderPRRows([i]);
            } else {
              // Multi-comment run — render group header + collapsed children
              var firstIdx = run.indices[0];
              var lastIdx = run.indices[run.indices.length - 1];
              var firstC = groupComments[firstIdx];
              var lastC = groupComments[lastIdx];
              var groupRowId = globalRowIdx++;
              var avatarUrl = firstC.type === 'user'
                ? 'https://raw.githubusercontent.com/packetqc/knowledge/main/references/Martin/vicky.png'
                : 'https://raw.githubusercontent.com/packetqc/knowledge/main/references/Martin/vicky-sunglasses.png';
              var avatarAlt = firstC.type === 'user' ? 'Martin' : 'Claude';
              var typeLabel = firstC.type === 'user' ? 'Martin' : 'Claude';
              // Aggregate time for the run
              var runStart = formatTime(firstC.created_at);
              var runEndIso = endTimes[lastIdx].iso;
              var runEndEst = endTimes[lastIdx].estimated;
              var runEnd = runEndIso ? (runEndEst ? '~' + formatTime(runEndIso) : formatTime(runEndIso)) : '\u2014';
              var runCalMin = runEndIso ? calcDuration(firstC.created_at, runEndIso) : null;
              // Status: use last comment's status for the group
              var lastStatus = '';
              for (var ri = run.indices.length - 1; ri >= 0; ri--) {
                var rc = groupComments[run.indices[ri]];
                if (rc.status === 'completed') { lastStatus = '\u2705'; break; }
                if (rc.status === 'in_progress') { lastStatus = '\u23f3'; break; }
              }
              if (!lastStatus && firstC.type === 'user') lastStatus = '\ud83d\udcac';
              // Preview: first comment's preview
              var runPreview = getPreview(firstC);
              var rowClass = firstC.type === 'user' ? 'sv-row-user' : 'sv-row-bot';
              rowClass += ' sv-row-parent sv-row-child sv-task-child-' + gIdx + ' sv-row-run';
              tbl += '<tr class="' + rowClass + '" data-idx="' + groupRowId + '"' +
                     ' data-task="task-' + gIdx + '"' +
                     ' style="padding-left:0.5rem">' +
                     '<td><img src="' + avatarUrl + '" alt="' + avatarAlt + '" class="sv-avatar"></td>' +
                     '<td>' + esc(runPreview) + ' <span style="font-weight:normal;opacity:0.6">(' + run.indices.length + ')</span></td>' +
                     '<td>' + runStart + '</td>' +
                     '<td>' + runEnd + '</td>' +
                     '<td></td>' +
                     '<td></td>' +
                     '<td>' + formatDuration(runCalMin) + '</td>' +
                     '<td>' + lastStatus + '</td></tr>';
              // Render individual comments as collapsed children
              run.indices.forEach(function(ci) {
                var childRowId = globalRowIdx++;
                tbl += renderCommentRow(groupComments[ci], ci, childRowId, true, groupRowId);
              });
              // PRs at issue level (siblings of the run, not nested inside)
              tbl += renderPRRows(run.indices);
            }
          });

          // Fill in the group's active time in the issue header row
          (function(idx, activeMin) {
            setTimeout(function() {
              var activeCell = tContent.querySelector('.sv-task-active-' + idx);
              if (activeCell) activeCell.textContent = formatDuration(activeMin);
            }, 0);
          })(gIdx, gGroupActiveMin);
        });

        tbl += '</tbody>';
        // Use actual calendar span for totals (not sum of tiles which can exceed real span)
        var footerCalMin = calDur != null ? calDur : totalCalMin;
        var footerInactiveMin = footerCalMin > totalActiveMin ? footerCalMin - totalActiveMin : 0;
        tbl += '<tfoot><tr style="font-weight:bold;border-top:2px solid var(--border, #93c5fd)">' +
               '<td colspan="4" style="text-align:right">' + t.totals + '</td>' +
               '<td>' + formatDuration(totalActiveMin) + '</td>' +
               '<td>' + formatDuration(footerInactiveMin) + '</td>' +
               '<td>' + formatDuration(footerCalMin) + '</td>' +
               '<td></td></tr></tfoot>';
        tbl += '</table>';
        tbl += '<p class="sv-time-note" style="margin:0.5em 0 0;font-size:0.85em;color:var(--text-secondary, #6b7280);font-style:italic">' +
          (lang === 'fr'
            ? '\u2139\ufe0f Le temps inactif refl\u00e8te les r\u00e9flexions, d\u00e9cisions et courtes pauses entre les interactions utilisateur\u2013syst\u00e8me.'
            : '\u2139\ufe0f Inactive time reflects reflections, decisions, and short pauses between user\u2013system interactions.') +
          '</p>';
        tContent.innerHTML = tbl;

        // --- Expand/collapse state persistence (localStorage) ---
        var tcStateKey = 'sv-tc-state-' + (s.task_number || s.id);
        function tcLoadState() {
          try { return JSON.parse(localStorage.getItem(tcStateKey)) || {}; } catch(e) { return {}; }
        }
        function tcSaveState(state) {
          try { localStorage.setItem(tcStateKey, JSON.stringify(state)); } catch(e) {}
        }

        function tcSetTask(row, expand, state, save) {
          var taskId = row.getAttribute('data-task');
          var gKey = taskId.replace('task-', '');
          if (expand) { row.classList.add('sv-expanded'); } else { row.classList.remove('sv-expanded'); }
          tContent.querySelectorAll('.sv-task-child-' + gKey).forEach(function(child) {
            if (expand) {
              // Skip run children and body rows — they are controlled by their parent run/comment
              if (child.classList.contains('sv-row-run-child') || child.classList.contains('sv-row-body')) return;
              child.classList.add('sv-visible');
            } else {
              child.classList.remove('sv-visible');
              child.classList.remove('sv-expanded');
              var childIdx = child.getAttribute('data-idx');
              if (childIdx) {
                tContent.querySelectorAll('.sv-row-pr[data-parent="' + childIdx + '"],.sv-row-body[data-parent="' + childIdx + '"],.sv-row-run-child[data-parent="' + childIdx + '"]').forEach(function(sub) {
                  sub.classList.remove('sv-visible');
                });
                if (state) state['c-' + childIdx] = false;
              }
            }
          });
          if (state) { state['g-' + gKey] = expand; if (save) tcSaveState(state); }
        }

        function tcSetComment(row, expand, state, save) {
          var idx = row.getAttribute('data-idx');
          if (expand) { row.classList.add('sv-expanded'); } else { row.classList.remove('sv-expanded'); }
          tContent.querySelectorAll('.sv-row-pr[data-parent="' + idx + '"],.sv-row-body[data-parent="' + idx + '"],.sv-row-run-child[data-parent="' + idx + '"]').forEach(function(child) {
            if (expand) {
              child.classList.add('sv-visible');
              // When revealing a run-child, also reveal its nested PR and body rows
              var childIdx = child.getAttribute('data-idx');
              if (childIdx) {
                tContent.querySelectorAll('.sv-row-pr[data-parent="' + childIdx + '"],.sv-row-body[data-parent="' + childIdx + '"]').forEach(function(nested) {
                  nested.classList.add('sv-visible');
                });
              }
            } else {
              child.classList.remove('sv-visible');
              child.classList.remove('sv-expanded');
              // When hiding a run-child, also hide its nested PR and body rows
              var childIdx = child.getAttribute('data-idx');
              if (childIdx) {
                tContent.querySelectorAll('.sv-row-pr[data-parent="' + childIdx + '"],.sv-row-body[data-parent="' + childIdx + '"]').forEach(function(nested) {
                  nested.classList.remove('sv-visible');
                });
                if (state) state['c-' + childIdx] = false;
              }
            }
          });
          if (state) { state['c-' + idx] = expand; if (save) tcSaveState(state); }
        }

        // Toggle handlers — issue rows
        tContent.querySelectorAll('.sv-row-task').forEach(function(row) {
          row.addEventListener('click', function() {
            var state = tcLoadState();
            tcSetTask(this, !this.classList.contains('sv-expanded'), state, true);
          });
        });

        // Toggle handlers — comment rows (expand/collapse body + PRs)
        tContent.querySelectorAll('.sv-row-parent:not(.sv-row-task)').forEach(function(row) {
          row.addEventListener('click', function(e) {
            e.stopPropagation();
            var state = tcLoadState();
            tcSetComment(this, !this.classList.contains('sv-expanded'), state, true);
          });
        });

        // Restore saved state or start collapsed (default)
        var tcState = tcLoadState();
        var hasState = Object.keys(tcState).length > 0;
        if (hasState) {
          tContent.querySelectorAll('.sv-row-task').forEach(function(row) {
            var gKey = row.getAttribute('data-task').replace('task-', '');
            if (tcState['g-' + gKey]) tcSetTask(row, true, null, false);
          });
          tContent.querySelectorAll('.sv-row-parent:not(.sv-row-task)').forEach(function(row) {
            var idx = row.getAttribute('data-idx');
            if (tcState['c-' + idx]) tcSetComment(row, true, null, false);
          });
        }
        // No saved state = everything starts collapsed (single or multi-issue)
      } else {
        // === Legacy PR-based table (no comments) ===
        var tbl = '<table class="sv-table"><thead><tr>' +
          '<th>#</th><th>' + t.task + '</th><th>' + t.start + '</th><th>' + t.end + '</th>' +
          '<th>' + t.duration + '</th><th>' + t.inactive + '</th><th>' + t.calendar + '</th><th>' + t.category + '</th>' +
          '</tr></thead><tbody>';
        var totalDurMin = 0;
        var totalCalMin = 0;
        tcPrs.forEach(function(pr, i) {
          var prStart = formatTime(pr.created_at);
          var prEnd = formatTime(pr.merged_at);
          var prDur = calcDuration(pr.created_at, pr.merged_at);
          var nextStart = (i + 1 < tcPrs.length) ? tcPrs[i + 1].created_at : pr.merged_at;
          var prCal = calcDuration(pr.created_at, nextStart);
          var prInactive = (prCal != null && prDur != null) ? Math.max(0, prCal - prDur) : null;
          if (prDur != null) totalDurMin += prDur;
          if (prCal != null) totalCalMin += prCal;
          tbl += '<tr><td><strong>T' + (i+1) + '</strong></td>' +
                 '<td>PR #' + pr.number + (pr.title ? ' \u2014 ' + esc(pr.title) : '') + '</td>' +
                 '<td>' + prStart + '</td>' +
                 '<td>' + prEnd + '</td>' +
                 '<td>' + formatDuration(prDur) + '</td>' +
                 '<td>' + (prInactive != null ? formatDuration(prInactive) : '\u2014') + '</td>' +
                 '<td>' + formatDuration(prCal) + '</td>' +
                 '<td>' + (s.request_type ? reqTypeBadge(s.request_type) : esc(s.type || '\u2014')) + '</td></tr>';
        });
        var totalInactive = Math.max(0, totalCalMin - totalDurMin);
        tbl += '</tbody><tfoot><tr style="font-weight:bold;border-top:2px solid var(--border, #93c5fd)">' +
               '<td colspan="4" style="text-align:right">' + t.totals + '</td>' +
               '<td>' + formatDuration(totalDurMin) + '</td>' +
               '<td>' + formatDuration(totalInactive) + '</td>' +
               '<td>' + formatDuration(totalCalMin) + '</td>' +
               '<td></td></tr></tfoot></table>';
        tbl += '<p class="sv-time-note" style="margin:0.5em 0 0;font-size:0.85em;color:var(--text-secondary, #6b7280);font-style:italic">' +
          (lang === 'fr'
            ? '\u2139\ufe0f Le temps inactif refl\u00e8te les r\u00e9flexions, d\u00e9cisions et courtes pauses entre les interactions utilisateur\u2013syst\u00e8me.'
            : '\u2139\ufe0f Inactive time reflects reflections, decisions, and short pauses between user\u2013system interactions.') +
          '</p>';
        tContent.innerHTML = tbl;
      }
    } else {
      tTotals.textContent = '';
      tContent.innerHTML = '<p class="sv-muted">' + t.noTimeData + '</p>';
    }

    // === PIE CHARTS ===
    // For charts, temporarily overlay effective data when aggregated
    var chartSession = s;
    if (agg) {
      chartSession = Object.assign({}, s, {
        prs: effPrs,
        pr_count: effPrCount,
        total_additions: effAdditions,
        total_deletions: effDeletions,
        total_files_changed: effFiles,
        total_commits: effCommits,
        active_minutes: effActive,
        first_pr_time: effFirstTime,
        last_pr_time: effLastTime
      });
    }
    renderCharts(chartSession, hasComments || hasAggComments, hasPrs);

    // 4. Deliveries (PRs) — use aggregated PRs if available
    var pBody = document.getElementById('sv-prs-body');
    pBody.innerHTML = '';
    if (!effPrs || effPrs.length === 0) {
      pBody.innerHTML = '<tr><td colspan="6" class="sv-muted">' + t.noPRs + '</td></tr>';
    } else {
      var prTotalAdd = 0, prTotalDel = 0, prTotalFiles = 0, prTotalCommits = 0;
      effPrs.forEach(function(pr) {
        var r = document.createElement('tr');
        var lnk = 'https://github.com/packetqc/knowledge/pull/' + pr.number;
        var add = pr.additions || 0, del = pr.deletions || 0, files = pr.changed_files || 0, cm = pr.commits || 0;
        prTotalAdd += add; prTotalDel += del; prTotalFiles += files; prTotalCommits += cm;
        var diffStr = add || del ? '<span style="color:#16a34a">+' + add + '</span> <span style="color:#dc2626">\u2212' + del + '</span>' : '\u2014';
        r.innerHTML = '<td><strong>#' + pr.number + '</strong></td><td>' + esc(pr.title || '\u2014') +
                      '</td><td>' + diffStr + '</td><td>' + (files || '\u2014') + '</td><td>' + (cm || '\u2014') +
                      '</td><td><a href="' + lnk + '" target="_blank">' + t.view + '</a></td>';
        pBody.appendChild(r);
      });
      // Totals footer row
      if (effPrs.length > 1) {
        var foot = document.createElement('tr');
        foot.style.cssText = 'font-weight:bold;border-top:2px solid var(--border, #93c5fd)';
        foot.innerHTML = '<td colspan="2" style="text-align:right">' + t.totals + '</td>' +
                         '<td><span style="color:#16a34a">+' + prTotalAdd + '</span> <span style="color:#dc2626">\u2212' + prTotalDel + '</span></td>' +
                         '<td>' + prTotalFiles + '</td><td>' + prTotalCommits + '</td><td></td>';
        pBody.appendChild(foot);
      }
    }
    // Issues (separate section — table format)
    var iSection = document.getElementById('sv-section-related-tasks');
    var iBody = document.getElementById('sv-tasks-body');
    var hasSessionTask = s.task_number && s.task_number !== null;
    var relatedTasks = s.related_tasks || [];
    // Fallback: if related_tasks not enriched, build from issues array
    if (relatedTasks.length === 0) {
      var relatedNums = (s.related_tasks || []).filter(function(n) { return n !== s.task_number; });
      relatedNums.forEach(function(n) {
        relatedTasks.push({ number: n, title: '', state: '', labels: [] });
      });
    }
    var totalTaskCount = (hasSessionTask ? 1 : 0) + relatedTasks.length;
    if (hasSessionTask || relatedTasks.length > 0) {
      iSection.style.display = '';
      iBody.innerHTML = '';
      // Update table headers with translated labels
      var thead = iBody.parentElement.querySelector('thead tr');
      thead.innerHTML = '<th>#</th><th>' + t.taskCol + '</th><th>' + t.typeCol + '</th><th>' + t.titleCol + '</th><th>' + t.sessionCol + '</th>';
      var taskIdx = 0;
      // Row 1: session's own issue
      if (hasSessionTask) {
        taskIdx++;
        var sr = document.createElement('tr');
        var sHref = 'https://github.com/packetqc/knowledge/issues/' + s.task_number;
        // Session kind emoji: 💬 original, 🔁 continuation
        var sKindEmoji = s.session_kind === 'continuation' ? '\ud83d\udd01' : '\ud83d\udcac';
        sr.innerHTML = '<td><strong>' + taskIdx + '</strong></td>' +
                       '<td><a href="' + sHref + '" target="_blank">#' + s.task_number + '</a></td>' +
                       '<td>' + taskLabelBadge(s.task_number, t.taskTypeSession) + '</td>' +
                       '<td>' + sKindEmoji + ' ' + esc(s.title || '') + '</td>' +
                       '<td><span style="opacity:0.5">\u2014</span></td>';
        iBody.appendChild(sr);
      }
      // Remaining rows: related issues with tree-aware emojis
      // 🔗 = non-session related issue
      // 💬 = parent session (created before current, in tree)
      // 🔁 = child/continuation session (created after current, in tree)
      var parentTasks = s.parent_tasks || [];
      var childrenTasks = s.children_tasks || [];
      relatedTasks.forEach(function(ri) {
        taskIdx++;
        var rr = document.createElement('tr');
        var rHref = 'https://github.com/packetqc/knowledge/issues/' + ri.number;
        var riTitle = ri.title || '\u2014';
        var riEmoji = '\ud83d\udd17'; // 🔗 default (related issue)
        if (parentTasks.indexOf(ri.number) !== -1) {
          riEmoji = '\ud83d\udcac'; // 💬 parent session
        } else if (childrenTasks.indexOf(ri.number) !== -1) {
          riEmoji = '\ud83d\udd01'; // 🔁 child/continuation session
        }
        var riSessionId = 'task-' + ri.number;
        var riSession = findSession(riSessionId);
        var riSessionCell = '';
        if (riSession) {
          riSessionCell = '<a href="javascript:void(0)" onclick="event.stopPropagation();document.getElementById(\'sv-session-select\').value=\'' + riSessionId + '\';document.getElementById(\'sv-session-select\').dispatchEvent(new Event(\'change\'))" title="' + esc(t.openSession) + '" style="margin-right:0.4em">\ud83d\udd0d</a>' +
                          '<a href="' + window.location.pathname + '?session=' + ri.number + '" target="_blank" title="' + esc(t.openTab) + '">\ud83d\udd17</a>';
        } else {
          riSessionCell = '<span style="opacity:0.5">\u2014</span>';
        }
        rr.innerHTML = '<td><strong>' + taskIdx + '</strong></td>' +
                       '<td><a href="' + rHref + '" target="_blank">#' + ri.number + '</a></td>' +
                       '<td>' + taskLabelBadge(ri.number, t.taskTypeRelated) + '</td>' +
                       '<td>' + riEmoji + ' ' + esc(riTitle) + '</td>' +
                       '<td>' + riSessionCell + '</td>';
        iBody.appendChild(rr);
      });
      // Totals footer row
      if (totalTaskCount > 1) {
        var ifoot = document.createElement('tr');
        ifoot.style.cssText = 'font-weight:bold;border-top:2px solid var(--border, #93c5fd)';
        ifoot.innerHTML = '<td colspan="3" style="text-align:right">' + t.totals + '</td>' +
                         '<td>' + totalTaskCount + ' issues</td>' +
                         '<td></td>';
        iBody.appendChild(ifoot);
      }
    } else { iSection.style.display = 'none'; }

    // 5. Lessons
    var lList = document.getElementById('sv-lessons-list');
    var noL = document.getElementById('sv-no-lessons');
    lList.innerHTML = '';
    if (!s.lessons || s.lessons.length === 0) {
      lList.style.display = 'none'; noL.style.display = ''; noL.textContent = t.noLessons;
    } else {
      lList.style.display = ''; noL.style.display = 'none';
      s.lessons.forEach(function(l) {
        var li = document.createElement('li'); li.textContent = l; lList.appendChild(li);
      });
    }
  }

  selectEl.addEventListener('change', function() { showSession(this.value); });

  // ===== Session-specific PDF export override =====
  // After layout JS loads, replace the exportPdf handler with session-aware version
  setTimeout(function() {
    var btn = document.getElementById('exportPdf');
    if (!btn) return;
    // Clone button to remove layout's default handler
    var newBtn = btn.cloneNode(true);
    btn.parentNode.replaceChild(newBtn, btn);
    newBtn.addEventListener('click', function() {
      var PAGE_SIZES = { letter: '8.5in 11in', legal: '8.5in 14in' };
      var sizeRadio = document.querySelector('input[name="pubPageSize"]:checked');
      var orientRadio = document.querySelector('input[name="pubOrient"]:checked');
      var format = sizeRadio ? sizeRadio.value : 'letter';
      var orient = orientRadio ? orientRadio.value : 'portrait';
      var size = PAGE_SIZES[format] || PAGE_SIZES.letter;
      if (orient === 'landscape') size += ' landscape';
      // Build session-specific filename: Session - 2026-02-27 15h33 - Title.pdf
      var origTitle = document.title;
      var fileName = 'Session Review';
      if (currentSession) {
        var cs = currentSession;
        var d = cs.date || '';
        var tm = cs.first_pr_time ? formatTime(cs.first_pr_time).replace(':', 'h') : '';
        var title = (cs.title || 'Untitled').replace(/[\u2014\u2013<>:"\/\\|?*#]/g, '').trim();
        if (title.length > 60) title = title.substring(0, 57) + '...';
        fileName = 'Session - ' + d + (tm ? ' ' + tm : '') + ' - ' + title;
      }
      document.title = fileName;
      // Generate timestamp
      var now = new Date();
      var ts = now.getFullYear() + '-' +
        String(now.getMonth() + 1).padStart(2, '0') + '-' +
        String(now.getDate()).padStart(2, '0') + ' ' +
        String(now.getHours()).padStart(2, '0') + ':' +
        String(now.getMinutes()).padStart(2, '0');
      // Populate cover page with session metadata
      var coverPage = document.getElementById('sv-cover-page');
      if (coverPage && currentSession) {
        var cs = currentSession;
        document.getElementById('sv-cover-title').textContent = cs.title || 'Untitled';
        var descParts = [];
        if (cs.type) descParts.push(cs.type);
        if (cs.request_type) descParts.push(cs.request_type);
        document.getElementById('sv-cover-desc').textContent = descParts.join(' \u2014 ') || 'Session Report';
        var metaLines = '';
        if (cs.date) metaLines += '<div>Date: ' + cs.date + '</div>';
        if (cs.branch) metaLines += '<div>Branch: <code>' + cs.branch + '</code></div>';
        if (cs.task_number) metaLines += '<div>Task: #' + cs.task_number + '</div>';
        var prCount = cs.prs ? cs.prs.length : 0;
        var commentCount = cs.comments ? cs.comments.length : 0;
        metaLines += '<div>' + prCount + ' PRs \u00b7 ' + commentCount + ' comments</div>';
        metaLines += '<div class="cover-gen-line">Generated: ' + ts + '</div>';
        metaLines += '<div style="margin-top:0.5cm;font-size:9pt;color:#555">Authors: Martin Paquet &amp; Claude (Anthropic, Opus 4.6)</div>';
        document.getElementById('sv-cover-meta').innerHTML = metaLines;
        coverPage.style.display = 'flex';
      }
      var styleEl = document.getElementById('printSizeStyle');
      if (styleEl) {
        styleEl.textContent =
          '@page { size: ' + size + '; }\n' +
          '@page {\n' +
          '  @bottom-left   { content: "Generated: ' + ts + '"; }\n' +
          '  @bottom-center { content: counter(page) " / " counter(pages); }\n' +
          '  @bottom-right  { content: "Knowledge"; }\n' +
          '}\n' +
          '@page :first {\n' +
          '  @top-left    { content: ""; border: none; }\n' +
          '  @top-center  { content: ""; border: none; }\n' +
          '  @top-right   { content: ""; border: none; }\n' +
          '  @bottom-left   { content: ""; border: none; }\n' +
          '  @bottom-center { content: ""; border: none; }\n' +
          '  @bottom-right  { content: ""; border: none; }\n' +
          '}';
      }
      window.addEventListener('afterprint', function() {
        document.title = origTitle;
        if (coverPage) coverPage.style.display = 'none';
      }, { once: true });
      setTimeout(function() { window.print(); }, 0);
    });
  }, 0);
})();
