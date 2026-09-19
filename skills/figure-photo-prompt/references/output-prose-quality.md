# 输出正文质量规范（Output Prose Quality）— SFW 全谱人体摄影

本文件约束 **形态 A 英文四段** 与 **形态 B 短密** 的**文字本身**——把句子写到「模型能画、人能读、**题材逻辑**落地」。

**不是私房文案课。** 健身、街拍、芭蕾、工地、航拍各自有合格正文标准。  
适用于 **Krea 2** 与 **Seedream** 的形态 A（同一五标准）。  
**执行：** 六层完整句；**高密四段版式（段间空行）**；全文默认 **200–380** 词；Seedream 更精炼并可附 B。  
分层 → [`krea2-qwen-te-layered-prompting.md`](krea2-qwen-te-layered-prompting.md)

> **三 skill 统一版式（figure / youth / erotic）：**  
> `This is a…` 空行 `Main subject:` 空行 `Environmental background:` 空行 `Composition and atmosphere:`  
> 首句 = 角度+景别+画幅 + **with 摄影类型** + **定格瞬间**；Main 以 `An adult…` 多句全链；禁止短开篇、禁止四段粘连。

---

## 1. 正文质量五标准（强制自检）

| # | 标准 | 合格 | 不合格 |
|---|------|------|--------|
| 1 | **可视** | 每句能对应画面里一块像素 | “very beautiful”“stunning atmosphere” 空喊 |
| 2 | **具体** | 有可替换的名词/动词/方位 | “a woman posing” |
| 3 | **单帧** | 一个瞬间，无 then/after/begins to | 时间线剧本 |
| 4 | **姿态优先** | 重心 + 肩髋 + 手位可读 | 只写脸美环境大 |
| 5 | **密度** | 信息密、少水词 | 同义反复、标签刷屏 |

**水词黑名单（正文少用或不用）：**  
`beautiful, stunning, gorgeous, perfect, amazing, lovely, sexy, hot, elegant`（除非紧跟具体动作/材质）  
改写：`elegant` → `spine long, chin slightly lifted, fingers relaxed along the coat lapel`

---

## 2. 四段各自写什么（高密版式 · 强制）

### 2.0 版式合同（交付前勾选）

| # | 要求 | 不合格例 |
|---|------|----------|
| 1 | 四标签齐全、顺序固定 | 缺 Env；改名 Subject |
| 2 | **段间空一行** | 四段粘成一段 |
| 3 | 首句含 **angle+distance+aspect+with photography type** + **定格** | `This is an editorial still, nice pose.` |
| 4 | Main 以 `An adult…` 起，**≥3 句**全链 | 一句 “beautiful model posing” |
| 5 | Comp 含 **占框/尺度 + 主光落体积 + 质量词** | 只有 masterpiece |

### 2.1 `This is a …`（1 句，约 **35–70** 词）

**句模：**
```
This is a [angle] [distance] [aspect] [still] with [editorial / documentary / sports / beauty / street photography]: a photoreal adult [subject] frozen [action phase], [skin/fabric finish], [toward lens/task/audience].
```

```
This is an eye-level full-body vertical 3:4 editorial still with clean commercial fashion photography: a photoreal adult East Asian woman frozen as weight settles onto the back foot against pale seamless paper, soft product-clean skin, garment lines fully readable toward the lens.
```

差：`This is a beautiful photo of a stunning model posing.`

### 2.2 `Main subject:`（核心；**100–180** 词）

**推荐句序（随题材调整，多句全链）：**

1. **`An adult…` + 人种**（**未指定默认 `East Asian`**；用户覆盖）  
2. **发态 / 体型可读一句**  
3. **大姿势 / 动作相位 / 任务朝向**（不要无脑 S 线）  
4. **支撑与重心**（脚/坐骨/器械/岩点）  
5. **手位或工具**  
6. **服饰或装备精确**  
7. **材质 / 介质 / 训练痕迹**  
8. **表情与注意力方向**  
9. **可选 1 道具**

