/* ═══════════════════════════════════════════════════════════════
   Project Viewer (I4) — JavaScript
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var lang = (window.location.pathname.indexOf('/fr/') !== -1) ? 'fr' : 'en';

  var L = {
    en: {
      projects: 'Projects', tasks: 'Tasks', prs: 'PRs',
      additions: 'Additions', deletions: 'Deletions', filesChanged: 'Files Changed',
      completion: 'Completion', gridScore: 'Grid Score',
      noData: 'No data available.', selectProject: 'Select a project to view details.',
      projectsAvailable: 'projects available.',
      taskCount: 'Tasks', completedTasks: 'Completed', branches: 'Branches',
      stage: 'Stage', progress: 'Progress', issue: 'Issue', title: 'Title',
      viewTask: 'View', stageDistribution: 'Stage Distribution',
      gridSummary: 'Knowledge Grid Summary', metrics: 'Metrics',
      projectTasks: 'Project Tasks', board: 'Board', overview: 'Overview',
      allProjects: 'All Projects', dashboard: 'Dashboard', detail: 'Detail',
      started: 'Started', updated: 'Updated',
    },
    fr: {
      projects: 'Projets', tasks: 'Tâches', prs: 'PRs',
      additions: 'Ajouts', deletions: 'Suppressions', filesChanged: 'Fichiers modifiés',
      completion: 'Complétion', gridScore: 'Score grille',
      noData: 'Aucune donnée disponible.', selectProject: 'Sélectionnez un projet pour voir les détails.',
      projectsAvailable: 'projets disponibles.',
      taskCount: 'Tâches', completedTasks: 'Complétées', branches: 'Branches',
      stage: 'Étape', progress: 'Progrès', issue: 'Issue', title: 'Titre',
      viewTask: 'Voir', stageDistribution: 'Distribution des étapes',
      gridSummary: 'Résumé grille Knowledge', metrics: 'Métriques',
      projectTasks: 'Tâches du projet', board: 'Board', overview: 'Vue d\'ensemble',
      allProjects: 'Tous les projets', dashboard: 'Tableau de bord', detail: 'Détail',
      started: 'Début', updated: 'Mis à jour',
    }
  };
  var t = L[lang] || L.en;

  var stageLabels = {
    en: { initial: 'Initial', plan: 'Plan', analyze: 'Analyze', implement: 'Implement',
          validation: 'Validation', documentation: 'Documentation', approval: 'Approval', completion: 'Completion' },
    fr: { initial: 'Initial', plan: 'Plan', analyze: 'Analyse', implement: 'Implémentation',
          validation: 'Validation', documentation: 'Documentation', approval: 'Approbation', completion: 'Complétion' }
  };
  var sL = stageLabels[lang] || stageLabels.en;

  var stageColors = {
    initial: '#8b949e', plan: '#bf8700', analyze: '#0969da', implement: '#8250df',
    validation: '#cf222e', documentation: '#0550ae', approval: '#1a7f37', completion: '#2da44e'
  };

  var stageOrder = ['initial', 'plan', 'analyze', 'implement', 'validation', 'documentation', 'approval', 'completion'];

  var allData = null;
  var currentProject = null;

  function esc(s) {
    var d = document.createElement('div');
    d.textContent = s || '';
    return d.innerHTML;
  }

  function fmtDate(iso) {
    if (!iso) return '--';
    try { return new Date(iso).toLocaleDateString(lang === 'fr' ? 'fr-CA' : 'en-CA'); }
    catch (e) { return iso.substring(0, 10); }
  }

  // ── Data Loading ──
  function loadData() {
    var base = document.getElementById('pv-viewer');
    var baseUrl = (base && base.dataset.baseurl) || '';
    var url = baseUrl + '/data/projects.json';

    fetch(url).then(function (r) { return r.json(); }).then(function (data) {
      allData = data;
      populateSelect(data.projects);
      renderOverview(data);
      updateCoverPage(data);
    }).catch(function (err) {
      console.error('Failed to load projects.json:', err);
    });
  }

  function populateSelect(projects) {
    var sel = document.getElementById('pv-project-select');
    if (!sel) return;
    sel.innerHTML = '<option value="">\u2014 ' + t.allProjects + ' \u2014</option>';
    projects.forEach(function (p) {
      var opt = document.createElement('option');
      opt.value = p.id;
      var label = p.title;
      if (p.task_count > 0) label += ' (' + p.task_count + ' ' + t.tasks.toLowerCase() + ')';
      opt.textContent = label;
      sel.appendChild(opt);
    });
  }

  // ── Cover page (print) ──
  function updateCoverPage(data, project) {
    var titleEl = document.getElementById('pv-cover-title');
    var descEl = document.getElementById('pv-cover-desc');
    var metaEl = document.getElementById('pv-cover-meta');
    if (!titleEl) return;

    if (project) {
      titleEl.textContent = project.title;
      descEl.textContent = project.task_count + ' ' + t.tasks.toLowerCase() + ' — ' +
        project.completion_pct + '% ' + t.completion.toLowerCase();
      var lines = [];
      if (project.board_url) lines.push('Board: #' + project.board_number);
      if (project.metrics) lines.push(t.prs + ': ' + project.metrics.prs + ' — +' +
        project.metrics.additions.toLocaleString() + '/-' + project.metrics.deletions.toLocaleString());
      lines.push(t.completion + ': ' + project.completion_pct + '%');
      lines.push('Generated: ' + new Date().toLocaleDateString());
      metaEl.innerHTML = lines.join('<br>');
    } else {
      titleEl.textContent = lang === 'fr' ? 'Visualiseur de projets' : 'Project Viewer';
      var totalTk = 0;
      data.projects.forEach(function(p) { totalTk += p.task_count || 0; });
      descEl.textContent = data.meta.total_projects + ' ' + t.projects.toLowerCase() + ' — ' +
        totalTk + ' ' + t.tasks.toLowerCase();
      metaEl.innerHTML = 'Generated: ' + new Date().toLocaleDateString();
    }
  }

  // ── Overview (all projects cards) ──
  function renderOverview(data) {
    hideViews();
    var el = document.getElementById('pv-view-overview');
    if (!el) return;
    el.style.display = 'block';

    // Stats
    var statsEl = document.getElementById('pv-overview-stats');
    if (statsEl) {
      var totalTasks = 0;
      var totalPrs = 0;
      var totalAdds = 0;
      data.projects.forEach(function (p) {
        totalTasks += p.task_count || 0;
        totalPrs += (p.metrics || {}).prs || 0;
        totalAdds += (p.metrics || {}).additions || 0;
      });
      statsEl.innerHTML =
        '<div class="pv-stat-card"><div class="pv-stat-value">' + data.meta.total_projects + '</div><div class="pv-stat-label">' + t.projects + '</div></div>' +
        '<div class="pv-stat-card"><div class="pv-stat-value">' + totalTasks + '</div><div class="pv-stat-label">' + t.tasks + '</div></div>' +
        '<div class="pv-stat-card"><div class="pv-stat-value">' + totalPrs + '</div><div class="pv-stat-label">' + t.prs + '</div></div>' +
        '<div class="pv-stat-card"><div class="pv-stat-value">+' + totalAdds.toLocaleString() + '</div><div class="pv-stat-label">' + t.additions + '</div></div>';
    }

    // Cards
    var cardsEl = document.getElementById('pv-project-cards');
    if (!cardsEl) return;
    var html = '';
    data.projects.forEach(function (p) {
      var completionCls = p.completion_pct >= 80 ? 'pv-green' : (p.completion_pct >= 40 ? 'pv-yellow' : 'pv-blue');
      var boardLink = p.board_url ? ' <a href="' + esc(p.board_url) + '" class="pv-link" target="_blank">' + t.board + '</a>' : '';
      html += '<div class="pv-card" data-project-id="' + esc(p.id) + '">';
      html += '<div class="pv-card-title">' + esc(p.title) + '</div>';
      html += '<div class="pv-card-meta">';
      html += '<span>' + p.task_count + ' ' + t.tasks.toLowerCase() + '</span>';
      html += '<span>' + ((p.metrics || {}).prs || 0) + ' ' + t.prs + '</span>';
      html += '<span>' + (p.completion_pct || 0) + '% ' + t.completion.toLowerCase() + '</span>';
      html += boardLink;
      html += '</div>';
      html += '<div class="pv-progress-bar"><div class="pv-progress-fill ' + completionCls + '" style="width:' + p.completion_pct + '%"></div></div>';
      html += '<div class="pv-muted">' + t.completion + ': ' + p.completion_pct + '% (' + p.completed_tasks + '/' + p.task_count + ')</div>';
      html += '</div>';
    });
    cardsEl.innerHTML = html;

    // Click handlers on cards
    cardsEl.querySelectorAll('.pv-card').forEach(function (card) {
      card.addEventListener('click', function () {
        var id = card.dataset.projectId;
        var sel = document.getElementById('pv-project-select');
        if (sel) sel.value = id;
        showProject(id);
      });
    });

    document.getElementById('pv-empty-state').style.display = 'none';
  }

  // ── Project Detail ──
  function showProject(projectId) {
    if (!allData) return;
    currentProject = null;
    for (var i = 0; i < allData.projects.length; i++) {
      if (allData.projects[i].id === projectId) {
        currentProject = allData.projects[i];
        break;
      }
    }
    if (!currentProject) {
      renderOverview(allData);
      updateCoverPage(allData);
      return;
    }
    renderDashboard(currentProject);
    updateCoverPage(allData, currentProject);
  }

  function renderDashboard(p) {
    hideViews();
    var el = document.getElementById('pv-view-dashboard');
    if (!el) return;
    el.style.display = 'block';
    document.getElementById('pv-empty-state').style.display = 'none';

    // Title
    var titleEl = document.getElementById('pv-project-title');
    if (titleEl) titleEl.textContent = p.title;

    // Meta
    var metaEl = document.getElementById('pv-project-meta');
    if (metaEl) {
      var metaHtml = '';
      if (p.board_url) metaHtml += '<a href="' + esc(p.board_url) + '" class="pv-link" target="_blank">GitHub Board #' + p.board_number + '</a> ';
      if (p.issue_url) metaHtml += '<a href="' + esc(p.issue_url) + '" class="pv-link" target="_blank">Issue #' + p.issue_number + '</a> ';
      metaHtml += '<span class="pv-muted">' + p.branches.length + ' ' + t.branches.toLowerCase() + '</span>';
      metaEl.innerHTML = metaHtml;
    }

    // Stats
    var statsEl = document.getElementById('pv-dashboard-stats');
    if (statsEl) {
      var m = p.metrics || {};
      statsEl.innerHTML =
        '<div class="pv-stat-card"><div class="pv-stat-value">' + p.task_count + '</div><div class="pv-stat-label">' + t.taskCount + '</div></div>' +
        '<div class="pv-stat-card"><div class="pv-stat-value">' + p.completed_tasks + '</div><div class="pv-stat-label">' + t.completedTasks + '</div></div>' +
        '<div class="pv-stat-card"><div class="pv-stat-value">' + (m.prs || 0) + '</div><div class="pv-stat-label">' + t.prs + '</div></div>' +
        '<div class="pv-stat-card"><div class="pv-stat-value">+' + (m.additions || 0).toLocaleString() + '</div><div class="pv-stat-label">' + t.additions + '</div></div>' +
        '<div class="pv-stat-card"><div class="pv-stat-value">-' + (m.deletions || 0).toLocaleString() + '</div><div class="pv-stat-label">' + t.deletions + '</div></div>' +
        '<div class="pv-stat-card"><div class="pv-stat-value">' + (m.files_changed || 0) + '</div><div class="pv-stat-label">' + t.filesChanged + '</div></div>';
    }

    // Completion bar
    var compEl = document.getElementById('pv-completion-bar');
    if (compEl) {
      var cls = p.completion_pct >= 80 ? 'pv-green' : (p.completion_pct >= 40 ? 'pv-yellow' : 'pv-blue');
      compEl.innerHTML =
        '<div class="pv-progress-bar"><div class="pv-progress-fill ' + cls + '" style="width:' + p.completion_pct + '%"></div></div>' +
        '<div class="pv-muted">' + t.completion + ': ' + p.completion_pct + '%</div>';
    }

    // Stage distribution bar
    renderStageBar(p);

    // Grid summary
    renderGridSummary(p);

    // Tasks table
    renderTasksTable(p);
  }

  function renderStageBar(p) {
    var el = document.getElementById('pv-stage-bar');
    if (!el || !p.stage_distribution) return;
    var total = p.task_count || 1;
    var html = '';
    var allStages = ['initial', 'plan', 'analyze', 'implement', 'validation', 'documentation', 'approval', 'completion'];
    allStages.forEach(function (stage) {
      var count = p.stage_distribution[stage] || 0;
      if (count === 0) return;
      var pct = (count / total * 100).toFixed(1);
      html += '<div class="pv-stage-segment" style="width:' + pct + '%;background:' + stageColors[stage] + '" title="' + sL[stage] + ': ' + count + '">';
      if (pct > 10) html += count;
      html += '</div>';
    });
    el.innerHTML = html || '<div class="pv-muted">' + t.noData + '</div>';

    // Legend
    var legendEl = document.getElementById('pv-stage-legend');
    if (legendEl) {
      var lhtml = '';
      allStages.forEach(function (stage) {
        var count = p.stage_distribution[stage] || 0;
        if (count === 0) return;
        lhtml += '<span style="margin-right:1rem;font-size:0.8rem;">';
        lhtml += '<span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:' + stageColors[stage] + ';margin-right:3px;"></span>';
        lhtml += sL[stage] + ' (' + count + ')';
        lhtml += '</span>';
      });
      legendEl.innerHTML = lhtml;
    }
  }

  function renderGridSummary(p) {
    var el = document.getElementById('pv-grid-summary');
    if (!el) return;
    var gs = p.grid_summary;
    if (!gs || Object.keys(gs).length === 0) {
      el.innerHTML = '<p class="pv-muted">' + t.noData + '</p>';
      return;
    }

    var sectionNames = Object.keys(gs);
    var maxCols = 0;
    sectionNames.forEach(function (name) {
      var count = Object.keys(gs[name]).length;
      if (count > maxCols) maxCols = count;
    });

    var html = '';
    sectionNames.forEach(function (name) {
      var cells = gs[name];
      var keys = Object.keys(cells).sort();
      // Section label
      html += '<div class="pv-gs-label pv-gs-section-label">' + esc(name) + '</div>';
      for (var h = 0; h < maxCols; h++) {
        html += '<div class="pv-gs-label">' + esc(keys[h] || '') + '</div>';
      }
      // Values row
      html += '<div class="pv-gs-label"></div>';
      for (var i = 0; i < maxCols; i++) {
        var key = keys[i];
        if (!key || !cells[key]) {
          html += '<div class="pv-gs-cell gs-low">--</div>';
          continue;
        }
        var cell = cells[key];
        var pct = cell.pct_vrai || 0;
        var cls = pct >= 75 ? 'gs-high' : (pct >= 25 ? 'gs-mid' : 'gs-low');
        html += '<div class="pv-gs-cell ' + cls + '">' + pct + '%</div>';
      }
    });

    el.innerHTML = html;
    el.style.gridTemplateColumns = 'auto repeat(' + maxCols + ', 1fr)';
    el.style.display = 'grid';

    // Grid score
    var scoreEl = document.getElementById('pv-grid-score');
    if (scoreEl) scoreEl.textContent = t.completion + ': ' + (p.completion_pct || 0) + '%';
  }

  function renderTasksTable(p) {
    var tbody = document.getElementById('pv-tasks-body');
    if (!tbody) return;
    var tasks = p.tasks || [];
    if (!tasks.length) {
      tbody.innerHTML = '<tr><td colspan="7" class="pv-muted">' + t.noData + '</td></tr>';
      return;
    }

    var baseUrl = (document.getElementById('pv-viewer') || {}).dataset.baseurl || '';
    var twPath = lang === 'fr' ? '/fr/interfaces/task-workflow/' : '/interfaces/task-workflow/';

    var html = '';
    tasks.forEach(function (tk) {
      var stage = tk.current_stage || tk.stage || 'initial';
      var stageBadge = '<span class="pv-badge pv-badge-stage">' + (sL[stage] || stage) + '</span>';
      var stageIdx = tk.current_stage_index;
      if (stageIdx == null) stageIdx = stageOrder.indexOf(stage);
      if (stageIdx < 0) stageIdx = 0;
      var visited = stageIdx + 1;
      var pct = ((visited / 8) * 100).toFixed(0);
      var issueLink = tk.issue_number ? '<a href="https://github.com/packetqc/knowledge/issues/' + tk.issue_number + '" class="pv-link" target="_blank">#' + tk.issue_number + '</a>' : '--';
      var taskLink = '<a href="' + baseUrl + twPath + '?task=' + (tk.id || '') + '" class="pv-link" target="_top">' + t.viewTask + '</a>';

      html += '<tr>';
      html += '<td>' + issueLink + '</td>';
      html += '<td>' + esc(tk.title).substring(0, 60) + '</td>';
      html += '<td>' + stageBadge + '</td>';
      html += '<td><div class="pv-progress-bar"><div class="pv-progress-fill pv-blue" style="width:' + pct + '%"></div></div><span class="pv-muted">' + pct + '%</span></td>';
      html += '<td>' + (tk.children_count || 0) + ' sub</td>';
      html += '<td>' + (tk.message_count || 0) + ' msg</td>';
      html += '<td>' + taskLink + '</td>';
      html += '</tr>';
    });
    tbody.innerHTML = html;
  }

  // ── View Management ──
  function hideViews() {
    document.querySelectorAll('.pv-view').forEach(function (v) { v.style.display = 'none'; });
  }

  // ── Event Handlers ──
  function init() {
    var sel = document.getElementById('pv-project-select');
    if (sel) {
      sel.addEventListener('change', function () {
        if (sel.value) {
          showProject(sel.value);
        } else {
          currentProject = null;
          if (allData) renderOverview(allData);
        }
      });
    }

    // Update count
    var countEl = document.getElementById('pv-project-count');
    if (countEl && allData) countEl.textContent = allData.meta.total_projects;

    loadData();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
