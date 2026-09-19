# -*- coding: utf-8 -*-
"""一次性审计：跨维度矛盾检测（pose/cloth 动作 vs scene 场景的冲突组合）。只读。"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "scripts" / "combo-prompts.json").read_text(encoding="utf-8"))

# 规则：pose/wardrobe 特征词 → 必须出现的 scene 类（或禁出现的 scene 类）
POSE_RULES = [
    ("滑雪动作", r"carving a ski|gliding downhill|poles at the side|snow spray", {"must": ["snow"]}),
    ("冲浪动作", r"surfboard|riding a wave", {"must": ["beach"]}),
    ("芭蕾动作", r"dance line|rehearsal turn|barre|pointed toe|ballet", {"must": ["dance-studio", "ballet", "theatre"]}),
    ("骑乘体位", r"straddling|astride", {"must": ["bedroom", "hotel", "love-hotel", "car", "fantasy-void", "dungeon", "outdoor", "office", "classroom", "library", "bath"]}),
    ("后入体位", r"entered from behind|hips presented", {"must": ["bedroom", "hotel", "love-hotel", "car", "fantasy-void", "dungeon", "outdoor", "office", "classroom", "library", "bath"]}),
    ("口交体位", r"lips wrapped around the shaft|lips near the shaft|accepting the shaft", {"must": ["bedroom", "hotel", "love-hotel", "car", "fantasy-void", "dungeon", "office", "classroom", "library", "bath", "outdoor"]}),
    ("跑步动作", r"mid-run|slow jog|stride open", {"must": ["gym", "street", "travel", "special", "snow", "beach", "camp", "flower-field"]}),
    ("瑜伽动作", r"forward fold|slow stretch with the arms", {"must": ["gym", "home", "ballet", "dance-studio", "beach", "travel"]}),
    ("窗沿姿态", r"seated on the sill|kneeling on the sill", {"must": ["window", "home", "hotel", "kitchen", "bath"]}),
    ("对镜姿态", r"facing the mirror", {"must": ["mirror", "home", "hotel", "bedroom", "bath", "office"]}),
    ("床上躺姿", r"lying (on her side|back|face-down)|reclined with the head", {"must": ["bed", "bedroom", "home", "hotel", "love-hotel", "bath", "outdoor", "beach", "sofa"]}),
]

WARDROBE_RULES = [
    ("滑冰裙", "skate-dress", {"must": ["ice-rink"]}),
    ("婚纱礼服", "bridal|cocktail", {"must": ["wedding", "theatre", "studio-paper", "travel", "garden_cn", "pavilion"]}),
    ("新中式", "guofeng", {"must": ["pavilion", "flower-field", "travel", "studio-paper", "street", "garden_cn"]}),
    ("制服工作装", "uniform", {"must": ["work", "street", "studio-paper"]}),
    ("内衣套装", "lingerie", {"must": ["hotel", "love-hotel", "bedroom", "dungeon", "fantasy-void", "bath", "office", "classroom", "library", "onsen", "outdoor", "car"]}),
    ("裸身", "nude", {"must": ["bath", "bedroom", "hotel", "love-hotel", "onsen", "dungeon", "fantasy-void", "outdoor", "car", "library", "office"]}),
    ("浴巾裹", "towel", {"must": ["bath", "bathroom", "hotel", "onsen", "bedroom", "home"]}),
    ("泳装", "swim", {"must": ["beach", "gym", "special", "travel"]}),
]

issues: list[str] = []
for key, v in data["items"].items():
    d = v["dims"]
    scene = d["scene"]
    pose = d["pose"]
    wc = d["wardrobe"]
    for name, pat, rule in POSE_RULES:
        if re.search(pat, pose) and scene not in rule["must"]:
            issues.append(f"{key} ({v['label']}): {name} pose 但 scene={scene}")
    for name, pat, rule in WARDROBE_RULES:
        if re.search(pat, wc) and scene not in rule["must"]:
            issues.append(f"{key} ({v['label']}): {name} wardrobe 但 scene={scene}")

print(f"跨维度矛盾: {len(issues)} 条")
for i in issues:
    print("  " + i)
