# 社区生态补强（2026）— Civitai.red / PH / 里番 / X / 谷歌

用于完善 `erotic-prompt` 的**实操层**（非再堆一个 fetish 列表）。  
与 `model-prompting-krea2-seedream.md`、`connection-templates.md`、`fantasy-erotic-catalog.md` 联用。

---

## 1. Civitai 双站（必知）

| 站 | 角色（2026 分裂后） |
|----|---------------------|
| **civitai.com** | 偏 PG / 主流；NSFW 受限 |
| **civitai.red** | **freedom-first / NSFW 主战场**：成人模型、LoRA、姿势、硬核样例、生成元数据 |

**对本 skill 的意义：**

1. **反推样例**：在 .red 找喜欢的图 → 打开 **Generation Data / Resources used** → 提取姿势句、光、LoRA 触发词，**改写成 Krea2/Seedream 自然语**，勿原样照搬错误生态标签。  
2. **LoRA 身份**：触发词只放工作流 `trigger` 字段（见 krea2-multi skill）；正文描述**不要**重复刷触发词。  
3. **Krea2 生态**：.red 已有 **Krea 2 NSFW**、refusal-reduction 类 LoRA 等社区资源；提示仍以散文+连接点为主，LoRA 补身份/露骨能力。  
4. **禁止**：把 Pony 的 `score_9, score_8_up` 无脑贴到 Krea2/Seedream/Flux（Civitai 官方也批评「坏提示」跨生态混用）。

### 1.1 Remix 工作流（写 prompt 时）

```
喜欢的样例图 → 读元数据
  → 保留：pose / camera / light / clothing state / act connection
  → 丢弃：错误 score 标签、重复 quality 刷屏、拼写崩坏权重
  → 输出：本 skill 四段 或 Seedream 短密
  → 身份：用用户自己的 LoRA/触发词替换样例角色
```

### 1.2 样例元数据里常有用的字段

| 字段 | 用法 |
|------|------|
| Prompt | 姿势与场景原料 |
| Negative | 仅 SD 族参考；Krea 正向改写为「要什么」 |
| Resources / LoRA | 记触发词与权重，不抄进散文主体 |
| Size / Seed | 画幅参考；seed 连续调姿 |

---

## 2. Civitai 提示原则 → 本 skill 映射

来源：Civitai Prompt-Crafting Guide / Prompting Compass 等社区共识。

| 原则 | 映射 |
|------|------|
| **为具体模型写提示** | 默认 Krea2；Seedream 双给短密；勿一套提示通吃 |
| **自然语适合复杂场景与互动** | 四段散文 + 连接点句模 |
| **坏提示**：错权重括号、拼写、生态错标签 | 输出前自检；禁止 `(word:1.9)` 当默认 |
| **摄影语言提升写实** | 见 §5 相机词表 |
| **动漫模型易偏幼** | **强制成人锁** 见 §4 |
| **Remix 传播坏提示** | 反推时清洗再输出 |

---

## 3. Pornhub / 成人类搜索 → 静帧翻译

视频站热搜是**叙事+标签**，文生图要改成**单帧可视**：

| 视频思维 | 静帧写法 |
|----------|----------|
| “then she rides harder” | hips fully seated, thighs tensed, mid-bounce freeze |
| 长镜头推拉 | 选一个角度写死 low-angle / POV |
| 分类名 creampie | 溢流视觉句，不是标签墙 |
| 标题党 hashtag | 全部展开成身体与光 |
| 竖屏 Shorties | 竖构图 + 主体占画面 60%+ |

**PH→prompt 三步：** 分类/标题 → 选一动作高潮帧 → connection-templates 填连接点。

---

## 4. 里番 / Danbooru 生态 → 成人锁与标签翻译

### 4.1 成人锁（防「幼态漂移」）

Illustrious/Pony/部分二次元底模训练数据偏幼时，**mature 要写进正向**：

英文锚点（必选其一或组合）：

```
adult woman in her early twenties, mature face, adult proportions
clearly 20 years old or older, womanly body
```

负向要点（形态 D，本地模型）：

