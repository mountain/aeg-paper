# Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes（奇异零几何与管）

*Branched Pullbacks, Arithmetic Zero Networks, and Topological Transport*

本目录包含一份处于数学审查中的草稿手稿：

> **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**
> *Branched Pullbacks, Arithmetic Zero Networks, and Topological Transport*

其规范源与生成产物是 `aeg-paper-3.tex` 与 `aeg-paper-3.pdf`。

## 草稿状态

这里的 **draft** 描述的是编辑与出版成熟度：概念组织、行文、图件以及正文–图件的整合仍在
开发中。它不是 `governance/` 中的数学论断状态标签，也不改变任何单个结果的状态。

本手稿研究 Paper I 所建立的正则零理论的边界。其核心区分在于：总零集、光滑零曲面、
局部平凡真管、嵌入或穿线管、辫闭包与纽结不变量之间。这些是不同层次的结构；后面的层次
不能仅由前面的层次推出。

## 从 Paper I 导入

- 正则与奇异 AES 定义；
- 正则零定理；
- 光滑总零集与投影淹没命题；
- properness 警告；
- 双边射影算子 $z\mapsto z+s$ 与 $z\mapsto-1/z$。

Paper II 提供了算术全纯性与普通全纯性的正则轨迹识别。本手稿所使用的所有奇异拉回与锥
计算都在此处重新证明。

## 已证明结果与严格边界

本手稿证明：

- 一个显式共形实现定理与有限/可数多重零模型；
- 一个全纯分支拉回定理：局部度 `m` 给出 `2m` 个零支、锥角 `2 pi m` 与一个本质临界点；
- 一个精确的 `q=4` Hecke–Hauptmodul 奇异 AES，其零集是 `{infinity,4}` Hecke 网络，包括
  符号特征下降与尖点/锥完备性边界；
- 符号覆盖的完备粗 AEG 曲面与柱面 `C*` 的全局等同；保留双曲 orbifold 后，其单位切丛在
  标准尖点紧化下是 `S^3 minus T(2,4)`；
- 一个多项式穿线载体族 `z^2=t^m`：其实虚部载体有亏格 `m-1`、四个边界分量与 `2m` 个鞍点
  重连，而其根闭合到 `T(2,m)`；判别式绕数、辫指数与负 Euler 特征数的一半都等于 `m`；
- 由 `q=4` 提升尖点斜率导出 `u^2=t^4` 的标记环面推导，连同精确损失 `P_2 -> B_2 -> S_2`：
  根置换平凡，但保留的纯辫坐标与环绕数为二；
- 一个内在对数–正切精细化：紧化标记符号覆盖在加权分次环中恢复 `U^2-V^4` 作为其尖点除子
  截面，其加权 Hopf 圆丛恢复同一个 `T(2,4)` 尖点链环；两个可能的 `Q(sqrt(2))` 二次扭曲
  仍是一个被声明的下降选择；
- 一个四股中心扩张校准，其中二阶 Garside 路径与四阶旋转路径具有相同的全扭残差；其积分
  核特征有等于单位切 Euler 类的 LHS 越界；这些多项式根路径是提供的，该特征不是 Paper I
  的仿射 torsion，且它们尚未由不受限历史生成；
- 一个固定的六次实验室 `x^6-x-t`：其五个显式径向消失半扭生成整个 `B_6`，紧超椭圆提升
  以满 `Sp_4(Z)` Gauss–Manin 像实现每个亏格二映射类；
- 相应的 Lyashko–Looijenga 遗忘映射：事件多项式 `Q_0(t)=t^5+5^5/6^6` 恰有 `1296` 个
  坐标归一化六次提升，或 `216` 个残差源旋转轨道；这些计数不作为非同构曲线计数宣传；
- 一个显式的 LL–Igusa 孪生：`x^6-x` 的源旋转轨道之外的第二个提升具有相同的 `Q_0`，但
  其 `t=1` 亏格二曲线有由二次 Igusa–Clebsch 不变量与判别式构造的不同绝对比，证明事件
  多项式遗忘了真正的复模量；
- 度-`216` 商覆盖可观测量把其叶值打包成带迹–范下降的单值谱多项式；规范平均分出常数并
  给出在 `Q_0` 处有精确正下界的单值不变有限纤维方差，而不声称沿 LL 基中每条开路径恒常；
- 沿两条显式 `t` 铅笔比值为 `((t-beta)/t)^5`，在两个正则纤维处带平衡除子电荷
  `5[beta]-5[0]`；这是对数电荷，不是有限 Dirichlet 能量；
- 算术纤维 `y^2=x^6-x-1`，其分支多项式有 Galois 群 `S_6`、其 Jacobian 有几何自同态环
  `Z`，连同对已证明几何孪生的开放满 `216` 轨道普查与算术、周期、标记单值精细化；Hodge
  或 Siegel 度量能量比较也仍开放；
- 从本原双曲 `q=4` 历史到 Hecke 周期轨道纽结的满射算子商映射，连同显式尖点环绕转数和
  与零 dessin 编码脊柱定理；
- 一个相对零除子定理，分离原始历史、射影算子、端点相等、系数域素分量、几何叶、Galois
  作用与分析单值；
