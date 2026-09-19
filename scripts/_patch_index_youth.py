# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "index.html"
t = p.read_text(encoding="utf-8")

if 'data-mode="youth"' in t and 'id="youth"' in t:
    print("[skip] index already has youth")
    raise SystemExit(0)

t = t.replace(
    "Skill 教学站 · figure & erotic",
    "Skill 教学站 · figure · youth · erotic",
)
t = t.replace("<p>图 · 导演台 · 写法规则</p>", "<p>三 Skill · 导演台 · 图文菜单</p>")

old_nav = """        <div class="nav-group">
          <h2>Erotic NSFW</h2>
          <a class="nsfw-link" href="#erotic">默认与用法</a>
          <a class="nsfw-link" href="#erotic-flow">工作流</a>
          <a class="nsfw-link" href="#erotic-scale">尺度图表</a>
          <a class="nsfw-link" href="#nsfw-gallery">示例图</a>
        </div>"""
new_nav = """        <div class="nav-group">
          <h2>Youth 纯欲</h2>
          <a class="youth-link" href="#youth">默认与用法</a>
          <a class="youth-link" href="#youth-menu">菜单全图</a>
          <a class="youth-link" href="#youth-flow">工作流</a>
          <a class="youth-link" href="#youth-gallery">示例图</a>
          <a class="youth-link" href="#youth-order">下单口令</a>
        </div>
        <div class="nav-group">
          <h2>Erotic NSFW</h2>
          <a class="nsfw-link" href="#erotic">默认与用法</a>
          <a class="nsfw-link" href="#erotic-flow">工作流</a>
          <a class="nsfw-link" href="#erotic-scale">尺度图表</a>
          <a class="nsfw-link" href="#nsfw-gallery">示例图</a>
        </div>"""
if old_nav not in t:
    raise SystemExit("nav not found")
t = t.replace(old_nav, new_nav, 1)

t = t.replace(
    "<h1>两个 Skill，一张图先选对路</h1>",
    "<h1>三个 Skill，一张图先选对路</h1>",
)
t = t.replace(
    "figure = SFW 摄影 · erotic = 大胆 NSFW。用<strong>导演台</strong>搜组合包、点选细节、复制四段英文；复杂精修丢回对话 skill。",
    "figure = SFW 摄影 · youth = 纯欲暗示 · erotic = 大胆 NSFW。用<strong>导演台</strong>切换三模式、搜组合包、点选细节、复制四段英文；复杂精修丢回对话 skill。",
)
t = t.replace(
    """          <div class="pills">
            <span class="pill pill-sfw">SFW 完整着装</span>
            <span class="pill pill-nsfw">NSFW 默认大胆</span>
            <span class="pill">默认东亚</span>
            <span class="pill">Krea 2 · 六/七层</span>
            <span class="pill">18+</span>
          </div>""",
    """          <div class="pills">
            <span class="pill pill-sfw">SFW 完整着装</span>
            <span class="pill pill-youth">纯欲暗示</span>
            <span class="pill pill-nsfw">NSFW 默认大胆</span>
            <span class="pill">默认东亚</span>
            <span class="pill">Krea 2 · 六/七层</span>
            <span class="pill">18+</span>
          </div>""",
)

t = t.replace(
    """              <div class="skill-switch" role="group" aria-label="选择 Skill">
                <button type="button" data-mode="figure" class="active-sfw">📷 Figure</button>
                <button type="button" data-mode="erotic">🔥 Erotic</button>
              </div>""",
    """              <div class="skill-switch" role="group" aria-label="选择 Skill">
                <button type="button" data-mode="figure" class="active-sfw">📷 Figure</button>
                <button type="button" data-mode="youth">✨ Youth</button>
                <button type="button" data-mode="erotic">🔥 Erotic</button>
              </div>""",
)

old_rules = """        <div class="grid-2">
          <article class="card sfw">
            <div class="card-body">
              <h3><span class="pill pill-sfw">Figure</span> 六层</h3>
              <p style="font-size:0.88rem;line-height:1.55;color:var(--muted)">镜头 → 动作 → 衣 → 材质 → 光 → 场<br/>
              Main <strong>80–140</strong> 词 · 全文 <strong>160–320</strong> 词<br/>
              超约 350 词先砍环境；<strong>永不砍动作与主光</strong></p>
            </div>
          </article>
          <article class="card nsfw">
            <div class="card-body">
              <h3><span class="pill pill-nsfw">Erotic</span> 七层</h3>
              <p style="font-size:0.88rem;line-height:1.55;color:var(--muted)">镜头 → 姿 → <strong>连接/暴露</strong> → 手服 → 材质 → 光 → 场<br/>
              Main <strong>85–145</strong> 词 · 全文 <strong>170–330</strong> 词<br/>
              超约 360 词先砍场；<strong>永不砍连接与主光</strong></p>
            </div>
          </article>
        </div>"""
