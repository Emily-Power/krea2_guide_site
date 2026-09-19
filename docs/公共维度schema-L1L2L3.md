# 出片公共维度 Schema（L1 → L2 → L3 → 按需 L4/L5 + 专属）

> **状态：** 2026-08-12 夜 **v2 联网扩库** · 点菜权威 `dimension_items.py`（公共≈410 + SUBJECT≈107 + 专属≈130）  
> **总公式：** `Skill = 公共树(L1→L2→L3→L4→L5) + 该 Skill 专属`  
> **生成：** `python skill-guide-site/scripts/gen_dimension_static.py`  
> **补全来源：** 裙型分类学 · 人像九光位 · 2025–26 亚发 · K-beauty · 姿族 · 成人静帧体位  
> **边界：** 18+；Figure SFW；Youth 非露骨；Erotic **E级与衣着品类分离**  

---

## 0. 层级定义

| 层 | 含义 | 本文件内容 |
|----|------|------------|
| **L1** | 大维度（瘦顶层 **12**） | §1 总表 |
| **L2** | 维内大类点菜 | 各维 §A 表（本文件主体） |
| **L3** | 再细化（版型/状态/参数） | 各维 §B 方向（条目级 L3 后补） |
| **L4/L5** | 按需 | 仅痛点维；本文件只标「可拆点」 |
| **专属** | Skill 独有 | §14 |

**点菜纪律：** 每维通常 **L2 主选 1** + 可选 L3 修饰 0～2；压缩时先砍 L3 装饰。  
**组合包** = 预填多维 L2/L3（+ 可选专属）的快照。

### 0.1 多选语义：横向 vs 纵向（导演台强制）

> 反例：发型同时勾「黑长直 + 长层次 + 披肩微卷 + 低马尾 + 凌乱丸子」——这是 **L2 主造型互斥** 被误当成多选，不合理。

| 模式 | 含义 | 典型维 |
|------|------|--------|
| **单选** | 整维只能 1 个 ID | eth / age / sex / body / zone / intensity / aes… |
| **纵向叠层** | **跨 group** 可多选（L2 造型 + L3 刘海 + L3 发态）；**同 group 互斥**（主造型只 1） | hair · cloth · pose · makeup · light · cam · set · grade · cast |
| **横向多选** | **同层多个 peer** 合理（多件道具、多点暗示） | prop · focus · bodyfocus · fantasy |

导演台实现：`skill-guide-site/assets/director.js` → `FIELD_POLICY`（按 option.`group` 限流 + `exclusiveGroupSets`）。  
**逐 group / 嵌套（含 L2 多槽 + L3 依赖）全文：** [`维度点菜策略-逐层分析.md`](./维度点菜策略-逐层分析.md)。

| L1 | 模式 | 同组规则 | 说明 |
|----|------|----------|------|
| subject 子字段 | 单选 | — | 人种/年龄/性别/体型语义互斥 |
| cast | 纵向 | 人数主类 1 · 关系 0～1 | 不是「solo+duo」 |
| hair | 纵向 | **L2造型只1** · 刘海/发态/发色各≤1 | 合理：`长直+窗帘刘海+风动` |
| makeup | 纵向 | 妆壳 1 · 妆件 ≤2 | 壳互斥，件可叠 |
| expr | 纵向 | 表情壳 1（含分轨互斥）· 视线 1 | |
| cloth | 纵向 | 外搭/上装/下装等槽位各 1 · 状态≤3 · 配≤3 | 层叠穿衣，非五个连衣裙 |
| pose | 纵向 | **站/走/坐…大族互斥只1** · 细姿≤2 | 单帧一个大姿 |
| prop | **横向** | 同层 ≤4 | 杯+书+包合理；`none` 清空 |
| set | 纵向 | 主场景只 1 · L3 锚可叠 | 不是街+酒店+卧室同时主场 |
| light | 纵向 | 主光型只 1（蚌式≠伦勃朗）· 辅光可叠 | 摄影光位互斥为主 |
| cam | 纵向 | 景别/角度/画幅/焦段各 1 | 一帧一套镜头参数 |
| grade | 纵向 | 主调色只 1 | 一帧 ≤1 look |

Skill 写作同构：主造型/主光/主场 **写死一个**；修饰维可叠句，勿把互斥 peer 写成同时成立。

