# -*- coding: utf-8 -*-
from pathlib import Path
from collections import Counter
import re

root = Path(__file__).resolve().parents[1]
t = (root / "assets/combo-gallery-data.js").read_text(encoding="utf-8")
skills = Counter(re.findall(r'skill:"(\w+)"', t))
groups = Counter(re.findall(r'group:"([^"]*)"', t))
imgs = Counter(re.findall(r'img:"([^"]*)"', t))
jpg = list((root / "assets/images").glob("*.jpg"))
print("combos by skill", dict(skills), "total", sum(skills.values()))
print("unique groups", len(groups))
print("unique mapped images", len(imgs))
print("jpg files on disk", len(jpg))
print("top groups:")
for g, n in groups.most_common(12):
    print(f"  {n:4d}  {g}")
