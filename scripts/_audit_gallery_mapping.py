# -*- coding: utf-8 -*-
"""一次性审计：674 图映射完整性（悬空引用 / 孤儿文件 / prompt 一致性 / skill 归属 / 损坏 / 字节重复）。"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "images"
GALLERY = ROOT / "assets" / "combo-gallery-data.js"
PROMPTS = ROOT / "scripts" / "combo-prompts.json"

ISSUES: list[str] = []


def check(name: str, bad: list[str], cap: int = 25) -> None:
    if bad:
        ISSUES.append(f"[{name}] {len(bad)} 处问题")
        for b in bad[:cap]:
            ISSUES.append(f"    {b}")
        if len(bad) > cap:
            ISSUES.append(f"    …还有 {len(bad) - cap} 处")


# 1. 解析 gallery（JS 对象字面量：逐对象提取 + 键加引号）
src = GALLERY.read_text(encoding="utf-8")
_total_decl = re.search(r"total:\s*(\d+)", src)
print(f"gallery total 声明 {_total_decl.group(1) if _total_decl else '?'}")


def _js_objs(body: str):
    objs, depth, start = [], 0, -1
    in_str = False
    for i, ch in enumerate(body):
        if ch == '"' and (i == 0 or body[i - 1] != "\\"):
            in_str = not in_str
        elif not in_str:
            if ch == "{":
                if depth == 0:
                    start = i
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0 and start >= 0:
                    objs.append(body[start : i + 1])
    return objs


items_src = re.search(r"items:\s*\[(.*)\]", src, re.S).group(1)
items = []
for raw in _js_objs(items_src):
    fixed = re.sub(r'([,{]\s*)(\w+)\s*:', r'\1"\2":', raw)
    items.append(json.loads(fixed))
print(f"实际条目 {len(items)}")

# 2. 悬空引用 / 重复引用
img_refs = [it["img"] for it in items]
missing = sorted({r for r in img_refs if not (ROOT / r).is_file()})
dup_refs = sorted({r for r, n in Counter(img_refs).items() if n > 1})
check("悬空引用(文件不存在)", missing)
check("重复引用(多combo同图)", [f"{r} ×{Counter(img_refs)[r]}" for r in dup_refs])

# 3. 孤儿文件：磁盘 hot-*/grp-* 但未被引用
ref_names = {Path(r).name for r in img_refs}
disk = {p.name for p in IMG.glob("*.jpg") if p.is_file()}
orphan = sorted(disk - ref_names - {
    "hero-banner.jpg", "home-soft.jpg", "beauty-glass.jpg",  # 站级/备用图，不参与 combo
})
check("孤儿文件(未被任何 combo 引用)", orphan)

# 4. prompt 一致性：gallery prompt vs combo-prompts.json
try:
    pdata = json.loads(PROMPTS.read_text(encoding="utf-8"))
    pitems = pdata.get("items") or {}
    print(f"combo-prompts.json: gen={pdata.get('gen')}, items={len(pitems)}")
    st = Counter(v.get("status") for v in pitems.values())
    tr = Counter(int(v.get("tries") or 0) for v in pitems.values())
    print(f"status 分布: {dict(st)}  tries 分布: {dict(tr)}")
    pmap = {k: v.get("prompt", "") for k, v in pitems.items()}
    mismatch_prompt = []
    gallery_keys = {f"{it['skill']}:{it['id']}" for it in items}
    for it in items:
        k = f"{it['skill']}:{it['id']}"
        if pmap.get(k) and pmap[k] != it["prompt"]:
            mismatch_prompt.append(k)
    check("gallery prompt ≠ combo-prompts.json", mismatch_prompt)
    notdone = [k for k, v in pitems.items() if v.get("status") != "done" and k in gallery_keys]
    check("prompts.json 状态非 done 但已被 gallery 引用", notdone)
    # prompts.json 有 key 但 gallery 没有（catalog 改动后不同步）
    extra_keys = sorted(set(pmap) - gallery_keys)
    check("prompts.json 有但 gallery 无的 key", extra_keys)
    # gallery 有但 prompts.json 无（prompt 为空的条目）
    no_prompt = [f"{it['skill']}:{it['id']}" for it in items if not it.get("prompt")]
    check("gallery 条目 prompt 为空", no_prompt)
except (ValueError, OSError) as e:
    print(f"[err] prompts.json 读取失败: {e}")

# 5. skill 归属：item.skill vs 文件名 hot-{skill}- 前缀
skill_mismatch = [
    f"{it['skill']}:{it['id']} -> {it['img']}"
    for it in items
    if Path(it["img"]).name.startswith("hot-") and not Path(it["img"]).name.startswith(f"hot-{it['skill']}-")
]
check("skill 与文件名前缀不符", skill_mismatch)

# 6. 文件名与 combo id 的 hash 一致性：用 build_combo_gallery 的 _slug_hash 重算
import importlib.util

spec = importlib.util.spec_from_file_location("bcg", ROOT / "scripts" / "build_combo_gallery.py")
bcg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bcg)
name_mismatch = [
    f"{it['skill']}:{it['id']} 应为 hot-{it['skill']}-{bcg._slug_hash(it['id'].replace('combo-', ''))}.jpg 实际 {Path(it['img']).name}"
    for it in items
    if it["img"].endswith(".jpg") and Path(it["img"]).name.startswith("hot-")
    and Path(it["img"]).name != f"hot-{it['skill']}-{bcg._slug_hash(it['id'].replace('combo-', ''))}.jpg"
]
check("文件名 hash 与 combo id 不符", name_mismatch)

# 7. 文件完整性 + 尺寸 + 字节重复
from PIL import Image

# 有意裁切特例（Krea2 景别服从弱，headshot 经 seed 扫描挑优后底部裁切收景）
KNOWN_CROP = {"hot-figure-headshot-clean-6f6e55e0.jpg"}
size_bad: list[str] = []
md5map: dict[str, list[str]] = {}
for p in sorted(IMG.glob("*.jpg")):
    if p.name.startswith(("hero-banner", "home-soft", "beauty-glass")):
        continue
    try:
        md5 = hashlib.md5(p.read_bytes()).hexdigest()
        md5map.setdefault(md5, []).append(p.name)
        with Image.open(p) as im:
            w, h = im.size
            if p.name in KNOWN_CROP:
                continue
            if not (0.70 < w / h < 0.78):  # 3:4 ≈ 0.75
                size_bad.append(f"{p.name} {w}×{h} 比例{w/h:.3f}")
    except Exception as e:
        size_bad.append(f"{p.name} 无法打开: {e}")
check("比例异常或损坏", size_bad)
dupe_content = [v for v in md5map.values() if len(v) > 1]
check("不同文件名字节完全相同", [" / ".join(v) for v in dupe_content])

print()
print("=" * 60)
if ISSUES:
    print("发现以下问题：")
    print("\n".join(ISSUES))
else:
    print("全部通过：无悬空、无孤儿、prompt 一致、skill 归属一致、无损坏、无字节重复")
