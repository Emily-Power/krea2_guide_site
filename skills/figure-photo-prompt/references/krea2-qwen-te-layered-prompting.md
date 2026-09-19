# Krea 2 / Qwen TE · 分层写法（figure-photo）

> **给执行者的规则（新对话直接可用）**  
> 1. 用 **完整英文句** 写形态 A，按 **六层** 组织信息。  
> 2. **高密四段版式强制**：`This is a…` / `Main subject:` / `Environmental background:` / `Composition and atmosphere:`，**段间空行**；首句含摄影类型+定格。  
> 3. 默认全文约 **200–380 英文词**；Main 约 **100–180 词**。  
> 4. 缺信息 → **补层（一句）**；不要靠同义形容词灌水。  
> 5. 需要压缩 → 先砍环境/重复；**永不砍动作与主光**；不砍四段空行。  
> 6. Seedream：同一结构，可更精炼；鼓励附形态 B。

---

## 1. 默认技术栈（写稿时假定）

| 项 | 默认 |
|----|------|
| 模型 | **Krea 2** |
| 文本编码 | Comfy **CLIPLoader type=`krea2`** + 权重 `qwen3vl_4b_*`（Qwen3-VL-4B） |
| 句式 | 自然语言完整句；少标签墙；少 `(word:1.3)` |
| 强调方式 | **语序靠前** + 具体名词；需要时换词复述一次 |

用户点名 Seedream / 即梦 / Flux / SD → 见 §4 与 `model-prompting.md`。

---

## 2. 六层栈（强制）

| 层 | 写什么 | 落点 | 压缩时 |
|----|--------|------|--------|
| **L1** 镜头 | 角度·景别·画幅·媒介 | `This is a…` | 保留一句 |
| **L2** 动作 | 重心·相位·支撑·任务朝向 | Main 前部 | **不砍** |
| **L3** 身份衣 | 成人+人种·服装备 | Main 中 | 保留 |
| **L4** 材质 | 1 种表面写透即可 | Main | 可只留 1 种 |
| **L5** 光 | 主光方向·落在哪块体积 | Main 末或 Comp | **不砍** |
| **L6** 场调 | 2–4 锚点·情绪·质量词×1–2 | Env + Comp | **先砍** |

冲突：`用户原话 > L2 > L5 > L3 > L6`。  
一帧一个主动作；至多一个修饰（如中步 + 雨反光）。

### 句模（交付时展开为带空行的四段）

```
L1  This is a [angle] [distance] [aspect] [still] with [genre photography]: photoreal adult frozen [phase].
L2  An adult East Asian ID. [Support + weight + action phase]. [Hands/tool].
L3  [Outfit/gear exact].
L4  [One fabric/medium catching light].
L5  [Key on which volume] → Comp.
L6  Env: [2–4 anchors]. Comp: [frame fill] [key+fill/rim] [DOF] [mood] [quality].
```

---

## 3. 篇幅（可执行目标）

| | Main | 全文形态 A |
|--|------|------------|
| **默认目标** | **100–180** 词 | **200–380 词** |
| **Turbo / 略短** | 90–150 | 180–320 |
| **上限（再长先压缩）** | — | **约 420 词** |

| 段 | 建议词数 |
|----|----------|
| This is a… | **35–70** |
| Main subject | **100–180** |
| 第二人（若有） | 25–55 |
| Environment | **40–80**（可压到 2 锚点） |
| Composition | **40–75** |

- 偏短且缺重心/光 → **补 L2/L5**，不加 water 词。  
- 偏长 → 删 Env 装修、Comp 重复、同义光效；**保留 L2/L5**。  
- 同一事实只写一次。

---

## 4. 分模型

| 目标 | 怎么做 |
|------|--------|
| **Krea 2（默认）** | 六层 + 上表篇幅；完整句 |
| **Krea Turbo** | 缩 L6；保 L1–L2–L5 |
| **Seedream / 即梦** | 同一六层与五标准；**用更少词写准**；默认可出 A，**鼓励附 B**（约 30–100 词 / 5.x 可约 50–150）；编辑用 keep/change |
| **Flux（点名）** | 中长自然语 |
| **SD/Pony（仅点名）** | 标签风；短；**非默认** |

---

## 5. 注意力卫生

1. 完整句；空间关系写清（left/behind/weight on…）。  
2. 景别匹配细节：远景/航拍不写五官毛孔。  
3. 正向写「要什么」；少堆「不要/无」。  
4. 丢弃：`score_9`、hashtag 墙、空 quality 刷屏。  
5. style ref / 一个摄影类型 > 十个画风形容词。

---

## 6. 自检

- [ ] 六层可指认  
- [ ] 全文约 200–380 词（或用户要 B / 未超约 420 词）  
- [ ] **四段版式：空行 + 首句摄影类型 + Main 全链**  
- [ ] L2 动作、L5 主光可读  
- [ ] 材质≥1；人种默认 East Asian 或用户覆盖  
- [ ] SFW  

详：`output-prose-quality.md` · `model-prompting.md`