**动词要强：**  
`leans / shifts / twists / plants / elongates / frames / rests / grips / arches / steps`  
少用：`is being, looks beautiful, appears elegant`

**感官层次（每段至少 2 层）：**

| 层 | 例 |
|----|----|
| 形状/姿态 | soft S-curve, weight on back foot, elongated neck |
| 表面 | wool texture, matte jersey, fine dry skin sheen |
| 接触 | fingers hooked in pocket, palm on hip bone |
| 光在体积上 | key light sculpting the near cheek and collarbone |

### 2.3 第二人段（若有，约 30–70 词 · 独立段 + 空行）

只写：**相对位置 + 互动手势 + 距离**。  
禁止第二段再复述主脸长文。

```
Beside her, an adult man in a charcoal coat walks half a step behind, his near hand lightly at her elbow; only his torso and profile are readable, slightly softer in focus.
```

### 2.4 `Environmental background:`（约 **40–80** 词）

**2～5 个锚点**，服务主体，不装修；可用 em-dash 串特质：

- 墙/窗/街/器材 各最多一句特质  
- 时代杂物最多 1 个  
- 避免逐件描写品牌与地毯花纹  

### 2.5 `Composition and atmosphere:`（约 **40–75** 词）

必须有：

1. **占框 / 人与环境尺度**  
2. 绝对视觉中心（脸 / 身姿线 / 服装廓形）  
3. **主光 + 可选 fill/rim**，落在体积上  
4. 景深与虚化对象  
5. 一句情绪/叙事张力 + 色盘  
6. 质量词 + 静帧类型：`masterpiece, best quality, photoreal editorial still`

---

## 3. 可画清单（写完对照）

Main subject 写完后，应能勾选 ≥6 项：

- [ ] 年龄/成人身份  
- [ ] **人种：默认 East Asian，或用户指定**  
- [ ] 头～哪一截身体在画内  
- [ ] 重心落在哪只脚（或坐姿承重点）  
- [ ] 肩与髋的相对朝向  
- [ ] 手在做什么  
- [ ] 服饰材质 + 一个细节  
- [ ] 表情/眼神  
- [ ] 主光打在哪块体积  
- [ ] （全身时）脚是否在画内  

缺 3 项以上 → 正文不合格，补写再交付。

---

## 4. 差 → 好（正文改写示例）

### 4.1 空泛时尚

**差：**
```
Main subject: A beautiful Asian girl in a nice outfit posing elegantly, stunning, masterpiece.
```

**好：**
```
Main subject: A young East Asian woman in her early twenties stands full-body in frame; long straight black hair falls behind one shoulder. Weight rests on her back leg, front knee soft, near shoulder angled toward the camera while the opposite hip gently pops, forming a soft S-curve. One hand rests lightly on her hip, the other hangs relaxed with fingers slightly curled. She wears a camel wool coat over a black knit turtleneck and straight trousers; the coat hangs open, belt loose. Calm eyes meet the lens, mouth soft, chin slightly lifted under clean butterfly-soft key light.
```

### 4.2 有姿势但不可读

**差：**
```
She is standing in a cool pose in the gym looking strong.
```

**好：**
```
She plants a wide athletic stance in the gym, front knee bent in a controlled lunge, back leg long; torso upright, shoulders stacked over hips. Both hands grip a barbell at hip height, knuckles forward. A matte black sports bra and high-waist training shorts read clearly; a fine sweat sheen catches hard side light along her deltoid and oblique. Focused eyes look past the camera, jaw set without grimace.
```

### 4.3 环境抢戏

**差：** 200 词描写咖啡馆菜单与墙纸。  
**好：** 人物 70% 篇幅；环境只留 large window, pale wall, wood table edge, soft city bokeh。

---

## 5. 节奏与长度

