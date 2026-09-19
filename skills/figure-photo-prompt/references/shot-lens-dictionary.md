# 景别 · 镜头 · 视角词典（文生图公式）

> 写入 `This is a…` 与比例铁律。  
> **SFW · 默认 East Asian 人物。**

---

## 1. 景别 Shot Size

| ID | 中文 | 英文种子 | 可写细节 | 禁用 |
|----|------|----------|----------|------|
| **ecu** | 大特写 | extreme close-up | 眼/唇/手纹理 | 全身要求 |
| **cu** | 特写 | close-up on face | 五官、妆、表情 | 脚部 |
| **mcu** | 近景 | medium close-up, head and shoulders | 脸+肩+领 | 全身线 |
| **ms** | 中景 | medium shot, waist-up | 手势、半身服 | 鞋细节 |
| **cowboy** | 牛仔景 | cowboy shot, mid-thigh up | 手+髋+上装 | 远景感 |
| **mls** | 中全景 | medium long shot, knees up | 大半身姿 | 极远 |
| **fs / full** | 全身 | full body, head to toe | 脚进画、全身服 | 毛孔级脸 |
| **ws** | 全景环境 | wide shot, figure in environment | 人+场 | 五官精修 |
| **ews** | 远景小人 | extreme wide, tiny figure | 大姿态剪影 | 任何近距细节 |

**句模：**  
`This is an eye-level [full body / medium close-up / cowboy shot] in vertical 3:4 framing…`

---

## 2. 视角 Camera Angle

| ID | 中文 | 英文 | 效果 |
|----|------|------|------|
| **eye** | 平视 | eye-level | 对等自然 |
| **low** | 略仰/仰 | slight low angle / low angle | 拉长、气场 |
| **high** | 略俯/俯 | slight high angle / high angle | 自拍脸小、图案 |
| **dutch** | 荷兰角 | dutch angle | 失衡（慎用） |
| **otss** | 过肩 | over-the-shoulder | 对话/双人 |
| **pov** | 主观 | POV | 可见自己肢体边缘 |
| **top** | 顶视 | top-down | 地面图案+人 |

---

## 3. 焦距感 Focal Length Feel

| ID | 英文 | 用途 |
|----|------|------|
| **fl-24** | 24mm wide environmental | 环境压迫、全身略畸变（控） |
| **fl-28-gr** | 28mm street snap (GR feel) | 街拍、理光感 |
| **fl-35** | 35mm reportage | 生活纪实 |
| **fl-50** | 50mm natural | 通用半身 |
| **fl-85** | 85mm portrait compression, creamy bokeh | 头肩、美妆 |
| **fl-135** | 135mm tight compression | 远摄压缩、浅景深 |
| **macro** | macro lens detail | 手/眼/首饰 |

---

## 4. 画幅 Aspect

| 用途 | 英文 |
|------|------|
| 小红书 | vertical 3:4 |
| 抖音/Reels | vertical 9:16 |
| IG feed | 4:5 or 1:1 |
| 电影感 | 16:9 or 2.39:1 letterbox feel |
| 证件 | 近似 1:1 或 3:4 头肩 |

---

## 5. 组合公式

```
This is a [angle] [shot size] in [aspect] framing with [fl-xx] feel and [style], freezing [moment].
```

**例：**
```
This is a slight low-angle full body shot in vertical 3:4 framing with 35mm street feel and open shade, freezing mid-stride OOTD.
```
```
This is an eye-level medium close-up in 4:5 framing with 85mm compression and soft butterfly light, freezing a calm professional gaze.
```

---

## 6. 自检

- [ ] 景别与细节等级一致  
- [ ] 全身时脚在画内  
- [ ] 远景无五官毛孔  
- [ ] 自拍常用 slight high + mcu  

---

## 7. 深度续（九轴）

焦距×景别语义、畸变/压缩短语、`This is` 金样 → [`nine-axes-web-fill-2026.md`](nine-axes-web-fill-2026.md) **§7**。
