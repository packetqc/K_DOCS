#!/usr/bin/env python3
"""
Interface Webcard Generator — Animated OG GIFs
===============================================
Generates animated social preview GIFs for interfaces and the viewer.
Follows the established webcard spec: 1200x630, gradient bg, grid, accent bars,
progressive reveal animation.

Usage:
  python3 Knowledge/K_DOCS/scripts/generate_interface_webcard.py --card viewer
  python3 Knowledge/K_DOCS/scripts/generate_interface_webcard.py --card claude-interface
  python3 Knowledge/K_DOCS/scripts/generate_interface_webcard.py --card all
"""

import argparse
import math
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow required. Install: pip3 install pillow")
    sys.exit(1)

CARD_W, CARD_H = 1200, 630
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
OUTPUT_DIR = PROJECT_ROOT / "docs" / "assets" / "og"

THEMES = {
    "cayman": {
        "bg_top": (239, 246, 255), "bg_bot": (219, 234, 254),
        "accent": (29, 78, 216), "fg": (15, 23, 42), "muted": (71, 85, 105),
        "box_bg": (239, 246, 255), "box_border": (29, 78, 216),
        "grid": (29, 78, 216, 20), "bar_colors": [(29, 78, 216), (124, 58, 237), (6, 182, 212), (16, 185, 129)],
    },
    "midnight": {
        "bg_top": (15, 23, 42), "bg_bot": (30, 27, 75),
        "accent": (96, 165, 250), "fg": (226, 232, 240), "muted": (148, 163, 184),
        "box_bg": (30, 41, 59), "box_border": (96, 165, 250),
        "grid": (96, 165, 250, 15), "bar_colors": [(96, 165, 250), (167, 139, 250), (56, 189, 248), (52, 211, 153)],
    },
}

# Card definitions: EN + FR content
CARDS = {
    "viewer": {
        "slug": "viewer",
        "en": {
            "pub_id": "K_DOCS", "title": "K_DOCS Viewer",
            "subtitle": "Universal Document Viewer",
            "keywords": ["4 Themes", "PDF Export", "Fullscreen", "Markdown Rendering"],
            "diagram": "split-panel",
            "panels": [
                {"label": "Toolbar", "x": 80, "y": 200, "w": 1040, "h": 40},
                {"label": "Document", "x": 80, "y": 260, "w": 700, "h": 260},
                {"label": "TOC", "x": 800, "y": 260, "w": 320, "h": 260},
            ],
        },
        "fr": {
            "pub_id": "K_DOCS", "title": "Visualiseur K_DOCS",
            "subtitle": "Visualiseur de documents universel",
            "keywords": ["4 Th\u00e8mes", "Export PDF", "Plein \u00e9cran", "Rendu Markdown"],
            "diagram": "split-panel",
            "panels": [
                {"label": "Barre d'outils", "x": 80, "y": 200, "w": 1040, "h": 40},
                {"label": "Document", "x": 80, "y": 260, "w": 700, "h": 260},
                {"label": "TDM", "x": 800, "y": 260, "w": 320, "h": 260},
            ],
        },
    },
    "claude-interface": {
        "slug": "claude-interface",
        "en": {
            "pub_id": "I6", "title": "Claude Interface",
            "subtitle": "AI-Powered Development Environment",
            "keywords": ["Claude API", "Live Mindmap", "Knowledge Tools", "Command Nav"],
            "diagram": "split-panel",
            "panels": [
                {"label": "Chat", "x": 80, "y": 200, "w": 500, "h": 320},
                {"label": "Mindmap", "x": 600, "y": 200, "w": 520, "h": 150},
                {"label": "Tools", "x": 600, "y": 370, "w": 520, "h": 150},
            ],
        },
        "fr": {
            "pub_id": "I6", "title": "Interface Claude",
            "subtitle": "Environnement de d\u00e9veloppement IA",
            "keywords": ["API Claude", "Mindmap vivant", "Outils Knowledge", "Nav. commandes"],
            "diagram": "split-panel",
            "panels": [
                {"label": "Chat", "x": 80, "y": 200, "w": 500, "h": 320},
                {"label": "Mindmap", "x": 600, "y": 200, "w": 520, "h": 150},
                {"label": "Outils", "x": 600, "y": 370, "w": 520, "h": 150},
            ],
        },
    },
}


