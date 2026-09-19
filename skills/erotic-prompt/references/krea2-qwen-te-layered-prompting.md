# Krea 2 / Qwen TE · 分层写法（erotic-prompt）

> **给执行者的规则（新对话直接可用）**  
> 1. 用 **完整英文句** 写形态 A，按 **七层** 组织；有行为必须有 **连接点整句**。  
> 2. **高密四段版式强制**：`This is a…` / `Main subject:` / `Environmental background:` / `Composition and atmosphere:`，**段间空行**；首句含摄影类型+定格。  
> 3. 默认全文约 **200–400 英文词**；Main 约 **100–180 词**。  
> 4. 缺信息 → **补连接/姿/光**；不要堆 sexy/hot。  
> 5. 需要压缩 → 先砍环境与次要 fetish；**永不砍连接点与主光**；不砍四段空行。  
> 6. Seedream：同一结构，可更精炼；鼓励附形态 B（连接靠前）。

---

## 1. 默认技术栈

| 项 | 默认 |
|----|------|
| 模型 | **Krea 2** |
| 文本编码 | Comfy **CLIPLoader type=`krea2`** + `qwen3vl_4b_*` |
| 句式 | 自然语言完整句；少标签墙 |
| NSFW | 本地写清连接/解剖；**仅 18+** |

---

## 2. 七层栈（强制）

| 层 | 写什么 | 落点 | 压缩时 |
|----|--------|------|--------|
| **L1** 镜头 | 角度·景别·画幅 | `This is a…` | 保留一句 |
| **L2** 大姿势 | 膝髋开合·支撑·朝向 | Main 前 | 高 |
| **L3** 连接/暴露 | 插入/口/展示写死；或 solo 敞开 | Main 核心 | **不砍** |
| **L4** 手服 | 简单手位；E 级精确 | Main | 保留 |
| **L5** 材质 | 汗/涎/油/爱液 1 个具体图像 | Main | 可只留 1 |
| **L6** 光 | 主光落在解剖/结合部 | Main 末或 Comp | **不砍** |
| **L7** 场调 | 2–4 锚·张力·质量词×1–2 | Env + Comp | **先砍** |

冲突：`用户原话 > L3 > L2 > L6 > L5 > L7`。  
一帧一个主动作 + 至多一个修饰（如 doggy + creampie）。

### 句模（交付时展开为带空行的四段）

```
L1  This is a [angle] [distance] [aspect] [still] with [cinematic erotic photography]: photoreal adult frozen [peak].
L2  An adult East Asian ID—[proportions]. [Knees/hips/support].
L3  [Connection whole sentence OR open display — not vague "having sex"].
L4  [Hands simple]. [Clothing state exact].
L5  [One wet/sweat/saliva image].
L6  [Key on junction / breast / face] → Comp.
L7  Env 2–4 anchors. Comp: frame fill; key+rim; DOF; quality.
```

---

## 3. 篇幅

| | Main | 全文形态 A |
|--|------|------------|
| **默认目标** | **100–180** 词 | **200–400 词** |
| **Turbo / 略短** | 90–160 | 180–340 |
| **上限（再长先压缩）** | — | **约 440 词** |

| 段 | 建议词数 |
|----|----------|
| This is a… | **35–70** |
| Main subject | **100–180** |
| Secondary | 25–55 |
| Environment | **40–80** |
| Composition | **40–75** |

短且无连接 → **补 L3**。  
偏长 → 砍 L7/重复 fetish；**保留 L3/L6**。

---

## 4. 分模型

| 目标 | 怎么做 |
|------|--------|
| **Krea 2（默认）** | 七层 + 上表篇幅；连接整句 |
| **Krea Turbo** | 缩 L7；保 L3+L6 |
| **Seedream / 即梦** | 同七层；更精炼；A 可 + **鼓励 B**（连接靠前；约 30–100 / 5.x 约 50–150 词） |
| **Flux（点名）** | 中长自然语 + 连接句 |
| **SD/Pony（仅点名）** | 短标签；**非默认** |

---

## 5. 注意力卫生

1. 主连接 1–2 个；群戏焦点一人。  
2. 景别匹配：要结合部细节 → 够近。  
3. 正向写要什么；丢弃 teen、`score_9`、hashtag 墙。  
4. 动漫：`anime-explicit` + 成人锁。

---

## 6. 自检

- [ ] 七层可指认；有行为则 L3 整句  
- [ ] 全文约 200–400 词（或 B / 未超约 440 词）  
- [ ] **四段版式：空行 + 首句摄影类型 + Main 全链**  
- [ ] L5+L6 各有具体图像  
- [ ] 18+；默认 East Asian 或用户覆盖  

详：`output-prose-quality.md` · `model-prompting-krea2-seedream.md` · `connection-templates.md`
