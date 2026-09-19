# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目定位

纯静态教学站（无构建系统、无依赖、无 package.json）：为 figure-photo-prompt / youth-seduction-prompt / erotic-prompt 三个文生图提示词技能提供导演台（表单拼装提示词）· 写法规则 · 图文菜单 · 示例图。

内容边界（不要改）：Figure = SFW 完整着装；Youth = 纯欲暗示非露骨；Erotic = 显式（E0–E4）。面向 18+。

## 运行与构建

```bash
# 本地预览（任选其一；改完页面 Ctrl+F5 强刷）
python -m http.server 8765        # 浏览器打开 http://127.0.0.1:8765/
# 或直接双击 index.html

# 重新生成数据文件（在仓库根目录，按此顺序）
python scripts/gen_dimension_static.py     # → scripts/director-catalog.static.json
python scripts/build_director_catalog.py   # → assets/director-catalog.js
python scripts/build_combo_gallery.py      # → assets/combo-gallery-data.js

# 只统计不写文件（核对各 skill combo 条数）
python scripts/build_director_catalog.py --check

# 反向：从现有 assets/director-catalog.js 反推 scripts/director-catalog.static.json
python scripts/build_director_catalog.py --bootstrap-static
```

无测试、无 lint。构建脚本只用 Python 标准库（argparse/json/re/pathlib）。

## 数据流：一条生成链

源头是仓库内 `skills/` 的 SKILL.md 与 `scripts/` 的手维深库，产出浏览器直接加载的 JS：

```
skills/*/SKILL.md（「命名组合包 Combo Recipes」markdown 表）
        │  build_director_catalog.py 正则解析（--figure/--erotic/--youth 可覆盖 SKILL.md 路径）
        ▼
assets/director-catalog.js       ← combo 段自动生成，勿手改
        │  build_combo_gallery.py（按关键词命中 images/ 图池，保证每条 combo 有图）
        ▼
assets/combo-gallery-data.js     ← combo → 实例图映射，勿手改

scripts/dimension_items{,_extra,_rounds}.py（手维维度深库）
        │  gen_dimension_static.py
        ▼
scripts/director-catalog.static.json（手维；catalog 非 combo 字段的来源）
```

- 改动 `skills/` 下任何 SKILL.md 后必须重跑 catalog + gallery 两个脚本；`director-catalog.js` 头部注释标注各 skill combo 条数（FIGURE=337 / EROTIC=226 / YOUTH=111），对照 `--check` 输出确认。
- erotic 的组合包表外置在 `skills/erotic-prompt/references/combo-recipes.md`，构建脚本会一并拼入解析——改 erotic 组合包改这个文件，不是 SKILL.md。
- `assets/dim-recommend.js` 是手写的软推荐先验（「推荐叠层」提示），不在生成链内。
- `scripts/_*.py` 均为开发期一次性脚本，改站不需要它们——**例外**：`_audit_gallery_mapping.py` / `_audit_theme_anchor.py` / `_audit_dim_conflict.py` 是 `regen_combo_unique.py` 出图后自动体检的运行时依赖，删掉体检会静默跳过。

## 图库主题锚生态（2026-09-09 根治后生效，扩展 skill 必读）

组合包 → 图库实例图经过「主题锚」生成链（combo_prompts.py），核心机制：

- **三级主题匹配**（class_of）：id 英文 slug > label 中文主题词 > look/group/en 细节词，英文词边界匹配（防 ski⊂skin、run⊂runes 类子串误命中）。
- **体位锚表 POSE_ACT**：erotic 体位词（口交/骑乘/后入/颜射…）→ 动作短语，优先级高于通用姿势表 POSE_LOOK。
- **beat 锚**：en ≥4 词直接用；短语渣用 SCENE_GLOSS + BEAT_EXPAND 主题词表扩展成语义锚句。
- **DIM_FIX**：单条目强制覆盖（pose/cam/scene/scene_sent/wardrobe），实测模型不服从的条目固化在这里。

**扩展 skill 新增组合包时的必走检查链**（防「图与主题货不对板」复发）：

1. 同步 skill → 重建 catalog（`--check` 确认条数）
2. `python scripts/combo_prompts.py --gen 3 --check-stale` 查缺漏 → 生成新 json（新增条目标 pending）
3. 新增条目的 label 主题词若不在 SCENE/BEAT_EXPAND 表内，需先补表（否则场景随机、beat 无锚）——`build_all` 已内置 **gate 门禁**：主题锚六路全空（场景/体位/姿态/衣着/beat/强制/主体覆盖）的条目自动打印 `[gate]` 高危清单，维度向/随机/词预算/连续锁类为设计豁免
4. `python scripts/regen_combo_unique.py` 出图（结束后**自动跑三项体检**：映射完整性/主题锚覆盖/跨维度矛盾，问题清单打印在输出尾部）
5. 视觉验收：spawn `vision-reviewer` 抽查新图（体位类、场景锚类必查）；模型不服从的条目走 DIM_FIX 或 seed 扫描（scripts/_headshot_seed_scan.py 可参数化复用）

**主体覆盖**：默认 LOCK 是 solo 东亚女。男像/双人条目必须在 `CAST_FIX`（主体句/代词/宾语/构图填充主语四字段）登记，并配 DIM_FIX 男装/双人动作——否则男像生成女性、双人缺伴侣（2026-09-10 根治）。

## 前端结构

单页应用 `index.html`（约 1100 行）：侧栏点 Figure / Youth / Erotic 进入 skill 壳，壳内 Tab 切换，不竖向平铺。三个壳的 Tab 集合**并不相同**：Figure 6（默认与用法 · 菜单全图 · 示例图 · 下单口令 · 工作流 · 架构）、Youth 5（默认与用法 · 菜单全图 · 工作流 · 示例图 · 下单口令）、Erotic 6（默认与用法 · 菜单全图 · 工作流 · 尺度图表 · 示例图 · 下单口令）。路由是 hash：`#<shellId>?tab=<panelId>`。

