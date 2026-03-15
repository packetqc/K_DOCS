#!/usr/bin/env python3
"""
Dynamic Webcard Generator — Live Mindmap
=========================================
Renders the K_MIND mindmap into an animated OG webcard GIF.
Visual style matches MindElixir's rendering (rounded pills, branch colors,
radial-ish layout). Pure Pillow — no browser dependency.

Usage:
  python3 Knowledge/K_DOCS/scripts/generate_mindmap_webcard.py                    # Both themes
  python3 Knowledge/K_DOCS/scripts/generate_mindmap_webcard.py --theme cayman     # Light only
  python3 Knowledge/K_DOCS/scripts/generate_mindmap_webcard.py --theme midnight   # Dark only
"""

import argparse
import math
import re
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow required. Install: pip3 install pillow")
    sys.exit(1)

CARD_W, CARD_H = 1200, 630
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
MIND_PATH = PROJECT_ROOT / "Knowledge" / "K_MIND" / "mind" / "mind_memory.md"
OUTPUT_DIR = PROJECT_ROOT / "docs" / "assets" / "og"

# MindElixir-matched palettes (from viewer theme sync)
THEMES = {
    "cayman": {
        "bg": "#eff6ff",
        "fg": "#1e293b",
        "accent": "#1d4ed8",
        "muted": "#64748b",
        "root_bg": "#1d4ed8",
        "root_fg": "#ffffff",
        "gradient_top": "#0d9488",
        "gradient_bot": "#1d4ed8",
        # MindElixir branch colors (from Cayman palette)
        "branch": ["#1d4ed8", "#0d9488", "#7c3aed", "#dc2626", "#ea580c", "#0284c7",
                    "#4f46e5", "#059669", "#9333ea", "#e11d48"],
        "leaf_alpha": 0.12,
    },
    "midnight": {
        "bg": "#0f172a",
        "fg": "#e2e8f0",
        "accent": "#60a5fa",
        "muted": "#94a3b8",
        "root_bg": "#1e40af",
        "root_fg": "#e2e8f0",
        "gradient_top": "#1e3a5f",
        "gradient_bot": "#0f172a",
        "branch": ["#60a5fa", "#34d399", "#a78bfa", "#fb7185", "#fb923c", "#38bdf8",
                    "#818cf8", "#6ee7b7", "#c084fc", "#fda4af"],
        "leaf_alpha": 0.18,
    },
}


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def blend(c1, c2, t):
    return tuple(int(c1[i] * (1 - t) + c2[i] * t) for i in range(3))


def parse_mindmap(mermaid_code):
    """Parse mermaid mindmap into tree."""
    lines = mermaid_code.split("\n")
    root = None
    stack = []

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("%%") or stripped == "mindmap":
            continue

        indent = len(line) - len(line.lstrip())
        text = stripped

        # Strip decorators
        rm = re.match(r'^root\(\((.*)\)\)$', text)
        if rm:
            text = rm.group(1)
        else:
            for pat in [r'^\(\((.*)\)\)$', r'^\((.*)\)$', r'^\[(.*)\]$', r'^\{(.*)\}$']:
                m = re.match(pat, text)
                if m:
                    text = m.group(1)
                    break

        node = {"text": text, "children": [], "indent": indent}

        if root is None:
            root = node
            stack = [(indent, node)]
            continue

        while stack and stack[-1][0] >= indent:
            stack.pop()
        if stack:
            stack[-1][1]["children"].append(node)
        stack.append((indent, node))

    return root


def measure_text(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def draw_rounded_pill(draw, x, y, w, h, radius, fill, outline=None, width=1):
    """Draw a rounded rectangle (pill shape)."""
    draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=radius,
                           fill=fill, outline=outline, width=width)


def draw_curved_edge(draw, x1, y1, x2, y2, color, width=2):
    """Draw a curved bezier-like edge between two points."""
    # Simple approach: draw a straight line with slight curve via midpoint offset
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    # Slight curve toward center
    cx_off = (x2 - x1) * 0.3
    # Draw as polyline approximation of bezier
    steps = 12
    points = []
    for i in range(steps + 1):
        t = i / steps
        # Quadratic bezier: P = (1-t)^2*P0 + 2t(1-t)*Pc + t^2*P1
        cpx = mx
        cpy = my - (y2 - y1) * 0.1  # slight curve
        px = (1-t)**2 * x1 + 2*t*(1-t) * cpx + t**2 * x2
        py = (1-t)**2 * y1 + 2*t*(1-t) * cpy + t**2 * y2
        points.append((px, py))

    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=color, width=width)


