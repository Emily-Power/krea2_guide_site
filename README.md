# Skill 教学站（krea2_guide_site）

**figure-photo-prompt** + **youth-seduction-prompt** + **erotic-prompt** 三个提示词技能的
导演台拼装 · 写法规则 · 图文菜单 · 示例图。

三个技能随仓库携带在 `skills/` 目录（SKILL.md + references + skill-commons 公共引用），
对齐最新 skill：Figure **六层** · Youth / Erotic **七层** 结构 · 目标篇幅 · 完整句 ·
Seedream 精炼 B。

## ⚠️ 内容分级（先读这一节）

- 本仓库**面向 18 岁以上成年人**，含成人向（NSFW）提示词内容；**禁止未成年**。
- 三条线的内容边界（属于设计前提，不是待修的问题）：

| 线 | 边界 | 层数 |
|----|------|------|
| **Figure** | SFW，完整着装 | 六层 |
| **Youth** | 纯欲暗示，非露骨 | 七层 |
| **Erotic** | 显式 | 七层 |

Erotic 的 **E0–E4 是暴露轴的取值范围**，实际默认落在 **E1 半褪 / E2 内衣**（未点名时不默认 E4）。

## 打开

```bash
# 任意方式起一个静态服务器（示例用 Python）
python -m http.server 8765
```

浏览器打开 http://127.0.0.1:8765/
或直接双击 `index.html`（改完请 **Ctrl+F5** 强刷）。

无需安装依赖，纯静态站，`file://` 直接打开也能用（数据全在 `.js` 里，不走 fetch）。

> 端口随意，8765 只是示例。仓库内 `scripts/_ui_capture.mjs` 等回归工具默认连 8766，
> 换端口时同步改。

## 三 Skill 路由

| Skill | 用途 | 默认尺度 |
|-------|------|----------|
| **Figure** | 街拍 / 旅拍 / 证件 / 运动 / 东亚写真 | SFW 完整着装 |
| **Youth** | 纯欲 / 独处暗示 / 被观看感 | 暗示 soft–sensual，禁露骨 |
| **Erotic** | 大胆 NSFW / 连接点 / 插入点名 | 默认 explicit · E1/E2（轴范围 E0–E4） |

## 导航与页面结构（Tab 切换）

侧栏**不竖向平铺**子栏目。结构是：

1. 侧栏点 **Figure / Youth / Erotic** 进入对应 Skill 壳
2. 壳内顶部 **Tab** 切换 —— 三个壳的 Tab 集合并不相同：

| 壳 | Tab（按页面顺序） | 个数 |
|----|------------------|------|
| **Figure** | 默认与用法 · 菜单全图 · 示例图 · 下单口令 · 工作流 · **架构** | 6 |
| **Youth** | 默认与用法 · 菜单全图 · 工作流 · 示例图 · 下单口令 | 5 |
| **Erotic** | 默认与用法 · 菜单全图 · 工作流 · **尺度图表** · 示例图 · 下单口令 | 6 |

3. **全量组合图库**：每个命名组合包都有实例图（组图映射）
4. 导演台选组合包时同步显示缩略图

「架构」是 Figure 独有的六层注意力栈图解；「尺度图表」是 Erotic 独有的 E0–E4 暴露轴对照。
路由是 hash：`#<shellId>?tab=<panelId>`。

## 导演台 v3（表单优先）

交互原则：**不依赖拖节点/拉线**。

0. **一键预设**（Figure / Youth / Erotic 各 10 套；点卡片套完整参数）
1. 切换 Figure / **Youth** / Erotic
2. **搜索并点选命名组合包**（带实例缩略图）
3. 展开分组点选姿/服/场/光
4. 右侧实时预览 → 复制英文 / 复制 `/skill` 命令
5. 可选：分镜条、配方存取、随机一镜

词数条显示约英文词数，对照 skill 目标篇幅。配方存 localStorage（key `skill-director-recipes-v4`）。

## 公共维度体系

```text
Skill = 公共 L1→L2→L3→L4…  +  专属轴
```

- **L1 十二维：** subject · cast · hair · makeup · expr · cloth · pose · prop · set · cam · light · grade
- **L2/L3/L4：** 品类与裙型/状态/鞋配等，见 `scripts/gen_dimension_static.py` → `director-catalog.static.json`
- **专属：** Figure=`zone`；Youth=`I级/暗示/壳`；Erotic=`E0–E4/连接/幻想`（E 级与衣着品类已拆分）
- **权威文档：** `docs/公共维度schema-L1L2L3.md`、`docs/维度点菜策略-逐层分析.md`

## 生成与同步组合包

组合包 catalog 由 `scripts/build_director_catalog.py` 从 **仓库内 `skills/` 的 SKILL.md**
自动生成，输出到 `assets/director-catalog.js`（**不要手改**其中的 combo 段）。

注意 Erotic 的组合包表**不在 SKILL.md 里**，而是外置在
`skills/erotic-prompt/references/combo-recipes.md`，构建脚本会一并拼进来解析。

```bash
# 重生成维度 static + 组合包 catalog（在仓库根目录）
python scripts/gen_dimension_static.py
python scripts/build_director_catalog.py
python scripts/build_director_catalog.py --check   # 只统计不写文件

# 重建组合图映射（改 catalog 后；⚠️ 见下方警告）
python scripts/build_combo_gallery.py
```

