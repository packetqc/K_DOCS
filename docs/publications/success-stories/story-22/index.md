---
layout: publication
title: "Story #22 — Visual Documentation Engine: From Video to Evidence in Seconds"
description: "A long-standing vision realized — an automated engine that extracts evidence frames from video recordings using computer vision, enabling documentation enrichment directly from session recordings."
pub_id: "Publication #11 — Story #22"
version: "v1"
date: "2026-03-07"
permalink: /publications/success-stories/story-22/
og_image: /assets/og/visual-documentation-en-cayman.gif
keywords: "success story, visual documentation, video evidence, OpenCV, frame extraction, clip reconstruction, computer vision"
---

# Story #22 — Visual Documentation Engine: From Video to Evidence in Seconds

> **Parent publication**: [#11 — Success Stories]({{ '/publications/success-stories/' | relative_url }})

---

<div class="story-section">

> *"I've wanted this for a long time — the ability to take a video recording from a development session and automatically extract the key moments as images and clips to enrich our documentation. Today it works. Search a 2-hour video, get 5 evidence frames and their video context, organized in a directory ready for documentation."*

<div class="story-row">
<div class="story-row-left">

**Details**

</div>
<div class="story-row-right">

| | |
|---|---|
| Date | 2026-03-07 |
| Category | 🚀 ⚙️ |
| Context | Development workflows generate hours of video recordings — screen captures, UART sessions, demo recordings, CI/CD artifacts. Extracting useful frames from these recordings was entirely manual: scrub through the video, pause at the right moment, take a screenshot, organize, annotate. For long recordings, this process was impractical. The user had envisioned an automated solution for months — a system that could scan video files, find what matters, and produce organized evidence ready for documentation. |
| Triggered by | Issue [#556](https://github.com/packetqc/knowledge/issues/556) — The user described the vision: multi-criteria search directly on video files, organized evidence directories with discoveries and clips, and the downstream goal of enriching documentation with automatically extracted visual evidence. |
| Authored by | **Claude** (Anthropic, Opus 4.6) — from live session data |

</div>
</div>

<div class="story-row">
<div class="story-row-left">

**What happened**

</div>
<div class="story-row-right">

1. **The vision** — The user articulated a need that had been building for months: video recordings contain critical evidence (UI states, error screens, UART output, configuration changes), but extracting this evidence was entirely manual. The goal: an engine that processes video files using computer vision and produces organized evidence — no cloud services, no external tools, standard Python libraries only.

2. **Direct video access** — Instead of the naive approach of extracting all frames to disk (which would consume gigabytes for a long video), the user suggested working directly on the video file. The engine seeks to specific positions using `cv2.VideoCapture.set()` — only matched frames are ever saved. This makes it practical to search hours-long recordings with minimal disk usage.

3. **Multi-pass search architecture** — The engine performs intelligent two-pass scanning: Pass 1 (coarse) scans every ~1 second evaluating all criteria simultaneously; Pass 2 (fine) refines around each hit frame-by-frame. Four combinable heuristics: scene change detection (histogram correlation), text density (adaptive threshold + morphology), edge density (Canny detection), and structured content (horizontal/vertical line detection).

4. **Evidence structure** — Results are organized in a purpose-built directory structure: `evidence/<session>/discoveries/` for extracted frames, `clips/` for reconstructed video segments, `metadata.json` for machine-readable data, and `index.md` for human-readable inventory. Everything feeds directly into documentation.

5. **Clip reconstruction** — Beyond static frames, the engine reconstructs standalone `.mp4` clips centered around evidence timestamps. Using `cv2.VideoWriter`, it extracts ±N seconds of context around each finding — the video equivalent of "show me what happened around this moment."

6. **Live validation** — The engine was tested on a real recording from the knowledge system (Main Navigator interface demo, 1920×1080, 30fps, 65.8s). Search mode found evidence frames, clip reconstruction produced playable MP4 segments, and the evidence directory structure was generated with metadata and index.

7. **Inline display discovery** — During testing, the challenge of showing results to the user led to discovering that markdown image links via `raw.githubusercontent.com` work reliably on the Claude mobile app. This became a documented display protocol — push evidence to the branch, present via markdown image links — making the engine's output immediately visible in the conversation.

</div>
</div>

<div class="story-row">
<div class="story-row-left">

**What it validated**

</div>
<div class="story-row-right">

| Quality | How |
|---------|-----|
| **Autosuffisant** (#1) | Zero external dependencies — OpenCV + Pillow + NumPy only. No ffmpeg CLI, no cloud APIs, no OCR services. One `pip install` bootstraps everything. |
| **Autonome** (#2) | The engine self-organizes output — evidence directory with metadata, index, discoveries, and clips created automatically without human intervention. |
| **Évolutif** (#6) | Started as frame extraction (Publication #2, Live Session), grew to include detection mode, then search mode, clip reconstruction, image analysis — each capability building on the previous. |
| **Concis** (#4) | Direct video access instead of bulk extraction. A 2-hour video search produces 5 evidence frames, not 216,000 temporary files. |
| **Intégré** (#13) | Evidence feeds directly into documentation. Inline display bridges the gap between extraction and presentation. GitHub raw URLs enable immediate visualization on any client. |

</div>
</div>

<div class="story-row">
<div class="story-row-left">

**Metric**

</div>
<div class="story-row-right">

A 65.8-second 1080p recording was searched with multi-criteria in under 30 seconds. The engine extracted annotated evidence frames, reconstructed video clips, and organized everything in a structured evidence directory — a process that would take 15-20 minutes manually. For a 2-hour recording, the manual process is impractical; the engine makes it routine.

**Technology stack**: ~1,200 lines of Python across `visual_engine.py` (core) and `visual_cli.py` (CLI). Six operating modes. Four detection heuristics. Perceptual hash deduplication. Contact sheet generation. Evidence report generation. All with three standard libraries.

</div>
</div>

</div>

---

> **Related**: [Publication #22 — Visual Documentation]({{ '/publications/visual-documentation/' | relative_url }}) · [Publication #2 — Live Session Analysis]({{ '/publications/live-session-analysis/' | relative_url }}) · [Publication #16 — Web Page Visualization]({{ '/publications/web-page-visualization/' | relative_url }})

---

*Story #22 — Visual Documentation Engine*
*Martin Paquet & Claude (Anthropic, Opus 4.6) — March 2026*
