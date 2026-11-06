# electrodynamics/ — AEG reading of classical electrodynamics

This directory holds one formal manuscript, two manuscript inserts, and their
verification artefacts.  It was produced by consolidating five working
discussions into a single LaTeX document, with every claim either traced to a
proved statement of the AEG manuscripts (`~/AEG/aeg-paper`), declared as a
dictionary hypothesis, or recomputed in place.

## Sources (the working notes, unchanged)

| file | content |
|---|---|
| `费曼图.md` | ideal-point → ordinary-point threading family as a Feynman history sum |
| `勒让德形式.md` | Legendre duality between the charge projection and the Reeb quotient |
| `电动力学讨论-01.md` | Coulomb's sign rule from the contact curvature $\mu\lambda\propto q_1q_2$ |
| `电动力学讨论-02.md` | direction angle, Ampère force, ripple compression, Møller/Bhabha |
| `电动力学讨论-03.md` | moving poles, projective torsion, Bohr–Sommerfeld quantization |

## Deliverables

| path | what it is |
|---|---|
| **`tex/aeg-electrodynamics.pdf`** | the consolidated manuscript: 46 pages, English body, Chinese reading guide before each section |
| `tex/aeg-electrodynamics.tex`, `tex/sections/*.tex` | its LaTeX sources; build with `tex/build.sh` (xelatex + ctex) |
| **`inserts/paper-0-pole-covariance.tex`** | *mirror* of Paper 0's Subsection 4.4 (poles: covariance, rigidity) — canonical copy now lives in the paper |
| **`inserts/paper-4-transport-density.tex`** | *mirror* of Paper IV's Subsection 4.8 (transport density, normalisation, edge-by-edge witness) |
| `inserts/verify-integration.sh`, `inserts/build-paper{0,4}-integrated.log` | checks the integrated state on scratch copies and records the numbers the new statements carry |
| `verify-notes.py`, `verification-report.txt` | 29 symbolic/numeric checks, all passing |
| **`BRANCH-COLLISION-2026-11-01.md`** | 2026-11-01：与 AEG **PR #21**（`paper-1/handle-surgery-annular-interfaces`）的对撞分析。编号平移表（Thm 10.12 → **10.19** 等，由 `tools/check-aeg-numbering.py` 实测）、**PR #21 改写了 capping 推论 (3)**、与我这轮工作的互补关系、建议整合顺序 |
| **AEG 规则集（2026-11-01）** | GitHub 规则集 **`all-branches-ci`**（id 26278108，`~ALL`）生效：所有分支要求 `scope-checks`、`finite-example`、`build-foundational-papers`、`research-checks` 通过，禁删除、禁强推；**admin 保留 bypass（可直推 main）**。详见 `BRANCH-COLLISION` 同级的会话记录 |
| **AEG 正式清单漂移（诊断）** | `~/AEG/aeg-paper/research/formal-inventory-drift/`：`paper-0/formal/inventory.json` 自 `99f15bc` 起过期（提交 95 条 vs 现场 102 条，+7 条在 `03-aes-and-motion.tex`，9/22 源文件摘要变化）。**只读诊断，未修**；`symbolic-derivations` 因此红但**不在** required checks 里 |
| **`tools/check-aeg-numbering.py`** | 可复用的印刷号校验器：把 `.tex` 的 label 与 PDF 的实际编号配对，核对我文档里登记的引用。main 当前全绿；PR #21 分支报 8 处平移。支持 `--shift-table`（打印编号平移表，合并后回灌用） |
| **AEG 正文已更新（2026-11-01）** | `paper-1/sections/08-caps-and-interface-disks.tex` 新增 **Remark 10.13**（$\mu\ne0$ 充分而非必要）与 **Remark 10.15**（第 (2) 支非空）；编号顺延：原 Cor 10.13 → **10.14**、原 Def 10.14 → **10.16**。构建 `./build.sh 1` 通过（57 页） |
| **`pants-v7-translation/`** | 2026-10-31：把 AEG 的 A3 翻译回缝上（`verify_bridge.py` + `evidence-bridge.json` + `README.md`）。枢纽：**"常值边界 ⟺ 平凡表示 $j=0$"**（W1）。W2 的表：$j=0$ 缝与横向 $j=1$ 缝**都**给 4 个非零组合，但支撑集互补、后者才有 $\theta$ 依赖 ⇒ "16→4"不是物理的签名；V4 实测的 $25/13$ 跨度正好排除标量缝。W3：A3 与 V4 是同一缺陷两侧。W4：V6 的 X4"张力"消散——两者都在说 $j=0$。同时交付 AEG 侧草稿 `PROPOSED-REMARK.tex` |
| **`pants-v6-interface/`** | 2026-10-31：把"缝的态空间 + 沿缝的转动"装进接口记录（`verify_v6_interface.py` + `evidence-v6-interface.json` + `README.md`）。扩展 $\mathcal I_e^+=(D_e,C_e;\sigma_e,r_e,\beta_e;V_e,\langle\cdot,\cdot\rangle_e,U_e)$。$\dim V_e=1,U_e=\mathbb 1$ 时精确退回 AEG 标量读数；极点留数 $=\frac12(1+\cos\theta)$ 有限；AEG 的"缝两侧定向相反"= 配对 $V\otimes V^*\to\mathbb C$（光子号差 $(2,1)$，取正定部分才 4/16）；并给出"Thm 10.12 管的是解析厚化而非拓扑层"这一**可证伪**读法 |
| **`pants-v5-labels/`** | 2026-10-31：M2 的最小尝试（`verify_v5_labels.py` + `evidence-v5-labels.json` + `README.md`）。精确符号代数：只给 CG 不变量张量 + 缝上的表示空间（取横模）+ 沿缝的 Wigner $d^1(\theta)$，四个非零振幅精确等于 $\pm\frac12(1\pm\cos\theta)$，自旋平均 $\propto(1+\cos^2\theta)$ —— **没有用旋量**。并证明"16 剩 4"等价于两个费米子对各自反平行（纯标签 + 规范）。M2 因此是**四件事**（标签／C 选择定则／不变量张量／缝的态空间与转动），而不是一件 |
| **`pants-v4-kernel/`** | 2026-10-31：M1 的最小尝试（`verify_v4_kernel.py` + `evidence-v4-kernel.json` + `README.md`）。精确代数：有理核 $1/\sigma$ 能以局部化进值层、且与 fiber product 可交换（K1–K3）；但代价是**极点处值层塌成零环**（K4）；并且同一 $\sigma$ 下不同拆分的权重不同（峰谷比 $25/13$），故权重**不是**接口值的函数（K5）。结论：M1 改写作"缺纤维上的测度"，且与 M2 不独立 |
| **`pants-v3-marking/`** | 2026-10-31：V3 的构造器 + 标记层（`verify_v3_marking.py` + `evidence-v3-marking.json` + `README.md`）。侧表面由粘合公式重建（不含 V1 代码）：$\chi=\sum(2-p)=2-2\beta_1-b$、$L=g$、树级裤子分解数 $=(2b-5)!!$、$b=4$ 的三分解 $=s/t/u$；7 条负对照。并据它修正了 `particle-physics` 图集里 6.1.2(b) 的接线错误 |
| **`pants-v2-qed/`** | 2026-10-31：V2-QED 的执行结果（`verify_v2_qed.py` + `evidence-v2-qed.json` + `README.md`）。几何层逐字取自 AEG 的 OQ-096 V1 检查器；新增语义层（守恒／确定性／前像计数）。核心结论：装饰**不进入**几何，因此"换装饰再跑"不构成证据（这一条已作为 falsifier 撤回） |
| **`pant-vs-feynman-01.md`** | 2026-10-31：把 $e^+e^-\to\mu^+\mu^-$ 用 AEG Paper I 第 10 章的 Pant 语言写一遍；与 OQ-096 V1 的已验证实例逐项对照（同一流形），并列出 Pant 语言当前缺的六项 M1–M6 |