new_rules = """        <div class="grid-3">
          <article class="card sfw">
            <div class="card-body">
              <h3><span class="pill pill-sfw">Figure</span> 六层</h3>
              <p style="font-size:0.88rem;line-height:1.55;color:var(--muted)">镜头 → 动作 → 衣 → 材质 → 光 → 场<br/>
              Main <strong>80–140</strong> 词 · 全文 <strong>160–320</strong> 词<br/>
              超约 350 词先砍环境；<strong>永不砍动作与主光</strong></p>
            </div>
          </article>
          <article class="card youth">
            <div class="card-body">
              <h3><span class="pill pill-youth">Youth</span> 七层</h3>
              <p style="font-size:0.88rem;line-height:1.55;color:var(--muted)">镜头 → 姿 → <strong>暗示焦点</strong> → 服饰 → 材质 → 光 → 场<br/>
              Main <strong>80–140</strong> 词 · 全文 <strong>160–320</strong> 词<br/>
              超约 350 词先砍场；<strong>永不砍姿/暗示/主光</strong></p>
            </div>
          </article>
          <article class="card nsfw">
            <div class="card-body">
              <h3><span class="pill pill-nsfw">Erotic</span> 七层</h3>
              <p style="font-size:0.88rem;line-height:1.55;color:var(--muted)">镜头 → 姿 → <strong>连接/暴露</strong> → 手服 → 材质 → 光 → 场<br/>
              Main <strong>85–145</strong> 词 · 全文 <strong>170–330</strong> 词<br/>
              超约 360 词先砍场；<strong>永不砍连接与主光</strong></p>
            </div>
          </article>
        </div>"""
if old_rules not in t:
    raise SystemExit("rules not found")
t = t.replace(old_rules, new_rules, 1)

t = t.replace(
    "左绿摄影，右粉色情。默认人种都是东亚成年。",
    "绿=摄影 SFW · 金=纯欲暗示 · 粉=露骨 NSFW。默认人种都是东亚成年。",
)

old_cards = """        <div class="grid-2">
          <article class="card sfw">
            <div class="card-media"><img src="assets/images/street-ootd.jpg" alt="街拍" /></div>
            <div class="card-body">
              <h3><span class="pill pill-sfw">SFW</span> figure-photo</h3>
              <p><code>/figure-photo-prompt</code></p>
            </div>
          </article>
          <article class="card nsfw">
            <div class="card-media"><img src="assets/images/nsfw-robe-hotel.jpg" alt="酒店氛围" /></div>
            <div class="card-body">
              <h3><span class="pill pill-nsfw">NSFW</span> erotic-prompt</h3>
              <p><code>/erotic-prompt</code></p>
            </div>
          </article>
        </div>
      </section>"""
new_cards = """        <div class="grid-3">
          <article class="card sfw">
            <div class="card-media"><img src="assets/images/street-ootd.jpg" alt="街拍" /></div>
            <div class="card-body">
              <h3><span class="pill pill-sfw">SFW</span> figure-photo</h3>
              <p><code>/figure-photo-prompt</code></p>
              <p class="card-note">街拍旅拍证件运动 · 姿态优先 · 禁默认私房</p>
            </div>
          </article>
          <article class="card youth">
            <div class="card-media"><img src="assets/images/ys-window-lace.jpg" alt="窗边纯欲" /></div>
            <div class="card-body">
              <h3><span class="pill pill-youth">纯欲</span> youth-seduction</h3>
              <p><code>/youth-seduction-prompt</code></p>
              <p class="card-note">独处暗示 · 窗边蕾丝 · 被观看感 · 禁止露骨</p>
            </div>
          </article>
          <article class="card nsfw">
            <div class="card-media"><img src="assets/images/nsfw-robe-hotel.jpg" alt="酒店氛围" /></div>
            <div class="card-body">
              <h3><span class="pill pill-nsfw">NSFW</span> erotic-prompt</h3>
              <p><code>/erotic-prompt</code></p>
              <p class="card-note">大胆自展 · 连接点 · 插入点名</p>
            </div>
          </article>
        </div>
      </section>"""
if old_cards not in t:
    raise SystemExit("compare cards not found")
t = t.replace(old_cards, new_cards, 1)

