# UI/UX 重构计划（全维度：字体 · 间距 · 对比度 · 交互状态 · 动效 · 触控 · 可用性）

> 状态：**已执行**（2026-09-07 当日完成全部 10 阶段；执行记录见文末「执行记录」节）
> 范围：`assets/styles.css`、`assets/director.css`、`index.html`（阶段 0–7 纯 CSS；阶段 8 为已批准的 JS 级可用性改进，仅限 director.js 指定函数 + index.html 两处属性）
> 红线：**阶段 0–7 不碰 JS**；阶段 8 只许改第八节列明的函数，不改类名/ID/data-* 属性、不动生成链
> 规范依据：WCAG 2.2 / Nielsen 十启发式 / Ant Design·有赞·Pixso 中文规范 / 8pt 间距体系（链接见文末）

---

## 一、现状诊断（2026-09-07 实测，按维度）

### 1. 字体（详见旧版结论，摘录）
- body 基字号 15px；面板正文普遍 12.3–13.2px；约 15 处文字 9.3–10.2px，低于中文 12px 下限
- 93 处 `font-size`、约 28 种值、无 token
- 行高多处 1.25–1.4，低于中文推荐 1.5–1.8

### 2. 色彩与对比度
- `--dim #667087` 在 `--bg #0b0d12` 上约 **3.9:1**，不达 WCAG AA 4.5:1；`--muted` 7.9:1 达标
- 三种技能色（sfw 绿/youth 黄/nsfw 粉）除颜色外有文字区分，未单独依赖颜色——**合格**，保持
- 链接蓝 `#6ea8ff` 与正文有颜色区分但无下划线（hover 才出），非下划线链接需与周围文本 ≥3:1——**待阶段 0 实测**

### 3. 间距系统
- 无 token；存在大量非 4px 倍数的零散值：`0.4rem`(6.4px)、`0.45rem`(7.2px)、`0.65rem`(10.4px)、`0.85rem`(13.6px) 等 padding/gap
- 内层与外层间距层级无统一规则（规范要求：外层容器间距 > 内层元素间距，且同关系同间距）

### 4. 交互状态（重灾区）
| 状态 | 现状 | 规范要求 |
|---|---|---|
| hover | 导航/tab/卡片/按钮有 | ✓ |
| **focus / focus-visible** | **全站零定义**（CSS 中 `:focus`/`outline` 零匹配） | 焦点环 2–3px、与相邻色 ≥3:1、键盘导航唯一可视指示（WCAG 2.4.7）|
| active（按压） | 无按压反馈 | 按压应区别于 hover（scale 0.97–0.98 或加深，100–150ms）|
| disabled | 无统一定义（现多用 `hidden` 属性隐藏） | 降透明度 + `cursor: not-allowed` |
| 输入框 focus | 未定义 | 边框变色 + ring |
| 错误/成功 | toast 有，无 aria-live 声明（待阶段 0 确认） | 错误就近显示 + `aria-invalid`/`aria-live` |

### 5. 动效
- 全站仅 4 处（面板 fade 0.18s、卡片 hover 0.15s、侧栏抽屉 0.2s、导演台按钮 0.12s），时长合理
- **无 `@media (prefers-reduced-motion)` 降级**
- easing 全部默认 `ease`，无统一 token

### 6. 触控目标（WCAG 2.5.5 AAA 44px / 2.5.8 AA 24px）
- 多个控件低于 24px 下限：`.copy-btn`（约 19px 高）、`.pill`（约 21px）、`.step .n` 26px 临界、`.shot-nav` 按钮（约 16px+）
- 站点桌面为主、移动端有抽屉导航——策略：**桌面工具层 ≥24px，移动端（≤640px）关键操作 ≥44px**（用 padding 扩热区或 `::after` 扩大命中区，不牺牲视觉密度）

