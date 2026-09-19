# -*- coding: utf-8 -*-
"""
把 Figure/Youth/Erotic 的多 section 收成「侧栏一点技能 + 栏内 Tab 切换」。
侧栏只保留技能入口，不再竖向平铺子页。
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"


def extract_section(html: str, section_id: str) -> tuple[str, str, str]:
    """Return (before, section_html_including_tags, after)."""
    pat = re.compile(
        rf'(<section\s+id="{re.escape(section_id)}"[^>]*>)(.*?)(</section>)',
        re.S,
    )
    m = pat.search(html)
    if not m:
        raise SystemExit(f"section not found: {section_id}")
    full = m.group(0)
    return html[: m.start()], full, html[m.end() :]


def strip_outer_section(section_html: str) -> tuple[str, str]:
    """Return (inner_html, first_h2_text_or_empty)."""
    m = re.match(r"<section[^>]*>(.*)</section>\s*$", section_html, re.S)
    if not m:
        return section_html, ""
    inner = m.group(1).strip()
    hm = re.search(r"<h2[^>]*>(.*?)</h2>", inner, re.S)
    title = re.sub(r"<[^>]+>", "", hm.group(1)).strip() if hm else ""
    # remove the first h2 from panel body (shell has title)
    if hm:
        inner = inner[: hm.start()] + inner[hm.end() :]
        inner = inner.strip()
    return inner, title


def make_shell(
    skill: str,
    shell_id: str,
    title_html: str,
    accent: str,
    tabs: list[tuple[str, str, str]],
) -> str:
    """tabs: (panel_id, tab_label, panel_inner_html)"""
    tab_btns = []
    panels = []
    for i, (pid, label, body) in enumerate(tabs):
        on = " active" if i == 0 else ""
        tab_btns.append(
            f'          <button type="button" class="skill-tab{on}" data-skill-tab="{pid}">{label}</button>'
        )
        panels.append(
            f'        <div class="skill-panel{on}" data-skill-panel="{pid}" id="{pid}">\n'
            f"{body}\n"
            f"        </div>"
        )
    return f"""
      <section id="{shell_id}" class="skill-shell skill-shell-{accent}" data-skill-shell="{skill}">
        <div class="skill-shell-head">
          <h2>{title_html}</h2>
          <div class="skill-tabs" role="tablist" aria-label="{skill} 栏目">
{chr(10).join(tab_btns)}
          </div>
        </div>
{chr(10).join(panels)}
      </section>
