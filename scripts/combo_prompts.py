# -*- coding: utf-8 -*-
"""
674 条组合包的差异化形态 A 散文生成器（确定性、可复现、纯标准库）。

设计（与 assets/prose-templates.js 同版式铁律）：
- 四段纯英文：This is a… / Main subject: / Environmental background: / Composition and atmosphere:
- 六个差异化维度（scene/wardrobe/light/pose/cam/grade），每维独立 md5 salt + gen 代际轮换；
- 变体选择 = h(skill, id, dim, gen) % len(pool)，同组同维五元组碰撞率超阈值时打印警告；
- 角色锁 = 纯文字 LOCK（不挂 LoRA）；提示词持久化到 scripts/combo-prompts.json，
  供 build_combo_gallery.py 写入 gallery 数据（lightbox「复制英文提示词」）与 regen 出图消费。
- 2026-09-08 对齐三 skill 锚生态铁律：无锚场景走 SCENE_FALLBACK 伪随机取模（禁恒取默认行）；
  衣着无锚走 WARDROBE_BY_SCENE 与场景成套协调；light/grade 按锚生态纪律
  （酒店钨丝=暖金+酒红点缀、love-hotel=品红青撞色、纯欲=奶油白/淡粉暖钨丝、白月光=冷白少彩、
  figure 街拍=低饱和淡人色）；场景类含 love-hotel/beach/ice-rink/wedding/ballet/bath。

用法：
  python scripts/combo_prompts.py --gen 2          # 生成 + 写 combo-prompts.json + 碰撞报告
  python scripts/combo_prompts.py --gen 2 --check-stale   # 与 catalog 比对缺漏（只读）
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "assets" / "director-catalog.js"
OUT = ROOT / "scripts" / "combo-prompts.json"
TEMPLATE_VERSION = 1

# ---- 复用 build_combo_gallery 的解析（importlib，同 regen 脚本方式） ----
_spec = importlib.util.spec_from_file_location("bcg", ROOT / "scripts" / "build_combo_gallery.py")
bcg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bcg)

CJK = re.compile(r"[一-鿿]")
ASCII_KW = re.compile(r"^[a-z]+$")


def kw_match(kw: str, blob: str) -> bool:
    """关键词命中：英文词用词边界（防 ski⊂skin / run⊂runes 子串误命中；数字粘连 id 如 hotel5 仍可命中）；中文保持子串。"""
    if ASCII_KW.match(kw):
        return re.search(rf"\b{re.escape(kw)}(?![a-z])", blob) is not None
    return kw in blob


def h(skill: str, cid: str, dim: str, gen: int) -> int:
    return int(hashlib.md5(f"{skill}:{cid}:{dim}:gen{gen}".encode("utf-8")).hexdigest()[:12], 16)


def pick(skill: str, cid: str, dim: str, gen: int, pool: list) -> str:
    return pool[h(skill, cid, dim, gen) % len(pool)]


# ---------------------------------------------------------------- 角色锁（纯文字）
LOCK = {
    "figure": (
        "An adult East Asian woman of twenty-two, one hundred fifty-eight centimeters, "
        "petite adult frame, slim waist, dancer hips under clothing, warm-neutral East Asian undertone, "
        "no glasses. Dark brown center-part hair. Soft natural lip. Adult face fully readable. "
        "Same heroine identity. She is fully dressed."
    ),
    "youth": (
        "An adult East Asian woman of twenty-two, petite adult frame, warm-neutral East Asian undertone, "
        "no glasses. Dark brown center-part hair. Soft lip. Adult face fully readable. "
        "Implied sensual only; body covered; no nudity; no sex."
    ),
    "erotic": (
        "An adult East Asian woman of twenty-two, petite adult frame with B-cup breasts, slim waist, "
        "dancer hips, warm-neutral East Asian undertone, no glasses. Dark brown center-part hair. "
        "True crimson lipstick. Adult face fully readable. One heroine only."
    ),
}

BAN = {
    "figure": "SFW, fully non-explicit.",
    "youth": "Soft-sensual implied only; no genitals, no penetration, no explicit sex; adult 18+ solo.",
    "erotic": "Adult 18+ only.",
}

# ---------------------------------------------------------------- 主体覆盖
# 默认 LOCK 是 solo 东亚女；男像/双人条目必须替换主体（否则男像生成女性、双人缺伴侣）。
# 字段：lock=Main 段主体句；subj=p1 段主语短语；pn=pose 段代词；fill=构图段填充主语。
_LOCK_MAN = (
    "An adult East Asian man of twenty-five, one hundred seventy-eight centimeters, slim athletic adult frame, "
    "warm-neutral East Asian undertone, no glasses. Short dark neat hair, clean skin, adult face fully readable. "
    "He is fully dressed."
)
_LOCK_COUPLE = (
    "An adult East Asian woman of twenty-two, one hundred fifty-eight centimeters, petite adult frame, "
    "warm-neutral East Asian undertone, no glasses. Dark brown center-part hair. Adult face fully readable. "
    "She is fully dressed. Beside her an adult East Asian man of twenty-five, clearly adult facial structure, "
    "casual layered clothing; one soft point of contact between them, SFW tender."
)
_LOCK_FRIENDS = (
    "Two adult East Asian women of twenty-two, similar height, warm-neutral East Asian undertone, no glasses. "
    "Dark brown hair, both adult faces fully readable. Both fully dressed, non-sexual friendship energy."
)
_CAST_MAN = {"lock": _LOCK_MAN, "subj": "a photoreal adult East Asian man", "pn": "He", "obj": "him", "wear": "He", "fill": "He fills most"}
_CAST_COUPLE = {"lock": _LOCK_COUPLE, "subj": "a photoreal adult East Asian couple", "pn": "She", "obj": "her", "wear": "She", "fill": "The couple fills most"}
_CAST_FRIENDS = {"lock": _LOCK_FRIENDS, "subj": "two photoreal adult East Asian women", "pn": "They", "obj": "them", "wear": "They", "fill": "They fill most"}
CAST_FIX = {
    "figure:combo-male-suit": _CAST_MAN,
    "figure:combo-male-trench": _CAST_MAN,
    "figure:combo-male-oversized": _CAST_MAN,
    "figure:combo-male-workwear": _CAST_MAN,
    "figure:combo-male-techwear": _CAST_MAN,
    "figure:combo-male-street-asian": _CAST_MAN,
    "figure:combo-male-headshot-asian": _CAST_MAN,
    "figure:combo-male-old-money": _CAST_MAN,
    "figure:combo-male-athletic": _CAST_MAN,
    "figure:combo-couple-walk": _CAST_COUPLE,
    "figure:combo-couple-forehead": _CAST_COUPLE,
    "figure:combo-duo-walk-couple": _CAST_COUPLE,
    "figure:combo-cp-walk": _CAST_COUPLE,
    "figure:combo-cp-forehead": _CAST_COUPLE,
    "figure:combo-cp-umbrella": _CAST_COUPLE,
    "figure:combo-cp-airport": _CAST_COUPLE,
    "figure:combo-gm-walk": _CAST_FRIENDS,
    "figure:combo-gm-steps": _CAST_FRIENDS,
    "figure:combo-gm-mirror": _CAST_FRIENDS,
    "figure:combo-lf-friend-walk": _CAST_FRIENDS,
    "figure:combo-hero-pet": {
        "lock": LOCK["figure"] + " Beside her a small dog looking up at her.",
        "subj": "a photoreal adult East Asian woman with her small dog",
        "pn": "She", "fill": "She fills most",
    },
    "figure:combo-hero-hero-male-soft": {
        "lock": LOCK["figure"] + " Behind her a male companion softly out of focus.",
        "subj": "a photoreal adult East Asian woman with a softly blurred male companion",
        "pn": "She", "fill": "She fills most",
    },
    "erotic:combo-hero-noface-him": {
        "lock": LOCK["erotic"] + " A male partner is with her, his face cropped out of frame above the chin.",
        "subj": "a photoreal adult East Asian woman with a male partner whose face is out of frame",
        "pn": "She", "fill": "She fills most",
    },
    # 中老年主体：senior-window（默认 LOCK 是 22 岁，中老年主题需换主体）
    "figure:combo-senior-window": {
        "lock": "An East Asian woman of fifty-eight, warm-neutral East Asian undertone, silver-streaked hair in a low bun, soft smile lines, glasses. Adult face fully readable with lived-in elegance. She is fully dressed.",
        "subj": "a photoreal adult East Asian woman of fifty-eight",
        "pn": "She", "fill": "She fills most",
    },
    # 国标架型：双人舞伴（舞裙+燕尾）
    "figure:combo-ballroom-frame": {
        "lock": (
            "An adult East Asian woman of twenty-two in a flowing ballroom gown, warm-neutral East Asian undertone, "
            "dark hair in an updo, adult face fully readable. Beside her an adult East Asian man of twenty-five "
            "in a black tailcoat and white shirt, in a formal dance hold."
        ),
        "subj": "a photoreal adult East Asian ballroom couple in dance hold",
        "pn": "She", "fill": "The couple fills most",
    },
    # erotic 多人/双人主体：LOCK「One heroine only」与 3P/轮/情侣/共感矛盾，需加伴侣
    "erotic:combo-threesome-mmf": {
        "lock": LOCK["erotic"].replace("One heroine only.", "Two male partners share her, one before and one behind."),
        "subj": "a photoreal adult East Asian woman between two male partners",
        "pn": "She", "fill": "She fills most",
    },
    "erotic:combo-threesome-ffm": {
        "lock": LOCK["erotic"].replace("One heroine only.", "A second adult woman joins her, both sharing one male partner."),
        "subj": "two photoreal adult East Asian women with one male partner",
        "pn": "They", "obj": "them", "wear": "They", "fill": "They fill most",
    },
    "erotic:combo-gangbang-focus": {
        "lock": LOCK["erotic"].replace("One heroine only.", "Surrounded by three male partners, one at each side."),
        "subj": "a photoreal adult East Asian woman surrounded by three male partners",
        "pn": "She", "fill": "She fills most",
    },
    "erotic:combo-amateur-couple": {
        "lock": LOCK["erotic"].replace("One heroine only.", "With her a male partner of similar age, casual and close."),
        "subj": "a photoreal adult East Asian couple",
        "pn": "She", "fill": "The couple fills most",
    },
    "erotic:combo-shared-orgasm": {
        "lock": LOCK["erotic"].replace("One heroine only.", "With her a male partner, both mid-ecstasy in sync."),
        "subj": "a photoreal adult East Asian woman with a male partner",
        "pn": "She", "fill": "She fills most",
    },
    "erotic:combo-hero-drained": {
        "lock": LOCK["erotic"].replace("One heroine only.", "Beneath her a drained male hero, his face readable."),
        "subj": "a photoreal adult East Asian woman astride a male partner",
        "pn": "She", "fill": "She fills most",
    },
    # 男娘主体：femboy-solo（LOCK 是女性，男娘需男身女装主体）
    "erotic:combo-femboy-solo": {
        "lock": "An adult East Asian femboy of twenty-two, slender androgynous adult frame, soft makeup, lingerie, long lashes, adult face fully readable.",
        "subj": "a photoreal adult East Asian femboy in lingerie",
        "pn": "He", "obj": "him", "wear": "He", "fill": "He fills most",
    },
}

# ---------------------------------------------------------------- 差异化维度表
# 每 skill：关键词有序表 → (类名, 变体池)。命中 = label+look+group+en 小写串首个关键词命中。

SCENE = {
    "figure": [
        (("棚", "studio", "lookbook", "editorial", "商业", "headshot", "头像", "证件", "假窗", "蚌式", "色片", "交叉光"), "studio-paper", [
            "a pale seamless paper studio with a faint floor seam, one softbox stand off-frame",
            "a white cyclorama with a single gray v-flat leaning against the wall",
            "an empty studio with a paper sweep, one apple box and a boom arm shadow",
        ]),
        (("pavilion", "亭台", "国风", "古风", "suzhou", "园林", "garden"), "pavilion", [
            "a classic Chinese pavilion with upturned eaves, one stone lantern and a pond",
            "an ancient corridor with red pillars, carved lattices and a garden beyond",
            "a hilltop pavilion with a railing, distant pagodas and morning mist",
        ]),
        (("flower", "花海", "花田", "花园", "garden", "樱花", "sakura", "银杏", "ginkgo"), "flower-field", [
            "a rolling flower field with pastel blooms, one narrow path and soft sky",
            "a garden border with roses, a wooden bench and drifting petals",
            "a meadow of wildflowers with a low fence and one distant tree",
            "a park path under full-bloom cherry trees, petals drifting in the air, one bench",
            "a ginkgo avenue with golden leaves carpeting the ground, one lamppost",
        ]),
        (("大头贴", "拍贴", "四宫格", "purikura", "photobooth"), "photo-booth", [
            "a purikura photo booth interior with bright white panels, one curtain and a sticker machine screen glow",
            "inside a purikura photo booth, flat white beauty flash, one stool and a pastel backdrop",
            "a purikura booth corner with a soft pastel wall, one ring flash and a curtain edge",
        ]),
        (("机场", "airport"), "airport", [
            "a bright airport terminal with departure boards, one luggage cart and big windows",
            "an airport lounge with rows of seats, a big window showing a plane on the tarmac",
            "a departure gate with glass walls, one travel trolley and soft daylight",
        ]),
        (("美术馆", "画廊", "gallery", "看展"), "gallery", [
            "a white-wall art gallery with large framed paintings, one bench and a skylight",
            "a contemporary gallery hall with spot-lit canvases and polished concrete floor",
            "an art museum corridor with tall ceilings, one sculpture plinth and soft gallery light",
        ]),
        (("钢琴", "piano"), "piano-room", [
            "a bright piano room with a grand piano, one music stand and tall windows",
            "a rehearsal room with an upright piano, one stool and warm wall light",
            "a conservatory corner with a black grand piano, one bench and soft daylight",
        ]),
        (("电竞", "gaming", "rgb"), "gaming-room", [
            "a gaming room with a multi-monitor setup, one chair and RGB strip lighting",
            "a streamer room with neon RGB strips, one desk and a shelf of figures",
            "a gaming corner with a mechanical keyboard glow, one headset and LED panels",
        ]),
        (("公园", "park", "picnic", "野餐"), "park", [
            "a city park with green lawns, one bench and a winding path",
            "a park pathway with plane trees, one lamppost and soft grass",
            "a lakeside park with a railing, one distant pavilion and morning light",
            "a picnic blanket on the grass with a basket, one tree overhead",
        ]),
        (("影院", "cinema"), "cinema-lobby", [
            "a cinema lobby with glowing poster walls, one ticket counter and a popcorn stand",
            "a movie theatre hallway with red carpet, one poster lightbox and warm bulbs",
            "a cinema entrance with a marquee, one concessions corner and soft lobby light",
        ]),
        (("洗衣", "laundromat"), "laundromat", [
            "a laundromat with rows of washing machines, one bench and a vending machine",
            "a coin laundry with warm fluorescent light, one basket and folded shelves",
            "a laundromat corner with a spinning dryer, one window and soft evening light",
        ]),
        (("夜市", "nightmarket"), "night-market", [
            "a night market street with glowing food stalls, one canopy and hanging bulbs",
            "a busy night market with string lights, one cart and steam rising",
            "a night market lane with neon signs, one stall counter and warm glow",
        ]),
        (("街", "street", "ootd", "denim", "通勤", "纪实", "neon", "cafe", "咖啡", "city", "夜景", "外滩", "洪崖洞", "胡同", "宽窄巷", "parking", "停车场", "地铁", "subway", "马路", "街拍", "alley", "巷弄", "步行", "并肩", "雨", "台阶", "伞"), "street", [
            "a crosswalk corner with storefront glass, a streetlamp and one parked bicycle",
            "a quiet sidewalk lined with plane trees, a low railing and window reflections",
            "a pedestrian overpass with railings, city skyline behind, two bollards",
            "a rain-washed street corner with wet pavement reflections, one umbrella stand",
            "outdoor stone steps with a low railing, city trees behind, soft daylight",
        ]),
        (("酒店", "hotel", "宾馆", "客房", "旅馆", "民宿"), "hotel", [
            "a bright hotel room with a king bed, sheer curtains and one luggage bench",
            "a boutique hotel lounge with a velvet sofa, brass lamps and marble floor",
            "a hotel suite window seat with a city view and a robe on the chair",
        ]),
        (("咖啡", "cafe", "咖啡馆", "咖啡店"), "cafe", [
            "a sunlit cafe interior with a marble table, one pendant light and a window seat",
            "a cozy cafe corner with a leather booth, a warm lamp and wall shelves",
            "a cafe counter with a barista machine, stools and soft daylight",
        ]),
        (("书店", "bookstore", "书咖", "书房", "图书馆", "library"), "library", [
            "a quiet bookstore with tall shelves, one reading lamp and a wooden ladder",
            "a library reading room with long tables, warm lamps and book-lined walls",
            "a book nook with a window seat, stacked volumes and soft daylight",
        ]),
        (("yoga", "瑜伽", "sport", "健身", "gym", "run", "athletic", "athlete", "martial", "climb", "cycle", "bodybuilding", "健美", "boxing", "拳", "tennis", "网球", "球"), "gym", [
            "a gym floor with wall mirrors, one barbell rack and a hanging rope",
            "an indoor track lane with painted lines and a foam roller at the edge",
            "a climbing wall with colored holds and one crash pad",
            "a boxing ring under a single overhead light, ropes and a corner stool",
        ]),
        (("山地车", "mtb", "山地", "bike", "自行车", "骑行"), "trail", [
            "a mountain bike trail with a dirt jump ramp, one pine line and open sky",
            "a forest singletrack with roots and stones, one wooden bridge",
            "a hillside gravel path with a berm curve and low bushes",
        ]),
        (("校园", "campus", "教室外", "教学楼", "graduate", "毕业"), "campus", [
            "a university campus lawn with a clock tower, one bicycle stand and a path",
            "a campus walkway with plane trees, one bicycle and a bench",
            "a school courtyard with a teaching building, one bike rack and soft daylight",
        ]),
        (("ski", "snow", "雪场"), "snow", [
            "a ski slope with groomed tracks, one boundary rope and distant peaks",
            "a snowfield at noon with bright white glare and one chairlift tower",
            "a mountain pass with fresh powder and a line of pine trees",
        ]),
        (("舞蹈", "舞者", "街舞", "现代舞", "dance", "rehearsal", "ballet", "ballroom", "balletcore"), "dance-studio", [
            "a rehearsal studio with a wall of mirrors, a barre and one folding chair",
            "a dance studio corner with wood floor, an upright piano and drawn curtains",
            "a practice room with a mirrored wall, a barre and soft morning light",
        ]),
        (("stage", "表演", "theatre", "话剧", "剧场", "gala", "红毯", "颁奖", "band", "concert", "演唱会", "runway", "catwalk", "走秀", "秀场", "后台", "backstage"), "theatre", [
            "a black-box stage with a single follow spot and stage tape marks",
            "a theatre stage with red curtains, one follow spot and a bare set",
            "a backstage wing with a rope line, one standing lamp and dark air",
        ]),
        (("office", "ol", "通勤", "职场", "exec", "西装", "tailor", "medical", "lab", "chef", "工地", "匠", "hangar", "机库", "keynote", "演讲"), "work", [
            "a modern office with glass partitions, one desk lamp and a whiteboard",
            "a conference room with a long table, chairs and a window blind",
            "a coworking corner with a bookshelf, one monitor and a potted plant",
        ]),
        (("黑白", "bw", "conceptual", "艺术", "concrete", "水泥"), "bw-studio", [
            "a dark studio with a single hard spotlight and a black backdrop",
            "a gray wall with one high window and a metal stool",
            "an empty concrete room with a light shaft and floor grid lines",
        ]),
        (("beach", "海边", "海岛", "seaside", "coast", "island", "surf", "冲浪"), "beach", [
            "a white sand beach with a soft surf line, one beach umbrella and driftwood",
            "a rocky coast path with sea pines and a low stone wall",
            "a seaside boardwalk with a railing, one bench and distant sailboats",
        ]),
        (("旅", "campus", "大学", "lawn", "forest", "森", "乡村", "田野", "田间", "麦田", "稻", "大景", "desert"), "travel", [
            "a lakeside promenade with a railing, one bench and distant mountains",
            "a mountain road pull-off with a guardrail and a lone sign",
            "an old town alley with stone walls, one doorway and hanging plants",
        ]),
        (("露营", "camp", "帐篷", "营地"), "camp", [
            "a campsite clearing with a pitched tent, one camp chair and string lights",
            "a forest camp at dusk with a low fire, folding stools and soft smoke",
            "a lakeside camp with a tent, a lantern on a stump and morning mist",
        ]),
        (("水下", "underwater", "潜水", "漂浮"), "underwater", [
            "a clear pool underwater with shafts of light from the surface, one tiled wall",
            "deep blue water with sun rays cutting through, soft bubbles drifting",
            "an underwater scene with rippling surface light and one submerged ladder",
        ]),
        (("屋顶", "rooftop", "天台"), "rooftop", [
            "a rooftop edge with a safety railing, one antenna and city haze",
            "a rooftop terrace with string lights, one lounge chair and skyline",
            "a concrete rooftop with an HVAC unit, one edge railing and dusk sky",
        ]),
        (("特殊"), "special", [
            "a rooftop edge with a safety railing, one antenna and city haze",
            "an aquarium tunnel with blue light and one viewing bench",
        ]),
        (("skate", "冰旋", "花滑", "冰场"), "ice-rink", [
            "an ice rink with cool white light, one open gate and glossy ice reflections",
            "a training rink with bleachers, cold haze and one spotlight",
            "a rink-side boards with a bench, ice shavings and cold ambient glow",
        ]),
        (("wedding", "婚礼", "aisle", "教堂", "bride", "婚纱"), "wedding", [
            "a wedding aisle with flower arrangements, white drapery and wooden pews",
            "an outdoor ceremony lawn with an arch of white roses and ribboned chairs",
            "a church doorway with stone steps, one floral urn and soft daylight",
        ]),
        (("bath", "浴", "robe", "浴缸", "bathtub"), "bath", [
            "a warm bathroom with a wide mirror, one hanging robe and a bathmat",
            "a bathtub edge with a folded towel, candle light and soft steam",
            "a tiled bath nook with a shower curtain and frosted window light",
        ]),
        (("home", "boudoir", "居家", "私房", "窗"), "home", [
            "a bright apartment living room with a linen sofa, one floor lamp and a rug",
            "a minimal bedroom with sheer curtains, one bedside table and a throw blanket",
            "a kitchen bar with stools, one pendant light and a fruit bowl",
            "a window-side nook with sheer curtains, one sill plant and soft daylight",
        ]),
        (("厨房", "kitchen", "台沿", "料理"), "kitchen", [
            "a bright kitchen with a marble counter, one pendant light and a fruit bowl",
            "a small kitchen nook with open shelves, a kettle and morning light",
            "a kitchen island with two stools, a cutting board and soft daylight",
        ]),
    ],
    "youth": [
        (("window", "窗", "sill", "ledge", "risk", "blind", "百叶"), "window", [
            "a bedroom window seat with sheer curtains, one plant and city lights beyond",
            "a wide apartment window at dusk, a low sill with a folded knit",
            "a half-open balcony door with a sheer curtain drifting, evening air",
        ]),
        (("sofa", "沙发", "couch", "scroll", "lazy"), "sofa", [
            "a soft linen sofa with two pillows, a knitted throw and one side lamp",
            "a low couch facing a warm floor lamp, a phone on the cushion",
            "a window-side sofa with a mug on the armrest and evening glow",
        ]),
        (("咖啡", "cafe", "奶茶", "coffee", "milk-tea", "boba"), "cafe", [
            "a cozy cafe corner with a latte on the table, one warm lamp and soft light",
            "a milk-tea shop interior with a straw cup, one window seat and pastel tones",
            "a quiet coffee shop with a sofa nook, one pendant light and daylight",
        ]),
        (("hotel", "酒店", "robe", "arrival"), "hotel", [
            "a hotel room with a luggage bench, one floor lamp and drawn sheers",
            "a hotel suite window with a city view and a robe on the chair",
            "a quiet hotel corridor nook with a luggage cart and soft downlight",
        ]),
        (("厨房", "kitchen", "台沿", "料理"), "kitchen", [
            "a bright kitchen with a marble counter, one pendant light and a fruit bowl",
            "a small kitchen nook with open shelves, a kettle and morning light",
            "a kitchen island with two stools, a cutting board and soft daylight",
        ]),
        (("mirror", "镜", "self-gaze", "vanity", "自拍"), "mirror", [
            "a full-length mirror against a bedroom wall, one jewelry tray below",
            "a vanity table with a round mirror, warm bulbs and a stool",
            "a hallway mirror beside a coat rack and a soft rug",
        ]),
        (("bed", "床", "sheet", "morning", "lie", "shirt", "衬衫"), "bed", [
            "a low bed with white sheets, a crumpled duvet and one bedside lamp",
            "a bedroom bed with linen bedding, curtains half drawn, morning light",
            "a hotel bed with crisp sheets, one reading light and a window",
        ]),
        (("bath", "浴", "steam", "shower", "towel"), "bath", [
            "a bathroom with fogged mirror, one folded towel and steam light",
            "a tiled bath corner with a shower curtain and warm backlight",
            "a bathroom shelf with a plant, soft steam and one hanging robe",
        ]),
        (("balcony", "阳台", "dusk", "city"), "balcony", [
            "a small balcony with a railing, one chair and dusk skyline",
            "a balcony at blue hour with string lights and a city breeze",
            "a narrow balcony with potted greens and distant traffic glow",
        ]),
        (("neon", "霓虹"), "neon", [
            "a rainy street with neon signage, one awning and wet reflections",
            "an underground garage with cool tube lights and one pillar",
        ]),
        (("car", "车内", "夜车"), "car", [
            "a parked car interior at night with dashboard glow and window drops",
            "the back seat of a night taxi, street lights passing outside the glass",
            "a car interior with a phone glow, one cup holder and soft evening light",
        ]),
        (("ballet", "芭蕾", "barre"), "ballet", [
            "a ballet studio with a barre, wall mirror and soft morning light",
            "a white-walled dance classroom with a freestanding barre and wood floor",
            "a rehearsal room corner with a piano bench, tulle skirt on the barre",
        ]),
        (("entryway", "玄关", "one-mile"), "entryway", [
            "a small apartment entryway with a shoe rack, one mirror and a soft mat",
            "a genkan with a wooden step, one slipper pair and warm indoor light",
            "a hallway nook with a coat hook, a potted plant and door glass light",
        ]),
        (("dance", "舞池", "dance-floor", "排练"), "dance-studio", [
            "a rehearsal studio with a wall of mirrors, a barre and one folding chair",
            "a dance practice room with wood floor, an upright piano and drawn curtains",
            "a mirrored practice room with a barre and soft morning light",
        ]),
    ],
    "erotic": [
        (("led", "霓虹", "love-hotel", "圆床", "情趣"), "love-hotel", [
            "a love hotel room with a round bed, magenta LED strips along the headboard and a wall mirror",
            "a neon-lit suite with purple and amber light bands, a rotating bed and mirrored ceiling",
            "a moody hotel nook with a magenta glow, one amber window sliver and a vanity mirror",
        ]),
        (("hotel", "酒店", "tungsten", "钨丝"), "hotel", [
            "a dim luxury hotel room with a king bed, one tungsten bedside lamp and drawn sheers",
            "a hotel suite with a leather bench, a floor lamp and window city glow",
            "a hotel bathroom with a wide mirror, a towel rack and warm downlight",
        ]),
        (("bed", "床", "sheet", "bedroom"), "bedroom", [
            "a bedroom with rumpled sheets, one warm lamp and soft shadows",
            "a low bed against a headboard, curtains closed, amber light",
            "a bedroom with a vanity glow, silk bedding and a floor mirror",
        ]),
        (("bath", "浴", "shower"), "bath", [
            "a steamy bathroom with a fogged mirror and a rain shower head",
            "a tiled shower with glass doors and one warm wall lamp",
            "a bathtub edge with a towel, candle light and soft steam",
        ]),
        (("office", "职场"), "office", [
            "an after-hours office with a desk lamp, glass walls and one chair",
            "an executive office with a leather chair and city night windows",
            "a meeting room with a long table and a single warm light",
        ]),
        (("kitchen", "厨房", "counter", "柜台"), "kitchen", [
            "a home kitchen with a counter island, one pendant light and stools",
            "a kitchen counter with a sink, one window and warm evening light",
        ]),
        (("classroom", "教室", "school"), "classroom", [
            "an empty classroom with desk rows, a chalkboard and one window",
            "a lecture hall corner with a desk and a projector glow",
        ]),
        (("outdoor", "野", "户外", "exhibition", "greenhouse", "温室"), "outdoor", [
            "a rooftop at night with a low wall, one light and city haze",
            "a forest edge with a fallen log and dappled moonlight",
            "a glass greenhouse at night with misted panes and hanging vines",
        ]),
        (("car", "车震", "蒸窗", "车窗"), "car", [
            "a parked car interior at night with streetlamp glow through the glass",
            "a car back seat in a quiet lot, window condensation and one distant light",
            "a car cabin with dashboard glow, steamed windows and soft shadows",
        ]),
        (("onsen", "温泉", "steam"), "onsen", [
            "a wooden onsen bath with steam, one stone lantern and warm lantern glow",
            "a rotenburo outdoor bath with snow-edged rocks and rising steam",
            "an indoor onsen with wood slats, a towel shelf and soft steam light",
        ]),
        (("library", "图书", "禁书", "书库"), "library", [
            "a dark library with tall shelves, one warm desk lamp and leather-bound rows",
            "a hidden archive room with a reading table, candles and dust motes",
            "an old reading hall with a ladder, stained glass and low warm light",
        ]),
        (("dungeon", "地牢", "bdsm", "束缚", "power", "pegging", "项圈", "牵绳"), "dungeon", [
            "a dark concrete room with a steel frame, one red lamp and leather textures",
            "a candle-lit chamber with a wooden bench and draped fabric",
        ]),
        (("lab", "实验", "fantasy", "幻想", "tentacle", "succubus", "rune", "runes", "slime", "magic", "alien", "异星", "train", "列车", "异界"), "fantasy-void", [
            "a dreamlike void with floating runes, soft purple fog and one stone platform",
            "a glowing cavern with bioluminescent vines and mist",
            "a surreal room with floating candles and warped perspective",
            "a sci-fi laboratory with glowing screens and one glass pod",
        ]),
    ],
}

# 无锚场景 fallback 池：伪随机取模（铁律：禁恒取默认行 bedroom/hotel 等）
SCENE_FALLBACK = {
    "figure": ["street", "studio-paper", "travel", "work", "home"],
    "youth": ["bed", "sofa", "window", "mirror", "bath", "balcony"],
    "erotic": ["hotel", "bedroom", "bath", "office", "love-hotel"],
}

WARDROBE = {
    "figure": [
        (("street", "街", "ootd", "denim", "rain", "crosswalk", "neon", "night", "urban"), "street", [
            "a leather jacket over a black turtleneck, straight trousers and chunky loafers",
            "an oversized hoodie with a pleated midi skirt and white sneakers",
            "a cropped knit with high-waist wide jeans and low-top canvas shoes",
            "a denim jacket over a striped tee, cargo pants and clean trainers",
        ]),
        (("office", "ol", "职场", "exec", "西装", "tailor"), "office", [
            "a tailored blazer with cigarette trousers and pointed flats",
            "a white shirt tucked into a pencil skirt with a thin belt and pumps",
            "a knit vest over a collared shirt, pleated trousers and loafers",
        ]),
        (("yoga", "瑜伽", "sport", "健身", "gym", "run", "athletic", "martial", "climb", "cycle", "surf", "冲浪", "游泳", "泳"), "sport", [
            "a zip-up track jacket with matching tapered joggers and running shoes",
            "a sports bra layered under a loose tank, leggings and training sneakers",
            "a tennis dress with a visor and court shoes",
        ]),
        (("skate", "冰旋", "花滑", "冰场"), "skate-dress", [
            "a figure-skating dress with a flared skirt, opaque tights and skate boots",
            "a sleeveless skate dress with crystal trim and sheer-sleeve gloves",
            "a practice skating dress with a wrap top, tights and blade guards off",
        ]),
        (("ballet", "芭蕾", "dance", "舞"), "dance", [
            "a ballet leotard with footless tights and ballet flats",
            "a wrap cardigan over a leotard and a rehearsal skirt",
            "a practice tutu with leg warmers and soft ballet slippers",
        ]),
        (("robe", "浴袍", "睡袍"), "bath-robe", [
            "a soft terry bathrobe loosely belted, hem at knee",
            "a white waffle robe with a draped collar",
            "a spa robe with a folded lapel, ankles bare",
        ]),
        (("国风", "新中式", "guofeng", "hanfu", "汉服"), "guofeng", [
            "a modern qipao-style dress with a mandarin collar and side slits",
            "a new-chinese set with a wrap top and a long flowing skirt",
            "a hanfu-inspired ensemble with a draped sash and flowing sleeves",
        ]),
        (("editorial", "lookbook", "商业", "scurve", "campaign", "runway"), "editorial", [
            "an oversized blazer dress with sheer tights and square-toe boots",
            "a structured corset top with wide-leg trousers and stiletto heels",
            "a long wool coat over a silk slip dress and ankle boots",
        ]),
        (("wedding walk", "婚礼通道", "bride", "婚纱", "bridal"), "bridal", [
            "a clean wedding gown with a soft train, veil pinned back",
            "an a-line wedding dress with lace sleeves and a fingertip veil",
            "a satin bridal gown with a structured bodice, train swept aside",
        ]),
        (("guest", "宾客", "观礼"), "cocktail", [
            "a pastel cocktail dress with a small clutch and low heels",
            "a floral midi guest dress with a tailored jacket over the arm",
            "a satin slip guest dress with a cardigan and minimal jewelry",
        ]),
        (("dress", "连衣裙", "slip", "柱裙"), "dress", [
            "a slip dress layered under an oversized blazer, white sneakers, hem at calf",
            "a ribbed column knit dress with vintage runners and a small shoulder bag",
            "a floral slip dress with ballet flats and a thin cardigan draped over shoulders",
        ]),
        (("skirt", "裙", "midi", "百褶", "缎面"), "skirt", [
            "a knife-pleat midi skirt with a fitted knit tucked in and pointed ballet flats",
            "a satin bias-cut midi skirt with a white shirt tucked and slim loafers",
            "a pleated midi skirt with a polo tucked in and mary-jane flats",
        ]),
        (("travel", "旅", "campus", "大学", "lawn", "library"), "campus", [
            "a knit sweater with a midi skirt and canvas sneakers",
            "a quilted jacket with a plaid scarf, jeans and hiking boots",
            "a collar shirt under a varsity jacket with chinos and loafers",
        ]),
        (("home", "boudoir", "居家", "私房"), "home", [
            "a relaxed cardigan over a tank top and soft lounge trousers",
            "an oversized shirt with leggings and crew socks",
        ]),
        (("chef", "lab", "medical", "工地", "匠", "work"), "uniform", [
            "a clean white chef coat with an apron and clogs",
            "a lab coat over a collared shirt with an ID lanyard and flat shoes",
        ]),
    ],
    "youth": [
        (("shirt", "衬衫", "boyfriend", "oversized"), "shirt", [
            "an oversized white boyfriend shirt with the top two buttons open",
            "an oversized light-blue shirt slipping off one shoulder, no bottoms shown",
            "a soft flannel shirt unbuttoned over a thin camisole",
        ]),
        (("knit", "毛衣", "sweater", "针织"), "knit", [
            "a chunky cream knit with a loose collar and long sleeves",
            "a fitted ribbed knit with a soft neckline",
            "a v-neck cashmere sweater with sleeves pushed to the elbows",
            "a cream knit two-piece with a camisole and an open cardigan, sleeves past the wrist",
        ]),
        (("robe", "浴袍", "睡袍"), "robe", [
            "a soft hotel robe with a loosely tied belt, collarbones visible",
            "a short satin robe with lace trim, knees bare",
        ]),
        (("dress", "裙", "slip", "吊带"), "dress", [
            "a thin slip dress with spaghetti straps, hem at mid-thigh",
            "a soft knit dress with a loose neckline and short sleeves",
        ]),
        (("sport", "瑜伽", "yoga"), "sport", [
            "a crop top with high-waist leggings, fully covered torso",
            "a zip hoodie over a sports bra and shorts",
        ]),
        (("ballet", "芭蕾", "dance", "barre", "护腿"), "ballet", [
            "a ballet leotard with a wrap skirt and knit leg warmers",
            "a soft pink leotard with sheer tights and ballet flats",
            "a practice leotard with a shrug cardigan and footless tights",
        ]),
    ],
    "erotic": [
        (("lingerie", "内衣", "e2", "garter", "stocking", "丝袜"), "lingerie", [
            "a lace bralette set with a garter belt and sheer stockings",
            "a satin slip with lace edges, one strap fallen",
            "a sheer bodysuit with high-cut legs",
            "an embroidered balconette bra set with a garter belt, cup edge pulled down",
            "a sheer mesh bodysuit with strappy back lines and a silver o-ring",
        ]),
        (("robe", "silk", "袍", "浴袍", "kimono"), "silk-robe", [
            "a deep-v silk robe loosely belted, one shoulder slipping bare",
            "a satin robe wrapped open over a lace bra, sash trailing",
            "a velvet robe half-open with a matching slip underneath",
        ]),
        (("undress", "半褪", "e1", "hiked", "knee", "shirt"), "undress", [
            "a button shirt open to the navel, skirt hiked, nothing removed",
            "trousers at the knees, shirt half-open, underwear still on",
            "a dress pulled up to the waist, bra still worn",
        ]),
        (("nude", "e4", "全裸", "naked"), "nude", [
            "fully nude, optional prop only",
        ]),
        (("uniform", "cosplay", "cos", "制服"), "uniform", [
            "a cosplay uniform half-removed, one shoulder bared",
            "an office shirt with the first buttons open and a short skirt",
        ]),
    ],
}

WARDROBE_DEFAULT = {
    "figure": "editorial",
    "youth": "shirt",
    "erotic": "undress",
}

# 光：按 scene 类分表
LIGHT = {
    "studio-paper": ["softbox key from front-left, gentle fill, thin hair rim", "clam-shell beauty light, even fill, soft falloff", "hard book light from the side, crisp shadow line", "top beauty dish with a low fill card"],
    "street": ["overcast soft daylight, even and muted", "low golden sun raking across the sidewalk", "neon rim at dusk with a soft streetlamp key", "soft window light bouncing off a storefront"],
    "gym": ["cool overhead panels with a soft window fill", "high windows with dust-beam light", "track lighting with one warm accent"],
    "dance-studio": ["window practice-room daylight with mirror bounce", "soft morning light across the mirrored wall", "even practice-room light with a warm fill"],
    "theatre": ["a single follow spot against dark air", "warm stage wash with a back rim", "a narrow side light with stage haze"],
    "work": ["daylight through blinds with a desk lamp warm fill", "clean overhead panels with monitor glow", "window key from the side, neutral fill"],
    "bw-studio": ["a single hard spotlight, deep shadows", "high side light carving the figure", "soft top light with a black void background"],
    "travel": ["golden hour side light with long shadows", "open shade with sky bounce", "sunset rim with warm fill"],
    "special": ["aquarium blue with a single warm spot", "rooftop dusk glow with city bokeh"],
    "underwater": ["underwater blue light with god rays", "sun shafts through deep water", "caustic rippling light from above"],
    "rooftop": ["rooftop dusk glow with city bokeh", "blue hour city light from above", "golden hour rooftop wash"],
    "home": ["window key at 45 degrees with soft catchlights", "evening lamp light with a warm wrap", "morning window light with sheer-curtain diffusion", "soft daylight from a patio door"],
    "window": ["window backlight with hair rim, face softly filled", "window key at 45 degrees with soft catchlights", "dusk window glow with a warm practical", "sheer-curtain daylight, soft and even"],
    "sofa": ["one warm floor lamp as key, soft falloff", "window light across the cushions, gentle fill", "screen glow mixed with a side lamp", "evening pendant light with a warm wrap"],
    "mirror": ["vanity bulbs warm and even", "window daylight bounced off the mirror", "soft lamp light with a mirror rim"],
    "bed": ["bedside lamp warm and low", "morning window light through half-drawn curtains", "phone screen glow with a soft lamp fill", "a string of warm fairy lights at the headboard"],
    "bath": ["steam-soft backlight with a warm wall lamp", "frosted window light, soft and even", "candle-warm accent with cool ambient"],
    "balcony": ["blue hour ambient with warm string lights", "dusk sky bounce, soft and even", "city glow from below with a cool rim"],
    "hotel": ["bedside tungsten warm and low", "sheer window light with a floor lamp fill", "bathroom downlight with mirror bounce", "warm cove lighting along the headboard"],
    "love-hotel": ["magenta LED strips with one amber window sliver", "purple neon wash with a warm practical", "magenta and amber dual-tone glow"],
    "neon": ["neon signage glow with a cool ambient base", "streetlamp key through window rain", "garage tube lights with a neon reflection rim"],
    "bedroom": ["one warm lamp as key, amber shadows", "closed-curtain darkness with a single slit of light", "vanity glow mixed with cool moonlight", "candle cluster with soft amber falloff"],
    "office": ["a single desk lamp in a dark glass room", "monitor glow with city night windows", "overhead panel with a warm desk accent"],
    "classroom": ["one window light across the desk rows", "chalkboard shadow with a warm overhead"],
    "outdoor": ["moonlight with a cool rim", "campfire-warm accent in a dark forest"],
    "dungeon": ["one red lamp, deep shadows", "candlelight flicker with hard shadow edges"],
    "fantasy-void": ["floating rune glow with a soft purple fog", "bioluminescent blue-green ambient", "candle cluster with a dreamy haze"],
    "beach": ["golden seaside sun with soft haze", "open sky light with gentle sea bounce", "sunset glow with long shadows on sand"],
    "ice-rink": ["cool white rink light with ice reflections", "a single cold spotlight with haze", "overhead arena light with a cool rim"],
    "wedding": ["soft window light through white drapery", "open-air daylight with a gentle fill", "warm aisle light with candle glow"],
    "ballet": ["soft morning window light across the barre", "even practice-room light with a mirror bounce", "warm side light with a gentle fill"],
    "snow": ["cold alpine daylight with bright snow bounce", "soft winter overcast with clean whites", "low winter sun raking across the slope"],
    "flower-field": ["open daylight with soft sky bounce", "golden hour glow through the blooms", "overcast pastel light, even and soft"],
    "pavilion": ["daylight through the pavilion eaves", "late sun raking across the railing", "morning mist light with soft fill"],
    "entryway": ["soft daylight from the door glass", "warm indoor light with a cool window edge", "evening bulb light with a gentle fill"],
    "car": ["streetlamp glow through the window", "dashboard glow mixed with outside light", "a single distant light with deep shadows"],
    "onsen": ["steam-soft warm lantern glow", "warm backlight through rising steam", "soft window light with warm wood bounce"],
    "library": ["one warm desk lamp in dark shelves", "candlelight with tall shadow lines", "a reading lamp with dust-mote light"],
    "cafe": ["window daylight with a warm pendant fill", "soft daylight across the table, gentle fill", "evening cafe glow with warm wall lamps"],
    "camp": ["campfire-warm flicker with a cool dusk base", "string-light glow with a soft fire fill", "morning mist light with a warm lantern"],
    "kitchen": ["morning window light over the counter", "warm pendant light with a cool window fill", "soft daylight with a warm under-cabinet glow"],
    "photo-booth": ["bright on-camera beauty flash, flat even light", "ring flash straight on, even skin glow", "flat white booth light with a soft frontal fill"],
    "airport": ["bright terminal daylight with glass reflections", "soft window light with a cool fill", "evening terminal glow with warm accents"],
    "gallery": ["soft skylight with clean white walls", "spot-lit wall wash with gentle fill", "even gallery light with soft falloff"],
    "piano-room": ["soft window light across the keys", "warm wall light with a gentle fill", "afternoon light through tall windows"],
    "gaming-room": ["RGB strip glow with monitor light", "cool LED ambient with a warm desk lamp", "neon accent light with soft room fill"],
    "park": ["open daylight with soft sky bounce", "golden hour through the trees", "overcast pastel light, even and soft"],
    "cinema-lobby": ["warm lobby bulbs with poster glow", "soft ambient light with a marquee glow", "dim theatre light with warm accents"],
    "laundromat": ["warm fluorescent light, even and clean", "soft evening window light with machine glow", "bright practical light with clean whites"],
    "night-market": ["string-light glow with steam haze", "warm stall light with neon accents", "hanging bulb glow with a soft ambient"],
    "trail": ["dappled forest light through the trees", "open sky daylight on the ridgeline", "morning mist light over the path"],
    "campus": ["soft campus daylight with tree shade", "warm afternoon light across the lawn", "clean morning light with long shadows"],
}
LIGHT_DEFAULT = ["soft key with gentle fill, thin hair rim"]

# 调色：按 scene 类
GRADE = {
    "studio-paper": ["natural true-color restrained", "polished catalog neutral", "clean bright editorial"],
    "street": ["natural true-color restrained", "jp cream low-saturation airy", "cinematic soft with subtle teal shadows", "muted low-saturation dan-ren palette"],
    "gym": ["clean bright midtones fresh skin", "natural true-color restrained", "cool athletic tone with clean whites"],
    "dance-studio": ["natural true-color restrained", "soft daylight cream", "clean bright practice-room tone"],
    "theatre": ["cinematic soft with subtle teal shadows", "rich midtones deep blacks", "warm stage amber"],
    "work": ["natural true-color restrained", "clean neutral corporate bright", "soft cinematic with warm skin"],
    "bw-studio": ["rich midtones deep blacks", "high-contrast black and white", "silver gray fine-art monochrome"],
    "travel": ["Portra-like warm skin soft grain", "golden natural with lifted shadows", "clean bright travel tone"],
    "special": ["deep blue aquatic grade", "cool ambient with a single warm accent"],
    "underwater": ["deep blue aquatic grade", "cool teal with light rays", "deep indigo with bright shafts"],
    "rooftop": ["dusk blue with warm city lights", "city-night cool with warm skin", "golden dusk with warm highlights"],
    "home": ["warm neutral home tone", "soft cream natural light", "cozy warm with gentle contrast"],
    "window": ["soft cream-green airy highlights", "warm neutral dusk tone", "clean bright morning light", "cool white low-chroma restrained"],
    "sofa": ["warm neutral with soft shadows", "cozy amber evening tone", "soft daylight cream"],
    "mirror": ["clean bright with soft skin", "warm vanity tone", "neutral with a soft glow"],
    "bed": ["warm amber bedside tone", "soft morning cream", "low-key warm with deep shadows", "cream-white with soft-pink blush, warm tungsten"],
    "bath": ["steamy soft with lifted whites", "cool tiles with warm skin", "soft high-key clean"],
    "balcony": ["blue-hour cool with warm highlights", "dusk magenta-blue blend", "city-night cool with warm skin"],
    "hotel": ["warm tungsten amber", "cinematic soft with teal shadows", "low-key moody warm", "warm tungsten amber with burgundy accent notes"],
    "love-hotel": ["neon magenta-amber contrast with skin glow", "purple-pink neon with deep blacks", "magenta haze with warm highlights"],
    "neon": ["neon contrast with deep blacks", "rain-street cinematic teal-magenta", "cool night with vivid accents"],
    "bedroom": ["warm amber low-key", "moody warm with soft blacks", "candlelit warm with gentle contrast"],
    "office": ["cool neutral with a warm desk accent", "night window blue with warm skin", "clean neutral corporate"],
    "classroom": ["soft daylight neutral", "warm afternoon film tone"],
    "outdoor": ["moonlit blue with warm skin", "dark green ambient with a warm accent"],
    "dungeon": ["deep red-black contrast", "candle amber with crushed blacks"],
    "fantasy-void": ["dreamy purple-magenta haze", "bioluminescent teal glow", "surreal pastel with soft contrast"],
    "beach": ["sun-washed natural with lifted blues", "golden coastal warmth", "clean bright seaside tone"],
    "ice-rink": ["cool blue-white with clean highlights", "cold silver with soft skin warmth", "high-key icy with crisp contrast"],
    "wedding": ["soft white-airy with warm skin", "classic ivory with gentle pastels", "bright airy with a light film grain"],
    "ballet": ["cream soft with gentle warm light", "pastel airy with soft skin", "natural morning tone with a light haze"],
    "snow": ["clean cold white with warm skin", "high-key winter brightness", "cool alpine with crisp contrast"],
    "flower-field": ["pastel airy with green warmth", "soft romantic pastel", "natural fresh with lifted colors"],
    "pavilion": ["classic ink-warm with soft color", "elegant warm with deep wood tones", "misty soft with muted color"],
    "entryway": ["warm neutral home tone", "soft daylight cream", "cozy warm with gentle contrast"],
    "car": ["night interior warm with cool windows", "moody dark with a warm accent", "low-key cinematic with greenish shadows"],
    "onsen": ["warm steam soft with deep blacks", "amber glow with soft skin", "moody warm with gentle contrast"],
    "library": ["moody warm with soft blacks", "amber candle with deep browns", "soft warm with a scholarly dust"],
    "cafe": ["soft cream natural light", "warm neutral with a coffee-tone accent", "bright airy with a warm wood grade"],
    "camp": ["warm firelight with deep green shadows", "dusk blue with a warm lantern accent", "earthy warm with soft contrast"],
    "kitchen": ["clean bright with warm morning light", "soft daylight cream", "warm neutral home tone"],
    "photo-booth": ["bright airy clean with soft skin", "candy pastel pop clean", "clean bright with a soft pink cast"],
    "airport": ["clean bright travel tone", "soft neutral with cool windows", "bright airy with a light film grain"],
    "gallery": ["clean gallery white with soft shadows", "muted artistic neutral", "soft high-key with gentle contrast"],
    "piano-room": ["warm wooden tones with soft light", "clean bright with warm accents", "classic warm with soft shadows"],
    "gaming-room": ["neon-cool with deep shadows", "vivid RGB contrast with clean skin", "dark moody with neon accents"],
    "park": ["natural fresh with lifted greens", "soft pastel daylight", "warm golden natural"],
    "cinema-lobby": ["warm cinematic with soft shadows", "rich midtones with poster colors", "cozy warm with gentle contrast"],
    "laundromat": ["clean bright practical tone", "soft neutral with warm accents", "slightly cool clean whites"],
    "night-market": ["warm night glow with vivid accents", "cinematic warm with steam haze", "rich contrast with neon pops"],
    "trail": ["natural fresh with green depth", "sun-washed natural with crisp air", "earthy warm with soft contrast"],
    "campus": ["clean bright campus tone", "soft daylight fresh", "warm afternoon academic"],
}
GRADE_DEFAULT = ["natural true-color restrained"]

# ---------------------------------------------------------------- beat 锚生态
# 场景类名 → 语义短语（短语渣 en 的兜底锚）
SCENE_GLOSS = {
    "studio-paper": "seamless studio", "street": "city street", "hotel": "hotel room",
    "cafe": "cafe", "library": "library", "gym": "gym", "snow": "snow slope",
    "dance-studio": "dance studio", "theatre": "stage", "work": "workplace",
    "bw-studio": "black-and-white studio", "beach": "beach", "travel": "travel",
    "special": "rooftop", "underwater": "underwater", "rooftop": "rooftop", "ice-rink": "ice rink", "wedding": "wedding",
    "photo-booth": "photo booth", "airport": "airport", "gallery": "art gallery", "piano-room": "piano room",
    "gaming-room": "gaming room", "park": "park", "cinema-lobby": "cinema lobby", "laundromat": "laundromat",
    "night-market": "night market", "campus": "campus", "trail": "mountain trail",
    "bath": "bathroom", "home": "cozy home", "camp": "camping",
    "window": "window-side", "sofa": "sofa", "mirror": "mirror gaze", "bed": "bedroom",
    "balcony": "balcony", "neon": "neon night", "ballet": "ballet studio",
    "entryway": "entryway", "kitchen": "kitchen",
    "love-hotel": "love hotel", "bedroom": "bedroom", "office": "office",
    "classroom": "classroom", "outdoor": "outdoor", "car": "car interior",
    "onsen": "hot spring onsen", "dungeon": "dungeon", "fantasy-void": "fantasy realm",
    "flower-field": "flower field", "pavilion": "pavilion",
}

# 中文主题词 → 英文锚片段（label/look 命中后拼入 beat，短语渣 en 专用）
BEAT_EXPAND = [
    ("酒店", "hotel"), ("旅馆", "hotel"), ("民宿", "guesthouse"),
    ("温泉", "hot spring onsen"), ("雪女", "snow spirit"), ("雪", "snow"),
    ("咖啡", "coffee"), ("奶茶", "milk tea"), ("奶油", "cream-soft"),
    ("私房", "boudoir soft"), ("居家", "cozy home"), ("厨房", "kitchen"),
    ("窗", "window-side"), ("纱", "sheer curtain"), ("镜", "mirror gaze"),
    ("床", "bedside"), ("浴", "after-bath"), ("淋浴", "shower"), ("浴缸", "bathtub"),
    ("沙发", "sofa"), ("玄关", "entryway"), ("阳台", "balcony"),
    ("街", "street"), ("街拍", "street style"), ("地铁", "metro"), ("外滩", "the Bund"),
    ("霓虹", "neon"), ("夜景", "night city"), ("雨", "rain"), ("雪", "snow"),
    ("花海", "flower field"), ("花园", "garden"), ("花田", "bloom field"),
    ("森林", "forest"), ("露营", "camping"), ("山脊", "mountain ridge"),
    ("海滩", "beach"), ("海边", "seaside"), ("海岛", "island"), ("泳池", "pool"),
    ("瑜伽", "yoga"), ("跑步", "running"), ("滑雪", "ski"), ("网球", "tennis"),
    ("健身", "fitness"), ("健美", "bodybuilding"), ("拳", "boxing"), ("球场", "court"),
    ("芭蕾", "ballet"), ("舞蹈", "dance"), ("舞", "dance"),
    ("走秀", "runway"), ("秀场", "runway"), ("舞台", "stage"), ("剧场", "theatre"),
    ("后台", "backstage"), ("红毯", "red carpet"), ("演唱会", "concert"),
    ("演讲", "keynote"), ("办公室", "office"), ("职场", "workplace"),
    ("教室", "classroom"), ("课堂", "classroom"), ("图书馆", "library"),
    ("书店", "bookstore"), ("书咖", "book cafe"), ("书房", "study room"),
    ("婚礼", "wedding"), ("婚纱", "wedding gown"), ("新娘", "bride"),
    ("国风", "guofeng"), ("汉服", "hanfu"), ("古风", "classical chinese"),
    ("新中式", "new-chinese style"), ("旗袍", "qipao"), ("港风", "hong kong style"),
    ("日系", "japanese style"), ("韩系", "korean style"), ("法式", "french chic"),
    ("名媛", "lady"), ("old money", "old money"),
    ("白月光", "white moonlight"), ("纯欲", "pure desire"), ("禁欲", "restrained"),
    ("妈生", "mom-natural"), ("淡感", "bare-makeup"), ("清冷", "cool-toned"),
    ("盐系", "salt style"), ("糖系", "sweet style"), ("冷白皮", "pale skin"),
    ("伪素颜", "no-makeup makeup"), ("高级感", "premium"),
    ("车震", "car sex"), ("口交", "oral"), ("骑乘", "cowgirl"), ("后入", "doggy style"),
    ("颜射", "facial"), ("自慰", "solo"), ("露出", "exhibition"),
    ("触手", "tentacle"), ("魅魔", "succubus"), ("天使", "angel"), ("恶魔", "demon"),
    ("祭坛", "altar"), ("女仆", "maid"), ("女教师", "teacher"), ("护士", "nurse"),
    ("和服", "kimono"), ("巫女", "shrine maiden"), ("鬼祭", "oni festival"), ("异界", "otherworld"),
    ("科幻", "sci-fi"), ("全息", "hologram"), ("机器", "android"), ("精灵", "elf"),
    ("花精", "flower spirit"), ("牛娘", "holstaur"), ("猫耳", "catgirl"), ("犬系", "dog"),
    ("百合", "yuri"), ("NTR", "NTR"),
    ("宠物", "pet"), ("证件", "ID photo"), ("简历", "resume"),
    ("胶片", "film"), ("黑白", "black-and-white"), ("微距", "macro"),
    ("剪影", "silhouette"), ("逆光", "backlit"), ("晨间", "morning"), ("黄昏", "dusk"),
    ("夜", "night"), ("直闪", "direct flash"),
    ("大头贴", "purikura photo booth"), ("四宫格", "four-panel photo strip"), ("拍贴", "purikura photo booth"),
    ("樱花", "sakura blossoms"), ("银杏", "ginkgo leaves"),
    ("美术馆", "art gallery"), ("画廊", "art gallery"), ("看展", "art gallery"),
    ("钢琴", "grand piano"), ("电竞", "gaming room"), ("rgb", "RGB strips"),
    ("公园", "park"), ("机场", "airport"), ("影院", "cinema lobby"), ("洗衣", "laundromat"),
    ("夜市", "night market"), ("暗黑", "dark moody"), ("长曝", "long exposure"), ("双重曝光", "double exposure"),
    ("ccd", "CCD digicam snapshot"), ("颗粒", "film grain"), ("怀旧", "retro 2016"),
    ("小红书", "xiaohongshu cover"), ("自拍", "selfie hand sign"), ("首饰", "jewelry"), ("湿发", "wet hair look"),
    ("辣妹", "spicy cool"), ("清纯", "pure youthful"), ("短光", "short light slimming"), ("魅力", "glamour"),
    ("番茄", "tomato girl style"), ("拍立得", "instant photo"), ("行李", "luggage"),
    ("锁骨", "collarbone close"), ("肩带", "strap detail"), ("冰美人", "ice queen"), ("手机", "phone screen glow"),
    ("凳沿", "stool edge"), ("蝴蝶结", "bow"), ("微醺", "tipsy"), ("拿铁", "latte warm"), ("釉面", "glazed skin"),
    ("蜂娘", "bee girl"), ("树精", "dryad"), ("根缚", "root bondage"), ("里番", "hentai anime style"),
    ("额抵", "foreheads touching"), ("共伞", "shared umbrella"), ("台阶", "steps"),
    ("外射", "cum on body"), ("透视", "x-ray view"), ("轮", "gangbang"), ("3P", "threesome"),
    ("男装", "menswear"), ("情侣", "couple"), ("闺蜜", "best friends"), ("双人", "duo"),
    ("vibe", "vibrator toy"),
    ("聚会", "party toast"), ("通勤", "commute"), ("coquette-bow", "ribbon bow coquette"), ("phone", "phone screen glow"), ("电影", "cinematic imperfect"),
    ("digicam", "digicam snapshot"), ("哥特", "gothic soft"), ("野餐", "picnic"),
    ("棱镜", "prism flare"), ("封面", "magazine cover"), ("glamour", "glamour"),
    ("水光", "glossy skin"), ("yugai", "clutching the collar"), ("原生", "natural flush"),
    ("三分", "rule of thirds"), ("框中框", "frame within frame"), ("负空间", "negative space"), ("引导线", "leading lines"),
    ("龟颈", "turtle neck posture"), ("不对称", "asymmetric shoulder"), ("低头抬眼", "chin down eyes up"),
    ("背影", "back view"), ("杯挡脸", "cup covering face"), ("门框", "half body doorway lean"),
    ("tomato", "tomato girl style"),
]


def beat_anchor(skill: str, item: dict, scene_cls: str) -> str:
    """beat 锚：主题词片段优先；en 成句（≥4 词）作为残词补在后面（大小写不敏感，防 CCD 类漏锚）。"""
    en = (item.get("en") or "").strip()
    words = [w for w in en.split() if ASCII_KW.match(w.strip("-")) and len(w.strip("-")) > 2]
    blob = f"{item['label']} {item['look']} {item['id']}"
    blob_lower = blob.lower()
    frags: list[str] = []
    joined_lower = " "
    for cn, ef in BEAT_EXPAND:
        if (cn in blob or cn in blob_lower) and ef.lower() not in joined_lower:
            frags.append(ef)
            joined_lower = " " + " ".join(frags).lower() + " "
    # 去空格归一判重：防 photo booth / photobooth 拼写变体重复追加
    norm = joined_lower.replace(" ", "")
    for w in words:
        if w not in joined_lower and w not in norm:
            frags.append(w)
            joined_lower = " " + " ".join(frags).lower() + " "
            norm = joined_lower.replace(" ", "")
    if len(frags) < 2:
        frags.insert(0, SCENE_GLOSS.get(scene_cls, scene_cls))
    return " ".join(frags)


# 机位：景别 × 角度
CAM = [
    "full-body vertical 3:4, eye-level",
    "three-quarter vertical 3:4, slightly low angle",
    "waist-up vertical 3:4, eye-level",
    "full-body vertical 3:4, low angle with vertical perspective",
    "medium close-up vertical 3:4, eye-level",
    "full-body vertical 3:4, high angle looking down",
]
CAM_DEFAULT = "full-body vertical 3:4, eye-level"

# 体位锚：erotic 体位主题 → 动作短语（优先级高于 POSE_LOOK；动作可读，配合 cam 段的 POV/景别）
POSE_ACT = [
    (("deepthroat", "深喉", "口爆"), [
        "on her knees before the partner, head tilted back accepting the shaft deep, lips stretched around it, hands on the partner's thighs, tears at the eye corners",
        "kneeling upright, lips wrapped around the shaft pressed deep, nose near the base, eyes up, saliva shining",
    ]),
    (("facesit", "坐脸", "颜面骑乘"), [
        "kneeling over a male partner's face, lowering her hips onto his mouth, thighs apart, back arched, his hands on her hips",
    ]),
    (("cunnilingus", "舔阴", "口阴"), [
        "seated with her thighs spread, one hand resting on the partner's hair below, back arched, chin lifted",
    ]),
    (("anal", "肛交", "菊"), [
        "on all fours with the back dipped low, hips raised high, entered from behind, head turned to the lens",
    ]),
    (("doggy", "后入", "后插", "背入"), [
        "on all fours with the back dipped, hips raised, a male partner behind her, entered from behind, hair falling forward",
        "kneeling on the bed with her chest lowered to the sheets, hips presented, a male partner behind her gripping her waist, head turned back to the lens",
    ]),
    (("cowgirl", "骑乘", "乘骑", "女上"), [
        "straddling the partner, knees planted on either side, hips rolling, back arched, riding motion readable",
        "seated upright astride the partner, hands on the partner's chest, head tipped back, motion readable",
    ]),
    (("missionary", "传教"), [
        "lying on her back, legs wrapped around the partner, arms above her head, face to the lens",
    ]),
    (("mating press", "种付", "压种"), [
        "lying back with her legs folded toward her shoulders, knees near her chest, pinned beneath the partner",
    ]),
    (("titjob", "乳交"), [
        "kneeling upright between a male partner's legs, breasts pressed together around the shaft, hands cupping them, eyes up",
    ]),
    (("footjob", "足交", "脚交"), [
        "reclined with her legs extended, feet pressed together around the shaft, toes pointed",
    ]),
    (("handjob", "手交"), [
        "one hand wrapped around the shaft mid-stroke, eyes on the lens, lips parted",
    ]),
    (("spitroast", "双插"), [
        "on all fours between two male partners, one shaft in her mouth and one behind her, both filled, spine level, eyes squeezed shut",
    ]),
    (("69", "六九"), [
        "inverted above the partner, hips over the partner's face, head lowered between the partner's legs",
    ]),
    (("oral", "bj", "口交", "口侍"), [
        "on her knees before the partner, lips wrapped around the shaft, gaze up to the lens, one hand at the base",
        "leaning in with parted lips near the shaft, one hand guiding, eyes on the lens",
    ]),
    (("masturbation", "自慰", "自摸", "自触"), [
        "one hand between her thighs, fingers working, head tipped back, lips parted",
        "reclined with one hand cupping her breast and the other low between her legs",
    ]),
    (("orgasm", "高潮", "绝顶"), [
        "back arched at the peak, mouth open, eyes squeezed shut, body taut, release written on the face",
    ]),
    (("facial", "颜射"), [
        "on her knees, head tilted up, face presented to receive the release, eyes half-lidded, streaks on the cheeks",
    ]),
    (("afterglow", "事后", "余韵"), [
        "spent and relaxed on rumpled sheets, damp skin, soft limbs, eyes half-lidded, tangled hair",
    ]),
    (("gangbang", "轮"), [
        "surrounded by three male partners, one shaft in her mouth, one inside her from behind, another waiting close, hands on her waist and hair",
    ]),
    (("3p", "threesome"), [
        "between two partners, one before her and one behind, both shafts inside her, face flushed to the lens",
        "two male partners close around her, one shaft in her mouth and one inside her, hands roaming",
    ]),
    (("xray", "透视"), [
        "an x-ray-style view showing the internal anatomy through translucent skin, the penetration readable inside her body",
    ]),
    (("外射", "body-cum"), [
        "kneeling upright with warm streaks of cum on her chest and belly, eyes up to the lens",
    ]),
    (("蜂娘", "bee"), [
        "in a bee-themed outfit with an antennae headband and striped accents, honey drips on her skin, one wing visible behind",
    ]),
    (("树精", "dryad", "根缚"), [
        "entwined with living roots and vines, bark textures wrapping her limbs, moss and leaves around her body",
    ]),
]

# 姿态：look 中文关键词主信号 → 英文姿态变体池（hash 选，避免同组同姿）
POSE_LOOK = [
    (("行走", "中步", "走", "street", "stride", "midstride"), [
        "mid-stride with the heel down, one hand near the pocket, stride readable",
        "mid-stride with the front toe planted, hair moving, arms swinging naturally",
        "walking toward the lens with the weight shifting to the front foot",
    ]),
    (("回头", "look-back", "over-shoulder", "overshoulder"), [
        "turning back over the shoulder, hair moving, one shoulder forward",
        "a glance back over the shoulder, one hand lifting the hair",
    ]),
    (("门框", "doorway", "peek"), [
        "half body leaning out of a doorway, one hand on the frame",
    ]),
    (("低头抬眼", "look-down", "eyes-up"), [
        "chin down with the eyes lifted to the lens",
    ]),
    (("龟颈", "turtle"), [
        "model 45-degree chin forward, one shoulder higher, beauty asymmetry",
    ]),
    (("背影", "back-view"), [
        "facing away from the lens, a back view with the head turned slightly",
    ]),
    (("fashion", "high-fashion", "lookbook", "编辑"), [
        "a high-fashion editorial stance, angular limbs, one hand at the waist, gaze past the lens",
        "a lookbook pose with clean lines, weight on one leg, chin lifted",
    ]),
    (("power", "气场", "西装"), [
        "upright power stance, shoulders squared, one hand in the jacket pocket",
    ]),
    (("地铁", "metro", "subway", "commute"), [
        "standing on a train holding the overhead strap, slight sway, one hand near the bag",
    ]),
    (("劳动", "田间", "rural"), [
        "mid-task bent slightly forward, hands at work with a tool, sleeves rolled",
    ]),
    (("健身", "fitness", "塑形"), [
        "a fitness stance with one weight in hand, muscle lines engaged",
    ]),
    (("健美", "bodybuilding"), [
        "a classic bodybuilding pose, arms flexed, muscle definition readable",
    ]),
    (("武术", "martial"), [
        "a martial arts stance, rooted low, hands in guard position",
    ]),
    (("弓步", "lunge"), [
        "a deep lunge stretch, front knee bent, arms balanced",
    ]),
    (("国标", "ballroom"), [
        "in a ballroom dance frame, one hand on the partner's shoulder, the other raised in hold",
    ]),
    (("乐手", "musician", "提琴", "violin"), [
        "violin under the chin, bow raised mid-stroke",
    ]),
    (("办公", "executive", "高管"), [
        "seated at a desk mid-task, one hand on a document, posture upright",
    ]),
    (("厨师", "chef", "灶"), [
        "mid-toss with a pan, flame rising, focused on the food",
    ]),
    (("工地", "site"), [
        "standing with a hard hat, one hand on a railing, safety vest on",
    ]),
    (("机组", "crew"), [
        "standing with a clipboard, one hand resting on the fuselage",
    ]),
    (("剪影", "silhouette"), [
        "a clean silhouette profile against the light, features in shadow",
    ]),
    (("对立式", "contrapposto"), [
        "a classical contrapposto stance, weight on one leg, hips shifted",
    ]),
    (("手部", "hands"), [
        "hands raised with fingers elegant, wrists soft, a study of gesture",
    ]),
    (("对话", "talk", "聊天"), [
        "seated mid-conversation, one hand gesturing, body turned toward the other",
    ]),
    (("婚礼", "wedding"), [
        "walking down the aisle, one hand holding the dress hem, soft steps",
    ]),
    (("红毯", "gala"), [
        "a red carpet stance, one hand on the hip, gaze to the flashing lights",
    ]),
    (("演讲", "keynote"), [
        "mid-gesture at a keynote, one arm extended toward the screen",
    ]),
    (("拳", "boxing"), [
        "a boxing guard stance, fists up, weight on the front foot",
    ]),
    (("冰旋", "skate", "滑冰"), [
        "mid-spin on the ice, arms extended, one blade raised",
    ]),
    (("坐", "sit", "sofa", "chair", "bench"), [
        "seated with knees together, back long, hands resting on the lap",
        "seated cross-legged with one elbow on the armrest",
        "seated with the legs curled under her, hugging one knee",
        "seated sideways with the legs tucked, chin resting on one hand",
    ]),
    (("靠", "lean", "wall", "rail", "栏杆", "阳台", "床头"), [
        "leaning against the surface, one foot crossed, weight on the shoulder",
        "leaning back on both hands, one knee bent, face tipped to the light",
    ]),
    (("跑", "run", "sport", "athletic", "stride", "cycle", "骑行", "aero"), [
        "mid-run with the stride open, arms engaged, motion readable",
        "a slow jog with the elbows pumping and the front foot landing soft",
        "low over the handlebars, elbows tucked, aero tuck, motion readable",
    ]),
    (("趴", "prone"), ["lying face-down on the bed, legs loosely apart, arms folded under the chin"]),
    (("躺", "lie", "bed", "recline", "床", "sheet"), [
        "reclined with the head propped, knees soft, one hand near the collarbone",
        "lying on her side with the legs loosely stacked, one hand under the cheek",
        "lying back with the arms stretched overhead, one knee raised",
    ]),
    (("盯镜", "cover gaze"), ["eyes locked to the lens, chin lifted, editorial cover confidence"]),
    (("跪", "kneel"), ["kneeling upright, hands on the thighs, spine long"]),
    (("蹲", "crouch", "squat"), ["low crouch with elbows on the knees, weight settled"]),
    (("跳", "jump", "腾空"), ["frozen mid-jump, knees tucked, arms sweeping"]),
    (("ski", "snow"), [
        "carving a ski turn with knees bent, poles at the side, snow spray behind",
        "gliding downhill with the body low, poles planted, one arm tucked",
    ]),
    (("surf", "冲浪"), [
        "riding a wave on a surfboard, knees bent, one arm out for balance",
        "standing on a surfboard mid-turn, arms spread, spray around",
    ]),
    (("街舞", "hiphop"), [
        "frozen mid-breakdance move, one hand on the ground, legs swept, urban energy",
        "a b-boy freeze with the body balanced on one arm, sneakers up",
    ]),
    (("舞", "dance", "stage", "ballet", "balletcore"), [
        "dance line with one arm extended, the opposite leg pointed, chin lifted",
        "a rehearsal turn with the arms rounded and the weight on one toe",
    ]),
    (("s线", "scurve", "编辑", "editorial"), [
        "weight on the back leg, soft S-curve, chin slightly lifted",
        "an exaggerated S-line with the hip popped and the shoulders rolled back",
    ]),
    (("伸手", "reach", "拉环", "handhold"), ["reaching up with one hand, the body stretched into the line"]),
    (("瑜伽", "yoga", "伸展", "stretch"), [
        "in a slow stretch with the arms long, one leg extended",
        "a seated forward fold with the spine long and the hands reaching past the toes",
    ]),
    (("mirror", "self-gaze", "对镜", "镜前", "镜自拍"), ["facing the mirror with one hand near the shoulder, meeting her own eyes"]),
    (("窗", "window", "sill", "半开"), [
        "seated on the sill with one knee drawn up, face turned to the light",
        "kneeling on the sill cushion with both hands on the frame",
    ]),
    (("跪坐", "正座"), ["kneeling back on the heels, hands on the thighs, spine long"]),
    (("爬", "climb", "爬行"), ["on all fours, back arched softly, knees wide"]),
]
POSE_DEFAULT = {
    "figure": ["weight on the back foot, one hand on the hip, eyes to the lens", "three-quarter stance with the near shoulder forward", "standing tall with the chin lifted and hands relaxed"],
    "youth": ["soft self-gaze with the chin dipped and one hand near the face", "half-lidded look over the shoulder, one knee drawn up", "stretched back against the cushions, arms long"],
    "erotic": ["hips seated fully, knees apart, back arched, act readable", "on all fours with the back dipped, head turned to the lens", "kneeling with the chest lifted, hands on the thighs"],
}

# 段 1 摄影类型
GENRE = {
    "figure": ("editorial still", "clean commercial fashion photography"),
    "youth": ("cinematic still", "intimate lifestyle photography"),
    "erotic": ("cinematic still", "cinematic erotic photography"),
}
SKIN = {
    "figure": "soft product-clean skin",
    "youth": "soft natural skin",
    "erotic": "soft skin with honest texture",
}


def all_combos() -> list[dict]:
    text = CAT.read_text(encoding="utf-8")
    out = []
    for skill, const in (("figure", "FIGURE"), ("youth", "YOUTH"), ("erotic", "EROTIC")):
        for c in bcg.parse_combos(bcg.grab_const(text, const)):
            out.append({"skill": skill, **c, "file": f"hot-{skill}-{bcg._slug_hash(c['id'].replace('combo-', ''))}.jpg"})
    return out


def class_of(skill: str, item: dict, table) -> str | None:
    cid = f"{item['id']}".lower()
    label = f"{item['label']}".lower()
    blob = f"{item['label']} {item['look']} {item['group']} {item['en']}".lower()
    # 主题锚三级：id（英文 slug 机器主题）> label（组合包名）> 全 blob（look/group/en 细节词）
    for kws, cls, _variants in table.get(skill, []):
        for kw in kws:
            if kw_match(kw, cid):
                return cls
    for kws, cls, _variants in table.get(skill, []):
        for kw in kws:
            if kw_match(kw, label):
                return cls
    for kws, cls, _variants in table.get(skill, []):
        for kw in kws:
            if kw_match(kw, blob):
                return cls
    return None


# 成套协调：场景类 → 衣着类池（无关键词命中时按场景伪随机，防 gym 配晚装式错位）
WARDROBE_BY_SCENE = {
    "figure": {
        "street": ["street"], "studio-paper": ["editorial"], "gym": ["sport"], "dance-studio": ["dance"],
        "theatre": ["dance", "editorial"],
        "work": ["office"], "bw-studio": ["editorial"], "travel": ["campus"], "special": ["sport"],
        "underwater": ["dress"], "rooftop": ["street", "campus"],
        "home": ["home"], "bath": ["bath-robe", "home"], "beach": ["dress"],
        "ice-rink": ["skate-dress"], "wedding": ["bridal", "cocktail"], "snow": ["sport"],
        "flower-field": ["dress"], "pavilion": ["guofeng", "dress"],
        "hotel": ["home", "bath-robe"], "cafe": ["street", "home"], "library": ["campus"],
        "camp": ["campus", "sport"],
        "photo-booth": ["street", "campus"],
        "airport": ["campus", "street"], "gallery": ["street", "campus"], "piano-room": ["campus", "street"],
        "gaming-room": ["street", "campus"], "park": ["campus", "street"], "cinema-lobby": ["street", "campus"],
        "laundromat": ["street", "campus"], "night-market": ["street", "campus"],
        "campus": ["campus"], "trail": ["sport"],
    },
    "youth": {
        "bed": ["shirt", "dress"], "sofa": ["knit"], "window": ["dress", "knit"], "mirror": ["dress"],
        "bath": ["robe", "shirt"], "balcony": ["knit"], "hotel": ["robe"], "neon": ["shirt"],
        "ballet": ["ballet"], "entryway": ["shirt", "knit"], "kitchen": ["knit", "shirt"],
    },
    "erotic": {
        "hotel": ["silk-robe", "lingerie"], "love-hotel": ["lingerie"], "bedroom": ["lingerie", "silk-robe"],
        "bath": ["nude", "lingerie"], "office": ["undress"], "classroom": ["uniform"],
        "outdoor": ["undress"], "dungeon": ["lingerie"], "fantasy-void": ["lingerie"],
        "car": ["undress"], "onsen": ["nude", "lingerie"], "library": ["lingerie", "undress"],
    },
}


def scene_variant(skill: str, item: dict, gen: int) -> tuple[str, str]:
    cls = class_of(skill, item, SCENE)
    if cls is None:
        cls = pick(skill, item["id"], "scene-fb", gen, SCENE_FALLBACK[skill])
    variants = next((v for _k, c, v in SCENE.get(skill, []) if c == cls), None) or []
    return cls, pick(skill, item["id"], "scene", gen, variants)


def wardrobe_variant(skill: str, item: dict, gen: int, scene_cls: str = "") -> tuple[str, str]:
    cls = class_of(skill, item, WARDROBE)
    if cls is None:
        pool = WARDROBE_BY_SCENE.get(skill, {}).get(scene_cls) or [WARDROBE_DEFAULT[skill]]
        cls = pick(skill, item["id"], "wardrobe-fb", gen, pool)
    variants = next((v for _k, c, v in WARDROBE.get(skill, []) if c == cls), None) or []
    return cls, pick(skill, item["id"], "wardrobe", gen, variants)


def light_variant(skill: str, item: dict, gen: int, scene_cls: str) -> str:
    blob = f"{item['id']} {item['label']} {item['look']} {item['en']}".lower()
    if any(kw_match(k, blob) for k in CLAM_KW):
        return "clam-shell beauty light, even fill, soft falloff"
    pool = LIGHT.get(scene_cls) or LIGHT_DEFAULT
    return pick(skill, item["id"], "light", gen, pool)


def grade_variant(skill: str, item: dict, gen: int, scene_cls: str) -> str:
    pool = GRADE.get(scene_cls) or GRADE_DEFAULT
    return pick(skill, item["id"], "grade", gen, pool)


# 特写/美妆类组合 → 近景机位池
CAM_CLOSE = [
    "close-up vertical 3:4, eye-level",
    "extreme close-up detail vertical 3:4, eye-level",
    "medium close-up chest face vertical 3:4, eye-level",
]
CLOSE_KW = ("特写", "头肩", "macro", "美妆", "beauty", "clam", "唇", "眼部", "五官", "headshot", "头像", "证件")
CLAM_KW = ("美妆", "beauty", "clam", "蚌")


def cam_variant(skill: str, item: dict, gen: int) -> str:
    blob = f"{item['id']} {item['label']} {item['look']} {item['en']}".lower()
    if kw_match("pov", blob):
        return "POV framing, subject facing the lens"
    if any(kw_match(k, blob) for k in CLOSE_KW):
        return pick(skill, item["id"], "cam", gen, CAM_CLOSE)
    pose = pose_variant(skill, item, gen)
    pool = CAM
    # 行走/跑跳/舞蹈/腾空/大动作类姿势需要全身景别承载
    if any(k in pose for k in ("stride", "walk", "run", "jump", "dance", "pointed toe", "arms engaged",
                               "airborne", "spin", "mid-toss", "stance", "sway", "arc", "guard",
                               "flexed", "mid-stroke", "sweeping")):
        pool = [c for c in CAM if "full-body" in c or "three-quarter" in c]
    return pick(skill, item["id"], "cam", gen, pool)


def pose_variant(skill: str, item: dict, gen: int) -> str:
    blob = f"{item['label']} {item['look']} {item['id']} {item['en']}".lower()
    # 体位锚优先（erotic 体位主题压过通用姿势词）
    for kws, phrases in POSE_ACT:
        for kw in kws:
            if kw_match(kw, blob):
                return pick(skill, item["id"], f"pose-act:{kw}", gen, phrases)
    for kws, phrases in POSE_LOOK:
        for kw in kws:
            if kw_match(kw, blob):
                return pick(skill, item["id"], f"pose:{kw}", gen, phrases)
    pool = POSE_DEFAULT[skill]
    return pick(skill, item["id"], "pose", gen, pool)


def render_prompt(skill: str, item: dict, gen: int, dims: dict | None = None, outfit: str | None = None, scene_sent: str | None = None) -> str:
    if dims:
        scene_cls = dims["scene"]
        light = dims["light"]
        grade = dims["grade"]
        cam = dims["cam"]
        pose = dims["pose"]
    else:
        scene_cls, scene_sent = scene_variant(skill, item, gen)
        light = light_variant(skill, item, gen, scene_cls)
        grade = grade_variant(skill, item, gen, scene_cls)
        cam = cam_variant(skill, item, gen)
        pose = pose_variant(skill, item, gen)
    if not scene_sent:
        scene_sent = _scene_sentence(skill, scene_cls, item, gen)
    if not outfit:
        outfit = wardrobe_variant(skill, item, gen, scene_cls)[1]
    still, genre = GENRE[skill]
    skin = SKIN[skill]
    cast = CAST_FIX.get(f"{skill}:{item['id']}") or {}
    lock = cast.get("lock") or LOCK[skill]
    subj = cast.get("subj") or "a photoreal adult East Asian woman"
    pn = cast.get("pn") or "She"
    pn_verb = "are" if pn == "They" else "is"
    obj = cast.get("obj") or "her"
    wear_pn = cast.get("wear") or "She"
    fill = cast.get("fill") or "She fills most"

    p1 = (
        f"This is a {cam} {still} with {genre}: {subj} "
        f"frozen mid-pose—{pose}, {skin}, garment lines readable toward the lens, "
        f"the shot built around the {beat_anchor(skill, item, scene_cls)} beat."
    )
    arousal = " Arousal reads honest—soft flush, damp skin." if skill == "erotic" else ""
    wear_v = "wear" if wear_pn == "They" else "wears"
    main = (
        f"Main subject: {lock} {pn} {pn_verb} frozen mid-pose—{pose}; the pose reads clearly from one frozen beat, "
        f"nothing between {obj} and the lens. {wear_pn} {wear_v} {outfit}, fabric drape readable.{arousal} {BAN[skill]}"
    )
    env = (
        f"Environmental background: A setting of {scene_sent}, with two to four readable anchors; "
        f"depth falls away softly behind {obj}; no clutter competing with the figure."
    )
    comp = (
        f"Composition and atmosphere: {fill} of the vertical frame with a thin margin; "
        f"visual center on the pose line; {light}; gentle fill, thin hair rim; "
        f"finished in a {grade} grade; masterpiece, best quality."
    )
    text = "\n\n".join([p1, main, env, comp])
    words = len(text.split())
    if words > 380:  # 压缩序：先砍 Env/Comp 修饰，永不砍动作与主光
        env = f"Environmental background: {scene_sent}; two to four readable anchors only."
        comp = f"Composition and atmosphere: {light}; {grade} grade; masterpiece, best quality."
        text = "\n\n".join([p1, main, env, comp])
    if CJK.search(text):
        raise ValueError(f"prompt contains CJK for {skill}:{item['id']}")
    return text


def collision_report(items: list[dict], rendered: dict) -> dict:
    """按组统计六维指纹完全相同的条目对，超阈值打印警告。"""
    from collections import defaultdict

    by_group = defaultdict(list)
    for it in items:
        key = f"{it['skill']}:{it['id']}"
        dims = rendered[key]["dims"]
        fp = (dims["scene"], dims["wardrobe"], dims["light"], dims["pose"], dims["cam"], dims["grade"])
        by_group[(it["skill"], it["group"])].append((fp, key))
    report = {}
    for (skill, grp), entries in by_group.items():
        fps = [fp for fp, _k in entries]
        dup = len(fps) - len(set(fps))
        rate = dup / len(fps) if fps else 0
        report[f"{skill}|{grp}"] = {"n": len(fps), "dup_fingerprints": dup, "dup_rate": round(rate, 3)}
        if rate > 0.2:
            print(f"[warn] 组内指纹重复率 {rate:.0%}：{skill} / {grp}（{dup}/{len(fps)}），建议扩表", file=sys.stderr)
    return report


# 历史坏种子规避：加固定偏移换一个可复现的新种子（试跑实测：campaign-center 出漂浮伪影）
SEED_FIX = {"figure:combo-campaign-center": 987654321}

# 历史雷同规避：强制覆盖指定组合的维度（终验收实测：cosplay-hotel 与 japanese-hotel 场景/机位/姿态撞车）
DIM_FIX = {
    "erotic:combo-cosplay-hotel": {
        "scene": "bedroom",
        "pose": "standing by the bed with one knee on the mattress, costume half-removed, one shoulder bared",
        "cam": "three-quarter vertical 3:4, eye-level",
    },
    # 终验收实测：近景机位被全身靠墙姿态带偏 → 强制头肩姿态配近景 + 空背景句
    "figure:combo-headshot-clean": {
        "pose": "seated straight upright, chin level, shoulders squared to the lens, eyes to the lens, both hands resting below the frame out of view, no waist, no hips, no legs, no feet, no shoes visible",
        "cam": "extreme close-up headshot portrait, head and shoulders only, cropped just below the collarbone, 85mm portrait lens, vertical 3:4, eye-level",
        "scene_sent": "a clean neutral seamless studio backdrop, completely empty, no stands, no lamps, no equipment in frame",
        "wardrobe": "a tailored blazer over a white shirt with pointed flats, fully dressed, SFW business portrait",
    },
    # 终验收实测：伸向镜头的手反复畸形 → 强制双手交叠低垂姿态
    "figure:combo-cn-guofeng-pavilion": {
        "pose": "standing with both hands clasped low in front, sleeves hanging long, chin lifted gently",
    },
    # 终验收实测：leaning back 被模型画成跪撑前倾 → 强制坐靠床头描述
    "youth:combo-hmcp-headboard": {
        "pose": "seated with her back pressed flat against the headboard, knees drawn up toward her chest, arms hugging her knees lightly, face turned to the lens",
    },
    # 自检实测：异界列车条目命中 fantasy-void 通用池（浮空符文），场景与列车主题不符 → 强制列车车厢场景句
    "erotic:combo-train-void": {
        "scene_sent": "a surreal train carriage with windows showing a passing void, warm lamps and drifting dust",
    },
    # 自检实测：网球条目命中 gym 池的攀岩墙变体 → 强制网球场场景句
    "figure:combo-out-tennis": {
        "scene_sent": "a tennis court with painted lines, a net behind her and a racket resting on the bench",
    },
    # 自检实测：雨巷条目命中 street 池的天桥变体（无雨无霓虹）→ 强制雨夜巷弄场景句
    "figure:combo-hk-rain-alley": {
        "scene_sent": "a narrow Hong Kong alley at night in the rain, neon signs glowing on wet pavement",
    },
    # 自检实测：双插三人构图需侧面全身景别（正面视角后部被躯干遮挡）→ 强制侧面
    "erotic:combo-dp-focus": {
        "pose": "on all fours in profile, a male partner at each end of her body, one shaft deep in her mouth and the other shaft buried inside her from behind, her underwear pulled aside, her spine level between them",
        "cam": "full-body side view vertical 3:4, profile angle",
    },
    # 自检实测：大头贴三兄弟未进主题锚表 → 场景随机/全身机位，与「近脸闪光拍贴」主题不符 → 强制近脸+拍贴机/四宫格布局
    "figure:combo-purikura-close": {
        "pose": "face close to the lens with a playful soft expression, one hand raised near the cheek in a small peace sign, bright flash catchlights in the eyes",
        "cam": "tight face close-up portrait, tight face crop, vertical 3:4, eye-level",
    },
    "figure:combo-purikura-four-cut-series": {
        "scene_sent": "a four-panel 2x2 photo strip layout on a clean bright backdrop, the same adult face in four playful expression variations with tiny hand changes, purikura-style frame stickers at the panel edges",
        "pose": "face close to the lens, one playful expression per panel with tiny hand changes, bright flash catchlights in the eyes",
        "cam": "face close-up photo strip grid, tight face crop, bright beauty flash, vertical 3:4, eye-level",
    },
    "figure:combo-purikura-photobooth": {
        "scene": "photo-booth",
        "pose": "leaning slightly toward the lens with a playful soft expression, one hand near the cheek, bright flash catchlights in the eyes",
        "cam": "close-up face portrait with tight face crop, bright beauty flash, vertical 3:4, eye-level",
    },
    # 男像/双人主体覆盖配套：男装姿态与双人动作（主体由 CAST_FIX 替换）
    "figure:combo-male-suit": {
        "pose": "standing with relaxed upright posture, shoulders open, one hand adjusting the jacket lapel, calm eyes to the lens",
        "wardrobe": "a tailored navy suit with a white shirt and polished leather shoes",
    },
    "figure:combo-male-trench": {
        "pose": "standing tall with one hand in the coat pocket, weight shifted, gaze past the camera",
        "wardrobe": "a long camel trench coat over a dark knit, tailored trousers and leather boots",
    },
    "figure:combo-male-oversized": {
        "pose": "mid-stride with hands in pockets, shoulders soft, cool city stance",
        "wardrobe": "an oversized boxy jacket with wide-leg trousers and chunky sneakers",
    },
    "figure:combo-male-workwear": {
        "pose": "leaning against a wall with one foot up, hands in pockets",
        "wardrobe": "a canvas work jacket with utility trousers and rugged boots",
    },
    "figure:combo-male-techwear": {
        "pose": "standing with functional layering readable, one hand adjusting a chest strap",
        "wardrobe": "a black techwear shell with cargo straps and futuristic sneakers",
    },
    "figure:combo-male-street-asian": {
        "pose": "mid-stride freeze, one hand in the jacket pocket, gaze past the camera",
        "wardrobe": "an oversized street jacket, relaxed trousers and sneakers",
    },
    "figure:combo-male-headshot-asian": {
        "pose": "head and shoulders square to the camera, chin level, even loop light, slight smile",
        "cam": "headshot portrait, head and shoulders only, vertical 3:4, eye-level",
        "wardrobe": "a blazer over a white shirt, clean business portrait",
    },
    "figure:combo-male-old-money": {
        "pose": "tall spine, hands loosely clasped in front, calm eyes",
        "wardrobe": "a navy knit under a beige blazer, tailored trousers",
    },
    "figure:combo-male-athletic": {
        "pose": "athletic stance with a towel on the neck, light sweat, mid-recovery",
        "wardrobe": "sportswear with light sweat, athletic fit",
    },
    "figure:combo-couple-walk": {"pose": "walking side by side, near hands loosely linked, matching pace"},
    "figure:combo-couple-forehead": {"pose": "facing each other half-step apart, foreheads gently together, eyes soft"},
    "figure:combo-duo-walk-couple": {"pose": "walking side by side, near hands loosely linked, matching pace"},
    "figure:combo-cp-walk": {"pose": "walking side by side, her hand lightly on his arm, matching pace"},
    "figure:combo-cp-forehead": {"pose": "facing each other half-step apart, foreheads gently together, eyes soft or closed"},
    "figure:combo-cp-umbrella": {"pose": "sharing one umbrella, close together under the rain, wet street"},
    "figure:combo-cp-airport": {"pose": "standing with luggage between them, travel layers, soft eye contact"},
    "figure:combo-gm-walk": {"pose": "two women walking side by side mid-laugh"},
    "figure:combo-gm-steps": {"pose": "sitting on outdoor steps at staggered heights, one leaning toward the other mid-laugh"},
    "figure:combo-gm-mirror": {
        "pose": "both standing before a full-length fitting mirror, different hand poses, OOTD mood",
        "scene_sent": "a fitting room with a full-length mirror and a soft bench, clothes racks at the edge",
    },
    "figure:combo-lf-friend-walk": {"pose": "two women walking side by side mid-laugh"},
    "figure:combo-lf-party-toast": {
        "pose": "raising a glass mid-toast, looking away from the lens, party casual",
        "scene_sent": "a rooftop party with string lights, one drink table and a few blurred guests in the background",
    },
    "figure:combo-hero-pet": {"pose": "standing with a small dog beside her looking up, one hand near the pet"},
    "figure:combo-hero-hero-male-soft": {
        "pose": "standing in the foreground sharp, a male companion softly out of focus behind her",
    },
    "erotic:combo-hero-noface-him": {
        "pose": "seated close against the partner, her face to the lens, his face cropped out of frame above the chin",
    },
    # 技术风格类主题：光线/调色/场景句强制（此前六路全空）
    "figure:combo-dark-moody": {
        "light": "one hard side key with deep shadow falloff",
        "grade": "low-key moody with crushed blacks",
    },
    "figure:combo-long-ghost": {
        "pose": "standing still while a translucent ghost trail of her own motion blurs behind her",
        "scene_sent": "a night street scene with long-exposure ghost trails of passing motion",
    },
    "figure:combo-double-expose": {
        "scene_sent": "a double-exposure layered composition, the portrait ghosted over a second texture scene",
    },
    # 季节条目：场景类命中 flower-field 但需强制对应植物（樱花/银杏）
    "figure:combo-sakura-season": {
        "scene_sent": "a park path under full-bloom cherry trees, pink petals drifting in the air, one bench",
    },
    "figure:combo-ginkgo-season": {
        "scene_sent": "a ginkgo avenue with golden leaves carpeting the ground, one lamppost",
    },
    "figure:combo-sakura-ginkgo-season": {
        "scene_sent": "a park path with cherry blossoms and ginkgo trees, petals and golden leaves mixing on the ground",
    },
    "figure:combo-sakura-cny-red": {
        "scene_sent": "a street with cherry blossoms and red Chinese New Year lanterns, petals in the air",
    },
    # 光线向条目：强制对应布光（此前六路全空）
    "erotic:combo-light-light-rim-dark": {"light": "a hard rim light carving the silhouette against deep darkness"},
    "erotic:combo-light-light-side-moody": {"light": "one moody side light raking across the figure"},
    "erotic:combo-light-light-topdown-boudoir": {"light": "a top-down softbox glow over the boudoir scene"},
    # 妆发场景快套：强制居家场景（youth SCENE 无 home 类，用 bed 卧居兜底）
    "youth:combo-mk-home-bai": {"scene": "bed"},
    "youth:combo-mk-home-coquette": {"scene": "bed"},
    "youth:combo-mk-home-jinyu": {"scene": "bed"},
    "youth:combo-mk-home-pure": {"scene": "bed"},
    # 凳沿主题：强制凳沿坐姿（beat 有锚但姿势随机）
    "youth:combo-hmcp-stool-edge": {
        "pose": "perched on the edge of a stool, back long, knees together, spine curve readable",
    },
    # 双主题组合：书咖·屋顶停车 → 强制屋顶停车+书咖场景句
    "figure:combo-sc-book-cafe": {
        "scene_sent": "a rooftop parking deck with a city skyline, one book cafe storefront at the corner",
    },
    "figure:combo-sc-parking-roof": {
        "scene_sent": "a rooftop parking lot with painted bays, one book cafe entrance at the corner",
    },
    # 水下漂浮：漂浮姿态 + 完整泳装 + 水下场景（special 杂类拆分后逐条强制）
    "figure:combo-underwater-float": {
        "scene": "underwater",
        "pose": "floating weightless underwater, hair drifting, arms extended softly, body horizontal mid-water",
        "wardrobe": "a modest one-piece swimsuit, fully covered, SFW swimwear",
    },
    "figure:combo-aerial-ridge": {
        "scene_sent": "a mountain ridge seen from a high aerial drone angle, tiny figure on the trail, sweeping valleys below",
        "light": "high aerial daylight, even and clear",
    },
    "figure:combo-industrial-scale": {
        "scene_sent": "a vast industrial structure with steel girders and pipes, one walkway and dramatic scale",
        "light": "cool overcast with strong structural shadows",
    },
    "figure:combo-fog-silhouette": {
        "scene_sent": "a thick fog bank over a quiet street, one lamp glowing, soft grey air",
        "light": "soft diffused fog light, one dim lamp glow",
    },
    "figure:combo-cv-rooftop-golden": {
        "light": "golden hour rooftop wash",
    },
    # 场景词错位清理：风格/状态词从场景类词表移除后，逐条强制正确场景句
    "figure:combo-cn-travel-desert-scale": {
        "scene_sent": "a vast desert dune field with one distant ridge and heat haze",
    },
    "figure:combo-jp-mori-forest": {
        "scene_sent": "a deep mossy forest with tall trees, one path and soft green light",
    },
    "erotic:combo-desk-balcony-risk": {
        "scene_sent": "a private balcony at dusk with a railing and city lights",
    },
    "erotic:combo-desk-bent": {
        "scene_sent": "a wooden desk in a quiet room, one lamp and scattered papers",
    },
    "erotic:combo-desk-sink-mirror": {"scene": "bath"},
    "erotic:combo-desk-vanity-prepare": {
        "scene_sent": "a vanity table with a round mirror and warm bulbs",
    },
    "erotic:combo-freeuse-home": {"scene": "bedroom"},
    "youth:combo-sc-wet-path3": {
        "scene_sent": "a rain-washed stone path with puddles and one streetlamp",
    },
    # 全盘检查：风景/山脊/职业衣着类补锚
    "figure:combo-golden-hour-land": {
        "scene_sent": "an open landscape at golden hour with a warm sky, one distant tree line and long shadows",
    },
    "figure:combo-adventure-ridge": {
        "scene_sent": "a mountain ridge trail with sweeping valleys below, one signpost and morning light",
    },
    "figure:combo-rural-labor": {
        "wardrobe": "plain work clothes with rolled sleeves, worn denim and sturdy boots",
    },
    "figure:combo-musician-bow": {
        "wardrobe": "a formal concert black dress, understated and elegant",
    },
    "figure:combo-crew-hangar": {
        "wardrobe": "a flight crew uniform with a badge lanyard, clean and functional",
    },
    "figure:combo-graduate-adult": {
        "wardrobe": "a graduation gown with a cap, tassel and a plain outfit beneath",
    },
    "figure:combo-mtb-air": {
        "wardrobe": "a full-face helmet, padded cycling jersey and knee pads",
        "pose": "airborne off a dirt jump on a mountain bike, both wheels off the ground, body leaned over the bars",
    },
    # 两女一男：POSE_ACT 的 3p 短语是两男型，ffm 需专属双女动作
    "erotic:combo-threesome-ffm": {
        "pose": "two women sharing one male partner, one kissing him while the other rides him, both bodies close, cooperative motion readable",
    },
    "erotic:combo-amateur-couple": {
        "pose": "close with the partner on a bed, casual intimate position, soft eye contact, lifelike spontaneous mood",
    },
    "erotic:combo-shared-orgasm": {
        "pose": "both mid-ecstasy in sync, bodies arched together, faces to the lens, shared release readable",
    },
    "erotic:combo-hero-drained": {
        "pose": "astride the drained male hero beneath her, hips rolled forward, one hand on his chest, soul-glow accent",
    },
    "erotic:combo-femboy-solo": {
        "pose": "reclined in lingerie, one hand low between the legs, soft androgynous lines, eyes half-lidded to the lens",
    },
    "figure:combo-senior-window": {
        "pose": "seated by the window, hands folded on the lap, calm eyes to the lens",
    },
    "figure:combo-ballroom-frame": {
        "pose": "in a ballroom dance frame, one hand on the partner's shoulder, the other raised in hold, both mid-sway",
    },
    "erotic:combo-femboy-solo": {
        "scene": "bedroom",
        "wardrobe": "lace lingerie with a garter belt, soft androgynous styling",
    },
    "figure:combo-rural-labor": {
        "scene_sent": "a farm field with crop rows, one wooden cart and open sky",
    },
    "figure:combo-senior-window": {
        "wardrobe": "an elegant knit cardigan over a silk blouse, tailored trousers, refined and age-appropriate",
    },
    # 对镜类条目：姿态要求镜子但场景随机无镜 → 强制镜面场景句
    "figure:combo-st-mall-mirror": {
        "scene_sent": "a mall storefront with a full-length mirror panel, one mannequin beside it",
    },
    "figure:combo-sf-mirror-full": {
        "scene_sent": "a bedroom wall with a full-length mirror, one jewelry tray below",
    },
    "figure:combo-sf-elevator": {
        "scene_sent": "an elevator interior with a mirrored wall, warm cabin light",
    },
    "figure:combo-cv-mirror-ootd": {
        "scene_sent": "a boutique fitting area with a full-length mirror, soft store light",
    },
    "figure:combo-mirror-concept": {
        "scene_sent": "a minimalist space with one large standing mirror, the figure doubled in the reflection",
    },
    "erotic:combo-mirror-clone": {
        "scene_sent": "a dim room with a large floor mirror, the figure doubled in the reflection",
    },
    # 樱花雪组合：樱花场景缺雪元素 → 强制樱花+残雪句
    "figure:combo-sakura-snow-portrait": {
        "scene_sent": "cherry blossoms in full bloom with late snow dusting the branches, petals on white ground",
    },
    # 共伞条目：street 变体可能无雨 → 强制雨街句
    "figure:combo-cp-umbrella": {
        "scene_sent": "a rain-washed street with wet reflections, the two close under one umbrella",
    },
}


def _scene_sentence(skill: str, scene_cls: str, item: dict, gen: int) -> str:
    variants = next((v for _k, c, v in SCENE.get(skill, []) if c == scene_cls), None) or []
    return pick(skill, item["id"], "scene", gen, variants)


def build_all(gen: int) -> dict:
    items = all_combos()
    out = {"gen": gen, "templateVersion": TEMPLATE_VERSION, "generatedAt": date.today().isoformat(), "items": {}}
    word_buckets = {"<200": 0, "200-380": 0, ">380": 0}
    for it in items:
        key = f"{it['skill']}:{it['id']}"
        fix = DIM_FIX.get(key) or {}
        scene_cls, scene_sent = scene_variant(it["skill"], it, gen)
        if fix.get("scene"):
            scene_cls = fix["scene"]
            scene_sent = _scene_sentence(it["skill"], scene_cls, it, gen)
        if fix.get("scene_sent"):
            scene_sent = fix["scene_sent"]
        _wc, outfit = wardrobe_variant(it["skill"], it, gen, scene_cls)
        if fix.get("wardrobe"):
            outfit = fix["wardrobe"]
        pose = fix.get("pose") or pose_variant(it["skill"], it, gen)
        cam = fix.get("cam") or cam_variant(it["skill"], it, gen)
        dims = {
            "scene": scene_cls, "wardrobe": _wc,
            "light": fix.get("light") or light_variant(it["skill"], it, gen, scene_cls),
            "pose": pose,
            "cam": cam,
            "grade": fix.get("grade") or grade_variant(it["skill"], it, gen, scene_cls),
        }
        prompt = render_prompt(it["skill"], it, gen, dims=dims, outfit=outfit, scene_sent=scene_sent)
        w = len(prompt.split())
        word_buckets["<200" if w < 200 else ">380" if w > 380 else "200-380"] += 1
        out["items"][key] = {
            "skill": it["skill"], "id": it["id"], "label": it["label"], "file": it["file"],
            "seed": (h(it["skill"], it["id"], "seed", gen) + SEED_FIX.get(key, 0)) % 9007199254740991,
            "dims": dims, "prompt": prompt, "status": "pending", "tries": 0, "err": "",
        }
    report = collision_report(items, out["items"])
    # 前置门禁：主题锚六路全空（场景/体位/姿态/衣着/beat/强制/主体覆盖 全无锚）→ 高危货不对板
    # 设计豁免：维度向/随机/词预算/连续锁/妆发套餐等 combo，主题在维度上、场景随机为预期
    GATE_EXEMPT = ("nine-dim", "six-dim", "nine-axes", "six-axes", "lock-series", "zoom-", "makeup-",
                   "emk-", "open-", "cl-", "hair-", "comp-", "mk-")
    unanchored = []
    exempt = []
    for it in items:
        key = f"{it['skill']}:{it['id']}"
        if key in DIM_FIX or key in CAST_FIX:
            continue
        en = (it.get("en") or "").strip()
        words = [w for w in en.split() if ASCII_KW.match(w.strip("-")) and len(w.strip("-")) > 2]
        blob = f"{it['label']} {it['look']} {it['id']}"
        if len(words) >= 2 or any(cn in blob for cn, _ef in BEAT_EXPAND):
            continue
        if class_of(it["skill"], it, SCENE) is not None or class_of(it["skill"], it, WARDROBE) is not None:
            continue
        if any(kw_match(k, it["id"] + " " + it["label"]) for kws, _p in POSE_ACT for k in kws):
            continue
        if any(kw_match(k, it["id"] + " " + it["label"]) for kws, _p in POSE_LOOK for k in kws):
            continue
        if any(p in it["id"] for p in GATE_EXEMPT):
            exempt.append(key)
            continue
        unanchored.append(key)
    if unanchored:
        print(f"[gate] 主题锚六路全空 {len(unanchored)} 条（高危货不对板）:", file=sys.stderr)
        for k in sorted(unanchored):
            print("   ", k, file=sys.stderr)
    else:
        print("[gate] 主题锚覆盖 0 缺口", file=sys.stderr)
    if exempt:
        print(f"[gate] 设计豁免（维度向/随机/词预算/连续锁）{len(exempt)} 条", file=sys.stderr)
    print(f"[ok] {len(items)} prompts  gen={gen}  words={word_buckets}")
    return out, report


def main() -> int:
    ap = argparse.ArgumentParser(description="674 组合包差异化形态 A 提示词生成器")
    ap.add_argument("--gen", type=int, default=2, help="代际计数（换代表全量换变体与 seed）")
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--check-stale", action="store_true", help="只与 catalog 比对缺漏，不写文件")
    args = ap.parse_args()

    data, _report = build_all(args.gen)
    if args.check_stale:
        cur = set()
        if args.out.is_file():
            old = json.loads(args.out.read_text(encoding="utf-8"))
            cur = set((old.get("items") or {}).keys())
        new = set(data["items"].keys())
        print(f"[check-stale] catalog={len(new)}  file={len(cur)}  missing={sorted(new - cur)[:10]}  extra={sorted(cur - new)[:10]}")
        return 0
    args.out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[ok] wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
