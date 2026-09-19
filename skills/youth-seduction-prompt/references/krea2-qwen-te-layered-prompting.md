# Krea 2 / Qwen TE · 分层写法（youth-seduction）

> **给执行者的规则（新对话直接可用）**  
> 1. 用 **完整英文句** 写形态 A，按 **七层** 组织信息。  
> 2. **高密四段版式强制**：`This is a…` / `Main subject:` / `Environmental background:` / `Composition and atmosphere:`，**段间空行**；首句含摄影类型+定格。  
> 3. 默认全文约 **200–380** 英文词；Main 约 **100–180** 词。  
> 4. 缺信息 → **补层（一句）**；不要靠 sexy/hot/pure 灌水。  
> 5. 需要压缩 → 先砍环境/重复；**永不砍姿态、暗示焦点与主光**；不砍四段空行。  
> 6. Seedream：同一结构，可更精炼；鼓励附形态 B。

---

## 1. 默认技术栈

| 项 | 默认 |
|----|------|
| 模型 | **Krea 2** |
| 文本编码 | Comfy **CLIPLoader type=`krea2`** + 权重 `qwen3vl_4b_*` |
| 句式 | 自然语言完整句；少标签墙；少 `(word:1.3)` |
| 强调方式 | **语序靠前** + 具体名词；暗示焦点写在 Main 前中部 |

用户点名 Seedream / 即梦 / Flux / SD → 见 §4 与 `model-prompting.md`。

---

## 2. 七层栈（强制）

| 层 | 写什么 | 落点 | 压缩时 |
|----|--------|------|--------|
| **L1** 镜头 | 角度·景别·画幅·媒介 | `This is a…` | 保留一句 |
| **L2** 姿态 | 重心·支撑·膝髋·朝向 | Main 前部 | **不砍** |
| **L3** 暗示焦点 | 锁骨/腰窝/大腿缘/肩带/视线/镜对视 | Main 紧接姿后 | **不砍** |
| **L4** 服饰状态 | 扣子数·领滑·下摆·肩带位置 | Main 中 | 保留 |
| **L5** 材质 | 1 种表面写透（棉/丝/汗湿） | Main | 可只留 1 |
| **L6** 光 | 主光方向·落在暗示区体积 | Main 末或 Comp | **不砍** |
| **L7** 场调 | 2–4 锚点·私密张力·质量词×1–2 | Env + Comp | **先砍** |

冲突：`用户原话 > L3 > L2 > L6 > L5 > L7`。  
一帧一个主暗示；至多一个修饰（如窗边 + 手机屏光）。

### 与相邻 skill 分层对照

| | figure | youth-seduction（本） | erotic |
|--|--------|----------------------|--------|
| 层数 | 六层 | **七层** | 七层 |
| 核心层 | L2 动作 | **L3 暗示焦点** | L3 连接/暴露 |
| 永不砍 | 动作+主光 | **姿+暗示+主光** | 连接+主光 |

### 句模（交付时展开为带空行的四段，勿贴成一层）

```
L1  This is a [angle] [distance] [aspect] [still] with [intimate photography]: photoreal adult frozen [phase].
L2  An adult East Asian early twenties—[proportions]. [Support + weight + pose].
L3  [One clear implication: collarbone / midriff / thigh edge / gaze / mirror].
L4  [Clothing state exact: buttons, straps, hem].
L5  [Fabric or damp skin catching light].
L6  [Key light on implication zone] → 写入 Comp。
L7  Env: [2–4 anchors]. Comp: [frame fill] [key+fill/rim] [DOF] [tension] [quality].
```

---

## 3. 篇幅

| | Main | 全文形态 A |
|--|------|------------|
| **默认目标** | **100–180** 词 | **200–380 词** |
| **Turbo / 略短** | 90–150 | 180–320 |
| **上限（再长先压缩）** | — | **约 420 词** |

| 段 | 建议词数 |
|----|----------|
| This is a… | **35–70** |
| Main subject | **100–180** |
| Environment | **40–80**（可压到 2 锚点） |
| Composition | **40–75** |

- 偏短且缺姿/暗示/光 → **补 L2/L3/L6**，不加 water 词。  
- 偏长 → 删 Env 装修、Comp 重复；**保留 L2/L3/L6**。  
- 同一事实只写一次。  
- **禁止**为省字删掉暗示焦点改成 “sexy pose”。

---

## 4. 分模型

| 目标 | 怎么做 |
|------|--------|
| **Krea 2（默认）** | 七层 + 上表篇幅；完整句 |
| **Krea Turbo** | 缩 L7；保 L1–L2–L3–L6 |
| **Seedream / 即梦** | 同一七层与五标准；**更短更准**；可 A，**鼓励附 B**（约 30–100 词，姿+暗示+光靠前） |
| **Flux（点名）** | 中长自然语 |
| **SD/Pony（仅点名）** | 标签风；短；**非默认** |

---

## 5. 注意力卫生

1. 完整句；空间关系写清（weight on…, strap off left shoulder…）。  
2. 景别匹配细节：远景不写唇釉与毛孔。  
3. 正向写「要什么」；少堆「不要/无」。  
4. 丢弃：`score_9`、hashtag 墙、`sexy, hot, pure desire` 空喊、teen/loli。  
5. 暗示用 **布料状态 + 光 + 局部**，不用 genitals / penetration 词。  
6. style：`cinematic intimate still` / `soft boudoir-adjacent portrait` 一类 > 十个空洞形容词。

---

## 6. 自检

- [ ] 七层可指认  
- [ ] 全文约 200–380 词（或用户要 B / 未超约 420 词）  
- [ ] **四段版式：空行 + 首句摄影类型 + Main 全链**  
- [ ] L2 姿、L3 暗示、L6 主光可读  
- [ ] 材质≥1；人种默认 East Asian 或用户覆盖  
- [ ] 成人 early twenties；无 explicit  

详：`output-prose-quality.md` · `model-prompting.md`
