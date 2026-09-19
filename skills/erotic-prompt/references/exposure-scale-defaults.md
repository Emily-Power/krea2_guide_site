# 暴露梯度 · 尺度默认 · 行为默认

> 对齐 figure-photo「完整着装 / 私房 L0–L3」的镜像：**用户原话优先；未说则用默认。**  
> **人种默认：** 亚洲年轻成年女 `adult East Asian woman early twenties`  
> **尺度默认：大胆 bold = explicit**（可写性器/插入/体液，但行为未点名时不自动上插入）

---

## 1. 尺度 Intensity（默认 bold/explicit）

| 级 | ID | 触发 | 写法 | 默认？ |
|----|-----|------|------|--------|
| 0 | **soft** | 软色情、暗示、擦边 | 轮廓、布料、剪影；情欲在姿与光 | 用户点 |
| 1 | **sensual** | 情色、私房、性感 | 半裸/内衣、曲线；性器可隐可露 | 用户点 |
| 2 | **explicit / bold** | 露骨、NSFW、硬核、**大胆** | 性器/连接/湿润可写清 | **是（默认）** |
| 3 | **max** | 最色、拉满 | 最色姿势包 + 湿/敞开/高潮边缘写满 | 用户点 |

**默认句（未指定尺度）：**  
按 **explicit** 写：身体与性征可读；**若用户未点具体行为**，默认 **solo-display 敞开自展**，不默认插入、不默认颜射中出。

用户说「大胆一点 / 正常色 / NSFW」→ 保持或确认 explicit。  
用户说「最色」→ max + 最色姿势包。

---

## 2. 暴露 / 服饰梯度 E0–E4

| 级 | 名称 | 英文种子 | 何时 |
|----|------|----------|------|
| **E0** | 完整着装情欲 | fully clothed erotic tension, fabric cling, pose only | 用户要穿衣色/clad-sex 未脱 |
| **E1** | 半褪 | half-undressed, exact heights of clothes written | 偷情、撞见、速战 |
| **E2** | 内衣/蕾丝 | lingerie detailed straps and lace | 用户说内衣/私房 sensual |
| **E3** | 外翻/拨开 | bra everted / fabric pulled aside, still worn | 展示重点 |
| **E4** | 全裸或只留道具 | nude, optional collar/heels/ribbon only | 用户说全裸/最色/只留项圈 |

**默认暴露（尺度 explicit 且未说衣服）：**  
优先 **E1 half-undressed** 或 **E2 lingerie**（私房感强、比突然全裸自然）。  
用户说全裸/一丝不挂/只剩项圈 → E4。  
用户说穿衣做 → E0 + clad-sex。

**铁律：** 禁止无视用户「不要全裸」而升 E4；禁止用户要 soft 却写插入全裸（除非改口）。

### 2.1 年轻女内衣 / 体毛 / 黏膜（未指定才填）

| 维 | 未指定时 | 禁止当默认 |
|----|----------|------------|
| 内衣套（early twenties） | 成套、她会买的：蕾丝三角/细肩带 + 同套低腰，可加小蝴蝶结 | 素色棉一片、浅米「薄款打底」、无花边无结 |
| 阴毛 | **白虎**：光滑无毛、无绒无胡茬 | `natural dark patch` / 默认一片阴毛 |
| 黏膜（露阴户时） | 粉嫩内唇 | 褐、灰、暗玫瑰当默认 |

用户点阴毛/体毛/深色黏膜则覆盖。熟女/用户要体毛再写。

---

## 3. 行为默认

| 用户情况 | 默认行为 |
|----------|----------|
| 只说「写个色情 / 大胆」无细节 | **solo-display**（自展敞开）+ explicit |
| 提到门/撞见/偷情 | **caught** 或 hotel-affair |
| 做爱/插入/体位名 | **intercourse** + 对应体位 |
| 口/深喉 | **oral** 对应 |
| 自慰 | **masturbation** |
| 事后 | **afterglow** |
| 未提体液结局 | **不写** creampie/facial（点了再写） |
| 未提幻想 | **F0 现实** |

---

## 4. 人种 / 年龄默认

```
an adult East Asian woman in her early twenties, mature facial proportions, clearly adult
```

| 用户说 | 处理 |
|--------|------|
| 未提人种 | **强制 East Asian** |
| 亚洲/东亚/华人 | East Asian |
| 日本/韩国等 | 可写 nationality 或保持 East Asian + 壳 |
| 白人/黑人/混血等 | **覆盖**，去掉默认东亚 |
| 未提年龄 | early twenties |
| 熟女/MILF | mid/thirties+ mature |
| 少女感 | youthful-adult + **adult 锁**，禁 teen |

男主未指定人种：默认 **adult East Asian man**（群戏次要可虚）。

---

## 5. 场景默认

未指定 → **bedroom** 或 **hotel**（钨丝）二选一；有日系词 → hotel；有浴 → bathroom/shower。

---

## 6. 与 figure / youth-seduction 路由

| 用户说法 | 去哪 |
|----------|------|
| 人体摄影/街拍/旅拍/证件/完整着装写真 | **figure-photo-prompt** |
| 少女私房/居家柔美/窗边针织 **不要露点** | **figure** soft-boudoir SFW |
| 纯欲暗示、独处暧昧、不露骨 | **youth-seduction-prompt** |
| 露骨/NSFW/插入/自慰敞开/最色 | **本 skill erotic-prompt** |
| 先软后硬 | 可先 figure 再「升级 erotic」同一连续锁 |

---

## 7. 默认填充一览（选题解析用）

```
人种: East Asian adult woman（未覆盖时）
年龄: early twenties
尺度: explicit（大胆）
行为: solo-display（无更具体行为时）
暴露: E1 half-undressed 或 E2 lingerie
场景: bedroom 或 hotel
幻想: F0 none
人数: solo
镜头: low-angle medium close-up vertical cinematic
出片: 叠 asian-erotic-p0-p2 妆发肤锁
```
