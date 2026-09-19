# 亚洲年轻女主体 · P0–P2 全补齐卷

> **主体默认：`adult East Asian woman` + 年龄带 early/mid/late twenties。**  
> **SFW · 18+。** 本卷解决「稳出片」层：妆发场景、修型、道具手、分镜、肤光、表情、调色、封面、配件、C 位双人、运动职场、连续锁脸与负向。  
> 与 `young-asian-women-catalog` / `style-packs` / `social-lifestyle` 正交叠用。

---

# P0-① 妆发 × 场景矩阵

| 场景 ID | 触发 | 妆 | 发 | 禁 |
|---------|------|-----|-----|-----|
| **mk-commute** | 通勤、上班 | 淡底、薄眉、唇豆沙雾面 | 低马尾/半扎/黑长直顺 | 浓烟熏、假睫毛刷屏 |
| **mk-date** | 约会 | 轻修容、水光唇、卧蚕轻 | 微卷披肩、一侧耳后 | 舞台妆 |
| **mk-id** | 证件/简历 | 自然大地、内眼线浅、唇自然 | 露耳、刘海勿遮眉眼 | 夸张修容、闪片 |
| **mk-flash-night** | 夜闪/Y2K/派对 | 可略重眼线、高光鼻梁 | 略乱有型、湿发可选 | 幼态妆 |
| **mk-sport** | 运动 | 近素颜、防晒感 | 高马尾/发带 | 浓妆易花写「花妆」除非要 |
| **mk-weimei** | 唯美/花海 | 柔粉、水光 | 披发风 | 冷艳浓黑 |
| **mk-qingleng** | 清冷 | 雾面、少红 | 中分直长 | 甜美腮红过重 |
| **mk-om** | 名媛 | 干净精致、唇豆沙 | 低盘/吹直 | Y2K 闪片 |
| **mk-kr-glass** | 韩系水光 | glass skin、横扫腮红 | 空气刘海/丝滑直 | 哑光假白 |
| **mk-jp-natural** | 日系 | 低饱和、咬唇 | 自然碎发 | 欧美深修容 |
| **mk-home-soft** | 私房软/居家 | 近素、唇润 | 随意半扎 | 全妆隆重 |
| **mk-travel** | 旅拍 | 耐看淡妆、防汗 | 防风造型（半扎） | 易花浓妆 |

**写入 Main：** 妆发各 **1 句**，勿堆全脸步骤。  
例：`natural commute makeup, soft matte lips, low ponytail with clean face line`

---

# P0-② 东亚年轻女 · 比例与修型（提示词层）

| 目标 | 英文种子 | 适用 |
|------|----------|------|
| 显脸小（自拍） | slight high angle, chin gently forward, shoulders drop | 自拍 mcu |
| 显腿长（全身） | slight low angle full body, weight on back foot, high-waist line clear, feet in frame | 街拍 |
| 显瘦肩 | three-quarter body, near shoulder closer, soft gap under arm | 通用 |
| 圆脸友好 | short lighting optional, chin soft-forward, hair frame cheeks lightly | 半身 |
| 娇小比例 | adult petite frame with adult facial proportions — not childlike; avoid huge head crop | 全身略远或环境 |
| 高瘦线条 | elongated limbs, vertical composition, long coat unbroken line | editorial |
| 防头大身小 | do not crop at elbows; show waist or use true full-body; match shot size | 中景 |
| 颈长干净 | elongate neck, shoulders down, chin off neck | 近景 |
| 坐姿显腿 | perch seat edge, one leg extended or ankles cross, spine long | 椅/台阶 |

**禁止：** 用幼态大眼小脸暗示未成年；娇小说 `petite adult` 必须 adult face。

```
proportion lock: adult East Asian woman early twenties, adult facial proportions, elongated neck, three-quarter slim read, high-waist visible, feet in frame on full body
```

---

# P0-③ 道具与手位专库（女主）

