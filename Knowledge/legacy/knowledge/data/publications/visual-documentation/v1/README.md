# Visual Documentation — Publication Documentation

**Publication #22 — Automated Documentation from Video Recordings**

*By Martin Paquet & Claude (Anthropic, Opus 4.6)*
*v1 — March 2026*

---

## Authors

**Martin Paquet** — Network Security Analyst Programmer, Network and System Security Administrator, Embedded Software Designer and Programmer. 30 years of experience spanning embedded systems, network security, telecom, and software development. Autodidact and builder by nature.

**Claude** (Anthropic, Opus 4.6) — AI development partner. Implemented the visual processing engine, detection algorithms, and CLI interface using standard Python libraries only.

---

## Abstract

This publication documents the **Visual Documentation Engine** — an automated system for extracting evidence frames from video recordings to create, update, and review documentation. The engine uses exclusively standard, recognized Python libraries (OpenCV, Pillow, NumPy) with no external tools, no cloud services, and no CLI dependencies.

The capability addresses a recurring need in development workflows: converting video recordings (screen captures, UART sessions, demo recordings) into structured visual evidence for documentation. Instead of manually scrubbing through video and taking screenshots, the `visual` command automates the entire pipeline:

1. **Timestamp mode** — Extract frames at specific times (seconds, HH:MM:SS, or full date-times)
2. **Detection mode** — Automatically scan video for significant frames using computer vision heuristics (scene changes, text density, edge density, structured content)
3. **Search mode** — Multi-criteria, multi-pass search directly on the video file — no bulk frame extraction, works on hours-long recordings with minimal disk usage
4. **Clip reconstruction** — Extract video segments (±N seconds context) around evidence for documentation
5. **Image analysis** — Evaluate single images for evidence matching using the same heuristics
6. **Output pipeline** — Annotated frames, perceptual hash deduplication, contact sheets, evidence reports, and organized evidence directories

The engine is part of the **Visuals** command category — a category that regroups all recording-related calls from the Knowledge System, alongside the existing `deep` and `analyze` commands from Live Session Analysis.

---

## Table of Contents

