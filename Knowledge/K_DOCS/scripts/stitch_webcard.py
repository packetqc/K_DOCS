#!/usr/bin/env python3
"""
Stitch captured MindElixir PNG frames into an animated webcard GIF.
Adds header/footer bars matching the viewer theme.

Usage:
  # First capture frames:
  node Knowledge/K_DOCS/scripts/capture_mindmap.js daltonism-light
  # Then stitch:
  python3 Knowledge/K_DOCS/scripts/stitch_webcard.py daltonism-light
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

CARD_W, CARD_H = 1200, 630
FRAME_DIR = Path("/tmp/mindmap-frames")
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
OUTPUT_DIR = PROJECT_ROOT / "docs" / "assets" / "og"

THEMES = {
    "daltonism-light": {
        "accent": "#0055b3", "gradient_top": "#0055b3", "gradient_bot": "#003d82",
    },
    "daltonism-dark": {
        "accent": "#5b9bd5", "gradient_top": "#2a4a7a", "gradient_bot": "#1a1a2e",
    },
    "cayman": {
        "accent": "#1d4ed8", "gradient_top": "#0d9488", "gradient_bot": "#1d4ed8",
    },
    "midnight": {
        "accent": "#60a5fa", "gradient_top": "#1e3a5f", "gradient_bot": "#0f172a",
    },
}


def hex_rgb(h):
    return tuple(int(h.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))


def blend(c1, c2, t):
    return tuple(int(c1[i]*(1-t) + c2[i]*t) for i in range(3))


def add_chrome(frame_img, theme_name, node_count, frame_num, total_frames):
    """Add header/footer bars to a MindElixir screenshot."""
    T = THEMES[theme_name]
    accent = hex_rgb(T["accent"])
    gt = hex_rgb(T["gradient_top"])
    gb = hex_rgb(T["gradient_bot"])

    card = Image.new("RGB", (CARD_W, CARD_H), (0, 0, 0))
    draw = ImageDraw.Draw(card)

    bar_h = 36
    bot_h = 22

    # Top gradient bar
    for y in range(bar_h):
        draw.line([(0, y), (CARD_W, y)], fill=blend(gt, gb, y / bar_h))

    # Bottom bar
    bot_y = CARD_H - bot_h
    draw.rectangle([(0, bot_y), (CARD_W, CARD_H)], fill=accent)

    # Fonts
    try:
        f_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        f_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
    except (IOError, OSError):
        f_title = f_small = ImageFont.load_default()

    draw.text((14, 9), "KNOWLEDGE \u2014 Live Knowledge Graph", fill=(255,255,255), font=f_title)
    draw.text((CARD_W - 190, 12), f"{node_count} nodes \u00b7 {theme_name}", fill=(200,220,255), font=f_small)
    draw.text((14, bot_y + 4), "packetqc/K_DOCS", fill=(255,255,255), font=f_small)
    draw.text((CARD_W - 170, bot_y + 4), "Dynamic Webcard", fill=(200,220,255), font=f_small)

    # Paste MindElixir frame into content area
    content_h = CARD_H - bar_h - bot_h
    frame_resized = frame_img.resize((CARD_W, content_h), Image.LANCZOS)
    card.paste(frame_resized, (0, bar_h))

    # Progress text overlay
    if frame_num < total_frames - 1:
        # Semi-transparent progress on the frame
        draw2 = ImageDraw.Draw(card)
        draw2.text((14, bar_h + 4), f"Building... {frame_num+1}/{total_frames}",
                   fill=(128, 128, 128), font=f_small)

    return card


def main():
    theme_name = sys.argv[1] if len(sys.argv) > 1 else "daltonism-light"
    lang = sys.argv[2] if len(sys.argv) > 2 else "en"

    if theme_name not in THEMES:
        print(f"Unknown theme: {theme_name}")
        sys.exit(1)

    # Count nodes from mindmap
    mind_path = PROJECT_ROOT / "Knowledge" / "K_MIND" / "mind" / "mind_memory.md"
    import re
    text = mind_path.read_text(encoding="utf-8")
    match = re.search(r"```mermaid\s*\n([\s\S]*?)```", text)
    node_count = 0
    if match:
        lines = [l.strip() for l in match.group(1).split("\n")
                 if l.strip() and not l.strip().startswith("%%") and l.strip() != "mindmap"]
        node_count = len(lines)

    # Load frames
    frame_files = sorted(FRAME_DIR.glob("frame-*.png"))
    if not frame_files:
        print(f"No frames found in {FRAME_DIR}")
        sys.exit(1)

    print(f"Stitching {len(frame_files)} frames for {theme_name}/{lang}")

    frames = []
    for i, fp in enumerate(frame_files):
        img = Image.open(fp).convert("RGB")
        card = add_chrome(img, theme_name, node_count, i, len(frame_files))
        frames.append(card)

    # Hold final frame
    for _ in range(3):
        frames.append(frames[-1])

    # Save animated GIF
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"live-mindmap-{lang}-{theme_name}.gif"
    output_path = OUTPUT_DIR / filename

    optimized = [f.quantize(colors=256, method=Image.Quantize.MEDIANCUT,
                            dither=Image.Dither.FLOYDSTEINBERG) for f in frames]
    # Cinematic timing: 600ms per transition frame, faster pacing for many frames
    durations = [600] * len(frame_files) + [2000] * 3

    optimized[0].save(str(output_path), save_all=True, append_images=optimized[1:],
                      duration=durations, loop=0, optimize=True)

    size_kb = output_path.stat().st_size / 1024
    print(f"  -> {output_path} ({size_kb:.0f} KB, {len(frames)} frames)")


if __name__ == "__main__":
    main()
