-- exchange.adb —— 交换的时序：任务与保护对象
--
-- 未编译验证（本机无 GNAT）。这里只展示 Ada 用什么组织“谁能改、什么时候能改”。
--
-- 对照 Rust/Python：
--   * 保护对象 = 互斥 + 条件（屏障），由运行期强制，编译期由 pragma 定优先级上限；
--   * 任务会合（accept）= 一次同步的信息交接，双方在同一个点上对齐；
--   * 约束子类型与可达性层 = 运行期兜底检查；
--   * 流的属性 = 跨进程/跨设备的表示契约。

with Ada.Text_IO;              use Ada.Text_IO;
with Packing;                  use Packing;

procedure Exchange is

   -- 受保护类型：所有对 Data 的访问由运行期串行化，屏障决定“什么时候能取”
   protected type Guarded_Buffer is
      pragma Priority_Ceiling (System.Default_Priority + 1);  -- 优先级天花板，防反转
      procedure Put (C : Circle);
      entry Take (C : out Circle);          -- 屏障不满足时调用者排队
      function Count return Natural;
   private
      Store : Buffer;
      Full  : Boolean := False;
      One   : Circle;
   end Guarded_Buffer;

   protected body Guarded_Buffer is
      procedure Put (C : Circle) is
      begin
         One  := C;
         Full := True;
      end Put;

      entry Take (C : out Circle) when Full is   -- 屏障：只有 Full 为真才放行
      begin
         C    := One;
         Full := False;
      end Take;

      function Count return Natural is (if Full then 1 else 0);
   end Guarded_Buffer;

   Shared : Guarded_Buffer;

   -- 生产者任务：把圆交给受保护对象
   task type Producer (Tag : Integer);

   task body Producer is
      C : Circle;
   begin
      for I in 1 .. 3 loop
         C := Make (Long_Float (Tag), Long_Float (I), 0.25);
         Shared.Put (C);                       -- 一次同步交换
      end loop;
   end Producer;

   -- 消费者任务：按会合点取走
   task Consumer;
   task body Consumer is
      C : Circle;
      Got : Natural := 0;
   begin
      for I in 1 .. 6 loop
         Shared.Take (C);                      -- 屏障不满足则阻塞在这里
         Got := Got + 1;
      end loop;
      Put_Line ("consumer got" & Natural'Image (Got));
   end Consumer;

   A : Producer (1);
   B : Producer (2);

begin
   -- 两支生产者任务在上一行被激活；显式等待它们结束，交换边界到此闭合
   null;
end Exchange;
