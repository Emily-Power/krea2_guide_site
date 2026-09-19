# -*- coding: utf-8 -*-
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
cat = (root / "assets/director-catalog.js").read_text(encoding="utf-8")
js = (root / "assets/director.js").read_text(encoding="utf-8")
html = (root / "index.html").read_text(encoding="utf-8")
st = json.loads((root / "scripts/director-catalog.static.json").read_text(encoding="utf-8"))
img = root / "assets/images"

assert "const YOUTH" in cat
assert "return { FIGURE, EROTIC, YOUTH, SUBJECT" in cat
assert "FIELD_GROUPS_YOUTH" in js
assert "PRESETS_YOUTH" in js
assert "mode-youth" in js
assert "/youth-seduction-prompt" in js
assert 'data-mode="youth"' in html
assert 'id="youth"' in html
assert "ys-window-lace.jpg" in html
assert "YOUTH" in st

for n in [
    "ys-window-lace",
    "ys-mirror-shirt",
    "ys-bed-soft",
    "ys-sofa-phone",
    "ys-wet-hair",
    "ys-softlife",
]:
    p = img / f"{n}.jpg"
    assert p.is_file() and p.stat().st_size > 10000, n

yi = cat.find("const YOUTH")
si = cat.find("const SUBJECT")
youth_combos = cat[yi:si].count('o("combo-')
print("ALL CHECKS OK")
print("YOUTH.combo ~", youth_combos)
print("YOUTH fields", list(st["YOUTH"]))
print("PRESETS_YOUTH count", js.count('id: "sunset-lace"') + js.count('id: "mirror-shirt"'))