Manuscript structure: §1 notation and the five dictionary hypotheses, §2
ideal-point histories, §3 Legendre duality, §4 Coulomb, §5 Ampère, §6 radiation,
§7 projective torsion, §8 scattering, §9 bound states, §10 status ledger,
appendices A–D (exact computations, curvature normalisation, radial action,
register of verified identities and of the repairs made to the AEG sources).

## The five dictionary hypotheses (not theorems)

H1 charge ↔ additive step (positron = reflection conjugate);
H2 depth $e^{-M}\leftrightarrow\ell_0/r$;
H3 contact pairing $\mu\lambda\leftrightarrow$ interaction energy;
H4 velocity ↔ world-line tilt $\theta$;
H5 nonvanishing projective holonomy ↔ radiation.

Every physical conclusion in the manuscript is conditional on these; the
mathematical content (operator fiber, dual tearing, cross-ratio holonomy, Borel
reduction, radial action) stands without them.

## Changes applied to the AEG sources (2026-10-20)

Three commits in `~/AEG/aeg-paper`, on `main`, not pushed.

### Commit 1 — `b43ac15` "Repair unresolved cross-references and a stale open problem"

Minimal, no mathematics changed:

1. `paper-4/sections/03-projective-quotients.tex` — added `\label{ex:f7-counts}`
   to the $\mathbb{F}_7$ example (Example 3.8).
