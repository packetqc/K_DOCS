---
layout: publication
title: "Live Session Analysis — AI-Assisted Real-Time Debugging for Embedded Systems"
description: "Real-time QA methodology: live video capture of running STM32 board → AI frame analysis → anomaly detection → forensic investigation. 4 modes: live, static, multi-live, hybrid deep."
pub_id: "Publication #2"
version: "v1"
date: "2026-02-19"
permalink: /publications/live-session-analysis/
og_image: /assets/og/live-session-en-cayman.gif
keywords: "live session, video analysis, UART, frame extraction, OBS, real-time"
---

# Live Session Analysis — AI-Assisted Real-Time Debugging and QA for Embedded Systems
{: #pub-title}

**Contents**

| | |
|---|---|
| [Abstract](#abstract) | Live debugging mechanism overview |
| [The Pipeline](#the-pipeline) | End-to-end capture and analysis flow |
| [Four Analysis Modes](#four-analysis-modes) | Live, static, multi-live, and hybrid deep |
| [Proven Results](#proven-results) | Bugs found and 3x speed compression |

## Abstract

A live session analysis mechanism for real-time debugging and quality assurance of embedded systems. Captures the screen output of a running development board via RTSP streaming, encodes rolling H.264 clips, and delivers them through Git to an AI agent for multimodal frame analysis.

The engineer drives the board in real time while the AI continuously monitors visual output, reports state changes, detects anomalies, and escalates to frame-by-frame forensic analysis when something unexpected appears. **~6 second latency** from board state change to AI feedback.

## The Pipeline

```
STM32 Board → OBS/RTSP → H.264 encode → Git auto-push → Claude pulls → Frame analysis → State report
   (5-8 seconds end-to-end)
```

## Four Analysis Modes

| Mode | Trigger | What it does |
|------|---------|-------------|
| **Live** | `I'm live` | Pull latest clip, extract last frame, report UI state |
| **Static** | `analyze <path>` | Key frame sampling from recordings, state progression timeline |
| **Multi-Live** | `multi-live` | Cross-source validation: UI + UART + camera simultaneously |
| **Hybrid Deep** | `deep <description>` | Frame-by-frame forensics when anomaly is spotted |

## Clip Lifecycle & Session Agent

Beyond the 4 analysis modes, the mechanism includes **clip lifecycle management** (discard vs capture modes with `clip_discard.py`) and a **SessionAgent** for real-time GitHub issue sync with Vicky Viking avatars (NPC = Martin, AWARE with sunglasses = Claude).

## Proven Results

| Result | Detail |
|--------|--------|
| 2 timing-dependent bugs | Found and fixed in a single 1-hour session |
| Config persistence race condition | Detected by comparing pre/post-reboot frames |
| Character rendering corruption | Detected by AI reading garbled text in live clips |
| 3x development speed compression | Measured vs. traditional debugging |

---

[**Read the full documentation →**]({{ '/publications/live-session-analysis/full/' | relative_url }})

---

*Authors: Martin Paquet & Claude (Anthropic, Opus 4.6)*
*Knowledge: [packetqc/knowledge](https://github.com/packetqc/knowledge)*
