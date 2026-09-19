# 九轴全网深度补全卷（第四波 · 2026）

> **轴定义**：①发型 ②妆容 ③道具 ④衣着 ⑤姿势 ⑥场景 ⑦**镜头** ⑧**光线** ⑨**构图**  
> **检索内化（非外链墙）**：日韩发型 2025–26（水母切/韩式 2-in-1 bob/C 卷烫/air-dry layers）· Vogue K-beauty 2026 四趋势 · 小红书原生美学/千金妆/洛可可妆壳 · 人像九光位钟表法 · 焦距 24–135 语义 · 构图三分/黄金/引导线/框中框 · 全身姿校（45°/后重心/臂缝/龟颈）· 胶囊层叠衣 · 探店第三空间 · 色胶/交叉光创意。  
> **主体默认**：`adult East Asian woman` + early/mid/late twenties（全谱可叠；年龄/性别随用户）。  
> **SFW · 18+ · 禁止未成年擦边。** 私房仅用户点名 → soft-boudoir 卷。

与相邻卷分工：

| 卷 | 分工 |
|----|------|
| six-axes-web-fill-2026 | 六轴第一波深库（发/妆/道具/衣/姿/场主干） |
| shot-lens-dictionary | 景别·视角·焦距·画幅薄词典 |
| lighting-composition | 布光+构图主表 |
| asian-young-woman-p0-p2 / web-fill-2026 | 出片层 / Core 美学标签 |
| **本卷** | **九轴第四波：缺口词 + 镜头/光/构图可画句模 + 2026 妆发新壳** |

**写入纪律（强制）：**

1. Main：**发≤1 句 · 妆≤1 句 · 道具≤1 · 衣 2–4 件**；镜头+光各至少半句可指认。  
2. Composition 段：**构图工具 1 个 + 主光方向 + 情绪/质量词**。  
3. 压缩：先砍场与装饰；**永不砍 L2 姿与 L5 主光**。  
4. 全部 **adult**；校服感仅成年大学/造型向。  

---

## 0. 本波审计（相对 skill 已有）

| 轴 | 已有 | 本卷新增 |
|----|------|----------|
| 发型 | 狼尾/bob/姬/窗帘/抓夹… | **水母切 · 2-in-1 韩 bob · C 卷烫 · air-dry · 奶茶 bob · peekaboo · 成人双丸** |
| 妆容 | 韩三点/水光/抖音软… | **2026 模糊唇 · 眼下腮红羽 · 直软眉 · butter skin · soft-matte · 千金/洛可可/原生** |
| 道具 | 40+ | **叙事锚扩充 + 手位禁区再强调** |
| 衣着 | 成套配方 | **过渡季胶囊 · 风衣开合 · midi 万能 · 层叠 3 层句** |
| 姿势 | OOTD/探店细条 | **龟颈 · 腰前倾 · 双手髋后 · 近膝弯 · 美妆 35–40° 肩不对称** |
| 场景 | 第三空间表 | **书咖一体 · 屋顶停车 · 花窗廊 · 更多快配** |
| 镜头 | 薄词典 | **焦距×景别语义 · 畸变/压缩 · 可写感公式** |
| 光线 | 主表+东亚光 | **九光位钟表 · 交叉光 · 色胶三法 · 假窗硬影** |
| 构图 | 工具表 | **堆叠公式 · 人像三分眼位 · 动线留白 · 填满 vs 负空间** |

---

## 1. 发型续库（Hair · 2025–26 可画）

> 趋势内化：狼剪热度回落 → **air-dry layers / 软长层 / 韩 2-in-1**；日系 **水母切 soft jellyfish · 姬 · 奶茶 bob · peekaboo 双色**；造型 **C-curl ends · build/air perm 空气感**。  
> 规则仍：**长度 + 轮廓 + 刘海/分区 + 当帧状态** 写 2–3 维。

### 1.1 新剪型 ID