| 道具 ID | 触发 | 手位英文（防崩） |
|---------|------|------------------|
| **prop-boba** | 奶茶、饮料 | both hands on cup at chest height, straw optional, fingers soft not fused |
| **prop-phone** | 手机 | one hand holding phone natural, screen toward or away |
| **prop-bag** | 包 | one hand on strap at shoulder, or both on bag front |
| **prop-camera** | 相机 | camera strap neck, hands on body lightly |
| **prop-keys** | 钥匙 | keys in one hand at hip |
| **prop-book** | 书 | book half-open at chest or lap |
| **prop-umbrella** | 伞 | canopy above, one hand on handle |
| **prop-earphones** | 耳机 | buds in, wire optional, hand adjust one bud |
| **prop-coffee** | 咖啡 | two hands wrap cup, steam soft |
| **prop-skate** | 滑板（可选） | board vertical beside leg, one hand top |
| **prop-flower** | 小花束 | bouquet at waist, stems visible |
| **prop-helmet** | 骑行盔 | helmet in hand at hip, not always worn |
| **prop-laptop** | 笔电 | cafe table, hands on keys mid-type freeze |
| **prop-none** | 空手 | pocket / hair tuck / rail — 仍写清 |

**规则：** 一帧 **1 主道具**；双手同时高难交互宁可不写。

---

# P0-④ 一套写真分镜模板（形态 E）

用户说「一套」「一组 N 张」「约拍流程」→ 输出 **Shot 1…N**，每张单帧全文或短密；**连续锁**见 P2。

## 模板 A · 日系/小清新 6 张

| Shot | 内容 | 景别 | 风格壳 |
|------|------|------|--------|
| 1 | 窗边半身空气 | mcu | jp-airy |
| 2 | 全身街拍中步 | full | street OOTD |
| 3 | 倚墙或门框 | mls | songchi |
| 4 | 特写表情 | cu | natural makeup |
| 5 | 生活道具（咖啡/书） | ms | lifestyle |
| 6 | 远景小人或背影 | ws | environment |

## 模板 B · 韩系概念 6 张

| Shot | 内容 |
|------|------|
| 1 | 棚拍水光头肩 |
| 2 | 色块全身站姿 |
| 3 | 坐姿编辑 |
| 4 | 侧面轮廓 |
| 5 | 道具/包特写含人 |
| 6 | 动态中步或回眸 |

## 模板 C · 旅拍地标 8 张

| Shot | 内容 |
|------|------|
| 1 | 地标全身尺度 |
| 2 | 中步 OOTD |
| 3 | 不看镜看景 |
| 4 | 半身窗/廊 |
| 5 | 特写 |
| 6 | 生活碎片（吃/坐） |
| 7 | 夜景或黄金时刻 |
| 8 | 背影或剪影 |

## 模板 D · 私房软 SFW 5 张

窗边坐 → 床沿 → 沙发 → 居家全身镜（着装完整）→ 脸部柔光特写  

## 模板 E · 证件+形象 3 张

证件正面 → 简历浅笑 → 半身办公室虚化  

**每 Shot 输出格式：**
```
### Shot k/N · [一句话]
[形态 A 四段 或 形态 B]
**连续锁**：…
```

---

# P0-⑤ 亚洲肤色与白平衡

| ID | 触发 | 英文 |
|----|------|------|
| **skin-warm-neutral** | 默认暖中性 | warm-neutral East Asian undertone, not orange spray-tan |
| **skin-fair-clear** | 冷白通透 | fair clear East Asian skin, natural not chalky |
| **skin-deeper** | 深一度 | deeper East Asian melanin, expose for face |
| **skin-glass** | 水光 | dewy glass specular on cheeks and nose bridge, healthy not oily-erotica |
| **skin-soft-matte** | 哑光 | soft-matte with subtle real pores |
| **wb-daylight** | 日光 | true daylight white balance, natural skin |
| **wb-shade** | 阴影 | open shade, avoid green cast on skin |
| **wb-flash** | 闪光 | flash-balanced face, ambient color behind ok |
| **wb-neon-mix** | 夜霓虹 | mixed WB storytelling, face still readable |
| **avoid-cast** | 反模式 | no sickly yellow-green cast, no plastic porcelain doll skin |

```
skin lock: warm-neutral East Asian undertone, realistic fine texture, true-to-life white balance, expose for facial midtones
```

---

