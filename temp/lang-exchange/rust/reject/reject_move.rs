// 交换之后再用原处 —— 被编译器拒绝
fn consume(v: Vec<u32>) -> usize { v.len() }
fn main() {
    let data = vec![1u32, 2, 3];
    let n = consume(data);
    println!("{}", data.len() + n); // data 已被移动
}