| ID | 触发 | 英文种子 |
|----|------|----------|
| **hair-jellyfish** | 水母切、jelly cut | soft jellyfish cut: rounded bob density on top, long thin flowing underlayers, airy float at mid-length |
| **hair-2in1-bob** | 韩式 2-in-1、隐藏 bob | Korean 2-in-1 cut: hidden blunt bob under long top layers; either long soft hush down OR claw-clip half-up revealing chin bob |
| **hair-2in1-down** | 2-in-1 披长 | top layers down over hidden bob, long softly layered hush silhouette |
| **hair-2in1-up** | 2-in-1 夹出 bob | upper length clipped up, revealed chin-to-shoulder blunt bob edge clean |
| **hair-c-curl-perm** | C 卷烫、韩 C | soft C-curl perm at mid-lengths to ends, root soft, ends curve under |
| **hair-airdry-layer** | 风干层、自然层 | air-dry layers, lived-in movement, minimal styling, soft crown volume |
| **hair-milk-tea-bob** | 奶茶 bob | milk-tea beige-brown blunt bob, soft elegant edge, healthy shine |
| **hair-peekaboo** | 内层挑染 peekaboo | dark top, peekaboo lighter underlayer flashes on movement — fashion adult |
| **hair-two-tone-bob** | 双色齐 bob | jet outer bob with blonde or ash under-flash on turn |
| **hair-long-flow-wave** | 长流动浪 | long soft blowout waves, face-framing layers, healthy ends |
| **hair-hush-long** | hush 长层 | long hush-cut soft layers, light face hug, quiet volume |
| **hair-hachi-bun-adult** | 成人双丸（造型点名） | two mid-high soft buns with loose face strands — adult fashion reference, never child |

### 1.2 状态补丁

| ID | 英文 |
|----|------|
| **style-c-ends** | ends in soft C-curl under, mid-lengths smooth |
| **style-s-wave-end** | gentle S-wave through lower third only |
| **style-root-lift-soft** | soft root lift, not helmet hair |
| **style-slick-wet-part** | wet-combed back from forehead, separated damp ribbons |
| **style-half-clip-2in1** | claw or pin holds top length to show under-bob |

**Main 发型金样：**
```
soft jellyfish cut, rounded top bob density with long flowing underlayers, soft curtain bangs, slight wind float
```
```
Korean 2-in-1: long hush layers down over hidden bob, soft C-curl ends, center part
```
```
claw-clip half-up revealing a clean chin-length under-bob, face wisps, adult casual chic
```

**禁：** 幼态双丸默认；荧光染色刷屏（用户点名除外）；ultra-wolf 硬塞每帧。

叠 six-axes §1 旧 ID 自由混用。

---

## 2. 妆容续库（Makeup · 2026 壳）

> **Vogue K-beauty 2026 四要点内化**：①**模糊唇 blurred lip**（圆钝唇线轻晕，比硬 ombré 更软）②**卧蚕 aegyo-sal**（强调笑时「可爱脂肪」区，亮眼）③**眼下腮红羽 under-eye flush**（眼下柔雾一团，非社交网高斜扫）④**直软眉 soft straight brows**（柔直、可淡一阶，少西方高挑拱）。  
> 并行：**butter skin**（丝绒润、非全脸油镜）· **soft-matte / soft blur** 底 · 中文圈 **原生美学 / 千金妆 / 洛可可粉裸 / 妈生眉睫**。

### 2.1 新妆壳

| ID | 触发 | 英文种子 | 宜搭 |
|----|------|----------|------|
| **mk-blur-lip-26** | 2026 模糊唇 | soft blurred lip, rounded liner gently melted, plump cloud edge not hard ombré | 韩概念、头肩 |
| **mk-aegyo-define** | 清晰卧蚕 | defined soft aegyo-sal: cool micro-contour under eye fat + tiny highlight on top | 美妆半身 |
| **mk-undereye-flush** | 眼下腮红羽 | diffuse blush plume just under eyes, soft animated flush — not high diagonal stripe | 糖系、春 |
| **mk-straight-soft-brow** | 直软眉 | soft straight brows, slightly lighter or fluffy, less severe arch | 全日韩 |
| **mk-butter-skin** | 黄油皮 | butter skin: satin hydrated, smooth luminous not wet-glass oily | 通勤、日系 |
| **mk-soft-matte-26** | 软雾面底 | sophisticated soft-matte base, controlled highlight only high planes | 清冷、职场 |
| **mk-native-cn** | 原生美学 | native-aesthetic makeup: bone-readable, soft ma-saeng brows, sheer lip, real-skin priority | 小红书生活 |
| **mk-qianjin** | 千金妆 | quiet-luxury qianjin flush: soft monochrome rose, clean skin, refined not loud | 名媛、酒店廊 |
| **mk-rococo-soft** | 洛可可软粉 | soft rococo pink-nude atmosphere, airy blush, romantic adult — not costume porcelain | 唯美、室内 |
| **mk-igari-soft** | Igari 宿醉腮（克制） | soft hangover flush across mid-face, adult editorial — never sickly | 日杂情绪 |
| **mk-old-money-mute** | 老钱千金雾 | muted old-money glow, soft brown-rose lip, quiet contour | 法式包 |
| **mk-wet-glam-half** | 湿发 glam 半身 | glass or butter skin + strong lip + wet hair beauty crop | 棚美妆 |