```
child, loli, shota, teen, underage, aged down, young girl, baby face, flat childish face
```

**本 skill 安全线不变**：永不写 teen/loli 正向；动漫风也锁成人。

### 4.2 高频里番概念 → 自然语（勿只丢罗马音标签）

| 标签/梗 | 自然语要点（成人） |
|---------|-------------------|
| ahegao | rolled eyes, tongue out, drool, fucked-silly face |
| netorare / NTR | third-party present or watching; her gaze to watcher; adult affair |
| netori | she actively takes another's partner; dominant smile |
| paizuri | breasts pressed around shaft |
| cumflation | soft rounded belly + overflow（轻量） |
| mind break | empty bliss eyes, slack smile, after heavy sex |
| virgin killer sweater 等服装梗 | 具体领口/露背剪裁，不写品牌梗空词 |
| miko / nun fallen | torn ritual clothes + lust runes optional |
| futanari | **explicit**：has both a functional penis and vagina / breasts + erect penis；解剖写清 |
| monmusu | species features 2–4 + human adult face |
| shokushu | elegant tentacles + connection |
| saimin / hypno | spiral pupils, bliss obedience（成人 RP） |
| oyakodon 等 | **仅全体明确成年**；否则拒绝 |

### 4.3 标签顺序思维（仅当用户要「动漫短句」时）

社区常见序（**非 Krea 默认**）：

`rating/explicit → count 1girl → body → hair/eyes → clothes state → pose/act → fluids → expression → background → quality`

Krea/Seedream 默认仍用**句子**，把同一信息嵌进 Main subject。

---

## 5. 摄影 / 技术词表（写实色情加分）

来自写实向 Civitai 指南与 X Seedream 样例；**点到为止 2～4 个**，勿刷屏。

| 类 | 示例 |
|----|------|
| 镜头 | 35mm, 50mm, 85mm portrait, slight wide-angle |
| 光圈景深 | f/1.8 shallow DOF, f/4 environmental |
| 光 | tungsten practical, softbox key, hard noon sun, rim light, chiaroscuro |
| 媒介 | shot on film, fine grain, RAW photo, editorial flash |
| 画质 | highly detailed skin pores, specular sweat, sharp eyes |

Composition 段示例：

```
85mm look, shallow depth of field, warm tungsten key from camera-left, film grain, highly detailed skin
```

---

## 6. X / 视频管线（静帧 → 动）

社区常见（非唯一）：

1. **Seedream / Krea** 出关键帧（本 skill 形态 A/B）  
2. **图生视频**（Seedance 等）：Motion **一句一个主动作**  
3. 续写：用末帧再滚（copy last frame）

动效句禁止：同时 thrust + undress + walk + spin。  
本 skill **O 节**已覆盖；此处强调 **先静帧可读，再动**。

X 有效动效例：

```
his hips thrust steadily into her; her breasts sway; she gasps toward camera
```

---

## 7. 结构化提示（Seedream/X 常见 JSON 风）

部分创作者用 JSON 字段组织再展平。本 skill **默认真文四段**；用户要「JSON 提示」时可输出：

```json
{
  "subject": "adult woman early twenties, ...",
  "pose_and_act": "connection sentence...",
  "clothing_state": "...",
  "environment": "...",
  "lighting": "...",
  "camera": "vertical 3:4, low angle, 50mm",
  "style": "cinematic erotic still"
}
```

展平规则：按 subject → pose_and_act → clothing → environment → lighting → camera → style 拼成自然段（Seedream 前重后轻）。

---

## 8. 资源与工作流习惯（.red / 本地）

| 习惯 | skill 行为 |
|------|------------|
| 人物 LoRA + 姿势 LoRA | 身份与姿势分离描述；姿势用连接句，不靠姿势 LoRA 名当正文 |
| 两段生成：构图 → inpaint 露骨 | 先出构图版（sensual）再出 explicit 补丁句 |
| 拒绝/审查 | 本地 Comfy **无云审核**；NSFW 文案直接写清。Krea2 NSFW LoRA 仅作工具层补能力，**不替代**连接点与散文质量 |
| 元数据分享 | 鼓励用户从 .red 带 Generation Data 来「是这样吗」校准 |