### 7. 可用性启发式走查（Nielsen 十原则抽查，映射本站）
| # | 原则 | 本站问题 | 处理 |
|---|---|---|---|
| 1 | 系统状态可见 | 复制/保存有 toast ✓ | 补 `aria-live`（纯 HTML 属性，可做）|
| 3 | 用户控制与自由（撤销） | **删除配方无确认直接删**；导入直接覆盖 | 需 JS → 第八节 |
| 4 | 一致性与标准 | 字号/间距碎片化（本计划主体） | 阶段 1–3 |
| 5 | 错误预防 | 同上删除/导入；一键 4 镜会覆盖分镜 | 需 JS → 第八节 |
| 6 | 识别而非回忆 | 图标按钮若无文字标签需补（阶段 0 确认 `.shot-nav` 按钮内容） | 诊断项 |
| 8 | 简洁 | 导演台信息密度高但属工具属性，合理 | 保持 |
| 9 | 错误诊断 | 导入非法 JSON 的提示文案待确认 | 诊断项/第八节 |

### 8. 可访问性总评
- 已达标：语义按钮/select/textarea、深色主题、`lang` 属性（待确认）、缩放 200% 用 rem 相对单位（待回归验证）
- 缺失：焦点可见性（最严重）、reduced-motion、触控目标、小字号、`--dim` 对比度

## 二、设计规范与 Token 方案

### 字体 token（`styles.css` `:root` 新增，8 级）
```css
--fs-meta: 0.75rem;    /* 12px mono id/计数 */
--fs-xs:   0.8125rem;  /* 13px 工具层辅助 */
--fs-sm:   0.875rem;   /* 14px 工具层正文 */
--fs-base: 1rem;       /* 16px 阅读层正文 */
--fs-md:   1.125rem;   /* 18px 强调正文 */
--fs-lg:   1.25rem;    /* 20px 面板标题 */
--fs-xl:   1.5rem;     /* 24px 章节标题 */
--fs-hero: clamp(1.625rem, 1.2rem + 1.5vw, 1.875rem);
--lh-tight: 1.35;  --lh-normal: 1.6;  --lh-loose: 1.75;
```
迁移映射表与旧版一致（0.62–0.68→meta、0.70–0.75→xs、工具层 0.78–0.88→sm、阅读层→base、0.90–0.98→md、1.05–1.25→lg、1.4→xl、1.55→hero）。全站中文 ≥12px；行高 1.25→1.35/1.6/1.75 分档。

### 间距 token（4px 基准，收敛现散值）
```css
--sp-1: 4px;  --sp-2: 8px;  --sp-3: 12px;  --sp-4: 16px;
--sp-6: 24px; --sp-8: 32px; --sp-12: 48px;
```
映射原则：内层元素间距 ≤ 容器 padding < 区块间距；同关系同值。执行时对 93+ 处 padding/gap/margin 逐一定档（如 `0.4rem→--sp-2`、`0.65rem→--sp-2/--sp-3` 按上下文、`0.85rem 0.95rem→--sp-3 --sp-4`），**阶段 1 先映射为最接近的 4px 倍数值（视觉微调 ≤±1px），阶段 3 再按层级规则归位**。

### 交互状态 token
```css
--focus-ring: 2px solid var(--blue);  --focus-offset: 2px;  /* 与深底对比 ≥3:1 */
--dur-fast: 120ms;  --dur-base: 180ms;  --ease: cubic-bezier(.2,.6,.3,1);
```
全局基线：
```css
:focus-visible { outline: var(--focus-ring); outline-offset: var(--focus-offset); }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation: none !important; transition: none !important; } }
button:active:not(:disabled) { transform: scale(.97); }
button:disabled, [aria-disabled="true"] { opacity: .5; cursor: not-allowed; pointer-events: none; }
input:focus, select:focus, textarea:focus { border-color: var(--blue); box-shadow: 0 0 0 2px var(--blue-soft); }
```

### 触控目标策略
- 桌面/工具层：所有可点元素 ≥24px（WCAG 2.5.8 AA）
- ≤640px：主操作按钮（复制、预设、保存配方等）≥44px
- 小控件（copy-btn、pill、chip ×）用透明 padding 扩热区，视觉不变

