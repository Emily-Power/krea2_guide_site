# Civitai 双站生态补全（.com + .red · 2026）— SFW 人体/人像

> **检索内化**：civitai.com · civitai.red · Civitai Prompting Compass · Prompt-Crafting Guide · 社区文 *Controlling Zoom With Words Alone*（Krea2）· *Guide to the General AI scene in 2026* · Pose LoRA 卡片（Instagram Style / Peeking Out 等）· 站内 tag 生态（photography / fashion / photorealistic）。  
> **本卷定位**：把 **Civitai 生态的写法共识、取景控制、反推清洗、站内热门姿/题材壳** 译成 **可画英文句**，叠进 figure-photo 的六层 + 大区 A–I。  
> **SFW · 18+**。露骨 → `erotic-prompt`。  
> 与 `research-protocol` / `pose-catalog` / `web-fill` / `model-prompting` 联用；**不重复**日韩中写真体系全文。

---

## 0. 双站分工（2026 分裂后）

| 站 | 角色 | 对本 skill |
|----|------|------------|
| **civitai.com** | 主流 / 偏 SFW·PG；摄影/时尚/概念 LoRA、生成元数据、文章指南 | **主参考**：姿势 LoRA、摄影语言、写实提示、Remix 反推 |
| **civitai.red** | freedom-first；NSFW 模型与硬核样例主战场 | 仅当用户给 **.red 链接/元数据** 时：提取 **姿/光/衣/机位**，**丢弃 NSFW 残渣** 后改写 SFW |

**原则：**

1. 本 skill **默认写 SFW**；从 .red 反推时 **禁止** 把露骨连接点带进正文。  
2. 从任意站 **Remix** 时执行 §2 清洗管线。  
3. 站内 **姿势概念 LoRA 名**（`dynapose` 等）→ 译成身体结构句，**不把触发词当散文主体**（除非用户本地加载该 LoRA）。

---

## 1. Prompting Compass → 本 skill 映射

来源：Civitai *The Prompting Compass* + *Prompt-Crafting Guide* 共识。

| 生态学校 | 特征 | figure-photo 默认 |
|----------|------|-------------------|
| **Danbooru 标签校** | `1girl, standing, looking at viewer…` | **非默认**；用户点 SD/Pony/Illustrious 短句时才用 |
| **自然语言校** | 完整句、摄影语、关系与氛围 | **默认（Krea2 / Seedream）** |
| **混合校** | 句描述场景 + 少量精确标签 | 仅用户要「动漫向短句」时；仍 **adult 锁** |

| 反模式（站内常见坏 Remix） | 正确做法 |
|---------------------------|----------|
| `score_9, score_8_up` 打在 Krea/Flux/Seedream | **删除**；改 `masterpiece, best quality` 或只靠光/材质句 |
| 一套提示通吃所有底模 | 按模型族切换（见 model-prompting） |
| hashtag 墙 / quality 刷屏 | 六层可画句 |
| 只写 beautiful girl | 身份+姿+光+材质 |
| 未写人种 → 欧美默认脸 | **East Asian 默认**（本 skill 强制） |
| 姿态 LoRA 触发词堆正文 | 触发放工作流；正文写 weight/hip/hand |

**摄影语言加分（写实 · 点 2～4 个）：**

```
85mm portrait · 35mm street · f/1.8 shallow DOF · open shade · Rembrandt key ·
hard noon sun · golden hour · on-camera flash · film grain · RAW photo feel
```

---

## 2. Generation Data / Remix 清洗管线（.com 与 .red 通用）

用户给链接、截图元数据、Resources used 时：

```
1. 提取：pose · camera/framing · light · clothing · setting · expression · medium
2. 丢弃：score_* · 错误 (word:1.9) 权重 · 重复 quality · teen/loli · NSFW 残渣 · 拼写崩坏
3. 补全：成人身份 + East Asian（未覆盖时）+ 六层缺层
4. 改写：形态 A 四段 或 Seedream B；身份用用户触发词/描述替换样例脸
5. 释义一行：**参考来源**：Civitai 样例反推（已清洗）
```

| 元数据字段 | SFW 用法 |
|------------|----------|
| Prompt | 姿/场/光原料 |
| Negative | 仅 SD 族参考；Krea 改为正向「要什么」 |
| Resources / LoRA | 记触发与权重；**不进** Main 散文堆叠 |
| Size | 画幅建议（3:4 / 9:16 / 16:9） |
| Seed | 连续改姿可提示用户锁 seed（工具层） |

---

## 3. 词预算变焦（Krea2 社区核心 · 深度）

> 内化自 Civitai 文 *Controlling "Zoom" With Words Alone*（Krea2 向，可迁移）。  
> **变焦 ≠ 只写 "close-up"**；变焦 = **谁先写、谁写得多**。

