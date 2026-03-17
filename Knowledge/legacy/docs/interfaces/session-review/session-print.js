// ═══ Session Review — Print/PDF Export (session-print.js) ═══
// Session-aware PDF export with cover page.

(function() {
  'use strict';
  var SV = window.SV;
  if (!SV) return;
  var lang = SV.lang;

  setTimeout(function() {
    var btn = document.getElementById('exportPdf');
    if (!btn) return;
    var newBtn = btn.cloneNode(true);
    btn.parentNode.replaceChild(newBtn, btn);
    newBtn.addEventListener('click', function() {
      var PAGE_SIZES = { letter: '8.5in 11in', legal: '8.5in 14in' };
      var sizeRadio = document.querySelector('input[name="pubPageSize"]:checked');
      var orientRadio = document.querySelector('input[name="pubOrient"]:checked');
      var format = sizeRadio ? sizeRadio.value : 'letter';
      var orient = orientRadio ? orientRadio.value : 'portrait';
      var size = PAGE_SIZES[format] || PAGE_SIZES.letter;
      if (orient === 'landscape') size += ' landscape';
      var origTitle = document.title;
      var fileName = 'Session Review';
      var cs = SV.currentSession;
      if (cs) {
        var d = cs.date || '';
        var tm = cs.first_pr_time ? SV.formatTime(cs.first_pr_time).replace(':', 'h') : '';
        var title = (cs.title || 'Untitled').replace(/[\u2014\u2013<>:"\/\\|?*#]/g, '').trim();
        if (title.length > 60) title = title.substring(0, 57) + '...';
        fileName = 'Session - ' + d + (tm ? ' ' + tm : '') + ' - ' + title;
      }
      document.title = fileName;
      var now = new Date();
      var ts = now.getFullYear() + '-' + String(now.getMonth() + 1).padStart(2, '0') + '-' +
        String(now.getDate()).padStart(2, '0') + ' ' + String(now.getHours()).padStart(2, '0') + ':' +
        String(now.getMinutes()).padStart(2, '0');
      var coverPage = document.getElementById('sv-cover-page');
      if (coverPage && cs) {
        document.getElementById('sv-cover-title').textContent = cs.title || 'Untitled';
        var descParts = [];
        if (cs.type) descParts.push(cs.type);
        if (cs.request_type) descParts.push(cs.request_type);
        document.getElementById('sv-cover-desc').textContent = descParts.join(' \u2014 ') || 'Session Report';
        var metaLines = '';
        if (cs.date) metaLines += '<div>Date: ' + cs.date + '</div>';
        if (cs.branch) metaLines += '<div>Branch: <code>' + cs.branch + '</code></div>';
        if (cs.issue_number) metaLines += '<div>Issue: #' + cs.issue_number + '</div>';
        metaLines += '<div>' + (cs.prs ? cs.prs.length : 0) + ' PRs \u00b7 ' + (cs.comments ? cs.comments.length : 0) + ' comments</div>';
        metaLines += '<div class="cover-gen-line">Generated: ' + ts + '</div>';
        metaLines += '<div style="margin-top:0.5cm;font-size:9pt;color:#555">Authors: Martin Paquet &amp; Claude (Anthropic, Opus 4.6)</div>';
        document.getElementById('sv-cover-meta').innerHTML = metaLines;
        coverPage.style.display = 'flex';
      }
      var styleEl = document.getElementById('printSizeStyle');
      if (styleEl) {
        styleEl.textContent = '@page { size: ' + size + '; }\n' +
          '@page { @bottom-left { content: "Generated: ' + ts + '"; } @bottom-center { content: counter(page) " / " counter(pages); } @bottom-right { content: "Knowledge"; } }\n' +
          '@page :first { @top-left { content: ""; border: none; } @top-center { content: ""; border: none; } @top-right { content: ""; border: none; } @bottom-left { content: ""; border: none; } @bottom-center { content: ""; border: none; } @bottom-right { content: ""; border: none; } }';
      }
      window.addEventListener('afterprint', function() {
        document.title = origTitle;
        if (coverPage) coverPage.style.display = 'none';
      }, { once: true });
      setTimeout(function() { window.print(); }, 0);
    });
  }, 0);
})();
