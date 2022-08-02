# -- coding: utf-8 --
import fibo


fibo.PrintFib(5)

ls = fibo.GetFib(5)
print(ls)


# 修改后的testfibo.py模块
import sys  # 导入系统模块
n = int(sys.argv[1])
# print(n)
fibo.PrintFib(n)