> ⚠️ **`build_combo_gallery.py` 依赖 `assets/images/` 里已有图池。** 目录里没有图时，它会把
> 全部 674 条映射退化成同一个不存在的路径（`hot-*` 逐条映射全部丢失）。仓库自带的
> `combo-gallery-data.js` **已经是正确的 674 条映射**——没图就别跑这一步；真要跑，先备份它。

| 生成 | 说明 |
|------|------|
| `FIGURE.combo` | figure 命名组合包全量（337） |
| `YOUTH.combo` | youth 命名组合包全量（111） |
| `EROTIC.combo` | erotic 命名组合包 + 出片/壳速查（226） |
| 其他字段 | `scripts/director-catalog.static.json`（手维） |

`--check` 的输出应与 `assets/director-catalog.js` 头部注释一致。另有反向开关
`--bootstrap-static`：从现有 `director-catalog.js` 反推 `director-catalog.static.json`。

## 目录

```
index.html                   # 单页应用（约 1100 行）
assets/
  styles.css / director.css  # 站点外壳 / 导演台样式
  app.js                     # 导航 · Tab · hash 路由 · 组合图库渲染 · 缺图兜底
  director.js                # 导演台 v3（约 2500 行）
  lightbox.js                # 站级大图弹层
  prose-templates.js         # 形态 A 散文模板（与 combo_prompts.py 共享版式铁律）
  dim-recommend.js           # 手写软推荐先验
  director-catalog.js        # 自动生成，勿手改 combo 段
  combo-gallery-data.js      # 组图映射，自动生成
  images/                    # 见「图片资源」（未随仓库分发时该目录不存在）
scripts/
  build_director_catalog.py  # SKILL.md + combo-recipes → catalog（核心构建）
  gen_dimension_static.py    # 维度 static
  build_combo_gallery.py     # 组合图映射
  dimension_items*.py        # 维度深库数据
  combo_prompts.py           # 图库提示词差异化生成（离线可跑，只需标准库）
  combo-prompts.json         # 图库提示词与 seed 状态文件（自动生成，1.4M）
  regen_combo_unique.py      # 本机批量出图（依赖 director-produce，分享版不可用）
  example_prompts.py         # 页面级示例图重出（同上）
  templates/krea2-image-api.json   # 出图工作流模板
  _*.py / _*.mjs             # 开发期脚本，见下
skills/                      # 三个技能快照（构建源）
  skill-commons/             # 三线公共引用（boundaries / defaults / routes）
  figure-photo-prompt/ youth-seduction-prompt/ erotic-prompt/
docs/
  公共维度schema-L1L2L3.md   # 权威
  维度点菜策略-逐层分析.md
  UIUX重构计划.md / UIUX重构-人工审核清单.md
LICENSE
```

## 与 skill 的关系

| 站内 | Skill |
|------|--------|
| 导演台 | 快速选题拼装 · 教学预览 |
| 写法规则 / 菜单地图 | 篇幅 · 层 · 点菜说明 |
| 对话 `/figure-photo-prompt` `/youth-seduction-prompt` `/erotic-prompt` | 完整润色与出片卷 |

## 图片资源

`assets/images/` **未提交进仓库**（体积大、属原始资源）。若你拿到的包里没有这个目录或目录为空：

- **站点不会裂图**：`assets/app.js` 注册了全局缺图兜底，缺图位置显示统一占位图，版式不塌；
  控制台会打印缺失张数提示。
- 图片清单与映射见 `assets/combo-gallery-data.js`（每条含 `prompt`）；
- 命名约定：

| 前缀 | 用途 | 数量 |
|------|------|------|
| `hot-*` | **组合图库缩略图**（主体） | 674 |
| `ys-*` | Youth 示例 | 6 |
| `fg-*` | Figure 示例 | 6 |
| `er-*` | Erotic 示例 | 6 |
| `nsfw-*` | Erotic 卡片图 | 5 |
| `hero-banner.jpg` 等单图 | 首页头图与各卡片 | 5 |

- 有本机 ComfyUI 环境时可用 `scripts/regen_combo_unique.py` 重建（见下一节，依赖 director-produce）。

## 本机开发脚本（分享版不可用）

`scripts/regen_combo_unique.py` + `scripts/example_prompts.py` 是**图库重生成**工具，依赖
本机 ComfyUI 与 `director-produce` 技能：

- 提示词由 `scripts/combo_prompts.py` 按 combo 差异化生成并持久化到 `scripts/combo-prompts.json`
  （该脚本**只依赖标准库，可独立运行**，是 catalog/图库的一致性来源）；
- 出图走本机 ComfyUI 用户库「导演/导出行图.json」的脚本副本
  `scripts/templates/krea2-image-api.json`（Moody-Krea-Mix 蒸馏模型，不挂 LoRA）；
- 这两个脚本在导入时 `import comfy_api`，位置由环境变量 **`DIRECTOR_PRODUCE_PATH`** 指定，
  未设时回退到 `~/.claude/skills/director-produce`。

本仓库未携带 `director-produce`，没有该环境时这两个脚本无法运行——站点浏览与 catalog 构建
不需要它们。

`scripts/_*.py` / `scripts/_*.mjs` 是开发期脚本，改站不需要它们；但注意
`_audit_gallery_mapping.py` / `_audit_theme_anchor.py` / `_audit_dim_conflict.py` 三项是
`regen_combo_unique.py` 出图结束后的自动体检依赖，删掉体检会静默跳过。

## 许可

代码与文档采用 **MIT**（见 `LICENSE`）。仓库承载的提示词内容面向 18+，含成人向内容，
禁止未成年——使用与再分发前请自行确认所在地法律允许。