---

## 1. L1 十二大维（已锁定）

| # | ID | 中文 | L2 密度 | 点菜模式 | 备注 |
|---|-----|------|---------|----------|------|
| 1 | `subject` | 主体档案 | 中（子字段） | 子字段**单选** | eth/age/body/sex |
| 2 | `cast` | 人数关系 | 薄 | 纵向 | 主类 + 修饰 |
| 3 | `hair` | 发型 | 中 | **纵向** | style×1 + bang/state/color |
| 4 | `makeup` | 妆容 | 中 | 纵向 | 妆壳×1 + 妆件 |
| 5 | `expr` | 表情视线 | 中 | 纵向 | 壳×1 + 视线 |
| 6 | `cloth` | 衣着 | **厚** | 纵向 | 品类槽位 + 状态/鞋配 |
| 7 | `pose` | 姿势 | 厚 | 纵向 | 大姿×1 + 细姿 |
| 8 | `prop` | 道具 | 中 | **横向** | 多件；含 none |
| 9 | `set` | 场景 | 厚 | 纵向 | 主场×1 + 锚 |
| 10 | `cam` | 镜头 | 中 | 纵向 | 景别/角度/画幅 |
| 11 | `light` | 光线 | 中 | 纵向 | 主光型×1 |
| 12 | `grade` | 调色媒介 | 薄 | 纵向 | 一帧主 look ≤1 |

**不进 L1：** acc/comp/foot/mood/material（子桶或写作）；anime 媒介可塞 grade。

---

## 2. `subject` 主体档案

### A. L2（子字段组合）

#### 2.1 `eth` 人种

| ID | 中文 | 默认 |
|----|------|------|
| `eastasian` | 东亚 | ★ 未指定强制 |
| `chinese` | 华人特征（非刻板） | |
| `japanese` | 日本向 | |
| `korean` | 韩国向 | |
| `seasian` | 东南亚 | 点名 |
| `southasian` | 南亚 | 点名 |
| `white` | 白人/欧裔 | 点名 |
| `black` | 黑人/非裔 | 点名 |
| `latine` | 拉丁裔 | 点名 |
| `mixed` | 混血 | 点名 |
| `override` | 用户原话 | 兜底 |

#### 2.2 `age` 年龄带（全 18+）

| ID | 中文 | 默认 |
|----|------|------|
| `e20` | 二十出头 | ★ |
| `m20` | 二十五上下 | |
| `l20` | 奔三前 | |
| `t30` | 轻熟/刚奔三 | |
| `m30` | 三十中段 | |
| `mature` | 更成熟（点名） | |

禁：teen/未成年。「少女感」= 美学，不占 age。

#### 2.3 `body` 体型（单选主型）

| ID | 中文 | 默认 |
|----|------|------|
| `slim` | 修长 | ★ |
| `average` | 自然均称 | |
| `petite` | 娇小成人（成人脸） | |
| `curvy` | 曲线 | |
| `athletic` | 运动体能 | |
| `busty` | 丰胸焦点 | erotic 常用 |
| `soft` | 柔软微肉 | |

高挑：写入 slim 句，不单开。

#### 2.4 `sex` 性别呈现（薄）

| ID | 中文 | 默认 |
|----|------|------|
| `woman` | 女 | Youth/Erotic ★ |
| `man` | 男 | |
| `androgynous` | 中性呈现 | 点名 |

### B. L3 方向

脸型关键词、痣/牙/眼镜锁、连续锁细节；肤 undertone 可与 grade/light 叠。

### C. 分轨

| Skill | 默认 |
|--------|------|
| Figure | eastasian+e20+slim；sex 随题材 |
| Youth | woman+eastasian+e20 |
| Erotic | 同 Youth；可 t30/m30/busty |

---

## 3. `cast` 人数关系

### A. L2 主类

| ID | 中文 | 默认 |
|----|------|------|
| `solo` | 单人 | ★ |
| `duo` | 双人 | |
| `group` | 群像 3+ | 须 1 主被摄 |
| `mirror` | 镜中双身（同一人） | |
| `hand_only` | 只露配角手/臂 | |
| `partial_other` | 配角半身/脸出画 | |

### B. L2 修饰（0～1）

