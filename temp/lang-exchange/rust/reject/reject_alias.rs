// 同一个值同时被两个可变借用 —— 被编译器拒绝
fn main() {
    let mut data = vec![1u32, 2, 3];
    let a = &mut data;
    let b = &mut data;      // E0499
    a.push(4);
    b.push(5);
}