### 2.2 局部拼句（并入一句）

| 局部 | 英文 |
|------|------|
| 模糊唇 | blurred lip cloud edge, soft rounded liner melt |
| 眼下羽 | blush sits under eyes in soft plume |
| 直眉 | straight soft brow, gentle lift at tail only |
| 黄油高光 | satin butter highlight on cheek high only |
| 妈生睫 | natural ma-saeng separated lashes |
| 黄皮友好 | warm-neutral undertone friendly, not gray cast |

**Main 妆金样：**
```
butter satin skin, soft straight brows, defined soft aegyo-sal, under-eye diffuse rose flush, blurred peach lip
```
```
soft-matte refined base, quiet qianjin monochrome rose, thin liner, adult clean luxury
```

**禁：** 幼态大眼强制；默认全脸油镜 glass 每帧（可点名）；舞台浓妆默认。

叠 six-axes §2 / p0-p2 妆壳。

---

## 3. 道具续（Props · 叙事锚）

> 一帧 **1 主道具**；手写接触点。六轴 §3 已有主干，本表 **补锚 + 禁组合**。

### 3.1 新增 / 强调

| ID | 触发 | 手位英文 |
|----|------|----------|
| **prop-matcha-latte** | 抹茶拿铁 | ceramic or clear cup both hands chest |
| **prop-paper-coffee** | 外带杯 | sleeve cup one hand, straw optional |
| **prop-dried-bouquet** | 干花束 | stems waist, texture readable |
| **prop-single-stem** | 单枝 | stem near collarbone — eyes free |
| **prop-tote-charm** | 托特+挂件 | tote strap + one small plush/key charm visible |
| **prop-mini-cam** | 卡片机/CCD | compact digicam at eye or chest |
| **prop-ebook-reader** | 阅读器 | e-reader one hand cafe |
| **prop-sketchbook** | 速写本 | open sketch mid-draw freeze |
| **prop-vinyl-sleeve** | 黑胶封套 | sleeve both hands cover art out |
| **prop-ticket-stub** | 电影票根 | stub + phone optional cinema lobby |
| **prop-plant-pot** | 小盆栽（花店） | small pot two hands waist |
| **prop-rail-hold** | 栏杆/扶手 | one hand rail, no prop — scene anchor |
| **prop-blazer-hook** | 西装挂指 | blazer over one finger shoulder |

### 3.2 防崩

- 禁同帧：化妆动作 + 杯 + 包 + 伞。  
- 优先：**杯 / 包带 / 栏杆 / 口袋 / 发后**。  
- I 人遮脸：杯/书/花 **挡下半脸**，保留一眼可读即可。

---

## 4. 衣着续（Clothing · 过渡胶囊）

> 2025–26 胶囊共识：**风衣过渡 · midi 万能 · 软针织层叠 · 直筒/阔腿牛仔 · Mary Jane/乐福/踝靴**。  
> 写 **2–4 件可读** + 可选 1 材质词。

### 4.1 层叠句模

| ID | 触发 | 英文 |
|----|------|------|
| **cl-trench-open** | 风衣敞开 | classic trench open, belt soft, vertical line, mid-layers readable |
| **cl-trench-cinch** | 风衣收腰 | trench belted at waist, clean A-line skirt or trouser under |
| **cl-3layer-trans** | 三层过渡 | light knit + shirt collar peek + open coat |
| **cl-midi-universal** | midi 万能 | midi dress or midi skirt column, modest neckline |
| **cl-knit-fine** | 细针织 | fine-gauge knit, not bulky swamp |
| **cl-straight-denim** | 直筒牛仔 | high-waist straight denim, clean break at shoe |
| **cl-column-skirt** | 直筒长裙 | long column skirt, elongated line |
| **cl-slip-layer** | 吊带叠（SFW） | slip dress under cardigan or blazer — fully covered shoulders or user modest |
| **cl-spring-poplin** | 春薄衬衫 | crisp poplin shirt, sleeves optional roll |
| **cl-light-leather** | 薄皮感 | lightweight leather or soft faux jacket — adult |

### 4.2 成套快配方（新）

