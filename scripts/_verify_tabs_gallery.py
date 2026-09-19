# -*- coding: utf-8 -*-
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
html = (root / "index.html").read_text(encoding="utf-8")
assert "skill-figure" in html and "skill-youth" in html and "skill-erotic" in html
assert "skill-tab" in html and "skill-panel" in html
assert "combo-gallery" in html
assert "combo-gallery-data.js" in html
# sidebar should NOT list 菜单全图 as top-level under figure group
assert html.count('href="#figure-menu"') == 0 or 'data-skill-tab' in html
# nav compact
assert "三大 Skill" in html
assert html.count("菜单全图") >= 3  # tabs still have the label

data = (root / "assets/combo-gallery-data.js").read_text(encoding="utf-8")
assert "total: 674" in data or "total:674" in data.replace(" ", "")
# count items
n = data.count('skill:"')
print("gallery items", n)
print("shells ok, tabs ok, total combos", n)
print("ALL VERIFY OK")
