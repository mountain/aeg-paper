"""exchange.py — 「什么组织了自由的信息交换」：Python 侧

场景与 Rust 侧同一份数据：一组圆 (x, y, r)。两个部件：producer 造数据，consumer 用数据。
观察点同样是三条：值怎么过去、谁持有引用、什么时候能改。
差别在于：这里三条都默认“自由”，组织它们的东西不在语言声明里，而在运行时的对象图与解释器上。

运行：python3 exchange.py
"""

import sys
import threading
import time
from dataclasses import dataclass


@dataclass
class Circle:
    x: float
    y: float
    r: float


def producer(n: int) -> list:
    return [Circle(x=0.5, y=0.0, r=1.0) for _ in range(n)]


# 边界 A：按“序列协议”接收 —— 不声明类型，只看有没有 __iter__
def consume_by_protocol(seq) -> float:
    return sum(c.r for c in seq)


# 边界 B：按“可变序列协议”接收 —— 不声明别名规则，直接就地改
def consume_by_mutation(seq) -> None:
    for c in seq:
        c.r *= 2.0


class LazyCircles:
    """只实现 __iter__，没有继承任何东西，也不需要注册。"""

    def __init__(self, n):
        self._n = n

    def __iter__(self):
        for i in range(self._n):
            yield Circle(x=float(i), y=0.0, r=0.25)


def race(kind: str, n_threads: int, n_rounds: int):
    """四种写法做同一件事：把共享计数器加 1。

    tight  : 紧循环里的 counter[0] += 1（读改写三步相邻）
    call   : 读和写之间夹一次普通 Python 函数调用（调用点是解释器的让出点）
    yield_ : 读和写之间夹一次 time.sleep(0)（显式让出）
    lock   : 同 yield_，但整段包在 Lock 里
    """
    counter = [0]
    lock = threading.Lock()

    def touch():
        pass

    def bump():
        for _ in range(n_rounds):
            if kind == "tight":
                counter[0] += 1
            elif kind == "call":
                v = counter[0]
                touch()
                counter[0] = v + 1
            elif kind == "yield_":
                v = counter[0]
                time.sleep(0)
                counter[0] = v + 1
            else:
                with lock:
                    v = counter[0]
                    time.sleep(0)
                    counter[0] = v + 1

    threads = [threading.Thread(target=bump) for _ in range(n_threads)]
    t0 = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return counter[0], n_threads * n_rounds, time.time() - t0


def main():
    print("== (1) 值怎么过去：默认共享，不复制 ==")
    a = producer(3)
    b = a
    print(f"  b is a: {b is a}，id 相同: {id(a) == id(b)}，引用计数: {sys.getrefcount(a)}")
    consume_by_mutation(b)
    print(f"  通过 b 就地改过之后，a 里第一个圆的半径 = {a[0].r}（a 从未被提到）")
    c = a[:]                                   # 只有显式切片/复制才断开
    consume_by_mutation(c)
    print(f"  显式切片后 b 不再受影响：a[0].r = {a[0].r}，c[0].r = {c[0].r}")

    print("== (2) 接口由协议决定，而不是声明 ==")
    print(f"  list      -> {consume_by_protocol(producer(4))}")
    print(f"  生成器     -> {consume_by_protocol(x for x in producer(2))}")
    print(f"  自定义类   -> {consume_by_protocol(LazyCircles(4))}")
    print("  三者都能过边界：边界不检查类型，只检查运行时有没有 __iter__")

    print("== (3) 什么时候能改：由解释器在哪里让出决定，与类型无关 ==")
    sys.setswitchinterval(5e-6)            # 放大切换频率，让让出点的影响显形
    for kind, label in (("tight", "紧循环 += 1        "),
                        ("call", "读改写中夹一次函数调用"),
                        ("yield_", "读改写中夹一次 sleep(0)"),
                        ("lock", "同 sleep(0) 但加锁    ")):
        got, want, dt = race(kind, 8, 100000)
        print(f"  {label}: 得到 {got:>8d} / 应为 {want:>8d}，丢失 {want - got:>8d}  ({dt:.2f}s)")
    sys.setswitchinterval(0.005)
    print("  紧循环不撕裂，是因为解释器不在读改写三步之间让出；一夹进调用点就撕裂。")

    print("== (4) 哪些操作在 GIL 下恰好是原子的 ==")
    shared = []
    def append_many():
        for i in range(50000):
            shared.append(i)                   # 单条字节码：CPython 下不会撕裂
    ts = [threading.Thread(target=append_many) for _ in range(4)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print(f"  4 线程 × 50000 次 append 得到 {len(shared)}，应为 200000")
    print(f"  GIL 当前是否启用: {getattr(sys, '_is_gil_enabled', lambda: 'n/a')()}")
    del shared[:]
    del shared


if __name__ == "__main__":
    main()
