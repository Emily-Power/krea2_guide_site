# 场景深库 2026 — youth-seduction

> **用途：** 专补 **Setting / 场 + 光绑定 + 2–4 道具锚 + 默认姿/I** 的广度与可画深度。  
> **边界：** 成人 early twenties · 默认东亚 · **暗示非露骨** · 默认 **solo**。  
> **交付：** 场只写 **2–4 锚**；L7 先砍；**永不砍** 姿/暗示/主光。  
> **叠用：** 五维 → `hmcp-depth-catalog-2026.md`；光全表 → `lighting-youth-seduction.md`；平台扩 → `web-fill`。

**检索内化：** 中文居家/酒店/窗边/浴室氛围帖；欧美 hotel boudoir 窗位与套房分区；浴室镜自拍姿；小空间自然光；阳台/玄关/厨房/WFH/loft 肖像。

---

## 0. 场景写法铁律

| 规则 | 说明 |
|------|------|
| 2–4 锚 | 家具/光/生活脏各取，勿装修说明书 |
| 主光必绑 | 每场景默认 1 个 light ID |
| 一帧一场 | 禁止「从玄关走到浴室再上床」时间线 |
| 暗示优先 | 场服务姿与暗示区，不抢戏 |
| 成人语义 | 宿舍→ adult apartment；禁未成年校园 |

**Environmental 句模：**
```
[setting type], [2–4 anchors], [optional implied-viewer ≤1], private solitary mood
```

---

## 1. 场景总表 sc-*（点菜）

