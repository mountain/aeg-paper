// 把只属于 h_RP 的词填进 h_PA，或者让它绕一圈 —— 编译期就被拦住。
trait RustPython { fn as_py(&self) -> String; }
trait PythonAda  { fn as_ada(&self) -> String; }
trait AdaRust    { fn as_rust(&self) -> String; }

struct Core;
struct Closure;
impl RustPython for Core { fn as_py(&self) -> String { "core".into() } }
impl PythonAda  for Core { fn as_ada(&self) -> String { "core".into() } }
impl AdaRust    for Core { fn as_rust(&self) -> String { "core".into() } }
impl RustPython for Closure { fn as_py(&self) -> String { "closure".into() } }

fn three_hole<A: RustPython, B: PythonAda, C: AdaRust>(_a: A, _b: B, _c: C) {}
fn ring<T: RustPython + PythonAda + AdaRust>(_x: T) {}

fn main() {
    three_hole(Closure, Closure, Core);   // 第二个孔要的是 Python–Ada 的词汇
    ring(Closure);                        // 绕一圈要三种词汇同时具备
}
