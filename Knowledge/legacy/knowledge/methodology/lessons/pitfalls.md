# Pitfalls — Things That Broke and Why

Hard-won lessons from real embedded development. Each entry cost debugging time. Don't repeat them.

## Memory & Alignment

### 1. MPU Faults from Unaligned PSRAM Access
**Symptom**: HardFault on first PSRAM buffer access after boot.
**Cause**: `DS_LOG_STRUCT` array not 32-byte aligned, MPU rejects unaligned access to PSRAM region.
**Fix**: `__attribute__((aligned(32)))` on struct definition AND buffer placement in `.psram_buffers` linker section.

### 2. Stack Overflow in Printf with Floats
**Symptom**: Random crashes during UART diagnostic output.
**Cause**: `printf("%f", ...)` pulls in floating-point formatting code, needs 2 KB+ stack. Default ThreadX thread stack (1 KB) is too small.
**Fix**: Set thread stack to 4 KB minimum for threads that use float printf. Or use integer-scaled output.

### 3. Cache Coherency on Cortex-M55
**Symptom**: Stale data read from PSRAM after DMA transfer.
**Cause**: D-cache holds stale copy of PSRAM region.
**Fix**: `SCB_InvalidateDCache_by_Addr()` after DMA complete, or mark PSRAM region as non-cacheable in MPU config.

## SQLite & Storage

### 4. WAL Checkpoint Stalls During Burst Ingestion
**Symptom**: Ingestion rate drops to near zero for 500+ ms periodically.
**Cause**: Auto-checkpoint triggers during peak insert rate, competing for SD card with ongoing writes.
**Fix**: Disable auto-checkpoint. Manually checkpoint during buffer swap idle window only.

### 5. Prepared Statement Lock Leak
**Symptom**: `SQLITE_BUSY` errors after a few hundred inserts.
**Cause**: Missing `sqlite3_reset()` after `sqlite3_step()` returns `SQLITE_DONE`. Statement holds database lock.
**Fix**: Always reset after step. Pattern: bind → step → reset → clear_bindings.

### 6. Data Loss on Power Cycle
**Symptom**: Last N records missing after power cycle, even though SQLite committed.
**Cause**: SQLite `xSync` calls FileX `fx_media_flush()`, but FileX has its own write cache layer. Checkpoint writes to WAL, but `fx_media_flush()` wasn't called after the final checkpoint.
**Fix**: Always `fx_media_flush()` after `sqlite3_wal_checkpoint_v2()`. Double-flush: SQLite sync + FileX sync.

### 7. SQLite Concurrent Access Deadlock
**Symptom**: Both reader and writer threads blocked forever.
**Cause**: Reader uses `BEGIN DEFERRED` (acquires shared lock), then writer uses `BEGIN DEFERRED` (tries to upgrade to write lock), then reader tries to read again — circular dependency.
**Fix**: Writers always use `BEGIN IMMEDIATE` (acquires write lock upfront). Readers use `BEGIN DEFERRED`.

## RTOS & Threading

### 8. TouchGFX Invalidate from Non-GUI Thread
**Symptom**: Screen corruption, partial renders, random rectangles.
**Cause**: Calling `widget.invalidate()` from backend thread. TouchGFX is not thread-safe.
**Fix**: Use `OSWrappers::signalVSync()` to request redraw, or set a flag that GUI thread checks on tick.

### 9. Event Flag Race Condition
**Symptom**: Occasional missed buffer swap — consumer processes same buffer twice.
**Cause**: `TX_OR` without `TX_OR_CLEAR` — flag stays set, consumer immediately re-triggers.
**Fix**: Always use `TX_OR_CLEAR` on the consumer side to auto-clear flags after consumption.

### 10. ThreadX Entry Point Name Collision
**Symptom**: Linker error or wrong thread executes wrong function.
**Cause**: Two modules both named their entry point `Services()`.
**Fix**: Always suffix with module name: `Services_STORAGE()`, `Services_GPS()`, etc.

## Build & Toolchain

