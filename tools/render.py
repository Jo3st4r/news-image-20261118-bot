#!/usr/bin/env python3
"""Render the 1024x1024 front-page poster for news-image-20261118.

Stories (all verified from real news sources on 18 Nov 2026):
 1. APEC Summit opens in Shenzhen; Trump, Xi and Putin to hold the first
    trilateral summit on 19 Nov (rajglobalstudies.com, kalminer/thewest.com.au).
 2. Trump arrives in Manila for Quad talks with Australia, India, Japan
    (jagranjosh.com, rajglobalstudies.com).
 3. Ukraine strikes the Crimean (Kerch) Bridge a second straight night;
    a road span collapses (gtdaily.news, jagranjosh.com).
 4. Iran drones strike a US military radar in Bahrain; US hits Qeshm island;
    Kuwait intercepts drones (jagranjosh.com, gtdaily.news, mediaalertpress.com).
Ticker: Spain general strike halts ports (themunicheye.com); Gaza ceasefire
"faces collapse" warns the Board of Peace (gtdaily.news); North Korea fires
a missile into the Sea of Japan (themunicheye.com).

Run: python3 tools/render.py  ->  writes assets/entry.png (1024x1024 PNG).
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (22, 22, 22)
NAVY = (27, 42, 74)
RED = (176, 30, 36)
GOLD = (217, 164, 65)
TEAL = (14, 107, 107)
GREY = (90, 90, 90)
CARD = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_center(draw, cx, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return draw.textbbox((0, 0), text, font=fnt)[3]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---------- Masthead ----------
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.rectangle([0, 118, W, 122], fill=RED)
    draw_center(d, W // 2, 12, "T H E   W O R L D   I N   O N E   I M A G E",
                font(SANS_B, 19), (200, 205, 220))
    draw_center(d, W // 2, 38, "18 NOVEMBER 2026",
                font(SERIF_B, 56), (255, 255, 255))
    draw_center(d, W // 2, 98, "WEDNESDAY  ·  THE DAY'S WORLD NEWS IN ONE PAGE",
                font(SANS_B, 15), GOLD)

    M = 28  # side margin

    # ---------- Lead panel: APEC ----------
    x0, y0, x1, y1 = M, 134, W - M, 428
    d.rectangle([x0, y0, x1, y1], fill=CARD, outline=INK, width=2)
    d.rectangle([x0, y0, x1, y0 + 6], fill=RED)
    tx = x0 + 22
    d.text((tx, y0 + 20), "DIPLOMACY  ·  SHENZHEN, CHINA", font=font(SANS_B, 20), fill=RED)
    d.text((tx, y0 + 52), "APEC OPENS", font=font(SERIF_B, 58), fill=INK)
    d.text((tx, y0 + 114), "IN SHENZHEN", font=font(SERIF_B, 58), fill=INK)
    d.text((tx, y0 + 190),
           "Trump, Xi and Putin to hold", font=font(SANS, 25), fill=INK)
    d.text((tx, y0 + 222),
           "first-ever trilateral summit", font=font(SANS, 25), fill=INK)
    d.text((tx, y0 + 254),
           "tomorrow on APEC sidelines.", font=font(SANS, 25), fill=GREY)
    # illustration: skyline + rising sun + three flags
    ix0, ix1 = 640, x1 - 18
    iy0, iy1 = y0 + 26, y1 - 18
    d.rectangle([ix0, iy0, ix1, iy1], fill=(232, 238, 245), outline=INK, width=2)
    # sun
    d.ellipse([ix0 + 118, iy0 + 18, ix0 + 178, iy0 + 78], fill=GOLD, outline=INK, width=2)
    # buildings (kept short so the flag row above stays clear of them)
    base = iy1
    for bx, bw, bh in [(ix0 + 12, 52, 80), (ix0 + 72, 44, 100),
                       (ix0 + 124, 56, 70), (ix0 + 188, 46, 95),
                       (ix0 + 242, 52, 75)]:
        d.rectangle([bx, base - bh, bx + bw, base], fill=NAVY)
        for wy in range(base - bh + 12, base - 8, 22):
            for wx in range(bx + 8, bx + bw - 8, 18):
                d.rectangle([wx, wy, wx + 7, wy + 9], fill=GOLD)
    # three flag bars: US / China / Russia (in the sky, above the rooftops)
    fy = iy0 + 90
    # US: stripes
    d.rectangle([ix0 + 22, fy, ix0 + 62, fy + 26], fill=(255, 255, 255), outline=INK, width=1)
    for i in range(4):
        d.rectangle([ix0 + 22, fy + i * 7, ix0 + 62, fy + i * 7 + 3], fill=RED)
    d.rectangle([ix0 + 22, fy, ix0 + 40, fy + 13], fill=NAVY)
    # China: red + stars
    d.rectangle([ix0 + 72, fy, ix0 + 112, fy + 26], fill=RED, outline=INK, width=1)
    for sx, sy in [(80, 4), (92, 9), (80, 13), (94, 16), (84, 18)]:
        d.ellipse([ix0 + sx, fy + sy, ix0 + sx + 5, fy + sy + 5], fill=GOLD)
    # Russia: white/blue/red
    d.rectangle([ix0 + 122, fy, ix0 + 162, fy + 26], fill=(255, 255, 255), outline=INK, width=1)
    d.rectangle([ix0 + 122, fy + 9, ix0 + 162, fy + 17], fill=(0, 90, 180))
    d.rectangle([ix0 + 122, fy + 17, ix0 + 162, fy + 26], fill=RED)
    d.text((ix0 + 22, fy + 34), "US  ·  CHINA  ·  RUSSIA", font=font(SANS_B, 14), fill=INK)

    # ---------- Row: Quad + Crimea bridge ----------
    y2a, y2b = 442, 716
    hw = (W - 2 * M - 16) // 2

    # Quad panel (left)
    qx0, qx1 = M, M + hw
    d.rectangle([qx0, y2a, qx1, y2b], fill=CARD, outline=INK, width=2)
    d.rectangle([qx0, y2a, qx1, y2a + 5], fill=NAVY)
    d.text((qx0 + 18, y2a + 16), "SUMMIT  ·  MANILA", font=font(SANS_B, 18), fill=NAVY)
    d.text((qx0 + 18, y2a + 44), "QUAD MEETS", font=font(SERIF_B, 40), fill=INK)
    d.text((qx0 + 18, y2a + 88), "IN MANILA", font=font(SERIF_B, 40), fill=INK)
    d.text((qx0 + 18, y2a + 138), "Trump lands for talks with", font=font(SANS, 21), fill=INK)
    d.text((qx0 + 18, y2a + 162), "Australia, India and Japan.", font=font(SANS, 21), fill=GREY)
    # four overlapping circles: US blue, India orange, Japan red, Australia green
    cy = y2b - 50
    cols = [(30, 90, 180), (230, 120, 30), (200, 30, 40), (20, 130, 90)]
    labels = ["US", "IN", "JP", "AU"]
    for i, (c, lab) in enumerate(zip(cols, labels)):
        cx = qx0 + 62 + i * 96
        d.ellipse([cx - 34, cy - 34, cx + 34, cy + 34], fill=c, outline=INK, width=2)
        lw = d.textlength(lab, font=font(SANS_B, 18))
        d.text((cx - lw / 2, cy - 10), lab, font=font(SANS_B, 18), fill=(255, 255, 255))

    # Crimea bridge panel (right)
    bx0, bx1 = M + hw + 16, W - M
    d.rectangle([bx0, y2a, bx1, y2b], fill=CARD, outline=INK, width=2)
    d.rectangle([bx0, y2a, bx1, y2a + 5], fill=RED)
    d.text((bx0 + 18, y2a + 16), "WAR  ·  UKRAINE", font=font(SANS_B, 18), fill=RED)
    d.text((bx0 + 18, y2a + 44), "UKRAINE HITS", font=font(SERIF_B, 40), fill=INK)
    d.text((bx0 + 18, y2a + 88), "CRIMEA BRIDGE", font=font(SERIF_B, 40), fill=INK)
    d.text((bx0 + 18, y2a + 140), "Road span collapses after", font=font(SANS, 21), fill=INK)
    d.text((bx0 + 18, y2a + 166), "second night of strikes.", font=font(SANS, 21), fill=GREY)
    # bridge illustration: deck, towers, broken middle span, smoke
    gy = y2b - 34
    d.line([bx0 + 20, gy, bx1 - 20, gy], fill=INK, width=4)
    for txp in (bx0 + 70, bx1 - 78):
        d.line([txp, gy - 52, txp, gy], fill=INK, width=4)
    d.line([bx0 + 70, gy - 52, bx1 - 78, gy - 52], fill=INK, width=2)
    # broken span: left part level, middle piece plunging into the gap
    mid = (bx0 + bx1) // 2
    d.line([bx0 + 78, gy - 8, mid - 30, gy - 8], fill=INK, width=6)
    d.line([mid - 30, gy - 8, mid + 2, gy + 20], fill=INK, width=6)
    d.line([mid + 38, gy - 8, bx1 - 86, gy - 8], fill=INK, width=6)
    # smoke puffs over the gap
    for sx, sy, sr in [(mid - 8, gy - 34, 12), (mid + 10, gy - 48, 15), (mid + 26, gy - 30, 10)]:
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(150, 150, 150),
                  outline=GREY, width=1)

    # ---------- Bottom panel: Gulf ----------
    gx0, gx1, gy0, gy1 = M, W - M, 730, 908
    d.rectangle([gx0, gy0, gx1, gy1], fill=CARD, outline=INK, width=2)
    d.rectangle([gx0, gy0, gx1, gy0 + 5], fill=TEAL)
    d.text((gx0 + 20, gy0 + 16), "MIDDLE EAST  ·  GULF ON EDGE",
           font=font(SANS_B, 18), fill=TEAL)
    d.text((gx0 + 20, gy0 + 44), "IRAN DRONES STRIKE", font=font(SERIF_B, 40), fill=INK)
    d.text((gx0 + 20, gy0 + 88), "BAHRAIN RADAR", font=font(SERIF_B, 40), fill=INK)
    d.text((gx0 + 20, gy0 + 138), "US hits Qeshm island; Kuwait intercepts more drones.",
           font=font(SANS, 20), fill=GREY)
    # radar illustration on the right
    rx, ry = gx1 - 150, gy0 + 92
    d.line([rx, ry, rx, ry + 62], fill=INK, width=5)
    d.pieslice([rx - 58, ry - 58, rx + 58, ry + 58], start=270, end=360,
               fill=(200, 220, 225), outline=INK, width=3)
    d.line([rx, ry, rx + 44, ry - 44], fill=INK, width=3)
    for r in (30, 52):
        d.arc([rx - r, ry - r, rx + r, ry + r], start=300, end=350,
              fill=TEAL, width=3)
    # drones
    for dx, dy in [(rx + 66, ry - 52), (rx + 84, ry - 28), (rx + 62, ry - 8)]:
        d.ellipse([dx - 5, dy - 3, dx + 5, dy + 3], fill=INK)
        d.line([dx - 12, dy, dx - 6, dy], fill=INK, width=2)
        d.line([dx + 6, dy, dx + 12, dy], fill=INK, width=2)
    # sea waves
    for wy in (gy1 - 26, gy1 - 14):
        for wx in range(gx1 - 210, gx1 - 20, 28):
            d.arc([wx, wy - 6, wx + 28, wy + 6], start=180, end=360, fill=TEAL, width=2)

    # ---------- Ticker ----------
    d.rectangle([0, 922, W, H], fill=INK)
    d.text((M, 934), "ALSO TODAY", font=font(SANS_B, 18), fill=GOLD)
    tick = ("Spain general strike halts ports and factories  ·  Gaza ceasefire "
            "\u201cfaces collapse\u201d, warns Board of Peace  ·  North Korea fires "
            "missile into Sea of Japan")
    lines = wrap(d, tick, font(SANS, 19), W - 2 * M)
    yy = 958
    for ln in lines[:2]:
        d.text((M, yy), ln, font=font(SANS, 19), fill=(235, 235, 235))
        yy += 24

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "entry.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out, "PNG", optimize=True)
    print("saved", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