| 目标取景 | 词序策略 | 英文操作 |
|----------|----------|----------|
| **头肩/美妆近** | 人物几乎占满词；场 1 句虚化 | face/eyes/makeup first; room = "blur of …" |
| **半身～2/3** | 主体领跑 + 明确裁切句 | `framed from head to mid-thigh` + 1 行 soft-focus room |
| **全身** | **可房间/地面先** 或 主体+强制脚 | `full body` + **`feet on …` / feet in frame** |
| **环境人像/房间尺度** | **场先段 · 人后短句** | 先墙家具光，再 `in the distance` / small figure |

**铁律补丁：**

1. 想某部位进画 → **直接描写该部位**（`bare feet on white rug`），别只靠 crop 标签。  
2. **接触点锚定尺度**：`hand on desk` · `feet on carpet` · `shoulder to wall`。  
3. 全身却总出半身 → 提高环境词占比 **或** 强制 `full body, feet in frame, headroom`。  
4. 环境人像人过大 → 场先 + 缩脸部词数 + `figure balanced with architecture`。

**句模（全身街拍）：**
```
A photo of a tree-lined city sidewalk in open shade: storefront glass, wet curb after rain, bicycle rack.
Full body shot of an adult East Asian woman in her early twenties mid-stride, weight on front foot, tote on near shoulder, feet on the pavement, casual coat open, calm gaze ahead — not a tight portrait.
```

**句模（头肩美妆）：**
```
Close beauty portrait of an adult East Asian woman mid-twenties, glass skin, soft glam eye, satin lip, asymmetric shoulders, face filling the frame; behind her only a pale seamless blur.
```

与 shot-lens-dictionary、比例铁律叠用。

---

## 4. 站内热门姿势概念 → 可画句（SFW）

> 来源：.com Pose/Concept LoRA 生态（Instagram Style、Peeking Out、The Pose 等）+ 摄影 tag 样例。  
> **写成结构，不抄 LoRA 名进交付**（除非用户点名加载）。

### 4.1 Instagram / 网红动态姿（dynapose 向）

| ID | 触发 | 可画要点 |
|----|------|----------|
| **ig-stand-confident** | 站姿自信 | weight back leg, free knee soft, one hand hip or pocket, shoulder drop |
| **ig-sit-edge** | 坐沿 | perch seat edge, ankles cross or knees soft, spine long, not sunk |
| **ig-crouch** | 蹲 | asymmetric knees, upright torso, heels optional, eyes to lens |
| **ig-midstride** | 中步 | front foot plant, rear heel lift, arm natural swing freeze |
| **ig-lean-wall** | 靠墙 | shoulder or hip committed to wall, arm gap from torso |
| **ig-look-back** | 过肩回眸 | chin off neck, three-quarter back, face returns to lens |
| **ig-chair-lounge** | 椅上慵懒 | sideways lounge, one arm over backrest, legs drape |

```
instagram-style SFW full-body still, adult East Asian woman early twenties, weight on back foot, free knee soft, one hand in coat pocket, other holding phone low, open shade street, feet in frame, candid-confident not stiff studio
```

### 4.2 探身 / 门框 / 半遮（peeking 向 · SFW）

| ID | 要点 |
|----|------|
| **peek-door** | upper body past door frame, hand on jamb, rest of body implied |
| **peek-wall** | face and one shoulder past wall edge, playful adult not coy-child |
| **peek-curtain** | sheer or drape parted, eyes visible, fully clothed |

```
peeking-out portrait SFW, adult East Asian woman, face and near shoulder past a wooden door frame, hand on jamb, soft indoor key, curious soft smile, modest clothing, clearly adult
```

### 4.3 趴姿脚抬（the-pose 向 · **仅 SFW 生活/居家**）

| 约束 | 写法 |
|------|------|
| 场景 | bed/sofa **居家生活**；非色情 |
| 姿 | on stomach, elbows prop optional, **feet up** soft, soles optional |
| 服 | **着装完整** 默认；用户点私房再升 soft-boudoir L0–L1 |
| 禁 | 自动露点、并自动 erotic |

```
home lifestyle SFW, adult East Asian woman on stomach on linen bed, chin on hands, feet lifted soft behind, oversized knit fully covering, window soft key, playful adult, not boudoir-explicit
```

### 4.4 社区高频标签 → 摄影句（SFW 过滤）

