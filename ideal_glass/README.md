# AEG ideal-glass prototype

这是一个可直接运行的 Python 原型，用来把札记中的 AEG 变量与协议族落到数值实验上。

它实现了：

- `P0` conventional baseline
- `P1` radii-minimized baseline
- `P2` triangulation-like repair protocol
- `P3` Scale -> Repair
- `P4` Repair -> Scale
- `P5` interleaved micro-steps
- `P6` reverse from ideal-like state

并在每个记录阶段计算：

- `m_contact, z_contact, a_C`
- `a_G`
- `v, ΔM, r_t, A_t, M_t, τ_disc`

在最终态计算：

- `phi_J`
- `K0, G0`
- `D(ω)` 代理（小系统）
- `chi_tilde_small_k`
- `C6(r), xi6, psi6_abs_mean`
- `g2(r), tau_tr`
- `T_m_proxy, phi_m_proxy`（仅作探索性代理）

## 重要说明

这不是对 Corwin 等人算法的逐行复现，而是一个 **AEG 研究原型**。当前版本采用了若干近似：

1. `repair graph` 用周期边界下的 `k` 近邻图近似，而不是严格的 periodic radical Delaunay / regular triangulation。
2. `a_C` 取自近接触图；`a_G` 取自 repair graph 上的约束残差。
3. `G0`、`D(ω)`、`T_m_proxy`、`phi_m_proxy` 都是工作代理，不应直接等同于论文中的精确物理量。
4. 程序的目的，是先检验札记里的协议几何、缺陷量与 ACS 编码是否具有稳定信号，而不是一步到位重建完整 ideal-glass 数值体系。

## 运行

### 1. 先做冒烟测试

```bash
python run_experiments.py --smoke-test --outdir smoke_results
```

### 2. 做小规模试跑

```bash
python run_experiments.py \
  --n-list 256 512 1024 \
  --num-seeds 4 \
  --fast \
  --outdir pilot_results \
  --workers 4
```

### 3. 做预定规模扫描

```bash
python run_experiments.py \
  --n-list 256 512 1024 2048 4096 8192 \
  --num-seeds 20 \
  --protocols P0 P1 P2 P3 P4 P5 P6 \
  --outdir full_results \
  --workers 8
```

较大规模建议先关闭最重的部分：

```bash
python run_experiments.py \
  --n-list 256 512 1024 2048 4096 8192 \
  --num-seeds 20 \
  --skip-thermal \
  --dos-max-n 256 \
  --outdir full_results \
  --workers 8
```

## 输出结构

每个 `(N, seed)` 会生成：

- `config.json`
- `summary_rows.json`
- `P0/ ... P6/`
  - `stages.json`
  - `observables.json`
  - `final_state.npz`

总目录下还会生成：

- `summary.csv`
- `config_used.json`

## 后处理

```bash
python analyze_results.py --summary full_results/summary.csv
```

它会输出：

- `matched_P4_minus_P3.csv`
- `matched_P2_minus_P1.csv`
- `finite_size_summary.csv`
- `regressions.csv`
- `protocol_means.csv`
- `analysis_report.md`

## 建议的首轮执行顺序

1. 先跑 `N = 256, 512, 1024`，每个 3–4 个 seed，确认程序稳定。
2. 优先检查 `P3` vs `P4` 的配对差值是否在 `a_G` 与 `tau_disc` 上显著分离。
3. 再把 `P0/P1/P2` 的层次关系看清：`a_C, a_G, phi_J, K0, G0, chi_tilde_small_k`。
4. 最后再把规模推到 `4096, 8192` 做有限尺度分析。
