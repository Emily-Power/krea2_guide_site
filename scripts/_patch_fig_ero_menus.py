# -*- coding: utf-8 -*-
"""Insert Figure/Erotic menu maps + galleries + order sections; update nav."""
import os
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"
# 一次性：从某次出图会话目录搬运示例图。该源目录属旧会话，已不存在；
# 需要重跑 copy_images() 时用环境变量 EXAMPLE_IMG_SRC 指向实际目录。
IMG_SRC = Path(os.environ["EXAMPLE_IMG_SRC"]) if os.environ.get("EXAMPLE_IMG_SRC") else None
IMG_DST = ROOT / "assets" / "images"

# session file -> site name (from generation order)
COPY_MAP = {
    "7.jpg": "fg-street-midstride.jpg",
    "9.jpg": "fg-metro-commute.jpg",
    "8.jpg": "fg-editorial.jpg",
    "14.jpg": "fg-yoga.jpg",
    "13.jpg": "fg-travel.jpg",
    "11.jpg": "fg-beauty.jpg",
    "12.jpg": "er-hotel-robe.jpg",
    "10.jpg": "er-window-sheer.jpg",
    "15.jpg": "er-bed-edge.jpg",
    "16.jpg": "er-neon-night.jpg",
    "17.jpg": "er-slip-sofa.jpg",
    "18.jpg": "er-bath-steam.jpg",
}


def copy_images() -> None:
    if IMG_SRC is None:
        print("[skip] 未设 EXAMPLE_IMG_SRC，跳过搬图")
        return
    for src_name, dst_name in COPY_MAP.items():
        s = IMG_SRC / src_name
        d = IMG_DST / dst_name
        if not s.is_file():
            print(f"[warn] missing {s}")
            continue
        shutil.copy2(s, d)
        print(f"[img] {src_name} -> {dst_name} ({d.stat().st_size})")


