#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 figure / erotic / youth-seduction 的 SKILL.md「命名组合包」表
1:1 生成 director-catalog.js 的 FIGURE.combo / EROTIC.combo / YOUTH.combo。

非 combo 字段（zone/pose/cloth…）来自同目录
director-catalog.static.json（手维）。

用法（在 skill-guide-site 根目录）:
  python scripts/build_director_catalog.py
  python scripts/build_director_catalog.py --check   # 只统计不写文件
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_JS = ROOT / "assets" / "director-catalog.js"
STATIC_JSON = ROOT / "scripts" / "director-catalog.static.json"

# 默认 skill 路径（可 --figure / --erotic / --youth 覆盖）：随仓库携带，见仓库根 skills/
DEFAULT_FIGURE = ROOT / "skills" / "figure-photo-prompt" / "SKILL.md"
DEFAULT_EROTIC = ROOT / "skills" / "erotic-prompt" / "SKILL.md"
DEFAULT_YOUTH = ROOT / "skills" / "youth-seduction-prompt" / "SKILL.md"
FALLBACK_FIGURE = DEFAULT_FIGURE
FALLBACK_EROTIC = DEFAULT_EROTIC
FALLBACK_YOUTH = DEFAULT_YOUTH

COMBO_SECTION_RE = re.compile(
    r"#\s*命名组合包\s*Combo Recipes.*?(?=\n#\s(?!#)|$(?!\n))",
    re.S,
)
# 追加速查小表（erotic 出片/壳/分镜）
EXTRA_COMBO_HEADINGS = (
    r"###\s*出片\s*/\s*东亚壳\s*/\s*分镜组合包",
)

# 表行：| cell | cell | ... |
ROW_RE = re.compile(r"^\|(.+)\|\s*$")
SEP_RE = re.compile(r"^\|[\s\-:|]+\|\s*$")
HEADING_RE = re.compile(r"^#{2,4}\s+(.+?)\s*$")
# ID 单元格：combo-xxx 或 **combo-xxx**
IDISH_RE = re.compile(r"combo-[a-z0-9\-\*]+", re.I)


def resolve_skill(primary: Path, fallback: Path) -> Path:
    if primary.is_file():
        return primary
    if fallback.is_file():
        return fallback
    raise FileNotFoundError(f"找不到 SKILL.md: {primary} 或 {fallback}")


def strip_md(s: str) -> str:
    s = s.strip()
    s = re.sub(r"^\*\*(.+?)\*\*$", r"\1", s)
    s = s.replace("**", "")
    s = re.sub(r"`([^`]+)`", r"\1", s)
    return s.strip()


def looks_english(s: str) -> bool:
    """\u7eaf\u82f1\u6587\u5224\u5b9a\uff1a\u62c9\u4e01\u5b57\u6bcd \u22654 \u4e14\u65e0 CJK\uff08\u6df7\u5408\u53e5\u4e0d\u518d\u89c6\u4f5c\u82f1\u6587\uff0c\u5f52\u5165 look\uff09\u3002"""
    if not s:
        return False
    latin = len(re.findall(r"[A-Za-z]", s))
    cjk = len(re.findall(r"[\u4e00-\u9fff]", s))
    return latin >= 4 and cjk == 0


def humanize_id(cid: str) -> str:
    body = re.sub(r"^combo-", "", cid, flags=re.I)
    # 常见粘连词可读化
    reps = (
        ("scurve", "s-curve"),
        ("midstride", "mid-stride"),
        ("lookbook", "lookbook"),
        ("creampie", "creampie"),
        ("doggy", "doggy"),
        ("cowgirl", "cowgirl"),
        ("deepthroat", "deepthroat"),
        ("ahegao", "ahegao"),
    )
    for a, b in reps:
        body = re.sub(rf"\b{a}\b", b, body, flags=re.I)
    body = body.replace("-", " ")
    return body.strip()


