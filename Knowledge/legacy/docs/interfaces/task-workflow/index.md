---
layout: publication
page_type: interface
title: "Tasks Workflow"
description: "Interactive task workflow viewer — track task progression through 8 workflow stages, validation results, and unit test status."
pub_id: "Interface I3"
version: "v1"
date: "2026-03-05"
permalink: /interfaces/task-workflow/
keywords: "tasks, workflow, validation, stages, unit tests, progression"
og_image: /assets/og/task-workflow-en-cayman.gif
dev_banner: "Interface in development — features and layout may change between sessions."
---

# Tasks Workflow

{::nomarkdown}

<div id="tw-viewer" data-baseurl="{{ site.baseurl }}">

<div class="tw-toolbar">
  <div class="tw-select-group">
    <label for="tw-task-select">Task</label>
    <select id="tw-task-select">
      <option value="">— All Tasks —</option>
    </select>
  </div>
  <div class="tw-select-group">
    <label for="tw-view-select">View</label>
    <select id="tw-view-select">
      <option value="dashboard">Dashboard</option>
      <option value="detail">Detail</option>
      <option value="validation">Validation</option>
    </select>
  </div>
</div>

<div id="tw-data-mode" class="tw-data-mode">
  <span class="tw-data-mode-icon">📋</span>
  <span class="tw-data-mode-text">
    <strong>Static mode</strong> — Task data is compiled from session runtime caches.
  </span>
</div>

<!-- Print-only cover page — hidden on screen, page 1 in PDF -->
<div id="tw-cover-page" aria-hidden="true">
  <div class="cover-body">
    <div class="cover-title" id="tw-cover-title">Tasks Workflow</div>
    <div class="cover-desc" id="tw-cover-desc"></div>
    <div class="cover-rule"></div>
    <div class="cover-meta" id="tw-cover-meta"></div>
  </div>
</div>

<!-- ═══ Task Progression (always visible when task selected) ═══ -->
<div id="tw-task-progression" class="tw-section" style="display:none;">
  <h2>Task Progression</h2>
  <div class="tw-progression-bar" id="tw-progression-bar"></div>
  <div class="tw-progression-meta" id="tw-progression-meta"></div>
</div>

<div id="tw-empty-state" class="tw-empty">
  <p>Select a task from the dropdown above to view its workflow report.</p>
  <p class="tw-muted"><span id="tw-task-count">0</span> tasks available.</p>
</div>

<!-- ═══ VIEW: Overview (all tasks) ═══ -->
<div id="tw-view-overview" style="display:none;">
  <div class="tw-section">
    <h2 id="tw-overview-title">All Tasks</h2>
    <div class="tw-stats-grid" id="tw-overview-stats"></div>
  </div>
  <div class="tw-section">
    <h3 id="tw-overview-stage-title">Stage Distribution</h3>
    <div class="tw-stage-bar-overview" id="tw-overview-stage-bar"></div>
    <div id="tw-overview-stage-legend"></div>
  </div>
  <div class="tw-section">
    <div class="tw-cards" id="tw-task-cards"></div>
  </div>
</div>

<!-- ═══ VIEW: Dashboard — Knowledge grid + Metrics + Time ═══ -->
<div id="tw-view-dashboard" class="tw-view" style="display:none;">

  <div class="tw-section">
    <h2>Session Dashboard</h2>
    <div class="tw-stats-grid" id="tw-dashboard-stats"></div>
  </div>

  <div class="tw-section">
    <h3>Knowledge Validation Grid</h3>
    <div id="tw-knowledge-grid" class="tw-knowledge-grid"></div>
  </div>

  <div class="tw-section">
    <h3>Metrics</h3>
    <div class="tw-stats-grid" id="tw-metrics-stats"></div>
  </div>

  <div class="tw-section">
    <h3>Time Compilation</h3>
    <div class="tw-stats-grid" id="tw-time-stats"></div>
    <div class="tw-chart-row">
      <div class="tw-chart-wrap" id="tw-chart-time-wrap">
        <canvas id="tw-chart-time" width="400" height="280"></canvas>
      </div>
      <div class="tw-chart-wrap" id="tw-chart-proportions-wrap">
        <canvas id="tw-chart-proportions" width="400" height="280"></canvas>
      </div>
    </div>
  </div>

  <div class="tw-section">
    <h3>Stage Duration Breakdown</h3>
    <div class="table-wrap">
      <table class="tw-table">
        <thead>
          <tr><th>Stage</th><th>Duration</th><th>% of Active</th></tr>
        </thead>
        <tbody id="tw-stage-duration-body"></tbody>
      </table>
    </div>
  </div>

