# Pan 与 Encke 缝边缘波 — 应用示例

本目录存放 **HTWR（Hyperbolic Tropical Wavefront–Residual，双曲热带波前残差）** 框架的一个
自包含应用示例：对土星 Encke 缝扇形（「波浪形」）边缘的两层说明，该边缘由守护卫星 Pan 塑造。

## 论文（双语）

| 语言 | LaTeX 源 | 构建 PDF | 可读 Markdown |
| --- | --- | --- | --- |
| 英文 | `aeg-app-pan-encke.tex` | `aeg-app-pan-encke.pdf` | `pan-encke-paper.md` |
| 中文 | `aeg-app-pan-encke-zh.tex` | `aeg-app-pan-encke-zh.pdf` | `pan-encke-paper.zh.md` |

共享参考文献：`aeg-app-pan-encke.bib`。

## 两层结果（摘要）

1. **算术层（HTWR 贡献）。** Pan 的 Lindblad 共振阶梯 `x = m/(m±1)` 是**共转（`x = 1`）的
   Farey 邻域**，实现为**双曲上半平面上堆积的 Ford 圆** —— HTWR 框架核心有理逼近结构的一个
   具体物理实例。`m = 551` 共振位于 Encke 外缘；缝由 **Chirikov 共振重叠**打开
   （`gap ≈ 8.5 R_H`）。状态：`STRUCTURAL PROPOSAL`（读法）+ 初等天体力学。

2. **动力学层（标准天体力学）。** 观测边缘波既非传播密度波也非（冷或压力）边缘模，而是 Pan
   的**静态潮汐畸变**（受迫本轮），振幅 `GM_P/(κ²d²) ≈ 0.79 km`、方位尺度 ≈ 250 km —— 匹配从
   公有领域 Cassini 图像 PIA08257 提取的值（≈ 0.65 km、≈ 300 km）。状态：
   `PROVED WITH STATED HYPOTHESES` + `COMPUTATIONALLY VERIFIED EXAMPLE`。

两层**互补，非同一现象**：算术骨架解释*缝在哪里*；潮汐畸变解释*为何其边缘呈扇形*。

## 同伴笔记

推导记录于笔记系列 `aeg-paper/notes/general/`：

- `007-pan-encke-farey` — Farey/Ford 共振阶梯与缝开。
- `008-encke-density-wave` — 紧绕密度波色散。
- `009-encke-edge-mode-wkb` — 边缘模排除（冷 + 压力）。
- `010-encke-scalloped-edge-tidal` — 静态潮汐畸变（解决）。

治理：开放项登记为 `governance/08-open-questions.md` 中 **OQ-104**；笔记级状态在
`governance/notes-reserve-audit.md` §2.9。

## 构建

从仓库根：

```bash
./build.sh app        # 构建英文（pdflatex）与中文（xelatex+ctex）PDF
./build.sh all        # 构建论文 0–6 加此应用
```

要求：`pdflatex`、`bibtex`、`xelatex`（中文版需 `ctex`）。

## 溯源

研究方向、对象选择与物理陈述：**苑明理**（通讯作者与科学责任唯一持有者）。推导、精确计算、
图像提取与 LaTeX 准备由 **DeepSeek Harness**（AI 研究代理）协助，记为协助非署名。NASA 图像属
公有领域。
