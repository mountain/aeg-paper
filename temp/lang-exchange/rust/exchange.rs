// exchange.rs — 「什么组织了自由的信息交换」：Rust 侧
//
// 场景与前一阶段同一份数据：一组圆 (x, y, r)。
// 两个部件：producer 造数据，consumer 用数据。交换边界就是函数签名。
// 观察点：边界上究竟由什么决定
//   (1) 什么值可以过去          —— 类型 + 所有权（移动/复制/借用）
//   (2) 谁可以持有引用、能否改  —— 别名与可变性互斥
//   (3) 什么时候可以改          —— Send/Sync + 同步原语
//
// 编译运行：rustc -O exchange.rs -o /tmp/exchange && /tmp/exchange

use std::cell::RefCell;
use std::panic::{catch_unwind, AssertUnwindSafe};
use std::rc::Rc;
use std::sync::{mpsc, Arc, Mutex};
use std::thread;

#[derive(Debug, Clone, Copy, PartialEq)]
struct Circle {
    x: f64,
    y: f64,
    r: f64,
}

fn producer(n: usize) -> Vec<Circle> {
    (0..n)
        .map(|i| {
            let t = std::f64::consts::PI * i as f64 / (n.max(2) - 1) as f64;
            Circle { x: t.cos() * 0.5, y: t.sin() * 0.5, r: 0.5 }
        })
        .collect()
}

// 边界 A：按值接收 —— 交换就是移动，交出后原处不再有它
fn consume_by_value(mut v: Vec<Circle>) -> usize {
    v.push(Circle { x: 0.0, y: 0.0, r: 1.0 });
    v.len()
}

// 边界 B：按共享借用接收 —— 只读，且允许多个读者并存
fn consume_by_ref(v: &[Circle]) -> f64 {
    v.iter().map(|c| c.r).sum()
}

// 边界 C：按可变借用接收 —— 独占，同一时刻只能有一个写者
fn consume_by_mut(v: &mut Vec<Circle>) {
    v.iter_mut().for_each(|c| c.r *= 2.0);
}

fn main() {
    println!("== (1) 所有权：值能不能自由过去 ==");
    let data = producer(4);
    let n = consume_by_value(data);
    println!("  按值交出后，consumer 看到 {} 个圆；原变量已被移动，此处无法再读写它", n);
    let mut data = producer(4); // 重新造一份（不能用被移动过的那份）
    println!("  重新造一份后按借用读取：Σr = {}", consume_by_ref(&data));
    {
        let w = &mut data;
        consume_by_mut(w);
    } // 可变借用在作用域结束才归还
    println!("  可变借用归还后仍可读：Σr = {}", consume_by_ref(&data));

    println!("== (2) 内部可变性：把检查从编译期挪到运行期 ==");
    let shared = Rc::new(RefCell::new(producer(2)));
    let h1 = Rc::clone(&shared);
    let h2 = Rc::clone(&shared);
    h1.borrow_mut().push(Circle { x: 0.0, y: 0.0, r: 9.0 });
    println!("  两个句柄 h1/h2 指向同一份数据（强引用计数 {}）：长度 {}", Rc::strong_count(&shared), h2.borrow().len());
    let doubled = catch_unwind(AssertUnwindSafe(|| {
        let _first = shared.borrow_mut();
        let _second = shared.borrow_mut(); // 运行期才会炸：already mutably borrowed
    }));
    println!("  同时两次 borrow_mut -> 运行期 panic：{}", doubled.is_err());

    println!("== (3) 跨线程：Send/Sync 由编译器判，临界区由锁定义 ==");
    let pool = Arc::new(Mutex::new(Vec::<Circle>::new()));
    let mut handles = Vec::new();
    for t in 0..4 {
        let p = Arc::clone(&pool);
        handles.push(thread::spawn(move || {
            for i in 0..100 {
                p.lock().unwrap().push(Circle { x: t as f64, y: i as f64, r: 0.25 });
            }
        }));
    }
    for h in handles {
        h.join().unwrap();
    }
    println!("  4 线程 × 100 次加锁写入后长度 = {}", pool.lock().unwrap().len());

    println!("== (4) 消息：所有权随消息一起搬过去 ==");
    let (tx, rx) = mpsc::channel();
    let sender = thread::spawn(move || {
        tx.send(producer(3)).unwrap();
    });
    let got = rx.recv().unwrap();
    sender.join().unwrap();
    println!("  收到一条消息，其中圆的个数 = {}", got.len());
}