def blend(c1, c2, t):
    return tuple(int(c1[i] * (1 - t) + c2[i] * t) for i in range(3))


def make_base(theme):
    """Create base image with gradient background, grid, and accent bars."""
    t = THEMES[theme]
    img = Image.new("RGB", (CARD_W, CARD_H))
    draw = ImageDraw.Draw(img)

    # Vertical gradient
    for y in range(CARD_H):
        frac = y / CARD_H
        color = blend(t["bg_top"], t["bg_bot"], frac)
        draw.line([(0, y), (CARD_W, y)], fill=color)

    # Subtle grid
    grid_img = Image.new("RGBA", (CARD_W, CARD_H), (0, 0, 0, 0))
    grid_draw = ImageDraw.Draw(grid_img)
    gc = t["grid"]
    for x in range(0, CARD_W, 40):
        grid_draw.line([(x, 0), (x, CARD_H)], fill=gc)
    for y in range(0, CARD_H, 40):
        grid_draw.line([(0, y), (CARD_W, y)], fill=gc)
    img.paste(Image.alpha_composite(Image.new("RGBA", (CARD_W, CARD_H), (0, 0, 0, 0)), grid_img).convert("RGB"),
              mask=grid_img.split()[3])

    # Top accent bar (gradient)
    bar_colors = t["bar_colors"]
    for x in range(CARD_W):
        frac = x / CARD_W
        seg = frac * (len(bar_colors) - 1)
        i = min(int(seg), len(bar_colors) - 2)
        local_t = seg - i
        c = blend(bar_colors[i], bar_colors[i + 1], local_t)
        for dy in range(3):
            draw.point((x, dy), fill=c)

    # Bottom accent bar
    for x in range(CARD_W):
        frac = x / CARD_W
        seg = frac * (len(bar_colors) - 1)
        i = min(int(seg), len(bar_colors) - 2)
        local_t = seg - i
        c = blend(bar_colors[i], bar_colors[i + 1], local_t)
        for dy in range(3):
            draw.point((x, CARD_H - 1 - dy), fill=c)

    return img