## 三、分阶段实施（每阶段独立 commit、独立回归、独立回滚）

| 阶段 | 内容 | 回归项 |
|---|---|---|
| **0 基线+诊断补全** | `git tag pre-ui-refactor`；跑全回归记录基线；确认遗留诊断项（`.shot-nav` 按钮内容、`lang` 属性、导入失败提示、toast aria-live、链接对比度实测） | A–I 全量基线 |
| **1 Token 化（行为不变）** | 字体/间距/动效 token 入 `:root`；93 处 font-size + 93+ 处 padding/gap 映射到 token，**值等于现值**（间距取最接近 4px 倍数，≤±1px）；`#dirToast` 内联样式抽入 CSS；不动字号、不动 `--dim` | A+B+C 必须与基线零差异 |
| **2 字号/行高/对比度上调** | 按迁移表上调字号；行高分档；`--dim→#7c879c`（5.3:1） | A+B+C+D |
| **3 密度修复+间距归位** | 修裁切（`.step` 88px、`.card-media` 130px、`.cg-label` 截断、`.shot-tags`、侧栏 250px、按钮组换行、表格小屏）；间距按层级规则归位 | C |
| **4 交互状态补全** | 全局 `:focus-visible` 焦点环；`:active` 按压；`:disabled` 统一定义；输入框 focus 态；卡片/按钮 hover 与 active 分离 | F+I（重点新增）|
| **5 动效规范** | 动效 token 化；`prefers-reduced-motion` 全局降级 | G |
| **6 触控目标** | 小控件扩热区至 ≥24px；≤640px 关键按钮 ≥44px；相邻目标间距 ≥8px | H |
| **7 流体+响应式** | 标题 clamp；断点复核；200% 缩放验证 | C+E |
| **8 JS 级可用性改进（已批准）** | 第八节五项：删除/覆盖 confirm、导入错误提示、toast aria-live、`.shot-nav` aria-label | B19–B22+F3 |
| **9 终验收尾** | CLAUDE.md 追加「字号/间距/动效一律用 token，新增 UI 不得裸写 font-size/padding；必须保留 :focus-visible 与 reduced-motion 降级」；`build_director_catalog.py --check` 兜底；本文档状态更新为「已执行」 | A–I 全量终验 |

## 四、红线约束
1. 阶段 0–7 不修改任何 JS；不改 `id`/类名/`data-skill-*`/按钮 `type`；不动 `hidden` 属性逻辑。阶段 8 仅允许改 director.js 的 `deleteRecipe` / `varyShots` / `importRecipe` / `toast` 四个函数与 index.html 的 `#dirToast`、`.shot-nav` 按钮属性，其他 JS 一律不动。
2. 不重跑生成脚本、不动 `skills/`/`scripts/`/`assets/images/`/三个生成 JS。
3. `hidden` 属性与 `.active`/`.show` 类名是 JS 的显隐机制，CSS 只改视觉、不改显示逻辑。
4. 每个 token 都先入 `:root` 再被引用，禁止阶段 1 后新增裸值。

## 五、功能清单（回归覆盖对象）
单页应用：侧栏 Figure / Youth / Erotic 三壳（hash `#<shellId>?tab=<panelId>`）；壳内 Tab：默认与用法 · 菜单全图 · 示例图 · 工作流 · 下单口令（figure 另有架构、erotic 另有暴露级）；章节 intro/director/rules/compare/router/shared/output/phrases/faq/combo-gallery。
导演台：mode 切换、一键预设、组合包搜索点选（缩略图）、分组点选、实时英文预览、中文对照、chips、复制英文、复制 `/skill` 命令、词数条、推荐面板（应用/换一版/不用）、Shot 管理（空 Shot/复制当前/一键 4 镜/分镜序列）、随机当前镜、恢复默认、配方 CRUD（localStorage `skill-director-recipes-v4`）、配方导出/导入 JSON。
组合图库：三 skill 切换、搜索、分组筛选、计数、点卡复制。

## 六、回归测试清单（全绿才验收）