t = t.replace(
    """        <div class="grid-3">
          <div class="def"><span class="k">figure 核心</span><span class="v">姿态 / 重心优先</span></div>
          <div class="def"><span class="k">erotic 核心</span><span class="v">性连接点优先</span></div>
          <div class="def"><span class="k">共同铁律</span><span class="v">单帧 · 完整句 · 不灌水</span></div>
        </div>""",
    """        <div class="grid-3">
          <div class="def"><span class="k">figure 核心</span><span class="v">姿态 / 重心优先</span></div>
          <div class="def"><span class="k">youth 核心</span><span class="v">姿态 + 暗示焦点</span></div>
          <div class="def"><span class="k">erotic 核心</span><span class="v">性连接点优先</span></div>
        </div>
        <div class="defaults" style="margin-top:0.6rem">
          <div class="def"><span class="k">共同铁律</span><span class="v">单帧 · 完整句 · 不灌水 · 默认东亚 18+</span></div>
        </div>""",
)

youth_html = Path(__file__).with_name("_youth_sections.inc.html").read_text(encoding="utf-8")
erotic_mark = "      <!-- EROTIC -->"
if erotic_mark not in t:
    raise SystemExit("erotic mark not found")
t = t.replace(erotic_mark, youth_html + erotic_mark, 1)

old_ph = """      <section id="phrases">
        <h2>说法模板</h2>
        <div class="grid-2">
          <div class="example">
            <div class="example-head"><span>Figure</span><button type="button" class="copy-btn">复制</button></div>
            <pre>/figure-photo-prompt 韩系松弛街拍 early twenties 奶茶

/figure-photo-prompt 组合:小红书封面 通勤地铁

/figure-photo-prompt 居家柔美窗边 L0 针织

/figure-photo-prompt 组合:电竞房RGB 词预算全身

/figure-photo-prompt 反推这条 Civitai 元数据（SFW）</pre>
          </div>
          <div class="example">
            <div class="example-head"><span>Erotic</span><button type="button" class="copy-btn">复制</button></div>
            <pre>/erotic-prompt 大胆 日系酒店 半褪 自展

/erotic-prompt 组合:骑乘中出 女主锐

/erotic-prompt soft 一点 不要插入

/erotic-prompt 组合:钨丝酒店 .red壳

/erotic-prompt 反推这条 civitai.red 元数据</pre>
          </div>
        </div>
      </section>"""
new_ph = """      <section id="phrases">
        <h2>说法模板</h2>
        <div class="grid-3">
          <div class="example">
            <div class="example-head"><span>Figure</span><button type="button" class="copy-btn">复制</button></div>
            <pre>/figure-photo-prompt 韩系松弛街拍 early twenties 奶茶

/figure-photo-prompt 组合:小红书封面 通勤地铁

/figure-photo-prompt 居家柔美窗边 L0 针织

/figure-photo-prompt 反推这条 Civitai 元数据（SFW）</pre>
          </div>
          <div class="example">
            <div class="example-head"><span>Youth</span><button type="button" class="copy-btn">复制</button></div>
            <pre>/youth-seduction-prompt 窗边 日落逆光 过肩回眸 I3蕾丝

/youth-seduction-prompt 组合:窗纱 半眯被观看

/youth-seduction-prompt 白月光窗边 I0 清冷

/youth-seduction-prompt 是这样吗（附图）光太平了</pre>
          </div>
          <div class="example">
            <div class="example-head"><span>Erotic</span><button type="button" class="copy-btn">复制</button></div>
            <pre>/erotic-prompt 大胆 日系酒店 半褪 自展

/erotic-prompt 组合:骑乘中出 女主锐

/erotic-prompt soft 一点 不要插入

/erotic-prompt 反推这条 civitai.red 元数据</pre>
          </div>
        </div>
      </section>"""
if old_ph not in t:
    raise SystemExit("phrases not found")
t = t.replace(old_ph, new_ph, 1)

t = t.replace(
    """          <div class="zone"><span class="badge">?</span><div><div class="name">大胆≠全裸插入</div><div class="desc">E1/E2+自展；全裸/插入要点名</div></div></div>
          <div class="zone"><span class="badge">?</span><div><div class="name">同一张脸</div><div class="desc">说连续锁 + 发色脸型</div></div></div>""",
    """          <div class="zone"><span class="badge">?</span><div><div class="name">大胆≠全裸插入</div><div class="desc">E1/E2+自展；全裸/插入要点名</div></div></div>
          <div class="zone"><span class="badge">?</span><div><div class="name">纯欲不心动？</div><div class="desc">写清场+光+姿+I，别只说纯欲</div></div></div>
          <div class="zone"><span class="badge">?</span><div><div class="name">Youth vs Erotic</div><div class="desc">暗示到 I3 止；再露骨转 erotic</div></div></div>
          <div class="zone"><span class="badge">?</span><div><div class="name">同一张脸</div><div class="desc">说连续锁 + 发色脸型</div></div></div>""",
)

p.write_text(t, encoding="utf-8")
print("[ok] index.html", p, "len", len(t))