| 配方 | 英文一句 |
|------|----------|
| 春过渡风衣 | `cotton trench open, fine cream knit, straight jeans, loafers, mini bag` |
| midi 约会 | `soft midi dress, light cardigan, Mary Janes, thin chain` |
| 胶囊通勤 | `tailored blazer, white tee, wide-leg trousers, loafers` |
| 秋三层 | `open wool coat, oxford shirt, knit vest or fine sweater, midi or trouser` |
| 盐系中性 | `oversized neutral coat, straight denim, sneakers, crossbody` |
| 千金静奢 | `camel coat, silk blouse, tailored pants, leather loafers, quiet jewelry` |

材质词：`poplin crisp · trench cotton drape · fine knit rib · denim grain · silk soft sheen · wool vertical fall`

---

## 5. 姿势续（Pose · 摄影校 + 美妆肩）

> 六轴 §5 + pose-catalog 主干。本表补 **全球人像校姿可操作句**。

### 5.1 校姿铁律（写入 Main 半句即可）

| 原则 | 英文句模 |
|------|----------|
| 45° 身 | body angled ~45° to camera, face returns to lens |
| 后重心 | weight on back leg, free knee soft |
| 臂缝 | soft air gap under near arm |
| 近膝弯 | near-camera knee slightly soft, feet closer optional for slim leg line |
| 龟颈 | chin slightly forward-and-down (turtle), neck long — not nostril tilt up |
| 头向镜倾 | head tilts slightly toward camera, never extreme away |
| 腰微前倾 | slight lean from waist toward camera for slimming line |
| 手自然腰 | hand at natural waist ~navel height, or strap/pocket |
| 髋后手 | hands light on hips or small of back for curve — fashion full body |
| 肩不对称美妆 | torso 35–40° away, near shoulder higher, far shoulder lower; face back to lens |
| 下巴 6–8° | chin lift mild 6–8° for jaw when beauty crop |
| 全身略仰 | slight low angle full body, feet in frame |

### 5.2 新 ID

| ID | 英文句模 |
|----|----------|
| **pose-turtle-chin** | chin soft forward-down, ears toward camera slightly, long neck |
| **pose-waist-lean** | slight lean from waist toward lens, spine long |
| **pose-hands-hip-back** | hands on hips or light on lower back, one hip soft pop |
| **pose-near-knee-soft** | feet near together, near knee soft bend, posture tall |
| **pose-beauty-asym-shoulder** | three-quarter beauty: torso rotated, asymmetric shoulders, face to lens |
| **pose-power-plant** | both feet plant, weight even or soft shift, shoulders back editorial |
| **pose-seat-ankle-cross** | perch edge, ankles cross, spine long, hands on knee or cup |

**全身金样：**
```
full-body read: weight back foot, soft free knee, body 45°, arm gap, one hand natural waist or bag strap, chin soft turtle, feet in frame
```

**美妆半身金样：**
```
medium close-up beauty: torso 35–40° away, near shoulder higher, face returns, chin mild lift, neck long, hands out of frame
```

---

## 6. 场景续（Setting · 锚点）

| ID | 触发 | 2–3 锚 | 光倾向 |
|----|------|--------|--------|
| **sc-book-cafe** | 书咖一体 | shelves + espresso bar + wood table | 暖混合 |
| **sc-flower-corridor** | 花店廊 | glass, buckets, wet floor optional | 散射通透 |
| **sc-parking-roof** | 屋顶停车 | painted lines, sky, rail | 硬日/蓝调 |
| **sc-stair-atrium** | 中庭楼梯 | handrail, glass, height layers | 混合 |
| **sc-riverside-path** | 河滨步道 | railing, water bokeh, path | 黄金/阴天 |
| **sc-shrine-path-adult** | 参道旅拍成人 | stone path, gate soft, respectful | 树荫 |
| **sc-design-hotel-corridor** | 设计酒店廊 | long carpet, wall sconce, door rhythm | 静奢 |
| **sc-vinyl-listening** | 黑胶试听角 | headphones, crates, warm lamp | 小店暖 |
| **sc-pottery-studio** | 陶艺工作室 | wheel soft, clay tools, apron SFW | 窗侧 |
| **sc-plant-shop** | 绿植店 | hanging plants, pots, glass | 绿散射 |

快配姿/道具：书咖→perch+coffee/book；花廊→midstride+bouquet；屋顶停→over-shoulder；酒店廊→midstride coat open。

---