def patch_html() -> None:
    t = HTML.read_text(encoding="utf-8")
    if 'id="figure-menu"' in t and 'id="erotic-menu"' in t:
        print("[skip] html sections already present")
    else:
        # nav Figure
        old_fig_nav = """        <div class="nav-group">
          <h2>Figure SFW</h2>
          <a class="sfw-link" href="#figure">默认与用法</a>
          <a class="sfw-link" href="#figure-flow">工作流</a>
          <a class="sfw-link" href="#figure-arch">架构</a>
        </div>"""
        new_fig_nav = """        <div class="nav-group">
          <h2>Figure SFW</h2>
          <a class="sfw-link" href="#figure">默认与用法</a>
          <a class="sfw-link" href="#figure-menu">菜单全图</a>
          <a class="sfw-link" href="#figure-gallery">示例图</a>
          <a class="sfw-link" href="#figure-flow">工作流</a>
          <a class="sfw-link" href="#figure-order">下单口令</a>
          <a class="sfw-link" href="#figure-arch">架构</a>
        </div>"""
        if old_fig_nav not in t:
            raise SystemExit("figure nav not found")
        t = t.replace(old_fig_nav, new_fig_nav, 1)

        # nav Erotic
        old_ero_nav = """        <div class="nav-group">
          <h2>Erotic NSFW</h2>
          <a class="nsfw-link" href="#erotic">默认与用法</a>
          <a class="nsfw-link" href="#erotic-flow">工作流</a>
          <a class="nsfw-link" href="#erotic-scale">尺度图表</a>
          <a class="nsfw-link" href="#nsfw-gallery">示例图</a>
        </div>"""
        new_ero_nav = """        <div class="nav-group">
          <h2>Erotic NSFW</h2>
          <a class="nsfw-link" href="#erotic">默认与用法</a>
          <a class="nsfw-link" href="#erotic-menu">菜单全图</a>
          <a class="nsfw-link" href="#erotic-flow">工作流</a>
          <a class="nsfw-link" href="#erotic-scale">尺度图表</a>
          <a class="nsfw-link" href="#nsfw-gallery">示例图</a>
          <a class="nsfw-link" href="#erotic-order">下单口令</a>
        </div>"""
        if old_ero_nav not in t:
            raise SystemExit("erotic nav not found")
        t = t.replace(old_ero_nav, new_ero_nav, 1)

        # insert figure sections before figure-flow
        fig_inc = Path(__file__).with_name("_figure_sections.inc.html").read_text(
            encoding="utf-8"
        )
        mark_fig = '      <section id="figure-flow">'
        if 'id="figure-menu"' not in t:
            if mark_fig not in t:
                raise SystemExit("figure-flow mark not found")
            t = t.replace(mark_fig, fig_inc + mark_fig, 1)

        # insert erotic-menu after erotic defaults section end - before erotic-flow
        ero_inc = Path(__file__).with_name("_erotic_sections.inc.html").read_text(
            encoding="utf-8"
        )
        # split: menu before erotic-flow; order after nsfw-gallery
        # erotic_sections has both erotic-menu and erotic-order
        parts = ero_inc.split('      <section id="erotic-order">')
        menu_part = parts[0]
        order_part = '      <section id="erotic-order">' + parts[1]

        mark_ero_flow = '      <section id="erotic-flow">'
        if 'id="erotic-menu"' not in t:
            if mark_ero_flow not in t:
                raise SystemExit("erotic-flow mark not found")
            t = t.replace(mark_ero_flow, menu_part + mark_ero_flow, 1)

        # enhance nsfw-gallery with new images
        old_gal = """      <section id="nsfw-gallery">
        <h2>NSFW 示例图 <span class="pill pill-nsfw">委婉</span></h2>
        <p class="lead">氛围记忆用。露骨连接句请用 <code>/erotic-prompt</code> 写正文。</p>
        <div class="gallery-3">
          <figure class="figure"><img src="assets/images/nsfw-robe-hotel.jpg" alt="" loading="lazy" /><figcaption>酒店浴袍</figcaption></figure>
          <figure class="figure"><img src="assets/images/nsfw-slip-sofa.jpg" alt="" loading="lazy" /><figcaption>丝质裙</figcaption></figure>
          <figure class="figure"><img src="assets/images/nsfw-bath-towel.jpg" alt="" loading="lazy" /><figcaption>浴室蒸汽</figcaption></figure>
          <figure class="figure"><img src="assets/images/nsfw-stockings-shirt.jpg" alt="" loading="lazy" /><figcaption>半褪叙事</figcaption></figure>
          <figure class="figure"><img src="assets/images/nsfw-window-back.jpg" alt="" loading="lazy" /><figcaption>窗边背影</figcaption></figure>
          <figure class="figure"><img src="assets/images/nsfw-neon-reflection.jpg" alt="" loading="lazy" /><figcaption>霓虹窗</figcaption></figure>
          <figure class="figure"><img src="assets/images/nsfw-hands-sheet.jpg" alt="" loading="lazy" /><figcaption>手位</figcaption></figure>
          <figure class="figure"><img src="assets/images/nsfw-choker-detail.jpg" alt="" loading="lazy" /><figcaption>项圈局部</figcaption></figure>
          <figure class="figure"><img src="assets/images/nsfw-bed-stilllife.jpg" alt="" loading="lazy" /><figcaption>乱床静物</figcaption></figure>
        </div>
      </section>"""
        new_gal = """      <section id="nsfw-gallery">
        <h2>Erotic 示例图 <span class="pill pill-nsfw">委婉氛围</span></h2>
        <p class="lead">氛围记忆用，非露骨连接示范。正式正文请导演台或 <code>/erotic-prompt</code>。</p>
        <div class="gallery-3">
          <figure class="figure"><img src="assets/images/er-hotel-robe.jpg" alt="" loading="lazy" /><figcaption>酒店钨丝浴袍</figcaption></figure>
          <figure class="figure"><img src="assets/images/er-bed-edge.jpg" alt="" loading="lazy" /><figcaption>床沿半褪叙事</figcaption></figure>
          <figure class="figure"><img src="assets/images/er-window-sheer.jpg" alt="" loading="lazy" /><figcaption>窗纱夜色</figcaption></figure>
          <figure class="figure"><img src="assets/images/er-neon-night.jpg" alt="" loading="lazy" /><figcaption>霓虹渗窗</figcaption></figure>
          <figure class="figure"><img src="assets/images/er-bath-steam.jpg" alt="" loading="lazy" /><figcaption>浴室蒸汽</figcaption></figure>
          <figure class="figure"><img src="assets/images/er-slip-sofa.jpg" alt="" loading="lazy" /><figcaption>沙发丝质裙</figcaption></figure>
          <figure class="figure"><img src="assets/images/nsfw-stockings-shirt.jpg" alt="" loading="lazy" /><figcaption>半褪叙事（旧）</figcaption></figure>
          <figure class="figure"><img src="assets/images/nsfw-hands-sheet.jpg" alt="" loading="lazy" /><figcaption>手位静物</figcaption></figure>
          <figure class="figure"><img src="assets/images/nsfw-bed-stilllife.jpg" alt="" loading="lazy" /><figcaption>乱床静物</figcaption></figure>
        </div>
      </section>"""
        if old_gal in t:
            t = t.replace(old_gal, new_gal, 1)
        elif 'er-hotel-robe.jpg' not in t and 'id="nsfw-gallery"' in t:
            print("[warn] nsfw-gallery block mismatch, skip gallery replace")

        if 'id="erotic-order"' not in t:
            # after nsfw-gallery section
            mark_out = '      <!-- OUTPUT -->'
            if mark_out not in t:
                # try after nsfw-gallery closing - insert before output
                mark_out = '      <section id="output">'
            if mark_out not in t:
                raise SystemExit("output mark not found")
            t = t.replace(mark_out, order_part + mark_out, 1)

        HTML.write_text(t, encoding="utf-8")
        print("[ok] index.html patched")


def main() -> int:
    copy_images()
    patch_html()
    # verify
    t = HTML.read_text(encoding="utf-8")
    for sid in (
        "figure-menu",
        "figure-gallery",
        "figure-order",
        "erotic-menu",
        "erotic-order",
    ):
        assert f'id="{sid}"' in t, sid
    for name in COPY_MAP.values():
        p = IMG_DST / name
        if not p.is_file():
            print(f"[warn] image missing: {name}")
        else:
            print(f"[ok] {name}")
    print("ALL DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