"""


def main() -> int:
    html = HTML.read_text(encoding="utf-8")

    # --- Sidebar: collapse skill sublinks ---
    new_nav = """      <nav>
        <div class="nav-group">
          <h2>总览</h2>
          <a href="#intro" data-nav="page">首页</a>
          <a href="#director" data-nav="page">🎬 导演台</a>
          <a href="#rules" data-nav="page">写法规则</a>
          <a href="#compare" data-nav="page">对比</a>
          <a href="#router" data-nav="page">路由</a>
          <a href="#shared" data-nav="page">共同机制</a>
        </div>
        <div class="nav-group">
          <h2>三大 Skill</h2>
          <a class="sfw-link" href="#skill-figure" data-nav="skill" data-skill="figure">📷 Figure SFW</a>
          <a class="youth-link" href="#skill-youth" data-nav="skill" data-skill="youth">✨ Youth 纯欲</a>
          <a class="nsfw-link" href="#skill-erotic" data-nav="skill" data-skill="erotic">🔥 Erotic NSFW</a>
        </div>
        <div class="nav-group">
          <h2>组合实例</h2>
          <a href="#combo-gallery" data-nav="page">🖼 全量组合图库</a>
        </div>
        <div class="nav-group">
          <h2>更多</h2>
          <a href="#output" data-nav="page">输出形态</a>
          <a href="#phrases" data-nav="page">说法模板</a>
          <a href="#faq" data-nav="page">FAQ</a>
        </div>
      </nav>"""
    html = re.sub(r"<nav>.*?</nav>", new_nav, html, count=1, flags=re.S)

    # Collect figure sections
    fig_ids = [
        "figure",
        "figure-menu",
        "figure-gallery",
        "figure-order",
        "figure-flow",
        "figure-arch",
    ]
    youth_ids = ["youth", "youth-menu", "youth-flow", "youth-gallery", "youth-order"]
    ero_ids = [
        "erotic",
        "erotic-menu",
        "erotic-flow",
        "erotic-scale",
        "nsfw-gallery",
        "erotic-order",
    ]

    def collect(ids: list[str]) -> list[tuple[str, str, str]]:
        out = []
        for sid in ids:
            if f'id="{sid}"' not in html:
                print(f"[warn] missing {sid}")
                continue
            _, sec, _ = extract_section(html, sid)
            inner, title = strip_outer_section(sec)
            # tab label
            labels = {
                "figure": "默认与用法",
                "figure-menu": "菜单全图",
                "figure-gallery": "示例图",
                "figure-order": "下单口令",
                "figure-flow": "工作流",
                "figure-arch": "架构",
                "youth": "默认与用法",
                "youth-menu": "菜单全图",
                "youth-flow": "工作流",
                "youth-gallery": "示例图",
                "youth-order": "下单口令",
                "erotic": "默认与用法",
                "erotic-menu": "菜单全图",
                "erotic-flow": "工作流",
                "erotic-scale": "尺度图表",
                "nsfw-gallery": "示例图",
                "erotic-order": "下单口令",
            }
            # For gallery panels, inject full combo gallery mount
            if sid in ("figure-gallery", "youth-gallery", "nsfw-gallery"):
                skill = (
                    "figure"
                    if sid.startswith("figure")
                    else "youth"
                    if sid.startswith("youth")
                    else "erotic"
                )
                mount = f'''
            <div class="combo-gallery-embed" data-combo-gallery="{skill}">
              <p class="lead">以下为该 Skill <strong>全部命名组合包</strong>实例图（组图映射 + 可搜可筛）。点卡片可复制组合包 ID。</p>
              <div class="cg-toolbar">
                <input type="search" class="cg-search" placeholder="搜索组合包 ID / 名称 / 分组…" />
                <select class="cg-group"><option value="all">全部分组</option></select>
                <span class="cg-count"></span>
              </div>
              <div class="cg-grid"></div>
            </div>
            <details class="more" style="margin-top:1rem">
              <summary>展开：精选大图（封面向）</summary>
              <div class="inner">
{inner}
              </div>
            </details>
'''
                inner = mount
            out.append((sid, labels.get(sid, sid), inner))
        return out

    fig_tabs = collect(fig_ids)
    youth_tabs = collect(youth_ids)
    ero_tabs = collect(ero_ids)

    fig_shell = make_shell(
        "figure",
        "skill-figure",
        'Figure · SFW <span class="pill pill-sfw">摄影</span>',
        "sfw",
        fig_tabs,
    )
    youth_shell = make_shell(
        "youth",
        "skill-youth",
        'Youth · 纯欲暗示 <span class="pill pill-youth">非露骨</span>',
        "youth",
        youth_tabs,
    )
    ero_shell = make_shell(
        "erotic",
        "skill-erotic",
        'Erotic · NSFW <span class="pill pill-nsfw">18+</span>',
        "nsfw",
        ero_tabs,
    )

    combo_gallery_page = """
      <section id="combo-gallery" class="combo-gallery-page">
        <h2>全量组合实例图库</h2>
        <p class="lead">三个 Skill 的<strong>每一个命名组合包</strong>都有实例图（按题材组映射）。导演台选包时也会显示缩略图。</p>
        <div class="cg-skill-switch" role="group">
          <button type="button" class="cg-skill-btn active" data-cg-skill="figure">Figure</button>
          <button type="button" class="cg-skill-btn" data-cg-skill="youth">Youth</button>
          <button type="button" class="cg-skill-btn" data-cg-skill="erotic">Erotic</button>
          <button type="button" class="cg-skill-btn" data-cg-skill="all">全部</button>
        </div>
        <div class="combo-gallery-embed" data-combo-gallery="figure" data-cg-main="1">
          <div class="cg-toolbar">
            <input type="search" class="cg-search" placeholder="搜索组合包 ID / 名称 / 分组…" />
            <select class="cg-group"><option value="all">全部分组</option></select>
            <span class="cg-count"></span>
          </div>
          <div class="cg-grid"></div>
        </div>
      </section>
"""

    # Remove old sections from HTML by replacing the whole span from first figure to end of erotic-order
    # Find start of <!-- FIGURE --> or <section id="figure"
    start_m = re.search(r"<!-- FIGURE -->|<section id=\"figure\"", html)
    end_m = re.search(r'<section id="output"', html)
    if not start_m or not end_m:
        raise SystemExit("figure/output anchors not found")
    # include comment if present
    start = start_m.start()
    # walk back if comment exists before figure
    comment = html.rfind("<!-- FIGURE", 0, start_m.start() + 1)
    if comment != -1 and start_m.start() - comment < 40:
        start = comment

    new_block = (
        "      <!-- SKILL SHELLS: tab 切换，勿再竖向平铺子导航 -->\n"
        + fig_shell
        + youth_shell
        + ero_shell
        + combo_gallery_page
        + "\n      "
    )
    html = html[:start] + new_block + html[end_m.start() :]

    # Ensure scripts include combo-gallery-data.js before app.js
    if "combo-gallery-data.js" not in html:
        html = html.replace(
            '<script src="assets/director-catalog.js"></script>',
            '<script src="assets/director-catalog.js"></script>\n'
            '  <script src="assets/combo-gallery-data.js"></script>',
        )
        # fallback: before app.js
        if "combo-gallery-data.js" not in html:
            html = html.replace(
                '<script src="assets/app.js"></script>',
                '<script src="assets/combo-gallery-data.js"></script>\n'
                '  <script src="assets/app.js"></script>',
            )

    # If director scripts at end, check
    if "combo-gallery-data.js" not in html:
        # append before director.js
        html = html.replace(
            '<script src="assets/director.js"></script>',
            '<script src="assets/combo-gallery-data.js"></script>\n'
            '  <script src="assets/director.js"></script>',
        )

    HTML.write_text(html, encoding="utf-8")
    print("[ok] restructured", HTML)
    print("  figure tabs", len(fig_tabs), "youth", len(youth_tabs), "erotic", len(ero_tabs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