| ID | 中文 |
|----|------|
| `hero_focus` | 主被摄优先 |
| `equal` | 对等双人 |
| `couple` | 情侣感 |
| `friends` | 闺蜜/友群 |
| `team` | 团队/同事 |
| `implied_viewer` | 隐含观看者（无第二人体） |
| `pov_self` | 第一人称边肢 |

### C. L3 / 专属

群戏 mmf/ffm/轮 → Erotic 专属，公共只用 group。  
Youth 默认无男体实体。

---

## 4. `hair` 发型

### A. L2 `style` 主造型（选 1）

| ID | 中文 | 默认 |
|----|------|------|
| `long_straight` | 黑长直/丝滑长直 | ★ |
| `long_layers` | 长层次 | |
| `waves` | 披肩微卷 | |
| `wolf` | 狼尾/狼剪 | |
| `bob` | 齐肩 bob | |
| `lob` | 锁骨发 | |
| `hime` | 姬发（成人） | 禁幼态 |
| `high_pony` | 高马尾 | |
| `low_pony` | 低马尾 | |
| `messy_bun` | 丸子/凌乱低髻 | |
| `half_up` | 半扎/抓夹半完成 | |
| `updo` | 低盘/正式盘 | |
| `wet` | 湿发贴顺 | |
| `messy` | 睡乱/微乱披肩 | |
| `slick_back` | 后梳贴/湿顺中分 | |
| `short_pixie` | 短发/长 pixie | 点名 |

### B. L2 `color`（可选）

`black★` · `dark_brown` · `warm_brown` · `ash_brown` · `milk_tea` · `highlight` · `other`

### C. L2 `state`（可选 0～1）

`loose` · `wind` · `tucked_ear` · `one_shoulder` · `face_curtain` · `ribbon` · `grabbed`（erotic）

### D. L3

刘海族（窗帘/空气/齐/侧分）、分区中分侧分、C 卷/数字烫参数。

---

## 5. `makeup` 妆容

### A. L2 妆壳（选 1）

| ID | 中文 |
|----|------|
| `bare` | 伪素/近素 |
| `commute` | 通勤淡妆 |
| `id_neutral` | 证件/简历自然 |
| `kr_glass` | 韩系水光 |
| `kr_3pt` | 韩三点 |
| `jp_bite` | 日系咬唇 |
| `douyin_soft` | 抖音纯欲软 |
| `soft_glam` | 软 glam |
| `warm_date` | 约会暖妆 |
| `qingleng` | 清冷雾面 |
| `mono_blush` | 单色腮红妆 |
| `fox_soft` | 轻狐狸眼 |
| `red_lip` | 经典红唇 |
| `smoky_soft` | 轻烟熏 |
| `flash_ready` | 直闪耐拍 |
| `sport_sheer` | 运动薄妆 |
| `home_soft` | 居家近素 |
| `mama_born` | 妈生感 |
| `dan_gan` | 淡感妆 |
| `ruined` | 花妆/泪妆残留（erotic） |

### B. L3

卧蚕、渐变唇、妈生眉、横扫腮、内眼线 — 拼进壳句，不单开 L2 菜单刷屏。

### C. 非本维

表情/视线 → `expr`。身体幻想标记 → Erotic 专属。

---

## 6. `expr` 表情视线

### A. L2 公共表情壳

| ID | 中文 |
|----|------|
| `soft_smile` | 浅笑 |
| `neutral` | 中性/证件 |
| `mute` | 抿唇 |
| `cool` | 冷眼 |
| `qingleng` | 清冷少笑 |
| `laugh` | 中途笑 |
| `focus_task` | 专注任务 |
| `away` | 看远 |
| `wind_squint` | 风中微眯 |
| `half_lidded` | 半眯 |
| `soft_bite` | 轻咬下唇 |
| `knowing_lens` | 盯镜头知情 |
| `sleepy` | 刚醒 |
| `tiny_smirk` | 极浅笑 |
| `self_gaze` | 自赏 |
| `confident` | 自信 |
| `candid` | 抓拍脸 |
| `weary` | 倦意 |

### B. L2 分轨加档（同维显隐）