## 7. 镜头轴（Lens · 可写语义）

> 补强 shot-lens-dictionary：写 **焦距感 + 景别 + 畸变/压缩一句**。  
> 文生图无真实镜头，用 **观感词**。

### 7.1 焦距语义

| ID | 观感 | 宜用 | 慎用 |
|----|------|------|------|
| **fl-24-env** | 环境压迫、略畸变 | 全身环境、自拍广角控 | 头肩近（脸畸） |
| **fl-28-street** | 理光/街拍进场 | 街、OOTD 中全景 | 美妆毛孔主 |
| **fl-35-story** | 故事型人像、含场 | 生活、环境人像、半身+场 | 强虚化偶像棚 |
| **fl-50-pure** | 自然视角、干净 | 半身通用、需有趣主体 | 无场时易「平」 |
| **fl-85-beauty** | 压缩奶油虚化 | 头肩、美妆、证件柔 | 全身小空间畸变反 |
| **fl-105-135** | 强压缩远摄感 | 远摄人像、背景贴平 | 手持晃、空间窄 |

### 7.2 景别 × 焦距推荐

| 目标 | 组合英文 |
|------|----------|
| 小红书全身 OOTD | `slight low-angle full body, vertical 3:4, 35mm street feel` |
| 环境人像 | `eye-level medium-wide, 35mm environmental, figure not dominating frame` |
| 韩/美妆头肩 | `eye-level medium close-up, 85mm compression, creamy bokeh` |
| 夜直闪街 | `eye-level full or cowboy, 28–35mm snapshot, hard flash character` |
| 地标尺度 | `wide shot, 24–35mm feel, tiny-to-medium figure vs landmark` |
| 运动腾空 | `full body, 70–135 feel compression optional, freeze shutter language` |

### 7.3 This is 句模

```
This is a [angle] [shot size] in [aspect] framing with [fl-xx] feel, [compression/distortion note], freezing [moment].
```

**例：**
```
This is a slight low-angle full body shot in vertical 3:4 with 35mm street feel and mild environmental depth, freezing mid-stride OOTD.
```
```
This is an eye-level medium close-up in 4:5 with 85mm compression and creamy background falloff, freezing a calm glass-skin gaze.
```

**畸变控制短语：** `controlled wide distortion, face proportions natural` · `no fisheye stretch`  
**压缩短语：** `telephoto compression flattening background planes` · `creamy subject separation`

---

## 8. 光线轴（Light · 九光位 + 创意）

> 钟表法（相机在 6 点、脸朝 6）：光位相对 **头与光** 的阴影关系。  
> 可与 lighting-composition 叠用。

### 8.1 九光位（可写英文）

| ID | 钟点/结构 | 英文要点 | 题材 |
|----|-----------|----------|------|
| **lt-split** | 3 或 9 | half face lit, half in shadow | 戏剧、音乐 |
| **lt-rim** | 背后 12 | rim light edge, profile optional | 剪影、演唱会 |
| **lt-butterfly** | 正前略高 ~6 | butterfly nose shadow under nose | 美妆、魅力 SFW |
| **lt-clamshell** | 蝶光 + 下补 | clamshell key above + fill below | 美妆、证件柔 |
| **lt-loop** | 5 或 7 略高 | small nose loop shadow | 通用肖像 |
| **lt-rembrandt** | 4 或 8 | Rembrandt triangle on far cheek | 性格、艺术 |
| **lt-short** | 远侧更亮 | short lighting, near cheek softer — slimming | 修型、戏剧 |
| **lt-broad** | 近侧更亮 | broad lighting, face reads wider friendlier | 开朗、补瘦脸过度 |
| **lt-cross** | 主 7–8 + 边缘 1–2 | cross lighting key + opposite edge, 3D drama | 时尚、戏剧 |

### 8.2 创意 / 现场补

| ID | 英文种子 |
|----|----------|
| **lt-gel-mono** | monochromatic gel wash, single hue mood, skin still readable |
| **lt-gel-blend** | soft blended pastel gels, gentle color mix |
| **lt-gel-comp** | bold complementary gel pair (e.g. teal-amber), controlled spill |
| **lt-fake-window** | hard light through cutters casting window-pane shadows on wall |
| **lt-optical-spot** | optical spot pattern or shaped beam on face/bg |
| **lt-shutter-drag** | subject sharp + ambient streak optional — motion language careful |
| **lt-butter-window** | large soft window, satin butter skin falloff |
| **lt-flash-ccd** | on-camera flash, compact digicam character, hard falloff |