| 段 | 建议 | 句数 |
|----|------|------|
| This is a | **35–70** | 1 |
| Main subject | **100–180** | **3–8** |
| 额外角色 | 25–55 | 1–2 |
| Environment | **40–80** | 2–3 |
| Composition | **40–75** | 2–3 |
| **全文默认** | **200–380 词** | — |
| **再长则压缩** | 约 **420** 词起先砍 Env/重复 | — |

- 偏短缺重心/光 → **补层**，不补水词。  
- 偏长 → 砍装修与重复，**勿砍姿态/主光**。  
- Seedream：A 可；鼓励 B（约 30–100 / 5.x 约 50–150 词）。  
- Main 须可指认 **动作 + 材质≥1 + 光落点**。

---

## 6. 中文释义质量

中文不是英文机翻，而是**用户可读的导演/摄影师说明**：

| 条 | 要求 |
|----|------|
| **本次分支/组合包** | 一行点名 |
| **镜头** | 角度景别画幅，人话 |
| **主体** | 重心→肩髋→手→衣→表情，与英文同构 |
| **勿** | 大段重复英文专有名词不解释 |
| **可** | 点明「防崩：一手插袋」「光：窗光主+脸亮」 |

释义长度：英文的 40–70%，清楚即可。

---

## 7. 形态 B 短密质量

```
eye-level full-body vertical, adult East Asian woman early twenties, long black hair, weight on back foot soft front knee S-curve, hand on hip, camel wool coat open black turtleneck, calm eye contact, white seamless studio, soft butterfly key, editorial still, highly detailed fabric
```

形态 B 同样：**未指定人种时保留 East Asian / Asian adult**，禁止默认 Caucasian/white。

禁止：
```
1girl, beautiful, masterpiece, best quality, elegant
```

---

## 8. 交付前正文质检（勾选）

- [ ] 无水词堆砌  
- [ ] 有强动词与方位  
- [ ] 单帧无 then  
- [ ] 有重心与肩髋关系  
- [ ] 成人身份明确  
- [ ] 人种已写（默认东亚 / 用户覆盖）  
- [ ] 服饰状态精确  
- [ ] 主光方向可读  
- [ ] 篇幅约 200–380 词（或 B / ≤约 420 词）  
- [ ] **四段空行 + 首句摄影类型 + Main 全链**  
- [ ] 动作与主光未因压缩丢失  
- [ ] 中文释义同构且可读  
- [ ] SFW，无色情升级  
- [ ] 无 score_9 / hashtag 墙  

---

## 9. SFW 人体摄影词库（优先用这些）

### 9.1 姿势 / 重心

`weight on the back foot` · `front knee soft` · `hip gently popped` · `soft S-curve` · `three-quarter angle to camera` · `spine long` · `chin slightly lifted` · `mid-stride` · `seated on the edge` · `one sole against the wall` · `contrapposto`

### 9.2 手 / 肢体

`one hand in the pocket` · `fingers lightly on the hip` · `hand resting on the railing` · `arms relaxed at her sides` · `holding the strap of a bag` · `elbows soft not locked` · `negative space between arm and torso`

### 9.3 服饰 / 材质

`camel wool coat hanging open` · `sharp tailored lapel` · `matte jersey cling of a sports top` · `pressed crease of trousers` · `knit texture catching side light` · `silk drape` · `wind lifting the hem`

### 9.4 表情

`calm eyes meet the lens` · `soft half-smile` · `gaze toward the key light` · `focused athletic concentration` · `candid mid-expression` · `looking over the near shoulder`

### 9.5 光（写在体积上）

`soft window key on the near cheek` · `Rembrandt triangle under the far eye` · `butterfly light under the nose` · `hard side light defining the deltoid` · `rim light separating hair from backdrop` · `golden hour warm key, long soft shadows`

### 9.6 空词 → 落地改写