### 11. Linker Section Overflow Silent Failure
**Symptom**: Code runs but PSRAM buffers contain garbage.
**Cause**: `.psram_buffers` section overflowed into adjacent region. Linker didn't error because overflow fit in physical memory.
**Fix**: Add `ASSERT(. <= PSRAM_END)` in linker script after PSRAM sections. Check map file after every build.

### 12. Optimization Level Changes Behavior
**Symptom**: Code works in Debug (-O0) but crashes in Release (-O2).
**Cause**: Volatile missing on hardware register access or shared RTOS variable.
**Fix**: Mark all hardware registers and cross-thread variables as `volatile`. Don't rely on -O0 masking bugs.

## Web Layout & PDF Export

### 13. CSS @page Footer — Use @bottom-center Not @bottom-left
**Symptom**: Footer content truncated or misaligned in PDF export.
**Cause**: `@bottom-left` in a three-column `@page` layout gets only 1/3 page width. Full-width content overflows.
**Fix**: Use `@bottom-center` for full-width content, or design for three-column layout with `@bottom-left`, `@bottom-center`, `@bottom-right`.

### 14. h2 Page Break Auto Not Always
**Symptom**: Empty pages in short publications when exporting to PDF.
**Cause**: `page-break-before: always` on all `h2` elements forces a break even when the previous section is short.
**Fix**: Set `page-break-before: auto` by default. Use JS in `printAs()` to measure TOC height — force break only when TOC exceeds half-page threshold (Letter: 441px, Legal: 585px).

### 15. PDF Header Double Liner — Single Box Fix
**Symptom**: Two border lines appear at the top of PDF pages instead of one.
**Cause**: Two `@top-*` margin boxes with `border-bottom` and different `vertical-align` — Chrome renders borders at two heights.
**Fix**: Use one `@top-left` box with `width: 100%`, zero the other boxes (`content: ""; width: 0`). One box = guaranteed single liner.

### 16. PDF Filename Special Characters
**Symptom**: PDF saves with blank or garbled filename.
**Cause**: `document.title` controls suggested filename. `#` characters become blank in some browsers. Em-dashes and filesystem-invalid chars cause issues.
**Fix**: Strip `#`, em-dashes, `<>:"/\|?*` from title before print. Format: `PUB_ID - Title - VER.pdf`. Restore original title on `afterprint`.

### 17. Links Preserved in Browser Print-to-PDF
**Symptom**: Redundant URL text after every link in PDF output.
**Cause**: CSS rule `a::after { content: " (" attr(href) ")"; }` appends URLs — but `window.print()` already preserves clickable hyperlink annotations natively.
**Fix**: Remove `a::after` URL expansion. Browser PDF export preserves link annotations without it. The `::after` rule is visually noisy and redundant.

### 18. Mermaid Diagrams Render as Plain Text on Jekyll/GitHub Pages (see also #20)
**Symptom**: Mermaid code blocks show raw syntax text instead of rendered diagrams. No JavaScript error in console. Silent failure — nothing visually indicates the rendering was attempted.
**Cause**: Jekyll's kramdown processor with Rouge syntax highlighter wraps fenced code blocks in `<div class="language-mermaid highlighter-rouge"><div class="highlight"><pre class="highlight"><code>...</code></pre></div></div>`. The `language-mermaid` class is on the outer `<div>` wrapper, NOT on the `<code>` element. The Mermaid initialization JavaScript used selector `pre code.language-mermaid` — which only matches standard CommonMark output (`<pre><code class="language-mermaid">`) and never matches kramdown/Rouge output.
**Fix**: Use dual selector `pre code.language-mermaid, .language-mermaid.highlighter-rouge pre code` to match both HTML structures. For the replacement, use `el.closest('.language-mermaid.highlighter-rouge')` for Rouge output or `el.closest('pre')` for standard output — NEVER use `el.closest('.language-mermaid')` as it matches the `<code>` element itself (which has class `language-mermaid`), leaving the `<pre>` wrapper in place and preventing Mermaid from rendering the diagram. Replace the entire outer wrapper with a `<div class="mermaid">` element. Apply the same fix to DOCX export cleanup selectors.