### 8.3 Composition 光句金样

```
Rembrandt key camera-left, warm triangle on far cheek, soft background falloff
```
```
clamshell beauty: soft key high front + gentle under fill, bright catchlights
```
```
cross lighting: warm key low-front-side, cool rim opposite edge, dimensional fashion still
```
```
large window soft key camera-right, open shadow on far cheek, real-skin microcontrast
```

---

## 9. 构图轴（Composition · 可堆叠）

### 9.1 工具 ID

| ID | 用途 | 英文 |
|----|------|------|
| **comp-thirds-eye** | 人像眼位 | eyes on upper third line |
| **comp-thirds-body** | 环境人 | body mass on vertical third |
| **comp-center-icon** | 海报偶像 | centered monumental figure |
| **comp-neg-space** | 情绪留白 | large negative space, quiet field |
| **comp-fill-frame** | 美妆填满 | face fills frame, minimal bg |
| **comp-lead-line** | 引导线 | leading lines of path/rail/architecture to figure |
| **comp-frame-frame** | 框中框 | doorway, window, arch frames subject |
| **comp-layer-depth** | 街拍层 | fg blur / subject / bg story |
| **comp-diagonal** | 动势 | body or gaze on diagonal |
| **comp-scale-dwarf** | 尺度 | tiny figure vs monument or void |
| **comp-head-foot-room** | 全身呼吸 | headroom + feet in frame |
| **comp-look-space** | 视线空间 | space in gaze direction |
| **comp-action-space** | 运动前方 | space ahead of motion vector |
| **comp-dutch-rare** | 荷兰角慎 | slight dutch only if mood needs unease |
| **comp-golden-soft** | 黄金柔 | subject near phi-ish off-center balance |

### 9.2 堆叠公式（Composition 段）

```
Composition and atmosphere: [1–2 tools]; visual center on [face/pose line/garment]; [key light]; [DOF/lens feel]; [mood]; masterpiece, best quality
```

**例：**
```
Composition and atmosphere: figure on right third with leading sidewalk lines; arm gap and full-body breath; open-shade even face with soft pavement bounce; 35mm depth layers; candid lifestyle stillness; masterpiece, best quality
```
```
Composition and atmosphere: face fills upper frame on thirds eyes; 85mm creamy separation; clamshell catchlights; butter-skin microcontrast; quiet editorial; masterpiece, best quality
```

### 9.3 失败 → 补丁

| 现象 | 补丁 |
|------|------|
| 证件僵 | 45° 身 + 后重心 或 任务朝向 |
| 环境人过大 | wide + scale-dwarf / thirds-body，减五官 |
| 美妆太平 | clamshell/loop + short light 可选 |
| 无故事 | 加 lead-line 或 frame-frame 1 个 |
| 脚被切 | head-foot-room 强制 |
| 运动顶边 | action-space 前方留白 |

---

## 10. 九轴写作公式

```
镜头 L1: [angle + shot size + aspect + fl-feel]
主体: adult East Asian woman [年龄带]
发: [§1 一句]
妆: [§2 一句]
衣: [§4 2–4 件]
姿: [§5 重心+手+可选龟颈/45°]
道具: [§3 ≤1]
场: [§6 2–4 锚]
光 L5: [§8 主光]
构图: [§9 1–2 工具 + 情绪]
```

**差：**
```
beautiful girl aesthetic vibe perfect lighting masterpiece
```

**好：**
```
This is a slight low-angle full body shot in vertical 3:4 with 35mm street feel, freezing a mid-stride flower-shop doorway moment.
Main subject: An adult East Asian woman in her early twenties with a soft jellyfish cut and curtain bangs stands weight on her back foot; free knee soft, body 45°, one hand holding a small bouquet at waist, the other on the glass door frame. Cream cardigan, white tee, midi denim skirt, Mary Janes. Butter satin skin, soft straight brows, blurred peach lip. 
Environmental background: flower buckets, green stems, glass door, soft street bokeh.
Composition and atmosphere: figure on third with door frame-in-frame; open overcast daylight; candid lifestyle; masterpiece, best quality
```

---

## 11. 组合包（本卷可点名）