def expand_id_cell(cell: str) -> list[str]:
    """展开 `combo-a / b / c`；含 * 的索引行跳过。"""
    raw = strip_md(cell)
    if not raw:
        return []
    if "*" in raw:
        return []  # combo-cp-* 等索引行
    # 丢弃非 combo 单元格（表头）
    if not re.search(r"combo-", raw, re.I) and not re.match(
        r"^[a-z0-9][a-z0-9\-]*$", raw, re.I
    ):
        # 可能是纯中文触发列被误读——返回空
        if not re.match(r"^[a-z0-9][a-z0-9\-/ ]*$", raw, re.I):
            return []

    parts = [p.strip() for p in re.split(r"\s*/\s*", raw) if p.strip()]
    if not parts:
        return []

    out: list[str] = []
    for i, p in enumerate(parts):
        p = strip_md(p)
        if not p or "*" in p:
            continue
        if p.startswith("combo-"):
            out.append(p)
            continue
        if not out:
            # 首段不是 combo- 则补前缀
            out.append("combo-" + p if not p.startswith("combo-") else p)
            continue
        # 兄弟 ID 展开
        first = out[0]
        sibling = p
        # 短 token（jp6 / kr6 / travel8）→ 去掉 last segment
        if re.fullmatch(r"[a-z]+[0-9]+", sibling, re.I) or (
            "-" not in sibling and re.fullmatch(r"[a-z0-9]+", sibling, re.I)
        ):
            base = first.rsplit("-", 1)[0]
            out.append(f"{base}-{sibling}")
        else:
            # coquette-sfw under combo-aes-clean-girl → combo-aes-coquette-sfw
            segs = first.split("-")
            if len(segs) >= 2:
                out.append(f"combo-{segs[1]}-{sibling}")
            else:
                out.append(f"combo-{sibling}")
    # 规范化
    clean = []
    for x in out:
        x = x.lower().strip()
        if not x.startswith("combo-"):
            x = "combo-" + x
        if re.fullmatch(r"combo-[a-z0-9]+(?:-[a-z0-9]+)+", x):
            clean.append(x)
    return clean


def latin_tokens(s: str, limit: int = 14) -> str:
    toks = re.findall(r"[A-Za-z][A-Za-z0-9\-]{1,}", s or "")
    # 去重保序
    seen = set()
    out = []
    for t in toks:
        k = t.lower()
        if k in seen:
            continue
        seen.add(k)
        out.append(t)
        if len(out) >= limit:
            break
    return " ".join(out)


def build_en(cid: str, trigger: str, scene: str, prefill: str) -> str:
    """教学站拼进 prompt 的英文碎片：ID 可读化 + 预填拉丁词 + 纯英文画面句（含 CJK 的 scene 不进 en，归 look）。"""
    base = humanize_id(cid)
    parts: list[str] = [base]
    lt = latin_tokens(prefill or "")
    if lt:
        parts.append(lt)
    if scene and looks_english(scene):
        parts.append(scene)
    # 触发词若含英文也并入（如 POV、MILF、OOTD）
    lt2 = latin_tokens(trigger or "", limit=8)
    if lt2 and lt2.lower() not in base.lower():
        parts.append(lt2)
    # 去重词级
    words: list[str] = []
    seen: set[str] = set()
    for chunk in parts:
        for w in chunk.split():
            k = w.lower()
            if k in seen:
                continue
            seen.add(k)
            words.append(w)
    text = " ".join(words)
    text = re.sub(r"\s+", " ", text).strip(" ,")
    return text[:220]


