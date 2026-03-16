---
layout: publication
page_type: interface
title: "Visualiseur de projets"
description: "Visualiseur interactif de projets — parcourez les projets, suivez la complétion des tâches, agrégez les métriques et scores de grille Knowledge."
pub_id: "Interface I4"
version: "v1"
date: "2026-03-09"
permalink: /fr/interfaces/project-viewer/
keywords: "projets, tâches, métriques, complétion, grille knowledge, flux de travail"
og_image: /assets/og/project-viewer-fr-cayman.gif
dev_banner: "Interface en developpement — les fonctionnalites et la mise en page peuvent changer entre les sessions."
lang: fr
---

# Visualiseur de projets

{::nomarkdown}

<div id="pv-viewer" data-baseurl="{{ site.baseurl }}">

<div class="pv-toolbar">
  <div class="pv-select-group">
    <label for="pv-project-select">Projet</label>
    <select id="pv-project-select">
      <option value="">— Tous les projets —</option>
    </select>
  </div>
</div>

<div id="pv-empty-state" class="pv-empty">
  <p>Sélectionnez un projet pour voir les détails, ou parcourez la vue d'ensemble ci-dessous.</p>
  <p class="pv-muted"><span id="pv-project-count">0</span> projets disponibles.</p>
</div>

<!-- Page de couverture (impression uniquement) — masquée à l'écran, page 1 en PDF -->
<div id="pv-cover-page" aria-hidden="true">
  <div class="cover-body">
    <div class="cover-title" id="pv-cover-title">Visualiseur de projets</div>
    <div class="cover-desc" id="pv-cover-desc"></div>
    <div class="cover-rule"></div>
    <div class="cover-meta" id="pv-cover-meta"></div>
  </div>
</div>

<!-- ═══ VUE: Vue d'ensemble (tous les projets) ═══ -->
<div id="pv-view-overview" class="pv-view" style="display:none;">
  <div class="pv-section">
    <h2>Vue d'ensemble</h2>
    <div class="pv-stats-grid" id="pv-overview-stats"></div>
  </div>
  <div class="pv-section">
    <div class="pv-cards" id="pv-project-cards"></div>
  </div>
</div>

<!-- ═══ VUE: Tableau de bord (projet unique) ═══ -->
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
    <h3>Distribution des étapes</h3>
    <div class="pv-stage-bar" id="pv-stage-bar"></div>
    <div id="pv-stage-legend"></div>
  </div>

  <div class="pv-section">
    <h3>Résumé grille Knowledge</h3>
    <div class="pv-grid-summary" id="pv-grid-summary"></div>
    <div class="pv-muted" id="pv-grid-score" style="margin-top:0.5rem;"></div>
  </div>

  <div class="pv-section">
    <h3>Tâches du projet</h3>
    <div class="table-wrap">
      <table class="pv-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Tâche</th>
            <th>Étape</th>
            <th>Progrès</th>
            <th>Changements</th>
            <th>Grille</th>
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
{:/nomarkdown}

<div class="pub-crossrefs">
<h3>Références croisées</h3>
<div class="pub-crossrefs-list">
<a href="{{ '/fr/interfaces/' | relative_url }}">Index des interfaces</a>
<a href="{{ '/fr/interfaces/session-review/' | relative_url }}">I1 Revue de session</a>
<a href="{{ '/fr/interfaces/main-navigator/' | relative_url }}">I2 Navigateur principal</a>
<a href="{{ '/fr/interfaces/task-workflow/' | relative_url }}">I3 Flux de travail</a>
</div>
</div>