---

## 9. 额外题材补漏（跨站高频、skill 可点）

| ID 建议 | 说明 |
|---------|------|
| **size-difference-soft** | 手掌对比腰；双方成人 |
| **clothed-female-nude-male** | CFNM 权力差 |
| **clothed-male-nude-female** | CMNF |
| **outbound-phone** | 通话中被做；表情 supressed moan |
| **recording-performative** | 知镜头表演式色情 |
| **asymmetric-undress** | 只剩一边袜/一鞋 |
| **makeup-ruined** | 妆花+精液/泪 |
| **tan-lines** | 晒痕强调裸区 |
| **body-writing** | 皮肤字（成人合意幻想） |
| **collar-only-nude** | 仅项圈全裸 |
| **from-below-upskirt-explicit** | 明确成人裙底；非偷拍未成年场景 |
| **against-mirror-double** | 镜中第二角度同行为 |

写入组合包或临时分支即可，不必每次全开。

---

## 10. 反模式总表（跨生态）

| 反模式 | 正确做法 |
|--------|----------|
| score_9 打在 Krea/Seedream | 删；改质量与光 |
| 正负提示复制同一套 | 按模型族切换 |
| hashtag 墙 | 视觉句 |
| 只写 nsfw 不写动作 | 连接点 |
| 动漫不写成年 | adult woman early twenties |
| 视频剧本塞静帧 | 单帧定格 |
| 从 .red 抄坏权重括号 | 清洗后重写 |
| 风格词互斥十个 | 一个主风格 + ref |

---

## 11. 给模型的执行清单（出 prompt 前）

1. 模型：Krea2 默认 / Seedream 双给？  
2. 有无 .red/样例元数据要清洗？  
3. 单帧连接点是否完整？  
4. 成人锁是否写入（尤其 anime-explicit）？  
5. 摄影词是否 2～4 个点到为止？  
6. 是否误带 SD 生态垃圾标签？  
7. 幻想元素是否助色而非猎奇？  
8. 安全：18+、无 teen/loli？  
9. 人种：未指定已 East Asian？  
10. 词预算取景是否与景别目标一致（§12）？  
11. POV/体位热概念是否已落成连接句而非标签（§13）？  

---

# 第四部分：Civitai.red / .com 2026 广度×深度补强

> 内化来源：双站分裂说明、*Guide to the General AI scene in 2026*、*The Civitai Prompting Compass*、*Prompt-Crafting Guide*（坏 Remix / score 跨生态）、*Controlling Zoom With Words Alone*（Krea2 词预算）、站内 NSFW POV / 体位 / ahegao 等 Concept LoRA 生态、Krea2 NSFW / refusal-reduction 资源讨论。  
> **目的**：补 skill 在 **站内实操深度** 与 **热概念→静帧** 上的缺口；**不**替代 connection-templates / breadth 主表。

---

## 12. 词预算变焦（Krea2 · 色情取景深度）

> 与 figure-photo 同源技巧；色情默认 **中近景**，但全身跪姿/后入/环境暴露必须会 **拉远**。

| 目标 | 词序 | 色情注意 |
|------|------|----------|
| **脸+胸私房** | 人物细节占满；场 1 句虚化 | 勿误砍表情与潮红 |
| **半身展示/自慰** | 明确 `framed head to …`；连接/手位写满 | L3 连接不因缩景别删除 |
| **全身跪/后入/骑乘** | 可场先短段 **或** 强制 `full body, knees/feet in frame` | **需要展示的结合部写进画内** |
| **房间尺度偷情** | 场先（酒店 tungten、乱床、门）→ 人短句 + `in room` | 远景禁止写黏膜丝；比例铁律 |

**接触点锚定（色情高频）：**

```
knees on mattress · hands gripping sheet edge · soles toward ceiling ·
shoulders to headboard · cheek to pillow · feet on floor standing fold ·
hands on partner's thighs (POV)
```