| 空 | 落地 |
|----|------|
| beautiful | clear facial structure under soft key, calm open expression |
| elegant pose | weight back, elongated neck, soft S-curve through torso |
| cool outfit | camel wool coat, black turtleneck, straight trousers, leather boots |
| good lighting | large soft key from camera-left, gentle fill, hair rim |
| strong body | defined shoulders and core under hard side light, athletic stance |

---

## 10. 完整金样（多题材 · 质量标杆）

### 10.1 时尚棚拍（A · **高密版式金样**）

```
This is an eye-level full-body vertical 3:4 editorial still with clean commercial fashion photography: a photoreal adult East Asian woman frozen as weight settles onto the back foot against pale seamless paper, soft product-clean skin, garment lines fully readable toward the lens.

Main subject: An adult East Asian woman in her early twenties—adult face and proportions, warm-neutral East Asian undertone, healthy matte skin finish. Long black hair tucked behind one ear. She stands fully in frame: weight on the back leg, front knee soft, near shoulder angled to camera, opposite hip gently popped — soft S-curve, spine long, chin slightly lifted. Right hand rests on the hip bone, left hangs relaxed with a slim light gap under the arm. Camel wool coat open over black turtleneck and charcoal trousers; leather ankle boots planted, feet in frame. Calm eyes meet the lens, mouth soft, editorial not coy.

Environmental background: Endless pale gray seamless—faint floor seam, no clutter, commercial clean field.

Composition and atmosphere: Subject fills most of the vertical frame with thin studio margin; visual center on the shoulder-to-hip S-curve and coat structure; soft key front-left, gentle fill, thin hair rim; polished catalog grade; masterpiece, best quality, photoreal editorial fashion still.
```

### 10.2 环境职业人像（B/E）

```
This is an eye-level environmental medium-wide shot in horizontal framing with documentary photography language, freezing a focused moment at a stainless steel workbench under cool lab lighting.

Main subject: An adult woman in her thirties, hair tied back, stands three-quarter to camera but oriented primarily to the bench. Weight even on both feet in closed-toe shoes; torso slightly leaned in. Both gloved hands steady a pipette over a rack of vials; safety goggles rest on her forehead, lab coat sleeves pushed once. Expression focused on the vials, mouth neutral — not a commercial smile.

Environmental background: White lab benches, a fume hood edge, muted equipment LEDs, one window strip of daylight at rear; clean but lived-in lab, no clutter chaos.

Composition and atmosphere: Figure and workspace share the frame roughly equally; visual center at hands-and-vials; cool fluorescent mix with window fill; documentary still, credible occupational portrait; masterpiece, best quality, highly detailed hands and materials.
```

### 10.3 运动腾空（C）

```
This is a low side-angle full-body sports freeze in horizontal framing with fast-shutter athletic photography, catching the airborne apex of a stride on an outdoor track.

Main subject: An adult male runner in his mid-twenties, lean athletic build, short hair. Body fully airborne: rear leg extended long, front knee driving high, opposite arm forward, free arm back; torso slight forward lean, core braced. Moisture-wicking singlet and split shorts read clearly; trail racing shoes pointed. Face focused forward down the lane, effort controlled not grimacing. Fine sweat sheen on shoulders under hard sun.

Environmental background: Red track lanes receding, white lane numbers soft, empty stands blurred, bright sky.

Composition and atmosphere: Diagonal force line through the body; leave space ahead of his motion; hard sun high-right, crisp shadow language on track; sharp limbs, sports editorial still; masterpiece, best quality, highly detailed muscle and motion freeze.
```

### 10.4 芭蕾排练（D）

```
This is an eye-level full-body shot in vertical framing inside a rehearsal studio, freezing a held arabesque with clear ballet structure.

Main subject: An adult female dancer in her twenties, hair in a neat bun. Supporting leg turned out and straight on flat or demi, working leg extended behind in arabesque above ninety as ability allows, hips square as possible, spine long, arms in a readable third-port-de-bras shape with finished fingers. Pale leotard and soft practice skirt, worn ballet slippers; light rosin dust near the supporting foot. Gaze over the front hand, calm performance focus.

Environmental background: Mirrored wall with barre, wood floor scuffs, cool daylight from high windows, empty studio depth.

Composition and atmosphere: Full limb line in frame including working foot; side window key sculpting the extended leg; clean rehearsal documentary-editorial hybrid; masterpiece, best quality, highly detailed posture line.
```

