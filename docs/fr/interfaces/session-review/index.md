---
layout: publication
page_type: interface
title: "Revu de session"
description: "Visionneuse interactive de sessions — sélectionnez une session knowledge et explorez son résumé, métriques, compilation des temps, livraisons et leçons apprises."
pub_id: "Interface I1"
version: "v1"
date: "2026-02-27"
permalink: /fr/interfaces/session-review/
keywords: "sessions, métriques, compilation des temps, productivité, revue"
og_image: /assets/og/session-review-fr-cayman.gif
dev_banner: "Interface en developpement — les fonctionnalites et la mise en page peuvent changer entre les sessions."
lang: fr
---

# Revu de session

{::nomarkdown}

<div id="session-viewer" data-baseurl="{{ site.baseurl }}">

<div class="sv-toolbar">
  <div class="sv-select-group">
    <label for="sv-session-select">Session</label>
    <select id="sv-session-select">
      <option value="">— Choisir une session —</option>
    </select>
  </div>
  <div class="sv-select-group">
    <label for="sv-refine-select">Vue</label>
    <select id="sv-refine-select">
      <option value="all">Toutes les sections</option>
      <option value="tasks">Vue des tâches</option>
      <option value="metrics">Tableau de bord métriques</option>
      <option value="timeline">Chronologie</option>
    </select>
  </div>
</div>

<div id="sv-data-mode" class="sv-data-mode">
  <span class="sv-data-mode-icon">📊</span>
  <span class="sv-data-mode-text">
    <strong>Mode statique</strong> — Les données sont mises à jour à la fin de chaque session de travail.
    <span class="sv-data-mode-hint">Connectez-vous avec GitHub OAuth2 pour des données de session en temps réel.</span>
  </span>
</div>

<div id="sv-empty-state" class="sv-empty">
  <p>Sélectionnez une session ci-dessus pour afficher son rapport complet.</p>
  <p class="sv-muted"><span id="sv-session-count">0</span> sessions disponibles.</p>
  <p class="sv-muted sv-version-note">Seules les sessions <strong>v51+</strong> (avec suivi de tâches) sont listées — la convention de protocole structuré appliquée depuis le 2026-02-27.</p>
</div>

<div id="sv-content" style="display:none;">

<!-- Page couverture pour impression — cachée à l'écran, page 1 en PDF -->
<div id="sv-cover-page" aria-hidden="true">
  <div class="cover-body">
    <div class="cover-title" id="sv-cover-title"></div>
    <div class="cover-desc" id="sv-cover-desc"></div>
    <div class="cover-rule"></div>
    <div class="cover-meta" id="sv-cover-meta"></div>
  </div>
</div>

<!-- Avis de source de données -->
<div id="sv-notice" class="sv-notice" style="display:none;"></div>

<!-- Section 1: Résumé + 8 blocs métriques -->
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
    </div>
  </div>
  <p id="sv-summary" class="sv-summary"></p>
  <div class="sv-stats-grid" id="sv-stats-grid"></div>
</div>

<!-- Section 2: Compilation des métriques -->
<div class="sv-section" id="sv-section-metrics">
  <h3>Compilation des métriques</h3>
  <p id="sv-metrics-totals" class="sv-totals-line"></p>
  <div class="table-wrap sv-metrics-table">
    <table class="sv-table">
      <thead>
        <tr><th>#</th><th>Catégorie</th><th>PRs</th><th>+/-</th><th>Fichiers</th><th>Commits</th><th>Tâches</th><th>Leçons</th></tr>
      </thead>
      <tbody id="sv-metrics-body"></tbody>
    </table>
  </div>
</div>

<!-- Section 3: Graphiques circulaires -->
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

<!-- Section 4: Compilation des temps -->
<div class="sv-section" id="sv-section-time">
  <h3>Compilation des temps</h3>
  <p id="sv-time-totals" class="sv-totals-line"></p>
  <div class="table-wrap sv-time-table" id="sv-time-content"></div>
</div>

<!-- Section 5: Livraisons (PRs) -->
<div class="sv-section" id="sv-section-deliveries">
  <h3>Livraisons</h3>
  <div class="table-wrap">
    <table class="sv-table">
      <thead>
        <tr><th>#</th><th>Pull Request</th><th>+/-</th><th>Fichiers</th><th>Commits</th><th>Lien</th></tr>
      </thead>
      <tbody id="sv-prs-body"></tbody>
    </table>
  </div>
</div>

<!-- Section 6: Tâches liées -->
<div class="sv-section" id="sv-section-related-tasks" style="display:none;">
  <h3>Tâches liées</h3>
  <div class="sv-table-wrap">
    <table class="sv-table sv-tasks-table">
      <thead>
        <tr><th>#</th><th>Tâche</th><th>Type</th><th>Titre</th></tr>
      </thead>
      <tbody id="sv-tasks-body"></tbody>
    </table>
  </div>
</div>

<!-- Section 7: Leçons et décisions -->
<div class="sv-section" id="sv-section-lessons">
  <h3>Leçons et décisions</h3>
  <ul id="sv-lessons-list"></ul>
  <p id="sv-no-lessons" class="sv-muted" style="display:none;">Aucune leçon enregistrée pour cette session.</p>
</div>

<!-- Section 8: Vélocité & Impact du code -->
<div class="sv-section" id="sv-section-velocity" style="display:none;">
  <h3>Vélocité &amp; Impact du code</h3>
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

<script src="{{ '/interfaces/session-review/session-review.js' | relative_url }}"></script>
{:/nomarkdown}

<div class="pub-crossrefs">
<h3>Références croisées</h3>
<div class="pub-crossrefs-list">
<a href="{{ '/fr/publications/' | relative_url }}">Index des publications</a>
<a href="{{ '/fr/publications/session-management/' | relative_url }}">#8 Gestion des sessions</a>
<a href="{{ '/fr/publications/session-metrics-time/' | relative_url }}">#20 Métriques et temps de session</a>
<a href="{{ '/fr/publications/interactive-work-sessions/' | relative_url }}">#19 Sessions de travail interactives</a>
<a href="{{ '/fr/publications/distributed-knowledge-dashboard/' | relative_url }}">#4a Tableau de bord des connaissances</a>
<a href="{{ '/fr/interfaces/main-navigator/' | relative_url }}">I2 Navigateur principal</a>
</div>
</div>
