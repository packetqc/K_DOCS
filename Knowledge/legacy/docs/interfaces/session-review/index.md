---
layout: publication
page_type: interface
title: "Session Review"
description: "Interactive session viewer — select a knowledge session and explore its summary, metrics, time compilation, deliveries, and lessons learned."
pub_id: "Interface I1"
version: "v1"
date: "2026-02-27"
permalink: /interfaces/session-review/
keywords: "sessions, metrics, time compilation, productivity, review"
og_image: /assets/og/session-review-en-cayman.gif
dev_banner: "Interface in development — features and layout may change between sessions."
---

# Session Review

{::nomarkdown}

<div id="session-viewer" data-baseurl="{{ site.baseurl }}" data-repo="{{ site.github_repo | default: 'packetqc/knowledge' }}">

<div class="sv-toolbar">
  <div class="sv-select-group">
    <label for="sv-session-select">Session</label>
    <select id="sv-session-select">
      <option value="">— All Sessions —</option>
    </select>
  </div>
  <div class="sv-select-group">
    <label for="sv-refine-select">View</label>
    <select id="sv-refine-select">
      <option value="all">All sections</option>
      <option value="tasks">Tasks Overview</option>
      <option value="metrics">Metrics Dashboard</option>
      <option value="timeline">Timeline</option>
    </select>
  </div>
</div>

<div id="sv-data-mode" class="sv-data-mode">
  <span class="sv-data-mode-icon">📊</span>
  <span class="sv-data-mode-text">
    <strong>Static mode</strong> — Data is refreshed at the end of each work session.
    <span class="sv-data-mode-hint">Connect with GitHub OAuth2 for real-time session data.</span>
  </span>
</div>

<div id="sv-empty-state" class="sv-empty">
  <p>Select a session from the dropdown above to view its full report.</p>
  <p class="sv-muted"><span id="sv-session-count">0</span> sessions available.</p>
  <p class="sv-muted sv-version-note">All sessions with GitHub integrity are listed.</p>
</div>

<!-- ═══ VIEW: Overview (all sessions) ═══ -->
<div id="sv-view-overview" style="display:none;">
  <div class="sv-section">
    <h2 id="sv-overview-title">All Sessions</h2>
    <div class="sv-stats-grid" id="sv-overview-stats"></div>
  </div>
  <div class="sv-section">
    <div class="sv-cards" id="sv-session-cards"></div>
  </div>
</div>

<div id="sv-content" style="display:none;">

<!-- Print-only cover page — hidden on screen, page 1 in PDF -->
<div id="sv-cover-page" aria-hidden="true">
  <div class="cover-body">
    <div class="cover-title" id="sv-cover-title"></div>
    <div class="cover-desc" id="sv-cover-desc"></div>
    <div class="cover-rule"></div>
    <div class="cover-meta" id="sv-cover-meta"></div>
  </div>
</div>

<!-- Data source notice -->
<div id="sv-notice" class="sv-notice" style="display:none;"></div>

<!-- Section 1: Summary + 8 metric blocs -->
<div class="sv-section" id="sv-section-summary">
  <div class="sv-section-header">
    <h2 id="sv-title"></h2>
    <div class="sv-meta">
      <span class="sv-badge sv-badge-type" id="sv-type"></span>
      <span class="sv-badge sv-badge-request" id="sv-request-type" style="display:none;"></span>
      <span class="sv-badge sv-badge-stage" id="sv-eng-stage" style="display:none;"></span>
      <span class="sv-date" id="sv-date"></span>
      <span class="sv-branch" id="sv-branch"></span>
      <span class="sv-source-badges" id="sv-source-badges"></span>
      <span class="sv-badge sv-badge-usid" id="sv-user-session-id" style="display:none;" title="Internal session ID"></span>
    </div>
  </div>
  <p id="sv-summary" class="sv-summary"></p>
  <div class="sv-stats-grid" id="sv-stats-grid"></div>
</div>

<!-- Section 2: Metrics Compilation -->
<div class="sv-section" id="sv-section-metrics">
  <h3>Metrics Compilation</h3>
  <p id="sv-metrics-totals" class="sv-totals-line"></p>
  <div class="table-wrap sv-metrics-table">
    <table class="sv-table">
      <thead>
        <tr><th>#</th><th>Category</th><th>Pull Requests</th><th>+/-</th><th>Files</th><th>Commits</th><th>Issues</th><th>Lessons</th></tr>
      </thead>
      <tbody id="sv-metrics-body"></tbody>
    </table>
  </div>
</div>

