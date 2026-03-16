// ═══ Project Viewer — Print/PDF Export (project-print.js) ═══
// Project-aware PDF export with cover page.
// Follows session-print.js pattern: override PDF button, explicitly show cover.

(function() {
  'use strict';

  setTimeout(function() {
    var btn = document.getElementById('exportPdf');
    if (!btn) return;

    // Clone button to remove layout's default handler
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
      var lang = (window.location.pathname.indexOf('/fr/') !== -1) ? 'fr' : 'en';
      var sel = document.getElementById('pv-project-select');
      var projectName = sel && sel.value ? sel.options[sel.selectedIndex].textContent.trim() : '';
      var fileName = projectName
        ? 'Project Viewer - ' + projectName.replace(/[\u2014\u2013<>:"\/\\|?*#]/g, '').trim()
        : (lang === 'fr' ? 'Visualiseur de projets' : 'Project Viewer');
      document.title = fileName;

      var now = new Date();
      var ts = now.getFullYear() + '-' + String(now.getMonth() + 1).padStart(2, '0') + '-' +
        String(now.getDate()).padStart(2, '0') + ' ' + String(now.getHours()).padStart(2, '0') + ':' +
        String(now.getMinutes()).padStart(2, '0');

      // Explicitly show the cover page before printing
      var coverPage = document.getElementById('pv-cover-page');
      if (coverPage) {
        // Cover is already populated by updateCoverPage() — just make it visible
        coverPage.style.display = 'flex';
        coverPage.style.alignItems = 'center';
        coverPage.style.justifyContent = 'center';
        coverPage.style.minHeight = '100vh';
        coverPage.style.pageBreakAfter = 'always';
        coverPage.style.textAlign = 'center';
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
