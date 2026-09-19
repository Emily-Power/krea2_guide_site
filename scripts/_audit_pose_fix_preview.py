# -*- coding: utf-8 -*-
"""预演：pose 匹配词边界修复 + 删中文单字"动"/"滑雪" + wardrobe 传 scene_cls 后，受影响条目清单。只读不写。"""
from __future__ import annotations

import importlib.util
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = __import__("pathlib").Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("cp", ROOT / "scripts" / "combo_prompts.py")
cp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cp)

ASCII_KW = re.compile(r"^[a-z]+$")


def kw_hit(kw: str, blob: str) -> bool:
    """修复版关键词命中：ASCII 词用词边界；中文仅弃用"动"与"滑雪"两个污染源。"""
    if ASCII_KW.match(kw):
        return re.search(rf"\b{re.escape(kw)}\b", blob) is not None
    if kw in ("动", "滑雪"):
        return False
    return kw in blob


def pose_variant_fixed(skill, item, gen):
    blob = f"{item['label']} {item['look']} {item['id']} {item['en']}".lower()
    for kws, phrases in cp.POSE_LOOK:
        for kw in kws:
            if kw_hit(kw, blob):
                return cp.pick(skill, item["id"], f"pose:{kw}", gen, phrases)
    pool = cp.POSE_DEFAULT[skill]
    return cp.pick(skill, item["id"], "pose", gen, pool)


def wardrobe_variant_fixed(skill, item, gen, scene_cls=""):
    cls = cp.class_of(skill, item, cp.WARDROBE)
    if cls is None:
        pool = cp.WARDROBE_BY_SCENE.get(skill, {}).get(scene_cls) or [cp.WARDROBE_DEFAULT[skill]]
        cls = cp.pick(skill, item["id"], "wardrobe-fb", gen, pool)
    variants = next((v for _k, c, v in cp.WARDROBE.get(skill, []) if c == cls), None) or []
    return cls, cp.pick(skill, item["id"], "wardrobe", gen, variants)


data = json.loads((ROOT / "scripts" / "combo-prompts.json").read_text(encoding="utf-8"))
gen = data["gen"]
items = {f"{it['skill']}:{it['id']}": it for it in cp.all_combos()}

pose_changed, ward_changed, both = [], [], []
for key, old in data["items"].items():
    it = items[key]
    fix = cp.DIM_FIX.get(key) or {}
    new_pose = fix.get("pose") or pose_variant_fixed(it["skill"], it, gen)
    scene_cls = fix.get("scene") or old["dims"]["scene"]
    _wc, _outfit = wardrobe_variant_fixed(it["skill"], it, gen, scene_cls)
    p = new_pose != old["dims"]["pose"]
    w = _wc != old["dims"]["wardrobe"]
    if p and w:
        both.append((key, old["dims"]["pose"], new_pose, old["dims"]["wardrobe"], _wc))
    elif p:
        pose_changed.append((key, old["dims"]["pose"], new_pose))
    elif w:
        ward_changed.append((key, old["dims"]["wardrobe"], _wc))

print(f"pose 变化 {len(pose_changed)} 条 / wardrobe 变化 {len(ward_changed)} 条 / 同时变化 {len(both)} 条")
print()
print("=== 姿态变化清单 ===")
for key, old, new in pose_changed + [(k, o, n) for k, o, n, _, _ in both]:
    print(f"  {key} ({data['items'][key]['label']})")
    print(f"    旧: {old}")
    print(f"    新: {new}")
print()
print("=== wardrobe 成套修复（前 20 条示例）===")
for key, old, new in (ward_changed + [(k, o, n) for k, o, n, _, _ in both])[:20]:
    print(f"  {key} ({data['items'][key]['label']}): {old} -> {new}")
if len(ward_changed) > 20:
    print(f"  …共 {len(ward_changed)} 条")