def parse_combo_tables(md_text: str, skill_tag: str) -> list[dict]:
    """返回 [{id,label,en,group}, ...] 保序去重。"""
    sections: list[tuple[str, str]] = []

    m = COMBO_SECTION_RE.search(md_text)
    if m:
        sections.append(("main", m.group(0)))
    else:
        print(f"[warn] {skill_tag}: 未找到「命名组合包 Combo Recipes」节", file=sys.stderr)

    for pat in EXTRA_COMBO_HEADINGS:
        for em in re.finditer(pat + r".*?(?=\n#{1,3}\s|\Z)", md_text, re.S):
            sections.append(("extra", em.group(0)))

    items: list[dict] = []
    seen: set[str] = set()
    current_group = "组合包"

    for _sec_name, sec in sections:
        for line in sec.splitlines():
            hm = HEADING_RE.match(line)
            if hm:
                title = hm.group(1).strip()
                # 跳过顶层标题
                if "命名组合包" in title or title.startswith("组合包选择"):
                    continue
                # 去掉「详见…」与括号说明，缩短 group 标签
                title = re.split(r"[（(]\s*详见|·\s*详见", title)[0].strip()
                title = re.sub(r"[（(].*$", "", title).strip()
                title = re.sub(r"\s*[·—-]\s*优先.*$", "", title).strip()
                current_group = title[:48] if title else "组合包"
                continue

            if SEP_RE.match(line):
                continue
            rm = ROW_RE.match(line)
            if not rm:
                continue
            cells = [c.strip() for c in rm.group(1).split("|")]
            if not cells:
                continue
            # 跳过表头
            head0 = strip_md(cells[0]).lower()
            if head0 in ("id", "组合包 id", "combo", "组合包id") or head0.startswith(
                "组合包"
            ):
                if "id" in head0 or "combo" in head0:
                    continue
            if head0 in ("id",) or cells[0].strip().lower() in (
                "id",
                "**id**",
                "组合包 id",
                "**组合包 id**",
            ):
                continue
            if "触发" in strip_md(cells[0]) and len(cells) <= 2:
                continue

            id_cell = cells[0]
            if not IDISH_RE.search(id_cell) and not (
                len(cells) >= 2 and IDISH_RE.search(id_cell)
            ):
                # 有些表第一列是 **combo-x**
                if not re.search(r"combo-", id_cell, re.I):
                    continue

            ids = expand_id_cell(id_cell)
            if not ids:
                continue

            # 列语义
            # 2 列: ID | 触发
            # 3 列: ID | 触发 | 画面一句
            # 4 列: ID | 触发 | 预填 | 画面
            trigger = strip_md(cells[1]) if len(cells) > 1 else humanize_id(ids[0])
            prefill = ""
            scene = ""
            if len(cells) == 3:
                scene = strip_md(cells[2])
            elif len(cells) >= 4:
                prefill = strip_md(cells[2])
                scene = strip_md(cells[3])

            # 多 ID 同行：共用触发，label 附加短名
            for j, cid in enumerate(ids):
                if cid in seen:
                    continue
                seen.add(cid)
                if len(ids) == 1:
                    label = trigger or humanize_id(cid)
                else:
                    short = cid.replace("combo-", "")
                    # 首个用完整触发，其余用短名+触发摘要
                    if j == 0:
                        label = trigger
                    else:
                        label = f"{short} · {trigger}" if trigger else short
                    if len(label) > 36:
                        label = short
                en = build_en(cid, trigger, scene, prefill)
                items.append(
                    {
                        "id": cid,
                        "label": label[:48],
                        "en": en,
                        "group": current_group,
                        # 画面一句（中文/混合句）仅作 UI 展示；纯英文句已在 en 中
                        "look": scene if scene and not looks_english(scene) else "",
                    }
                )
    return items


def js_escape(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\r", "")
    )


def emit_o_list(items: list[dict], indent: int = 6) -> str:
    sp = " " * indent
    lines = []
    for it in items:
        lines.append(
            f'{sp}o("{js_escape(it["id"])}", "{js_escape(it["label"])}", '
            f'"{js_escape(it["en"])}", "{js_escape(it["group"])}", '
            f'"{js_escape(it.get("look") or "")}"),'
        )
    return "\n".join(lines)


def emit_static_key(key: str, items: list[dict], indent: int = 4) -> str:
    sp = " " * indent
    body = emit_o_list(items, indent + 2)
    return f"{sp}{key}: [\n{body}\n{sp}],"


def load_static() -> dict:
    if not STATIC_JSON.is_file():
        raise FileNotFoundError(
            f"缺少静态库 {STATIC_JSON}。请先运行一次并提供 director-catalog.static.json"
        )
    return json.loads(STATIC_JSON.read_text(encoding="utf-8"))