| ID | 中文 | Skill |
|----|------|--------|
| `bedroom_eyes` | 卧室眼 | Youth/Erotic |
| `shocked_aroused` | 撞见慌欲 | Erotic |
| `tears_pleasure` | 快感泪 | Erotic |
| `orgasm` | 高潮脸 | Erotic |
| `afterglow` | 事后慵懒 | Erotic |
| `ahegao` | 阿黑颜（点名） | Erotic |
| `fucked_silly` | 被干傻脸（点名） | Erotic |
| `performative` | 舞台表演脸 | Figure |
| `editorial_blank` | 走秀无表情 | Figure |

### C. L2 视线（可选）

`to_lens` · `off_frame` · `to_light` · `to_task` · `to_mirror` · `to_partner` · `down`

---

## 7. `cloth` 衣着（厚维）

### A. L2 品类（主选 1；外套可叠外层）

| ID | 中文 | 备注 |
|----|------|------|
| `outer_coat` | 外套/大衣/风衣 | 可外层 |
| `blazer_suit` | 西装/通勤套 | |
| `shirt_blouse` | 衬衫/上衣 | |
| `knit_cardigan` | 针织/开衫 | |
| `tee_hoodie` | T恤/卫衣 | |
| `dress` | **连衣裙** | 与裙分开 |
| `skirt` | **半身裙** | 痛点补全 |
| `pants` | 裤装 | 非牛仔主标 |
| `denim` | 牛仔 | |
| `sport` | 运动装 | |
| `lounge` | 家居完整装 | SFW |
| `sleep` | 睡衣/睡裙 | |
| `robe` | 浴袍 | |
| `formal` | 礼服/场合 | |
| `old_money` | 名媛静奢叠 | |
| `new_chinese` | 新中式 | 尊重 |
| `slip` | 吊带裙/slip | Youth 常用 |
| `shirt_only` | 仅大衬衫 | |
| `cami_set` | 吊带短裤套 | |
| `swim` | 泳装 | Figure 点名 |
| `techwear` | 机能 | |
| `lingerie` | 内衣套装 | Fig 禁默认 |
| `towel` | 浴巾裹 | 点名 |
| `cos_costume` | COS 套装 | |
| `latex_leather` | 乳胶/皮 | Erotic |
| `ol_set` | OL 制服向 | |
| `layer_ootd` | 潮流层叠 | |
| `wet_cling` | 湿衣贴肤效果 | 宜+底品类 |

### B. L2/L3 公共着装状态（可选）

| ID | 中文 |
|----|------|
| `full` | 穿戴整齐 ★Figure |
| `relaxed` | 居家随意 |
| `layer_open` | 外套敞开 |
| `strap_slip` | 肩带滑落 |
| `few_buttons` | 少扣/领开 |
| `hem_up` | 下摆掀卷 |
| `half_off` | 半褪（公共） |
| `sheer_wet` | 湿透贴肤 |

### C. L3 版型方向（后补条目）

- **裙：** mini / midi / maxi；A 字 / 包臀 / 百褶 / 鱼尾 / 伞裙 / 开衩  
- **裤：** 阔腿 / 直筒 / 紧身 / 西装褶  
- **面料词：** 棉/丝/雪纺/牛仔纹理/针织罗纹（写作 1 词）

### D. 子桶（非 L1）

**foot：** sneaker · loafer · maryjane · boot_ankle · boot_knee · heel · sandal · barefoot  
**acc：** glasses · earrings · chain · watch · hat · mask · none  

### E. Erotic 暴露级（专属，不替代品类）

`E0` 穿衣情欲 · `E1` 半褪★ · `E2` 内衣 · `E3` 外翻拨开 · `E4` 全裸点名  

点菜：`品类 L2` + `E级`。

---

## 8. `pose` 姿势（单帧）

> 参照：站/坐/靠/走摄影共识 + figure pose-catalog 族。

### A. L2 姿族（选 1 主族）