- 两个带强制端点方程的提供寄存器模型：二次覆盖 `u^2=t`（其端点除子遗忘标记历史）与
  四次 `(u^2-t)^2-3`（其算术不可约性、几何分量、判别式、单值与 Frobenius 循环是显式的）；
- 一个标记前缀迹与普通极点余循环，区分射影中性词 `omega_4` 与空历史；
- 一个秩-`r` 参数化零截面与真管定理；
- 圆上紧无边实零管的环面结构定理，带全局定向垂直切丛；
- 一个带已计算分量、覆盖与边界传输的紧螺旋管；
- 奇异 AEG Morse 分岔与独立复分支模型 `w^2=tau`；
- 真有限根辫单值，以及由 Paper II 的算术全纯场实现每个辫；
- 对数根提升规范定律；
- 标量/仿射新颖性过滤器，包括一个非零共振扭曲上同调类，其平面经典链环状态和仍然坍缩
  为 Alexander-quandle 染色计数。

它**不**声称多重零模型的全局分类、与 AEG 流相容的一般奇异性正规形定理、每个族的
properness、内在实零到辫的函子、函子式穿线选择、新的 Markov 归一化 AEG 纽结不变量，或
超越 Alexander/Burau 的分离。特别是：

- `q=4` 纽结映射与有限寄存器构造在其末端层次穿过射影算子分解；从标记历史到相对素除子
  的一般函子仍开放；
- 二维零 dessin 是经典模板的编码脊柱，本身不是纽结、链环、零管或三维模板；
- 测地流模板与尖点环绕公式是经典输入；不从其 AEG 实现推断任何新纽结不变量；
- 延伸 `q=4` 环面边界线的径向亏格三载体是提供数据，纯辫扩张不是单位切中心扩张或 Paper I
  的切片 torsion；独立的四股比较只有在其根路径被提供后才与中心扩张匹配；
- `1296` 个 LL 提升是归一化多项式实现，不是 `1296` 个两两非同构曲线，且既没有一个 LL 叶
  也没有一条参数环被某个一般标记算术历史选中；孪生定理只证明至少两个源旋转轨道给出不同
  模量，而不是对所有 `216` 个轨道的分类；
- 光滑总零集不自动是管；
- 管不自动是嵌入或穿线管；
- 辫级数据不自动是纽结不变量；
- 视觉管构造不确立同痕或 Markov 不变性。


## 强度修正（2026-11-09）

第 9.1 与 9.5 节区分固定赋值与固定度量，以及内在零曲线长度与环境距离。在紧连通曲面上，
固定赋值共形族坍缩为一个点，而不是带内在度量的零曲线。精确距离需要留在域内的梯度路径；
面积使用显式单侧 coarea 密度。柱面捷径、圆盘边界阻碍与半面积柱面仍作为回归示例保留。

修正后的论断与历史排除登记于 `../governance/05-mathematical-status.md` 的 S-0011。用以下
命令运行显式检查：

```bash
python3 paper-3/scripts/verify-intensity-collapse.py
python3 -O paper-3/scripts/verify-intensity-collapse.py
```

这些是有限见证，不是对一般紧性论证的计算证明。参见
`../governance/paper-III-intensity-revision-2026-11-09.md` 了解修订审计与验证边界。

## 构建

从仓库根目录用以下命令构建本手稿：

```bash
./build.sh 3
```

全部手稿命令为：

```bash
./build.sh
```

## 源布局

```text
paper-3/
├── aeg-paper-3.tex
├── sections/
│   ├── 01-singular-aes.tex
│   ├── 02-local-zero-models.tex
│   ├── 03-multi-zero-constructions.tex
│   ├── 04-arithmetic-zero-networks.tex
│   ├── 04-parameter-discriminants.tex
│   ├── 05-q4-geodesic-knots.tex
│   ├── 05-polynomial-threaded-carriers.tex
│   ├── 05-sextic-ll-laboratory.tex
│   ├── 05-history-divisor-naturality.tex
│   ├── 05-regular-tubes.tex
│   ├── 06-singular-fibers.tex
│   ├── 07-monodromy-and-braids.tex
│   └── 08-threading-and-knot-questions.tex
└── appendices/
    ├── app-A-regularity-and-properness.tex
    ├── app-B-configuration-and-braid-background.tex
    └── app-C-affine-quandle-calculations.tex
```

## 历史源文件族与溯源警告

- 多重零、`E_k`、`E_log` 与管笔记（仅历史动机）；
- 遗留 `sections/sec04.tex` 与 `sec09.tex` 中与管相关的部分；
- `notes/knots-and-loops/` 与 `images/sources/` 下与纽结相关的文件；
- 关于管、辫单值与 Markov 不变性的重组讨论。

`E_k` 与 `E_log` 记号是历史研究标签，不是已确定的模型类。对当前树与 249 个 Git 提交的
扫描未发现以任一名称存在的可验证一般构造。本手稿中的公式是重新推导并审计的，而非静默
归于那些标签。`../governance/` 下的权威范围与状态记录优先于所有遗留溯源来源。

## 集成记录

- [`../governance/paper-III-source-audit.md`](../governance/paper-III-source-audit.md)
- [`../governance/decisions-paper-III.md`](../governance/decisions-paper-III.md)
- [`../governance/paper-III-closure-report.md`](../governance/paper-III-closure-report.md)