| 站内高频方向 | 正文落点 |
|--------------|----------|
| looking at viewer | eyes to camera, catchlight |
| from above / high angle | slight high for自拍感；忌压扁全身比例 |
| from below / low angle | fashion power / 腿长；SFW 勿默认裙底 |
| cowboy shot | mid-thigh crop 明示 |
| upper body / portrait | 词预算拉近 |
| full body | feet + headroom |
| outdoors / street | 环境锚 2–4 |
| indoors / bedroom | 仅 I 区或用户点名；默认着装 |
| natural lighting / soft lighting | open shade / window |
| cinematic lighting | motivated key + rim 一句 |
| depth of field / bokeh | shallow DOF 服务主体 |
| film grain / analog | 胶片媒介词 ≤2 |

---

## 5. 站内题材壳（.com 热 · 可点菜）

在 A–I 大区之上，补 **Civitai 生成流高频壳**（非再造日韩中体系）：

| ID | 触发 | 大区 | 画面一句 |
|----|------|------|----------|
| **cv-gaming-rgb** | 电竞房/RGB 房 | G/E | RGB 灯带+椅+显示器；用 §3 词预算控全身/半身 |
| **cv-cafe-window** | 咖啡窗座 | G | 窗侧光、杯、街虚化 |
| **cv-office-glass** | 玻璃走廊 OL | E | 冷荧+窗混、中步或侧坐 |
| **cv-rooftop-golden** | 天台黄金时 | B/G | 暖侧光、天际线 |
| **cv-subway-hold** | 地铁拉环 | B | 通勤、现场混光 |
| **cv-museum-scale** | 馆拍尺度 | G | 人+作品同框（叠 web-fill §4） |
| **cv-studio-seamless** | 无缝棚 | A | 干净背景、版型可读 |
| **cv-lookbook-white** | 白底 lookbook | A | 全身脚进画 |
| **cv-hard-flash-night** | 夜直闪 | B | 叠 style-packs GR/CCD |
| **cv-film-street** | 胶片街 | B | 颗粒+中步 |
| **cv-beauty-softbox** | 美妆柔箱 | A | 头肩、肤质 |
| **cv-sports-freeze** | 运动定格 | C | 相位+支撑 |
| **cv-dance-studio** | 练功房 | D | 镜墙+把杆 |
| **cv-travel-landmark** | 旅拍地标 | G | 人与地标尺度 |
| **cv-rain-umbrella** | 雨伞街 | B | 湿反光 |
| **cv-library-quiet** | 图书馆 | E/G | 安静坐姿、侧窗 |
| **cv-kitchen-morning** | 厨房晨 | G | 生活任务姿 |
| **cv-mirror-ootd** | 全身镜 OOTD | social | 镜中全身、手机可入画 |

**组合包 ID：** `combo-cv-*` 与上表同名后缀。

---

## 6. 亚洲人种与站内偏差（深度）

| 现象（社区观察） | 本 skill 对策 |
|------------------|---------------|
| 部分新模型 / PE 增强易漂 **白人脸** | Main **起句**写死 `adult East Asian woman/man` |
| 部分亚洲特化模型过度「网红磨皮」 | 写 `real pores, natural skin texture, not plastic` |
| 只写 Asian 不够 | 可细化 `East Asian` / `Japanese` / `Korean` / `Chinese features`（用户或语境） |
| 年龄漂幼 | `early/mid twenties` + mature adult proportions；禁 teen |
| 用户要欧美人 | **用户覆盖**，去掉默认东亚 |

```
Main subject: An adult East Asian woman in her early twenties …
```

---

## 7. 资源层（提示词作者需知 · 非默认堆进 prompt）

| 社区习惯 | skill 行为 |
|----------|------------|
| 人物 LoRA + 姿势 LoRA | 身份与姿势 **分离描述**；姿势用结构句 |
| 风格 LoRA / embedding | 用户点名再提；正文用光色介质表达 |
| Krea2 / Qwen TE | 默认六层完整句（已是本 skill 主轴） |
| Qwen-Image / Edit（站内 2026 热） | 用户点名时：自然语指令清晰；编辑用 keep/change |
| Z-Image Turbo 等快模 | 缩 L6；保姿+光 |
| SDXL/Pony（点名） | 短标签可选；**非默认** |
| 站内 Buzz / 云端生成 | 与本地 Comfy 无关；仍按模型族写提示 |

---

## 8. 差 → 好（Civitai 坏提示 → figure 正文）

**差（跨生态 Remix 典型）：**
```
score_9, score_8_up, 1girl, beautiful, masterpiece, best quality, asian girl, cute, street, solo
```

