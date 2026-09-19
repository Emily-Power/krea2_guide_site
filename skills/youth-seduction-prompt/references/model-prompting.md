# 模型族提示策略（youth-seduction）

默认服务 **本地 ComfyUI · Krea 2 + Qwen3-VL TE**。  
题材始终是 **纯欲暗示**，不因模型换成标签墙或 explicit。

分层与篇幅 → [`krea2-qwen-te-layered-prompting.md`](krea2-qwen-te-layered-prompting.md)

---

## 1. Krea 2（默认）

| 项 | 建议 |
|----|------|
| 加载 | CLIPLoader **type=`krea2`** + `qwen3vl_4b_*` |
| 句式 | 完整英文句；七层 |
| 篇幅 | Main 100–180；全文 200–380；**高密四段空行版式** |
| 强调 | 姿 + **暗示焦点** + 主光靠前；少 `(w:1.3)` |
| 质量词 | 末尾 ×1–2：`masterpiece, best quality` |
| 丢弃 | score_9、hashtag、sexy/hot 空喊、teen |

用户问「怎么加载」→ 答 type=`krea2` + qwen3vl 权重即可，不展开无关工作流。

### Krea Turbo

缩 L7 环境；**保留 L2 姿 · L3 暗示 · L6 光**。全文可 140–260 词。

---

## 2. Seedream / 即梦

| 项 | 建议 |
|----|------|
| 结构 | **同一七层** 与五标准 |
| 风格 | **更短更准**；少重复 |
| 输出 | 形态 A 可；**鼓励附形态 B**（约 30–100 词） |
| B 顺序 | shot → adult East Asian ID → pose+implication → clothing state → gaze → setting → light → quality |
| 编辑 | 用户要改图时用 keep/change 类说明（若工作流支持） |

---

## 3. Flux（仅点名）

中长自然语言；同样七层信息；可略散文化。不默认。

---

## 4. SD 1.5 / SDXL / Pony（仅点名）

短标签兼容，**非默认**。若用户坚持：

```
adult woman, early twenties, east asian, bedroom, oversized shirt, midriff, collarbone, half-lidded eyes, warm lamp, looking at viewer, detailed skin
```

仍禁：`teen, loli, nsfw, pussy, penetration` 等（本 skill 边界）。  
质量标签可少量；不要 score 刷屏。

---

## 5. 图生视频（用户要动效时）

静帧仍出形态 A；释义后附：

```
Motion: [one clear present-tense action, 1–2 sentences]
```

例：`Motion: she slowly lifts the slipped strap and lets it fall again; eyes stay on the mirror.`  
一帧一主动作；勿 undress + walk + turn 连打。

---

## 6. 负向（形态 D 扩写提示）

通用：

`child, teen, loli, underage, aged down, extra fingers, fused limbs, bad anatomy, deformed hands, nsfw, nude, genitals, explicit sex, ahegao, watermark, text, flat lighting, oversharpen`

着装要求严时加：`topless, underwear only, nipples`  
镜面场景加：`mismatched mirror reflection`  

---

## 7. 自检（模型维）

- [ ] 未点名时按 Krea A 交付  
- [ ] Seedream 已考虑附 B  
- [ ] 无跨生态垃圾标签  
- [ ] 未因「模型更色」越界到 erotic  
