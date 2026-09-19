# -*- coding: utf-8 -*-
"""一次性：headshot-clean 的 seed 扫描（5 个变体，人工/vision 挑优后手动转 jpg）。"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

SKILL_DIR = Path(
    os.environ.get("DIRECTOR_PRODUCE_PATH")
    or (Path.home() / ".claude" / "skills" / "director-produce")
)
sys.path.insert(0, str(SKILL_DIR / "scripts"))
import comfy_api as C  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "scripts" / "templates" / "krea2-image-api.json"
data = json.loads((ROOT / "scripts" / "combo-prompts.json").read_text(encoding="utf-8"))
it = data["items"]["figure:combo-headshot-clean"]
base_seed = it["seed"]
wf_base = json.loads(TEMPLATE.read_text(encoding="utf-8"))
wf_base["627"]["inputs"]["text"] = it["prompt"]
wf_base["857"]["inputs"]["aspect_ratio"] = "3:4 (Portrait Standard)"
wf_base["857"]["inputs"]["megapixels"] = 2.5

pids = {}
for i in range(5):
    wf = json.loads(json.dumps(wf_base))
    seed = base_seed + (i + 7) * 97453
    wf["851"]["inputs"]["seed"] = seed
    wf["732"]["inputs"]["filename_prefix"] = f"combo-unique/hs-scan-{i}"
    pid = C.submit_prompt(wf, f"hs-scan-{i}")
    pids[pid] = i
    print(f"submit {i} seed={seed} pid={pid}", flush=True)

for pid, i in pids.items():
    hist = C.wait_done(pid, timeout=600)
    imgs = C.history_images(hist)
    if imgs:
        src = C.resolve_output(imgs[0][0], imgs[0][1])
        print(f"done {i} -> {src}", flush=True)
    else:
        print(f"no image {i}", flush=True)
print("ALL DONE", flush=True)