**全身后入却出半身 → 补丁：**
```
full body from side-rear, her knees and feet on the bed fully in frame, ass raised, his hips and thighs visible behind, wet junction in lower third, headroom included
```

**只出脸却要中出细节 → 改景别或改内容**，禁止矛盾。

---

## 13. .red / 站内热概念 LoRA → 自然语连接（广度）

> 社区大量 **Concept / Pose / Action LoRA**（POV 全家桶、doggy、cowgirl、ahegao、解剖细节等）。  
> **交付原则**：触发词留工作流；正文写 **可读连接点**（见 connection-templates）。

### 13.1 POV 全家桶映射（约 19 类社区覆盖的压缩表）

| 社区方向 | 本 skill 落点 | 连接/构图一句要点 |
|----------|---------------|-------------------|
| POV blowjob / deepthroat | combo-pov-bj · B3 | lips on shaft, eyes to lens, your hips edge optional |
| POV doggy | combo-pov-doggy | ass to camera, hands on waist, shaft entering rear |
| POV missionary | B2 missionary + H=pov | legs open toward lens, partner torso crop |
| POV cowgirl | B2 cowgirl + pov | she straddles toward you, hips down, breasts forward |
| POV reverse cowgirl | reverse-cowgirl + pov | back and ass to lens, look over shoulder |
| POV standing fold | standing + pov | against wall, one leg up, junction low frame |
| POV titjob | B3 titjob | shaft in cleavage channel, chin above |
| POV footjob | Q footjob | soles/arch around shaft, low angle |
| POV facesitting | B3 facesitting | hips over face, from below |
| POV handjob | Q handjob | hands on shaft, torso crop |
| undressing mid | E1 half-undressed | garment height frozen mid-peel |
| creampie POV | K=creampie | overflow at entrance toward lens |
| facial POV | K=facial | ropes on face toward viewer |
| mating press POV | B2 mating-press | knees to chest, deep fold, from above-slight |
| prone bone | B2 prone-bone | flat stomach, hips slightly raised |
| spoons POV | B2 spoon | side-lying intimate crop |
| against glass | against-glass | breasts/cheek to glass, city bokeh |
| ahegao still | L=ahegao | eyes roll, tongue, drool — **adult** |
| looking at viewer + act | L=eye-contact | 行为中盯镜 |

### 13.2 解剖 / 细节 LoRA 向 → 散文深度

| 社区训练焦点 | 正文写法（中近景） |
|--------------|-------------------|
| realistic labia / booty | outer labia shape, glute curve, thigh compression — 非空词 wet pussy |
| penis model | shaft, glans, root at junction, veins only if focused |
| wet skin / sweat | continuous specular, bead runnel |
| ruined makeup | mascara track, lipstick smear + fluid |
| ahegao realistic | fucked-silly face without cartoon unless anime-explicit |

**禁止：** 把 LoRA 名（`UberVag` 等）写进用户可见英文正文当魔法词。

### 13.3 站内高频机位标签 → 铁律

| 标签 | 用法 |
|------|------|
| from below / low angle | 最色开放默认友好；写 `looking slightly up` |
| from above | 脆弱/被观看；折叠压常用 |
| looking at viewer | 与口交/自展强绑定 |
| extreme close-up | 结合部/唇；声明主体 |
| cowboy shot | 中大腿；注意是否切掉关键连接 |
| wide shot | 词预算场先；细节降级 |

---

## 14. 2026 模型生态地图（.red 实操 · 提示策略）

> 社区指南共识（随时间变；**提示策略**稳定，具体模型名仅作路由参考）。

| 层 | 代表方向 | 本 skill 提示 |
|----|----------|----------------|
| **默认写实 NSFW** | Krea 2 + NSFW / refusal-reduction LoRA（.red） | **七层散文 + 连接整句**；LoRA 不替代描写 |
| **强编辑 / 文图** | Qwen-Image / Qwen Edit | 用户点名：指令清晰；`Change only pose/act; keep face` |
| **快模** | Z-Image Turbo 等 | 缩 L7；保 L3 连接 + L6 光 |
| **二次元 NSFW** | Illustrious 系 / Anima 等 | `anime-explicit` + **强制成人锁**；可混合短标签 |
| **硬核解剖补** | SDXL/Pony 二程 inpaint | 主图 Krea 构图 → 补丁句升 explicit；或用户点 Pony 短标签 |
| **视频** | Wan 等 I2V | 先静帧可读 → Motion 单动作 |

