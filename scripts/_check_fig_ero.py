# -*- coding: utf-8 -*-
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
t = (root / "index.html").read_text(encoding="utf-8")
ids = re.findall(r'<section id="([^"]+)"', t)
print("sections:", ids)
for s in [
    "figure-menu",
    "figure-gallery",
    "figure-order",
    "erotic-menu",
    "erotic-order",
    "fg-street-midstride",
    "er-hotel-robe",
]:
    print(s, s in t)
img = root / "assets/images"
for n in [
    "fg-street-midstride",
    "fg-metro-commute",
    "fg-editorial",
    "fg-yoga",
    "fg-travel",
    "fg-beauty",
    "er-hotel-robe",
    "er-window-sheer",
    "er-bed-edge",
    "er-neon-night",
    "er-bath-steam",
    "er-slip-sofa",
]:
    p = img / f"{n}.jpg"
    print("img", n, p.is_file(), p.stat().st_size if p.is_file() else 0)