<!-- Section 3: Pie Charts -->
<div class="sv-section" id="sv-section-pies">
  <div class="sv-pies-row">
    <div class="sv-chart-wrap" id="sv-chart-scope-wrap" style="display:none;">
      <canvas id="sv-chart-scope" width="280" height="280"></canvas>
    </div>
    <div class="sv-chart-wrap" id="sv-chart-metrics-wrap" style="display:none;">
      <canvas id="sv-chart-metrics" width="280" height="280"></canvas>
    </div>
    <div class="sv-chart-wrap" id="sv-chart-lines-wrap" style="display:none;">
      <canvas id="sv-chart-lines" width="280" height="280"></canvas>
    </div>
    <div class="sv-chart-wrap" id="sv-chart-time-wrap" style="display:none;">
      <canvas id="sv-chart-time" width="280" height="280"></canvas>
    </div>
  </div>
</div>

<!-- Section 4: Time Compilation -->
<div class="sv-section" id="sv-section-time">
  <h3>Time Compilation</h3>
  <p id="sv-time-totals" class="sv-totals-line"></p>
  <div class="table-wrap sv-time-table" id="sv-time-content"></div>
</div>

<!-- Section 5: Deliveries (PRs) -->
<div class="sv-section" id="sv-section-deliveries">
  <h3>Deliveries</h3>
  <div class="table-wrap">
    <table class="sv-table">
      <thead>
        <tr><th>#</th><th>Pull Request</th><th>+/-</th><th>Files</th><th>Commits</th><th>Link</th></tr>
      </thead>
      <tbody id="sv-prs-body"></tbody>
    </table>
  </div>
</div>

<!-- Section 6: Related Issues -->
<div class="sv-section" id="sv-section-issues" style="display:none;">
  <h3>Related Issues</h3>
  <div class="sv-table-wrap">
    <table class="sv-table sv-issues-table">
      <thead>
        <tr><th>#</th><th>Issue</th><th>Type</th><th>Title</th></tr>
      </thead>
      <tbody id="sv-issues-body"></tbody>
    </table>
  </div>
</div>

<!-- Section 7: Lessons & Decisions -->
<div class="sv-section" id="sv-section-lessons">
  <h3>Lessons &amp; Decisions</h3>
  <ul id="sv-lessons-list"></ul>
  <p id="sv-no-lessons" class="sv-muted" style="display:none;">No lessons recorded for this session.</p>
</div>

<!-- Section 7b: Collateral Tasks (v2.0) -->
<div class="sv-section" id="sv-section-collateral" style="display:none;">
  <h3>Collateral Tasks</h3>
  <div class="table-wrap" id="sv-collateral-body"></div>
</div>

<!-- Section 7c: Session Tasks -->
<div class="sv-section" id="sv-section-tasks" style="display:none;">
  <h3>Session Tasks</h3>
  <div class="table-wrap">
    <table class="sv-table">
      <thead>
        <tr><th>#</th><th>Task</th><th>Stage</th><th>Progress</th><th></th></tr>
      </thead>
      <tbody id="sv-tasks-body"></tbody>
    </table>
  </div>
</div>

<!-- Section 9: Task Progression (v2.0) -->
<div class="sv-section" id="sv-section-progression" style="display:none;">
  <h3>Task Progression</h3>
  <div id="sv-progression-body"></div>
</div>

<!-- Section 8: Velocity & Code Impact -->
<div class="sv-section" id="sv-section-velocity" style="display:none;">
  <h3>Velocity &amp; Code Impact</h3>
  <div class="sv-velocity-row">
    <div class="sv-velocity-gauges" id="sv-velocity-gauges"></div>
    <div class="sv-chart-wrap sv-chart-wide" id="sv-chart-impact-wrap" style="display:none;">
      <canvas id="sv-chart-impact" width="500" height="280"></canvas>
    </div>
  </div>
</div>

</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>

<link rel="stylesheet" href="{{ '/interfaces/session-review/session-review.css' | relative_url }}">

<!-- Session Review v2 — modular JS -->
<script src="{{ '/interfaces/session-review/session-core.js' | relative_url }}"></script>
<script src="{{ '/interfaces/session-review/session-charts.js' | relative_url }}"></script>
<script src="{{ '/interfaces/session-review/session-render.js' | relative_url }}"></script>
<script src="{{ '/interfaces/session-review/session-time.js' | relative_url }}"></script>
<script src="{{ '/interfaces/session-review/session-print.js' | relative_url }}"></script>
{:/nomarkdown}

<div class="pub-crossrefs">
<h3>Cross-references</h3>
<div class="pub-crossrefs-list">
<a href="{{ '/publications/' | relative_url }}">Publications Index</a>
<a href="{{ '/interfaces/' | relative_url }}">Interfaces Index</a>
<a href="{{ '/interfaces/main-navigator/' | relative_url }}">I2 Main Navigator</a>
<a href="{{ '/interfaces/task-workflow/' | relative_url }}">I3 Tasks Workflow</a>
</div>
</div>