**两段式（社区高频 · 映射 skill）：**

```
Pass A（构图/情绪）：sensual 或 soft-explicit，姿与光正确，连接可隐
Pass B（露骨）：同一锁脸+场，只升级 L3 连接/E 级/体液句 → 形态 C 补丁或全文
```

本地 Comfy：**无云审核**；文案直接写满。NSFW LoRA = 工具能力，**不是**「少写连接」的借口。

---

## 15. Prompting Compass 深映射（色情）

| Compass 点 | erotic-prompt |
|------------|---------------|
| 一套提示通吃是神话 | 默认 Krea 句；Pony score **仅** Pony 底模 |
| 自然语胜复杂互动 | 双人/触手/群戏 **必须**句子连接 |
| 标签胜细碎零件 | 用户点 anime 短句时：act 标签译成句再嵌 Main |
| score 是审美拨盘不是万能质量 | 非 Pony **删除** score_* |
| 读 model card | 用户指定底模时遵守其触发；输出仍可四段自然语 |
| 坏 Remix 传播 | §1.1 清洗强制 |

**差 Remix → 好：**

差：
```
score_9, score_8_up, 1girl, nsfw, sexy, milf, doggy, creampie, masterpiece
```

好：
```
Main subject: An adult East Asian woman in her early twenties on all fours on rumpled hotel sheets, knees wide, ass raised, deep back arch; his erect penis buried to the hilt from behind, wet junction visible in the lower frame; her hands twist the sheet, cheek to pillow, mouth open, eyes half-lidded toward the camera. Thin sweat sheen on her back under warm tungsten from camera-left.
```

---

## 16. .red 样例题材壳（可点 · 与组合包对齐）

| ID | 触发 | 预填 |
|----|------|------|
| **red-hotel-tungsten** | 钨丝酒店 | E=hotel · 半褪 · tungsten · east-asian |
| **red-love-hotel-mirror** | 情趣镜 | love-hotel · mirror-sex · LED |
| **red-onsen-steam** | 温泉蒸汽 | onsen · wet · mixed-bath 可选 |
| **red-shower-tile** | 淋浴瓷砖 | shower · standing · water |
| **red-car-steam** | 车震蒸窗 | car · cramped · steamed glass |
| **red-window-city** | 窗边城市 | window · against-glass · exhibition |
| **red-office-blind** | 办公室百叶 | office-afterhours · blinds |
| **red-pov-bed** | 床上 POV | H=pov · 竖构图 |
| **red-gonzo-flash** | 业余直闪 | hard flash · amateur · photoreal |
| **red-anime-explicit** | 里番风 | anime-explicit · 成人锁 · max 可选 |
| **red-tentacle-altar** | 触手祭坛 | F3 · 默认 caress 除非点插入 |
| **red-succubus-ride** | 魅魔骑乘 | fantasy catalog |
| **red-oil-softbox** | 精油柔箱 | oil · wet-gloss · display |
| **red-bondage-soft** | 轻缚床头 | bondage · wrists · 美型绳 |

组合包：`combo-red-*` 与上表后缀一致；可与 combo-creampie-doggy 等叠（主包+≤1 修饰）。

---

## 17. 亚洲默认与站内偏差（色情）

| 现象 | 对策 |
|------|------|
| 未写人种 → 白人/混血脸 | 起句 `adult East Asian woman in her early twenties` |
| 部分模型磨皮网红 | `real pores, natural subsurface, sweat not plastic` |
| 二次元幼态漂 | mature face, adult proportions + 负向 teen/loli |
| 用户要其他族裔 | 覆盖，不叠东亚 |
| 「Japanese」标签站内极多 | 可写 Japanese/Korean/Chinese features **或** 泛 East Asian |

---

