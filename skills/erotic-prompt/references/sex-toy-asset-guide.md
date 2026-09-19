# 性玩具道具资产指南（sex-toy-asset-guide）

**用途**：写仿真性玩具（飞机杯/名器/倒模）的道具描述，或把性玩具做成一整张 Krea2 道具资产图（产品转面图/结构卡）时读本节。道具结构图的具体规范见 `../../krea2-prop-asset-prompt` skill（面板职责、准入检查、闭环测试），本文件只锁定"性玩具这类道具"的事实与已验证写法。

## 一、锁定的分区结构（设计事实）

飞机杯（名器/倒模）内部分区——从入口到最深端，模拟真实阴道的分区设计：

| 分区 | 视觉事实 |
|---|---|
| 入口 | 紧致光滑环（tight smooth ring），收紧段 |
| 通道中段 | 横向环状褶皱带（transverse ringed folds），以浅沟槽分隔；入口端最密最隆，向深处渐缓 |
| 深段 | 通道收窄，隆起光滑圆润的宫颈状台座（cervical mound / rounded dome），深棕粉 |
| 末端 | 宫颈中央小软开口（small soft central opening）→ 软壁小囊腔（pocket chamber，子宫腔式封闭端；封闭末端靠排气制造真空吮吸） |

材质：软高弹仿真肌肤（soft high-elasticity skin-mimicking，TPE 系）；外皮暖自然肉色、柔雾光泽、肤表微纹理；内衬比外皮更深湿润粉（deeper moist pink）+ 细密水珠高光（fine bead-like moisture highlights）；通道四周保留实心圆润材料（solid rounded material）。

背景事实（理解用，不写死进提示词）：真实产品通道深度约 14–15 cm、内径约 1–3.5 cm、软胶 400–950 g。

## 二、Krea2 四段式资产图模板（已验证 · 2026-09）

画幅 4:3，面板 2×2，每格职责唯一：
1. **俯视外阴 hero**（slightly elevated top-down view of the vulva end）——信息量最高
2. **直立正视**（straight-on front view, eye level）
3. **纵剖面**（longitudinal cross-section / product cutaway）——分区结构全在一张图
4. **微距**（macro close-up：外阴唇部 + 肤表微纹理）

完整模板（复制可用，上次验证通过版）：

```
This is a 4:3 photographic prop asset sheet rendered as one continuous studio plate on a bright seamless pure white background, presenting a single realistic male masturbation cup in four named view positions arranged in a two-by-two grid and separated by measured intervals of empty white space. The upper-left position is the hero view: a slightly elevated top-down view of the vulva end, showing the full moulded vulva, the vaginal entrance and how it sits on the circular end face of the cylinder. The upper-right position is a straight-on front view of the same upright cylinder at eye level, showing the outer silhouette, the overall proportions and the vulva profile rising from the top end face. The lower-left position is a longitudinal cross-section of the same object, cut open down its central axis and shown to the viewer like a product cutaway, revealing the solid wall thickness around the narrow channel and the channel in full section: a tight smooth ring at the entrance, dense transverse ringed folds lining the inner walls, and at the deepest section a raised smooth rounded cervical mound with a small central opening leading into a small closed pocket chamber. The lower-right position is a macro close-up of the same vulva and the surrounding skin surface, showing the soft labia detail and the fine skin-like micro-texture of the flesh-toned material.

Main subject: one single realistic male masturbation cup with a solid cylindrical body, a vertical cylinder slightly taller than it is wide, cast in a realistic soft high-elasticity skin-mimicking material in warm natural flesh tones, with a soft matte sheen, subtle skin-colour variation and a fine micro-texture like real human skin. A naturalistic vulva is moulded into the top end face of the cylinder, with full soft labia forming a defined vaginal entrance between them. Inside, a deep closed-end vaginal channel runs from the entrance down into the body, entered through a tight smooth ring, its interior lined with soft transverse folds that encircle the channel like wavy rings separated by shallow grooves, the folds thickest and most raised near the entrance and gradually calming towards the deepest section, where the channel narrows over a raised smooth rounded cervical mound in deep brownish pink with a small soft central opening, the opening leading into a small softly lined pocket chamber at the very end; the whole inner lining is a deeper moist pink than the exterior skin and softly glistens with fine bead-like moisture highlights, with solid rounded material left around the whole channel. The object is presented clean and undamaged in its resting state. The same one physical object appears identically in every panel: the same cylinder dimensions and proportions, the same flesh-toned skin-like material, the same vulva shape, the same labia, the same vaginal entrance, the same tight entrance ring, the same narrow channel, the same transverse ringed folds, the same deeper pink lining, the same cervical mound and the same pocket chamber, with all full-object views aligned to the same vertical centre line and the same bottom base line.

Environmental background: one continuous bright seamless pure white studio plate extends edge to edge behind and beneath all four view positions, evenly exposed with a single consistent white value, and only measured intervals of empty white space separate the panels. Each view of the object rests on the same white plate with restrained contact shadows only, giving a soft physical foothold without any visible seam, table edge, shadow ramp or tinted ground that would break the pure white field.

Composition and atmosphere: the elevated top-down view is the information-leading hero because one glance reads the complete vulva design, the vaginal entrance and the circular end face together; the straight-on front view adds the outer silhouette, the height-to-diameter proportions and the vulva profile in elevation; the longitudinal cross-section lays the whole interior open in one view like a product cutaway — the tight entrance ring, the dense ringed folds, the deep brownish cervical mound and the small closed pocket chamber, all wrapped in the solid flesh-toned body wall; the macro panel carries the soft labia detail and the skin-like micro-scale surface that the wider panels cannot hold. The two full-object panels keep one consistent display scale and one common base line, and every object sits fully in frame with comfortable white margins. A smooth neutral studio light from a large soft source renders the soft matte sheen of the flesh tones with gentle micro highlights along the rounded barrel, keeping each anatomical and material surface readable while the warm skin-toned realism carries a restrained, tactile, lifelike character.
```