| combo | 触发 |
|-------|------|
| **combo-hair-jellyfish** | 水母切 |
| **combo-hair-2in1-down / 2in1-up** | 韩 2-in-1 披/夹 |
| **combo-hair-c-curl** | C 卷烫 |
| **combo-hair-milk-tea-bob** | 奶茶 bob |
| **combo-mk-blur-aegyo-26** | 2026 模糊唇+卧蚕 |
| **combo-mk-undereye-flush** | 眼下腮红羽 |
| **combo-mk-butter-native** | 黄油皮原生 |
| **combo-mk-qianjin** | 千金妆 |
| **combo-mk-rococo-soft** | 洛可可软粉 |
| **combo-cl-trench-open-spring** | 春风衣敞开 |
| **combo-cl-midi-date** | midi 约会成套 |
| **combo-pose-turtle-45** | 龟颈+45° 全身 |
| **combo-pose-beauty-asym** | 美妆不对称肩 |
| **combo-sc-book-cafe** | 书咖 |
| **combo-sc-parking-roof** | 屋顶停车 |
| **combo-lens-35-ootd** | 35mm 全身 OOTD |
| **combo-lens-85-beauty** | 85mm 美妆 |
| **combo-lt-clamshell-beauty** | 蚌式美妆光 |
| **combo-lt-cross-fashion** | 交叉光时尚 |
| **combo-lt-gel-comp** | 互补色胶 |
| **combo-lt-fake-window** | 假窗硬影 |
| **combo-comp-thirds-lead** | 三分+引导线 |
| **combo-comp-frame-neg** | 框中框+负空间 |
| **combo-nine-axes-menu** | 九轴点菜菜单 |

---

## 12. 冷门池加料（第四波 · 九轴）

1. 水母切 + 花店廊 + 捧花中步 + 35mm  
2. 2-in-1 夹出 bob + 咖啡窗坐沿 + 模糊唇  
3. C 卷 + 盐系屋顶停车回眸 + 硬日  
4. 奶茶 bob + 红唇克制 + 酒店廊风衣  
5. 眼下腮红羽 + 9:16 封面半身 + 85mm  
6. 黄油皮原生 + 书咖托腮 + 暖混合光  
7. 千金妆 + 静奢廊 + 蚌式光  
8. 洛可可软粉 + 窗纱（非私房默认场：客厅窗/酒店）  
9. 春风衣敞开三层 + 直筒牛仔乐福街  
10. midi 约会 + Mary Jane + 黄金河滨  
11. 龟颈 45° 全身 + 臂缝 + 托特  
12. 美妆不对称肩 + 湿发 + 交叉光  
13. 假窗硬影棚 + 编辑姿  
14. 互补色胶半身时尚  
15. 框中框门洞 + 负空间清冷  
16. 引导线斑马线中步 + 28mm 直闪可选  
17. 黑胶试听角 + 封套道具  
18. 陶艺工作室窗侧 + 围裙 SFW 功能姿  
19. 绿植店散射 + 小盆栽  
20. 电影票根影院大堂沙发  
21. Rembrandt 性格肖像 + 三分眼  
22. 短光显瘦西装职场窗  
23. 广角 24 控畸变自拍脚前景成人脸稳  
24. 135 压缩地标小人远摄感  
25. 生活感胶片壳 + air-dry 层 + 街角等待  

---

## 13. 点菜菜单（给用户）

```
**九轴全网补全点菜（2026 · SFW·18+）**

① 发型：水母切 · 韩2-in-1披/夹 · C卷 · air-dry层 · 奶茶bob · peekaboo · 狼尾/bob/姬（旧库）· 湿发/抓夹
② 妆容：模糊唇 · 卧蚕 · 眼下腮红羽 · 直软眉 · 黄油皮 · 软雾面 · 原生 · 千金 · 洛可可软 · 韩水光/抖音软（旧）
③ 道具：杯/花/托特挂件/CCD/书/黑胶/票根/栏杆空手（≤1）
④ 衣着：风衣开合 · 三层过渡 · midi · 胶囊通勤 · 千金静奢
⑤ 姿势：45° · 后重心 · 臂缝 · 龟颈 · 腰倾 · 美妆不对称肩 · 坐沿
⑥ 场景：书咖 · 花廊 · 屋顶停 · 酒店廊 · 河滨 · 绿植店 · 旧第三空间库
⑦ 镜头：24环境 · 28街 · 35故事 · 50自然 · 85美妆 · 135压缩 + 景别画幅
⑧ 光线：九光位（蝶/蚌/环/伦勃朗/分割/短宽/交叉/轮廓）· 窗/色胶/假窗/直闪
⑨ 构图：三分眼/身 · 引导线 · 框中框 · 负空间 · 填满 · 层次 · 动线留白

例：`水母切+花店+35mm+开衫中裙` / `2-in-1夹bob+模糊唇+咖啡窗` / `85mm蚌式+黄油皮头肩` / `风衣敞开+屋顶停+回眸硬日` / `交叉光+美妆不对称肩`
说明：一帧发妆各一句、道具一个；少女感=成年气质；私房另点名。
```