</div>


<!-- ═══ VIEW: Detail — Full task report ═══ -->
<div id="tw-view-detail" class="tw-view" style="display:none;">

  <!-- Section 1: Task Summary -->
  <div class="tw-section" id="tw-section-summary">
    <div class="tw-section-header">
      <h2 id="tw-title"></h2>
      <div class="tw-meta">
        <span class="tw-badge tw-badge-stage" id="tw-current-stage"></span>
        <span class="tw-badge tw-badge-issue" id="tw-issue-badge"></span>
        <span class="tw-date" id="tw-date"></span>
        <span class="tw-branch" id="tw-branch"></span>
      </div>
    </div>
    <p id="tw-description" class="tw-description"></p>
    <div class="tw-stats-grid" id="tw-detail-stats"></div>
  </div>

  <!-- Section 2: Stage Timeline -->
  <div class="tw-section" id="tw-section-timeline">
    <h3>Stage Timeline</h3>
    <div class="tw-timeline" id="tw-timeline"></div>
  </div>

  <!-- Section 3: Stage History -->
  <div class="tw-section" id="tw-section-history">
    <h3>Stage History</h3>
    <div class="table-wrap">
      <table class="tw-table">
        <thead>
          <tr><th>#</th><th>Stage</th><th>Direction</th><th>Reason</th><th>Entered</th><th>Duration</th></tr>
        </thead>
        <tbody id="tw-history-body"></tbody>
      </table>
    </div>
  </div>

  <!-- Section 4: Step History (for stages with steps) -->
  <div class="tw-section" id="tw-section-steps" style="display:none;">
    <h3>Step History</h3>
    <div class="table-wrap">
      <table class="tw-table">
        <thead>
          <tr><th>#</th><th>Stage</th><th>Step</th><th>Entered</th><th>Duration</th></tr>
        </thead>
        <tbody id="tw-steps-body"></tbody>
      </table>
    </div>
  </div>

</div>

<!-- ═══ VIEW: Validation — Validation results ═══ -->
<div id="tw-view-validation" class="tw-view" style="display:none;">

  <div class="tw-section" id="tw-section-validation">
    <h3>Validation Results</h3>
    <div class="tw-validation-grid" id="tw-validation-grid"></div>
  </div>

  <div class="tw-section" id="tw-section-checks" style="display:none;">
    <h3>Validation Checks</h3>
    <div class="table-wrap">
      <table class="tw-table">
        <thead>
          <tr><th>Stage</th><th>Check</th><th>Result</th><th>Time</th></tr>
        </thead>
        <tbody id="tw-checks-body"></tbody>
      </table>
    </div>
  </div>

  <div class="tw-section" id="tw-section-tests" style="display:none;">
    <h3>Unit Tests</h3>
    <div class="table-wrap">
      <table class="tw-table">
        <thead>
          <tr><th>ID</th><th>Stage</th><th>Description</th><th>Source</th><th>Result</th></tr>
        </thead>
        <tbody id="tw-tests-body"></tbody>
      </table>
    </div>
  </div>

</div>


</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>

<link rel="stylesheet" href="{{ '/interfaces/task-workflow/task-workflow.css' | relative_url }}">

<script src="{{ '/interfaces/task-workflow/task-workflow.js' | relative_url }}"></script>
<script src="{{ '/interfaces/task-workflow/task-print.js' | relative_url }}"></script>
{:/nomarkdown}

<div class="pub-crossrefs">
<h3>Cross-references</h3>
<div class="pub-crossrefs-list">
<a href="{{ '/interfaces/' | relative_url }}">Interfaces Index</a>
<a href="{{ '/interfaces/session-review/' | relative_url }}">I1 Session Review</a>
<a href="{{ '/interfaces/main-navigator/' | relative_url }}">I2 Main Navigator</a>
<a href="{{ '/publications/' | relative_url }}">Publications Index</a>
</div>
</div>