### A. 加载链与数据
| # | 操作 | 预期 |
|---|---|---|
| A1 | 打开页面看 Console | 无报错/404；`DIRECTOR_CATALOG` 等全局可读 |
| A2 | script 顺序 | catalog → combo-gallery → dim-recommend → director → app |
| A3 | 三壳依次进入 | 正常渲染 |
| A4 | 组合图库 | 网格渲染、计数非零 |
| A5 | （阶段 7）`--check` | combo 条数与头注释一致（337/226/111） |

### B. 功能回归（22 项，字号无关也必须零影响）
B1 hash 直达三壳×各面板 · B2 刷新保持 · B3 前进/后退 · B4 Tab 逐个切换（6/5/6 面板）· B5 一键预设×3 mode · B6 组合包搜索点选 · B7 分组点选（单选互斥/多选累积）+预览实时 · B8 复制英文/复制命令+toast · B9 词数条与实际词数一致 · B10 推荐面板三按钮 · B11 Shot 增删复制/一键 4 镜/切换（阶段 8 后：覆盖前有确认，取消不覆盖）· B12 随机/恢复默认 · B13 配方保存→刷新→加载/导出/导入往返（阶段 8 后：删除有确认、取消不删；导入覆盖有确认；导入非法 JSON 有明确错误 toast）· B14 图库搜索/筛选/计数/点卡复制 · B15 router 决策器 · B16 details 折叠+copy-btn · B17 ≤1100px 抽屉开合 · B18 localStorage 清空后不崩 · B19 confirm 弹窗的「取消」路径均不产生任何副作用 · B20 一键 4 镜在空态/有内容两种情况下提示逻辑正确 · B21 导入同一文件两次，第二次覆盖确认生效 · B22 `#dirToast` 有 `role="status" aria-live="polite"` 且文案可被读屏播报

### C. 视觉回归（11 项）
C1 三壳默认面板无裁切 · C2 侧栏 250px 导航不溢出 · C3 `.step` 88px 不溢出 · C4 卡片图 130px+正文 · C5 `.cg-label` 2 行截断正常 · C6 `.shot-tags` 2.6em · C7 预览 pre/chips 无横向滚动 · C8 表格小屏 · C9 按钮组换行 · C10 三档响应式（>1100/≤1100 抽屉/≤640/≤400）· C11 无被 `overflow-x:hidden` 掩盖的断裂

### D. 对比度与可读性
D1 `--dim` 新值抽查 ≥4.5:1 · D2 行高 1.6–1.75 生效 · D3 全站中文无 <12px · D4 链接与正文区分度（hover 之外也有可辨差异，如颜色对比）

### E. 缩放回归（WCAG 1.4.4）
E1 150%/200% 下 A/B 主路径无丢失 · E2 系统字体缩放 · E3 200% 图库网格重排

### F. 键盘回归（新增，阶段 4 核心）
| # | 操作 | 预期 |
|---|---|---|
| F1 | 纯键盘 Tab 走全站（三壳、导演台、图库、FAQ） | **每个可交互元素有可见焦点环**（2px、与相邻色 ≥3:1）|
| F2 | 鼠标点击任意元素后 | 不出现焦点环（focus-visible 行为）|
| F3 | Enter/Space 触发按钮、details、select、textarea | 全部可操作；toast 可被读屏播报（若阶段 0 已补 aria-live）|
| F4 | 焦点顺序 | 视觉顺序一致，无焦点陷阱 |

### G. 动效回归（新增，阶段 5 核心）
| # | 操作 | 预期 |
|---|---|---|
| G1 | 系统开启「减弱动态效果」后浏览全站 | 面板切换/抽屉/卡片 hover 无动画无过渡，功能不变 |
| G2 | 正常模式下动效时长 | 与 `--dur-*` 一致（120–180ms），无迟滞 |
| G3 | 侧栏抽屉 0.2s 动画 | 开合流畅，不卡 |

