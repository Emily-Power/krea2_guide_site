# 公共维度目录 2026（L1→L5 + 专属 · **v4 五轮全网加厚**）

> **公式：** `Skill = 公共(L1→L2→L3→L4→L5) + 专属`  
> **库文件：** `dimension_items.py` + `dimension_items_extra.py` + **`dimension_items_rounds.py`（R1–R5）**  
> **规模 v4：** 公共 **≈935** · SUBJECT **≈175** · FIGURE≈957 · Youth≈1012 · Erotic≈1060  

## 五轮加厚做了什么

| 轮 | 焦点 | 内容 |
|----|------|------|
| **R1** | cloth L2–L5 | 内衣分类学(teddy/bustier/garter…)·礼服·运动泳装·鞋色图案面料 |
| **R2** | set L3 | 中式地标(外滩/西湖/洪崖洞/重庆赛博/园林…)·书店中庭/拍贴/桑拿/露营… |
| **R3** | pose/light/cam | 芭蕾街舞职业任务姿·主光方位光比反光板器材凝胶·构图裁切 |
| **R4** | hair/makeup/expr/grade | 更多发质编发·编辑妆件·微表情·**Portra/Fuji/CineStill/Tri-X 胶片谱** |
| **R5** | 专属+道具+收口 | Youth美学/行为·Erotic体位幻想E细·Figure广告标签·道具科技/塔罗… |

## 点菜基数（必读）

**group 级 S/M/V/H** → [`dimension-select-policy-2026.md`](dimension-select-policy-2026.md)  
（例：发型 **L2造型只 1**，可叠刘海/发态；道具可横向多选。禁止五发型主造型同写。）

## L1 一览

| L1 | 下钻 | 基数摘要 |
|----|------|----------|
| subject/cast | 人种/年龄/体型/人数关系加厚 | 人种/性别 X；年龄体型 V；人数 V |
| hair | 造型·刘海·态·色·质 L2–L4 | **造型 S** · 态 M(2) · 余 S |
| makeup | 妆壳·妆件 L2–L3 | 壳 S · 件 M(3) |
| expr | 表情·分轨·视线 L2–L3 | 壳 S · 视线 S |
| cloth | 品类·裙裤内衣礼服·状态·鞋配·面料色图案 **最厚** | 品类槽各 S · 状态/配 M |
| pose | 站走靠坐卧跪运动表演任务 | 大姿跨族 1 · 细姿 M(2) |
| prop | 生活/职业/幻想道具 | **H** M(4) |
| set | 城/室内/户外/地标/特殊 | 主场 1 · 锚可叠 |
| light | 自然实用棚·方位光比·器材色温 | 主光型 1 · 辅光 M |
| cam | 景别角度画幅·焦段光圈·构图 | 各轴 S · 构图 M(2) |
| grade | 电影调色·**胶片库存模拟**·数码感 | 主 look 1 |

## 专属

- **Figure：** zone A–I + 广告/品类标签  
- **Youth：** I 级·暗示·美学壳（含 dark feminine / cottage / coastal…）  
- **Erotic：** 行为体位·**E0–E4（含 E 细）**·幻想·权力 — **≠ 衣着品类**

## 重建

```powershell
cd skill-guide-site
python scripts/gen_dimension_static.py   # public≈935
python scripts/build_director_catalog.py
```
