/* ═══ Tasks Workflow Viewer (I3) — JavaScript ═══ */

// Landscape default — per-page key (matches session-core.js pattern)
(function() {
  var KEY = 'knowledge-orient:' + location.pathname.replace(/\/+$/, '');
  if (!localStorage.getItem(KEY)) localStorage.setItem(KEY, 'landscape');
})();

(function () {
  'use strict';

  var root = document.getElementById('tw-viewer');
  if (!root) return;
  var baseurl = root.getAttribute('data-baseurl') || '';
  var dataUrl = baseurl + '/data/tasks.json';

  // ── Bilingual labels ──
  var lang = (document.documentElement.lang === 'fr' || window.location.pathname.indexOf('/fr/') !== -1) ? 'fr' : 'en';
  var L = {
    en: {
      selectTask: '— Select a task —',
      allStages: 'All stages',
      overview: 'Overview', detail: 'Detail',
      validation: 'Validation', progression: 'Progression',
      tasks: 'tasks', stage: 'Stage', progress: 'Progress',
      passed: 'Passed', failed: 'Failed', skipped: 'Skipped',
      pending: 'Pending', total: 'Total', noData: 'No data',
      loadError: 'Failed to load task data.',
      stageDistribution: 'Stage Distribution',
      validationResults: 'Validation Results',
      unitTests: 'Unit Tests', checks: 'Checks',
      direction: 'Direction', reason: 'Reason',
      entered: 'Entered', duration: 'Duration',
      source: 'Source', result: 'Result', updated: 'Updated',
      relatedTasks: 'Related Tasks',
      stagesVisited: 'Stages visited',
      transitions: 'Transitions',
      validations: 'Validations',
      dashboard: 'Dashboard',
      knowledgeGrid: 'Request Validation Grid',
      metrics: 'Metrics', prs: 'PRs',
      filesChanged: 'Files changed', linesChanged: 'Lines changed',
      additions: 'Additions', deletions: 'Deletions', deliverables: 'Deliverables',
      timeCompilation: 'Time Compilation',
      calendarTime: 'Calendar time', activeTime: 'Active time',
      inactiveTime: 'Inactive time', blocks: 'Blocks',
      stageDuration: 'Stage Duration Breakdown',
      proportions: 'Time Proportions',
      ofActive: '% of Active',
      stageNames: {
        initial: 'Initial', plan: 'Plan', analyze: 'Analyze',
        implement: 'Implement', validation: 'Validation',
        documentation: 'Documentation', approval: 'Approval',
        completion: 'Completion'
      },
    },
    fr: {
      selectTask: '— Sélectionner une tâche —',
      allStages: 'Toutes les étapes',
      overview: 'Aperçu', detail: 'Détail',
      validation: 'Validation', progression: 'Progression',
      tasks: 'tâches', stage: 'Étape', progress: 'Progrès',
      passed: 'Réussi', failed: 'Échoué', skipped: 'Ignoré',
      pending: 'En attente', total: 'Total', noData: 'Aucune donnée',
      loadError: 'Échec du chargement des données.',
      stageDistribution: 'Distribution des étapes',
      validationResults: 'Résultats de validation',
      unitTests: 'Tests unitaires', checks: 'Vérifications',
      direction: 'Direction', reason: 'Raison',
      entered: 'Début', duration: 'Durée',
      source: 'Source', result: 'Résultat', updated: 'Mis à jour',
      relatedTasks: 'Tâches associées',
      stagesVisited: 'Étapes visitées',
      transitions: 'Transitions',
      validations: 'Validations',
      dashboard: 'Tableau de bord',
      knowledgeGrid: 'Grille de validation de la demande',
      metrics: 'Métriques', prs: 'PRs',
      filesChanged: 'Fichiers modifiés', linesChanged: 'Lignes modifiées',
      additions: 'Ajouts', deletions: 'Suppressions', deliverables: 'Livrables',
      timeCompilation: 'Compilation temporelle',
      calendarTime: 'Temps calendrier', activeTime: 'Temps actif',
      inactiveTime: 'Temps inactif', blocks: 'Blocs',
      stageDuration: 'Durées par étape',
      proportions: 'Proportions temporelles',
      ofActive: '% du actif',
      stageNames: {
        initial: 'Initial', plan: 'Planification', analyze: 'Analyse',
        implement: 'Implémentation', validation: 'Validation',
        documentation: 'Documentation', approval: 'Approbation',
        completion: 'Complétion'
      },
    }
  };
  var t = L[lang] || L.en;

  // Helper: translate a stage identifier to display name
  function stageName(s) { return (t.stageNames && t.stageNames[s]) || s; }

  // ── Selectors ──
  var taskSelect = document.getElementById('tw-task-select');
  var viewSelect = document.getElementById('tw-view-select');
  var emptyState = document.getElementById('tw-empty-state');
  var taskCount = document.getElementById('tw-task-count');

  if (!taskSelect || !viewSelect || !emptyState) {
    console.error('I3: Required DOM elements missing');
    return;
  }

  var views = {
    dashboard: document.getElementById('tw-view-dashboard'),
    detail: document.getElementById('tw-view-detail'),
    validation: document.getElementById('tw-view-validation'),
  };

  var allTasks = [];
  var selectedTask = null;
  var overviewEl = document.getElementById('tw-view-overview');
  var allTasksLabel = lang === 'fr' ? '\u2014 Toutes les t\u00e2ches \u2014' : '\u2014 All Tasks \u2014';

  // ── Theme detection ──
  function isDarkTheme() {
    var dt = document.documentElement.getAttribute('data-theme') || '';
    return (dt === 'midnight' || dt === 'daltonism-dark') ||
           (!dt || dt === 'auto') && window.matchMedia &&
           window.matchMedia('(prefers-color-scheme: dark)').matches;
  }

  // ── Stage colors (theme-aware) ──
  var stageColorsLight = {
    initial: '#6f42c1',
    plan: '#0366d6',
    analyze: '#0891b2',
    implement: '#2ea44f',
    validation: '#d29922',
    approval: '#f97316',
    documentation: '#8b5cf6',
    completion: '#28a745',
  };

  var stageColorsDark = {
    initial: '#a371f7',
    plan: '#58a6ff',
    analyze: '#3bc9db',
    implement: '#3fb950',
    validation: '#d29922',
    approval: '#f0883e',
    documentation: '#bc8cff',
    completion: '#56d364',
  };

  function getStageColors() {
    return isDarkTheme() ? stageColorsDark : stageColorsLight;
  }

  var stageColors = getStageColors();

  var stageLabels = [
    'initial', 'plan', 'analyze', 'implement',
    'validation', 'documentation', 'approval', 'completion'
  ];

  // ── Utilities ──
  function esc(s) {
    var d = document.createElement('div');
    d.textContent = s || '';
    return d.innerHTML;
  }

  function shortDate(iso) {
    if (!iso) return '—';
    var d = new Date(iso);
    return d.getFullYear() + '-' + ('0'+(d.getMonth()+1)).slice(-2) + '-' + ('0'+d.getDate()).slice(-2);
  }

  function shortTime(iso) {
    if (!iso) return '—';
    var d = new Date(iso);
    return ('0'+d.getHours()).slice(-2) + ':' + ('0'+d.getMinutes()).slice(-2) + ':' + ('0'+d.getSeconds()).slice(-2);
  }

  function durationStr(startIso, endIso) {
    if (!startIso || !endIso) return '—';
    var ms = new Date(endIso) - new Date(startIso);
    if (ms < 0) return '—';
    var secs = Math.floor(ms / 1000);
    if (secs < 60) return secs + 's';
    var mins = Math.floor(secs / 60);
    secs = secs % 60;
    if (mins < 60) return mins + 'm ' + secs + 's';
    var hrs = Math.floor(mins / 60);
    mins = mins % 60;
    return hrs + 'h ' + mins + 'm';
  }

  function resultIcon(result) {
    if (result === 'passed') return '<span class="tw-result-passed">&#x2705;</span>';
    if (result === 'failed') return '<span class="tw-result-failed">&#x274C;</span>';
    if (result === 'skipped') return '<span class="tw-result-skipped">&#x23ED;</span>';
    return '<span class="tw-result-pending">&#x2B1C;</span>';
  }

  // ── localStorage helpers ──
  function lsGet(key) {
    try { return localStorage.getItem(key); }
    catch (e) { return null; }
  }

  function lsSet(key, val) {
    try { localStorage.setItem(key, val); }
    catch (e) { /* storage unavailable */ }
  }

  // ── Data Loading ──
  function loadData() {
    fetch(dataUrl)
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then(function (data) {
        allTasks = data.tasks || [];
        if (taskCount) taskCount.textContent = allTasks.length;
        populateTaskSelect();
      })
      .catch(function (err) {
        console.error('Failed to load tasks.json:', err);
        if (taskCount) taskCount.textContent = '0';
        var p = emptyState.querySelector('p');
        if (p) p.textContent = t.loadError;
        emptyState.style.display = '';
        hideAllViews();
      });
  }

  function populateTaskSelect() {
    taskSelect.innerHTML = '<option value="">' + allTasksLabel + '</option>';

    // Sort by date descending (most recent first)
    var sorted = allTasks.slice().sort(function (a, b) {
      var da = a.started_at || a.updated_at || '';
      var db = b.started_at || b.updated_at || '';
      return db.localeCompare(da);
    });

    // Group by date for optgroup headers (items indented under date like Session Viewer)
    var currentDate = '';
    var currentGroup = null;
    sorted.forEach(function (task) {
      var taskDate = shortDate(task.started_at || task.updated_at || '');
      if (taskDate && taskDate !== currentDate) {
        currentDate = taskDate;
        currentGroup = document.createElement('optgroup');
        currentGroup.label = taskDate;
        taskSelect.appendChild(currentGroup);
      }
      var opt = document.createElement('option');
      opt.value = task.id;
      var timeRaw = task.started_at || '';
      var time = timeRaw ? shortTime(timeRaw).substring(0, 5) : '';
      var prefix = task.task_number ? '#' + task.task_number + ' ' : '';
      opt.textContent = (time ? time + ' ' : '') + prefix + (task.title || 'Untitled') + ' [' + task.current_stage + ']';
      if (currentGroup) {
        currentGroup.appendChild(opt);
      } else {
        taskSelect.appendChild(opt);
      }
    });

    // Auto-select: URL param > localStorage > all tasks overview
    var params = new URLSearchParams(window.location.search);
    var taskParam = params.get('task');
    if (taskParam && taskSelect.querySelector('option[value="' + taskParam + '"]')) {
      taskSelect.value = taskParam;
      selectTask(taskParam);
    } else {
      var saved = lsGet('tw-selected-task');
      if (saved && taskSelect.querySelector('option[value="' + saved + '"]')) {
        taskSelect.value = saved;
        selectTask(saved);
      } else {
        // Default: show all tasks overview
        selectTask('');
      }
    }
  }

  var taskProgression = document.getElementById('tw-task-progression');

  function selectTask(taskId) {
    // "All Tasks" overview mode
    if (!taskId) {
      selectedTask = null;
      emptyState.style.display = 'none';
      hideAllViews();
      if (taskProgression) taskProgression.style.display = 'none';
      if (overviewEl) {
        overviewEl.style.display = '';
        renderTaskOverview();
      }
      try { localStorage.removeItem('tw-selected-task'); } catch(e) {}
      return;
    }
    // Hide overview when viewing a single task
    if (overviewEl) overviewEl.style.display = 'none';

    selectedTask = allTasks.find(function (tk) { return tk.id === taskId; }) || null;
    if (selectedTask) {
      emptyState.style.display = 'none';
      showView(viewSelect.value);
      lsSet('tw-selected-task', taskId);
      renderTaskProgression(selectedTask);
    } else {
      emptyState.style.display = '';
      hideAllViews();
      if (taskProgression) taskProgression.style.display = 'none';
    }
    renderCurrentView();
  }

  // ── Task Progression (always visible when task selected) ──
  function renderTaskProgression(task) {
    if (!taskProgression || !task) return;
    taskProgression.style.display = '';
    var bar = document.getElementById('tw-progression-bar');
    var meta = document.getElementById('tw-progression-meta');
    if (!bar) return;

    var currentIdx = task.current_stage_index || 0;
    var html = '';
    stageLabels.forEach(function (stage, i) {
      var dotClass = 'tw-prog-dot';
      var dotContent = '';
      var vs = (task.validation_summary || {})[stage];

      if (vs && vs.skipped) {
        dotClass += ' skipped';
        dotContent = '&#x23ED;';
      } else if (i < currentIdx) {
        dotClass += ' completed';
        dotContent = '&#x2713;';
      } else if (i === currentIdx) {
        dotClass += ' current';
        dotContent = (i + 1);
      } else {
        dotClass += ' pending';
        dotContent = (i + 1);
      }

      html += '<div class="tw-prog-node">' +
        '<div class="' + dotClass + '">' + dotContent + '</div>' +
        '<div class="tw-prog-label">' + esc(stageName(stage)) + '</div>' +
        '</div>';

      if (i < stageLabels.length - 1) {
        var lineClass = 'tw-prog-line';
        if (i < currentIdx) lineClass += ' completed';
        html += '<div class="' + lineClass + '"></div>';
      }
    });
    bar.innerHTML = html;

    if (meta) {
      var visited = (task.stages_visited || []).length;
      var pct = visited > 0 ? ((visited / 8) * 100).toFixed(0) : '0';
      meta.innerHTML =
        '<span class="tw-prog-badge">' + esc(stageName(task.current_stage)) + '</span>' +
        '<span>' + pct + '% (' + visited + '/8 stages)</span>' +
        (task.task_number ? '<span>#' + task.task_number + '</span>' : '') +
        '<span>' + shortDate(task.started_at) + '</span>';
    }
  }

  // ── View Management ──
  function hideAllViews() {
    Object.keys(views).forEach(function (k) {
      if (views[k]) views[k].style.display = 'none';
    });
  }

  function showView(name) {
    hideAllViews();
    if (views[name]) views[name].style.display = '';
  }

  function renderCurrentView() {
    var view = viewSelect.value;
    showView(view);
    if (view === 'dashboard') renderDashboard();
    else if (view === 'detail') renderDetail();
    else if (view === 'validation') renderValidation();
  }

  function stat(value, label) {
    return '<div class="tw-stat"><div class="tw-stat-value">' + value +
           '</div><div class="tw-stat-label">' + esc(label) + '</div></div>';
  }

  // ── VIEW: Detail ──
  function renderDetail() {
    if (!selectedTask) return;
    var task = selectedTask;

    document.getElementById('tw-title').textContent = task.title || 'Untitled';
    document.getElementById('tw-current-stage').textContent = task.current_stage;
    document.getElementById('tw-task-badge').textContent = task.task_number ? '#' + task.task_number : '';
    document.getElementById('tw-task-badge').style.display = task.task_number ? '' : 'none';
    document.getElementById('tw-date').textContent = shortDate(task.started_at);
    document.getElementById('tw-branch').textContent = task.branch || '';
    document.getElementById('tw-description').textContent = task.description || '';

    // Stats
    var statsGrid = document.getElementById('tw-detail-stats');
    statsGrid.innerHTML =
      stat(task.stage_count || 0, t.stagesVisited) +
      stat(task.total_transitions || 0, t.transitions) +
      stat(Object.keys(task.validation_summary || {}).length, t.validations) +
      stat((task.unit_test_summary || {}).total || 0, t.unitTests);

    // Timeline hidden — top progression bar already shows stage progress
    var timelineSection = document.getElementById('tw-section-timeline');
    if (timelineSection) timelineSection.style.display = 'none';

    // Stage History
    var histBody = document.getElementById('tw-history-body');
    histBody.innerHTML = '';
    (task.stage_history || []).forEach(function (entry, i) {
      var tr = document.createElement('tr');
      tr.innerHTML =
        '<td>' + (i + 1) + '</td>' +
        '<td><span class="tw-badge tw-badge-stage">' + esc(stageName(entry.stage)) + '</span></td>' +
        '<td>' + esc(entry.direction || '—') + '</td>' +
        '<td>' + esc(entry.reason || '—') + '</td>' +
        '<td>' + shortTime(entry.entered_at) + '</td>' +
        '<td>' + durationStr(entry.entered_at, entry.exited_at) + '</td>';
      histBody.appendChild(tr);
    });

    // Step History
    var stepSection = document.getElementById('tw-section-steps');
    var stepBody = document.getElementById('tw-steps-body');
    var steps = task.step_history || [];
    if (steps.length) {
      stepSection.style.display = '';
      stepBody.innerHTML = '';
      steps.forEach(function (entry, i) {
        var tr = document.createElement('tr');
        tr.innerHTML =
          '<td>' + (i + 1) + '</td>' +
          '<td>' + esc(stageName(entry.stage)) + '</td>' +
          '<td>' + esc(entry.step) + '</td>' +
          '<td>' + shortTime(entry.entered_at) + '</td>' +
          '<td>' + durationStr(entry.entered_at, entry.exited_at) + '</td>';
        stepBody.appendChild(tr);
      });
    } else {
      stepSection.style.display = 'none';
    }
  }

  function renderTimeline(task) {
    var container = document.getElementById('tw-timeline');
    container.innerHTML = '';
    var currentIdx = task.current_stage_index || 0;

    stageLabels.forEach(function (stage, i) {
      var node = document.createElement('div');
      node.className = 'tw-timeline-node';

      var dot = document.createElement('div');
      dot.className = 'tw-timeline-dot';
      if (i < currentIdx) {
        dot.className += ' completed';
        dot.innerHTML = '&#x2713;';
      } else if (i === currentIdx) {
        dot.className += ' current';
        dot.textContent = (i + 1);
      } else {
        dot.className += ' pending';
        dot.textContent = (i + 1);
      }

      var vs = (task.validation_summary || {})[stage];
      if (vs && vs.skipped) dot.className = 'tw-timeline-dot skipped';

      var label = document.createElement('div');
      label.className = 'tw-timeline-label';
      label.textContent = stageName(stage);

      node.appendChild(dot);
      node.appendChild(label);
      container.appendChild(node);

      if (i < stageLabels.length - 1) {
        var conn = document.createElement('div');
        conn.className = 'tw-timeline-connector';
        if (i < currentIdx) conn.className += ' completed';
        container.appendChild(conn);
      }
    });
  }

  // ── VIEW: Validation ──
  function renderValidation() {
    if (!selectedTask) return;
    var task = selectedTask;
    var vr = task.validation_results || {};
    var vs = task.validation_summary || {};

    var grid = document.getElementById('tw-validation-grid');
    grid.innerHTML = '';
    stageLabels.forEach(function (stage) {
      var sv = vs[stage];
      var card = document.createElement('div');
      card.className = 'tw-validation-card';
      card.onclick = function () { renderChecksForStage(stage); };

      var status = sv ? sv.status : 'pending';
      var checks = sv ? sv.total_checks : 0;
      var passed = sv ? sv.passed : 0;
      var pct = checks > 0 ? Math.round(passed / checks * 100) : 0;
      var barColor = status === 'passed' ? 'var(--tw-success)' :
                     status === 'failed' ? 'var(--tw-danger)' :
                     status === 'skipped' ? 'var(--tw-warning)' : 'var(--tw-border)';

      card.innerHTML =
        '<div class="tw-validation-card-title">' + esc(stageName(stage)) + '</div>' +
        '<div class="tw-validation-card-status">' + resultIcon(status) + ' ' + esc(status) +
        (checks ? ' — ' + passed + '/' + checks + ' ' + t.checks : '') + '</div>' +
        '<div class="tw-validation-card-bar"><div class="tw-validation-card-bar-fill" style="width:' +
        pct + '%;background:' + barColor + ';"></div></div>';

      grid.appendChild(card);
    });

    // Checks table
    var checksSection = document.getElementById('tw-section-checks');
    var checksBody = document.getElementById('tw-checks-body');
    checksBody.innerHTML = '';
    var hasChecks = false;
    Object.keys(vr).forEach(function (stage) {
      var checks = (vr[stage] || {}).checks || [];
      checks.forEach(function (c) {
        hasChecks = true;
        var tr = document.createElement('tr');
        tr.innerHTML =
          '<td>' + esc(stageName(stage)) + '</td>' +
          '<td>' + esc(c.check_id) + '</td>' +
          '<td>' + resultIcon(c.result) + ' ' + esc(c.result) + '</td>' +
          '<td>' + shortTime(c.recorded_at) + '</td>';
        checksBody.appendChild(tr);
      });
    });
    checksSection.style.display = hasChecks ? '' : 'none';

    // Unit tests table
    var testsSection = document.getElementById('tw-section-tests');
    var testsBody = document.getElementById('tw-tests-body');
    var tests = task.unit_tests || [];
    testsBody.innerHTML = '';
    tests.forEach(function (test) {
      var tr = document.createElement('tr');
      tr.innerHTML =
        '<td>' + esc(test.id) + '</td>' +
        '<td>' + esc(test.stage) + '</td>' +
        '<td>' + esc(test.description) + '</td>' +
        '<td>' + esc(test.source) + '</td>' +
        '<td>' + resultIcon(test.result) + ' ' + esc(test.result || 'pending') + '</td>';
      testsBody.appendChild(tr);
    });
    testsSection.style.display = tests.length ? '' : 'none';
  }

  function renderChecksForStage(stage) {
    var checksSection = document.getElementById('tw-section-checks');
    if (checksSection) checksSection.scrollIntoView({ behavior: 'smooth' });
  }

  // ── VIEW: Dashboard — Knowledge grid + Metrics + Time ──
  var chartTime = null;
  var chartProportions = null;

  function fmtSec(secs) {
    if (!secs || secs <= 0) return '—';
    var h = Math.floor(secs / 3600);
    var m = Math.floor((secs % 3600) / 60);
    if (h > 0) return h + 'h ' + (m < 10 ? '0' : '') + m + 'm';
    return m + 'm';
  }

  function renderDashboard() {
    if (!selectedTask) return;
    var task = selectedTask;

    // ── Dashboard stats ──
    var statsEl = document.getElementById('tw-dashboard-stats');
    if (statsEl) {
      var mc = task.metrics_compilation || {};
      var tc = task.time_compilation || {};
      var visited = (task.current_stage_index || 0) + 1;
      var pct = ((visited / 8) * 100).toFixed(0);
      statsEl.innerHTML =
        '<div class="tw-stat-card"><div class="tw-stat-value">' + esc(stageName(task.current_stage)) + '</div><div class="tw-stat-label">' + t.stage + '</div></div>' +
        '<div class="tw-stat-card"><div class="tw-stat-value">' + pct + '%</div><div class="tw-stat-label">' + t.progress + '</div></div>' +
        '<div class="tw-stat-card"><div class="tw-stat-value">' + (task.message_count || 0) + '</div><div class="tw-stat-label">' + (lang === 'fr' ? 'Messages' : 'Messages') + '</div></div>' +
        '<div class="tw-stat-card"><div class="tw-stat-value">' + (mc.prs || (task.task_number ? '#' + task.task_number : '—')) + '</div><div class="tw-stat-label">' + (mc.prs ? t.prs : 'Task') + '</div></div>';
    }

    // ── Knowledge Grid ──
    var gridEl = document.getElementById('tw-knowledge-grid');
    if (gridEl) {
      var kg = task.knowledge_grid;
      if (kg && kg.resultats && Object.keys(kg.resultats).length > 0) {
        var resultats = kg.resultats;
        var kgLabels = kg.labels || {};
        var knowledgeNames = Object.keys(resultats);
        // Find max columns across all knowledge sections
        var maxCols = 0;
        knowledgeNames.forEach(function (name) {
          var count = Object.keys(resultats[name]).length;
          if (count > maxCols) maxCols = count;
        });
        var html = '';
        knowledgeNames.forEach(function (name) {
          var vals = resultats[name];
          var keys = Object.keys(vals).sort();
          // Header row with question labels (bilingual) instead of IDs
          html += '<div class="tw-kg-label tw-kg-section-label">' + esc(name) + '</div>';
          for (var h = 0; h < maxCols; h++) {
            var hKey = keys[h];
            var headerText = hKey || '';
            if (hKey && kgLabels[hKey]) {
              headerText = kgLabels[hKey][lang] || kgLabels[hKey].fr || hKey;
            }
            html += '<div class="tw-kg-header">' + esc(headerText) + '</div>';
          }
          // Value row
          html += '<div class="tw-kg-label"></div>';
          for (var i = 0; i < maxCols; i++) {
            var key = keys[i];
            var val = key ? vals[key] : '';
            var cls = 'tw-kg-cell';
            if (val === 'Vrai' || val === 'True') cls += ' kg-vrai';
            else if (val === 'Faux' || val === 'False') cls += ' kg-faux';
            else if (val === 'Passer' || val === 'Skip') cls += ' kg-passer';
            else if (val === '--') cls += ' kg-pending';
            html += '<div class="' + cls + '">' + esc(val || '') + '</div>';
          }
        });
        if (kg.synthesized) {
          html += '<div class="tw-kg-synth-note" style="grid-column:1/-1;text-align:right;font-size:0.75rem;opacity:0.6;margin-top:4px;">' +
            (lang === 'fr' ? 'Grille reconstituée depuis les données disponibles' : 'Grid reconstructed from available data') + '</div>';
        }
        gridEl.innerHTML = html;
        gridEl.style.gridTemplateColumns = 'auto repeat(' + maxCols + ', 1fr)';
      } else {
        gridEl.innerHTML = '<p class="tw-muted">' + t.noData + '</p>';
      }
    }

    // ── Metrics stats ──
    var metricsEl = document.getElementById('tw-metrics-stats');
    if (metricsEl) {
      var mc = task.metrics_compilation;
      if (mc) {
        metricsEl.innerHTML =
          '<div class="tw-stat-card"><div class="tw-stat-value">' + (mc.prs || 0) + '</div><div class="tw-stat-label">' + t.prs + '</div></div>' +
          '<div class="tw-stat-card"><div class="tw-stat-value">' + (mc.pr_numbers || []).join(', ') + '</div><div class="tw-stat-label">PR #</div></div>' +
          '<div class="tw-stat-card"><div class="tw-stat-value">' + (mc.files_changed || 0) + '</div><div class="tw-stat-label">' + t.filesChanged + '</div></div>' +
          '<div class="tw-stat-card"><div class="tw-stat-value">+' + (mc.additions || 0) + ' / -' + (mc.deletions || 0) + '</div><div class="tw-stat-label">' + t.linesChanged + '</div></div>';
      } else {
        metricsEl.innerHTML = '<p class="tw-muted">' + t.noData + '</p>';
      }
    }

    // ── Time stats ──
    var timeStatsEl = document.getElementById('tw-time-stats');
    if (timeStatsEl) {
      var tc = task.time_compilation;
      if (tc) {
        timeStatsEl.innerHTML =
          '<div class="tw-stat-card"><div class="tw-stat-value">' + fmtSec(tc.calendar_seconds) + '</div><div class="tw-stat-label">' + t.calendarTime + '</div></div>' +
          '<div class="tw-stat-card"><div class="tw-stat-value">' + fmtSec(tc.active_seconds) + '</div><div class="tw-stat-label">' + t.activeTime + '</div></div>' +
          '<div class="tw-stat-card"><div class="tw-stat-value">' + fmtSec(tc.inactive_seconds) + '</div><div class="tw-stat-label">' + t.inactiveTime + '</div></div>' +
          '<div class="tw-stat-card"><div class="tw-stat-value">' + ((tc.stage_durations || []).length) + '</div><div class="tw-stat-label">' + t.blocks + '</div></div>';
      } else {
        timeStatsEl.innerHTML = '<p class="tw-muted">' + t.noData + '</p>';
      }
    }

    // ── Stage Duration table ──
    var durBody = document.getElementById('tw-stage-duration-body');
    if (durBody) {
      var tc = task.time_compilation;
      if (tc && tc.stage_durations && tc.stage_durations.length > 0) {
        var totalActive = tc.active_seconds || 1;
        durBody.innerHTML = tc.stage_durations.map(function (sd) {
          var pct = totalActive > 0 ? Math.round((sd.duration_seconds / totalActive) * 100) : 0;
          return '<tr><td><span class="tw-badge tw-badge-stage">' + esc(stageName(sd.stage)) + '</span></td>' +
            '<td>' + fmtSec(sd.duration_seconds) + '</td>' +
            '<td>' + pct + '%</td></tr>';
        }).join('');
      } else {
        durBody.innerHTML = '<tr><td colspan="3" class="tw-muted">' + t.noData + '</td></tr>';
      }
    }

    // ── Time Bar Chart (stage durations) ──
    var timeCanvas = document.getElementById('tw-chart-time');
    if (timeCanvas && typeof Chart !== 'undefined') {
      var tc = task.time_compilation;
      if (tc && tc.stage_durations && tc.stage_durations.length > 0) {
        if (chartTime) chartTime.destroy();
        var sc = getStageColors();
        var labels = tc.stage_durations.map(function (d) { return d.stage; });
        var data = tc.stage_durations.map(function (d) { return Math.round(d.duration_seconds / 60); });
        var colors = labels.map(function (s) { return sc[s] || '#999'; });
        chartTime = new Chart(timeCanvas, {
          type: 'bar',
          data: {
            labels: labels,
            datasets: [{ label: t.duration + ' (min)', data: data, backgroundColor: colors }]
          },
          options: { responsive: true, plugins: { title: { display: true, text: t.stageDuration } } }
        });
      }
    }

    // ── Time Proportions Doughnut (active/inactive) ──
    var propCanvas = document.getElementById('tw-chart-proportions');
    if (propCanvas && typeof Chart !== 'undefined') {
      var tc = task.time_compilation;
      if (tc && tc.calendar_seconds > 0) {
        if (chartProportions) chartProportions.destroy();
        var dark = isDarkTheme();
        chartProportions = new Chart(propCanvas, {
          type: 'doughnut',
          data: {
            labels: [t.activeTime, t.inactiveTime],
            datasets: [{
              data: [Math.round(tc.active_seconds / 60), Math.round(tc.inactive_seconds / 60)],
              backgroundColor: dark ? ['#3fb950', '#484f58'] : ['#28a745', '#e1e4e8']
            }]
          },
          options: { responsive: true, plugins: { title: { display: true, text: t.proportions } } }
        });
      }
    }
  }

  // ── Overview rendering (All Tasks) ──
  function renderTaskOverview() {
    if (!overviewEl || !allTasks.length) return;

    // Aggregate stats
    var totalTasks = allTasks.length;
    var totalCompleted = 0;
    var totalPRs = 0;
    var totalAdds = 0;
    var totalDels = 0;
    var stageDist = {};
    stageLabels.forEach(function(s) { stageDist[s] = 0; });

    allTasks.forEach(function(tk) {
      var mc = tk.metrics_compilation || {};
      totalPRs += mc.prs || 0;
      totalAdds += mc.additions || 0;
      totalDels += mc.deletions || 0;
      if (tk.current_stage === 'completion') totalCompleted++;
      if (tk.current_stage && stageDist.hasOwnProperty(tk.current_stage)) {
        stageDist[tk.current_stage]++;
      }
    });

    var avgProgress = 0;
    allTasks.forEach(function(tk) {
      var visited = (tk.current_stage_index || 0) + 1;
      avgProgress += (visited / 8) * 100;
    });
    avgProgress = totalTasks > 0 ? Math.round(avgProgress / totalTasks) : 0;

    // Stats
    var statsEl = document.getElementById('tw-overview-stats');
    if (statsEl) {
      statsEl.innerHTML =
        '<div class="tw-stat-card"><div class="tw-stat-value">' + totalTasks + '</div><div class="tw-stat-label">' + (lang === 'fr' ? 'T\u00e2ches' : 'Tasks') + '</div></div>' +
        '<div class="tw-stat-card"><div class="tw-stat-value">' + totalCompleted + '</div><div class="tw-stat-label">' + (lang === 'fr' ? 'Termin\u00e9es' : 'Completed') + '</div></div>' +
        '<div class="tw-stat-card"><div class="tw-stat-value">' + totalPRs + '</div><div class="tw-stat-label">' + t.prs + '</div></div>' +
        '<div class="tw-stat-card"><div class="tw-stat-value">+' + totalAdds.toLocaleString() + '</div><div class="tw-stat-label">' + t.additions + '</div></div>' +
        '<div class="tw-stat-card"><div class="tw-stat-value">' + avgProgress + '%</div><div class="tw-stat-label">' + t.progress + '</div></div>';
    }

    // Stage distribution bar
    var barEl = document.getElementById('tw-overview-stage-bar');
    var legendEl = document.getElementById('tw-overview-stage-legend');
    if (barEl) {
      var sc = getStageColors();
      var barHtml = '';
      var legendHtml = '';
      stageLabels.forEach(function(stage) {
        var count = stageDist[stage] || 0;
        if (count === 0) return;
        var pct = (count / totalTasks * 100).toFixed(1);
        barHtml += '<div style="width:' + pct + '%;background:' + sc[stage] + ';display:flex;align-items:center;justify-content:center;font-size:0.65rem;font-weight:600;color:#fff;min-width:2px;">';
        if (parseFloat(pct) > 10) barHtml += count;
        barHtml += '</div>';
        legendHtml += '<span style="margin-right:1rem;font-size:0.8rem;">';
        legendHtml += '<span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:' + sc[stage] + ';margin-right:3px;"></span>';
        legendHtml += stageName(stage) + ' (' + count + ')';
        legendHtml += '</span>';
      });
      barEl.innerHTML = barHtml;
      if (legendEl) legendEl.innerHTML = legendHtml;
    }

    // Task cards
    var cardsEl = document.getElementById('tw-task-cards');
    if (!cardsEl) return;

    var sorted = allTasks.slice().sort(function(a, b) {
      var da = a.started_at || a.updated_at || '';
      var db = b.started_at || b.updated_at || '';
      return db.localeCompare(da);
    });

    var html = '';
    sorted.forEach(function(tk) {
      var title = esc(tk.title || 'Untitled');
      if (title.length > 60) title = title.substring(0, 57) + '...';
      var date = shortDate(tk.started_at || tk.updated_at || '');
      var taskTag = tk.task_number ? '#' + tk.task_number + ' ' : '';
      var visited = (tk.current_stage_index || 0) + 1;
      var pct = ((visited / 8) * 100).toFixed(0);
      var mc = tk.metrics_compilation || {};

      html += '<div class="tw-card" data-task-id="' + esc(tk.id) + '">';
      html += '<div class="tw-card-title">' + taskTag + title + '</div>';
      html += '<div class="tw-card-meta">';
      html += '<span class="tw-badge tw-badge-stage">' + esc(stageName(tk.current_stage)) + '</span>';
      html += '<span>' + date + '</span>';
      html += '<span>' + pct + '%</span>';
      html += '<span>+' + (mc.additions || 0) + '/-' + (mc.deletions || 0) + '</span>';
      html += '</div>';
      html += '<div class="tw-card-progress"><div class="tw-card-progress-fill" style="width:' + pct + '%;"></div></div>';
      html += '</div>';
    });
    cardsEl.innerHTML = html;

    // Click handlers on cards
    cardsEl.querySelectorAll('.tw-card').forEach(function(card) {
      card.addEventListener('click', function() {
        var id = card.getAttribute('data-task-id');
        taskSelect.value = id;
        selectTask(id);
      });
    });
  }

  // ── Event Listeners ──
  taskSelect.addEventListener('change', function () {
    selectTask(this.value);
  });

  viewSelect.addEventListener('change', function () {
    renderCurrentView();
  });


  // ── Init ──
  loadData();

})();