### H. 触控回归（新增，阶段 6 核心）
| # | 操作 | 预期 |
|---|---|---|
| H1 | DevTools 触控模拟（375px）点所有控件 | 命中区 ≥24px（主操作 ≥44px），无误触 |
| H2 | 相邻目标（copy-btn 组、shot-nav、chip 组） | 间距 ≥8px 或命中区不重叠 |
| H3 | 真机抽查（可选） | 单手持机可完成「预设→点选→复制」主路径 |

### I. 状态回归（新增，阶段 4 核心）
| # | 检查 | 预期 |
|---|---|---|
| I1 | 每个按钮 hover / active / disabled 三态 | 均有且互异（按压 ≠ hover）|
| I2 | 输入框/select/textarea focus | 边框+ring 可见 |
| I3 | `.skill-tab.active`、`.cg-skill-btn.active`、选中 chip | 选中态与焦点态可同时辨识（不打架）|

## 七、执行方式
- 每阶段一个 commit（`ui: stage N …`），回滚单位 = 阶段。
- 本地 `python -m http.server 8765` + DevTools 覆盖 375/640/1100/1440 + 触控模拟 + 系统减弱动效开关。
- **视觉验收统一走 `vision-reviewer` 子代理**（用户级 `~/.claude/agents/vision-reviewer.md`，sonnet 档映射 deepseek-v4-flash-vision-exp，2026-09-07 实测读图正常）：阶段 0 基线截图、C 视觉回归逐项检查、D 对比度抽查、各阶段截图对比，均由主会话截图后 spawn 该子代理按口径判定，主会话不自行看图代替。**spawn 时须带 Agent 工具 `model: "sonnet"` 覆盖参数**（定义文件改动后同会话内旧定义被快照缓存；新会话无需）。
- 阶段 0 基线记录（截图/键盘走查结论）存 `docs/_ui-baseline/`（gitignore 或压缩入库，执行者定）。
- 全部通过后更新本文档状态为「已执行」。

## 八、JS 级改进（已批准 · 阶段 8 实施）

实现方案：原生 `confirm()`，零新依赖、零新 UI 组件、不引入 CSS 类。

1. **删除配方确认**：`deleteRecipe()` 删除前 `confirm('删除配方「<名>」？此操作不可恢复')`；取消则直接返回。
2. **一键 4 镜覆盖确认**：`varyShots()` 在已有非空分镜将被覆盖时 `confirm()`；全新/空态不弹窗。
3. **导入覆盖与错误提示**：`importRecipe(file)` 若目标名已存在先 `confirm` 覆盖；JSON 解析失败或字段缺失时 toast 明确错误文案（阶段 0 确认现状缺失后补）。
4. **toast 播报**：`index.html` `#dirToast` 加 `role="status" aria-live="polite"`。
5. **`.shot-nav` 图标按钮**：若为纯图标（阶段 0 确认内容），补 `aria-label`。

改动白名单：director.js 仅 `deleteRecipe` / `varyShots` / `importRecipe` / `toast` 四个函数；index.html 仅 `#dirToast` 与 `.shot-nav` 按钮属性。其余 JS 一律不动。