def generate_frame(theme_name, root, visible_branches, node_count, total_branches):
    """Render one frame with N visible branches using MindElixir visual style."""
    T = THEMES[theme_name]
    bg = hex_rgb(T["bg"])
    fg = hex_rgb(T["fg"])
    accent = hex_rgb(T["accent"])
    muted = hex_rgb(T["muted"])
    root_bg = hex_rgb(T["root_bg"])
    root_fg = hex_rgb(T["root_fg"])
    gt = hex_rgb(T["gradient_top"])
    gb = hex_rgb(T["gradient_bot"])
    branch_colors = [hex_rgb(c) for c in T["branch"]]
    leaf_alpha = T["leaf_alpha"]

    card = Image.new("RGB", (CARD_W, CARD_H), bg)
    draw = ImageDraw.Draw(card)

    # === Top gradient bar (36px) ===
    bar_h = 36
    for y in range(bar_h):
        t = y / bar_h
        draw.line([(0, y), (CARD_W, y)], fill=blend(gt, gb, t))

    # === Fonts ===
    try:
        f_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        f_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
        f_root = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)
        f_branch = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 11)
        f_leaf = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    except (IOError, OSError):
        f_title = f_small = f_root = f_branch = f_leaf = ImageFont.load_default()

    # Title bar
    draw.text((14, 9), "K_MIND \u2014 Live Knowledge Graph", fill=(255, 255, 255), font=f_title)
    draw.text((CARD_W - 190, 12), f"{node_count} nodes \u00b7 {theme_name}", fill=(200, 220, 255), font=f_small)

    # Bottom bar (22px)
    bot_y = CARD_H - 22
    draw.rectangle([(0, bot_y), (CARD_W, CARD_H)], fill=accent)
    draw.text((14, bot_y + 4), "packetqc/K_DOCS", fill=(255, 255, 255), font=f_small)
    draw.text((CARD_W - 170, bot_y + 4), "Dynamic Webcard", fill=(200, 220, 255), font=f_small)

    # === Content area ===
    ct = bar_h + 6
    cb = bot_y - 6
    ch = cb - ct
    cx = CARD_W // 2
    cy = ct + ch // 2

    # Filter to visible branches
    children = root.get("children", [])[:visible_branches]

    # === Layout: root center, branches distributed around ===
    # Use horizontal tree: 3 branches left, 3 branches right (or split evenly)
    n = len(children)
    left_n = (n + 1) // 2
    right_n = n - left_n

    # Collect all nodes to draw
    nodes = []  # (x, y, text, depth, branch_idx, is_root)
    edges = []  # (from_idx, to_idx)

    # Root node at center
    rw, rh = measure_text(draw, root["text"], f_root)
    nodes.append((cx, cy, root["text"], 0, -1))

    # Branch spacing
    branch_x_offset = 220  # horizontal distance from root to branch
    leaf_x_offset = 180    # horizontal distance from branch to leaf
    vert_spacing = max(38, ch / max(max(left_n, right_n) + 1, 2))

    for bi, child in enumerate(children):
        bc = branch_colors[bi % len(branch_colors)]

        if bi < left_n:
            # Left side
            side = -1
            slot = bi
            total_on_side = left_n
        else:
            # Right side
            side = 1
            slot = bi - left_n
            total_on_side = right_n

        # Vertical position
        y_start = cy - (total_on_side - 1) * vert_spacing / 2
        bx = cx + side * branch_x_offset
        by = y_start + slot * vert_spacing

        # Clamp to content area
        by = max(ct + 18, min(cb - 18, by))

        b_idx = len(nodes)
        nodes.append((bx, by, child["text"], 1, bi))
        edges.append((0, b_idx))

        # Second-level children (leaves)
        grandchildren = child.get("children", [])
        max_leaves = 4  # limit for readability
        for gi, gc in enumerate(grandchildren[:max_leaves]):
            leaf_vert = vert_spacing * 0.55
            gc_total = min(len(grandchildren), max_leaves)
            gy_start = by - (gc_total - 1) * leaf_vert / 2
            gx = bx + side * leaf_x_offset
            gy = gy_start + gi * leaf_vert
            gy = max(ct + 12, min(cb - 12, gy))

            gc_idx = len(nodes)
            text = gc["text"]
            if len(text) > 22:
                text = text[:20] + ".."
            nodes.append((gx, gy, text, 2, bi))
            edges.append((b_idx, gc_idx))

        # Show "+N more" if truncated
        if len(grandchildren) > max_leaves:
            more = len(grandchildren) - max_leaves
            gc_total = min(len(grandchildren), max_leaves)
            gy = by - (gc_total - 1) * leaf_vert / 2 + max_leaves * leaf_vert
            gy = max(ct + 12, min(cb - 12, gy))
            gx = bx + side * leaf_x_offset
            gc_idx = len(nodes)
            nodes.append((gx, gy, f"+{more} more", 3, bi))  # depth 3 = "more" indicator

    # === Draw edges ===
    for (si, di) in edges:
        sx, sy = nodes[si][0], nodes[si][1]
        dx, dy = nodes[di][0], nodes[di][1]
        bi = nodes[di][4]
        bc = branch_colors[bi % len(branch_colors)]
        edge_color = blend(bc, bg, 0.5)
        draw_curved_edge(draw, sx, sy, dx, dy, edge_color, width=2)

    # === Draw nodes (back to front: leaves, branches, root) ===
    for i in reversed(range(len(nodes))):
        x, y, text, depth, bi = nodes[i]
        bc = branch_colors[bi % len(branch_colors)] if bi >= 0 else root_bg

        if depth == 0:
            # Root — large rounded pill, accent color
            tw, th = measure_text(draw, text, f_root)
            px, py = 18, 10
            draw_rounded_pill(draw, x - tw//2 - px, y - th//2 - py,
                              tw + px*2, th + py*2, 14, root_bg, outline=accent, width=2)
            draw.text((x - tw//2, y - th//2), text, fill=root_fg, font=f_root)

        elif depth == 1:
            # Branch — colored pill (MindElixir style)
            tw, th = measure_text(draw, text, f_branch)
            if len(text) > 20:
                text = text[:18] + ".."
                tw, th = measure_text(draw, text, f_branch)
            px, py = 12, 6
            draw_rounded_pill(draw, x - tw//2 - px, y - th//2 - py,
                              tw + px*2, th + py*2, 10, bc)
            draw.text((x - tw//2, y - th//2), text, fill=(255, 255, 255), font=f_branch)

        elif depth == 2:
            # Leaf — subtle tinted background
            tw, th = measure_text(draw, text, f_leaf)
            px, py = 8, 4
            leaf_bg = blend(bg, bc, leaf_alpha)
            leaf_border = blend(bg, bc, 0.3)
            draw_rounded_pill(draw, x - tw//2 - px, y - th//2 - py,
                              tw + px*2, th + py*2, 6, leaf_bg, outline=leaf_border)
            draw.text((x - tw//2, y - th//2), text, fill=fg, font=f_leaf)

        elif depth == 3:
            # "+N more" indicator
            tw, th = measure_text(draw, text, f_leaf)
            draw.text((x - tw//2, y - th//2), text, fill=muted, font=f_leaf)

    # Progress indicator
    if visible_branches < total_branches:
        draw.text((14, ct), f"Building... {visible_branches}/{total_branches} branches",
                  fill=muted, font=f_small)

    return card


def generate_webcard(theme_name, lang="en"):
    """Generate the animated mindmap webcard GIF."""
    print(f"Generating mindmap webcard: {theme_name}/{lang}")

    text = MIND_PATH.read_text(encoding="utf-8")
    match = re.search(r"```mermaid\s*\n([\s\S]*?)```", text)
    if not match:
        print("Error: No mermaid block found")
        return None

    code = match.group(1).strip()
    node_lines = [l.strip() for l in code.split("\n")
                  if l.strip() and not l.strip().startswith("%%") and l.strip() != "mindmap"]
    node_count = len(node_lines)

    root = parse_mindmap(code)
    if not root:
        print("Error: Failed to parse mindmap")
        return None

    total = len(root.get("children", []))
    print(f"  Mindmap: {node_count} nodes, {total} top-level branches")

    # Progressive frames: one per branch
    frames = []
    for i in range(1, total + 1):
        frame = generate_frame(theme_name, root, i, node_count, total)
        frames.append(frame)

    # Hold final frame
    for _ in range(3):
        frames.append(frames[-1])

    print(f"  Animation: {total} + 3 hold = {len(frames)} frames")

    # Save as animated GIF
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"live-mindmap-{lang}-{theme_name}.gif"
    output_path = OUTPUT_DIR / filename

    optimized = [f.quantize(colors=256, method=Image.Quantize.MEDIANCUT,
                            dither=Image.Dither.FLOYDSTEINBERG) for f in frames]

    durations = [800] * total + [2000] * 3

    optimized[0].save(str(output_path), save_all=True, append_images=optimized[1:],
                      duration=durations, loop=0, optimize=True)

    size_kb = output_path.stat().st_size / 1024
    print(f"  Output: {output_path} ({size_kb:.0f} KB)")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Generate mindmap dynamic webcard")
    parser.add_argument("--theme", choices=["cayman", "midnight"], help="One theme only")
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
        print("\nNo webcards generated")
        sys.exit(1)


if __name__ == "__main__":
    main()