def generate_js(
    figure_combos: list[dict],
    erotic_combos: list[dict],
    youth_combos: list[dict],
    static: dict,
) -> str:
    fig = static["FIGURE"]
    ero = static["EROTIC"]
    you = static.get("YOUTH") or {}
    sub = static["SUBJECT"]

    def block(obj: dict, combo_items: list[dict], name: str) -> str:
        parts = [f"  const {name} = {{"]
        # combo 永远第一
        parts.append("    combo: [")
        parts.append(emit_o_list(combo_items, 6))
        parts.append("    ],")
        for key, items in obj.items():
            if key == "combo":
                continue
            parts.append(emit_static_key(key, items, 4))
        parts.append("  };")
        return "\n".join(parts)

    header = f"""/**
 * 导演台完整选项库
 * AUTO-GENERATED — 勿手改 combo 段
 * 生成: python scripts/build_director_catalog.py
 * FIGURE.combo = {len(figure_combos)}  ·  EROTIC.combo = {len(erotic_combos)}  ·  YOUTH.combo = {len(youth_combos)}
 * 非 combo 字段来自 scripts/director-catalog.static.json
 */
window.DIRECTOR_CATALOG = (() => {{
  const o = (id, label, en, group, look) => ({{ id, label, en, group: group || "", look: look || "" }});

"""
    footer = """
  return { FIGURE, EROTIC, YOUTH, SUBJECT, o };
})();
"""
    # SUBJECT
    sub_lines = ["  const SUBJECT = {"]
    for key, items in sub.items():
        sub_lines.append(emit_static_key(key, items, 4))
    sub_lines.append("  };")

    return (
        header
        + block(fig, figure_combos, "FIGURE")
        + "\n\n"
        + block(ero, erotic_combos, "EROTIC")
        + "\n\n"
        + block(you, youth_combos, "YOUTH")
        + "\n\n"
        + "\n".join(sub_lines)
        + footer
    )


O_CALL_RE = re.compile(
    r'o\(\s*"((?:\\.|[^"\\])*)"\s*,\s*"((?:\\.|[^"\\])*)"\s*,\s*'
    r'"((?:\\.|[^"\\])*)"\s*,\s*"((?:\\.|[^"\\])*)"\s*'
    r'(?:,\s*"((?:\\.|[^"\\])*)"\s*)?\)',
)


def _unesc_js(s: str) -> str:
    return (
        s.replace("\\n", "\n")
        .replace('\\"', '"')
        .replace("\\\\", "\\")
    )