## 参考链接（检索来源）
- 字体：[Ant Design 字体规范](https://2x.ant.design/docs/spec/font-cn) · [有赞设计系统](https://design.youzan.com/visual/font.html) · [Pixso 字体技巧](https://pixso.cn/designskills/zitishejijiqiao/) · [Skyscanner Typography](https://www.skyscanner.design/latest/foundations/typography/typography/overview-QHfrAvWP) · [studioubique 2025 指南](https://www.studioubique.com/typography-in-web-design/#lets-talk)
- 间距：[uiguides · Spacing Systems](https://www.uiguides.com/guides/spacing-systems-for-ui-design) · [Incode · Spacing](https://developer.incode.com/design-and-ux/spacing/) · [Compound · Layout](https://compound.thephoenixgroup.com/latest/guidelines/foundations/layout/overview-S6gUR3JE)
- 触控目标：[W3C 2.5.5 Understanding](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced) · [CSS-Tricks 触控目标](https://css-tricks.com/looking-at-wcag-2-5-5-for-better-target-sizes/) · [govtnz 触控目标](https://govtnz.github.io/web-a11y-guidance/ka/accessible-ux-best-practices/mobile-apps/mobile-app-a11y-by-feature-type/touch-and-pointer-target-sizing.html)
- 交互状态：[Shopify Polaris · Interaction states](https://github.com/Shopify/polaris-react-archive/blob/main/polaris.shopify.com/content/design/interaction-states.mdx) · [HPE · Component states](https://design-system.hpe.design/design-tokens/component-states)
- 可用性：[Nielsen 十启发式](https://www.uxtigers.com/post/usability-heuristics-history) · [Telerik UX Crash Course](https://www.telerik.com/blogs/ux-crash-course-nielsens-usability-heuristics)
- 对比度/无障碍：[W3C G145](https://www.w3.org/WAI/WCAG22/Techniques/general/G145.html) · [govtnz 文字对比度](https://govtnz.github.io/web-a11y-guidance/ka/accessible-ux-best-practices/colour-and-contrast/design-with-colour-in-an-accessible-way/contrast-for-text-and-images-of-text.html)

---

## 执行记录（2026-09-07）

| 阶段 | commit | 结果 |
|---|---|---|
| 0 基线+诊断 | f6842e1（tag pre-ui-refactor） | 诊断补全：.shot-nav 不存在（§8.5 N/A）；链接蓝 vs 正文 2.15:1 ❌ 新发现；焦点环实为 UA auto 1px；640px 溢出为截图竞态伪影（已作废）；缩放右缘裁切为 setPageScaleFactor 伪影（已用视口收缩法重测达标） |
| 1 Token 化 | 4e02a63 | 93+ 处间距映射 4px token；vision-reviewer 11/11 无可见回归 |
| 2 字号/行高/对比度 | 473c34b | --dim→#7c879c（5.37:1）；--blue→#4f82cc（vs 正文 3.47:1）；中文 <12px 清零（余 37 处为 mono 英文 code）；.cg-id 折行回归修复 |
| 3 密度修复 | 63d1c8c | .step 88→96px；.shot-tags line-clamp；小屏表格容器滚动；5/5 通过 |
| 4 交互状态 | 79dd841 | :focus-visible 2px #4f82cc；:active scale(.97)；:disabled；输入 focus；键盘走查 40/40 |
| 5 动效规范 | ca07169 | 动效 token 化；prefers-reduced-motion 全局降级（探针实测 0s） |
| 6 触控目标 | 653e381 | 桌面 <24px 清零；640 主操作 ≥44px；间距 ≥8px |
| 7 流体+响应式 | 2f89783 | 缩放等价验证（960/720 视口重排达标）；--check 337/226/111 ✓；回归工具重构 |
| 8 JS 级改进 | d2dd611 | deleteRecipe/varyShots/importRecipe confirm + 错误文案 + toast aria-live；B19–B22 自动化实测通过 |
| 9 终验收尾 | 本记录 commit | CLAUDE.md 追加 token/交互/回归规范；全量终验 A–I |

**执行偏差说明**：
- §8.5（.shot-nav aria-label）：阶段 0 确认该元素不存在（旧诊断遗留），N/A。
- 导入覆盖确认的实现口径：现有 importRecipe 并不写入配方列表而是替换当前导演台状态，故确认文案为「覆盖当前导演台的模式与分镜」（原计划「目标名已存在」语义不适用）。
- varyShots 空态判定：picks 须与 sanitizeAllPicks 补全后的默认值比较，否则空态误弹窗（执行中发现并修复）。
- 自动化回归依赖 `scripts/_ui_capture.mjs`（Edge headless + CDP，端口 8766）；headless 限制：Input 触发的 confirm 不推 dialog 事件（盲处理）、dsf 切换会挂起后续真实导航（缩放用视口收缩等价模拟）。

**遗留人工清单**：见会话最终汇报（读屏播报、真机触控、系统减弱动效开关实测、B 清单 22 项浏览器手测、375px 触控模拟等）。
