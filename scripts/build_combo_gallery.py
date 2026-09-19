# -*- coding: utf-8 -*-
"""
从 director-catalog.js 提取全部 combo，为每个组合分配实例图路径，
写出 assets/combo-gallery-data.js 供页面与导演台使用。

规则：按 skill + group + id/label 关键词命中图池；保证每条 combo 都有 img。
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "assets" / "director-catalog.js"
OUT = ROOT / "assets" / "combo-gallery-data.js"
IMG = ROOT / "assets" / "images"

O_RE = re.compile(
    r'o\(\s*"((?:\\.|[^"\\])*)"\s*,\s*"((?:\\.|[^"\\])*)"\s*,\s*'
    r'"((?:\\.|[^"\\])*)"\s*,\s*"((?:\\.|[^"\\])*)"\s*'
    r'(?:,\s*"((?:\\.|[^"\\])*)"\s*)?\)'
)


def unesc(s: str) -> str:
    return s.replace("\\n", "\n").replace('\\"', '"').replace("\\\\", "\\")


def grab_const(text: str, name: str) -> str:
    m = re.search(rf"const\s+{name}\s*=\s*\{{", text)
    if not m:
        raise ValueError(name)
    start = m.end() - 1
    depth = 0
    for i, ch in enumerate(text[start:], start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    raise ValueError(f"unclosed {name}")


def parse_combos(obj_src: str) -> list[dict]:
    m = re.search(r"combo\s*:\s*\[", obj_src)
    if not m:
        return []
    i = m.end() - 1
    depth = 0
    for j, ch in enumerate(obj_src[i:], i):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                body = obj_src[i : j + 1]
                break
    else:
        return []
    items = []
    for om in O_RE.finditer(body):
        items.append(
            {
                "id": unesc(om.group(1)),
                "label": unesc(om.group(2)),
                "en": unesc(om.group(3)),
                "group": unesc(om.group(4)),
                "look": unesc(om.group(5) or ""),
            }
        )
    return items


def existing(name: str) -> str | None:
    p = IMG / name
    return f"assets/images/{name}" if p.is_file() else None


# 图池：文件名 → 关键词（命中 id/label/group）
POOL_RULES: list[tuple[str, list[str]]] = [
    # Figure
    ("fg-street-midstride.jpg", ["street", "midstride", "街拍", "纪实", "ootd", "stride", "denim"]),
    ("fg-metro-commute.jpg", ["metro", "commute", "地铁", "通勤", "train"]),
    ("fg-editorial.jpg", ["editorial", "fashion", "lookbook", "scurve", "s-curve", "时尚", "商业", "campaign", "runway"]),
    ("fg-yoga.jpg", ["yoga", "fitness", "sport", "瑜伽", "运动", "run", "climb", "athlete", "cycle", "martial"]),
    ("fg-travel.jpg", ["travel", "旅", "land", "golden-hour-land", "scenic", "ridge", "underwater", "aerial"]),
    ("fg-beauty.jpg", ["beauty", "clam", "美妆", "macro", "glass", "headshot"]),
    ("street-ootd.jpg", ["urban", "night-neon", "rain", "crosswalk", "geometry"]),
    ("beauty-glass.jpg", ["kr", "korean", "水光", "beauty"]),
    ("yoga-sport.jpg", ["bodybuilding", "gym", "sport"]),
    ("home-soft.jpg", ["home", "boudoir-soft", "居家", "私房", "soft-sfw", "heya"]),
    # Youth
    ("ys-window-lace.jpg", ["window", "lace", "窗", "纱", "curtain", "overshoulder", "look-back", "qingleng"]),
    ("ys-mirror-shirt.jpg", ["mirror", "shirt", "boyfriend", "镜", "衬衫", "self-gaze"]),
    ("ys-bed-soft.jpg", ["bed", "sheet", "床", "morning-sheet", "side-lie"]),
    ("ys-sofa-phone.jpg", ["sofa", "phone", "沙发", "scroll", "lazy"]),
    ("ys-wet-hair.jpg", ["wet", "bath", "蒸汽", "wet-hair", "towel", "after-bath", "fog"]),
    ("ys-softlife.jpg", ["softlife", "soft-life", "vanilla", "cream", "coffee", "金辉", "golden"]),
    ("nsfw-window-back.jpg", ["balcony", "dusk", "阳台"]),
    ("nsfw-robe-hotel.jpg", ["hotel", "robe", "酒店", "arrival"]),
    # Erotic (atmosphere)
    ("er-hotel-robe.jpg", ["hotel", "robe", "japanese-hotel", "钨丝", "tungsten"]),
    ("er-bed-edge.jpg", ["bed", "edge", "display", "自展", "half", "e1", "e2"]),
    ("er-window-sheer.jpg", ["window", "sheer", "窗", "silhouette"]),
    ("er-neon-night.jpg", ["neon", "霓虹", "night", "apartment"]),
    ("er-bath-steam.jpg", ["bath", "steam", "浴", "shower", "towel"]),
    ("er-slip-sofa.jpg", ["slip", "sofa", "丝", "couch"]),
    ("nsfw-stockings-shirt.jpg", ["stocking", "丝袜", "shirt", "半褪"]),
    ("nsfw-hands-sheet.jpg", ["hand", "sheet", "手", "床单"]),
    ("nsfw-choker-detail.jpg", ["choker", "项圈", "collar", "detail"]),
    ("nsfw-bed-stilllife.jpg", ["still", "prop", "道具", "messy"]),
    ("nsfw-mirror-shirt.jpg", ["mirror", "镜"]),
    ("nsfw-neon-reflection.jpg", ["neon", "reflect"]),
    ("hotel-mood.jpg", ["hotel", "mood"]),
    ("erotic-abstract.jpg", ["fantasy", "幻想", "tentacle", "magic", "ahegao", "futanari"]),
]

DEFAULTS = {
    "figure": "fg-street-midstride.jpg",
    "youth": "ys-window-lace.jpg",
    "erotic": "er-hotel-robe.jpg",
}

GROUP_FALLBACK = [
    (["A 商业", "时尚", "lookbook", "beauty"], "fg-editorial.jpg"),
    (["B 纪实", "街拍", "街"], "fg-street-midstride.jpg"),
    (["C 运动", "体能"], "fg-yoga.jpg"),
    (["D 表演", "舞台", "舞"], "fg-editorial.jpg"),
    (["E 职业"], "fg-metro-commute.jpg"),
    (["F 艺术", "黑白"], "fg-beauty.jpg"),
    (["G 生活", "旅", "关系"], "fg-travel.jpg"),
    (["H 特殊"], "fg-travel.jpg"),
    (["I 私房", "boudoir"], "home-soft.jpg"),
    (["常青"], "ys-window-lace.jpg"),
    (["全网"], "ys-sofa-phone.jpg"),
    (["垂类"], "ys-softlife.jpg"),
    (["出片", "HMCP", "妆"], "ys-mirror-shirt.jpg"),
    (["场景"], "ys-bed-soft.jpg"),
    (["镜头"], "fg-beauty.jpg"),
    (["权力", "玩法"], "er-bed-edge.jpg"),
    (["情境", "叙事"], "er-hotel-robe.jpg"),
    (["幻想", "二次元", "非现实"], "erotic-abstract.jpg"),
    (["竖屏"], "er-slip-sofa.jpg"),
    (["东亚", "出片"], "er-hotel-robe.jpg"),
]


SKILL_POOLS = {
    "figure": [
        "fg-street-midstride.jpg",
        "fg-metro-commute.jpg",
        "fg-editorial.jpg",
        "fg-yoga.jpg",
        "fg-travel.jpg",
        "fg-beauty.jpg",
        "street-ootd.jpg",
        "beauty-glass.jpg",
        "yoga-sport.jpg",
        "home-soft.jpg",
    ],
    "youth": [
        "ys-window-lace.jpg",
        "ys-mirror-shirt.jpg",
        "ys-bed-soft.jpg",
        "ys-sofa-phone.jpg",
        "ys-wet-hair.jpg",
        "ys-softlife.jpg",
        "nsfw-window-back.jpg",
        "nsfw-robe-hotel.jpg",
        "home-soft.jpg",
    ],
    "erotic": [
        "er-hotel-robe.jpg",
        "er-bed-edge.jpg",
        "er-window-sheer.jpg",
        "er-neon-night.jpg",
        "er-bath-steam.jpg",
        "er-slip-sofa.jpg",
        "nsfw-stockings-shirt.jpg",
        "nsfw-hands-sheet.jpg",
        "nsfw-choker-detail.jpg",
        "nsfw-bed-stilllife.jpg",
        "nsfw-mirror-shirt.jpg",
        "nsfw-neon-reflection.jpg",
        "hotel-mood.jpg",
        "erotic-abstract.jpg",
    ],
}


def _hash_pick(key: str, pool: list[str]) -> str:
    h = sum(ord(c) for c in key) + len(key) * 17
    usable = [f for f in pool if existing(f)]
    if not usable:
        return DEFAULTS.get("figure", "hero-banner.jpg")
    return usable[h % len(usable)]


def _slug_hash(s: str) -> str:
    import hashlib

    h = hashlib.md5(s.encode("utf-8")).hexdigest()[:8]
    s2 = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    s2 = re.sub(r"-+", "-", s2)
    if len(s2) < 2:
        s2 = "g"
    return f"{s2[:24]}-{h}"


def pick_img(skill: str, item: dict) -> str:
    """优先级：每条组合独图 > 分组封面 > 关键词池 > 散列池。"""
    cid = item.get("id") or ""
    g = item.get("group") or ""
    body = cid.replace("combo-", "")
    hot_name = f"hot-{skill}-{_slug_hash(body)}.jpg"
    if existing(hot_name):
        return f"assets/images/{hot_name}"

    grp_name = f"grp-{skill}-{_slug_hash(g)}.jpg"
    if existing(grp_name):
        return f"assets/images/{grp_name}"

    blob = f"{cid} {item['label']} {g} {item['en']}".lower()
    best = None
    best_score = 0
    for fname, kws in POOL_RULES:
        if not existing(fname):
            continue
        score = sum(1 for k in kws if k.lower() in blob)
        if score > best_score:
            best_score = score
            best = fname
    if best_score >= 2 and best:
        return f"assets/images/{best}"
    for keys, fname in GROUP_FALLBACK:
        if any(k in g for k in keys) and existing(fname):
            return f"assets/images/{fname}"
    if best_score > 0 and best:
        return f"assets/images/{best}"
    fname = _hash_pick(cid + g, SKILL_POOLS.get(skill, []))
    return f"assets/images/{fname}"


def js_escape(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\r", "")
    )


def _load_prompts() -> dict[str, str]:
    """scripts/combo-prompts.json（存在时）→ {"skill:combo-id": prompt}。"""
    import json as _json

    p = ROOT / "scripts" / "combo-prompts.json"
    if not p.is_file():
        return {}
    try:
        data = _json.loads(p.read_text(encoding="utf-8"))
        return {
            k: v.get("prompt", "")
            for k, v in (data.get("items") or {}).items()
            if v.get("prompt")
        }
    except (ValueError, OSError):
        return {}


def main() -> int:
    text = CAT.read_text(encoding="utf-8")
    prompts = _load_prompts()
    packs = []
    for skill, const in (("figure", "FIGURE"), ("youth", "YOUTH"), ("erotic", "EROTIC")):
        obj = grab_const(text, const)
        combos = parse_combos(obj)
        for c in combos:
            packs.append(
                {
                    "skill": skill,
                    "id": c["id"],
                    "label": c["label"],
                    "group": c["group"],
                    "en": c["en"],
                    "look": c["look"],
                    "prompt": prompts.get(f"{skill}:{c['id']}", ""),
                    "img": pick_img(skill, c),
                }
            )
        print(f"[{skill}] combos={len(combos)}")

    # group stats
    from collections import Counter

    print("[img usage top]")
    ctr = Counter(p["img"] for p in packs)
    for img, n in ctr.most_common(12):
        print(f"  {n:4d}  {img}")

    lines = [
        "/** AUTO-GENERATED by scripts/build_combo_gallery.py — 勿手改 */",
        "window.COMBO_GALLERY = {",
        f"  generatedAt: {__import__('time').strftime('%Y%m%d')},",
        f"  total: {len(packs)},",
        "  items: [",
    ]
    for p in packs:
        lines.append(
            "    {"
            f'skill:"{p["skill"]}",'
            f'id:"{js_escape(p["id"])}",'
            f'label:"{js_escape(p["label"])}",'
            f'group:"{js_escape(p["group"])}",'
            f'look:"{js_escape(p["look"])}",'
            f'prompt:"{js_escape(p["prompt"])}",'
            f'img:"{js_escape(p["img"])}"'
            "},"
        )
    lines.append("  ],")
    lines.append("};")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[ok] {OUT} total={len(packs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
