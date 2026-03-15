---
layout: publication
title: "Visualisation de pages web — Documentation complète"
description: "Référence technique complète pour le pipeline de rendu local : architecture, patrons de code, préservation des sources Mermaid, exclusion du pipeline web, résultats de validation et analyse de sécurité."
pub_id: "Publication #16 — Complète"
version: "v1"
date: "2026-02-26"
permalink: /fr/publications/web-page-visualization/full/
og_image: /assets/og/web-page-visualization-fr-cayman.gif
keywords: "visualisation web, rendu Mermaid, Playwright, Chromium, diagnostics IA, gestion documentaire, pipeline autonome, préservation des sources"
---

# Visualisation de pages web — Documentation complète
{: #pub-title}

**Sommaire**

| | |
|---|---|
| [Auteurs](#auteurs) | Auteurs de la publication |
| [Résumé](#résumé) | Ce que fait cette fonctionnalité et pourquoi |
| [Public cible](#public-cible) | Qui devrait lire quoi |
| [Architecture](#architecture) | Inventaire des composants et flux de données |
| [Pipeline 1 : Visualisation de page complète](#pipeline-1--visualisation-de-page-complète) | Rendu de pages web complètes |
| [Pipeline 2 : Diagramme Mermaid vers image](#pipeline-2--diagramme-mermaid-vers-image) | Rendu de diagrammes individuels |
| [Cas d'utilisation](#cas-dutilisation) | Trois domaines de réutilisation |
| [Préservation des sources Mermaid](#préservation-des-sources-mermaid) | Conception du format hybride |
| [Exclusion du pipeline web](#exclusion-du-pipeline-web) | Prévention des conflits de rendu |
| [Contraintes et limitations](#contraintes-et-limitations) | Limites connues |
| [Découvertes clés](#découvertes-clés) | Résultats des sessions |
| [Résultats de validation](#résultats-de-validation) | Tests effectués |
| [Sécurité par conception](#sécurité-par-conception) | Conformité à la qualité autosuffisant |
| [Publications connexes](#publications-connexes) | Références croisées |

## Auteurs

**Martin Paquet** — Analyste-programmeur en sécurité réseau, administrateur de sécurité réseau et systèmes, concepteur et programmeur de logiciels embarqués. 30 ans d'expérience en systèmes embarqués, sécurité réseau, télécommunications et développement logiciel.

**Claude** (Anthropic, Opus 4.6) — Partenaire de développement IA. A implémenté les pipelines de rendu, validé l'approche contre les contraintes de sécurité par conception, et documenté la méthodologie à partir des sessions de développement interactif.

---

## Résumé

Cette publication documente un **pipeline autonome, zéro dépendance** pour le rendu de pages web et de diagrammes Mermaid en images, directement depuis l'environnement d'un assistant de code IA. Le pipeline utilise uniquement des outils pré-installés (Python, Playwright, Chromium) et un paquet npm local (mermaid.js) — aucun service externe, aucun appel CDN au moment du rendu, aucune dépendance API.

La fonctionnalité a émergé d'un besoin diagnostique : vérifier comment les pages web sont réellement rendues (diagrammes Mermaid, thèmes CSS, mise en page bilingue) sans demander à l'utilisateur de vérifier manuellement dans un navigateur. Elle s'est révélée immédiatement réutilisable dans trois domaines :

1. **Diagnostics interactifs** — Claude rend la page, identifie les problèmes de rendu, propose des correctifs — le tout dans la même session
2. **Conception interactive** — Validation visuelle pendant la construction itérative de pages web (changements de mise en page, thèmes CSS, miroirs bilingues)
3. **Gestion documentaire** — Génération de captures d'écran pour les publications, conversion de diagrammes Mermaid pour les pipelines d'exportation (PDF, DOCX), comparaison visuelle avant/après

Le pipeline respecte la qualité *autosuffisant* du système de connaissances : un seul `git clone` démarre tout. Aucun service externe signifie aucun service à casser, aucune clé API à gérer, aucune dépendance réseau au moment du rendu.

---

## Public cible

| Audience | Sections recommandées |
|----------|----------------------|
| **Administrateurs réseau/système** | Architecture — conception autonome et zéro appels réseau. Sécurité par conception — aucune dépendance externe |
| **Programmeurs / développeurs** | Patrons de code des pipelines — patrons Python/Playwright réutilisables. Préservation des sources Mermaid — l'approche hybride `<picture>` + `<details>` |
| **Gestionnaires techniques** | Cas d'utilisation — trois domaines de réutilisation. Résumé pour vue stratégique |
| **Ingénieurs documentation** | Préservation des sources Mermaid + Exclusion du pipeline web — conception de la chaîne de génération documentaire |
| **Praticiens du développement assisté par IA** | Publication complète — le paradigme d'un agent IA qui peut voir ce qu'il construit |

---

## Architecture

Le pipeline opère entièrement dans l'environnement du conteneur Claude Code. Aucun appel API externe au moment du rendu.

```
urllib (récupérer HTML) → HTML autonome → Playwright + Chromium → npm mermaid → captures
```

### Inventaire des composants

| Composant | Rôle | Emplacement | Externe? |
|-----------|------|-------------|----------|
| **urllib** | Récupérer le HTML depuis GitHub Pages | stdlib Python | Non — contourne le proxy via socket direct |
| **Playwright** | Automatisation de navigateur headless | Paquet Python (pré-installé) | Non — paquet local |
| **Chromium** | Moteur de rendu DOM complet (CSS, SVG, JS) | `/root/.cache/ms-playwright/chromium-*/chrome-linux/chrome` | Non — binaire pré-installé |
| **npm mermaid** | Rendu de diagrammes Mermaid (code → SVG) | `/tmp/mermaid-local-test/node_modules/mermaid/dist/mermaid.min.js` | Non — paquet npm local |

**Zéro appels réseau au moment du rendu.** Le seul appel réseau est la récupération initiale du HTML via urllib (optionnel — peut aussi rendre depuis des fichiers markdown locaux ou du HTML généré).

### Pourquoi urllib?

Le proxy du conteneur intercepte les clients HTTP standard (`curl`, `requests`, navigation par `page.goto()`). Le `urllib` de Python ouvre des connexions socket directes, contournant entièrement le proxy. C'est le même mécanisme que `gh_helper.py` utilise pour les appels API GitHub. C'est la sortie de secours universelle dans l'environnement Claude Code.

### Pourquoi Chromium (pas jsdom)?

Les tentatives précédentes avec jsdom (une implémentation DOM JavaScript pour Node.js) ont échoué car jsdom n'implémente pas les méthodes DOM SVG (`getBBox`, `getComputedTextLength`) que Mermaid requiert pour le calcul de la mise en page des diagrammes. Chromium fournit un DOM complet avec support SVG intégral — le même moteur de rendu que les utilisateurs voient dans leurs navigateurs.

---

## Pipeline 1 : Visualisation de page complète

Rendre une page web complète telle que l'utilisateur la verrait, avec tous les diagrammes Mermaid rendus, le CSS appliqué et la mise en page calculée.

### Étapes

1. **Récupérer le HTML** — via `urllib.request` (contourne le proxy, retourne le HTML brut de GitHub Pages)
2. **Extraire le contenu body** — retirer les références CSS/JS externes qui bloqueraient dans le conteneur
3. **Construire un HTML autonome** — injecter le style CSS type GitHub en ligne. Tout le style est embarqué
4. **Lancer Playwright** — Chromium headless avec `--no-sandbox`, `--disable-gpu`
5. **Injecter mermaid.js** — via `page.add_script_tag(path=...)` depuis le paquet npm local
6. **Rendre les blocs Mermaid** — trouver les éléments `<code class="language-mermaid">`, rendre chacun en SVG
7. **Capturer les écrans** — page complète et/ou par viewport (paginé)

### Patron de code

```python
import asyncio
import os
import re
from playwright.async_api import async_playwright
import urllib.request

MERMAID_JS = "/tmp/mermaid-local-test/node_modules/mermaid/dist/mermaid.min.js"
CHROME = "/root/.cache/ms-playwright/chromium-1194/chrome-linux/chrome"

async def render_web_page(url, output_dir="/tmp"):
    """Rendre une page web avec diagrammes Mermaid en captures d'écran."""

    # 1. Récupérer le HTML
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")

    # 2. Extraire le body
    body_match = re.search(r'<body[^>]*>(.*)</body>', html, re.DOTALL)
    body = body_match.group(1) if body_match else html

    # 3. HTML autonome avec style GitHub
    self_contained = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial;
       max-width: 980px; margin: 0 auto; padding: 20px; line-height: 1.5;
       color: #24292f; }}
h1, h2 {{ border-bottom: 1px solid #d0d7de; padding-bottom: .3em; }}
table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
th, td {{ border: 1px solid #d0d7de; padding: 6px 13px; }}
th {{ background: #f6f8fa; font-weight: 600; }}
code {{ background: #f6f8fa; padding: 2px 6px; border-radius: 3px; font-size: 85%; }}
pre {{ background: #f6f8fa; padding: 16px; border-radius: 6px; overflow: auto; }}
.mermaid {{ text-align: center; margin: 16px 0; }}
</style>
</head><body>{body}</body></html>"""

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path=CHROME,
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
        )
        page = await browser.new_page(viewport={"width": 1280, "height": 900})
        await page.goto("about:blank")
        await page.add_script_tag(path=MERMAID_JS)
        await page.evaluate("""(html) => {
            document.open(); document.write(html); document.close();
        }""", self_contained)
        await page.wait_for_timeout(2000)

        result = await page.evaluate("""async () => {
            mermaid.initialize({startOnLoad: false, theme: 'default',
                                securityLevel: 'loose'});
            const blocks = document.querySelectorAll('code.language-mermaid');
            let ok = 0, fail = 0;
            for (let i = 0; i < blocks.length; i++) {
                try {
                    const { svg } = await mermaid.render('mmd-' + i,
                                                          blocks[i].textContent);
                    const div = document.createElement('div');
                    div.className = 'mermaid';
                    div.innerHTML = svg;
                    blocks[i].parentElement.replaceWith(div);
                    ok++;
                } catch(e) { fail++; }
            }
            return {total: blocks.length, ok, fail};
        }""")

        await page.screenshot(path=f"{output_dir}/page-full.png", full_page=True)
        await browser.close()
        return result
```

---

## Pipeline 2 : Diagramme Mermaid vers image

Rendre des diagrammes Mermaid individuels en SVG ou PNG avec fond transparent. Essentiel pour le pipeline d'exportation DOCX (Mermaid n'est pas supporté dans Word) et pour générer des images de diagrammes autonomes pour les publications.

### Patron de code

```python
async def render_mermaid_to_image(diagram_code, output_path, format="png"):
    """Rendre un diagramme Mermaid unique en SVG ou PNG."""

    with open(MERMAID_JS, "r") as f:
        mermaid_js_content = f.read()

    html = f"""<!DOCTYPE html>
<html><head><script>{mermaid_js_content}</script>
<style>body {{ background: transparent; margin: 0; }}</style>
</head><body>
<div id="target"></div>
<div id="result" style="display:none"></div>
<script>
mermaid.initialize({{startOnLoad: false, theme: 'default',
                      securityLevel: 'loose'}});
async function render() {{
    try {{
        const {{ svg }} = await mermaid.render('diagram', `{diagram_code}`);
        document.getElementById('target').innerHTML = svg;
        document.getElementById('result').textContent = 'OK';
    }} catch(e) {{
        document.getElementById('result').textContent = 'ERROR: ' + e.message;
    }}
}}
render();
</script>
</body></html>"""

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True, executable_path=CHROME,
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
        )
        page = await browser.new_page()
        await page.set_content(html)
        await page.wait_for_timeout(3000)

        result = await page.evaluate(
            "document.getElementById('result').textContent")
        if result == 'OK':
            if format == "svg":
                svg = await page.evaluate(
                    "document.querySelector('#target svg').outerHTML")
                with open(output_path, "w") as f:
                    f.write(svg)
            else:
                target = page.locator('#target svg')
                await target.screenshot(path=output_path, type="png")

        await browser.close()
        return result == 'OK'
```

---

## Cas d'utilisation

Le pipeline sert trois domaines distincts, chacun exploitant la même capacité de rendu de base.

### 1. Diagnostics interactifs

Lorsqu'une page web rend incorrectement (diagrammes Mermaid cassés, problèmes de thèmes CSS, problèmes de mise en page bilingue), Claude peut rendre la page, voir le résultat réel et diagnostiquer le problème — le tout dans une même session.

**Flux de travail** :
1. L'utilisateur signale un problème de rendu (ou Claude le détecte via `pub check`)
2. Claude récupère et rend la page localement
3. Claude analyse la capture — identifie le problème visuellement
4. Claude propose et applique un correctif
5. Claude re-rend pour confirmer que le correctif fonctionne

**Exemple réel** : Issue #334 — les diagrammes sur la page FR Architecture Diagrams rendaient incorrectement. Claude a rendu la page, identifié que 13/14 diagrammes rendaient correctement (1 échoué à cause du conflit Liquid `{{ "{{" }}`, pas un problème de rendu), et l'utilisateur a confirmé : *« ça semble fonctionner le visual d'une page web »*.

### 2. Conception interactive

Pendant la construction itérative de pages web, Claude rend l'état courant d'une page pour valider la mise en page, le style et le contenu — sans que l'utilisateur ait besoin de rafraîchir un navigateur.

**Applications** :
- Valider que les pages miroir bilingues EN/FR rendent de façon identique
- Vérifier le support dual-thème (Cayman clair vs Midnight sombre)
- Vérifier le formatage des tableaux, le style des blocs de code, les liens de navigation
- Prévisualiser les nouvelles publications avant déploiement

### 3. Gestion documentaire

Génération d'artefacts visuels pour le pipeline documentaire : captures d'écran pour les publications, images de diagrammes pour l'exportation, rapports de validation visuelle.

**Applications** :
- Pré-rendu de diagrammes Mermaid pour le support dual-thème (`<picture>` avec PNG Cayman + Midnight)
- Conversion de diagrammes pour le pipeline d'exportation PDF/DOCX (Publication #13)
- Génération de captures visuelles pour les commentaires d'issues et descriptions de PR
- Validation du rendu des webcards et de l'affichage des images OG

---

## Préservation des sources Mermaid

Lorsque les diagrammes Mermaid sont pré-rendus en PNG, le code source original doit être préservé. Le supprimer brise la chaîne de génération documentaire.

### Le problème

| Sans la source | Avec la source préservée |
|----------------|--------------------------|
| Impossible de mettre à jour — doit redessiner | Modifier la source, re-rendre |
| Claude voit seulement des pixels | Claude lit et comprend l'architecture |
| Impossible de générer d'autres formats | La source alimente tout pipeline de rendu |
| Œuf et poule : besoin de la source supprimée | Complète — la source voyage avec le rendu |

### La solution : format hybride

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="diagram-midnight.png">
  <img src="diagram-cayman.png" alt="Diagramme">
</picture>

<details class="mermaid-source">
<summary>Source Mermaid</summary>
...
</details>
```

### Règles

1. Tout diagramme pré-rendu DOIT conserver sa source dans un `<details class="mermaid-source">`
2. Le résumé est « Mermaid source » (EN) ou « Source Mermaid » (FR)
3. Pour modifier un diagramme, éditer la source d'abord, puis re-rendre le PNG
4. La source Mermaid est la **source unique de vérité** — le PNG est un artefact dérivé

---

## Exclusion du pipeline web

Les blocs `<details class="mermaid-source">` sont **exclus du rendu web** sur GitHub Pages. Sans exclusion, kramdown traite les blocs Mermaid en éléments `<code class="language-mermaid">`, et le mermaid.js du layout tente de les rendre — causant trois modes de défaillance :

| Mode de défaillance | Impact |
|--------------------|--------|
| **Double rendu** | mermaid.js rend des diagrammes qui existent déjà en PNG |
| **Erreurs d'analyse** | Certaine syntaxe échoue dans le parser live — défaillance en cascade |
| **Contamination d'exportation** | Les pipelines PDF/DOCX captent les blocs Mermaid bruts |

### Mécanisme d'exclusion (deux couches)

| Couche | Action | Méthode |
|--------|--------|---------|
| **CSS** | Masque `.mermaid-source` de la page | `display: none !important` + `@media print` |
| **JavaScript** | Empêche mermaid.js de traiter les blocs préservés | `if (el.closest('.mermaid-source')) return;` |

### Matrice de visibilité

| Contexte | Visible? | Raison |
|---------|----------|--------|
| Vue source GitHub | **Oui** | `<details>` nativement dépliable |
| Diff git / revue PR | **Oui** | Le markdown brut montre la source |
| Claude / lecture IA | **Oui** | Le fichier markdown contient le code |
| GitHub Pages web | **Non** | Exclusion CSS + JS |
| Export PDF | **Non** | Règle `@media print` |
| Export DOCX | **Non** | Éléments cachés retirés |

---

## Contraintes et limitations

| Contrainte | Impact | Contournement |
|-----------|--------|---------------|
| **Proxy bloque `page.goto()`** | Navigation externe impossible | Récupérer via urllib, charger localement |
| **Références CSS/JS externes bloquent** | Délai d'expiration | HTML autonome |
| **Décalage de version Chromium** | Playwright attend binaire plus récent | Paramètre `executable_path` |
| **Scripts inline trop volumineux** | mermaid.js ~3 Mo trop gros pour `set_content()` | `page.add_script_tag(path=...)` |
| **Conflit Liquid `{{ "{{" }}`** | Jekyll retire les nœuds Mermaid hexagonaux | Rendu local évite Liquid |
| **jsdom manque SVG DOM** | `getBBox()` non implémenté | Utiliser Chromium |

---

## Découvertes clés

1. **Playwright + Chromium pré-installés** — décalage de version, mais `executable_path` le contourne
2. **npm mermaid nécessite un vrai DOM** — jsdom échoue sur SVG ; Chromium fournit un DOM complet
3. **urllib contourne le proxy** — même mécanisme que `gh_helper.py`
4. **HTML autonome est la clé** — retirer les refs externes, injecter le CSS en ligne
5. **mermaid.ink validé mais exclu** — API externe viole la qualité *autosuffisant*
6. **La source doit être préservée** — la supprimer crée un problème œuf-poule
7. **L'exclusion web est critique** — la source non-exclue cause des défaillances en cascade

---

## Résultats de validation

| Test | Résultat | Détails |
|------|----------|---------|
| Mermaid simple (graph TB) | OK | SVG 9,9 Ko |
| Mermaid complexe (flowchart TD, 12 nœuds, emojis) | OK | SVG 154 Ko, PNG 55 Ko |
| Page complète (14 diagrammes, FR) | 13/14 OK | 1 échoué : conflit Liquid |
| Capture pleine page | OK | 18 080 px hauteur, 2,5 Mo PNG |
| Captures par viewport | OK | 10 pages à 1280×900 |
| Exclusion pipeline web | OK | `.mermaid-source` masqué sur Pages, visible sur source |

---

## Sécurité par conception

Le pipeline applique la qualité *autosuffisant* à chaque couche :

| Principe | Application |
|----------|-------------|
| **Zéro service externe** | Pas de CDN, pas d'API, pas de service cloud |
| **Zéro réseau au rendu** | Seulement la récupération HTML optionnelle |
| **Outils pré-installés** | Playwright + Chromium pré-installés ; npm mermaid une fois par session |
| **Indépendant du proxy** | urllib contourne directement le proxy |
| **Aucune accréditation requise** | Pas de tokens, pas de clés API |
| **Reproductible** | Même environnement → même résultat |

---

## Publications connexes

| Pub | Titre | Relation |
|-----|-------|----------|
| #13 | [Pagination web et exportation]({{ '/fr/publications/web-pagination-export/' | relative_url }}) | Cible d'intégration — Mermaid vers image pour export DOCX |
| #14 | [Analyse d'architecture]({{ '/fr/publications/architecture-analysis/' | relative_url }}) | Source de contenu — la compréhension architecturale guide la conception |
| #15 | [Diagrammes d'architecture]({{ '/fr/publications/architecture-diagrams/' | relative_url }}) | Premier sujet de test — 14 diagrammes, dual-thème, préservation source |
| #5 | [Webcards et partage social]({{ '/fr/publications/webcards-social-sharing/' | relative_url }}) | Concept parallèle — artefacts visuels générés |
| #6 | [Normalize et concordance structurelle]({{ '/fr/publications/normalize-structure-concordance/' | relative_url }}) | Application — `normalize` vérifie la convention `.mermaid-source` |
