# -*- coding: utf-8 -*-
"""一次性审计：label 主题词 → prompt 英文锚的覆盖率（量化主题脱节规模）。只读。"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("bcg", ROOT / "scripts" / "build_combo_gallery.py")
bcg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bcg)

combos = {}
for skill, const in (("figure", "FIGURE"), ("youth", "YOUTH"), ("erotic", "EROTIC")):
    for c in bcg.parse_combos(bcg.grab_const((ROOT / "assets" / "director-catalog.js").read_text(encoding="utf-8"), const)):
        combos[f"{skill}:{c['id']}"] = c

data = json.loads((ROOT / "scripts" / "combo-prompts.json").read_text(encoding="utf-8"))

# 主题锚表：中文主题词 → prompt 中应当出现的英文词（含词形变化）
ANCHORS = [
    ("酒店", [r"hotel"]),
    ("温泉", [r"onsen"]),
    ("浴", [r"bath", r"shower"]),
    ("床", [r"bed"]),
    ("窗", [r"window", r"sill", r"curtain"]),
    ("镜", [r"mirror"]),
    ("沙发", [r"sofa", r"couch"]),
    ("咖啡", [r"coffee", r"cafe"]),
    ("厨房", [r"kitchen"]),
    ("阳台", [r"balcony"]),
    ("车震|车内|车窗|车厢|汽车", [r"car"]),
    ("教室", [r"classroom"]),
    ("图书馆|图书|书库", [r"library", r"bookshelf", r"shelf"]),
    ("办公室|职场|办公", [r"office"]),
    ("海滩|海边|海岛", [r"beach", r"seaside", r"coast"]),
    ("瑜伽", [r"yoga"]),
    ("芭蕾", [r"ballet", r"barre"]),
    ("滑雪", [r"ski"]),
    ("冲浪", [r"surf"]),
    ("拳", [r"boxing"]),
    ("跑", [r"run"]),
    ("婚礼|婚纱|新娘", [r"wedding", r"bridal", r"bride"]),
    ("国风|古风|亭台|汉服", [r"pavilion", r"hanfu", r"qipao"]),
    ("花海|花田|花园", [r"flower", r"garden", r"bloom"]),
    ("露营", [r"camp"]),
    ("网球", [r"tennis"]),
    ("滑雪场|雪场", [r"ski", r"snow"]),
    ("温泉|雪女", [r"onsen", r"snow", r"yuki"]),
    ("教室|课堂", [r"classroom", r"lecture"]),
    ("地铁", [r"metro", r"subway", r"train"]),
    ("通勤", [r"street", r"commute", r"workplace", r"sidewalk", r"crosswalk", r"overpass"]),
    ("山地车|mtb", [r"bike", r"mtb", r"trail"]),
    ("自行车|bike", [r"bike", r"bicycle", r"campus"]),
    ("街拍|街|马路", [r"street", r"sidewalk", r"crosswalk"]),
    ("健身房|健身|gym", [r"gym", r"track", r"climbing", r"boxing", r"barbell"]),
    ("泳池|游泳", [r"pool", r"swim"]),
    ("雨", [r"rain"]),
    ("霓虹", [r"neon"]),
    ("屋顶|天台", [r"rooftop"]),
    ("水下|潜水", [r"underwater"]),
    ("机库|飞机", [r"hangar", r"plane"]),
    ("工地", [r"construction", r"site"]),
    ("医院|医护", [r"medical", r"hospital", r"clinic"]),
    ("实验室|lab", [r"lab"]),
    ("剧院|舞台|剧场", [r"theatre", r"stage", r"theater"]),
    ("拳台|擂台", [r"ring"]),
    ("停车场", [r"parking"]),
    ("胡同|小巷|弄堂", [r"alley", r"hutong"]),
    ("外滩", [r"bund"]),
    # 2026-09-09 根治扩展：季节/地点/技术风格/道具/妆发/体位/主体类主题
    ("大头贴|拍贴|四宫格", [r"purikura", r"photo booth", r"four-panel", r"photo strip"]),
    ("樱花|sakura", [r"sakura", r"cherry"]),
    ("银杏|ginkgo", [r"ginkgo"]),
    ("美术馆|画廊|看展", [r"gallery"]),
    ("钢琴|piano", [r"piano"]),
    ("电竞|gaming", [r"gaming", r"rgb"]),
    ("公园", [r"park"]),
    ("机场|airport", [r"airport", r"terminal"]),
    ("影院|cinema", [r"cinema"]),
    ("洗衣|laundromat", [r"laundromat", r"washing"]),
    ("夜市", [r"night market", r"stall"]),
    ("暗黑", [r"dark", r"moody", r"low-key"]),
    ("长曝", [r"long-exposure", r"ghost"]),
    ("双重曝光", [r"double-exposure"]),
    ("CCD|数码感|ccd", [r"ccd", r"digicam"]),
    ("怀旧|颗粒", [r"retro", r"grain"]),
    ("小红书", [r"xiaohongshu"]),
    ("自拍", [r"selfie"]),
    ("首饰|珠宝", [r"jewelry"]),
    ("湿发", [r"wet hair"]),
    ("辣妹", [r"spicy"]),
    ("清纯", [r"pure youthful"]),
    ("番茄", [r"tomato"]),
    ("拍立得|instant", [r"instant"]),
    ("锁骨", [r"collarbone"]),
    ("肩带", [r"strap"]),
    ("冰美人", [r"ice queen"]),
    ("手机", [r"phone"]),
    ("凳沿|凳", [r"stool"]),
    ("蝴蝶结", [r"bow"]),
    ("微醺", [r"tipsy"]),
    ("拿铁", [r"latte"]),
    ("釉面", [r"glazed"]),
    ("蜂娘", [r"bee"]),
    ("树精|根缚", [r"dryad", r"root", r"vine"]),
    ("里番", [r"hentai"]),
    ("轮", [r"gangbang"]),
    ("3P|3p", [r"threesome"]),
    ("外射", [r"cum on body"]),
    ("透视", [r"x-ray"]),
    ("男装|男像|亚洲男|male", [r"adult east asian man", r"male companion"]),
    ("情侣|couple", [r"couple", r"beside her", r"man of twenty-five"]),
    ("闺蜜|gm-", [r"two adult east asian women", r"friendship"]),
    ("双人|duo", [r"beside her", r"duo"]),
    ("宠物|pet", [r"pet", r"dog"]),
    ("门框|探身", [r"doorway"]),
    ("低头抬眼", [r"chin down"]),
    ("龟颈", [r"turtle", r"asymmetry"]),
    ("背影", [r"back view"]),
]

bad, ok, total = [], 0, 0
for key, v in data["items"].items():
    c = combos[key]
    label = c["label"]
    prompt = (v["prompt"] or "").lower()
    misses = []
    for cn, ens in ANCHORS:
        if re.search(cn, label) and not any(re.search(e, prompt) for e in ens):
            misses.append(f"{cn}→{ens[0]}")
    total += 1
    if misses:
        bad.append((key, label, misses))
    else:
        ok += 1

print(f"共 {total} 条：主题锚缺失 {len(bad)} 条 / 通过 {ok} 条")
print()
for key, label, misses in bad:
    print(f"  {key} | {label}")
    print(f"      缺失锚: {', '.join(misses)}")
