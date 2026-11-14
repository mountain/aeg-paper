# Pan/Encke 边缘波：紧缠绕密度波色散与径向波长（OQ-104.1）

> **文档性质**：算术表达式几何（AEG）研究笔记（之七：OQ-104.1——解紧缠绕密度波色散关系，得边缘波径向波长 `λ(Δr)` 并与观测对照）
> **前置依赖**：笔记七《Pan 与 Encke 缝隙边缘波》（[007-pan-encke-farey.md](007-pan-encke-farey.md)）
> **日期**：2026-11-14
> **可运行见证**：[008-encke-density-wave-witness.py](008-encke-density-wave-witness.py)（纯 Python `math`，无第三方依赖）

---

## 一、色散关系（紧缠绕 WKB）

Pan 的第 m 阶密度波（图样速度 `ω = mΩ_P`）在紧缠绕（WKB）极限满足自引力 + 压强的色散关系

```
(ω − mΩ)² = κ² − 2πGΣ|k| + c²k² ,   κ = Ω（Kepler 本轮频率）
```

其中 `Σ` 是环面密度、`c` 是速度弥散、`k` 是**径向**波数。令去谐 `D = (ω−mΩ)² − κ²`（共振处 `D=0`）。

## 二、闭合解（k 的二次方程）

`c²k² − 2πGΣk − D = 0`，得尾随波（`k>0`）

```
k = [2πGΣ + √((2πGΣ)² + 4c²D)] / (2c²)
```

共振处 `D=0`：`λ₀ = 2π/k = c²/(GΣ)`。取 `Σ=500 kg/m²`、`c=0.5 cm/s`：

```
λ₀ = c²/(GΣ) ≈ 749 m ≈ 0.75 km
```

**关键**：`k` 是 `D` 的**闭合二次式**，本步不需要 OQ-104.2 预想的多元求解器（那是给全色散 `(m,k)` 联合解 + 边界条件用的）。

## 三、结果：`λ(Δr)` 曲线

| m | r_res | 方位角波长 `2πr/m` | 径向 λ（Δr=0） | 径向 λ（Δr=2 km） | 径向 λ（Δr=10 km） |
| ---: | --- | ---: | ---: | ---: | ---: |
| 551 | a_P+161.6 km | 1525 km | 0.749 km | 0.630 km | 0.445 km |
| 100 | a_P+889.1 km | 8449 km | 0.749 km | 0.721 km | 0.639 km |
| 20 | a_P+4416.5 km | 43354 km | 0.749 km | 0.744 km | 0.723 km |

**结论**：径向波长 `λ ≈ 0.75 km`（由 `c²/GΣ` 设定），随距共振距离**单调减小**（"wrapped-up"螺旋）。方位角波长 `2πr/m` 是另一个（固定 m 时恒定）量。

## 四、与观测对照

Tiscareno 等（DPS 2005，abstract 64.02）对 Encke 缝隙边缘的观测："**wavelength in some regions does not remain constant but varies smoothly in a repeating pattern**… wavy edges are ubiquitous… covering 360° of longitude on both sides."

这正是**密度波 wrapped-up 螺旋的签名**：径向波长随距共振距离平滑变化、且不被碰撞高效阻尼（`timescales ≳ 10 months`）。因此**色散关系是正确的框架**，本笔记把 OQ-104.1 的"解色散"这一步闭合。

## 五、状态与边界

| 编号 | 结论 | 状态 |
| --- | --- | --- |
| D1 | 色散关系 `(ω−mΩ)²=κ²−2πGΣ|k|+c²k²` 及闭合解 | `PROVED WITH STATED HYPOTHESES`（WKB + 二次方程） |
| D2 | 共振处 `λ₀ = c²/(GΣ) ≈ 0.75 km` | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` |
| D3 | 径向波长随 Δr 减小（wrapped-up），匹配"波长平滑变化"观测 | `COMPUTATIONALLY VERIFIED EXAMPLE` + 观测对照 |
| D4 | 与观测**具体**波长的定量匹配 | `OPEN`（需澄清观测量是径向还是方位角波长 + 更准的 Σ/c；见 OQ-104.1 收尾） |

**诚实边界**：本步解的是**径向**波长（~0.75 km，随 Δr 减小）。观测里"波纹"的**具体数值**（几十 km 还是 km 级）与这里的径向波长是否直接对应，取决于观测量定义与 `Σ,c` 取值——这一步留作 OQ-104.1 的收尾，不在此过度断言。OQ-104.2 的"多元求解器"对本步**不必要**（二次闭合式），只在做全色散（m,k 联合、边界条件）时才是真正的能力缺口。

## 六、登记

本笔记不修改论文正文、不升级既有 claim。它把 OQ-104.1 的"解色散 + 得波长曲线 + 观测对照"落地，并登记进 [governance/notes-reserve-audit.md](../../governance/notes-reserve-audit.md) §2.9；OQ-104.1 状态在 [governance/08-open-questions.md](../../governance/08-open-questions.md) 更新为 `ADVANCED`。研究问题与方向：苑明理；本分析、见证与状态标注：DeepSeekHarness，2026-11-14。