## 18. 联网 / 反推检索模板（.red 优先 NSFW）

```
site:civitai.red Krea2 NSFW prompt
site:civitai.red POV doggy OR cowgirl generation
site:civitai.com articles prompt guide score_9 OR natural language
site:civitai.com articles Krea2 zoom OR framing
site:civitai.red Illustrious OR Pony NSFW adult
```

用户丢链接 → 打开 Generation Data → §1.1。  
用户问「站内最近硬核热什么」→ 检索后 **静帧化**，禁止编造具体排名数字。

---

## 19. 冷门池加料（Civitai 向 · 成人）

1. 钨丝酒店后入中出（全身脚膝进画）  
2. POV 深喉泪光竖屏  
3. 骑乘女上盯镜  
4. 窗边贴玻璃城市光  
5. 淋浴站立水流  
6. 车内折叠肢体蒸窗  
7. 业余直闪乱床自慰  
8. 镜中双角度插入  
9. 百叶窗办公室半褪口侍  
10. 精油柔箱自展  
11. 轻缚腕上床头敞开  
12. 温泉蒸汽双人（成人）  
13. 触手撑开展示无插入  
14. 魅魔骑乘淫纹  
15. 里番 ahegao 折叠压 + 成人锁  
16. 颜射事后花妆  
17. 不对称半褪单袜  
18. 通话中压抑表情+插入  
19. 词预算房间尺度：门开撞见半裸  
20. 结合部特写方幅 + 主脸虚化可选  

抽取 → **prose-quality 全文 + 连接点**。

---

## 20. 组合包速查（本卷新增）

| combo | 触发 |
|-------|------|
| combo-red-hotel-tungsten | 钨丝酒店 |
| combo-red-love-hotel-mirror | 情趣镜 |
| combo-red-onsen-steam | 温泉蒸汽 |
| combo-red-shower-tile | 淋浴瓷砖 |
| combo-red-car-steam | 车震 |
| combo-red-window-city | 窗边城市 |
| combo-red-office-blind | 办公室百叶 |
| combo-red-pov-bed | 床上 POV |
| combo-red-gonzo-flash | 业余直闪 |
| combo-red-anime-explicit | 里番成人 |
| combo-red-oil-softbox | 精油柔箱 |
| combo-red-bondage-soft | 轻缚 |
| combo-zoom-fullbody-sex | 词预算全身性行为 |
| combo-zoom-mcu-face-breast | 词预算脸胸私房 |
| combo-pass-compose-then-explicit | 两段式：构图→露骨补丁 |

---

## 21. 点菜菜单（给用户）

```
**Civitai.red / .com 生态点菜（18+ · 本地 NSFW 写满）**

写法：Krea 七层自然语 · 禁 score 跨生态 · Remix 清洗
取景：词预算变焦（脸胸 / 半身 / 全身行为 / 房间偷情）
POV：口/后入/骑乘/传教士/乳/足… → 连接句不是标签
壳：钨丝酒店 · 情趣镜 · 温泉 · 淋浴 · 车震 · 窗边 · 办公 · 直闪业余 · 里番成人锁
工具层：Krea2 NSFW LoRA 可提；不替代连接点
两段式：先构图再升 explicit

例：`组合:钨丝酒店后入中出` / `组合:POV深喉` / `反推这条.red元数据` / `两段式先构图`
```

---

## 22. 与其它文件关系

| 文件 | 分工 |
|------|------|
| **本文件 §1–11** | 原生态：双站、PH、里番、摄影词、反模式 |
| **本文件 §12–21** | 2026 双站补强：变焦、POV 映射、模型地图、.red 壳 |
| connection-templates | 连接成句 |
| erotic-breadth-catalog | 主点菜 A–R |
| fantasy-erotic-catalog | 非现实全表 |
| asian-erotic-p0-p2 | 妆发锁脸分镜 |
| model-prompting-krea2-seedream | 篇幅与默认模型 |

**交付释义可写：**  
`**参考来源**：Civitai.red/.com 生态补强 2026（词预算变焦 · POV 概念静帧化 · Remix 清洗）`
