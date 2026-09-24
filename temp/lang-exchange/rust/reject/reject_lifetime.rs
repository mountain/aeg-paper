// 把对局部的引用交出去 —— 被编译器拒绝
fn leak() -> &'static Vec<u32> {
    let local = vec![1u32, 2, 3];
    &local          // E0515: 返回了引用局部变量的值
}
fn main() { println!("{}", leak().len()); }