| ID | 中文触发 | 默认光 | 默认 I | 高信号锚（选 2–4） |
|----|----------|--------|--------|-------------------|
| **sc-bed-night** | 卧室夜/深夜床 | bedside-tungsten | I1–I2 | 床头灯、乱床单、亮屏手机、半杯饮料 |
| **sc-bed-morning** | 晨间床/刚醒 | morning-cool / window-45 | I1 | 窗纱、卷被、发夹、护肤瓶 |
| **sc-bed-golden** | 金辉床边 | golden-hour-window | I0–I1 | 长影、暖尘、薄被、杯 |
| **sc-sofa-day** | 沙发日/居家九式 | window-45 | I1 | 抱枕、毛毯、遥控、窗 |
| **sc-sofa-night** | 沙发夜刷机 | phone-screen / tv-idle-blue | I1–I2 | 屏光、空调被、耳机线 |
| **sc-window-day** | 窗边日 | window-45 / sheer-backlight | I1 | 窗框、纱帘、城市 bokeh |
| **sc-window-blind** | 百叶窗 | blind-stripes | I1–I2 | 百叶条纹、白衬衫、都市 |
| **sc-window-night** | 夜窗霓虹 | neon-spill | I1–I2 | 彩光渗入、暖实用灯、肩带 |
| **sc-bath-steam** | 浴室蒸汽 | steam-bath | I2–I3 | 雾镜、挂巾、地面积水反光、瓶罐 |
| **sc-bath-marble** | 酒店大理石浴 | vanity-bulb-row | I2–I3 | 大理石、浴袍、镜、暖泡 |
| **sc-hotel-arrival** | 酒店刚到 | hotel-lamp | I1–I2 | 箱包开、房卡、白巾、钨丝 |
| **sc-hotel-bed** | 酒店床 | hotel-lamp / window | I1–I2 | 白床单、靠垫、落地灯 |
| **sc-hotel-window** | 酒店落地窗 | window-45 night/day | I1 | 城市高楼、薄纱、脚沿 |
| **sc-entry-night** | 玄关夜归 | entry warm practical | I1 | 钥匙盘、鞋一只、购物袋、门缝光 |
| **sc-entry-onemile** | ワンマイル出门前 | entry-daylight | I0–I1 | 玄关镜、帆布袋、鞋半穿 |
| **sc-kitchen-am** | 厨房晨 | window soft / golden | I0–I1 | 台沿水珠、杯、吐司、冰箱贴 |
| **sc-kitchen-fridge** | 深夜冰箱 | fridge-cavity | I1 | 开冰箱冷白光、裸足、暗厨 |
| **sc-wfh-night** | 居家加班角 | monitor + window night | I1 | 合盖笔电、耳机、外套椅背、夜窗 |
| **sc-desk-corner** | 书桌角 | desk lamp warm | I0–I1 | 台灯、书、椅转侧 |
| **sc-balcony-dusk** | 黄昏阳台 | golden / dusk | I1 | 栏杆、晾衣、冰饮冷凝 |
| **sc-balcony-rain** | 雨阳台 | overcast + wet glass | I1 | 雨丝玻璃、湿袖、收衣 |
| **sc-dance-studio** | 练舞房 | studio-gold / high window | I1 | 墙镜、水瓶、毛巾、木地板反光 |
| **sc-yoga-mat** | 家居瑜伽垫 | window-45 | I0–I1 | 垫、水瓶、发带松 |
| **sc-car-night** | 车内夜 | neon + dash | I1 | 副驾、安全带松、后视挂饰 |
| **sc-loft-night** | 画室 loft 夜 | floor lamp | I1–I2 | 画布边、颜料点、坐垫、落地灯 |
| **sc-reading-nook** | 阅读角 | warm lamp / window | I0–I1 | 书堆、椅、毯、一盏灯 |
| **sc-laundry-adult** | 成人公寓洗衣 | cool practical / window | I0–I1 | 洗衣机、篮、等待靠筒 |
| **sc-hallway-soft** | 公寓走廊软 | dim practical | I1 | 门框、壁灯、半公开轻风险仍遮盖 |
| **sc-closet-mirror** | 衣帽间镜 | vanity / soft flash | I1–I2 | 全身镜、衣架虚化、地毯 |
| **sc-cream-room** | 奶油风房 | cream-high-key | I1 | 奶油被、木纹、绿植、毛绒枕 |
| **sc-sparse-white** | 白月光空房 | morning-cool / sheer | I0–I1 | 白墙、少物、窗 |
| **sc-neon-apt** | 霓虹公寓 | neon-spill + warm | I1–I2 | 窗彩光、床/沙发一角 |
| **sc-tub-edge** | 浴缸沿坐（遮盖） | steam / vanity | I2–I3 | 浴缸沿、湿发、巾或袍 **写死遮盖** |
| **sc-stairs-home** | 家中楼梯（成人公寓） | window stair light | I0–I1 | 扶手、阶、侧身线 · 非未成年宿舍 |
| **sc-corner-portrait** | 墙角肖像 | single soft key | I1 | 两墙夹角、简道具、中近景 |
| **sc-floor-rug** | 地毯地板姿 | window / tungsten | I1–I2 | 软毯、靠沙发/床沿、全身线 |
| **sc-projector** | 投影仪光 | projector wash | I1 | 白墙光斑、腿/身切光、暗室 |
| **sc-ac-winter** | 暖气旁冬 | warm practical | I1 | 暖气片、只穿袜、毛毯可选 |
| **sc-bay-window** | 飘窗垫 | window-45 / golden | I0–I1 | 宽窗台垫、城市远、膝蜷、薄毯 |
| **sc-vanity-night** | 梳妆台夜 routine | vanity-side-only / mirror-vanity | I1 | 镜灯、护肤瓶、缎面睡衣、凳 |
| **sc-minimal-day** | 极简自然光房 | high-key-minimal | I0–I1 | 少家具、大窗、白/米墙、表情优先 |
| **sc-hotel-sofa** | 酒店套房沙发 | hotel-lamp | I1–I2 | 现代沙发、落地灯、箱包远、白袍/衬衫 |
| **sc-bedroom-door** | 卧室门框 | practical-only-dark | I1 | 门把、门缝光、半身入框 |
| **sc-string-bokeh** | 灯串虚化房 | digicam-hard-flash 或 tungsten + bokeh | I1–I2 | 灯串仅 bokeh、床沿、直闪可选 |
| **sc-skincare-corner** | 护肤角 | vanity / morning-cool | I0–I1 | 小冰箱/瓶罐、棉柔巾、水光脸 |
| **sc-rain-window-sit** | 雨窗坐 | overcast-indoor | I1 | 雨丝玻璃、窗沿坐、热饮冷凝 |
| **sc-closet-change** | 衣帽间换装中 | soft practical / flash soft | I1–I2 | 半穿袍/衬衫状态写死、镜、地毯 |
| **sc-bookshelf-soft** | 书架软角 | warm lamp | I0–I1 | 书脊虚化、站或跪、quiet |
| **sc-penthouse-glass** | 高楼玻璃幕（成人） | neon-spill / city night | I1 | 落地玻璃、城市点光、仍遮盖 |

