// 把非 Send 的共享句柄送给另一个线程 —— 被编译器拒绝
use std::cell::RefCell;
use std::rc::Rc;
use std::thread;
fn main() {
    let shared = Rc::new(RefCell::new(vec![1u32]));
    let handle = Rc::clone(&shared);
    thread::spawn(move || { handle.borrow_mut().push(2); }); // E0277: Rc 不是 Send
    thread::sleep(std::time::Duration::from_millis(10));
    println!("{}", shared.borrow().len());
}
