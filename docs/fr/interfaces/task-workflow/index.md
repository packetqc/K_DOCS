---
layout: publication
page_type: interface
title: "Flux de travail des tâches"
description: "Visualiseur interactif du flux de travail — suivez la progression des tâches à travers 8 étapes, les résultats de validation et l'état des tests unitaires."
pub_id: "Interface I3"
version: "v1"
date: "2026-03-05"
permalink: /fr/interfaces/task-workflow/
keywords: "tâches, flux de travail, validation, étapes, tests unitaires, progression"
og_image: /assets/og/task-workflow-fr-cayman.gif
dev_banner: "Interface en developpement — les fonctionnalites et la mise en page peuvent changer entre les sessions."
lang: fr
---

# Flux de travail des tâches

{::nomarkdown}

<div id="tw-viewer" data-baseurl="{{ site.baseurl }}">

<div class="tw-toolbar">
  <div class="tw-select-group">
    <label for="tw-task-select">Tâche</label>
    <select id="tw-task-select">
      <option value="">— Sélectionner une tâche —</option>
    </select>
  </div>
  <div class="tw-select-group">
    <label for="tw-view-select">Vue</label>
    <select id="tw-view-select">
      <option value="dashboard">Tableau de bord</option>
      <option value="detail">Détail</option>
      <option value="validation">Validation</option>
    </select>
  </div>
</div>

<div id="tw-data-mode" class="tw-data-mode">
  <span class="tw-data-mode-icon">📋</span>
  <span class="tw-data-mode-text">
    <strong>Mode statique</strong> — Les données sont compilées à partir des caches de session.
  </span>
</div>

<!-- ═══ Progression de la tâche (toujours visible quand une tâche est sélectionnée) ═══ -->
<div id="tw-task-progression" class="tw-section" style="display:none;">
  <h2>Progression de la tâche</h2>
  <div class="tw-progression-bar" id="tw-progression-bar"></div>
  <div class="tw-progression-meta" id="tw-progression-meta"></div>
</div>

<div id="tw-empty-state" class="tw-empty">
  <p>Sélectionnez une tâche dans le menu ci-dessus pour voir son rapport de flux de travail.</p>
  <p class="tw-muted"><span id="tw-task-count">0</span> tâches disponibles.</p>
</div>

<!-- ═══ VUE: Tableau de bord — Grille Knowledge + Métriques + Temps ═══ -->
<div id="tw-view-dashboard" class="tw-view" style="display:none;">

  <div class="tw-section">
    <h2>Tableau de bord de session</h2>
    <div class="tw-stats-grid" id="tw-dashboard-stats"></div>
  </div>

  <div class="tw-section">
    <h3>Grille de validation Knowledge</h3>
    <div id="tw-knowledge-grid" class="tw-knowledge-grid"></div>
  </div>

  <div class="tw-section">
    <h3>Métriques</h3>
    <div class="tw-stats-grid" id="tw-metrics-stats"></div>
  </div>

  <div class="tw-section">
    <h3>Compilation temporelle</h3>
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
    <h3>Durées par étape</h3>
    <div class="table-wrap">
      <table class="tw-table">
        <thead>
          <tr><th>Étape</th><th>Durée</th><th>% du actif</th></tr>
        </thead>
        <tbody id="tw-stage-duration-body"></tbody>
      </table>
    </div>
  </div>

</div>

<!-- ═══ VUE: Détail ═══ -->
<div id="tw-view-detail" class="tw-view" style="display:none;">
  <div class="tw-section" id="tw-section-summary">
    <div class="tw-section-header">
      <h2 id="tw-title"></h2>
      <div class="tw-meta">
        <span class="tw-badge tw-badge-stage" id="tw-current-stage"></span>
        <span class="tw-badge tw-badge-task" id="tw-task-badge"></span>
        <span class="tw-date" id="tw-date"></span>
        <span class="tw-branch" id="tw-branch"></span>
      </div>
    </div>
    <p id="tw-description" class="tw-description"></p>
    <div class="tw-stats-grid" id="tw-detail-stats"></div>
  </div>
  <div class="tw-section" id="tw-section-timeline">
    <h3>Chronologie des étapes</h3>
    <div class="tw-timeline" id="tw-timeline"></div>
  </div>
  <div class="tw-section" id="tw-section-history">
    <h3>Historique des étapes</h3>
    <div class="table-wrap">
      <table class="tw-table">
        <thead>
          <tr><th>#</th><th>Étape</th><th>Direction</th><th>Raison</th><th>Début</th><th>Durée</th></tr>
        </thead>
        <tbody id="tw-history-body"></tbody>
      </table>
    </div>
  </div>
  <div class="tw-section" id="tw-section-steps" style="display:none;">
    <h3>Historique des sous-étapes</h3>
    <div class="table-wrap">
      <table class="tw-table">
        <thead>
          <tr><th>#</th><th>Étape</th><th>Sous-étape</th><th>Début</th><th>Durée</th></tr>
        </thead>
        <tbody id="tw-steps-body"></tbody>
      </table>
    </div>
  </div>
</div>

<!-- ═══ VUE: Validation ═══ -->
<div id="tw-view-validation" class="tw-view" style="display:none;">
  <div class="tw-section" id="tw-section-validation">
    <h3>Résultats de validation</h3>
    <div class="tw-validation-grid" id="tw-validation-grid"></div>
  </div>
  <div class="tw-section" id="tw-section-checks" style="display:none;">
    <h3>Vérifications</h3>
    <div class="table-wrap">
      <table class="tw-table">
        <thead>
          <tr><th>Étape</th><th>Vérification</th><th>Résultat</th><th>Heure</th></tr>
        </thead>
        <tbody id="tw-checks-body"></tbody>
      </table>
    </div>
  </div>
  <div class="tw-section" id="tw-section-tests" style="display:none;">
    <h3>Tests unitaires</h3>
    <div class="table-wrap">
      <table class="tw-table">
        <thead>
          <tr><th>ID</th><th>Étape</th><th>Description</th><th>Source</th><th>Résultat</th></tr>
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
{:/nomarkdown}

<div class="pub-crossrefs">
<h3>Références croisées</h3>
<div class="pub-crossrefs-list">
<a href="{{ '/fr/interfaces/' | relative_url }}">Index des interfaces</a>
<a href="{{ '/fr/interfaces/session-review/' | relative_url }}">I1 Revue de session</a>
<a href="{{ '/fr/interfaces/main-navigator/' | relative_url }}">I2 Navigateur principal</a>
<a href="{{ '/fr/publications/session-management/' | relative_url }}">#8 Gestion de session</a>
</div>
</div>