---

## 2. 场景分区详写（可画锚 + 禁）

### 2.1 卧室系

| 变体 | Environmental 英文锚 | 禁 |
|------|----------------------|-----|
| 夜钨丝 | rumpled bed, warm bedside lamp camera-left, phone face-up dim, half-drunk glass | 全屋开灯平光 |
| 晨窗纱 | sheer morning light, sheets half-kicked, hair clip on nightstand | 过曝死白无阴影 |
| 金辉 | low golden sun stripe across duvet, dust motes optional | 无姿只拍房间 |
| 破碎小灯 | single clip/fill on face, rest of room near-dark, messy pillow | 恐怖片冷蓝 |

### 2.2 酒店系（套房可轮换机位仍单帧）

| 变体 | 锚 | 默认姿向 |
|------|-----|----------|
| 进门 | open suitcase, keycard, warm lamp, jacket half-off | 半敞站/床沿 |
| 床 | white hotel linens, stacked pillows, clean modern | 侧卧/坐沿 |
| 浴 | marble vanity, large mirror, steam optional, robe | 镜自拍/抹雾 |
| 窗 | floor-to-ceiling city night, sheer, toe at glass | 倚窗 I1 |

**酒店光教学内化：** 大窗 = 可正侧逆位；小窗 = 更易暗调；窗帘可当背景；**一帧只取一窗位关系**。

### 2.3 浴室系

| 变体 | 锚 | 注意 |
|------|-----|------|
| 雾镜 | fogged glass, palm-clear patch, second towel, bottles | 脸在清雾区清晰 |
| 台沿 | hip to sink, chrome faucet edge, dewy skin | I1–I2 |
| 浴缸沿 | sits tub edge, robe or towel **coverage locked** | 禁 explicit 泡泡裸 |
| 直闪镜 | mirror + mild flash, marble, candid | digicam 叠 |

### 2.4 窗 / 阳台 / 半公开

| 变体 | 锚 | 风险感 |
|------|-----|--------|
| 日窗 45° | frame, soft interior fill, city soft | 低 |
| 纱逆光 | sheer bloom, rim hair/shoulder | 轮廓欲 |
| 百叶 | hard soft stripes on torso | 都市暧昧 |
| 夜霓虹 | cyan-magenta spill + warm face key | 港风 |
| 阳台黄昏 | rail, wind hair, distant roofs | 中 · 仍遮盖 |
| 雨贴玻璃 | wet pane, breath fog optional | 情绪冷门 |

### 2.5 生活动线（成人公寓）

| 变体 | 锚 | 欲从哪来 |
|------|-----|----------|
| 玄关夜归 | keys, one shoe kicked, bag on floor, door light line | 松弛刚进门 |
| 厨房晨 | mug steam, counter palm, morning window | soft life |
| 冰箱夜 | open fridge cavity cool key, bare feet | 生活冷欲 |
| WFH 夜 | laptop closed, chair turn, city window | Office soft |
| 洗衣等待 | washer drum glow optional, lean, adult laundry room | I0–I1 冷门 |
| 阅读角 | lamp pool, book, soft chair | quiet/白月光轻 |

### 2.6 运动 / loft / 车

| 变体 | 锚 | 妆发向 |
|------|-----|--------|
| 练舞房 | wall mirror, water bottle, sweat sheen, gold window | mk-after-sport |
| 瑜伽垫 | mat on wood, long stretch, home clutter soft | 健康非广告 |
| loft 夜 | canvas edge, paint fleck, floor cushion, lamp | 艺校壳 |
| 车夜 | passenger seat, neon on collarbone, seatbelt loose | I1 着装完整偏 |

---

## 3. 场景 × 默认光 × 默认姿（快绑）