# P1-⑥ 表情微库（女主 × 风格）

| ID | 表情 | 英文 | 宜搭风格 |
|----|------|------|----------|
| **ex-soft-smile** | 浅笑 | soft closed or slight open smile, eyes gentle | 日系、小清新、生活 |
| **ex-mute-lips** | 抿唇 | lips softly pressed, calm | 名媛、清冷 |
| **ex-look-away** | 看远 | gaze off-frame into light or street | 旅拍、电影 |
| **ex-cool-stare** | 冷眼 | direct cool eye contact, minimal smile | 韩概念、Y2K、暗黑 |
| **ex-half-laugh** | 中途笑 | mid soft laugh, candid imperfect | 生活、抓拍 |
| **ex-chin-down-eyes-up** | 低头抬眼 | chin down, eyes lift to lens | 美妆、私房软 |
| **ex-neutral-id** | 证件中性 | neutral professional, eyes sharp | 证件 |
| **ex-wind-squint** | 风中微眯 | soft squint, hair motion | 天台、海边 |
| **ex- comm mute** | 通勤淡 | blank-soft commute face | 地铁 |
| **ex-focus-task** | 专注 | looking at phone/book/work | 生活职场 |

---

# P1-⑦ 调色包（Composition 末句 1 个）

| ID | 触发 | 英文 |
|----|------|------|
| **grade-jp-cream** | 日系奶油 | low-sat cream-green grade, airy highlights |
| **grade-kr-clean** | 韩系干净 | clean bright midtones, fresh skin |
| **grade-qingleng** | 清冷 | cool muted cyan-gray, low contrast |
| **grade-flash-pop** | 直闪高饱和 | punchy flash contrast, vivid ambient |
| **grade-portra** | 胶片肤 | Portra-like warm skin, soft grain |
| **grade-cine-teal** | 电影青橙轻 | subtle teal shadows, warm skin (soft) |
| **grade-bw-rich** | 黑白 | rich midtones, deep blacks |
| **grade-night-neon** | 夜霓虹 | mixed neon color bleed |
| **grade-old-money** | 静奢 | clean neutral, restrained saturation |
| **grade-iphone** | 手机自然 | natural HDR phone look |

**规则：** 一帧 **1 个** grade，勿三四个滤镜叠。

---

# P1-⑧ 小红书封面构图

| 规则 | 英文 |
|------|------|
| 画幅 | vertical 3:4 Xiaohongshu cover frame |
| 脸位 | face in upper-middle third, not glued to top edge |
| 留白 | small negative space for optional title (no forced text unless user asks) |
| 安全边 | subject not touching frame edges; feet room on full body |
| 主体大 | heroine fills interest, background simplified |
| 清晰 | sharp eyes, readable outfit color |

```
composition: 3:4 vertical cover layout, face upper third, clean negative space top or side, high clarity subject, Xiaohongshu thumbnail readable
```

---

# P1-⑨ 配件：眼镜 / 口罩 / 耳机

| ID | 触发 | 英文要点 | 注意 |
|----|------|----------|------|
| **acc-glasses** | 眼镜 | thin metal or clear frame glasses, catchlight in eyes through lenses | 控反光：`minimal glare on lenses` |
| **acc-sunglasses** | 墨镜 | sunglasses on face or pushed to hair | 夜闪可戴 |
| **acc-mask-sfw** | 口罩 | soft-colored mask covering nose-mouth, eyes expressive | 仅用户要；非医用惊悚 |
| **acc-buds** | 无线耳机 | white buds visible | 通勤 |
| **acc-neck-phones** | 颈挂耳机 | headphones around neck | 双手自由 |
| **acc-airpods-case** | 盒在手 | case in hand | 生活 |
| **acc-watch** | 手表 | watch on wrist mid-gesture | 名媛/通勤 |
| **acc-scarf** | 丝巾 | silk scarf at neck | 法式 |

---

# P1-⑩ 女主 C 位 · 男配 / 宠物

## 女主 + 男配

```
heroine priority: adult East Asian woman sharp in focus fills primary frame; adult East Asian man secondary softer or partial body, one clear contact (elbow/hand), never equal face detail unless user wants duo equal
```

