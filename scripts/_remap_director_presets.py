# -*- coding: utf-8 -*-
from pathlib import Path
import re

p = Path(__file__).resolve().parents[1] / "assets" / "director.js"
t = p.read_text(encoding="utf-8")
repls = [
    ('pose: "midstride"', 'pose: "walk_midstride"'),
    ('pose: "scurve"', 'pose: "stand_scurve"'),
    ('pose: "windowsill"', 'pose: "window_pose"'),
    ('pose: "bededge"', 'pose: "bed_edge"'),
    ('pose: "power"', 'pose: "stand_power"'),
    ('pose: "sitedge"', 'pose: "sit_edge"'),
    ('pose: "yoga"', 'pose: "yoga_asana"'),
    ('pose: "look-back"', 'pose: "over_shoulder"'),
    ('pose: "mirror-stretch"', 'pose: "mirror_self"'),
    ('pose: "bed-edge"', 'pose: "bed_edge"'),
    ('pose: "sofa-curl"', 'pose: "sit_cross"'),
    ('pose: "straddle"', 'pose: "kneel"'),
    ('pose: "allfours"', 'pose: "kneel"'),
    ('pose: "standwin"', 'pose: "window_pose"'),
    ('pose: "againstwall"', 'pose: "lean"'),
    ('pose: "backlie"', 'pose: "lie_back"'),
    ('cloth: "trench"', 'cloth: "outer_coat"'),
    ('cloth: "blazer"', 'cloth: "blazer_suit"'),
    ('cloth: "knit"', 'cloth: "knit_cardigan"'),
    ('cloth: "ootd"', 'cloth: "layer_ootd"'),
    ('cloth: "sportset"', 'cloth: "sport"'),
    ('cloth: "hoodie"', 'cloth: "tee_hoodie"'),
    ('cloth: "oversized-shirt"', 'cloth: "shirt_only"'),
    ('cloth: "sleep-set"', 'cloth: "sleep"'),
    ('cloth: "cami-shorts"', 'cloth: "cami_set"'),
    ('cloth: "lace-set"', 'cloth: "lingerie"'),
    ('cloth: "e0"', 'exposure: "e0"'),
    ('cloth: "e1"', 'exposure: "e1"'),
    ('cloth: "e2"', 'exposure: "e2"'),
    ('cloth: "e3"', 'exposure: "e3"'),
    ('cloth: "e4"', 'exposure: "e4"'),
    ('set: "sidewalk"', 'set: "street_city"'),
    ('set: "window"', 'set: "window_sill"'),
    ('set: "window-city"', 'set: "window_sill"'),
    ('hair: "longblack"', 'hair: "long_straight"'),
    ('light: "openshade"', 'light: "overcast"'),
    ('light: "sheer-backlight"', 'light: "window_back"'),
    ('cam: "full34"', 'cam: "full"'),
    ('cam: "full-v"', 'cam: "full"'),
    ('cam: "lowmcu"', 'cam: "mcu"'),
    ('expr: "softsmile"', 'expr: "soft_smile"'),
    ('expr: "half-lidded"', 'expr: "half_lidded"'),
    ('expr: "bedroom"', 'expr: "bedroom_eyes"'),
    ('grade: "none"', 'grade: "natural"'),
    ('act: "display"', 'act: "solo-display"'),
]
for a, b in repls:
    t = t.replace(a, b)
# erotic presets that only set exposure: also give a cloth default nearby is hard;
# leave exposure only — findOpt will fallback for missing cloth in build if needed
p.write_text(t, encoding="utf-8")
print("ok", p)
print("e-cloth left", t.count('cloth: "e'))
print("exposure", t.count("exposure:"))
