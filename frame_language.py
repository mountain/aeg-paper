#!/usr/bin/env python3
"""三孔标架语言（frame language）：一对三维标架 + 每个孔的标签与定向。

设计要点
--------
1. **三维标架**：坐标轴的标签固定为 (时, 孔, 构)，顺序即规范序。
     · 时  —— 相位索引，模 n（理想态 n = 4，即 90° 一步）
     · 构  —— 结构索引，即"在哪台计算机上"，模 3
     · 孔  —— 从当前构出发要穿越的那条边（相邻对），由 (构, 定向) 决定
   `定向` ∈ {+1, -1} 是标架的定向；`手性` 是轴序相对规范序的奇偶（±1）。

2. **一对儿**：`FramePair` 同时持有正转标架与反转标架 —— 对应"正转反转同时发生"。
   两个标架各自带满 (时, 孔, 构) 与定向、手性。

3. **孔也是对象**：`Hole` 带有自己的标签 (时, 孔, 构) 与定向、手性，
   即"这个孔在哪一刻、是哪条边、从哪个构到哪个构、朝哪个方向"。

4. **三个变换必须区分开**（仓库里明确要求：镜像、时间反演、路径取逆不可混同）：
     · 时间反演  reverse_time  : 定向 ↦ -定向，时 ↦ -时
     · 镜像      mirror        : 交换 孔 与 构 两个轴，手性 ↦ -手性
     · 路径取逆  path_inverse  : 把一串孔倒序并对每个孔取反方向

5. **分级结构**（与 04-hyperoperation.md §14 对齐）：
   `compose` 满足"指标相加、系数相乘"；`Spec` 是该分级下的支撑。
"""

from dataclasses import dataclass, replace
from itertools import permutations

LABELS = ("时", "孔", "构")          # 规范轴序
N_TIME = 4                           # 相位周期（90° 一步）
N_STRUCT = 3                         # 结构周期（三台计算机）

PAIRS = [("Rust", "Python"), ("Python", "Ada"), ("Ada", "Rust")]


def pair_index(c_from: int, c_to: int) -> int:
    """相邻对的编号（无向）：Rust-Python=0, Python-Ada=1, Ada-Rust=2。"""
    s = {c_from, c_to}
    for i, (a, b) in enumerate(PAIRS):
        if s == {i, (i + 1) % N_STRUCT}:
            return i
    raise ValueError(f"{c_from} 与 {c_to} 不是相邻对")


# --------------------------------------------------------------- 标架
@dataclass(frozen=True)
class Frame:
    时: int                    # 相位索引，模 N_TIME
    构: int                    # 结构索引，模 N_STRUCT
    定向: int = +1             # +1 = 正转，-1 = 反转
    手性: int = +1             # 轴序奇偶

    def __post_init__(self):
        if self.定向 not in (+1, -1) or self.手性 not in (+1, -1):
            raise ValueError("定向与手性只能取 ±1")

    @property
    def 孔(self) -> int:
        """从当前构出发、按定向要穿越的那条边。"""
        return pair_index(self.构, (self.构 + self.定向) % N_STRUCT)

    def labels(self) -> tuple:
        """(时, 孔, 构) —— 三个轴的取值。"""
        return (self.时 % N_TIME, self.孔, self.构 % N_STRUCT)

    def axes(self) -> tuple:
        """带名字的轴：按规范序给出 (标签, 取值)。"""
        t, h, c = self.labels()
        return tuple(zip(LABELS, (t, h, c)))

    def step(self) -> "Frame":
        """走一步：时与构同时按定向推进（这就是流动）。"""
        return replace(self,
                       时=(self.时 + self.定向) % N_TIME,
                       构=(self.构 + self.定向) % N_STRUCT)

    def hole(self) -> "Hole":
        """当前这一步所穿越的孔，作为对象，带上自己的标签与定向。"""
        c_to = (self.构 + self.定向) % N_STRUCT
        return Hole(索引=self.孔, 时=self.时, 构_从=self.构, 构_到=c_to,
                    定向=self.定向, 手性=self.手性)

    # ---- 三个不可混同的变换
    def reverse_time(self) -> "Frame":
        return replace(self, 定向=-self.定向, 时=(-self.时) % N_TIME)

    def mirror(self) -> "Frame":
        """交换 孔 与 构 两个轴：孔轴取值变成原构轴取值，反之亦然。"""
        t, h, c = self.labels()
        return replace(self, 时=t, 构=h, 手性=-self.手性)

    def canonical(self) -> "Frame":
        """把 时/构 都归到非负代表元。"""
        return replace(self, 时=self.时 % N_TIME, 构=self.构 % N_STRUCT)


