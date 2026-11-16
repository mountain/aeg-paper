# Paper III 强度修订审计

**日期：** 2026-11-09。**状态：** 审查中的仓库修订，不是预印本发布。

**基础仓库：** `mountain/aeg-paper`。
**已验证 main commit：** `db06fd057513f94f8da5bdcaf3122b244ab235d6`。
**范围：** Paper III 第 9.1 与 9.5 节、其治理记录与聚焦回归。本审计从属于仓库范围与论断
登记。

## 数学结果

1. **P3-L11 被限制为实际固定的数据。** 固定赋值给出乘积零关联。固定度量只有在同时固定矫正
   带符号坐标时才给出同一载体。在 Euclid 平面上，`a=(mu/lambda)sinh(lambda(x-b(mu,lambda)))`
   满足 eikonal 恒等式，而其零线随任意光滑 `b` 移动。单位重标恒等式仍有效；框架方向不变，
   而向量按 `s^{-1}` 缩放。
2. **P3-L12 不再等同诱导与环境距离。** 零曲线拉回张量与 lambda 无关。环境路径不必留在零集
   中。在乘积柱面上，对跖零点的环境距离趋于零，尽管其内在距离保持 `pi/mu`。
3. **修正后的紧极限是一个点。** 对带边且 dA 处处非零的紧连通光滑 M，共形度量直径趋于零。
   证明使用带非零内部中心的有限网、横截内部路径与支配收敛。它不假定全局可用的梯度轨迹，
   也不断言一般定量速率。
4. **距离公式有正确方向。** 矫正赋值有单位梯度，给出普遍下界。当其归一化梯度路径在域内
   到达零时等号成立。一个圆盘例子显示即使零曲线横截交边界时也是严格的。
5. **面积由两个单侧密度控制。** 若 coarea 密度在零附近满足 `I(c)=I_+ + O(c)` 与
   `I(c)=I_- + O(|c|)`，主导系数是 `pi(I_++I_-)/(2 mu lambda)`。对两个匹配侧恢复旧系数。对
   `[0,1] x S^1`、`A=t`、`mu=1`，面积恰为 `2 pi arctan(lambda)/lambda`，主导项为
   `pi^2/lambda`，而非其两倍。
6. **赋值不随度量下降。** 其振荡保持为正，故 GH 单点上的任何常数都不均匀逼近 A。把 A 限制
   到其零集是不同运算。

移动线、柱面捷径、圆盘访问与单侧面积示例保留在主论文中，而非仅在外部勘误说明中。

## 显式化的假设

- 定性点坍缩定理的紧性与连通性。
- 正固定 mu；lambda 趋于正无穷。
- 诱导张量的光滑零曲线部分，而不声称任意边界零集的全局分层。
- 精确距离上估计的留在 M 内的梯度轨迹。
- 面积速率的独立单侧 Lipschitz coarea 密度假设。
- 紧性不由有界范围取代。在环境族中移除临界点不自动保持紧定理。

## 改变的文件

- `paper-3/sections/04-parameter-discriminants.tex`：修正陈述、证明、边界条件与反例；语义标签
  保留。
- `paper-3/scripts/verify-intensity-collapse.py`：21 个符号/几何见证。
- `.github/workflows/paper3-intensity.yml`：聚焦见证与 Paper III 构建门禁。
- `paper-3/README.md`：修正范围与测试说明。
- `governance/05-mathematical-status.md`：标记 S-0010 为历史并添加 S-0011。
- `governance/03-theorem-dependency-graph.md`：修正蕴含与排除。
- `governance/decisions-paper-III.md`：D3-28 记录修订边界。
- `governance/discussions/aeg-intensity-plane-and-tube-collapse.md`：显著取代警告；旧讨论作为
  历史证据保留。
- 本审计记录。

无材料被移到另一论文或从历史记录删除。Paper 0 未被编辑。未发现依赖定理使用 P3-L11 或
P3-L12。

## 验证

- 全部 34 个物化基线文本文件在固定基础 commit 对其规范 Git blob SHA 值验证。
- `python paper-3/scripts/verify-intensity-collapse.py`：PASS，21 个检查。
- 优化 Python 重放：PASS，字节相同输出。检查不依赖 Python 可移除的 `assert` 语句。
- 现有 `paper-3/computations/ll-igusa-twin/verify-explicit-twin.py`：PASS。
- 独立 AI 数学交叉检查：未发现阻塞问题；横截路径与赋值振荡措辞随后收紧。这不是独立人工
  审查或作者验收。
- `bash build.sh 3`：PASS。构建环境初始未配置的 TeX 格式与字体映射只在临时可写目录中生成；
  未改变源依赖或系统安装。
- 完整手稿 PDF 产出且修订页视觉检查。详细最终 PDF：86 页、877703 字节、SHA-256
  `ec693ee5fd5e5360720202a5d3b39d96091cacecfc2bdc6e8fa9cde1718f97fc`。最终 LaTeX 与 BibTeX
  日志无重要警告、未定义引用或引用、重复标签、缺失字符或 overfull/underfull box。修订页
  57–63 视觉检查无布局问题。
- `git diff --check`：PASS。新 workflow YAML 解析；远程 Actions 执行在 pull request 中与这些
  本地结果分开跟踪。

有限测试守护显式示例与恒等式。它们不替代论文内的一般紧性与 coarea 证明。其他论文与仓库
范围 CI 套件未被重建。

## 未解决边界与下次审查

不声称一般坍缩速率。非紧族、附加边界几何下的速率与装饰度量极限需要单独分析。第二个基本
模型度量族保持不同且无新 GH 断言。

仓库发布与合并随后由作者授权。修订遵循仓库 pull-request 规则；该授权不是独立数学审查或
正式 PR 批准。精确远程检查与合并状态由 GitHub 记录，与本本地审计分开。不声称预印本发布或
部署。