| 模式 | 写法 |
|------|------|
| **hero-blur-him** | 男配肩/手入画，脸虚或出画 |
| **hero-walk-lead** | 女主略前，男后半步 |
| **hero-look-cam** | 女看镜，男看她 |

## 女主 + 宠物

```
adult East Asian woman with small dog/cat in arms or on leash, animal secondary, her face primary, park soft light, SFW tender, animal calm
```

禁：伤害动物、恐怖。

---

# P1-⑪ 运动线（年轻女）

| ID | 触发 | 姿+光 |
|----|------|-------|
| **sp-yoga** | 瑜伽 | named long line, soft side light, adult calm |
| **sp-pilates** | 普拉提 | core control, clean studio |
| **sp-run** | 跑步 | airborne or support phase, morning |
| **sp-tennis** | 网球 | ready stance racket, club soft |
| **sp-cycle** | 骑行 | bike pose, helmet hand or worn |
| **sp-hike** | 徒步 | trail mid-step, pack |
| **sp-swim-sfw** | 泳（用户点） | athletic suit non-explicit, pool light |
| **sp-gym-mirror** | 健身镜 | form check, sportswear |
| **sp-stretch** | 拉伸 | lunge stretch, park |

妆用 **mk-sport**；肤可微汗 `fine sport sheen` 非情色油光。

---

# P1-⑫ 职场年轻女

| ID | 触发 | 场景锚 | 姿 |
|----|------|--------|-----|
| **wk-commute-full** | 通勤全身 | metro rail, tote | 拉环/看手机 |
| **wk-desk** | 工位 | monitor glow, desk | 侧脸看屏 |
| **wk-meeting** | 会议室 | glass room, notebook | 坐姿脊直 |
| **wk-overtime-window** | 加班窗 | night city window | 持杯看外 |
| **wk-elevator** | 电梯 | mirror steel | 松弛站 |
| **wk-coffee-run** | 楼下咖啡 | cup, office plaza | 中步 |
| **wk-blazer-portrait** | 西装半身 | seamless or office | 形象浅笑 |

妆 **mk-commute**；服 blazer + trousers/skirt midi。

---

# P2 · 低优先补齐

## P2-⑬ 二线地标快表（可画一句）

| 城 | 锚 |
|----|-----|
| 南京 | confucius temple lanterns / city wall ginkgo |
| 苏州 | garden lattice / Pingjiang canal |
| 武汉 | East Lake willows |
| 长沙 | IFS climbing building night |
| 厦门 | Gulangyu slope / coastal road |
| 西安 | city wall ramp / Datang night |
| 重庆 | Hongyadong gold night / Liziba train |
| 成都 | Kuanzhai / Taikoo Li |

详城 → `city-landmarks-cn.md`

## P2-⑭ 婚礼宾客 / 伴娘（薄）

```
wedding guest SFW: adult East Asian woman, elegant midi dress, soft smile, ceremony garden bokeh, not the bride unless user says, bouquet optional small
```
```
bridesmaid group: heroine sharp center, other adult bridesmaids softer matching dresses
```

## P2-⑮ 乐器 / 画室 / 工作室

| ID | 英文 |
|----|------|
| **art-violin** | violin under chin or at rest, practice room window |
| **art-piano** | seated at piano, hands on keys freeze |
| **art-guitar** | acoustic guitar lifestyle sit |
| **art-paint** | easel, brush in hand, stained apron soft |
| **art-desk-create** | tablet/stylus, creative desk lamp |

## P2-⑯ 连续锁脸 Checklist（系列必写）

释义固定一行：
```
**连续锁**：East Asian · early twenties · [发色发型] · [脸型关键词] · [痣/牙/眼镜] · [体型] · photoreal
```

Main 前置重复：发色、眼型一句、是否眼镜、体型。  
变：仅姿/场/光/服。

## P2-⑰ 女脸/手负向要点（形态 D）

```
**Negative 要点（亚洲年轻女稳像）**：
child, teen, loli, baby face aged-down,
extra fingers, fused fingers, bad hands holding cup,
asymmetric creepy eyes, cross-eye, tooth mush,
plastic doll skin, yellow-green skin cast, orange tan,
extra limbs, warped fisheye face,
text, watermark, logo spam,
nsfw, nude（若要求着装）
```