def get_font(size, bold=False):
    """Get best available font."""
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def draw_title_zone(draw, content, theme):
    """Draw pub_id, title, subtitle in title zone."""
    t = THEMES[theme]
    # Pub ID
    fid = get_font(42, bold=True)
    bbox = draw.textbbox((0, 0), content["pub_id"], font=fid)
    tw = bbox[2] - bbox[0]
    draw.text(((CARD_W - tw) // 2, 40), content["pub_id"], fill=t["accent"], font=fid)

    # Title
    ft = get_font(38, bold=True)
    bbox = draw.textbbox((0, 0), content["title"], font=ft)
    tw = bbox[2] - bbox[0]
    draw.text(((CARD_W - tw) // 2, 95), content["title"], fill=t["fg"], font=ft)

    # Subtitle
    fs = get_font(20)
    bbox = draw.textbbox((0, 0), content["subtitle"], font=fs)
    tw = bbox[2] - bbox[0]
    draw.text(((CARD_W - tw) // 2, 145), content["subtitle"], fill=t["muted"], font=fs)


def draw_footer(draw, content, theme):
    """Draw keywords + author line in footer zone."""
    t = THEMES[theme]
    # Keywords
    kw_text = " \u00b7 ".join(content["keywords"])
    fk = get_font(16)
    bbox = draw.textbbox((0, 0), kw_text, font=fk)
    tw = bbox[2] - bbox[0]
    draw.text(((CARD_W - tw) // 2, 555), kw_text, fill=t["muted"], font=fk)

    # Author
    author = "Martin Paquet & Claude  |  packetqc/knowledge"
    fa = get_font(14)
    bbox = draw.textbbox((0, 0), author, font=fa)
    tw = bbox[2] - bbox[0]
    draw.text(((CARD_W - tw) // 2, 585), author, fill=t["muted"], font=fa)


def draw_panel(draw, panel, theme, alpha=1.0):
    """Draw a rounded rectangle panel with label."""
    t = THEMES[theme]
    x, y, w, h = panel["x"], panel["y"], panel["w"], panel["h"]
    # Border color with alpha simulation
    border = tuple(int(t["box_border"][i] * alpha + t["bg_top"][i] * (1 - alpha)) for i in range(3))
    fill = tuple(int(t["box_bg"][i] * alpha + t["bg_top"][i] * (1 - alpha)) for i in range(3))

    draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=8, fill=fill, outline=border, width=2)

    # Label
    fl = get_font(16, bold=True)
    lbl = panel["label"]
    bbox = draw.textbbox((0, 0), lbl, font=fl)
    lw = bbox[2] - bbox[0]
    label_color = tuple(int(t["accent"][i] * alpha + t["bg_top"][i] * (1 - alpha)) for i in range(3))
    draw.text((x + (w - lw) // 2, y + 12), lbl, fill=label_color, font=fl)


def generate_card(card_key, lang, theme):
    """Generate animated GIF for a card variant."""
    card = CARDS[card_key]
    content = card[lang]
    panels = content["panels"]

    frames = []

    # Frame 0: Base only (title + subtitle)
    base = make_base(theme)
    draw = ImageDraw.Draw(base)
    draw_title_zone(draw, content, theme)
    draw_footer(draw, content, theme)
    frames.append(base.copy())

    # Frames 1-N: Progressive panel reveal
    for i in range(len(panels)):
        frame = base.copy()
        draw = ImageDraw.Draw(frame)
        # Draw all previous panels at full opacity
        for j in range(i):
            draw_panel(draw, panels[j], theme, alpha=1.0)
        # Draw new panel at dim opacity
        draw_panel(draw, panels[i], theme, alpha=0.6)
        frames.append(frame.copy())

    # Final frame: All panels full brightness + thicker borders
    final = base.copy()
    draw = ImageDraw.Draw(final)
    for p in panels:
        draw_panel(draw, p, theme, alpha=1.0)
    frames.append(final.copy())

    # Brighten pulse frame
    pulse = base.copy()
    draw = ImageDraw.Draw(pulse)
    for p in panels:
        draw_panel(draw, p, theme, alpha=1.0)
        # Draw a subtle glow/thicker border
        t = THEMES[theme]
        x, y, w, h = p["x"], p["y"], p["w"], p["h"]
        draw.rounded_rectangle([(x - 1, y - 1), (x + w + 1, y + h + 1)],
                               radius=9, outline=t["accent"], width=3)
    frames.append(pulse.copy())

    # Save animated GIF
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    slug = card["slug"]
    filename = f"{slug}-{lang}-{theme}.gif"
    out_path = OUTPUT_DIR / filename

    # Durations: 800ms per frame, 3000ms hold on final
    durations = [800] * (len(frames) - 1) + [3000]

    frames[0].save(
        out_path, save_all=True, append_images=frames[1:],
        duration=durations, loop=0, optimize=True,
    )
    print(f"  {filename} ({len(frames)} frames, {out_path.stat().st_size // 1024}KB)")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Generate interface webcard GIFs")
    parser.add_argument("--card", required=True, choices=list(CARDS.keys()) + ["all"],
                        help="Which card to generate")
    parser.add_argument("--theme", choices=["cayman", "midnight", "all"], default="all",
                        help="Theme variant")
    args = parser.parse_args()

    cards = list(CARDS.keys()) if args.card == "all" else [args.card]
    themes = list(THEMES.keys()) if args.theme == "all" else [args.theme]

    for card_key in cards:
        print(f"\n=== {card_key} ===")
        for lang in ["en", "fr"]:
            for theme in themes:
                generate_card(card_key, lang, theme)


if __name__ == "__main__":
    main()