## 三、翻车教训（4 轮生成验证）

| 症状 | 根因 | 最小修补 |
|---|---|---|
| 入口画成小圆孔 | 写 `single open entrance` 糊词 → 模型套圆柱模板 | 写死外阴 + 入口环 + 褶皱 + 宫颈 + 囊腔全链 |
| 剖面画成空腔/隧道 | 剖切句没描述"切面"本身 | cutaway 句必含 `cut open down its central axis` + `facing the viewer` + `solid wall thickness`；壁厚与切面材质同外皮 |
| 褶皱画成洞口外波纹 | 褶皱只写"环绕"，没绑定剖面分区 | 按分区序写：入口环 → 褶皱带 → 宫颈台座 → 囊腔 |
| 深处画成光球/空洞 | 只写 dome 没写开口与后继腔 | 写 `central opening leading into a small closed pocket chamber` |
| 3/4 面板与正视重复 | 圆柱对 3/4 角度不稳定，生成两份正面 | 删冗余面板，换缺失信息维度（剖面或往里看透视） |
| 剖面连翻 3 轮 | 模型上限，非提示词问题 | 换"往里看"透视视图（deep top-down view into the channel，模型稳定）；仍不行 → 用户供参考图做图像参照 |

**词汇陷阱**：
- 避免 `cervix` 医学术语——Krea2 会染上解剖内镜图画风；用 `cervical mound` / `rounded dome in deep brownish pink` 等自然语。
- 真人参考图的气泡/飞沫 → 改为 `fine bead-like moisture highlights`（留湿润质感、去生理杂相）。
- 中文"横截面"按上下文取**沿中轴纵剖面**（只有这个切法能看到分区结构）；用户想要的若只是垂直于轴的环形截面，需单独说明。

## 四、事实来源

- 阴道皱襞解剖（横向环状、沟槽分隔、入口端最密、内衬粉红湿润）：IMAIOS e-Anatomy（Vaginal rugae）、Elsevier Complete Anatomy（Mucosa of Vagina）、StatPearls（Vaginal Structure and Function）。
- 产品内部分区（收紧环/环状褶皱/宫颈+子宫腔囊/封闭端真空）：ToysHeart Level Ninety-Nine（双子宫腔 + 宫颈纹理环）、KOKOS Hanna/Jenny（G/P/A 点分区）、Magic Eyes Lolinco Virgo（紧致通道 + 真空子宫）、对子哈特（颗粒/褶皱纹理）等产品资料；中文科普见知乎《飞机杯与倒模名器的区别》。
