// ═══ Session Review — Charts (session-charts.js) ═══
// Chart.js doughnut/bar charts: time, scope, metrics, lines, impact.

(function() {
  'use strict';
  var SV = window.SV;
  if (!SV) return;

  var chartTime = null, chartScope = null, chartMetrics = null, chartLines = null, chartImpact = null;
  var t = SV.t;
  var lang = SV.lang;

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

  SV.destroyCharts = function() {
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
  };

  function makeDoughnut(canvasId, wrapId, labels, data, bgColors, borderColors, title) {
    var wrap = document.getElementById(wrapId);
    wrap.style.display = '';
    document.getElementById('sv-section-pies').style.display = '';
    var ctx = document.getElementById(canvasId).getContext('2d');
    var isDark = SV.isDarkTheme();
    return new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: labels,
        datasets: [{ data: data, backgroundColor: bgColors, borderColor: borderColors, borderWidth: 2 }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          legend: { position: 'bottom', labels: { color: isDark ? '#93c5fd' : '#475569', font: { size: 12 }, padding: 12 } },
          title: { display: true, text: title, color: isDark ? '#ffffff' : '#0f172a', font: { size: 14, weight: 'bold' } }
        }
      }
    });
  }

  SV.renderAllCharts = function(s) {
    SV.destroyCharts();
    if (typeof Chart === 'undefined') return;

    var eff = SV.effectiveData(s);
    var hasComments = s.comments && s.comments.length > 0;
    var hasAggComments = eff.agg && eff.agg.comments_by_issue && eff.agg.comments_by_issue.length > 0;
    var hasPrs = eff.prs.length > 0;

    // --- Time pie chart: Active vs Inactive ---
    var activeMin = 0, inactiveMin = 0, calMin = 0;
    if (hasComments && s.comments.length > 0) {
      var chEndTimes = [];
      s.comments.forEach(function(c, i) {
        var endIso = null;
        if (c.updated_at && c.updated_at !== c.created_at) endIso = c.updated_at;
        else if (i + 1 < s.comments.length) endIso = s.comments[i + 1].created_at;
        else if (s.last_pr_time) endIso = s.last_pr_time;
        chEndTimes.push(endIso);
      });
      s.comments.forEach(function(c, i) {
        var endIso = chEndTimes[i];
        var cCal = endIso ? SV.calcDuration(c.created_at, endIso) : 0;
        if (cCal == null || cCal < 0) cCal = 0;
        calMin += cCal;
        var prsByC = [];
        if (hasPrs) {
          eff.prs.forEach(function(pr) {
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
            var d = SV.calcDuration(pr.created_at, pr.merged_at);
            if (d != null && d > 0) cActive += d;
          });
          if (cActive === 0) cActive = cCal;
        } else { cActive = cCal; }
        activeMin += cActive;
        if (i > 0 && chEndTimes[i - 1]) {
          var gap = SV.calcDuration(chEndTimes[i - 1], c.created_at);
          if (gap != null && gap > 0) inactiveMin += gap;
        }
      });
    } else if (hasPrs) {
      eff.prs.forEach(function(pr, i) {
        var prDur = SV.calcDuration(pr.created_at, pr.merged_at);
        var nextStart = (i + 1 < eff.prs.length) ? eff.prs[i + 1].created_at : pr.merged_at;
        var prCal = SV.calcDuration(pr.created_at, nextStart);
        if (prDur != null && prDur > 0) activeMin += prDur;
        if (prCal != null && prCal > 0) calMin += prCal;
        if (i > 0 && eff.prs[i - 1].merged_at) {
          var gap = SV.calcDuration(eff.prs[i - 1].merged_at, pr.created_at);
          if (gap != null && gap > 0) inactiveMin += gap;
        }
      });
    }
    if (calMin > 0) {
      chartTime = makeDoughnut('sv-chart-time', 'sv-chart-time-wrap',
        [(lang === 'fr' ? 'Actif' : 'Active') + ' (' + SV.formatDuration(activeMin) + ')',
         (lang === 'fr' ? 'Inactif' : 'Inactive') + ' (' + SV.formatDuration(inactiveMin) + ')'],
        [activeMin, inactiveMin],
        [chartColors.active.bg, chartColors.inactive.bg],
        [chartColors.active.border, chartColors.inactive.border],
        lang === 'fr' ? 'Proportions temporelles' : 'Time Proportions'
      );
    }

    // --- Scope pie chart ---
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
    var scopeByType = {};
    (s.related_issues || []).forEach(function(ri) {
      if (ri.number === s.issue_number) return;
      var labels = ri.labels || [];
      var typeLabel = null;
      for (var li = 0; li < labels.length; li++) {
        if (labels[li] !== 'SESSION') { typeLabel = labels[li]; break; }
      }
      if (!typeLabel) typeLabel = '_other';
      if (!scopeByType[typeLabel]) scopeByType[typeLabel] = { count: 0, lines: 0 };
      scopeByType[typeLabel].count++;
      var cs = SV.findSession('issue-' + ri.number);
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
      chartScope = makeDoughnut('sv-chart-scope', 'sv-chart-scope-wrap',
        scLabels, scData, scBg, scBorder,
        t.scopeTitle + ' (' + scopeTotal + ' issues)'
      );
    }

    // --- Deliverables pie chart ---
    var mPrs = eff.prCount, mCommits = 0, mFiles = 0;
    if (eff.prs.length > 0) {
      eff.prs.forEach(function(p) { mCommits += (p.commits || 0); mFiles += (p.changed_files || 0); });
    }
    var mIssues = (s.issues && s.issues.length) || 0;
    var mLessons = (s.lessons && s.lessons.length) || 0;
    var mTotal = mPrs + mCommits + mFiles + mIssues + mLessons;
    if (mTotal > 0) {
      var mLabels = [], mData = [], mBg = [], mBorder = [];
      if (mPrs > 0) { mLabels.push(t.prCount + ' (' + mPrs + ')'); mData.push(mPrs); mBg.push(chartColors.cats[0].bg); mBorder.push(chartColors.cats[0].border); }
      if (mCommits > 0) { mLabels.push(t.commits + ' (' + mCommits + ')'); mData.push(mCommits); mBg.push(chartColors.cats[3].bg); mBorder.push(chartColors.cats[3].border); }
      if (mFiles > 0) { mLabels.push(t.filesChanged + ' (' + mFiles + ')'); mData.push(mFiles); mBg.push(chartColors.cats[4].bg); mBorder.push(chartColors.cats[4].border); }
      if (mIssues > 0) { mLabels.push(t.issueCount + ' (' + mIssues + ')'); mData.push(mIssues); mBg.push(chartColors.cats[1].bg); mBorder.push(chartColors.cats[1].border); }
      if (mLessons > 0) { mLabels.push(t.lessonCount + ' (' + mLessons + ')'); mData.push(mLessons); mBg.push(chartColors.cats[2].bg); mBorder.push(chartColors.cats[2].border); }
      chartMetrics = makeDoughnut('sv-chart-metrics', 'sv-chart-metrics-wrap',
        mLabels, mData, mBg, mBorder,
        lang === 'fr' ? 'Livrables' : 'Deliverables'
      );
    }

    // --- Lines changed pie chart ---
    if (hasPrs) {
      var totalAdd = 0, totalDel = 0;
      eff.prs.forEach(function(p) { totalAdd += (p.additions || 0); totalDel += (p.deletions || 0); });
      if (totalAdd + totalDel > 0) {
        chartLines = makeDoughnut('sv-chart-lines', 'sv-chart-lines-wrap',
          [t.additionsLabel + ' (+' + totalAdd + ')', t.deletionsLabel + ' (-' + totalDel + ')'],
          [totalAdd, totalDel],
          ['rgba(22,163,74,0.7)', 'rgba(220,38,38,0.7)'],
          ['#16a34a', '#dc2626'],
          t.linesChanged + ' (' + (totalAdd + totalDel) + ')'
        );
      }
    }

    // --- Code impact bar chart ---
    if (hasPrs) {
      var hasImpact = eff.prs.some(function(p) { return (p.additions || 0) + (p.deletions || 0) > 0; });
      if (hasImpact) {
        var impactWrap = document.getElementById('sv-chart-impact-wrap');
        impactWrap.style.display = '';
        var ctx = document.getElementById('sv-chart-impact').getContext('2d');
        var isDark = SV.isDarkTheme();
        chartImpact = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: eff.prs.map(function(p) { return '#' + p.number; }),
            datasets: [
              { label: t.additionsLabel, data: eff.prs.map(function(p) { return p.additions || 0; }), backgroundColor: 'rgba(22,163,74,0.7)', borderColor: '#16a34a', borderWidth: 1 },
              { label: t.deletionsLabel, data: eff.prs.map(function(p) { return -(p.deletions || 0); }), backgroundColor: 'rgba(220,38,38,0.7)', borderColor: '#dc2626', borderWidth: 1 }
            ]
          },
          options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'top', labels: { color: isDark ? '#93c5fd' : '#475569', font: { size: 11 }, padding: 10 } },
              title: { display: true, text: t.codeImpact, color: isDark ? '#ffffff' : '#0f172a', font: { size: 13, weight: 'bold' } },
              tooltip: { callbacks: { label: function(ctx) { return ctx.dataset.label + ': ' + Math.abs(ctx.raw); } } }
            },
            scales: {
              x: { grid: { color: isDark ? 'rgba(148,163,184,0.2)' : 'rgba(0,0,0,0.08)' }, ticks: { color: isDark ? '#94a3b8' : '#64748b', callback: function(v) { return Math.abs(v); } } },
              y: { grid: { display: false }, ticks: { color: isDark ? '#94a3b8' : '#64748b', font: { size: 10 } } }
            }
          }
        });
        var minH = Math.max(200, eff.prs.length * 28 + 80);
        document.getElementById('sv-chart-impact').parentElement.style.minHeight = minH + 'px';
      }
    }
  };
})();