| ID | 中文 | 说明 |
|----|------|------|
| `stand_weight` | 站-重心偏移 | 后脚重心、软膝；默认生活/时尚 |
| `stand_scurve` | 站-S 线/时尚 | 时尚编辑；勿无脑默认运动/纪实 |
| `stand_power` | 站-气场/权力 | 双手腰、挺拔 |
| `walk_midstride` | 走-中步 | 街拍/旅拍 |
| `lean` | 倚靠 | 墙/栏/门框 |
| `sit_edge` | 坐-沿 | 椅沿/窗沿/床沿 |
| `sit_cross` | 坐-交腿/蜷 | 沙发、咖啡 |
| `sit_floor` | 坐-地（成人） | 地毯等；着装得体 |
| `perch` | 半坐搭靠 | 桌沿、吧台 |
| `over_shoulder` | 回眸 | 过肩看镜头或光 |
| `mirror_self` | 镜前姿 | 对镜站/侧身 |
| `lie_side` | 侧卧 | 床/沙发；分 skill 尺度 |
| `lie_back` | 仰躺/半躺 | |
| `crouch` | 蹲/低姿 | 时尚或功能 |
| `stretch` | 伸展定格 | 居家/纯欲 |
| `hand_face` | 手与脸互动 | 托腮、拨发（手简单） |
| `task_work` | 任务功能姿 | 职业/纪实手上有活 |
| `athletic` | 运动发力姿 | 弓步、准备势、瑜伽支撑 |
| `dance_line` | 舞蹈线 | 芭蕾/舞台延伸 |
| `bed_edge` | 床沿前倾/坐 | Youth/Erotic 高频 |
| `kneel` | 跪姿族 | 尺度分 skill；erotic 开腿另专属 |
| `wall_step` | 离墙一步侧 | 侧光塑形 |
| `window_pose` | 窗边站/坐 | 与 set 窗绑 |
| `pov_open` | 开放对镜/对镜头 | erotic 常用主姿入口 |

### B. L3 方向

支撑脚/坐骨写死；肩髋反向；手位简单（插袋/拉带/插发）；运动相位（腾空/触地）；舞蹈支撑腿 vs 工作腿。

### C. 分轨

| Skill | 默认倾向 |
|--------|----------|
| Figure | 随大区：站走/任务/运动/舞 |
| Youth | sit/lie/mirror/stretch/window |
| Erotic | kneel/bed/open + 连接另写 |

---

## 9. `prop` 道具

### A. L2（主选 1 或 none）

| ID | 中文 |
|----|------|
| `none` | 空手 ★ 常用 |
| `phone` | 手机 |
| `cup_drink` | 杯/咖啡/奶茶 |
| `bottle` | 水瓶/饮料瓶 |
| `bag_tote` | 托特/肩包/腋下包 |
| `luggage` | 行李箱 |
| `book` | 书/杂志 |
| `flower` | 花束/单枝 |
| `umbrella` | 伞 |
| `camera` | 相机/拍立得 |
| `keys` | 钥匙 |
| `food` | 小吃/甜筒（手持） |
| `tool_work` | 职业工具 |
| `sport_gear` | 拍/垫/盔 |
| `sheet_clutch` | 抓床单/被（居家） |
| `mirror_frame` | 扶镜框（非道具实体也可写作） |
| `toy_adult` | 成人玩具 | **Erotic 点名** |
| `restraint` | 绳/铐/项圈道具 | **Erotic** |
| `other` | 用户指定 |

### B. L3

手位接触点写死；一帧 1 主道具；防崩：少双手高难交互。

---

## 10. `set` 场景

### A. L2 场大类（选 1）

| ID | 中文 | 2～4 锚方向 |
|----|------|-------------|
| `street_city` | 街/城 | 建筑线、人行、招牌虚 |
| `metro_transit` | 地铁/站台/通勤 | 拉环、车厢、站台 |
| `cafe` | 咖啡/书咖 | 窗位、杯、木桌 |
| `indoor_home` | 家-客厅/卧室 | 沙发、床、窗纱 |
| `hotel` | 酒店/套房 | 钨丝、床、行李 |
| `bathroom` | 浴室 | 雾、瓷砖、镜 |
| `window_sill` | 窗边专场 | 窗框、城市 bokeh |
| `studio` | 棚/无缝 | 纸底、灯具可虚 |
| `office` | 办公/职场 | 玻璃廊、桌、夜窗 |
| `nature_outdoor` | 自然户外 | 树、海、山脊尺度 |
| `landmark_travel` | 旅拍地标 | 具名锚（北上杭…） |
| `shop_third` | 第三空间探店 | 书店/花店/便利店/洗衣房/影院大堂 |
| `night_neon` | 夜霓虹/夜市 | 混光、湿反光 |
| `gym_sport` | 健身房/运动场 | 镜、器械 |
| `stage_theater` | 舞台/剧场 | 追光、黑场 |
| `car_interior` | 车内 | 座、玻璃雾 |
| `balcony_rooftop` | 阳台/天台 | 栏杆、天际 |
| `campus_adult` | 校园成人 | 草坪、图书馆（成人锁） |
| `love_hotel` | 情趣酒店 | **Erotic** LED/镜 |
| `fantasy_space` | 幻想场 | **Erotic F** 法阵/异界 |
| `other` | 用户指定 | |

