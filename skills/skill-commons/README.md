# Skill Commons — 三线公共层（非独立 skill）

本目录不是可调用 skill，只给三条线 9 个领域 skill 共用：

| 线 | 导演（剧本） | 静帧（文生图） | 视频（MiniMax H3） |
|----|------------|---------------|-------------------|
| 露骨 | `erotic-director` | `erotic-prompt` | `erotic-prompt-minimax` |
| 纯欲 | `youth-seduction-director` | `youth-seduction-prompt` | `youth-seduction-minimax` |
| SFW | `figure-photo-director` | `figure-photo-prompt` | `figure-photo-minimax` |

## 文件

| 路径 | 职责 |
|------|------|
| [`references/routes.md`](references/routes.md) | 三线路由：9 skill 分工、环节判断、线判断、兜底 |
| [`references/boundaries.md`](references/boundaries.md) | 全体系公共硬边界（成人锁、人种默认、名人/RP、对白 BGM） |
| [`references/defaults.md`](references/defaults.md) | 全体系公共默认填充（人种/年龄/时长/画幅/镜头/人数） |

**约定**：三线同构的路由、边界、默认只写在这里；各领域 SKILL.md 引用本层并只保留**本线特有**的判别句、禁区与默认。改公共规则先改这里，9 个 skill 跟着读，不要各抄一份。

- 三线共享的 H3 视频规范在 `../minimax-h3-core/`，不是这里。
- 无人体题材的通用 MiniMax 提示词走 `minimax-h3-r2va-enhanced-prompt`，不读本层。