---

## 14. 写作时如何调用

1. 用户说「发型/妆容/道具/衣/姿/场/**镜头/光线/构图**」或「再全网补全/九轴」→ **本卷**；六轴旧词仍有效。  
2. 仅镜头/画幅 → 可只开 §7 + shot-lens-dictionary。  
3. 仅光 → §8 + lighting-composition。  
4. 仅构图 → §9。  
5. 与 p0-p2 / web-fill / six-axes **叠 ID，不互相覆盖用户原话**。  
6. 「有哪些」→ §13 点菜，勿整卷粘贴。  
7. 「最新流行」→ 本卷 + 可再联网复核。  

---

## 15. 参考来源（检索内化摘要）

- **发型**：日系 hime / wolf / soft jellyfish / milk-tea bob / peekaboo；韩 2-in-1 hidden bob；C-curl / air-dry layers 2025–26  
- **妆**：Vogue 2026 K-beauty — blurred lips · aegyo-sal · under-eye flush · soft straight brows；butter skin vs glass；中文原生/千金/洛可可壳  
- **姿**：45° body · weight back · arm gap · turtle chin · waist lean · beauty asymmetric shoulders  
- **衣**：trench transition · midi · fine knit layering · capsule neutrals  
- **光**：PPA/John Gress 九光位钟表；cross lighting；gel mono/blend/complementary；fake window cutters  
- **镜**：35 故事 / 85 美妆 / 24 环境语义与畸变压缩  
- **构图**：thirds · leading lines · frame-in-frame · negative space · fill frame · action/look space  
- **道具场**：书咖/花/杯/CCD 等叙事锚；一主道具防崩  

**交付释义可写：**  
`**参考来源**：九轴全网补全 2026（发妆道具衣姿场 + 镜头光线构图内化）`

---

## 16. 交叉引用

| 需要 | 文件 |
|------|------|
| 六轴主干词库 | six-axes-web-fill-2026 |
| 景别焦距薄表 | shot-lens-dictionary |
| 布光构图主表 | lighting-composition |
| 妆发场景矩阵 | asian-young-woman-p0-p2 |
| Core 标签 | asian-young-woman-web-fill-2026 |
| 检索模板 | research-protocol |
| 私房点名 | soft-boudoir-sfw-web-fill-2026 |

---

## 17. 五次联网补 · 2026-09（镜头/光线/构图）

| ID | 中文触发 | 英文句模 |
|----|------|----------|
| lt-prism-spectrum | 棱镜光谱 | Sunlight passed through a glass prism held at eye level, a rainbow spectrum band projected across her cheek and neck, sharp white daylight key, clean neutral background letting the band read |
| lt-candle-glow | 烛光塑形 | Single lit candle on a table at chin height, warm flickering low light sculpting the face from below-front, soft shadow falloff up the forehead, everything beyond two meters falling into black |
| lt-rain-glass | 雨窗光斑 | Shot from inside through a rain-speckled window, blurred water droplets catching streetlight as soft bokeh circles, even diffused light on the face, glass texture layered between camera and subject |
| comp-9x16-frame | 竖版九比十六 | Full-body vertical 9:16 frame, subject in the center column, generous negative space above the head, camera tilted 10-15 degrees from below for leg length, feed-native framing |
| comp-mirror-selfie | 镜中自拍构图 | Full-length mirror selfie with the camera visible in the reflection, one arm extended holding the phone, on-device flash lighting the scene flat, room context framing the mirrored figure |
| comp-cine-2-39 | 宽银幕横幅 | Anamorphic 2.39:1 widescreen composition, subject placed at the left third looking across the long horizontal frame, environment stretching wide behind, cinematic banded framing |

> 来源：<https://www.photoworkout.com/photoshoot-ideas/> · <https://www.inspirefusion.com/photography-trends-2026/> · <https://www.lemon8-app.com/discover/photoshoot%20prop%20ideas?region=us> · <https://www.voncreativeco.com/creative-corner/flash-forward-mastering-the-paparazzi-aesthetic-without-losing-the-romance>