### B. L3

每场绑默认光倾向；Env **2～4 锚** 非装修清单；单帧单场。

---

## 11. `cam` 镜头

### A. L2 景别

| ID | 中文 |
|----|------|
| `ewide` | 超远/环境小人 |
| `full` | 全身 |
| `cowboy` | 牛仔景（大腿上） |
| `medium` | 中景 |
| `mcu` | 中近景 |
| `cu` | 近景/特写脸 |
| `ecu` | 局部极近（眼/手/结合部 erotic） |

### B. L2 角度

| ID | 中文 |
|----|------|
| `eye` | 平视 ★ |
| `low` | 仰 |
| `high` | 俯 |
| `dutch` | 荷兰角（慎） |
| `topdown` | 顶视 |

### C. L2 画幅

| ID | 中文 |
|----|------|
| `ar_23` | 2:3 |
| `ar_34` | 3:4 ★ 封面常用 |
| `ar_916` | 9:16 竖屏 |
| `ar_32` | 3:2 横 |
| `ar_169` | 16:9 |
| `ar_11` | 1:1 |

### D. L2 焦段感（可选）

| ID | 中文 |
|----|------|
| `lens_24_35` | 广角环境/OOTD |
| `lens_50` | 标准人文 |
| `lens_85` | 85 美妆人像 ★ 半身 |
| `lens_135` | 长焦压缩 |

### E. L2 构图子桶 `comp`（可选，不升 L1）

| ID | 中文 |
|----|------|
| `thirds` | 三分 |
| `center` | 居中 |
| `neg_space` | 负空间 |
| `frame_in` | 框中框 |
| `leading` | 引导线 |
| `vertical_zones` | 竖屏上中下分区 |
| `foot_room` | 全身留脚 |

### F. L3

景别与细节密度匹配（远景不写毛孔）；DOF 深浅一句。

---

## 12. `light` 光线

> 经典人像光型 + 实用现场光（联网/摄影共识：Rembrandt、loop、butterfly、split、clamshell、rim 等）。

### A. L2 光型（选 1 主）

| ID | 中文 | 说明 |
|----|------|------|
| `window_soft` | 窗光软 | 侧窗 45° 常用 |
| `window_back` | 窗逆光/轮廓 | 发缘光、脸需补 |
| `overcast` | 阴天平光 | 软、低反差 |
| `golden` | 黄金时刻 | 暖侧长影 |
| `blue_hour` | 蓝调时刻 | |
| `tungsten` | 钨丝/暖实用灯 | 酒店床头 |
| `practical_lamp` | 现场台灯/落地灯 | 一主灯衰减 |
| `clamshell` | 蚌式 | 美妆棚 |
| `rembrandt` | 伦勃朗 | 三角光斑 |
| `loop` | 环形光 | 鼻影小环 |
| `butterfly` | 蝶形/派拉蒙 | 鼻下蝶影 |
| `split` | 分割光 | 半明半暗 |
| `rim` | 轮廓/逆光缘 | |
| `hard_side` | 硬侧光 | 肌理/时尚 |
| `softbox_studio` | 棚柔光 | |
| `neon_mix` | 霓虹混光 | 夜 |
| `flash_on` | 直闪/机顶硬闪 | CCD/夜拍 |
| `screen_glow` | 屏幕/手机冷光 | |
| `steam_diffuse` | 蒸汽漫射 | 浴室 |
| `spotlight_stage` | 舞台追光 | 黑场 |
| `short_light` | 短光显瘦 | 脸侧 |
| `broad_light` | 宽光 | |
| `high_key` | 高键 | 亮净 |
| `low_key` | 低调 | 深阴影亲密 |