按场景加减：有奶茶加 `melting cup into hand`；有眼镜加 `opaque lens glare hiding eyes`。

---

# 组合包速查（本卷）

| combo | 内容 |
|-------|------|
| **combo-mk-commute-metro** | 通勤妆+地铁 |
| **combo-mk-date-window** | 约会妆+窗 |
| **combo-prop-boba-street** | 奶茶街拍 |
| **combo-session-jp6** | 日系6张分镜 |
| **combo-session-kr6** | 韩系6张 |
| **combo-session-travel8** | 旅拍8张 |
| **combo-session-home5** | 私房软5张 |
| **combo-cover-xhs** | 小红书封面构图 |
| **combo-hero-pet** | 女主+宠物 |
| **combo-hero-male-soft** | 女主C位男配虚 |
| **combo-sp-yoga** | 瑜伽 |
| **combo-sp-run** | 跑步 |
| **combo-wk-overtime** | 加班窗 |
| **combo-wk-blazer** | 西装形象 |
| **combo-acc-glasses** | 眼镜人像 |
| **combo-guest-wedding** | 婚礼宾客 |
| **combo-art-piano** | 钢琴 |
| **combo-lock-series** | 强制连续锁输出 |

---

# 交付自检（亚洲年轻女主体）

**P0**
- [ ] 妆发匹配场景矩阵 1 句  
- [ ] 比例/修型种子（自拍俯/全身仰等）  
- [ ] 道具手清晰或明示空手  
- [ ] 多图则 Shot 分镜+连续锁  
- [ ] 肤色 undertone + 白平衡  

**P1**
- [ ] 表情匹配风格  
- [ ] 调色包 ≤1  
- [ ] 封面需求则 3:4 构图句  
- [ ] 配件反光/口罩规则  
- [ ] 双人时女主 C 位  

**P2**
- [ ] 系列锁脸完整  
- [ ] 需要时附 Negative 女脸要点  

---

# 点菜

```
**亚洲年轻女 · 出片层点菜**
妆发场景：通勤/约会/证件/夜闪/运动/韩水光/日系…
修型：自拍显脸小/全身显腿长/圆脸友好/娇小成人
道具：奶茶/包/相机/伞/耳机…
分镜：日系6 / 韩系6 / 旅拍8 / 私房软5 / 证件3
调色：奶油/清冷/直闪/Portra/电影青橙轻
封面：小红书3:4
配件：眼镜/口罩/耳机
C位：女主+宠物 / 女主+男配虚
运动：瑜伽/跑/网球…  职场：通勤/加班窗/西装
系列锁脸 / 负向女脸

例：`通勤妆+地铁+奶茶` / `一套旅拍8张+外滩` / `韩水光+封面构图`
```

---

# 交叉 · 全网续补 2026

美学 Core（Clean Girl / Office Siren…）、盐糖冷白皮、Citywalk、美术馆、I人背影、狗仔感、冬外套靠开压、湿发美妆、骑行、偶像手势等：  
→ [`asian-young-woman-web-fill-2026.md`](asian-young-woman-web-fill-2026.md)

写时与本卷 **妆发矩阵 / 修型 / 道具** 叠用（例：Clean Girl → 近素妆；冬装 → 靠开压 + 全身显腿长）。

**发型独立库 / 妆容壳扩 / 道具 40+ / 衣着零件 / 姿细条 / 探店场景 / 2026 胶片·生活感·氛围感**：  
→ [`six-axes-web-fill-2026.md`](six-axes-web-fill-2026.md)  
（本卷矩阵「妆/发」列可用 six-axes 的 hair-* / mk-* ID 填深；道具表合并，仍 **一帧 1 主道具**。）

**私房/居家柔美（用户点名）** → 叠  
[`soft-boudoir-sfw-web-fill-2026.md`](soft-boudoir-sfw-web-fill-2026.md)  
妆用 **mk-home-soft**；服级 L0 默认；模板 D 私房软 5 张可升级为该卷 session6/8。
