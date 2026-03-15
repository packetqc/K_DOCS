#!/usr/bin/env python3
"""
Dynamic Webcard Generator — Live Mindmap
=========================================
Renders the K_MIND mindmap (mind_memory.md) into an animated OG webcard GIF.
This is the second dynamic webcard (after Knowledge Dashboard #4a).

The mindmap content changes every session, so the webcard reflects the current
knowledge state — branches, work items, conventions, and documentation structure.

Animation: builds the mindmap branch-by-branch, then shows the full graph.

Requirements:
  - @mermaid-js/mermaid-cli (npx mmdc)
  - Pillow (pip3 install pillow)

Usage:
  python3 scripts/generate_mindmap_webcard.py                    # Both themes
  python3 scripts/generate_mindmap_webcard.py --theme cayman     # Light only
  python3 scripts/generate_mindmap_webcard.py --theme midnight   # Dark only
  python3 scripts/generate_mindmap_webcard.py --lang fr          # French
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow required. Install: pip3 install pillow")
    sys.exit(1)

# === Config ===
CARD_W, CARD_H = 1200, 630
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MIND_PATH = PROJECT_ROOT / "Knowledge" / "K_MIND" / "mind" / "mind_memory.md"
OUTPUT_DIR = PROJECT_ROOT / "docs" / "assets" / "og"

THEMES = {
    "cayman": {
        "bg": "#eff6ff",
        "fg": "#0f172a",
        "accent": "#1d4ed8",
        "muted": "#475569",
        "border": "#93c5fd",
        "gradient_top": "#0d9488",
        "gradient_bot": "#1d4ed8",
        "mermaid_theme": "default",
    },
    "midnight": {
        "bg": "#0f172a",
        "fg": "#e2e8f0",
        "accent": "#60a5fa",
        "muted": "#94a3b8",
        "border": "#334155",
        "gradient_top": "#1e3a5f",
        "gradient_bot": "#0f172a",
        "mermaid_theme": "dark",
    },
}


def read_mindmap():
    """Extract mermaid code from mind_memory.md."""
    text = MIND_PATH.read_text(encoding="utf-8")
    match = re.search(r"```mermaid\s*\n([\s\S]*?)```", text)
    if not match:
        print("Error: No mermaid block found in mind_memory.md")
        sys.exit(1)
    return match.group(1).strip()


def count_nodes(mermaid_code):
    """Count approximate node count from mermaid mindmap code."""
    lines = [l.strip() for l in mermaid_code.split("\n") if l.strip() and not l.strip().startswith("%%") and l.strip() != "mindmap"]
    return len(lines)


def render_mermaid_to_png(mermaid_code, output_path, theme="default", width=1200):
    """Render mermaid code to PNG using mmdc (mermaid-cli)."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".mmd", delete=False) as f:
        f.write(mermaid_code)
        mmd_path = f.name

    # mmdc config for theme
    config = {"theme": theme}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(config, f)
        config_path = f.name

    try:
        cmd = [
            "npx", "--yes", "@mermaid-js/mermaid-cli",
            "-i", mmd_path,
            "-o", str(output_path),
            "-w", str(width),
            "-b", "transparent",
            "--configFile", config_path,
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            print(f"mmdc error: {result.stderr}")
            return False
        return True
    except FileNotFoundError:
        print("Error: mmdc not found. Install: npm install -g @mermaid-js/mermaid-cli")
        return False
    except subprocess.TimeoutExpired:
        print("Error: mmdc timed out")
        return False
    finally:
        os.unlink(mmd_path)
        os.unlink(config_path)


def build_progressive_frames(mermaid_code):
    """
    Build progressive versions of the mindmap for animation.
    Returns list of mermaid code strings, each adding more nodes.
    """
    lines = mermaid_code.split("\n")
    # Find the init directive and mindmap/root lines
    header_lines = []
    content_lines = []
    in_header = True

    for line in lines:
        stripped = line.strip()
        if in_header and (stripped.startswith("%%") or stripped == "mindmap" or stripped.startswith("root")):
            header_lines.append(line)
        else:
            in_header = False
            content_lines.append(line)

    # Group content by top-level branches (indent level 4 = top-level child of root)
    branches = []
    current_branch = []
    for line in content_lines:
        if not line.strip():
            continue
        # Count leading spaces
        indent = len(line) - len(line.lstrip())
        if indent <= 4 and current_branch:
            branches.append(current_branch)
            current_branch = [line]
        else:
            current_branch.append(line)
    if current_branch:
        branches.append(current_branch)

    # Build progressive frames: header + 1 branch, +2 branches, etc.
    frames = []
    for i in range(1, len(branches) + 1):
        frame_lines = header_lines[:]
        for branch in branches[:i]:
            frame_lines.extend(branch)
        frames.append("\n".join(frame_lines))

    return frames


def create_card_frame(mindmap_png_path, theme_name, node_count, frame_label=None):
    """
    Compose a 1200x630 webcard frame with the mindmap rendered inside.
    """
    theme = THEMES[theme_name]
    # Parse hex colors
    bg = tuple(int(theme["bg"].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    fg = tuple(int(theme["fg"].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    accent = tuple(int(theme["accent"].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    muted = tuple(int(theme["muted"].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    gt = tuple(int(theme["gradient_top"].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    gb = tuple(int(theme["gradient_bot"].lstrip("#")[i:i+2], 16) for i in (0, 2, 4))

    card = Image.new("RGB", (CARD_W, CARD_H), bg)
    draw = ImageDraw.Draw(card)

    # Top gradient bar (40px)
    bar_h = 40
    for y in range(bar_h):
        r = int(gt[0] + (gb[0] - gt[0]) * y / bar_h)
        g = int(gt[1] + (gb[1] - gt[1]) * y / bar_h)
        b = int(gt[2] + (gb[2] - gt[2]) * y / bar_h)
        draw.line([(0, y), (CARD_W, y)], fill=(r, g, b))

    # Title text on gradient bar
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
    except (IOError, OSError):
        font_title = ImageFont.load_default()
        font_small = font_title
        font_label = font_title

    draw.text((16, 10), "K_MIND — Live Knowledge Graph", fill=(255, 255, 255), font=font_title)
    draw.text((CARD_W - 200, 14), f"{node_count} nodes · {theme_name}", fill=(200, 220, 255), font=font_small)

    # Bottom bar (24px)
    bot_y = CARD_H - 24
    draw.rectangle([(0, bot_y), (CARD_W, CARD_H)], fill=accent)
    draw.text((16, bot_y + 4), "packetqc/K_DOCS", fill=(255, 255, 255), font=font_small)
    draw.text((CARD_W - 180, bot_y + 4), "Dynamic Webcard #2", fill=(200, 220, 255), font=font_small)

    # Load and paste mindmap PNG
    if mindmap_png_path and Path(mindmap_png_path).exists():
        mindmap_img = Image.open(mindmap_png_path).convert("RGBA")
        # Fit into available area (1200 x ~566px minus padding)
        avail_w = CARD_W - 32
        avail_h = CARD_H - bar_h - 24 - 16  # top bar + bottom bar + padding
        # Scale to fit
        scale = min(avail_w / mindmap_img.width, avail_h / mindmap_img.height)
        if scale < 1:
            new_w = int(mindmap_img.width * scale)
            new_h = int(mindmap_img.height * scale)
            mindmap_img = mindmap_img.resize((new_w, new_h), Image.LANCZOS)
        # Center in available area
        x = (CARD_W - mindmap_img.width) // 2
        y = bar_h + (avail_h - mindmap_img.height) // 2
        # Composite with background
        bg_layer = Image.new("RGBA", (CARD_W, CARD_H), bg + (255,))
        bg_layer.paste(card.convert("RGBA"))
        bg_layer.paste(mindmap_img, (x, y), mindmap_img)
        card = bg_layer.convert("RGB")

    # Frame label (for progressive animation)
    if frame_label:
        draw2 = ImageDraw.Draw(card)
        draw2.text((16, bar_h + 4), frame_label, fill=muted, font=font_label)

    return card


def generate_webcard(theme_name, lang="en"):
    """Generate the animated mindmap webcard GIF."""
    print(f"Generating mindmap webcard: {theme_name}/{lang}")
    theme = THEMES[theme_name]

    mermaid_code = read_mindmap()
    node_count = count_nodes(mermaid_code)
    print(f"  Mindmap: {node_count} nodes")

    # Build progressive frames
    progressive = build_progressive_frames(mermaid_code)
    print(f"  Animation: {len(progressive)} progressive frames + 3 hold frames")

    frames = []
    with tempfile.TemporaryDirectory() as tmpdir:
        # Render each progressive frame
        for i, frame_code in enumerate(progressive):
            png_path = os.path.join(tmpdir, f"frame_{i}.png")
            label = f"Building... ({i+1}/{len(progressive)})" if i < len(progressive) - 1 else None
            success = render_mermaid_to_png(frame_code, png_path, theme=theme["mermaid_theme"])
            if success:
                frame = create_card_frame(png_path, theme_name, node_count, frame_label=label)
            else:
                frame = create_card_frame(None, theme_name, node_count, frame_label=f"Frame {i+1}")
            frames.append(frame)

        # Hold on final frame (full mindmap) for longer
        if frames:
            for _ in range(3):
                frames.append(frames[-1])

    if not frames:
        print("  Error: No frames generated")
        return None

    # Save as animated GIF
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # Naming: live-mindmap-<lang>-<theme>.gif
    filename = f"live-mindmap-{lang}-{theme_name}.gif"
    output_path = OUTPUT_DIR / filename

    # Optimize: 256-color palette, Floyd-Steinberg dithering
    optimized = []
    for f in frames:
        optimized.append(f.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG))

    # Frame durations: 800ms per progressive frame, 2000ms for hold frames
    durations = [800] * len(progressive) + [2000] * 3

    optimized[0].save(
        str(output_path),
        save_all=True,
        append_images=optimized[1:],
        duration=durations,
        loop=0,
        optimize=True,
    )

    size_kb = output_path.stat().st_size / 1024
    print(f"  Output: {output_path} ({size_kb:.0f} KB, {len(frames)} frames)")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Generate mindmap dynamic webcard")
    parser.add_argument("--theme", choices=["cayman", "midnight"], help="Generate one theme only")
    parser.add_argument("--lang", default="en", help="Language (default: en)")
    args = parser.parse_args()

    if not MIND_PATH.exists():
        print(f"Error: {MIND_PATH} not found")
        sys.exit(1)

    themes = [args.theme] if args.theme else ["cayman", "midnight"]

    results = []
    for theme in themes:
        path = generate_webcard(theme, args.lang)
        if path:
            results.append(str(path))

    if results:
        print(f"\nGenerated {len(results)} webcard(s):")
        for r in results:
            print(f"  {r}")
    else:
        print("\nNo webcards generated (check errors above)")
        sys.exit(1)


if __name__ == "__main__":
    main()
