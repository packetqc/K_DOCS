// ═══ Session Review — Render (session-render.js) ═══
// Summary, metrics, deliveries, issues, lessons, velocity sections.

(function() {
  'use strict';
  var SV = window.SV;
  if (!SV) return;
  var t = SV.t;
  var lang = SV.lang;

  // ── Section 1: Summary ──
  SV.renderSummary = function(s) {
    var eff = SV.effectiveData(s);
    var hasPRs = s.pr_count > 0;
    var hasNotes = s.has_notes;
    var hasIssue = s.has_issue;

    // Data source notice
    var noticeEl = document.getElementById('sv-notice');
    if (!hasNotes && !hasIssue) {
      noticeEl.className = 'sv-notice sv-notice-warn';
      noticeEl.innerHTML = '<strong>\u26a0\ufe0f</strong> ' + t.prOnly;
      noticeEl.style.display = '';
    } else if (!hasNotes && hasIssue) {
      noticeEl.className = 'sv-notice sv-notice-info';
      noticeEl.innerHTML = '<strong>\u2139\ufe0f</strong> ' + t.noCompilation;
      noticeEl.style.display = '';
    } else {
      noticeEl.style.display = 'none';
    }

    document.getElementById('sv-title').textContent = s.title || t.noTitle;
    document.getElementById('sv-type').textContent = s.type || '';
    document.getElementById('sv-date').textContent = s.date || '';

    var rtEl = document.getElementById('sv-request-type');
    if (s.request_type) {
      rtEl.textContent = SV.reqTypeBadge(s.request_type);
      rtEl.title = t.reqType + ': ' + s.request_type;
      rtEl.style.display = '';
    } else { rtEl.style.display = 'none'; }

    var stEl = document.getElementById('sv-eng-stage');
    if (s.engineering_stage) {
      stEl.textContent = SV.engStageBadge(s.engineering_stage);
      stEl.title = t.engStage + ': ' + s.engineering_stage;
      stEl.style.display = '';
    } else { stEl.style.display = 'none'; }

    var brEl = document.getElementById('sv-branch');
    if (s.branch) { brEl.textContent = s.branch; brEl.style.display = ''; }
    else { brEl.style.display = 'none'; }

    var badgesEl = document.getElementById('sv-source-badges');
    var badges = '';
    if (hasPRs) badges += '<span class="sv-src-badge sv-src-pr">' + t.srcPR + '</span>';
    if (hasNotes) badges += '<span class="sv-src-badge sv-src-notes">' + t.srcNotes + '</span>';
    if (hasIssue) badges += '<span class="sv-src-badge sv-src-issue">' + t.srcIssue + '</span>';
    badgesEl.innerHTML = badges;

    var sumEl = document.getElementById('sv-summary');
    sumEl.textContent = s.summary || '';
    sumEl.style.display = s.summary ? '' : 'none';

    // Stats grid
    var grid = document.getElementById('sv-stats-grid');
    grid.innerHTML = '';
    var calendarMin = SV.calcDuration(eff.firstTime, eff.lastTime);
    var calendarStr = calendarMin != null ? SV.formatDuration(calendarMin) : '\u2014';
    var activeStr = eff.active > 0 ? SV.formatDuration(eff.active) : '\u2014';
    var totalLines = eff.additions + eff.deletions;
    var linesStr = totalLines > 0 ? ('+' + eff.additions + ' \u2212' + eff.deletions) : '\u2014';
    var stats = [
      { v: eff.prCount || 0, l: t.prCount },
      { v: eff.commits > 0 ? String(eff.commits) : '\u2014', l: t.commits },
      { v: linesStr, l: t.linesChanged },
      { v: eff.files > 0 ? String(eff.files) : '\u2014', l: t.filesChanged },
      { v: activeStr, l: t.activeTime },
      { v: calendarStr, l: t.calendarTime },
      { v: (s.issues || []).length, l: t.issueCount },
      { v: (s.lessons || []).length, l: t.lessonCount }
    ];
    // v2.0: show system session count if > 1
    var sysCount = SV.systemSessionCount(s);
    if (sysCount > 1) {
      stats.push({ v: sysCount, l: t.systemSessions });
    }
    // v2.0: show collateral tasks count
    var ctCount = eff.collateralTasks.length;
    if (ctCount > 0) {
      stats.push({ v: ctCount, l: t.collateralTasks });
    }
    stats.forEach(function(c) {
      var d = document.createElement('div'); d.className = 'sv-stat-card';
      d.innerHTML = '<div class="sv-stat-value">' + c.v + '</div><div class="sv-stat-label">' + c.l + '</div>';
      grid.appendChild(d);
    });

    // v2.0: user session identity badge
    var idEl = document.getElementById('sv-user-session-id');
    if (idEl) {
      var usid = SV.userSessionId(s);
      if (usid) {
        idEl.textContent = usid;
        idEl.title = t.internalId;
        idEl.style.display = '';
      } else {
        idEl.style.display = 'none';
      }
    }
  };

  // ── Section 2: Metrics ──
  SV.renderMetrics = function(s) {
    var eff = SV.effectiveData(s);
    var mTotals = document.getElementById('sv-metrics-totals');
    var mBody = document.getElementById('sv-metrics-body');
    var pc = eff.prCount, tf = eff.files, tc = eff.commits;
    var ic = (s.issues||[]).length, lc = (s.lessons||[]).length;

    mTotals.innerHTML = '<strong>' + t.totals + ':</strong> ' + pc + ' PRs \u00b7 ' + tc + ' commits \u00b7 +' +
      eff.additions + ' \u2212' + eff.deletions + ' lines \u00b7 ' + tf + ' files' +
      (s.lines_per_hour ? ' \u00b7 <em>' + s.lines_per_hour + ' ' + t.linesPerHour + '</em>' : '') +
      (eff.agg ? ' \u00b7 <em>' + (eff.agg.children_count || 0) + ' child issues</em>' : '');

    mBody.innerHTML = '';
    var subLabels = {
      feat: { icon: '\ud83d\ude80', en: 'Feature', fr: 'Fonctionnalit\u00e9' },
      fix: { icon: '\ud83d\udd27', en: 'Fix', fr: 'Correctif' },
      doc: { icon: '\ud83d\udcdd', en: 'Documentation', fr: 'Documentation' },
      test: { icon: '\ud83e\uddea', en: 'Test / QA', fr: 'Test / QA' },
      refactor: { icon: '\u267b\ufe0f', en: 'Refactor', fr: 'Refactorisation' },
      chore: { icon: '\u2699\ufe0f', en: 'Chore', fr: 'Maintenance' }
    };
    var groups = {};
    var groupOrder = ['feat', 'fix', 'test', 'doc', 'refactor', 'chore'];
    eff.prs.forEach(function(p) {
      var st = p.sub_type || 'feat';
      if (!groups[st]) groups[st] = [];
      groups[st].push(p);
    });
    var groupIdx = 0;
    groupOrder.forEach(function(st) {
      if (!groups[st]) return;
      var prGroup = groups[st];
      groupIdx++;
      var gid = 'mg-' + groupIdx;
      var gAdd = 0, gDel = 0, gFiles = 0, gCommits = 0;
      prGroup.forEach(function(p) {
        gAdd += p.additions || 0; gDel += p.deletions || 0;
        gFiles += p.changed_files || 0; gCommits += p.commits || 0;
      });
      var info = subLabels[st] || { icon: '\u2022', en: st, fr: st };
      var gLabel = info.icon + ' ' + (lang === 'fr' ? info.fr : info.en);
      var gAddDel = (gAdd || gDel) ?
        '<span style="color:#16a34a">+' + gAdd + '</span> <span style="color:#dc2626">\u2212' + gDel + '</span>' : '\u2014';
      var ptr = document.createElement('tr');
      ptr.className = 'sv-row-parent';
      ptr.setAttribute('data-group', gid);
      ptr.innerHTML = '<td><strong>M' + groupIdx + '</strong></td><td>' + gLabel + '</td><td>' + prGroup.length + '</td><td>' + gAddDel + '</td><td>' + gFiles + '</td><td>' + gCommits + '</td><td></td><td></td>';
      ptr.addEventListener('click', function() {
        var expanded = this.classList.toggle('sv-expanded');
        var children = mBody.querySelectorAll('.sv-child-' + gid);
        for (var i = 0; i < children.length; i++) children[i].classList.toggle('sv-visible', expanded);
      });
      mBody.appendChild(ptr);
      prGroup.forEach(function(p) {
        var ctr = document.createElement('tr');
        ctr.className = 'sv-row-child sv-child-' + gid;
        var pAddDel = (p.additions || p.deletions) ?
          '<span style="color:#16a34a">+' + (p.additions || 0) + '</span> <span style="color:#dc2626">\u2212' + (p.deletions || 0) + '</span>' : '\u2014';
        ctr.innerHTML = '<td></td><td>#' + p.number + ' ' + SV.esc(p.title || '').substring(0, 50) + (p.title && p.title.length > 50 ? '\u2026' : '') +
          '</td><td></td><td>' + pAddDel + '</td><td>' + (p.changed_files || 0) + '</td><td>' + (p.commits || 0) + '</td><td></td><td></td>';
        mBody.appendChild(ctr);
      });
    });
    var addDelTotal = (s.total_additions || s.total_deletions) ?
      '<span style="color:#16a34a">+' + (s.total_additions || 0) + '</span> <span style="color:#dc2626">\u2212' + (s.total_deletions || 0) + '</span>' : '\u2014';
    var tfoot = document.createElement('tr');
    tfoot.style.fontWeight = '700';
    tfoot.style.borderTop = '2px solid var(--border, #93c5fd)';
    tfoot.innerHTML = '<td colspan="2" style="text-align:right">' + t.totals + '</td><td>' + pc + '</td><td>' + addDelTotal + '</td><td>' + tf + '</td><td>' + tc + '</td><td>' + ic + '</td><td>' + lc + '</td>';
    mBody.appendChild(tfoot);
  };

  // ── Section 5: Deliveries ──
  SV.renderDeliveries = function(s) {
    var eff = SV.effectiveData(s);
    var pBody = document.getElementById('sv-prs-body');
    pBody.innerHTML = '';
    if (!eff.prs || eff.prs.length === 0) {
      pBody.innerHTML = '<tr><td colspan="6" class="sv-muted">' + t.noPRs + '</td></tr>';
      return;
    }
    var prTotalAdd = 0, prTotalDel = 0, prTotalFiles = 0, prTotalCommits = 0;
    eff.prs.forEach(function(pr) {
      var r = document.createElement('tr');
      var lnk = 'https://github.com/' + SV.REPO + '/pull/' + pr.number;
      var add = pr.additions || 0, del = pr.deletions || 0, files = pr.changed_files || 0, cm = pr.commits || 0;
      prTotalAdd += add; prTotalDel += del; prTotalFiles += files; prTotalCommits += cm;
      var diffStr = add || del ? '<span style="color:#16a34a">+' + add + '</span> <span style="color:#dc2626">\u2212' + del + '</span>' : '\u2014';
      r.innerHTML = '<td><strong>#' + pr.number + '</strong></td><td>' + SV.esc(pr.title || '\u2014') +
        '</td><td>' + diffStr + '</td><td>' + (files || '\u2014') + '</td><td>' + (cm || '\u2014') +
        '</td><td><a href="' + lnk + '" target="_blank">' + t.view + '</a></td>';
      pBody.appendChild(r);
    });
    if (eff.prs.length > 1) {
      var foot = document.createElement('tr');
      foot.style.cssText = 'font-weight:bold;border-top:2px solid var(--border, #93c5fd)';
      foot.innerHTML = '<td colspan="2" style="text-align:right">' + t.totals + '</td>' +
        '<td><span style="color:#16a34a">+' + prTotalAdd + '</span> <span style="color:#dc2626">\u2212' + prTotalDel + '</span></td>' +
        '<td>' + prTotalFiles + '</td><td>' + prTotalCommits + '</td><td></td>';
      pBody.appendChild(foot);
    }
  };

  // ── Section 6: Issues ──
  SV.renderIssues = function(s) {
    var iSection = document.getElementById('sv-section-issues');
    var iBody = document.getElementById('sv-issues-body');
    var hasSessionIssue = s.issue_number && s.issue_number !== null;
    var relatedIssues = s.related_issues || [];
    if (relatedIssues.length === 0) {
      (s.issues || []).filter(function(n) { return n !== s.issue_number; }).forEach(function(n) {
        relatedIssues.push({ number: n, title: '', state: '', labels: [] });
      });
    }
    var totalIssueCount = (hasSessionIssue ? 1 : 0) + relatedIssues.length;
    if (!hasSessionIssue && relatedIssues.length === 0) { iSection.style.display = 'none'; return; }
    iSection.style.display = '';
    iBody.innerHTML = '';
    var thead = iBody.parentElement.querySelector('thead tr');
    thead.innerHTML = '<th>#</th><th>' + t.issueCol + '</th><th>' + t.typeCol + '</th><th>' + t.titleCol + '</th><th>' + t.sessionCol + '</th>';
    var issueIdx = 0;
    if (hasSessionIssue) {
      issueIdx++;
      var sr = document.createElement('tr');
      var sHref = 'https://github.com/' + SV.REPO + '/issues/' + s.issue_number;
      var sKindEmoji = s.session_kind === 'continuation' ? '\ud83d\udd01' : '\ud83d\udcac';
      sr.innerHTML = '<td><strong>' + issueIdx + '</strong></td><td><a href="' + sHref + '" target="_blank">#' + s.issue_number + '</a></td>' +
        '<td>' + SV.issueLabelBadge(s.issue_number, t.issueTypeSession) + '</td>' +
        '<td>' + sKindEmoji + ' ' + SV.esc(s.title || '') + '</td><td><span style="opacity:0.5">\u2014</span></td>';
      iBody.appendChild(sr);
    }
    var parentIssues = s.parent_issues || [];
    var childrenIssues = s.children_issues || [];
    relatedIssues.forEach(function(ri) {
      issueIdx++;
      var rr = document.createElement('tr');
      var rHref = 'https://github.com/' + SV.REPO + '/issues/' + ri.number;
      var riEmoji = '\ud83d\udd17';
      if (parentIssues.indexOf(ri.number) !== -1) riEmoji = '\ud83d\udcac';
      else if (childrenIssues.indexOf(ri.number) !== -1) riEmoji = '\ud83d\udd01';
      var riSessionId = 'issue-' + ri.number;
      var riSession = SV.findSession(riSessionId);
      var riSessionCell = riSession
        ? '<a href="javascript:void(0)" onclick="event.stopPropagation();document.getElementById(\'sv-session-select\').value=\'' + riSessionId + '\';document.getElementById(\'sv-session-select\').dispatchEvent(new Event(\'change\'))" title="' + SV.esc(t.openSession) + '" style="margin-right:0.4em">\ud83d\udd0d</a>' +
          '<a href="' + window.location.pathname + '?session=' + ri.number + '" target="_blank" title="' + SV.esc(t.openTab) + '">\ud83d\udd17</a>'
        : '<span style="opacity:0.5">\u2014</span>';
      rr.innerHTML = '<td><strong>' + issueIdx + '</strong></td><td><a href="' + rHref + '" target="_blank">#' + ri.number + '</a></td>' +
        '<td>' + SV.issueLabelBadge(ri.number, t.issueTypeRelated) + '</td>' +
        '<td>' + riEmoji + ' ' + SV.esc(ri.title || '\u2014') + '</td><td>' + riSessionCell + '</td>';
      iBody.appendChild(rr);
    });
    if (totalIssueCount > 1) {
      var ifoot = document.createElement('tr');
      ifoot.style.cssText = 'font-weight:bold;border-top:2px solid var(--border, #93c5fd)';
      ifoot.innerHTML = '<td colspan="3" style="text-align:right">' + t.totals + '</td><td>' + totalIssueCount + ' issues</td><td></td>';
      iBody.appendChild(ifoot);
    }
  };

  // ── Section 7: Lessons ──
  SV.renderLessons = function(s) {
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
  };

  // ── Section 7b: Collateral Tasks (v2.0) ──
  SV.renderCollateral = function(s) {
    var section = document.getElementById('sv-section-collateral');
    if (!section) return;
    var eff = SV.effectiveData(s);
    var tasks = eff.collateralTasks;
    if (!tasks || tasks.length === 0) {
      section.style.display = 'none';
      return;
    }
    section.style.display = '';
    var body = document.getElementById('sv-collateral-body');
    if (!body) return;

    var statusEmoji = { completed: '\u2705', in_progress: '\u23f3', pending: '\u23f8\ufe0f' };
    var typeEmoji = {
      fix: '\ud83d\udd27', feature: '\ud83d\ude80', doc: '\ud83d\udcdd',
      test: '\ud83e\uddea', chore: '\u2699\ufe0f', refactor: '\u267b\ufe0f'
    };

    // Collateral summary bar
    var completed = tasks.filter(function(ct) { return ct.status === 'completed'; }).length;
    var inProgress = tasks.filter(function(ct) { return ct.status === 'in_progress'; }).length;
    var pending = tasks.filter(function(ct) { return ct.status === 'pending'; }).length;
    var pctDone = tasks.length > 0 ? Math.round((completed / tasks.length) * 100) : 0;

    var html = '<div class="sv-progress-summary">' +
      '<div class="sv-progress-bar"><div class="sv-progress-fill sv-fill-done" style="width:' + pctDone + '%"></div>' +
      '<div class="sv-progress-fill sv-fill-active" style="width:' + Math.round((inProgress / tasks.length) * 100) + '%"></div></div>' +
      '<span class="sv-progress-legend">' + t.progressCompleted + ': ' + completed +
      ' · ' + t.progressInProgress + ': ' + inProgress +
      ' · ' + t.progressPending + ': ' + pending + '</span></div>';

    html += '<table class="sv-table"><thead><tr>' +
      '<th>' + t.status + '</th><th>' + t.titleCol + '</th><th>' + t.typeCol + '</th>' +
      '<th>PRs</th><th></th></tr></thead><tbody>';
    tasks.forEach(function(ct) {
      var emoji = statusEmoji[ct.status] || '\u2022';
      var tEmoji = typeEmoji[ct.type] || '\ud83d\udce6';
      var prLinks = (ct.pr_numbers || []).map(function(n) {
        return '<a href="https://github.com/' + SV.REPO + '/pull/' + n + '" target="_blank">#' + n + '</a>';
      }).join(' ');
      var issueLink = ct.issue_number ?
        '<a href="https://github.com/' + SV.REPO + '/issues/' + ct.issue_number + '" target="_blank">#' + ct.issue_number + '</a> ' : '';
      // Task viewer link for collateral tasks with issue_number
      var taskLink = ct.issue_number ?
        '<a href="' + SV.baseurl + '/interfaces/task-workflow/?task=task-' + ct.issue_number + '" target="_blank" title="' + SV.esc(t.openTaskViewer) + '">\ud83d\udcca</a>' : '';
      html += '<tr><td>' + emoji + '</td><td>' + issueLink + SV.esc(ct.title || '') + '</td>' +
        '<td>' + tEmoji + ' ' + SV.esc(ct.type || '') + '</td><td>' + (prLinks || '\u2014') + '</td><td>' + taskLink + '</td></tr>';
    });
    html += '</tbody></table>';
    body.innerHTML = html;
  };

  // ── Section 7c: Session Tasks ──
  SV.renderTasks = function(s) {
    var section = document.getElementById('sv-section-tasks');
    if (!section) return;
    var tasks = s.tasks || [];
    if (!tasks || tasks.length === 0) {
      section.style.display = 'none';
      return;
    }
    section.style.display = '';
    var body = document.getElementById('sv-tasks-body');
    if (!body) return;
    body.innerHTML = '';

    var stageLabels = {
      initial: 'Initial', plan: 'Plan', analyze: 'Analyze',
      implement: 'Implement', validation: 'Validation',
      documentation: 'Documentation', approval: 'Approval',
      completion: 'Completion'
    };
    if (lang === 'fr') {
      stageLabels = {
        initial: 'Initial', plan: 'Planification', analyze: 'Analyse',
        implement: 'Impl\u00e9mentation', validation: 'Validation',
        documentation: 'Documentation', approval: 'Approbation',
        completion: 'Compl\u00e9tion'
      };
    }

    tasks.forEach(function(task) {
      var tr = document.createElement('tr');
      var stageIdx = task.current_stage_index || 0;
      var pct = Math.round(((stageIdx + 1) / 8) * 100);
      var stageName = stageLabels[task.current_stage] || task.current_stage;
      var issueLink = task.issue_number ?
        '<a href="https://github.com/' + SV.REPO + '/issues/' + task.issue_number + '" target="_blank">#' + task.issue_number + '</a>' : '';
      var taskViewerLink = task.task_id ?
        '<a href="' + SV.baseurl + '/interfaces/task-workflow/?task=' + task.task_id + '" target="_blank" title="Open in Task Viewer">\ud83d\udcca</a>' : '';

      tr.innerHTML =
        '<td>' + issueLink + '</td>' +
        '<td>' + SV.esc(task.title || '') + '</td>' +
        '<td><span class="sv-badge sv-badge-stage">' + SV.esc(stageName) + '</span></td>' +
        '<td><div style="display:flex;align-items:center;gap:6px;">' +
          '<div style="flex:1;height:6px;background:var(--border,#e1e4e8);border-radius:3px;overflow:hidden;">' +
            '<div style="width:' + pct + '%;height:100%;background:var(--accent,#2ea44f);border-radius:3px;"></div>' +
          '</div>' +
          '<span style="font-size:11px;opacity:0.7;">' + pct + '%</span>' +
        '</div></td>' +
        '<td>' + taskViewerLink + '</td>';
      body.appendChild(tr);
    });
  };

  // ── Section 9: Task Progression (v2.0) ──
  SV.renderProgression = function(s) {
    var section = document.getElementById('sv-section-progression');
    if (!section) return;

    var engStage = s.engineering_stage;
    var issueNum = s.issue_number;

    // Engineering stages in order
    var stages = [
      { key: 'analysis', emoji: '\ud83d\udd0d' },
      { key: 'planning', emoji: '\ud83d\udccb' },
      { key: 'design', emoji: '\ud83c\udfa8' },
      { key: 'implementation', emoji: '\ud83d\udee0\ufe0f' },
      { key: 'testing', emoji: '\ud83e\uddea' },
      { key: 'validation', emoji: '\u2705' },
      { key: 'review', emoji: '\ud83d\udc41\ufe0f' },
      { key: 'deployment', emoji: '\ud83d\ude80' }
    ];

    var currentIdx = -1;
    if (engStage) {
      for (var i = 0; i < stages.length; i++) {
        if (stages[i].key === engStage) { currentIdx = i; break; }
      }
    }

    if (currentIdx < 0 && !issueNum) {
      section.style.display = 'none';
      return;
    }
    section.style.display = '';
    var body = document.getElementById('sv-progression-body');
    if (!body) return;

    var html = '';

    // Stage progression bar
    if (currentIdx >= 0) {
      html += '<div class="sv-stage-track">';
      stages.forEach(function(stg, idx) {
        var cls = 'sv-stage-dot';
        if (idx < currentIdx) cls += ' sv-stage-done';
        else if (idx === currentIdx) cls += ' sv-stage-current';
        var info = SV.engStageMap[stg.key] || { label: stg.key };
        html += '<div class="' + cls + '" title="' + SV.esc(info.label) + '">' +
          '<span class="sv-stage-icon">' + stg.emoji + '</span>' +
          '<span class="sv-stage-name">' + SV.esc(info.label) + '</span></div>';
      });
      html += '</div>';
    }

    // Task viewer link
    if (issueNum) {
      var taskId = 'task-' + issueNum;
      html += '<div class="sv-task-link">' +
        '<a href="' + SV.baseurl + '/interfaces/task-workflow/?task=' + taskId + '" target="_blank" class="sv-btn-task-viewer">' +
        '\ud83d\udcca ' + t.openTaskViewer + ' \u2192</a></div>';
    }

    body.innerHTML = html;
  };

  // ── Section 8: Velocity ──
  SV.renderVelocity = function(s) {
    var eff = SV.effectiveData(s);
    var velSection = document.getElementById('sv-section-velocity');
    var tl = eff.additions + eff.deletions;
    var hasVelocityData = s.lines_per_hour || s.commits_per_hour || s.files_per_hour || tl > 0;
    if (!hasVelocityData) { velSection.style.display = 'none'; return; }
    velSection.style.display = '';
    var gauges = document.getElementById('sv-velocity-gauges');
    gauges.innerHTML = '';
    var pc = eff.prCount, tf = eff.files, tc = eff.commits;
    var avgLines = pc > 0 ? Math.round(tl / pc) : 0;
    var avgFiles = pc > 0 ? Math.round(tf / pc) : 0;
    var avgCommits = pc > 0 ? (tc / pc).toFixed(1) : 0;
    [
      { label: t.linesPerHour, value: s.lines_per_hour || 0, max: 2000 },
      { label: t.commitsPerHour, value: s.commits_per_hour || 0, max: 40 },
      { label: t.filesPerHour, value: s.files_per_hour || 0, max: 30 },
      { label: t.linesChanged + ' (' + t.avgPerPR + ')', value: avgLines, max: 500 },
      { label: t.filesChanged + ' (' + t.avgPerPR + ')', value: avgFiles, max: 20 },
      { label: t.commits + ' (' + t.avgPerPR + ')', value: avgCommits, max: 5 }
    ].forEach(function(g) {
      var pct = Math.min(100, Math.round((g.value / g.max) * 100));
      var el = document.createElement('div'); el.className = 'sv-gauge';
      el.innerHTML = '<div class="sv-gauge-label">' + g.label + '</div>' +
        '<div class="sv-gauge-value">' + g.value + '</div>' +
        '<div class="sv-gauge-bar"><div class="sv-gauge-fill" style="width:' + pct + '%"></div></div>';
      gauges.appendChild(el);
    });
  };
})();
