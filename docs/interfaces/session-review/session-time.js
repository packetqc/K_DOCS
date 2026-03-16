// ═══ Session Review — Time Compilation (session-time.js) ═══
// 3-level tree: Task → Comment → PR with expand/collapse state.

(function() {
  'use strict';
  var SV = window.SV;
  if (!SV) return;
  var t = SV.t;
  var lang = SV.lang;

  function getPreview(c) {
    var p = c.step_name || c.preview || '';
    p = p.replace(/<[^>]+>/g, '').replace(/\|/g, ' ').replace(/^#+\s*/g, '').replace(/\*\*/g, '').replace(/\[([^\]]*)\]\([^)]*\)/g, '$1').replace(/\s+/g, ' ').trim();
    if (p.length > 70) p = p.substring(0, 67) + '...';
    return p;
  }

  // Build comment groups for a session (handles parent/child/continuation scoping)
  function buildCommentGroups(s, eff, tcPrs) {
    var commentGroups = [];
    var hasComments = s.comments && s.comments.length > 0;
    var hasAggComments = eff.agg && eff.agg.comments_by_task && eff.agg.comments_by_task.length > 0;
    var sessionWindowStart = s.task_created_at || eff.firstTime || null;
    var sessionWindowEnd = null;
    var isScoped = false;

    if (s.session_kind === 'continuation' && s.parent_tasks && s.parent_tasks.length > 0) {
      var parentNum = s.parent_tasks[0];
      var parentSession = null;
      for (var pi = 0; pi < SV.sessionsData.sessions.length; pi++) {
        if (SV.sessionsData.sessions[pi].task_number === parentNum) { parentSession = SV.sessionsData.sessions[pi]; break; }
      }
      if (parentSession && parentSession.children_tasks) {
        var siblings = [];
        parentSession.children_tasks.forEach(function(cNum) {
          for (var ci = 0; ci < SV.sessionsData.sessions.length; ci++) {
            if (SV.sessionsData.sessions[ci].task_number === cNum) { siblings.push(SV.sessionsData.sessions[ci]); break; }
          }
        });
        siblings.sort(function(a, b) { return (a.task_created_at || '').localeCompare(b.task_created_at || ''); });
        for (var si = 0; si < siblings.length; si++) {
          if (siblings[si].task_number === s.task_number) {
            if (si + 1 < siblings.length) sessionWindowEnd = siblings[si + 1].task_created_at;
            break;
          }
        }
        isScoped = true;
        var allSources = [parentSession].concat(siblings);
        var sourceMap = {};
        allSources.forEach(function(src) {
          if (!src || !src.comments || src.comments.length === 0) return;
          var num = src.task_number;
          if (sourceMap[num]) return;
          sourceMap[num] = { task_number: num, task_title: src.title || '', comments: [] };
          src.comments.forEach(function(c) {
            var ct = c.created_at || '';
            if (ct >= sessionWindowStart && (!sessionWindowEnd || ct < sessionWindowEnd)) sourceMap[num].comments.push(c);
          });
        });
        Object.keys(sourceMap).forEach(function(k) {
          if (sourceMap[k].comments.length > 0) commentGroups.push(sourceMap[k]);
        });
        commentGroups.sort(function(a, b) {
          if (a.task_number === s.task_number) return -1;
          if (b.task_number === s.task_number) return 1;
          var aT = a.comments.length > 0 ? a.comments[0].created_at : '';
          var bT = b.comments.length > 0 ? b.comments[0].created_at : '';
          return aT.localeCompare(bT);
        });
        if (tcPrs.length > 0) {
          tcPrs = tcPrs.filter(function(pr) {
            var pt = pr.created_at || '';
            return pt >= sessionWindowStart && (!sessionWindowEnd || pt < sessionWindowEnd);
          });
        }
      }
    }

    if (commentGroups.length === 0 && !isScoped) {
      if (hasAggComments) {
        var sessionDate = (s.task_created_at || s.date || '').substring(0, 10);
        eff.agg.comments_by_task.forEach(function(g) {
          if (g.task_number === s.task_number) {
            commentGroups.push({ task_number: g.task_number, task_title: g.task_title || '', comments: g.comments });
            return;
          }
          var scopedComments = g.comments.filter(function(c) { return (c.created_at || '').substring(0, 10) === sessionDate; });
          if (scopedComments.length > 0) commentGroups.push({ task_number: g.task_number, task_title: g.task_title || '', comments: scopedComments });
        });
      } else if (hasComments) {
        commentGroups = [{ task_number: s.task_number, task_title: s.title || '', comments: s.comments }];
      }
    }

    return { groups: commentGroups, isScoped: isScoped, tcPrs: tcPrs };
  }

  SV.renderTime = function(s) {
    var eff = SV.effectiveData(s);
    var tTotals = document.getElementById('sv-time-totals');
    var tContent = document.getElementById('sv-time-content');
    var hasComments = s.comments && s.comments.length > 0;
    var hasAggComments = eff.agg && eff.agg.comments_by_task && eff.agg.comments_by_task.length > 0;

    // Scope PRs to session date
    var tcPrs = (eff.agg && eff.agg.prs && eff.agg.prs.length > 0) ? eff.agg.prs : (s.prs || []);
    if (eff.agg && tcPrs.length > 0) {
      var prSessionDate = (s.task_created_at || s.date || '').substring(0, 10);
      if (prSessionDate) tcPrs = tcPrs.filter(function(pr) { return (pr.created_at || '').substring(0, 10) === prSessionDate; });
    }
    var hasPrs = tcPrs.length > 0;

    if (!hasComments && !hasAggComments && !hasPrs) {
      tTotals.textContent = '';
      tContent.innerHTML = '<p class="sv-muted">' + t.noTimeData + '</p>';
      return;
    }

    // Time spans
    var tcFirstTime = (eff.agg ? eff.agg.first_activity_time : null) || s.first_pr_time || s.task_created_at || eff.firstTime;
    var tcLastTime = (eff.agg ? eff.agg.last_activity_time : null) || s.last_pr_time || eff.lastTime;
    if (hasComments && s.comments.length > 0) {
      var ownTimes = [];
      s.comments.forEach(function(c) { if (c.created_at) ownTimes.push(c.created_at); if (c.updated_at) ownTimes.push(c.updated_at); });
      tcPrs.forEach(function(p) { if (p.created_at) ownTimes.push(p.created_at); if (p.merged_at) ownTimes.push(p.merged_at); });
      if (ownTimes.length > 0) { ownTimes.sort(); tcFirstTime = ownTimes[0]; tcLastTime = ownTimes[ownTimes.length - 1]; }
    }

    var result = buildCommentGroups(s, eff, tcPrs);
    var commentGroups = result.groups;
    var isScoped = result.isScoped;
    tcPrs = result.tcPrs;

    // Recompute time span from scoped groups
    if ((isScoped || hasAggComments) && commentGroups.length > 0) {
      var allTimes = [];
      commentGroups.forEach(function(g) { g.comments.forEach(function(c) { if (c.created_at) allTimes.push(c.created_at); }); });
      tcPrs.forEach(function(p) { if (p.created_at) allTimes.push(p.created_at); if (p.merged_at) allTimes.push(p.merged_at); });
      if (allTimes.length > 0) { allTimes.sort(); tcFirstTime = allTimes[0]; tcLastTime = allTimes[allTimes.length - 1]; }
    }

    var calStart = tcFirstTime ? SV.formatTime(tcFirstTime) : '\u2014';
    var calEnd = tcLastTime ? SV.formatTime(tcLastTime) : '\u2014';
    var calDur = SV.calcDuration(tcFirstTime, tcLastTime);
    var block = SV.timeBlock(tcFirstTime);
    var totalCommentCount = 0;
    commentGroups.forEach(function(g) { totalCommentCount += g.comments.length; });
    var itemCount = totalCommentCount || tcPrs.length;

    var scopeLabel = isScoped ? ' \u00b7 \ud83d\udd2c ' + (lang === 'fr' ? 'Fen\u00eatre de session' : 'Session window') : '';
    tTotals.textContent = t.totals + ': ' + itemCount + ' ' + t.tasks +
      (commentGroups.length > 1 ? ' \u00b7 ' + commentGroups.length + ' tasks' : '') +
      ' \u00b7 ' + t.calendarTime + ': ' + calStart + '\u2014' + calEnd +
      (calDur != null ? ' (' + SV.formatDuration(calDur) + ')' : '') +
      ' \u00b7 ' + block + scopeLabel;

    if (commentGroups.length > 0) {
      renderCommentTree(s, commentGroups, tcPrs, hasPrs, calDur, eff, tContent, isScoped);
    } else {
      renderLegacyPRTable(s, tcPrs, calDur, tContent);
    }
  };

  function renderCommentTree(s, commentGroups, tcPrs, hasPrs, calDur, eff, tContent, isScoped) {
    var tbl = '<table class="sv-table"><thead><tr>' +
      '<th>#</th><th>' + t.task + '</th><th>' + t.start + '</th><th>' + t.end + '</th>' +
      '<th>' + t.duration + '</th><th>' + t.inactive + '</th><th>' + t.calendar + '</th><th>' + t.status + '</th>' +
      '</tr></thead><tbody>';
    var totalActiveMin = 0, totalInactiveMin = 0, totalCalMin = 0;
    var globalRowIdx = 0;
    var isMultiTask = commentGroups.length > 1;
    var assignedPrs = {};

    commentGroups.forEach(function(group, gIdx) {
      var groupComments = group.comments;
      var taskNum = group.task_number;
      var gFirstTime = groupComments.length > 0 ? groupComments[0].created_at : null;
      var gLastTime = groupComments.length > 0 ? groupComments[groupComments.length - 1].created_at : null;
      var gCalMin = SV.calcDuration(gFirstTime, gLastTime);
      var gGroupActiveMin = 0;

      var taskRowId = 'task-' + gIdx;
      var taskLnk = taskNum ? '<a href="https://github.com/' + SV.REPO + '/issues/' + taskNum + '" target="_blank" style="text-decoration:none">#' + taskNum + '</a>' : '';
      var truncTitle = (group.task_title || '').length > 55 ? group.task_title.substring(0, 52) + '...' : (group.task_title || '');
      tbl += '<tr class="sv-row-parent sv-row-task" data-task="' + taskRowId + '" style="background:var(--code-bg, #f0f4ff);font-weight:bold;cursor:pointer">' +
        '<td></td><td>' + (taskLnk ? taskLnk + ' ' : '') + '\ud83d\udccc ' + SV.esc(truncTitle) + ' <span style="font-weight:normal;opacity:0.6">(' + groupComments.length + ')</span></td>' +
        '<td>' + (gFirstTime ? SV.formatTime(gFirstTime) : '\u2014') + '</td><td>' + (gLastTime ? SV.formatTime(gLastTime) : '\u2014') + '</td>' +
        '<td class="sv-task-active-' + gIdx + '"></td><td></td><td>' + SV.formatDuration(gCalMin) + '</td><td></td></tr>';

      // Map PRs to comments
      var prsByComment = {};
      groupComments.forEach(function(c, ci) { prsByComment[ci] = []; });
      if (hasPrs) {
        tcPrs.forEach(function(pr) {
          var prKey = (pr.number || '') + '-' + (pr.created_at || '');
          if (assignedPrs[prKey]) return;
          var bestIdx = -1;
          for (var ci = groupComments.length - 1; ci >= 0; ci--) {
            if (groupComments[ci].created_at <= pr.created_at) { bestIdx = ci; break; }
          }
          if (bestIdx >= 0) { prsByComment[bestIdx].push(pr); assignedPrs[prKey] = true; }
        });
      }

      // Pre-compute end times
      var endTimes = [];
      groupComments.forEach(function(c, i) {
        var endIso = null, estimated = false;
        if (c.updated_at && c.updated_at !== c.created_at) { endIso = c.updated_at; }
        else if (i + 1 < groupComments.length) { endIso = groupComments[i + 1].created_at; estimated = true; }
        else if (isMultiTask) { endIso = gLastTime; estimated = true; }
        else if (eff.lastTime) { endIso = eff.lastTime; estimated = true; }
        endTimes.push({ iso: endIso, estimated: estimated });
      });

      // Build runs of consecutive same-type comments
      var runs = [];
      groupComments.forEach(function(c, i) {
        if (runs.length === 0 || runs[runs.length - 1].type !== c.type) runs.push({ type: c.type, indices: [i] });
        else runs[runs.length - 1].indices.push(i);
      });

      function renderCommentRow(c, i, rowId, isChild, parentRowId) {
        var avatarUrl = c.type === 'user'
          ? 'https://raw.githubusercontent.com/' + SV.REPO + '/main/references/Martin/vicky.png'
          : 'https://raw.githubusercontent.com/' + SV.REPO + '/main/references/Martin/vicky-sunglasses.png';
        var avatarAlt = c.type === 'user' ? 'Martin' : 'Claude';
        var statusIcon = '';
        if (c.status === 'completed') statusIcon = '\u2705';
        else if (c.status === 'in_progress') statusIcon = '\u23f3';
        else if (c.type === 'user') statusIcon = '\ud83d\udcac';
        var cStart = SV.formatTime(c.created_at);
        var endIso = endTimes[i].iso;
        var estimated = endTimes[i].estimated;
        var cEnd = endIso ? (estimated ? '~' + SV.formatTime(endIso) : SV.formatTime(endIso)) : '\u2014';
        var calMin = endIso ? SV.calcDuration(c.created_at, endIso) : null;
        var hasCh = prsByComment[i] && prsByComment[i].length > 0;
        var activeMin = null;
        if (hasCh) {
          activeMin = 0;
          prsByComment[i].forEach(function(pr) { var d = SV.calcDuration(pr.created_at, pr.merged_at); if (d != null && d > 0) activeMin += d; });
          if (activeMin === 0) activeMin = calMin;
        } else { activeMin = calMin; }
        var inactiveMin = null;
        if (i > 0 && endTimes[i - 1].iso) {
          var gap = SV.calcDuration(endTimes[i - 1].iso, c.created_at);
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
        var html = '<tr class="' + rowClass + '" data-idx="' + rowId + '" data-task="task-' + gIdx + '"' +
          (isChild ? ' data-parent="' + parentRowId + '"' : '') + '>' +
          '<td>' + (isChild ? '' : '<img src="' + avatarUrl + '" alt="' + avatarAlt + '" class="sv-avatar">') + '</td>' +
          '<td>' + SV.esc(preview) + '</td><td>' + cStart + '</td><td>' + cEnd + '</td>' +
          '<td>' + SV.formatDuration(activeMin) + '</td><td>' + (inactiveMin != null ? SV.formatDuration(inactiveMin) : '\u2014') + '</td>' +
          '<td>' + SV.formatDuration(calMin) + '</td><td>' + statusIcon + '</td></tr>';
        if (hasBody && !isChild) {
          var bodyHtml = c.body_lines.map(function(line) { return SV.esc(line); }).join('\n');
          html += '<tr class="sv-row-body" data-parent="' + rowId + '" data-task="task-' + gIdx + '"><td></td><td colspan="7">' + bodyHtml + '</td></tr>';
        }
        return html;
      }

      function renderPRRows(commentIndices) {
        var html = '';
        commentIndices.forEach(function(ci) {
          if (!prsByComment[ci] || prsByComment[ci].length === 0) return;
          prsByComment[ci].forEach(function(pr) {
            var prDur = SV.calcDuration(pr.created_at, pr.merged_at);
            html += '<tr class="sv-row-child sv-row-pr sv-task-child-' + gIdx + '" data-task="task-' + gIdx + '">' +
              '<td><svg class="sv-avatar" width="20" height="20" viewBox="0 0 16 16" style="vertical-align:middle;border-radius:50%;background:#8b5cf6;padding:2px;box-sizing:border-box" fill="#ffffff"><path fill-rule="evenodd" d="M5 3.254V3.25v.005a.75.75 0 110-.005v.004zm.45 1.9a2.25 2.25 0 10-1.95.218v5.256a2.25 2.25 0 101.5 0V7.123A5.735 5.735 0 009.25 9h1.378a2.251 2.251 0 100-1.5H9.25a4.25 4.25 0 01-3.8-2.346zM12.75 9a.75.75 0 100-1.5.75.75 0 000 1.5zm-8.5 4.5a.75.75 0 100-1.5.75.75 0 000 1.5z"></path></svg></td>' +
              '<td>PR #' + pr.number + (pr.title ? ' \u2014 ' + SV.esc(pr.title) : '') + '</td>' +
              '<td>' + SV.formatTime(pr.created_at) + '</td><td>' + SV.formatTime(pr.merged_at) + '</td>' +
              '<td>' + SV.formatDuration(prDur) + '</td><td></td><td></td><td></td></tr>';
          });
        });
        return html;
      }

      // Render runs
      runs.forEach(function(run) {
        if (run.indices.length === 1) {
          var i = run.indices[0];
          var rowId = globalRowIdx++;
          tbl += renderCommentRow(groupComments[i], i, rowId, false, null);
          tbl += renderPRRows([i]);
        } else {
          var firstIdx = run.indices[0], lastIdx = run.indices[run.indices.length - 1];
          var firstC = groupComments[firstIdx], lastC = groupComments[lastIdx];
          var groupRowId = globalRowIdx++;
          var avatarUrl = firstC.type === 'user'
            ? 'https://raw.githubusercontent.com/' + SV.REPO + '/main/references/Martin/vicky.png'
            : 'https://raw.githubusercontent.com/' + SV.REPO + '/main/references/Martin/vicky-sunglasses.png';
          var runStart = SV.formatTime(firstC.created_at);
          var runEndIso = endTimes[lastIdx].iso;
          var runEnd = runEndIso ? (endTimes[lastIdx].estimated ? '~' + SV.formatTime(runEndIso) : SV.formatTime(runEndIso)) : '\u2014';
          var runCalMin = runEndIso ? SV.calcDuration(firstC.created_at, runEndIso) : null;
          var lastStatus = '';
          for (var ri = run.indices.length - 1; ri >= 0; ri--) {
            var rc = groupComments[run.indices[ri]];
            if (rc.status === 'completed') { lastStatus = '\u2705'; break; }
            if (rc.status === 'in_progress') { lastStatus = '\u23f3'; break; }
          }
          if (!lastStatus && firstC.type === 'user') lastStatus = '\ud83d\udcac';
          var rowClass = firstC.type === 'user' ? 'sv-row-user' : 'sv-row-bot';
          rowClass += ' sv-row-parent sv-row-child sv-task-child-' + gIdx + ' sv-row-run';
          tbl += '<tr class="' + rowClass + '" data-idx="' + groupRowId + '" data-task="task-' + gIdx + '">' +
            '<td><img src="' + avatarUrl + '" alt="' + (firstC.type === 'user' ? 'Martin' : 'Claude') + '" class="sv-avatar"></td>' +
            '<td>' + SV.esc(getPreview(firstC)) + ' <span style="font-weight:normal;opacity:0.6">(' + run.indices.length + ')</span></td>' +
            '<td>' + runStart + '</td><td>' + runEnd + '</td><td></td><td></td>' +
            '<td>' + SV.formatDuration(runCalMin) + '</td><td>' + lastStatus + '</td></tr>';
          run.indices.forEach(function(ci) {
            var childRowId = globalRowIdx++;
            tbl += renderCommentRow(groupComments[ci], ci, childRowId, true, groupRowId);
          });
          tbl += renderPRRows(run.indices);
        }
      });

      // Fill task active time
      (function(idx, am) {
        setTimeout(function() {
          var cell = tContent.querySelector('.sv-task-active-' + idx);
          if (cell) cell.textContent = SV.formatDuration(am);
        }, 0);
      })(gIdx, gGroupActiveMin);
    });

    tbl += '</tbody>';
    var footerCalMin = calDur != null ? calDur : totalCalMin;
    var footerInactiveMin = footerCalMin > totalActiveMin ? footerCalMin - totalActiveMin : 0;
    tbl += '<tfoot><tr style="font-weight:bold;border-top:2px solid var(--border, #93c5fd)">' +
      '<td colspan="4" style="text-align:right">' + t.totals + '</td>' +
      '<td>' + SV.formatDuration(totalActiveMin) + '</td><td>' + SV.formatDuration(footerInactiveMin) + '</td>' +
      '<td>' + SV.formatDuration(footerCalMin) + '</td><td></td></tr></tfoot>';
    tbl += '</table>';
    tbl += '<p class="sv-time-note" style="margin:0.5em 0 0;font-size:0.85em;color:var(--text-secondary, #6b7280);font-style:italic">' +
      (lang === 'fr' ? '\u2139\ufe0f Le temps inactif refl\u00e8te les r\u00e9flexions, d\u00e9cisions et courtes pauses entre les interactions utilisateur\u2013syst\u00e8me.'
        : '\u2139\ufe0f Inactive time reflects reflections, decisions, and short pauses between user\u2013system interactions.') + '</p>';
    tContent.innerHTML = tbl;
    bindExpandCollapse(s, tContent);
  }

  function renderLegacyPRTable(s, tcPrs, calDur, tContent) {
    var tbl = '<table class="sv-table"><thead><tr>' +
      '<th>#</th><th>' + t.task + '</th><th>' + t.start + '</th><th>' + t.end + '</th>' +
      '<th>' + t.duration + '</th><th>' + t.inactive + '</th><th>' + t.calendar + '</th><th>' + t.category + '</th>' +
      '</tr></thead><tbody>';
    var totalDurMin = 0, totalCalMin = 0;
    tcPrs.forEach(function(pr, i) {
      var prDur = SV.calcDuration(pr.created_at, pr.merged_at);
      var nextStart = (i + 1 < tcPrs.length) ? tcPrs[i + 1].created_at : pr.merged_at;
      var prCal = SV.calcDuration(pr.created_at, nextStart);
      var prInactive = (prCal != null && prDur != null) ? Math.max(0, prCal - prDur) : null;
      if (prDur != null) totalDurMin += prDur;
      if (prCal != null) totalCalMin += prCal;
      tbl += '<tr><td><strong>T' + (i+1) + '</strong></td>' +
        '<td>PR #' + pr.number + (pr.title ? ' \u2014 ' + SV.esc(pr.title) : '') + '</td>' +
        '<td>' + SV.formatTime(pr.created_at) + '</td><td>' + SV.formatTime(pr.merged_at) + '</td>' +
        '<td>' + SV.formatDuration(prDur) + '</td><td>' + (prInactive != null ? SV.formatDuration(prInactive) : '\u2014') + '</td>' +
        '<td>' + SV.formatDuration(prCal) + '</td>' +
        '<td>' + (s.request_type ? SV.reqTypeBadge(s.request_type) : SV.esc(s.type || '\u2014')) + '</td></tr>';
    });
    var totalInactive = Math.max(0, totalCalMin - totalDurMin);
    tbl += '</tbody><tfoot><tr style="font-weight:bold;border-top:2px solid var(--border, #93c5fd)">' +
      '<td colspan="4" style="text-align:right">' + t.totals + '</td>' +
      '<td>' + SV.formatDuration(totalDurMin) + '</td><td>' + SV.formatDuration(totalInactive) + '</td>' +
      '<td>' + SV.formatDuration(totalCalMin) + '</td><td></td></tr></tfoot></table>';
    tbl += '<p class="sv-time-note" style="margin:0.5em 0 0;font-size:0.85em;color:var(--text-secondary, #6b7280);font-style:italic">' +
      (lang === 'fr' ? '\u2139\ufe0f Le temps inactif refl\u00e8te les r\u00e9flexions, d\u00e9cisions et courtes pauses entre les interactions utilisateur\u2013syst\u00e8me.'
        : '\u2139\ufe0f Inactive time reflects reflections, decisions, and short pauses between user\u2013system interactions.') + '</p>';
    tContent.innerHTML = tbl;
  }

  function bindExpandCollapse(s, tContent) {
    var tcStateKey = 'sv-tc-state-' + (s.task_number || s.id);
    function tcLoadState() { try { return JSON.parse(localStorage.getItem(tcStateKey)) || {}; } catch(e) { return {}; } }
    function tcSaveState(state) { try { localStorage.setItem(tcStateKey, JSON.stringify(state)); } catch(e) {} }

    function tcSetTask(row, expand, state, save) {
      var taskId = row.getAttribute('data-task');
      var gKey = taskId.replace('task-', '');
      if (expand) row.classList.add('sv-expanded'); else row.classList.remove('sv-expanded');
      tContent.querySelectorAll('.sv-task-child-' + gKey).forEach(function(child) {
        if (expand) {
          if (child.classList.contains('sv-row-run-child') || child.classList.contains('sv-row-body')) return;
          child.classList.add('sv-visible');
        } else {
          child.classList.remove('sv-visible');
          child.classList.remove('sv-expanded');
          var childIdx = child.getAttribute('data-idx');
          if (childIdx) {
            tContent.querySelectorAll('.sv-row-pr[data-parent="' + childIdx + '"],.sv-row-body[data-parent="' + childIdx + '"],.sv-row-run-child[data-parent="' + childIdx + '"]').forEach(function(sub) { sub.classList.remove('sv-visible'); });
            if (state) state['c-' + childIdx] = false;
          }
        }
      });
      if (state) { state['g-' + gKey] = expand; if (save) tcSaveState(state); }
    }

    function tcSetComment(row, expand, state, save) {
      var idx = row.getAttribute('data-idx');
      if (expand) row.classList.add('sv-expanded'); else row.classList.remove('sv-expanded');
      tContent.querySelectorAll('.sv-row-pr[data-parent="' + idx + '"],.sv-row-body[data-parent="' + idx + '"],.sv-row-run-child[data-parent="' + idx + '"]').forEach(function(child) {
        if (expand) {
          child.classList.add('sv-visible');
          var childIdx = child.getAttribute('data-idx');
          if (childIdx) {
            tContent.querySelectorAll('.sv-row-pr[data-parent="' + childIdx + '"],.sv-row-body[data-parent="' + childIdx + '"]').forEach(function(nested) { nested.classList.add('sv-visible'); });
          }
        } else {
          child.classList.remove('sv-visible');
          child.classList.remove('sv-expanded');
          var childIdx = child.getAttribute('data-idx');
          if (childIdx) {
            tContent.querySelectorAll('.sv-row-pr[data-parent="' + childIdx + '"],.sv-row-body[data-parent="' + childIdx + '"]').forEach(function(nested) { nested.classList.remove('sv-visible'); });
            if (state) state['c-' + childIdx] = false;
          }
        }
      });
      if (state) { state['c-' + idx] = expand; if (save) tcSaveState(state); }
    }

    tContent.querySelectorAll('.sv-row-task').forEach(function(row) {
      row.addEventListener('click', function() {
        var state = tcLoadState();
        tcSetTask(this, !this.classList.contains('sv-expanded'), state, true);
      });
    });
    tContent.querySelectorAll('.sv-row-parent:not(.sv-row-task)').forEach(function(row) {
      row.addEventListener('click', function(e) {
        e.stopPropagation();
        var state = tcLoadState();
        tcSetComment(this, !this.classList.contains('sv-expanded'), state, true);
      });
    });

    // Restore saved state
    var tcState = tcLoadState();
    if (Object.keys(tcState).length > 0) {
      tContent.querySelectorAll('.sv-row-task').forEach(function(row) {
        var gKey = row.getAttribute('data-task').replace('task-', '');
        if (tcState['g-' + gKey]) tcSetTask(row, true, null, false);
      });
      tContent.querySelectorAll('.sv-row-parent:not(.sv-row-task)').forEach(function(row) {
        var idx = row.getAttribute('data-idx');
        if (tcState['c-' + idx]) tcSetComment(row, true, null, false);
      });
    }
  }
})();