@dataclass(frozen=True)
class Hole:
    """一个孔：带 (时, 孔, 构) 标签与定向、手性。"""
    索引: int
    时: int
    构_从: int
    构_到: int
    定向: int = +1
    手性: int = +1

    def labels(self) -> tuple:
        return (self.时 % N_TIME, self.索引, (self.构_从, self.构_到))

    def reversed(self) -> "Hole":
        """同一个孔的反方向穿越（孔本身不变，方向与两端互换）。"""
        return replace(self, 构_从=self.构_到, 构_到=self.构_从, 定向=-self.定向)

    def name(self) -> str:
        a, b = PAIRS[self.索引]
        arrow = "→" if self.定向 > 0 else "←"
        return f"{a}{arrow}{b}"


@dataclass(frozen=True)
class FramePair:
    """一对儿标架：正转与反转同时存在。"""
    正: Frame
    反: Frame

    @staticmethod
    def at(时: int, 构: int) -> "FramePair":
        f = Frame(时=时, 构=构, 定向=+1)
        return FramePair(正=f, 反=f.reverse_time())

    def step(self) -> "FramePair":
        return FramePair(正=self.正.step(), 反=self.反.step())

    def rendezvous(self) -> tuple:
        """两个方向是否在同一点相遇：(时, 构) 是否一致。"""
        return (self.正.时 % N_TIME == self.反.时 % N_TIME
                and self.正.构 % N_STRUCT == self.反.构 % N_STRUCT)

    def time_gap(self) -> int:
        """两个方向在'时'上的差（校准残差的来源）。"""
        d = (self.正.时 - self.反.时) % N_TIME
        return min(d, N_TIME - d)


# ------------------------------------------------- 分级结构（权重语言）
def compose(a: dict, b: dict) -> dict:
    """括号：指标相加、系数相乘（再乘 (n − m)，与 [L_m, L_n] = (n−m)L_{m+n} 对齐）。"""
    out: dict = {}
    for m, dm in a.items():
        for n, dn in b.items():
            out[m + n] = out.get(m + n, 0) + dm * dn * (n - m)
    return {n: c for n, c in out.items() if c != 0}


def spec(j: dict) -> list:
    """Spec_op = 分级支撑：只做指标加法、系数相乘与非零判断。"""
    return sorted(n for n, c in j.items() if c != 0)


def ad_E(j: dict) -> dict:
    """[E, ·]：按权重分次。"""
    return {n: n * c for n, c in j.items() if n * c != 0}


# --------------------------------------------------------------- 路径
def walk(start: Frame, steps: int) -> list:
    """从某个标架出发走若干步，返回标架序列。"""
    out, f = [start], start
    for _ in range(steps):
        f = f.step()
        out.append(f)
    return out


def path_inverse(holes: list) -> list:
    """路径取逆：倒序 + 每个孔反向。"""
    return [h.reversed() for h in reversed(holes)]


def apply_holes(frame: Frame, holes: list) -> Frame:
    """按一串孔推进标架（孔的 时/构 与标架脱钩，只取方向）。"""
    f = frame
    for h in holes:
        f = replace(f, 定向=h.定向).step()
    return f


def chirality_of(order: tuple) -> int:
    """给定轴序，返回相对规范序 (时,孔,构) 的排列奇偶。"""
    canon = list(range(len(order)))
    idx = [LABELS.index(l) for l in order]
    inv = sum(1 for i in range(len(idx)) for j in range(i + 1, len(idx)) if idx[i] > idx[j])
    return -1 if inv % 2 else 1


if __name__ == "__main__":
    print("轴序手性检查（相对规范序 (时,孔,构)）:")
    for p in permutations(LABELS):
        print(f"   {p} → 手性 {chirality_of(p):+d}")
