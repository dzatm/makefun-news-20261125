#!/usr/bin/env python3
"""Draw the 25 November 2026 front page: THE WORLD - IN ONE IMAGE.

The page is built entirely from fixed text and fixed geometry: no clock,
no randomness, no network. Running this script twice writes the same
bytes to entry.png every time.
"""
import hashlib
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

PAGE_W, PAGE_H = 1024, 1024
MARGIN = 48
PAPER = (248, 243, 232)
INK = (18, 18, 18)
CRIMSON = (164, 24, 34)
MUTED = (98, 94, 86)
FAINT = (182, 176, 164)
SKY = (214, 222, 228)
AMBER = (214, 126, 32)

FONTS = Path("/usr/share/fonts/truetype/dejavu")


def load(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def serif_bold(size):
    return load("DejaVuSerif-Bold.ttf", size)


def sans(size):
    return load("DejaVuSans.ttf", size)


def sans_bold(size):
    return load("DejaVuSans-Bold.ttf", size)


EDITION = "WEDNESDAY, 25 NOVEMBER 2026"

LEAD = {
    "kicker": "MIDDLE EAST  ·  RIYADH",
    "headline": "HOUTHIS HIT RIYADH TOWER AGAIN",
    "deck": "Second strike in five days on Riyadh's tallest tower wounds "
            "11; Hodeidah told to evacuate.",
}

GRID = [
    ("UNITED STATES  ·  NEW YORK",
     "HUAWEI CONVICTED IN US TRIAL",
     "A Brooklyn jury finds the tech giant guilty on 10 of 12 counts, "
     "including trade-secret theft and bank fraud."),
    ("UKRAINE  ·  BLACK SEA",
     "KYIV HITS RUSSIAN SHIPS IN TWO SEAS",
     "Zelenskiy confirms the Gulf of Finland strike as Putin vows "
     "retaliation; Kyiv also claims a warship sunk off Libya."),
    ("NATO  ·  POLAND",
     "NATO SENDS EARLY-WARNING JETS TO POLAND",
     "The alliance will deploy surveillance aircraft after missiles "
     "landed in Poland during an attack on Ukraine."),
    ("MARKETS  ·  AI STOCKS",
     "AI STOCKS SLIDE AS RALLY FADES",
     "Nvidia falls about 7% a day after Huang's return; Anthropic "
     "drops below its $83 IPO price."),
    ("IRAN  ·  STRAIT OF HORMUZ",
     "IRAN SAYS TANKERS HIT BY MINES",
     "The Revolutionary Guard Navy says three oil tankers were struck "
     "by naval mines in the strait."),
    ("NEPAL",
     "QUAKE OF 5.6 SHAKES NEPAL'S EAST",
     "A magnitude 5.6 earthquake strikes Koshi Province near the "
     "Chinese border."),
]

SOURCES = ("Compiled 25 November 2026  ·  Sources: Reuters · AP · AFP · "
           "Al Jazeera · BBC")


class Page:
    """A thin wrapper around Pillow's drawing context."""

    def __init__(self):
        self.img = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
        self.d = ImageDraw.Draw(self.img)

    def rule(self, y, weight=2, colour=INK, left=MARGIN, right=None):
        self.d.rectangle(
            [left, y, (right or PAGE_W - MARGIN), y + weight - 1], fill=colour)

    def wrapped(self, text, font, max_width):
        """Split text into lines that fit max_width, word by word."""
        lines, current = [], ""
        for word in text.split():
            trial = (current + " " + word).strip()
            if self.d.textlength(trial, font=font) <= max_width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        return lines

    def paragraph(self, x, y, text, font, width, leading, colour=INK):
        for line in self.wrapped(text, font, width):
            self.d.text((x, y), line, font=font, fill=colour, anchor="la")
            y += leading
        return y

    def centre(self, y, text, font, colour=INK):
        self.d.text((PAGE_W / 2, y), text, font=font, fill=colour,
                    anchor="ma")


def burst(draw, cx, cy, outer, inner, colour):
    """A simple starburst: alternating long and short spikes."""
    import math
    points = []
    for i in range(16):
        angle = math.pi * i / 8
        radius = outer if i % 2 == 0 else inner
        points.append((cx + radius * math.cos(angle),
                       cy + radius * math.sin(angle)))
    draw.polygon(points, fill=colour)


def draw_skyline(page, x0, y0, x1, y1):
    """A small skyline of the financial district with a hit tower."""
    d = page.d
    d.rectangle([x0, y0, x1, y1], fill=SKY)
    d.rectangle([x0, y1 - 8, x1, y1], fill=INK)
    # Background towers, left to right: (start, height, end, colour).
    towers = [
        (0.02, 0.52, 0.13, MUTED),
        (0.15, 0.34, 0.26, (140, 136, 128)),
        (0.28, 0.44, 0.38, MUTED),
        (0.60, 0.40, 0.71, (140, 136, 128)),
        (0.73, 0.55, 0.84, MUTED),
        (0.86, 0.30, 0.97, (140, 136, 128)),
    ]
    span = x1 - x0
    for frac_x, frac_h, frac_end, colour in towers:
        tx = x0 + frac_x * span
        tw = (frac_end - frac_x) * span
        th = frac_h * (y1 - y0)
        d.rectangle([tx, y1 - 8 - th, tx + tw, y1 - 8], fill=colour)
    # The tall PIF tower in the middle, slightly tapered.
    tx0, tx1 = x0 + 0.40 * span, x0 + 0.58 * span
    top = y0 + 0.10 * (y1 - y0)
    d.polygon([(tx0, y1 - 8), (tx0 + 4, top), (tx1 - 4, top),
               (tx1, y1 - 8)], fill=INK)
    # Impact burst near the tower's crown, with drifting smoke.
    burst(d, (tx0 + tx1) / 2, top + 18, 34, 14, AMBER)
    burst(d, (tx0 + tx1) / 2, top + 18, 20, 8, CRIMSON)
    for sx, sy, r in [(0.30, 0.16, 5), (0.24, 0.24, 4), (0.70, 0.12, 5)]:
        d.ellipse([x0 + sx * span - r, y0 + sy * (y1 - y0) - r,
                   x0 + sx * span + r, y0 + sy * (y1 - y0) + r],
                  fill=(120, 116, 108))
    d.text((x0 + 6, y1 - 26), "RIYADH  ·  PIF TOWER", font=sans_bold(14),
           fill=(255, 255, 255), anchor="la")


def draw_masthead(page):
    page.rule(22, 6)
    page.rule(32, 2)
    page.d.text((PAGE_W / 2, 44), "THE WORLD", font=serif_bold(80),
                fill=INK, anchor="ma")
    page.centre(132, "— IN ONE IMAGE —", sans_bold(22))
    page.d.text((MARGIN, 164), EDITION, font=sans_bold(19), fill=INK,
                anchor="la")
    page.d.text((PAGE_W - MARGIN, 164), "ONE DAY · ONE PAGE",
                font=sans(19), fill=MUTED, anchor="ra")
    page.rule(194, 4)


def draw_lead(page):
    d = page.d
    text_w = 620
    d.text((MARGIN, 210), LEAD["kicker"], font=sans_bold(21), fill=CRIMSON,
           anchor="la")
    y = 238
    y = page.paragraph(MARGIN, y, LEAD["headline"], serif_bold(46),
                       text_w, 54)
    y += 8
    y = page.paragraph(MARGIN, y, LEAD["deck"], sans(21), text_w, 27,
                       colour=(38, 38, 38))
    draw_skyline(page, 688, 210, PAGE_W - MARGIN, 388)
    return max(y, 400)


def draw_grid(page, top):
    d = page.d
    col_w = (PAGE_W - 2 * MARGIN - 28) // 2
    row_h = (948 - top) // 3
    for i, (kicker, headline, summary) in enumerate(GRID):
        col, row = i % 2, i // 2
        x = MARGIN + col * (col_w + 28)
        y = top + row * row_h
        d.rectangle([x, y + 4, x + 9, y + 13], fill=CRIMSON)
        d.text((x + 18, y), kicker, font=sans_bold(16), fill=CRIMSON,
               anchor="la")
        y += 28
        y = page.paragraph(x, y, headline, serif_bold(23), col_w, 28)
        y += 3
        page.paragraph(x, y, summary, sans(16), col_w, 21, colour=MUTED)
    # Dividers: one vertical, two horizontal.
    d.line([PAGE_W // 2, top, PAGE_W // 2, 948], fill=FAINT, width=1)
    page.rule(top + row_h - 2, 1, FAINT)
    page.rule(top + 2 * row_h - 2, 1, FAINT)


def build():
    page = Page()
    draw_masthead(page)
    bottom = draw_lead(page)
    page.rule(bottom + 14, 2)
    draw_grid(page, bottom + 36)
    page.rule(960, 2)
    page.centre(972, SOURCES, sans(15), MUTED)
    return page.img


def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else \
        Path(__file__).with_name("entry.png")
    build().save(target, format="PNG")
    blob = target.read_bytes()
    print(f"WROTE {target} {len(blob)} bytes "
          f"sha256={hashlib.sha256(blob).hexdigest()}")


if __name__ == "__main__":
    main()
