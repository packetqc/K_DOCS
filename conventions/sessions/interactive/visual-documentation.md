# Visual Documentation — Convention

> Adapted from `packetqc/knowledge:knowledge/methodology/methodology-documentation-visual.md`

Automated evidence extraction from video recordings for documentation. Processes video files using computer vision to extract significant frames — no external services, no cloud APIs, standard libraries only.

## Technology Stack

| Library | Role |
|---------|------|
| **OpenCV** (cv2) | Video decoding, frame extraction, image processing |
| **Pillow** (PIL) | Image annotation, format conversion, contact sheets |
| **NumPy** | Array operations (OpenCV dependency) |
| **Python stdlib** | pathlib, datetime, json, urllib, tempfile, hashlib |

**Constraint**: No external tools (no ffmpeg CLI, no cloud vision APIs). All processing via Python library calls.

## Operating Modes

| Mode | Purpose | Input |
|------|---------|-------|
| **Timestamp** | Extract at known points | `--timestamps 10 30 60` or `--times 00:01:30` |
| **Detection** | Auto-find significant frames | `--sensitivity 0.35 --max-frames 50` |
| **Search** | Multi-criteria multi-pass scan | `--scene-change --min-text 0.15` |
| **Clip** | Extract video segment | `--clip 45.0 --context 10` |
| **Image** | Single image analysis | `--image screenshot.png` |

### Detection Heuristics

| Detector | What it finds | Threshold |
|----------|--------------|-----------|
| Scene change | Major visual transitions (histogram correlation) | `< 1.0 - sensitivity` |
| Text density | Documentation-relevant frames (adaptive threshold) | `> 0.15` |
| Edge density | Diagrams, tables, code, UI (Canny edge) | `> 0.12` |
| Structured content | Tables, grids, forms (line detection) | `> 0.08` |

## Evidence Structure

```
evidence/<session-name>/
  metadata.json          — source info, criteria, findings count
  discoveries/           — extracted evidence frames
  clips/                 — reconstructed video segments
  index.md               — markdown inventory
```

## Deduplication

DCT-based perceptual hashing: resize 64x64 grayscale → DCT → 16x16 low-freq → binary threshold → Hamming distance. Default: 0.92 similarity = duplicate.

## Integration

| Aspect | Live Session | Visual Documentation |
|--------|-------------|---------------------|
| **Timing** | Real-time (during recording) | Post-hoc (after recording) |
| **Input** | Live RTSP stream clips | Video files (local or GitHub) |
| **Output** | Immediate diagnostic report | Evidence frames + report + sheet |

## Scripts

- `visual_engine.py` — Core processing engine (VideoInfo, EvidenceSession, extract/detect/search)
- `visual_cli.py` — CLI entry point (argparse dispatcher)

## Safety Limits

| Limit | Value |
|-------|-------|
| Max video duration | 7200s (2h) |
| Max detection frames | 50 |
| Min detection interval | 1s (configurable) |
| Dedup threshold | 0.92 (configurable) |
