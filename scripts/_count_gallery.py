# -*- coding: utf-8 -*-
import re
from collections import Counter
from pathlib import Path

t = Path(__file__).resolve().parents[1].joinpath("assets/combo-gallery-data.js").read_text(encoding="utf-8")
imgs = re.findall(r'img:"([^"]+)"', t)
print("items", len(imgs), "unique", len(set(imgs)))
print("top")
for i, n in Counter(imgs).most_common(10):
    print(n, i)
print("singletons", sum(1 for n in Counter(imgs).values() if n == 1))
