// 一个“孔”= 一个调用位置 = 一个带词汇界的泛型槽。
// 三条边各有一个孔，每个孔的界就是那一对语言的公共词汇。
// 编译运行：rustc -O holes_ok.rs -o /tmp/holes_ok && /tmp/holes_ok

trait RustPython { fn as_py(&self) -> String; }   // h_RP 的词汇：在 Python 侧怎么拼
trait PythonAda  { fn as_ada(&self) -> String; }  // h_PA 的词汇：在 Ada 侧怎么拼
trait AdaRust    { fn as_rust(&self) -> String; } // h_AR 的词汇：回到 Rust 侧怎么拼

struct Core { v: i64 }        // 三重交集：三家都懂
struct Closure { n: i64 }     // 只在 h_RP 里
struct Exception { c: i64 }   // 只在 h_PA 里
struct Generic { p: i64 }     // 只在 h_AR 里

impl RustPython for Core { fn as_py(&self) -> String { format!("core:{}", self.v) } }
impl PythonAda  for Core { fn as_ada(&self) -> String { format!("core:{}", self.v) } }
impl AdaRust    for Core { fn as_rust(&self) -> String { format!("core:{}", self.v) } }
impl RustPython for Closure { fn as_py(&self) -> String { format!("closure:{}", self.n) } }
impl PythonAda  for Exception { fn as_ada(&self) -> String { format!("exception:{}", self.c) } }
impl AdaRust    for Generic { fn as_rust(&self) -> String { format!("generic:{}", self.p) } }

// 三孔表达式：每个孔由它那条边的词汇填充，界在编译期检查
fn three_hole<A: RustPython, B: PythonAda, C: AdaRust>(a: A, b: B, c: C) -> Vec<String> {
    vec![a.as_py(), b.as_ada(), c.as_rust()]
}

// 绕一圈 R→P→A→R：同一个词必须同时属于三条边的词汇
fn ring<T: RustPython + PythonAda + AdaRust>(x: T) -> Vec<String> {
    vec![x.as_py(), x.as_ada(), x.as_rust()]
}

fn main() {
    // 1) 全部用核心词汇填：三个孔都能过
    let r = three_hole(Core { v: 1 }, Core { v: 2 }, Core { v: 3 });
    println!("all-core filling: {:?}", r);
    // 2) 每个孔各用自己那条边的词：这是“更自由”的填法
    let r = three_hole(Closure { n: 7 }, Exception { c: 8 }, Generic { p: 9 });
    println!("edge-wise filling: {:?}", r);
    // 3) 混填
    let r = three_hole(Closure { n: 7 }, Core { v: 8 }, Generic { p: 9 });
    println!("mixed filling: {:?}", r);
    // 4) 绕一圈：只有核心词汇走得完
    println!("ring(core): {:?}", ring(Core { v: 5 }));
    // ring(Closure { n: 1 });  // 换成这一行就编译不过：见 holes_reject.rs
}
