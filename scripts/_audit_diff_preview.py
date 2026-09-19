# -*- coding: utf-8 -*-
"""预演：用当前 combo_prompts 代码 build_all 与旧 json 逐条 diff。只读不写。"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("cp", ROOT / "scripts" / "combo_prompts.py")
cp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cp)

old = json.loads((ROOT / "scripts" / "combo-prompts.json").read_text(encoding="utf-8"))
gen = old["gen"]
new, report = cp.build_all(gen)

changed_prompt = []
changed_dims = []
for key in old["items"]:
    o, n = old["items"][key], new["items"][key]
    if o["prompt"] != n["prompt"]:
        changed_prompt.append(key)
    if o["dims"] != n["dims"]:
        changed_dims.append((key, o["dims"], n["dims"]))

print(f"prompt 变化 {len(changed_prompt)} 条 / dims 变化 {len(changed_dims)} 条 / 不变 {len(old['items']) - len(changed_prompt)} 条")
print()
print("=== dims 变化清单 ===")
for key, o, n in changed_dims:
    diffs = [k for k in o if o[k] != n[k]]
    print(f"  {key} ({old['items'][key]['label']})  变化维度: {diffs}")
    for k in diffs:
        print(f"      {k}: {o[k]!r} -> {n[k]!r}")