| sc-* | light | body 优先 | fit 优先 |
|------|-------|-----------|----------|
| sc-bed-night | bedside-tungsten | side-lie / bed-gaze | bf-shirt / pj |
| sc-bed-morning | morning-cool | morning-sheet sit | oversized tee |
| sc-sofa-day | window-45 | side-sit-chin / sofa-curl | cream tank |
| sc-window-blind | blind-stripes | window-lean | white shirt |
| sc-bath-steam | steam-bath | fog-wipe | towel I3 |
| sc-hotel-arrival | hotel-lamp | bed-side-sit | half-open shirt |
| sc-kitchen-am | window soft | kitchen-hip | bf-shirt |
| sc-kitchen-fridge | fridge-cavity | stand fridge edge | tee+shorts |
| sc-wfh-night | monitor+window | chair-side | blouse 2 open |
| sc-balcony-dusk | golden | balc-rail | crop+shorts |
| sc-dance-studio | studio-gold | dance-floor-rest | sport |
| sc-cream-room | cream-high-key | sofa-curl | knit-cream |
| sc-neon-apt | neon-spill | window or bed edge | slip/cami |
| sc-entry-night | warm entry | entry-half | jacket half-off |
| sc-vanity-night | vanity-side-only | vanity-sit | satin pj |
| sc-minimal-day | high-key-minimal | window-lean / knee-hug | full casual I0–I1 |
| sc-bay-window | window-45 | window-sill-perch / knee-hug | lounge set |
| sc-hotel-sofa | hotel-lamp | kneel-sofa / sofa-curl | robe/shirt |
| sc-rain-window-sit | overcast-indoor | window-chin-side | knit + mug |

---

## 4. 场景组合包 combo-sc-*

| ID | 触发 | 预填 |
|----|------|------|
| **combo-sc-hotel-suite3** | 酒店套房三帧 | arrival → bath marble → bed eyes（形态 E） |
| **combo-sc-home-day4** | 居家日四帧 | window → sofa9/7 → kitchen mug → mcu |
| **combo-sc-night-alone3** | 独居夜三帧 | entry → sofa phone → bed tungsten |
| **combo-sc-wet-path3** | 浴后动线三帧 | steam mirror → towel hall soft → bed damp hair |
| **combo-sc-window-study3** | 窗专题三帧 | day 45 → blind → night neon |
| **combo-sc-softlife-am3** | soft life 晨 | golden bed → kitchen → window mug |
| **combo-sc-office-home2** | 加班回家 | wfh night → entry or bed residual makeup |
| **combo-sc-cream-vanilla2** | 奶油 Vanilla | cream room full → sofa knit mcu |
| **combo-sc-night-routine3** | 夜 routine 三帧 | vanity sit → closet change mid → bed edge damp/tousled |
| **combo-sc-minimal-window2** | 极简窗 | minimal day full → mcu eyes |
| **combo-sc-bay-rain2** | 飘窗/雨窗 | bay curl → rain glass sip |
| **combo-sc-hotel-sofa-bed2** | 酒店沙发→床 | sofa kneel → bed eyes |

每张仍 **单帧 + 连续锁**。

---

## 5. 场景深度句（Environmental 可嵌）

```
warm bedside lamp pools on rumpled sheets; phone glows face-down; one glass with condensation
sheer morning light cuts a soft rectangle across the white duvet; city soft beyond the glass
marble vanity and fogged mirror; second towel on the rack; humid air beads on shoulder
open suitcase on the luggage rack; keycard on the nightstand; single warm hotel lamp
hip to the kitchen counter; ceramic mug; morning window catching the faucet chrome
cool white light from the open fridge; the rest of the kitchen falls dark; bare feet on tile
neon spill through the apartment window rims her shoulder; warm practical lamp holds her face
```

---

## 6. 冷门场景池 61–80（接 web-fill 41–60）

61. 衣帽间全身镜地毯跪坐  
62. 楼梯扶手侧身（成人公寓）  
63. 墙角单灯肖像  
64. 投影仪光切小腿  
65. 暖气片旁只穿袜  
66. 共享洗衣房等待（成人）  
67. 阅读角灯池与书  
68. 雨阳台收丝质睡裙  
69. 浴缸沿袍坐吹半干发  
70. 酒店套房沙发跪撑  
71. 走廊尽头壁灯下回眸（仍遮盖）  
72. loft 地板坐垫+画布  
73. 车后座停驶霓虹（I0–I1 完整衣）  
74. 飘窗垫蜷+城市远  
75. 书房转椅侧对镜头松领  
76. 玄关穿鞋凳坐低头系带（I0）  
77. 阳台灯串 bokeh 仅背景  
78. 搬家泡沫箱当桌写字（服完整）  
79. 顶楼水塔平台远城剪影（远景小人物）  
80. 便利店冷白光刚进门的玄关反差  