2. `paper-4/sections/04-condensation-and-continuation.tex` — retargeted
   `prop:telescoping` → `prop:exact-transport-telescope` and
   `eq:chart-projector` → `eq:local-projector`; added
   `\label{rem:reductive-connection}` to Remark 4.12.
3. `paper-4/sections/13-boundaries-and-programme.tex` — the projective-torsion
   open problem is replaced by a paragraph recording its resolution
   (Theorem 4.11, Example 4.13) and leaving open only the normalisation
   question.
4. `paper-0/sections/09-contact-of-tearing.tex` — four further unresolved
   references found in the same pass and repaired (`prop:reeb-quotient` →
   `prop:p0-contact-quotient`, `eq:contact-form` →
   `eq:arithmetic-contact-form`, `thm:charge-descent` → `thm:p0-descent`,
   `prop:surface-never-closes` → `prop:p0-surface-does-not-close`).
5. `governance/paper-IV-closure-report.md` — dated status amendment recording
   items 1–3.

### Commit 2 — `6c036dc` "Add the pole-covariance subsection to Paper 0 and the transport-density subsection to Paper IV"

The two files were added under `paper-0/sections/04b-pole-covariance.tex` and
`paper-4/sections/04b-transport-density.tex`, each wired with one `\input` line,
and both PDFs rebuilt.  In the same commit, the display of the cross-ratio
holonomy in Paper IV was repaired: it carried a prose fragment
(`tr(...)^{-1}-normalized`) and overflowed the margin by 29.5pt.

Result: Paper 0 builds at 92 pages with new Subsection 4.4 (Lemma 4.6,
Proposition 4.7, Remarks 4.8–4.9) and Paper IV at 59 pages with new
Subsection 4.8 (Lemma 4.14, Corollary 4.15, Propositions 4.16–4.17,
Example 4.19).  Neither paper has an undefined reference; Paper IV has no
overfull line.  `inserts/verify-integration.sh` re-checks all of this on scratch
copies, so the AEG checkout and its tracked PDFs are left untouched.

### Commit 3 — `7d282e9` "Fix the sign, the factor, and a stale equation number in the connection remark"

Raised in review of Paper IV Remark 4.12 and repaired there:

* the solder component θ₊ = Φ⁻¹(1+ab)⁻¹da was evaluated on the Borel sector as
  −Φ⁻¹da; with a = −ξ the correct value is θ₊|_{b=0} = Φ⁻¹da = −e^{−M}dξ, i.e.
  **minus** Paper 0's left Maurer–Cartan form — the minus belongs to the step,
  not to the definition;
* the remark identified the first-order expansion of Λ(□) with
  (1+ab)⁻²da∧db without a coefficient, although dω_H = 2(1+ab)⁻²da∧db and the
  transport density is −(1+ab)⁻²da∧db; the remark now carries the derivation
  and points forward to §4.8, which identifies the halved connection;
* the citation "Paper 0, Equation (58)" was stale — the left Maurer–Cartan
  translation form is Equation (60) in the current Paper 0, and (58) is an
  unrelated formula.

§4.8 was realigned in the same commit: the duplicated curvature computation was
removed from Proposition 4.17 (it now cites the remark's identity), and
Remark 4.18 states the factor exactly — to first order the holonomy of ω_H is
Λ(□)², not Λ(□).

The second review comment — eight unresolved references in the new subsections —
describes the snapshot *before* commit `b43ac15`.  Evidence: the committed PDF of
the previous commit (`100896c`) contains exactly 5 `??` in Paper 0 and 3 in
Paper IV, matching the reported 5 + 3; `b43ac15`, `6c036dc` and `7d282e9` contain
none, and a from-scratch clone build reports 0 undefined references in both
papers.