### 10.5 航拍点景（H）

```
This is an extreme high-angle aerial wide shot in horizontal framing, freezing a solitary hiker as a tiny mark on a pale dune ridge under clear desert light.

Main subject: A minuscule adult human figure reduced to a dark upright shape with a small backpack silhouette; walking posture implied by a slight forward lean — no face, no fingers, no clothing brand detail readable at this scale.

Environmental background: Wind-carved dune ridges, long sun shadows raking the sand, distant haze horizon, empty sky.

Composition and atmosphere: Terrain dominates; figure placed on a third intersection of the ridge line for scale poetry; natural hard sun; landscape-with-figure still; masterpiece, best quality, highly detailed sand texture.
```

---

## 11. 正文骨架（按大区填空）

### 11.1 时尚全身（A）
```
…freezing [weight on back foot / mid-stride].
Main subject: [ID]. [line/pose for garment]. [hands]. [outfit structure detail]. [face editorial].
Env: [seamless or street anchors].
Comp: [garment line center] [key] [DOF].
```

### 11.2 环境/职业（B/E）
```
…freezing [task moment].
Main subject: [ID]. [body oriented to task]. [tool hands]. [uniform/PPE]. [gaze on work].
Env: [workplace 3 anchors].
Comp: [figure≈place] [available light].
```

### 11.3 运动相位（C）
```
…freezing [airborne / lockout / three-point].
Main subject: [ID athletic]. [support + force vector]. [gear]. [effort face].
Env: [field/gym/track].
Comp: [motion space ahead] [hard or venue light].
```

### 11.4 舞蹈（D）
```
…freezing [named shape].
Main subject: [support vs working leg]. [port de bras / floor contact]. [costume]. [gaze].
Env: [studio/stage].
Comp: [full distal limbs] [side or spot].
```

### 11.5 艺术剪影/明暗（F）
```
…freezing [still sculpture moment].
Main subject: [volume / outline / limbs separated].
Env: [single field of light or dark void].
Comp: [shape first] [chiaroscuro or backlight].
```

### 11.6 私房（I · 仅点名 · SFW）
```
…freezing [relaxed seated/standing at home].
Main subject: [clothed or user-specified non-explicit]. soft natural pose — no sexual act language.
Env: [home window, not porn set].
```

### 11.7 舞台色光（D）
```
…freezing [lyric peak / gesture].
Main subject: [mic or prop contact]; [stage body line]; gel color on skin; sweat optional athletic.
Env: [black void or LED wall bokeh].
Comp: [expose for spot on face]; saturated gels OK.
```

### 11.8 攀岩伸展（C）
```
…freezing [dynamic reach].
Main subject: [outstretched limbs all readable]; [chalk]; [hips off wall].
Env: [rock texture raking light]; scale of wall.
```

### 11.9 短光修正肖像（A）
```
…freezing [still portrait].
Main subject: [three-quarter]; short lighting; weight back; lean from waist; neck long.
Env: [simple studio].
```

### 11.10 亚洲年轻女 · 日系空气（成人）
```
This is an eye-level medium shot in vertical framing with airy Japanese lifestyle portrait photography, freezing a soft glance in backlit afternoon light.

Main subject: An adult East Asian woman in her early twenties, long straight black hair with sunlit rim, fair dewy skin. Weight on her back foot beside a large window; front knee soft; one hand lightly holds a canvas tote strap. Ivory knit cardigan over a white shirt. Eyes soft to lens, tiny natural smile, clearly adult facial proportions. Fine hair strands catch backlight.

Environmental background: Sheer curtain, pale wall, outdoor green bokeh, gentle controlled lens flare.

Composition and atmosphere: Airy negative space camera-left; backlight rim on hair, soft fill on face; dreamy shallow DOF; masterpiece, best quality, natural East Asian skin undertone.
```