### 冷门续 81–95（四次扩）

81. 梳妆台只开一侧镜灯涂唇油中途  
82. 极简白房大窗抱膝（成人）  
83. 飘窗垫上看雨+陶瓷杯  
84. 酒店套房沙发跪撑落地灯  
85. 卧室门框手扶门把将离回眸  
86. 灯串 bokeh 床沿 digicam  
87. 护肤小冰箱门微开冷白点光  
88. 衣帽间地毯半穿缎袍定格  
89. 书架前低光侧脸 quiet  
90. 高楼玻璃幕城市点光肩 rim（I1）  
91. 雨窗哈气圆圈边的侧脸  
92. 夜 routine 香水点颈定格  
93. 换装中衬衫只扣一颗对镜  
94. 飘窗日落金边剪影薄补脸  
95. 套房浴缸放水声中的门缝蒸汽（人在门内遮盖）  

---

## 7. 场景失败模式

| 坑 | 修正 |
|----|------|
| 装修博览会 | 砍到 2–4 锚 |
| 多房间时间线 | 单帧单场 |
| 酒店变广告样板间 | 加 1 生活脏（开箱/乱床） |
| 浴室变露骨 | towel/robe 遮盖写死 |
| 半公开变偷拍犯罪感 | 风险轻、仍成人独处自诱惑 |
| 宿舍未成年读 | adult apartment / college-age adult housing |
| 场亮姿死 | 主光落暗示区 |

---

## 8. 用户意图 → 本节

| 说法 | 打开 |
|------|------|
| 有哪些场景/换个地方 | §1 总表 |
| 酒店一整套 | combo-sc-hotel-suite3 · §2.2 |
| 浴室/雾镜/浴缸沿 | §2.3 |
| 窗/百叶/霓虹/阳台 | §2.4 |
| 厨房/冰箱/玄关/加班 | §2.5 |
| 练舞/车/loft | §2.6 |
| 奶油房/空房白月光 | sc-cream-room / sc-sparse-white |
| 冷门场景 | §6 |
| 场景+发型妆衣姿一起 | 本卷 sc + **hmcp** 五维 |
| 夜 routine / 梳妆台 | sc-vanity-night · combo-sc-night-routine3 |
| 极简自然光 / 少道具房 | sc-minimal-day |
| 飘窗 / 雨窗坐 | sc-bay-window / sc-rain-window-sit |
| 镜头机位 | **camera-composition-catalog-2026** |

---

## 9. 检索备忘

```
中文：酒店拍照 床上 窗边 浴室 氛围 / 居家场景 玄关 厨房 阳台
      梳妆台 夜 routine / 飘窗 雨天 / 极简 自然光 房间
英文：hotel boudoir window light positions / bathroom mirror selfie poses
      apartment corner portrait natural light / balcony dusk rail pose
      vanity night routine portrait / bay window cushion pose / minimalist natural light bedroom
```

---

## 10. 五次联网补 · 场景 sc+（2026-09）

| ID | 中文触发 | 英文句模 |
|----|------|----------|
| sc-canopy-cocoon | 床幔茧房 | Four-poster bed wrapped in sheer ivory canopy draping low around the mattress, layered quilts and velvet cushions inside the cocoon, dim warm practical light, boutique-hotel hush |
| sc-bow-bedroom | 蝴蝶结卧室 | Bow-decor bedroom: satin ribbon tie-backs on sheer curtains, oversized bow cushions on ruffle-edged bedding, dusty pink and cream palette, soft window daylight, coquette grown-up not childish |
| sc-deep-cocoon | 通刷深色茧房 | Color-drenched room with walls and ceiling in deep mocha or plum, one warm lamp pooling amber light, plush layered bedding in tonal browns, rich shadowed corners, intimate winter-evening mood |

> 来源：<https://www.housebeautiful.com/design-inspiration/a69619733/bedroom-design-trends-2026/> · <https://everlastingfabric.com/blogs/ever-lasting-blog/how-to-style-the-perfect-coquette-summer-bedroom> · <https://kitchensbedroomsandbathrooms.com/bedrooms/bold-bedroom-trends-for-2026-to-keep-on-your-radar/>