- [Target Audience](#target-audience)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Operating Modes](#operating-modes)
- [Detection Algorithms](#detection-algorithms)
- [Output Pipeline](#output-pipeline)
- [Integration](#integration)
- [Usage Examples](#usage-examples)
- [Related Publications](#related-publications)

---

## Target Audience

| Audience | Value |
|----------|-------|
| **Developers** | Automated evidence capture from session recordings |
| **QA Engineers** | Visual regression detection across test recordings |
| **Technical Writers** | Automated screenshot extraction for documentation |
| **AI-assisted workflows** | Claude sessions processing video evidence programmatically |

---

## Architecture

### Design Constraints

| Constraint | Rationale |
|------------|-----------|
| **No external tools** | No ffmpeg CLI, no ImageMagick, no cloud APIs |
| **Standard libraries only** | OpenCV (4.x), Pillow (12.x), NumPy (2.x), Python stdlib |
| **Self-contained** | One `pip install` bootstraps all dependencies |
| **Portable** | Runs in any Python 3.11+ environment (containers, WSL, native) |

### Module Structure

```
scripts/
├── visual_engine.py    # Core processing engine
│   ├── VideoInfo / EvidenceSession  — Metadata + evidence structure
│   ├── Timestamp extraction (3 input formats)
│   ├── Detection engine (4 heuristics)
│   ├── search_video()        — Multi-criteria, multi-pass search
│   ├── reconstruct_clip()    — Video segment extraction
│   ├── analyze_image()       — Single image evidence analysis
│   ├── Contact sheet + evidence report generation
│   ├── GitHub video fetching
│   └── Perceptual hash deduplication
│
└── visual_cli.py       # CLI entry point (argparse)
    ├── Argument parsing (7 mode groups)
    ├── Source resolution (local/GitHub/image)
    ├── Execution pipeline (timestamp/detect/search/clip/image)
    └── Output formatting (text/JSON/search summary)
```

---

## Technology Stack

### OpenCV (cv2) — Video Processing Core

- **Video decoding**: `cv2.VideoCapture` reads all major codecs (H.264, H.265, VP8/VP9)
- **Frame extraction**: Seek to any position via `CAP_PROP_POS_FRAMES`
- **Image processing**: Color space conversion, histogram analysis, edge detection
- **Morphological operations**: Text region detection, structure identification

### Pillow (PIL) — Image Output

- **Contact sheet generation**: Grid layout with thumbnails and metadata labels
- **Font rendering**: DejaVu font family for annotations
- **Format conversion**: PNG output for all evidence frames

### NumPy — Numerical Operations

- **Array operations**: Frame data manipulation (OpenCV native format)
- **DCT computation**: Perceptual hashing for deduplication
- **Statistical analysis**: Histogram comparison, threshold computation

---

## Operating Modes

### Timestamp Mode

Three input formats for when you know when the evidence occurred:

| Format | CLI Flag | Input Example |
|--------|----------|---------------|
| Seconds | `--timestamps` | `10.5 30.0 60.0` |
| Clock time | `--times` | `00:01:30 00:05:00` |
| Date-time | `--dates` | `"2026-03-01 14:30:00"` |

Optional offset calculation with `--video-start` or `--video-start-datetime`.

### Detection Mode

Four computer vision heuristics scan the video for significant frames:

| Heuristic | Signal | Method | Threshold |
|-----------|--------|--------|-----------|
| **Scene change** | Major visual transitions | Histogram correlation | `< 1.0 - sensitivity` |
| **Text density** | Documentation content | Adaptive threshold + morphology | `> 0.15` |
| **Edge density** | Diagrams, UI, code | Canny edge detection | `> 0.12` |
| **Structured content** | Tables, grids, forms | H/V line detection | `> 0.08` |

Parameters: `--sensitivity` (0-1), `--interval` (seconds), `--max-frames` (cap).

### Search Mode (Multi-Criteria, Multi-Pass)

Intelligent search directly on the video — no bulk frame extraction. Two-pass architecture:

| Pass | Strategy | Speed |
|------|----------|-------|
| **Coarse** | Scan every ~1 second, evaluate all criteria | Fast |
| **Fine** | Frame-by-frame refinement around each hit (±0.5s) | Precise |

Combinable criteria:

| Criterion | Flag | Description |
|-----------|------|-------------|
| Scene changes | `--scene-change` | Major visual transitions |
| Text density | `--min-text 0.15` | Frames with text content |
| Edge density | `--min-edge 0.12` | Diagrams, tables, UI |
| Structured content | `--structured` | Tables, grids, forms |
| Time ranges | `--time-range 30 60` | Restrict search scope |

**Key design**: Instead of extracting frames to disk (gigabytes for long video), the engine seeks directly in the video file via `cv2.VideoCapture.set()`. Only matched frames are saved.

### Clip Reconstruction

Extract a standalone `.mp4` video segment centered around a timestamp:
```bash
visual recording.mp4 --clip 45.0 --context 10
```
Produces a clip from `[center - context, center + context]` using `cv2.VideoWriter`. Automatic in search mode (clips generated for each finding).

### Image Analysis

Analyze a single image with the same heuristics as video detection:
```bash
visual --image screenshot.png
```
Returns scores (text density, edge density, structured content) and a boolean evidence assessment. Optional annotated output with scores overlay.

### Evidence Directory Structure

When using `--evidence`, results are organized:
```
evidence/<session-name>/
  metadata.json          — source, criteria, timestamps
  discoveries/           — evidence frames (only the hits)
  clips/                 — reconstructed video segments
  index.md               — markdown inventory
```

---

## Detection Algorithms

### Scene Change Detection

```
1. Convert frame to grayscale
2. Compute 256-bin histogram
3. Normalize histogram
4. Compare with previous frame using cv2.HISTCMP_CORREL
5. If correlation < (1.0 - sensitivity) → scene change detected
```

### Text Density Estimation

```
1. Apply adaptive Gaussian threshold (inverted, block=15, C=10)
2. Morphological close with 5x2 rectangular kernel (connect characters)
3. Count non-zero pixels as fraction of total
4. If ratio > 0.15 AND frame differs from previous → text frame detected
```

### Edge Density Estimation

```
1. Apply Canny edge detection (thresholds: 50, 150)
2. Count edge pixels as fraction of total
3. If ratio > 0.12 → high information density frame
```

### Structured Content Detection

```
1. Apply Canny edge detection
2. Morphological open with 40x1 kernel (detect horizontal lines)
3. Morphological open with 1x40 kernel (detect vertical lines)
4. Combine horizontal + vertical → structured content regions
5. If combined ratio > 0.08 → structured content detected
```

---

## Output Pipeline

### Frame Annotation

Each extracted frame receives an optional overlay:
- **Bottom bar**: Semi-transparent black bar with timestamp (HH:MM:SS.mmm) and source info
- **Detection badge**: Green badge with detection reason (top-left, detection mode only)
- **Corner marks**: Green evidence indicator marks at all four corners

### Deduplication

Perceptual hashing (pHash) removes near-identical frames:
1. Resize to 64x64 grayscale
2. Apply DCT (Discrete Cosine Transform)
3. Extract 16x16 low-frequency block
4. Binary threshold at median value
5. Compare Hamming distance between consecutive frames
6. Skip frames with similarity > threshold (default: 0.92)

### Contact Sheet

Thumbnail grid (configurable columns, default: 4) with header and per-frame labels showing timestamp and detection reason.

### Evidence Report

Markdown document with: video metadata, summary table (timestamp/frame/reason/hash), per-frame detail sections with embedded image references.

---

## Integration

### Visuals Command Category

The `visual` command belongs to the **Visuals** category — a new command group that regroups all recording analysis tools:

| Command | Origin | Description |
|---------|--------|-------------|
| `visual` | **New** | Automated evidence extraction (this publication) |
| `deep` | Live Session | Frame-by-frame anomaly analysis |
| `analyze` | Live Session | Static video analysis with state timeline |

Real-time capture commands (`I'm live`, `pause`, `resume capture`, `multi-live`, `recipe`) remain in the Live Session category.

### Knowledge Asset Sync

Both `visual_engine.py` and `visual_cli.py` are synced to satellite projects on wakeup (like `gh_helper.py` and other portable tools).

### GitHub Video Fetching

Videos can be fetched directly from any GitHub repository:
```bash
visual --repo packetqc/stm32-poc --file live/dynamic/clip_0.mp4 --detect
```

Uses `raw.githubusercontent.com` with automatic main/master fallback and optional GH_TOKEN authentication.

---

## Usage Examples

### Post-Session Evidence Collection

```bash
# After a development session recording, extract key moments
visual session_recording.mp4 --detect --dedup --report --sheet \
  --title "Sprint 12 Demo Evidence" \
  --description "UI flow demonstration for stakeholder review"
```

### Targeted Timestamp Extraction

```bash
# Extract frames at known bug reproduction timestamps
visual bug_repro.mp4 --timestamps 12.5 45.0 67.3 --title "Bug #123 Evidence"
```

### GitHub Repository Video Analysis

```bash
# Analyze test recording from CI/CD artifact repo
visual --repo packetqc/stm32-poc --file recordings/test_run_042.mp4 \
  --detect --subjects "UART" "error" "timeout" --report
```

---

## Related Publications

| # | Publication | Relationship |
|---|-------------|--------------|
| #0 | Knowledge System | Parent — Visuals is a new command category |
| #2 | Live Session Analysis | Sibling — real-time capture vs post-hoc analysis |
| #16 | Web Page Visualization | Sibling — web rendering pipeline (Playwright) |
| #19 | Interactive Work Sessions | Framework — Visual fits the feature development session type |

---

## Methodology

Full specification: [`methodology/visual-documentation.md`](../../../methodology/visual-documentation.md)

---

*Knowledge System Publication #22 — Visual Documentation*
*Martin Paquet & Claude (Anthropic) — March 2026*