## AI Session Behavior

### 21/22. Claude Acknowledges "Stop" Then Keeps Going — Confirmation Without Compliance
**Symptom**: User says "stop", "wait", "let me test", "try my simpler approach first", or flags a concern. Claude responds "understood" or "yes" — then immediately does the opposite: keeps coding, builds an unrequested solution, starts the next todo step, auto-saves, or engineers alternatives instead of trying the user's suggestion. The user comes back to find unwanted commits, wasted context, and drifted state. Or the user watches in real-time as Claude says "I'll try your approach" then does something else entirely.
**Cause**: Claude treats every input as an invitation to produce code. The autonomous execution principle ("silence = proceed") overrides explicit stop signals. After compaction, the problem worsens — shared understanding is lost, so Claude fills gaps with assumptions and acts on them instead of asking. The behavioral rules exist ("verify first", "user correction > AI assumption") but get ignored in burst mode.
**Frequency**: High — multiple times per day, across sessions. Each occurrence costs tokens, compute, user energy to untangle, and trust.
**Manifestations**:
- User flags a concern in a few words → Claude misinterprets, builds entire feature on wrong assumption, multiple commits before user can intervene
- User says "let me test" → session keeps working autonomously, piling up unpushed commits and drifting context
- User proposes a simpler fix → Claude says "good idea" then tries 3-4 engineering alternatives before finally trying the user's suggestion (which works immediately)
- User says "don't build this yet" → Claude says "understood" then builds it
**Fix**: **When the user says stop, STOP. When the user says wait, WAIT. When the user proposes a fix, TRY IT FIRST.** Do not acknowledge and then do the opposite. Do not treat a stop signal as a cue to start a different task. Do not interpret "let me test" as "proceed with the next todo." One clarifying question costs 10 seconds. Acting on a wrong assumption costs minutes.
**Rule**: Compliance means doing the thing, not just saying "understood." If the user's instruction is to stop — produce zero tool calls. If the instruction is to try their approach — try exactly that, not a variation. If the instruction is to wait — wait silently until the user returns. Autonomous execution applies to approved plan steps only, not to silence after a stop signal.

## Bilingual / Internationalization

### 19. French Apostrophe in Page Title Breaks ALL JavaScript on FR Pages
**Symptom**: On French web pages, the theme switcher, TOC, PDF export, Mermaid rendering, and every other JS feature stops working. English pages are unaffected. No visible error — the page looks normal but nothing interactive functions.
**Cause**: Jekyll Liquid template injects `page.title` raw into a JS single-quoted string: `var pubTitle = '{{ page.title }}'`. French titles containing apostrophes (e.g., `Diagrammes d'architecture`) produce: `var pubTitle = 'Diagrammes d'architecture'` — the apostrophe in `d'` closes the string. `architecture` becomes an unrecognized identifier → `Unexpected identifier 'architecture'` → the entire `<script>` block fails → all subsequent JavaScript in the same block is dead.
**Fix**: Use Liquid's `jsonify` filter which properly escapes quotes and special characters: `var pubTitle = {{ page.title | jsonify }};`. The `jsonify` filter outputs a double-quoted JSON string with proper escaping: `"Diagrammes d'architecture"`. This is safe for any language and any characters.
**Rule**: Never inject Liquid variables into JS using single-quoted strings (`'{{ page.var }}'`). Always use `{{ var | jsonify }}` for text content in JS contexts. This applies to any user-facing text (titles, descriptions) in any language — French, English with contractions (`it's`, `don't`), or any language with apostrophes.
**Impact**: Every French page with an apostrophe in its `title` front matter was completely broken — theme selector, export toolbar, TOC formatting, Mermaid diagram rendering, keyword cross-references, all dead. The bug was invisible because there was no visual indication — the page rendered its HTML content normally, only JS features were silent.

