# -*- coding: utf-8 -*-
"""
One unique still per combo in the teaching-site full gallery (Krea2 蒸馏管线版).

工作流：ComfyUI 用户库「导演/导出行图.json」的脚本副本 scripts/templates/krea2-image-api.json
（Moody-Krea-Mix-premium int8 UNET + qwen3vl_4b_bf16 CLIP + qwen_image VAE，8 步 euler_ancestral cfg1，
已旁路 LoRA 节点——角色锁纯文字）。
提示词与 seed：scripts/combo_prompts.py 确定性差异化生成，持久化于 scripts/combo-prompts.json（唯一状态文件）。

用法：
  python scripts/regen_combo_unique.py --dry-run   # 仅生成/校验 674 条提示词（不触 ComfyUI）
  python scripts/regen_combo_unique.py --backup    # 旧 hot-*.jpg 移入 assets/images/backup-<date>/ 并重置状态
  python scripts/regen_combo_unique.py --limit 5   # 试跑 5 张验工作流
  python scripts/regen_combo_unique.py             # 全量串行出图（断点续跑），结束自动重建 gallery
  python scripts/regen_combo_unique.py --only-failed   # 只重跑失败条
  python scripts/regen_combo_unique.py --bump-gen  # gen+1 全量换变体与 seed 后重出

依赖 director-produce 技能（comfy_api）+ 本机 ComfyUI。GitHub 分享版不携带 director-produce。
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import time
from datetime import date
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "images"
TEMPLATE = ROOT / "scripts" / "templates" / "krea2-image-api.json"
PROMPTS = ROOT / "scripts" / "combo-prompts.json"
OLD_LOG = ROOT / "scripts" / "combo-unique-log.json"

# director-produce 技能位置：分享版不携带该技能，用环境变量 DIRECTOR_PRODUCE_PATH 指定；
# 未设时回退到用户级技能目录 ~/.claude/skills/director-produce
SKILL_DIR = Path(
    os.environ.get("DIRECTOR_PRODUCE_PATH")
    or (Path.home() / ".claude" / "skills" / "director-produce")
)
sys.path.insert(0, str(SKILL_DIR / "scripts"))
import comfy_api as C  # noqa: E402

_spec = importlib.util.spec_from_file_location("bcg", ROOT / "scripts" / "build_combo_gallery.py")
bcg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bcg)
_spec2 = importlib.util.spec_from_file_location("cp", ROOT / "scripts" / "combo_prompts.py")
cp = importlib.util.module_from_spec(_spec2)
_spec2.loader.exec_module(cp)

ASPECT = "3:4 (Portrait Standard)"
MP = 2.5  # 3:4 × 2.5MP ≈ 1376×1856，lightbox 放大质量与出图速度的平衡；实测慢可降 1.5


def load_prompts() -> dict:
    return json.loads(PROMPTS.read_text(encoding="utf-8"))


def save_prompts(data: dict) -> None:
    PROMPTS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def png_to_jpg(src: Path, dest: Path) -> None:
    Image.open(src).convert("RGB").save(dest, quality=92, optimize=True)


def run_one(base: dict, item: dict) -> None:
    wf = json.loads(json.dumps(base))
    wf["627"]["inputs"]["text"] = item["prompt"]
    # 重试（tries>1）时种子偏移，避免随机伪影在确定性种子上复现
    wf["851"]["inputs"]["seed"] = item["seed"] + 100000 * max(0, int(item.get("tries") or 0) - 1)
    wf["732"]["inputs"]["filename_prefix"] = f"combo-unique/{item['file'][:-4]}"
    wf["857"]["inputs"]["aspect_ratio"] = ASPECT
    wf["857"]["inputs"]["megapixels"] = MP
    pid = C.submit_prompt(wf, f"combo-{item['id'][:40]}")
    # VRAM 竞争时单张可到 8 分钟+，超时给足（正常 ~30s 不受影响）
    hist = C.wait_done(pid, timeout=1200)
    imgs = C.history_images(hist)
    if not imgs:
        raise RuntimeError("no image")
    src = C.resolve_output(imgs[0][0], imgs[0][1])
    png_to_jpg(src, IMG / item["file"])


def backup_old() -> int:
    """旧 hot-*.jpg 移入 assets/images/backup-<date>/；旧状态文件改名留证；清空新状态。"""
    hot = sorted(IMG.glob("hot-*.jpg"))
    if not hot:
        print("[backup] 无旧 hot 图", flush=True)
    else:
        dest_dir = IMG / f"backup-{date.today().isoformat()}"
        if dest_dir.exists():
            print(f"[backup] 目标已存在 {dest_dir}，请先手动处理，中止", file=sys.stderr)
            return 1
        dest_dir.mkdir(parents=True, exist_ok=True)
        for p in hot:
            p.rename(dest_dir / p.name)
        print(f"[backup] {len(hot)} 张旧 hot 图 -> {dest_dir}", flush=True)
    if OLD_LOG.is_file():
        OLD_LOG.rename(ROOT / "scripts" / f"combo-unique-log.bak-{date.today().isoformat()}.json")
        print("[backup] combo-unique-log.json 改名留证", flush=True)
    if PROMPTS.is_file():
        data = load_prompts()
        for it in data["items"].values():
            it["status"] = "pending"
            it["err"] = ""
        save_prompts(data)
        print("[backup] combo-prompts.json 状态重置为 pending", flush=True)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="674 组合包独图重生成（Krea2 蒸馏管线）")
    ap.add_argument("--dry-run", action="store_true", help="仅生成提示词，不触 ComfyUI")
    ap.add_argument("--backup", action="store_true", help="旧图备份 + 状态重置后退出")
    ap.add_argument("--limit", type=int, default=0, help="最多出图 N 张（试跑用）")
    ap.add_argument("--only-failed", action="store_true", help="只重跑 failed 条")
    ap.add_argument("--bump-gen", action="store_true", help="gen+1 后全量重出")
    args = ap.parse_args()

    if args.bump_gen:
        old = load_prompts() if PROMPTS.is_file() else {"gen": 1}
        data, _ = cp.build_all(int(old.get("gen", 1)) + 1)
        save_prompts(data)
        print(f"[bump-gen] gen={data['gen']} 提示词已重生成")
        return 0

    if not PROMPTS.is_file():
        print("[info] 生成 674 条提示词（combo_prompts）…", flush=True)
        data, _ = cp.build_all(2)
        save_prompts(data)

    if args.dry_run:
        data = load_prompts()
        print(f"[dry-run] {len(data['items'])} 条提示词就绪（{PROMPTS}），未触 ComfyUI", flush=True)
        return 0

    if args.backup:
        return backup_old()

    if not TEMPLATE.is_file():
        print(f"[err] 缺少工作流副本 {TEMPLATE}（用 ComfyUI 用户库 导演/导出行图.json 生成）", file=sys.stderr)
        return 1

    data = load_prompts()
    items = list(data["items"].values())
    if args.only_failed:
        items = [it for it in items if it.get("status") == "failed"]
        print(f"[only-failed] {len(items)} 条待重试", flush=True)
    else:
        items = [it for it in items if it.get("status") != "done"]
        print(f"[queue] {len(items)} 条待出图", flush=True)
    if args.limit > 0:
        items = items[: args.limit]

    base = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    done = 0
    for i, item in enumerate(items, 1):
        key = f"{item['skill']}:{item['id']}"
        dest = IMG / item["file"]
        if dest.is_file() and dest.stat().st_size > 8000 and item.get("status") == "done":
            continue
        t0 = time.time()
        try:
            run_one(base, item)
            item["status"] = "done"
            item["tries"] = int(item.get("tries") or 0) + 1
            item["err"] = ""
            done += 1
            save_prompts(data)
            print(f"[{i}/{len(items)}] ok {item['id']} -> {item['file']} {time.time()-t0:.1f}s", flush=True)
        except Exception as e:
            item["status"] = "failed"
            item["tries"] = int(item.get("tries") or 0) + 1
            item["err"] = str(e)[:400]
            save_prompts(data)
            print(f"[{i}/{len(items)}] FAIL {item['id']}: {e}", flush=True)
            time.sleep(2)

    print("building gallery map", flush=True)
    rc = bcg.main()
    run_audits()
    print(f"finished done+{done} failed={sum(1 for it in data['items'].values() if it.get('status') == 'failed')}", flush=True)
    return rc


def run_audits() -> None:
    """出图后自动体检：映射完整性 / 主题锚覆盖 / 跨维度矛盾。问题清单打印到 stdout 供会话审查。"""
    import subprocess

    for script in ("_audit_gallery_mapping.py", "_audit_theme_anchor.py", "_audit_dim_conflict.py"):
        p = ROOT / "scripts" / script
        if not p.is_file():
            print(f"[audit:{script}] 不存在，跳过", flush=True)
            continue
        r = subprocess.run(
            [sys.executable, str(p)], capture_output=True, text=True, encoding="utf-8", timeout=300
        )
        print(f"[audit:{script}] rc={r.returncode}", flush=True)
        out = (r.stdout or "") + (r.stderr or "")
        print(out[-2500:], flush=True)


if __name__ == "__main__":
    raise SystemExit(main())
