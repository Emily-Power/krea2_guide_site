# Krea2 静帧构图防崩清单（实战积累）

> 来源：《猎单》全片重制期间 19 张坏图修复实战（2026-08）。写静帧词时先扫本清单，把已知崩坏模式挡在出图前。

## 1. 空间关系构图：选对机位

| 构图 | 崩坏模式 | 解法 |
|------|---------|------|
| 女躺+男跪腿间（侧拍） | 连崩 5 版：模型顽固生成「女坐床边/半坐斜靠」 | **改俯拍机位**（`seen from directly above`）一次命中 |
| 镜面反射双人 | 镜像多生 2-4 个人形（复读癖） | 加硬约束句（见下） |
| 门缝/狭窄视口 | 顽固「塞人」——缝里多出完整人脸 | 只写局部不写人（`only the hand and the phone enter the slit — no face, no body`）；改 4 版无效则接受现状（视频层以词为主） |
| 清新女装+裸腿锁 | 顽固加吊袜带/短袜 | 写死 `SMOOTH BARE LEGS from hem to heel — no socks, no stockings, no garters`；3 轮仍在则作边缘崩收下 |
| 办公大堂 | 漂成咖啡厅（黑板菜单+咖啡机） | 写 `glass-door lobby, wall clock`；点名禁止 chalkboard / espresso |
| 围观有人拍 | 手机塞进**女主**手里 | 写死她两手职责（抓衣/抓包）；`NO phone in her hands`；只有路人可举手机 |
| 衣已落地 | 身上还挂着同一件（双外套） | 写死「该件只存在于地上，身上没有第二件」 |

## 2. 硬约束句式（防多人/复读）

写进 Main subject 段末尾：

```
Only two people exist in this scene: A and B.
The mirror reflects exactly these two and nothing else —
no extra figures, no duplicates, no other passengers.
```

效果实测：E05 电梯镜面图加此句后「4 人崩坏」→「2 人正常」。

## 3. 人种崩坏（外国人脸）

Krea2 对「东亚」约束会漂移，静帧词主体定义里加特征锚点：

```
an East Asian woman's face with distinctly East Asian features —
dark eyes, straight black hair in a claw clip, soft nose bridge
```

审图模板第 1 问有人种检查（`director-produce/scripts/review_images.py`），坏图重出后必须复审该问。

## 4. 性别崩坏

写「an adult man」生成女性面孔时（实战 E06 S13 两次崩），**改成只写身体局部不生成脸**：

```
A man's hand in a white shirt cuff ... his face stays out of frame above,
only his arm, shoulder and shirt cuff in the upper frame — no face generated.
```

## 5. 无主 / 离体性器：朝向与空间

正面胯下机位极易「插反」：龟头对镜头、根埋进她身体，看起来像从她身上长出来。根部贴画框边裁切，模型会把男人身体补出来。

| 崩坏 | 解法 |
|------|------|
| 龟头朝镜头 / 根埋她身体 | 侧面或四分之三；写死 `glans toward her mouth/vulva, root hanging in empty air in front of her` |
| 根贴画框边 → 补出男人躯干/手/第二根 | **整根入画**，囊四周留空，禁止 `root cropped by the frame`；`NO male body, NO hips, NO hand, NO second penis` |
| 写「贴在穴上 / 腿间 / 坐在腿上」 | 变成从她身上长出。改成身前一掌空、肚脐到髋高、`she does not have a penis` |
| 可见男同事胯上长出一根 | 旁观者白衬衫+完整西裤、远景；鸡巴单独漂，禁止接到任何可见男人胯上 |
| 插入特写连崩 | 静帧改用可读的悬空接近（朝向正确即可）；插入动作交给视频词 |

审图：词里有性器则必答第 10 问朝向/空间，不过不进视频。过关几何可克隆已审过的同构图静帧，不要把根裁在画框边。
视频层同句：视频词里性器作为连接物时同样写死「root at his crotch between the hips, NEVER from his belly / NEVER from her body」+ 行为期 `stays bare and visible`（规范 minimax-h3-core `prompt-spec.md` §7）。

## 6. 重出策略阶梯

1. 词没问题 → 换种子（seed + 100000 递增）
2. 连崩 2 次 → 改词（加人种锚点/硬约束句/局部化）
3. 改词 2 版仍崩 → 换机位或换构图策略（俯拍/低机位/空景化）
4. 3 轮无效 → 接受现状（确认核心要素：人种/身份/连接关系已修即可，边缘崩坏不阻塞视频生产）

## 7. 款式品类词 bias 速查（Krea2 实测 2026-08《商场》）

| 写的词 | 模型实际画成 | 解法 |
|--------|-------------|------|
| `sleeveless crop top`（一般） | 帽袖/挂颈打结款、袖头仍在 | 用用户认可图的定版句原文，不要新造 |
| `bandeau`（一字抹胸） | 全盖胸、只露腰腹（「露乳」消失） | 定版句注入 |
| `wrap-top` + neck strings | **比基尼化**：短裤消失、全裸臀、露点 | 显式「完整穿着热裤+高跟、NOT a bikini」+定版句 |
| rolled-up T（卷起） | 卷边高度失控（压乳尖=半露点 / 卷到乳上=尖全露） | **品类改为「剪裁款 cut tee」**而非动作词 |
| `horizontal front slit`（前胸横缝） | 初稿=打结款；**定版句逐字复用后稳定** | 定版句注入（唯一稳妥路径） |
| 性器「未出」状态（布下鼓包） | 整根提前暴露、手错放 | **局部化**：把难画区整段切出画（S3 案例：只画她蹲姿+手指勾皮带扣+裤腰以上，性器区不入画），状态由视频词交代 |

**节奏**：款式 2 版仍漂 → 放弃品类词创作，改用「已确认定版句逐字注入」（全剧服装段=同一句）→ 仍漂 → 局部化；不要再加新形容词。**用户贴图 = 唯一事实基准**，语义化其正视图写定版句。
