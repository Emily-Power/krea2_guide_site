# -*- coding: utf-8 -*-
import re
from pathlib import Path
from collections import Counter

t = Path(__file__).resolve().parents[1].joinpath("assets/combo-gallery-data.js").read_text(
    encoding="utf-8"
)
imgs = re.findall(r'img:"([^"]+)"', t)
print("unique images in map", len(set(imgs)))
print("hot refs", sum(1 for i in imgs if "/hot-" in i))
print("grp refs", sum(1 for i in imgs if "/grp-" in i))
print("other", sum(1 for i in imgs if "/hot-" not in i and "/grp-" not in i))
print("total combos", len(imgs))
print("top 8", Counter(imgs).most_common(8))
img_dir = Path(__file__).resolve().parents[1] / "assets/images"
print("grp files", len(list(img_dir.glob("grp-*.jpg"))))
print("hot files", len(list(img_dir.glob("hot-*.jpg"))))
