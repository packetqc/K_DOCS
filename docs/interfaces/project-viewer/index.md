---
layout: publication
page_type: interface
title: "Project Viewer"
description: "Interactive project viewer — browse projects, track task completion, aggregate metrics and knowledge grid scores across tasks."
pub_id: "Interface I4"
version: "v1"
date: "2026-03-09"
permalink: /interfaces/project-viewer/
keywords: "projects, tasks, metrics, completion, knowledge grid, workflow"
og_image: /assets/og/project-viewer-en-cayman.gif
dev_banner: "Interface in development — features and layout may change between sessions."
---

# Project Viewer

{::nomarkdown}

<div id="pv-viewer" data-baseurl="{{ site.baseurl }}">

<div class="pv-toolbar">
  <div class="pv-select-group">
    <label for="pv-project-select">Project</label>
    <select id="pv-project-select">
      <option value="">— All Projects —</option>
    </select>
  </div>
</div>

<div id="pv-empty-state" class="pv-empty">
  <p>Select a project to view details, or browse the overview below.</p>
  <p class="pv-muted"><span id="pv-project-count">0</span> projects available.</p>
</div>

<!-- Print-only cover page — hidden on screen, page 1 in PDF -->
<div id="pv-cover-page" aria-hidden="true">
  <div class="cover-body">
    <div class="cover-title" id="pv-cover-title">Project Viewer</div>
    <div class="cover-desc" id="pv-cover-desc"></div>
    <div class="cover-rule"></div>
    <div class="cover-meta" id="pv-cover-meta"></div>
  </div>
</div>

<!-- ═══ VIEW: Overview (all projects) ═══ -->
<div id="pv-view-overview" class="pv-view" style="display:none;">
  <div class="pv-section">
    <h2>Overview</h2>
    <div class="pv-stats-grid" id="pv-overview-stats"></div>
  </div>
  <div class="pv-section">
    <div class="pv-cards" id="pv-project-cards"></div>
  </div>
</div>

<!-- ═══ VIEW: Dashboard (single project) ═══ -->
<div id="pv-view-dashboard" class="pv-view" style="display:none;">

  <div class="pv-section">
    <div class="pv-section-header">
      <h2 id="pv-project-title"></h2>
      <div id="pv-project-meta"></div>
    </div>
    <div class="pv-stats-grid" id="pv-dashboard-stats"></div>
    <div id="pv-completion-bar"></div>
  </div>

  <div class="pv-section">
    <h3>Stage Distribution</h3>
    <div class="pv-stage-bar" id="pv-stage-bar"></div>
    <div id="pv-stage-legend"></div>
  </div>

  <div class="pv-section">
    <h3>Knowledge Grid Summary</h3>
    <div class="pv-grid-summary" id="pv-grid-summary"></div>
    <div class="pv-muted" id="pv-grid-score" style="margin-top:0.5rem;"></div>
  </div>

  <div class="pv-section">
    <h3>Project Tasks</h3>
    <div class="table-wrap">
      <table class="pv-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Task</th>
            <th>Stage</th>
            <th>Progress</th>
            <th>Changes</th>
            <th>Grid</th>
            <th></th>
          </tr>
        </thead>
        <tbody id="pv-tasks-body"></tbody>
      </table>
    </div>
  </div>

</div>

</div>

<link rel="stylesheet" href="{{ '/interfaces/project-viewer/project-viewer.css' | relative_url }}">

<script src="{{ '/interfaces/project-viewer/project-viewer.js' | relative_url }}"></script>
<script src="{{ '/interfaces/project-viewer/project-print.js' | relative_url }}"></script>
{:/nomarkdown}

<div class="pub-crossrefs">
<h3>Cross References</h3>
<div class="pub-crossrefs-list">
<a href="{{ '/interfaces/' | relative_url }}">Interfaces Index</a>
<a href="{{ '/interfaces/session-review/' | relative_url }}">I1 Session Review</a>
<a href="{{ '/interfaces/main-navigator/' | relative_url }}">I2 Main Navigator</a>
<a href="{{ '/interfaces/task-workflow/' | relative_url }}">I3 Tasks Workflow</a>
</div>
</div>