script 加载顺序（有依赖，勿乱序）：

1. `director-catalog.js` → 2. `combo-gallery-data.js` → 3. `dim-recommend.js` → 4. `prose-templates.js` → 5. `lightbox.js` → 6. `director.js` → 7. `app.js`

- `assets/director.js`（导演台 v3，约 2500 行）：**表单优先，不依赖拖节点/拉线**。读 `window.DIRECTOR_CATALOG`（FIGURE/YOUTH/EROTIC + SUBJECT），一键预设 → 搜索点选命名组合包（分组折叠 + 缩略图 + 画面一句 look）→ 分组点选 → 实时英文预览（形态 A 四段散文）→ 复制英文 / 复制 `/skill` 命令；配方存 localStorage（key `skill-director-recipes-v4`）；有词数条对照目标篇幅。
- `assets/prose-templates.js`：形态 A 散文模板（`window.PROSE_TEMPLATES`），三 mode 的维度装饰器 + 段装配器；`scripts/combo_prompts.py` 与它共享同一版式铁律（JS 交互拼装 / Python 离线批量）。
- `assets/lightbox.js`：站级大图弹层（`window.Lightbox`），导演台与组合图库共用；点击放大 + 复制英文提示词 / `/skill` 命令 / 组合 ID，←/→ 切换、ESC/遮罩关闭。
- `assets/app.js`：导航、Tab 切换、hash 路由、全量组合图库渲染。
- `assets/styles.css` 管站点外壳（含 `.lb-*` lightbox 段），`assets/director.css` 管导演台。

## UI/UX 规范（2026-09-07 重构后生效，新增 UI 必须遵守）

- 字号/行高/间距/动效一律用 `:root` token：`--fs-*`（meta/xs/sm/base/md/lg/xl/hero）、`--lh-*`（tight/normal/loose）、`--sp-*`（1/2/3/4/6/8/12）、`--dur-*`/`--ease`。**禁止新增裸写 font-size/padding/gap/transition 值**；中文正文 ≥12px，正文行高 1.6。
- 交互状态必须保留：全局 `:focus-visible` 焦点环（键盘导航唯一可视指示）、`button:active` 按压反馈、输入框 focus 态、`@media (prefers-reduced-motion: reduce)` 动效降级。
- 触控目标：桌面可点元素 ≥24px，≤640px 主操作 ≥44px。
- 回归：改完 UI 跑 `node scripts/_ui_capture.mjs`（Edge headless + CDP，8766 端口），视觉验收 spawn `vision-reviewer`（model:"sonnet"）。catalog 校验 `python scripts/build_director_catalog.py --check`。

## 图片资源

`assets/images/` 被 .gitignore 排除（原始资源不入库），克隆后该目录**不存在**（不是空目录），由拉取者自行生成或替换：

- **缺图兜底**：`assets/app.js` 顶部注册了全局 `error` 捕获 + 补扫，缺图位置自动换成内联 SVG 占位图（3:4，同站内人像比例），版式不塌。**不要删这段**，否则全新克隆打开就是满屏裂图。
- 命名约定：`ys-*` = Youth · `fg-*` = Figure · `er-*` = Erotic · `nsfw-*` = Erotic 卡片图 · `hot-*` = 组合图库缩略图（674 张，主体）；另有 `hero-banner.jpg` 等 5 张页面级单图（index.html 硬编码，不在上述前缀内）。
- 映射见 `assets/combo-gallery-data.js`（每条含 `prompt`，来自 `scripts/combo-prompts.json`）
- **坑**：`build_combo_gallery.py` 依赖 `assets/images/` 图池；无图时它会把 674 条映射退化成同一个不存在的路径（`hot-*` 逐条映射全丢）。入库的 `combo-gallery-data.js` 已是正确映射，无图环境**不要**重跑这一步。
- `scripts/regen_combo_unique.py`（组合图库）+ `scripts/example_prompts.py`（页面级示例图）是本机出图工具，导入时 `import comfy_api`，位置由环境变量 `DIRECTOR_PRODUCE_PATH` 指定（未设则回退 `~/.claude/skills/director-produce`）；出图走本机 ComfyUI 用户库「导演/导出行图.json」的脚本副本 `scripts/templates/krea2-image-api.json`（Moody-Krea-Mix 蒸馏，不挂 LoRA）。异地拿到后不可运行；旧批次图备份在 `assets/images/backup-*/`。
- `scripts/combo_prompts.py` **只依赖标准库、可独立运行**，是提示词与图库的一致性来源，不依赖 ComfyUI。

## 权威文档

- `docs/公共维度schema-L1L2L3.md`：维度体系权威。总公式 `Skill = 公共树(L1→L2→L3→L4→L5) + 该 Skill 专属`；L1 十二维 subject · cast · hair · makeup · expr · cloth · pose · prop · set · cam · light · grade；专属 Figure=`zone`、Youth=`I级/暗示/壳`、Erotic=`E0–E4/连接/幻想`。
- `docs/维度点菜策略-逐层分析.md`：逐层点菜策略。

## 与技能的关系

仓库内 `skills/` 是三个技能的完整快照（SKILL.md + references/），是 catalog 构建的源头，README 要求「对齐最新 skill」——若技能在仓库外更新，先同步到 `skills/` 再重建 catalog。教学站负责拼装与教学预览；完整润色与出片走对话内 `/figure-photo-prompt` `/youth-seduction-prompt` `/erotic-prompt` 斜杠命令。
