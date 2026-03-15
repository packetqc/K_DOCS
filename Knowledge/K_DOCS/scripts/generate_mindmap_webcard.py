#!/usr/bin/env python3
"""
Dynamic Webcard Generator — Live Mindmap
=========================================
Renders the K_MIND mindmap into an animated OG webcard GIF.
Visual style matches MindElixir: curved bezier edges, rounded pill nodes,
organic radial layout. Pure Pillow — no browser dependency.

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

# MindElixir-matched 4-theme palettes (from viewer CSS variables)
THEMES = {
    "cayman": {
        "bg": "#eff6ff", "fg": "#1e293b", "accent": "#1d4ed8", "muted": "#64748b",
        "root_bg": "#1d4ed8", "root_fg": "#ffffff",
        "gradient_top": "#0d9488", "gradient_bot": "#1d4ed8",
        "branch": ["#2563eb", "#0d9488", "#7c3aed", "#dc2626", "#ea580c", "#0284c7",
                    "#4f46e5", "#059669", "#9333ea", "#e11d48"],
        "leaf_alpha": 0.12, "edge_alpha": 0.35,
    },
    "midnight": {
        "bg": "#0f172a", "fg": "#e2e8f0", "accent": "#60a5fa", "muted": "#94a3b8",
        "root_bg": "#1e40af", "root_fg": "#e2e8f0",
        "gradient_top": "#1e3a5f", "gradient_bot": "#0f172a",
        "branch": ["#60a5fa", "#34d399", "#a78bfa", "#fb7185", "#fb923c", "#38bdf8",
                    "#818cf8", "#6ee7b7", "#c084fc", "#fda4af"],
        "leaf_alpha": 0.20, "edge_alpha": 0.50,
    },
    "daltonism-light": {
        "bg": "#faf6f1", "fg": "#1a1a2e", "accent": "#0055b3", "muted": "#5c5c78",
        "root_bg": "#0055b3", "root_fg": "#ffffff",
        "gradient_top": "#0055b3", "gradient_bot": "#003d82",
        "branch": ["#0055b3", "#b35900", "#6b21a8", "#b91c1c", "#0e7490", "#15803d",
                    "#1d4ed8", "#a16207", "#7e22ce", "#be123c"],
        "leaf_alpha": 0.10, "edge_alpha": 0.30,
    },
    "daltonism-dark": {
        "bg": "#1a1a2e", "fg": "#e8e0d4", "accent": "#5b9bd5", "muted": "#8888a0",
        "root_bg": "#2a4a7a", "root_fg": "#e8e0d4",
        "gradient_top": "#2a4a7a", "gradient_bot": "#1a1a2e",
        "branch": ["#5b9bd5", "#f0a050", "#b088d0", "#e87070", "#50b8d0", "#60c080",
                    "#7090e0", "#d0a040", "#a070e0", "#e08090"],
        "leaf_alpha": 0.18, "edge_alpha": 0.45,
    },
}


def hex_rgb(h):
    return tuple(int(h.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))


def blend(c1, c2, t):
    return tuple(int(c1[i] * (1 - t) + c2[i] * t) for i in range(3))


def parse_mindmap(mermaid_code):
    lines = mermaid_code.split("\n")
    root = None
    stack = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("%%") or stripped == "mindmap":
            continue
        indent = len(line) - len(line.lstrip())
        text = stripped
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


def measure(draw, text, font):
    bb = draw.textbbox((0, 0), text, font=font)
    return bb[2] - bb[0], bb[3] - bb[1]


def draw_bezier(draw, x1, y1, x2, y2, color, width=2):
    """Draw a smooth cubic bezier curve (MindElixir-style)."""
    # Control points: horizontal first, then vertical
    cx1 = x1 + (x2 - x1) * 0.5
    cy1 = y1
    cx2 = x1 + (x2 - x1) * 0.5
    cy2 = y2
    steps = 20
    pts = []
    for i in range(steps + 1):
        t = i / steps
        t2 = t * t
        t3 = t2 * t
        mt = 1 - t
        mt2 = mt * mt
        mt3 = mt2 * mt
        px = mt3*x1 + 3*mt2*t*cx1 + 3*mt*t2*cx2 + t3*x2
        py = mt3*y1 + 3*mt2*t*cy1 + 3*mt*t2*cy2 + t3*y2
        pts.append((px, py))
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=color, width=width)


def generate_frame(theme_name, root, visible_branches, node_count, total_branches):
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
    edge_alpha = T["edge_alpha"]

    card = Image.new("RGB", (CARD_W, CARD_H), bg)
    draw = ImageDraw.Draw(card)

    # Top gradient bar
    bar_h = 36
    for y in range(bar_h):
        draw.line([(0, y), (CARD_W, y)], fill=blend(gt, gb, y / bar_h))

    # Fonts
    try:
        f_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        f_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
        f_root = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
        f_branch = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 11)
        f_leaf = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    except (IOError, OSError):
        f_title = f_small = f_root = f_branch = f_leaf = ImageFont.load_default()

    draw.text((14, 9), "K_MIND \u2014 Live Knowledge Graph", fill=(255, 255, 255), font=f_title)
    draw.text((CARD_W - 190, 12), f"{node_count} nodes \u00b7 {theme_name}", fill=(200, 220, 255), font=f_small)

    bot_y = CARD_H - 22
    draw.rectangle([(0, bot_y), (CARD_W, CARD_H)], fill=accent)
    draw.text((14, bot_y + 4), "packetqc/K_DOCS", fill=(255, 255, 255), font=f_small)
    draw.text((CARD_W - 170, bot_y + 4), "Dynamic Webcard", fill=(200, 220, 255), font=f_small)

    # Content area
    ct = bar_h + 8
    cb = bot_y - 8
    ch = cb - ct
    cx = CARD_W // 2
    cy = ct + ch // 2

    children = root.get("children", [])[:visible_branches]
    n = len(children)
    left_n = (n + 1) // 2
    right_n = n - left_n

    # Compute positions
    nodes = []   # (x, y, text, depth, branch_idx)
    edges = []   # (src_idx, dst_idx, branch_idx)

    nodes.append((cx, cy, root["text"], 0, -1))

    branch_x = 200
    leaf_x = 160

    for bi, child in enumerate(children):
        if bi < left_n:
            side = -1
            slot, count = bi, left_n
        else:
            side = 1
            slot, count = bi - left_n, right_n

        v_space = min(55, ch / max(count + 1, 2))
        y_center = cy
        by = y_center + (slot - (count - 1) / 2) * v_space
        by = max(ct + 20, min(cb - 20, by))
        bx = cx + side * branch_x

        b_idx = len(nodes)
        t = child["text"]
        if len(t) > 22:
            t = t[:20] + ".."
        nodes.append((bx, by, t, 1, bi))
        edges.append((0, b_idx, bi))

        # Leaves
        gc_list = child.get("children", [])
        max_gc = 4
        gc_show = gc_list[:max_gc]
        gc_n = len(gc_show)
        lv_space = min(28, v_space * 0.7)

        for gi, gc in enumerate(gc_show):
            gy = by + (gi - (gc_n - 1) / 2) * lv_space
            gy = max(ct + 12, min(cb - 12, gy))
            gx = bx + side * leaf_x
            gc_idx = len(nodes)
            t = gc["text"]
            if len(t) > 22:
                t = t[:20] + ".."
            nodes.append((gx, gy, t, 2, bi))
            edges.append((b_idx, gc_idx, bi))

        if len(gc_list) > max_gc:
            gy = by + (max_gc - (gc_n - 1) / 2) * lv_space
            gy = max(ct + 12, min(cb - 12, gy))
            gx = bx + side * leaf_x
            gc_idx = len(nodes)
            nodes.append((gx, gy, f"+{len(gc_list) - max_gc} more", 3, bi))
            edges.append((b_idx, gc_idx, bi))

    # Draw edges (bezier curves)
    for (si, di, bi) in edges:
        sx, sy = nodes[si][0], nodes[si][1]
        dx, dy = nodes[di][0], nodes[di][1]
        bc = branch_colors[bi % len(branch_colors)]
        ec = blend(bc, bg, 1 - edge_alpha)
        draw_bezier(draw, sx, sy, dx, dy, ec, width=2)

    # Draw small circles at edge connection points on nodes
    for (si, di, bi) in edges:
        bc = branch_colors[bi % len(branch_colors)]
        dot_color = blend(bc, bg, 0.3)
        dx, dy = nodes[di][0], nodes[di][1]
        # Small dot at destination
        depth = nodes[di][3]
        if depth == 1:
            # Connection dot on the branch node side facing root
            side = 1 if nodes[di][0] > cx else -1
            tw, _ = measure(draw, nodes[di][2], f_branch)
            dot_x = nodes[di][0] - side * (tw // 2 + 14)
            draw.ellipse([(dot_x - 3, dy - 3), (dot_x + 3, dy + 3)], fill=dot_color)

    # Draw nodes
    for i, (x, y, text, depth, bi) in enumerate(nodes):
        bc = branch_colors[bi % len(branch_colors)] if bi >= 0 else root_bg

        if depth == 0:
            # Root — large rounded pill
            tw, th = measure(draw, text, f_root)
            px, py = 20, 10
            draw.rounded_rectangle(
                [(x - tw//2 - px, y - th//2 - py), (x + tw//2 + px, y + th//2 + py)],
                radius=16, fill=root_bg, outline=blend(root_bg, (255,255,255), 0.3), width=2
            )
            draw.text((x - tw//2, y - th//2), text, fill=root_fg, font=f_root)

        elif depth == 1:
            # Branch pill
            tw, th = measure(draw, text, f_branch)
            px, py = 12, 6
            # Slight gradient effect via outline
            draw.rounded_rectangle(
                [(x - tw//2 - px, y - th//2 - py), (x + tw//2 + px, y + th//2 + py)],
                radius=12, fill=bc, outline=blend(bc, (255,255,255), 0.2), width=1
            )
            draw.text((x - tw//2, y - th//2), text, fill=(255, 255, 255), font=f_branch)

        elif depth == 2:
            # Leaf — tinted pill
            tw, th = measure(draw, text, f_leaf)
            px, py = 8, 4
            lbg = blend(bg, bc, leaf_alpha)
            lborder = blend(bg, bc, 0.25)
            draw.rounded_rectangle(
                [(x - tw//2 - px, y - th//2 - py), (x + tw//2 + px, y + th//2 + py)],
                radius=8, fill=lbg, outline=lborder, width=1
            )
            draw.text((x - tw//2, y - th//2), text, fill=fg, font=f_leaf)

        elif depth == 3:
            tw, th = measure(draw, text, f_leaf)
            draw.text((x - tw//2, y - th//2), text, fill=muted, font=f_leaf)

    # Progress
    if visible_branches < total_branches:
        draw.text((14, ct), f"Building... {visible_branches}/{total_branches}",
                  fill=muted, font=f_small)

    return card


def generate_webcard(theme_name, lang="en"):
    print(f"Generating: {theme_name}/{lang}")
    text = MIND_PATH.read_text(encoding="utf-8")
    match = re.search(r"```mermaid\s*\n([\s\S]*?)```", text)
    if not match:
        print("Error: No mermaid block")
        return None

    code = match.group(1).strip()
    node_lines = [l.strip() for l in code.split("\n")
                  if l.strip() and not l.strip().startswith("%%") and l.strip() != "mindmap"]
    node_count = len(node_lines)
    root = parse_mindmap(code)
    if not root:
        return None

    total = len(root.get("children", []))
    print(f"  {node_count} nodes, {total} branches")

    frames = []
    for i in range(1, total + 1):
        frames.append(generate_frame(theme_name, root, i, node_count, total))
    for _ in range(3):
        frames.append(frames[-1])

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"live-mindmap-{lang}-{theme_name}.gif"
    output_path = OUTPUT_DIR / filename

    optimized = [f.quantize(colors=256, method=Image.Quantize.MEDIANCUT,
                            dither=Image.Dither.FLOYDSTEINBERG) for f in frames]
    durations = [800] * total + [2000] * 3

    optimized[0].save(str(output_path), save_all=True, append_images=optimized[1:],
                      duration=durations, loop=0, optimize=True)

    size_kb = output_path.stat().st_size / 1024
    print(f"  -> {output_path} ({size_kb:.0f} KB, {len(frames)} frames)")
    return output_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--theme", choices=["cayman", "midnight", "daltonism-light", "daltonism-dark"])
    parser.add_argument("--lang", default="en")
    args = parser.parse_args()

    if not MIND_PATH.exists():
        print(f"Error: {MIND_PATH} not found")
        sys.exit(1)

    themes = [args.theme] if args.theme else ["cayman", "midnight"]
    for theme in themes:
        generate_webcard(theme, args.lang)


if __name__ == "__main__":
    main()
