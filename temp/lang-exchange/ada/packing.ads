-- packing.ads —— 交换的界面：规格（spec）就是契约
--
-- 本机没有 GNAT/alire，这两份 Ada 文件未经编译验证，只作为界面结构的对照。
-- 可编译的形式见同目录 README 的说明。
--
-- 要点：Ada 把「什么值可以过去」写进类型与包规格；
--       客户代码只能看到规格部分，表示（record 布局、缓冲区）在 private 部分里。

package Packing is

   Max_Circles : constant := 1024;
   type Index is range 1 .. Max_Circles;

   -- 私有类型：外部拿不到分量，只能通过下面的子程序交换信息
   type Circle is private;

   function Make (X, Y, R : Long_Float) return Circle;
   function X_Of (C : Circle) return Long_Float;
   function Y_Of (C : Circle) return Long_Float;
   function Radius (C : Circle) return Long_Float;
   -- 半径不可能为负：用子类型承载不变量，赋值处会插入运行期检查
   subtype Positive_Radius is Long_Float range Long_Float'Succ (0.0) .. Long_Float'Last;

   -- 交换的载体也是私有类型，外部只能按下面声明的接口动它
   type Buffer is limited private;

   procedure Append (B : in out Buffer; C : Circle);
   -- 参数模式声明了信息流向：in 只读、in out 可读可写。
   -- 注意：Ada 检查模式，但不检查别名 —— 两个 in out 实参可以指向同一对象。
   function Length (B : Buffer) return Natural;

   type Circle_Array is array (Index range <>) of Circle;
   function Snapshot (B : Buffer) return Circle_Array;

private
   type Circle is record
      X, Y, R : Long_Float;
   end record;

   type Circle_Store is array (Index) of Circle;

   type Buffer is limited record
      Data : Circle_Store;
      Last : Natural := 0;
   end record;

end Packing;