### B. L3

主光方向（相机左/右/上）；补光比；色温；光落在哪块体积（锁骨/面颊/布料）。

---

## 13. `grade` 调色媒介

### A. L2（一帧 ≤1）

| ID | 中文 |
|----|------|
| `natural` | 自然真色 ★ |
| `jp_cream` | 日系奶油 |
| `kr_clean` | 韩系干净亮 |
| `qingleng` | 清冷青灰 |
| `portra` | 胶片肤/Portra 感 |
| `cine_soft` | 电影青橙轻 |
| `bw` | 黑白 |
| `flash_pop` | 直闪高反差 |
| `ccd` | CCD/数码直出感 |
| `neon_night` | 夜霓虹溢色 |
| `old_money` | 静奢克制饱和 |
| `iphone` | 手机 HDR 自然 |
| `warm_sunset` | 暖夕 |
| `cool_mute` | 冷雾低饱和 |
| `anime_cel` | 二次元平涂媒介 | 点名；默认可不出现 Figure |

### B. L3

颗粒强弱、halation 轻、是否压高光 — 一句即可。

---

## 14. Skill 专属（不进公共 L1 强制）

### Figure

| 轴 | 内容 |
|----|------|
| `zone` | 大区 A–I |
| 题材语义 | 职业/运动/舞蹈/艺术人体点名 |
| SFW 锁 | 禁露骨；私房仅点名 |

### Youth

| 轴 | 内容 |
|----|------|
| `imply` / focus | 暗示焦点（锁骨/腰/大腿缘…） |
| `I0–I3` | 暴露暗示梯度（非 E 级） |
| `aes` / vertical | 白月光/禁欲/coquette/Vanilla… |
| 人数 | 默认 solo；无默认男体 |

### Erotic

| 轴 | 内容 |
|----|------|
| `connection` | 连接点句 |
| `E0–E4` | 暴露级 |
| `act` / 体位 | 行为与体位 |
| `finish` | 体液结局 |
| `dynamic` | 权力关系 |
| `fantasy` / F | 触手/淫纹/物种等 |
| `bodyfocus` | 身体焦点（胸臀等） |

---

## 15. 默认快配（未指定时）

| 维 | Figure | Youth | Erotic |
|----|--------|-------|--------|
| subject | EA女 e20 slim | 同左 woman | 同左 |
| cast | solo | solo | solo |
| hair | long_straight | long_straight | long_straight/wet |
| makeup | commute/bare | bare/home_soft | bare/ruined 可 |
| expr | soft_smile/candid | half_lidded | bedroom_eyes |
| cloth | full 通勤/层叠 | shirt_only/sleep | + E1/E2 |
| pose | stand/walk 随区 | sit/mirror | bed/kneel 入口 |
| prop | none 或 1 | phone/cup | none/sheet |
| set | street/cafe 轮换 | home/hotel | hotel/bedroom |
| cam | 随题材；封面 3:4 | medium/mcu 竖 | low mcu 竖 |
| light | window_soft 等 | tungsten/window | tungsten |
| grade | natural | natural/jp_cream | natural/cine |

---

## 16. 落盘对照（导演台）

| 现 static | 目标 |
|-----------|------|
| SUBJECT.hair | 迁顶层 `hair` |
| FIGURE set/light/cam… | ID 对齐本表 L2 |
| EROTIC cloth=e0–e4 | 拆：品类 L2 + E 专属 |
| 无 cast | 新增 |
| makeup 仅 Figure | 三 skill 共用 L2 ID |

**写入 skill/static：** 本文件确认采用后另轮；改组合包后跑 `build_director_catalog.py`。

---

## 17. 进度

| L1 | L2 表 | 状态 |
|----|-------|------|
| subject～expr | 本文件 §2–6 | ✅（含用户已确认稿） |
| cloth～grade | 本文件 §7–13 | ✅ 代理定稿 |
| L3 条目库 | 方向已标 | ⬜ 下一阶段按维扩 |
| 专属详表 | §14 索引 | ⬜ 与现有 reference 对齐 ID |
| skill/static 写入 | — | ⬜ 用户醒来后可开 |

---

*代理全权推进 · 可与 TODO.md 对照 · 睡醒后续：审阅本文 → 开 L3 或落盘 static。*