### 11.11 韩系松弛街拍（成人）
```
…freezing mid-stride on a city sidewalk.
Main subject: adult East Asian woman mid-twenties; songchi weight on one hip; glass-skin soft; oversized blazer + clean tee; gaze slightly past camera.
Env: gray building, soft open shade.
Comp: full-body street, even daylight.
```

年轻亚洲女词库与年龄锁 → [`young-asian-women-catalog.md`](young-asian-women-catalog.md)

---



### 11.12 韩系概念色块（成人）
```
This is an eye-level medium shot in vertical framing with Korean concept studio photography, freezing a composed stare against a single color field.

Main subject: An adult East Asian woman in her mid-twenties, sleek dark hair, glass-skin dewy finish with soft glam. Shoulders angled, chin level, one hand lightly at blazer lapel. Color-blocked tailored look matching the set. Cool editorial eyes to lens, no wide smile, clearly adult.

Environmental background: Seamless color wall, minimal prop, clean floor line.

Composition and atmosphere: Centered magazine crop; soft frontal key + subtle gel rim; polished concept still; masterpiece, best quality.
```

### 11.13 江南旅拍（成人）
```
…freezing mid-step on wet stone by a garden corridor.
Main subject: adult East Asian woman early twenties; three-quarter gaze off camera; light modern-traditional dress; soft overcast; slight wind in hair.
Env: lattice window, water reflection, grey tiles.
Comp: corridor leading lines; muted Jiangnan palette.
```

东亚写真体系 → [`east-asian-portrait-systems.md`](east-asian-portrait-systems.md)



### 11.14 OOTD 街拍（社交竖图）
```
This is an eye-level full-body shot in vertical 3:4 social framing with street style photography, freezing a relaxed OOTD moment on a city sidewalk.

Main subject: An adult East Asian woman in her early twenties stands with weight on the back foot, free knee soft, near shoulder to camera. One hand holds a coffee, the other rests on a shoulder bag strap. Cream blazer, white tee, straight jeans, sneakers — outfit fully readable. Soft smile, gaze slightly past lens. Feet near the bottom of the frame.

Environmental background: Shop glass bokeh, pavement, one street tree, open shade.

Composition and atmosphere: Xiaohongshu-style vertical still; open shade even light; candid not stiff; masterpiece, best quality, highly detailed fabric.
```

### 11.15 全身镜自拍
```
…vertical mirror selfie, adult woman mid-twenties, phone visible at chest in reflection, free hand on hip, full lounge-chic outfit, clean bedroom mirror, soft window fill, SFW Instagram lifestyle.
```

### 11.16 窗边私房软 SFW
```
…soft home portrait, adult woman early twenties on bed edge by large window, oversized knit and pants fully covering, morning window key, gaze to light, clean sheets, youthful-adult quiet mood, no nudity.
```

社交形态全谱 → [`social-lifestyle-portrait.md`](social-lifestyle-portrait.md)

## 12. 中文释义金样结构

```
---
**中文释义**

**本次分支/组合包**：editorial · S 线 · 棚拍白/灰无缝
**镜头与风格**：竖幅、平视、全身、浅景深、时尚编辑静帧
**主体**：二十出头东亚女性…（重心→肩髋→手→衣→表情）
**环境背景**：灰无缝、地面弱缝（2～4 点）
**构图与氛围**：视觉中心在身姿 S 线；前左柔光；干净商业感
**画幅建议**：竖 3:4
```


---

## 14. 一套写真分镜（形态 E）

模板与连续锁 → [`asian-young-woman-p0-p2.md`](asian-young-woman-p0-p2.md) §P0-④ · §P2-⑯  

每 Shot 仍过五标准；系列前置身份+人种+发色锁。