**好：**
```
This is an eye-level full-body street photograph, open-shade candid, vertical 3:4.
Main subject: An adult East Asian woman in her early twenties stands mid-stride on wet sidewalk; weight on front foot, rear heel lifting, near hand on tote strap, free arm soft at side. Oversized charcoal coat open over cream knit and straight jeans; sneakers fully in frame. Soft closed-mouth expression, gaze slightly past camera.
Environmental background: tree-lined old street, shop glass reflections, bicycle rack soft.
Composition and atmosphere: figure balanced with architecture, shallow depth behind, natural skin pores, masterpiece, best quality.
```

---

## 9. 冷门池（Civitai 向 · 跨大区）

1. RGB 电竞房全身（场先词预算）  
2. 门框探身半身 SFW  
3. 椅侧慵懒 2/3 身  
4. 白底 lookbook 转身定格  
5. 地铁拉环现场钠灯  
6. 雨夜直闪街中步  
7. 图书馆侧窗托书  
8. 练功房镜前一位  
9. 天台黄金时风衣  
10. 厨房晨光持杯任务姿  
11. 全身镜 OOTD 手机入画  
12. 馆拍装置旁小人  
13. 趴床抬脚居家针织（SFW）  
14. 蹲姿不对称膝街拍  
15. 过肩回眸巷弄  
16. 咖啡窗座三分构图  
17. 运动腾空相位（C）  
18. 棚拍短光显瘦半身  
19. 胶片颗粒公园步  
20. 机场窗边拉杆箱全身  

抽取后必须 **完整六层正文**，禁止只回 ID。

---

## 10. 组合包速查

| combo | 触发 |
|-------|------|
| combo-cv-gaming-rgb | 电竞房 RGB |
| combo-cv-cafe-window | 咖啡窗 |
| combo-cv-office-glass | 玻璃走廊 OL |
| combo-cv-rooftop-golden | 天台黄金时 |
| combo-cv-subway-hold | 地铁拉环 |
| combo-cv-studio-seamless | 无缝棚 |
| combo-cv-lookbook-white | 白底 lookbook |
| combo-cv-hard-flash-night | 夜直闪 |
| combo-cv-mirror-ootd | 镜 OOTD |
| combo-cv-peek-door | 门框探身 |
| combo-cv-ig-midstride | IG 中步 |
| combo-cv-ig-crouch | IG 蹲姿 |
| combo-cv-home-feetup-sfw | 居家抬脚 SFW |
| combo-cv-zoom-roomscale | 词预算房间尺度 |
| combo-cv-zoom-beauty | 词预算美妆近景 |

---

## 11. 联网检索模板（Civitai 专用）

```
site:civitai.com portrait posing full body photorealistic
site:civitai.com fashion editorial lighting prompt
site:civitai.com articles prompt guide Krea2 OR SDXL
site:civitai.com pose LoRA standing sitting crouching
site:civitai.com "Main subject" East Asian OR Korean OR Japanese woman
site:civitai.red （仅用户 NSFW 链接时）→ 提取后清洗为 SFW
```

用户说「Civitai 热门姿/最近站内流行」→ **先搜再写**；禁止编造具体下载量排名。

---

## 12. 写作时如何调用

1. 用户丢 .com/.red 链接或元数据 → §2 清洗 → 六层正文  
2. 全身出半身 / 环境人像比例不对 → §3 词预算变焦  
3. IG/网红/蹲站坐姿 → §4.1  
4. 探身门框 → §4.2  
5. 电竞房/RGB/lookbook 等壳 → §5 combo-cv-*  
6. 白人脸漂 → §6 起句锁东亚  
7. 趋势不确定 → §11 检索  

---

## 13. 点菜菜单（给用户）

```
**Civitai 生态补全点菜（SFW·18+）**

写法：自然语言六层 · 禁 score 跨生态 · Remix 清洗
取景：词预算变焦（近/半身/全身/房间尺度）
姿壳：IG站坐蹲中步 · 门框探身 · 居家抬脚SFW
题材壳：电竞RGB · 咖啡窗 · OL走廊 · 天台 · 地铁 · 白底lookbook · 夜直闪 · 镜OOTD
人种：默认 East Asian adult；用户可覆盖

例：`组合:词预算房间尺度` / `组合:IG中步` / `组合:电竞房RGB` / `反推这条Civitai元数据`
```

---

## 14. 交叉引用

| 需要 | 文件 |
|------|------|
| 六层/篇幅 | krea2-qwen-te-layered-prompting |
| 大区 A–I | breadth-catalog |
| 姿库 | pose-catalog |
| 景别 | shot-lens-dictionary |
| 亚洲女出片 | asian-young-woman-p0-p2 · web-fill |
| 联网总协议 | research-protocol |
| 露骨 | erotic-prompt / community-ecosystem-2026 |

**交付释义可写：**  
`**参考来源**：Civitai.com/.red 生态补全 2026（Prompting Compass · 词预算变焦 · 姿概念内化）`