def extract_static_from_existing_js(js_path: Path) -> dict:
    """从现有 director-catalog.js 用正则抽出非 combo 数组。"""
    text = js_path.read_text(encoding="utf-8")

    def grab_object(const_name: str) -> str:
        m = re.search(
            rf"(?:const\s+)?{const_name}\s*=\s*\{{",
            text,
        )
        if not m:
            raise ValueError(f"找不到 {const_name}")
        start = m.end() - 1
        depth = 0
        for i, ch in enumerate(text[start:], start):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return text[start : i + 1]
        raise ValueError(f"未闭合 {const_name}")

    def parse_keys(obj_src: str) -> dict[str, list[dict]]:
        # key: [ ... o(), ... ],
        result: dict[str, list[dict]] = {}
        for km in re.finditer(r"(\w+)\s*:\s*\[", obj_src):
            key = km.group(1)
            if key == "combo":
                continue
            i = km.end() - 1
            depth = 0
            for j, ch in enumerate(obj_src[i:], i):
                if ch == "[":
                    depth += 1
                elif ch == "]":
                    depth -= 1
                    if depth == 0:
                        body = obj_src[i : j + 1]
                        items = []
                        for om in O_CALL_RE.finditer(body):
                            items.append(
                                {
                                    "id": _unesc_js(om.group(1)),
                                    "label": _unesc_js(om.group(2)),
                                    "en": _unesc_js(om.group(3)),
                                    "group": _unesc_js(om.group(4)),
                                    "look": _unesc_js(om.group(5) or ""),
                                }
                            )
                        result[key] = items
                        break
        return result

    figure = parse_keys(grab_object("FIGURE"))
    erotic = parse_keys(grab_object("EROTIC"))
    subject = parse_keys(grab_object("SUBJECT"))
    out = {"FIGURE": figure, "EROTIC": erotic, "SUBJECT": subject}
    try:
        out["YOUTH"] = parse_keys(grab_object("YOUTH"))
    except ValueError:
        pass
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="SKILL 组合包 → director-catalog.js")
    ap.add_argument("--figure", type=Path, default=None)
    ap.add_argument("--erotic", type=Path, default=None)
    ap.add_argument("--youth", type=Path, default=None)
    ap.add_argument("--check", action="store_true", help="只打印统计")
    ap.add_argument(
        "--bootstrap-static",
        action="store_true",
        help="从现有 director-catalog.js 写出 static.json",
    )
    args = ap.parse_args()

    if args.bootstrap_static:
        data = extract_static_from_existing_js(OUT_JS)
        # 保留手维 YOUTH（bootstrap 若旧 catalog 无 YOUTH）
        if STATIC_JSON.is_file():
            old = json.loads(STATIC_JSON.read_text(encoding="utf-8"))
            if "YOUTH" in old and "YOUTH" not in data:
                data["YOUTH"] = old["YOUTH"]
        STATIC_JSON.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"[ok] wrote {STATIC_JSON}")
        return 0

    fig_path = resolve_skill(
        args.figure or DEFAULT_FIGURE,
        FALLBACK_FIGURE,
    )
    ero_path = resolve_skill(
        args.erotic or DEFAULT_EROTIC,
        FALLBACK_EROTIC if FALLBACK_EROTIC.is_file() else DEFAULT_EROTIC,
    )
    you_path = resolve_skill(
        args.youth or DEFAULT_YOUTH,
        FALLBACK_YOUTH if FALLBACK_YOUTH.is_file() else DEFAULT_YOUTH,
    )
    # erotic fallback: claude path only if default ok
    if not (args.erotic or DEFAULT_EROTIC).is_file() and not FALLBACK_EROTIC.is_file():
        # try agents
        alt = ROOT / "skills" / "erotic-prompt" / "SKILL.md"
        if alt.is_file():
            ero_path = alt

    print(f"[src] figure: {fig_path}")
    print(f"[src] erotic: {ero_path}")
    print(f"[src] youth:  {you_path}")

    fig_md = fig_path.read_text(encoding="utf-8")
    ero_md = ero_path.read_text(encoding="utf-8")
    # 新版 erotic SKILL.md 将「命名组合包」表外置于 references/combo-recipes.md：拼进来一起解析
    ero_recipes = ero_path.parent / "references" / "combo-recipes.md"
    if ero_recipes.is_file():
        ero_md = ero_md + "\n\n" + ero_recipes.read_text(encoding="utf-8")
    you_md = you_path.read_text(encoding="utf-8")
    figure_combos = parse_combo_tables(fig_md, "figure")
    erotic_combos = parse_combo_tables(ero_md, "erotic")
    youth_combos = parse_combo_tables(you_md, "youth")

    print(f"[combo] FIGURE: {len(figure_combos)}")
    print(f"[combo] EROTIC: {len(erotic_combos)}")
    print(f"[combo] YOUTH:  {len(youth_combos)}")

    # 分组统计
    def by_group(items):
        g: dict[str, int] = {}
        for it in items:
            g[it["group"]] = g.get(it["group"], 0) + 1
        return g

    print("[figure groups]")
    for k, v in by_group(figure_combos).items():
        print(f"  {v:4d}  {k}")
    print("[erotic groups]")
    for k, v in by_group(erotic_combos).items():
        print(f"  {v:4d}  {k}")
    print("[youth groups]")
    for k, v in by_group(youth_combos).items():
        print(f"  {v:4d}  {k}")

    # 验收闸门：en 必须纯英文；look 为 UI 展示画面句
    all_items = figure_combos + erotic_combos + youth_combos
    en_cjk = sum(1 for it in all_items if re.search(r"[一-鿿]", it["en"]))
    look_n = sum(1 for it in all_items if it.get("look"))
    print(f"[quality] en 含 CJK: {en_cjk}（预期 0） / look 填充: {look_n} / 总计 {len(all_items)}")

    if args.check:
        return 0

    if not STATIC_JSON.is_file():
        if OUT_JS.is_file():
            print("[info] bootstrap static.json from existing catalog")
            data = extract_static_from_existing_js(OUT_JS)
            STATIC_JSON.write_text(
                json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        else:
            print("[err] 无 static.json 且无现有 catalog", file=sys.stderr)
            return 1

    static = load_static()
    if "YOUTH" not in static:
        print("[err] static.json 缺少 YOUTH 字段，请先补菜单", file=sys.stderr)
        return 1
    js = generate_js(figure_combos, erotic_combos, youth_combos, static)
    OUT_JS.write_text(js, encoding="utf-8")
    print(f"[ok] wrote {OUT_JS}")
    print(
        f"     FIGURE.combo={len(figure_combos)}  EROTIC.combo={len(erotic_combos)}  "
        f"YOUTH.combo={len(youth_combos)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