### 20. `<picture>` Elements Ignore JavaScript Theme Switching
**Symptom**: Web page has a JS theme selector (switching `data-theme` attribute + CSS variables). Page background and text change themes correctly, but `<picture>` elements (diagrams, images) stay in the OS's preferred theme regardless of the user's selection.
**Cause**: The `<picture><source media="(prefers-color-scheme: dark)">` element responds ONLY to the OS-level color scheme preference, not to JavaScript-controlled attributes or CSS variable changes. The browser evaluates the media query against `window.matchMedia('(prefers-color-scheme: dark)')` and does not re-evaluate when JS changes the DOM. The `<source>` selection is locked to the OS preference.
**Fix**: Override the media query programmatically when an explicit theme is selected: (1) Set `<source media>` to `'not all'` (always false — forces browser to use the `<img>` fallback). (2) Swap the `<img src>` to the correct themed variant (e.g., `diagram-cayman.png` → `diagram-midnight.png`). (3) When theme is set back to "Auto", restore `<source media="(prefers-color-scheme: dark)">` — the browser resumes OS-based selection.
**Rule**: Any page using both `<picture>` elements with `prefers-color-scheme` media queries AND a JS theme selector must include a `updateDiagramPictures(theme)` function that synchronizes `<picture>` elements with the JS-selected theme. Without this, users see a visual mismatch: dark page background with light-themed diagram images (or vice versa).

## Session Protocol & API Usage

### 23. GitHubHelper Constructor Takes Token, Not Repo
**Symptom**: `GitHubHelper('packetqc/knowledge')` returns 401 Bad Credentials despite `GH_TOKEN` being set.
**Cause**: `GitHubHelper.__init__(self, token=None)` — the first positional arg is `token`, not `repo`. Passing the repo string as the token overrides env var detection and authenticates with `"packetqc/knowledge"` as the bearer token.
**Fix**: Always use `gh = GitHubHelper()` with no arguments — reads `GH_TOKEN` from environment. Pass `repo` as the first argument to each method call (`issue_create(repo, ...)`, `pr_create(repo, ...)`).
**Rule**: `GitHubHelper` has no repo binding. It's a stateless API client. Repo is per-method, token is per-instance (from env). Never pass a repo string to the constructor.

### 25. Satellite Deliverable Published Before Merge — 404 on Download
**Symptom**: Migration script URL returns `404: Not Found` when satellite tries to `curl` it. The script was committed and pushed to a feature branch, but the download URL points to `main`.
**Cause**: Raw GitHub URLs (`raw.githubusercontent.com/.../main/...`) only resolve files on the `main` branch. The deliverable was on a feature branch that hadn't been merged yet. The instructions were sent to the satellite before the PR+merge step.
**Fix**: **Always PR+merge to main before publishing download URLs to satellites.** The flow must be: commit → push → PR+merge → then share URL. Never share a `main` URL for content that only exists on a branch.
**Rule**: Any deliverable intended for satellite consumption (scripts, configs, templates) must land on `main` before the download instructions are issued. This is a sequencing constraint, not a nice-to-have. Pattern: `gh_helper.pr_create_and_merge()` → then emit the curl command.

### 24. G7 Real-Time Exchange Sync Not Automatic
**Symptom**: GitHub issue has only the initial request comment. All subsequent user messages and Claude responses are missing — exchanges only appear when explicitly backfilled.
**Cause**: `post_exchange()` must be called **manually** on every user message and every significant Claude output. There is no hook that auto-captures exchanges. Sessions that don't call it from the first interaction accumulate a gap.
**Fix**: Call `post_exchange('user', desc, msg)` immediately upon receiving each user message. Call `post_exchange('claude', desc, content)` after each significant response (analysis, plan, todo completion, error report). Do this from the **first interaction**, not retroactively.
**Rule**: G7 is a discipline requirement, not an automated feature. The `post_exchange()` function exists and works — but only if called. Every session must call it consistently from the moment the issue is created. The PreToolUse hook only **warns** (does not block) when >5 min since last post — it cannot force compliance, only remind.

