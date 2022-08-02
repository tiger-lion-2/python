# -- coding: utf-8 --
# 当一个模块中定义了列表__all__,则from模块名import *语句只能
# 导入__all__列表中存在的表示符

# __all__ = ['PrintFib']
# 如果采用上述方式导入时，在testfibo模块中则出现错误

def PrintFib(n):
    a, b = 1, 1   # 将a,b 赋值为1
    for i in range(1, n+1):     # i的取值依次为1,2,3，，，，n
        print(a, end=' ')    # 输出斐波那契数列的第i项
        a, b = b, a+b   # 更新斐波那契额数列第i+1项的值，并计算第i+2项的值
    print("\n")


def GetFib(n):
    fib = []
    a, b = 1, 1
    for i in range(1, n+1):
        fib.append(a)
        a, b = b, a+b
    return fib


# PrintFib(10)
# ls = GetFib(10)
# print(ls)


# 修改后的fibo.py模块
# 全局变量__name__
if __name__ == "__main__":  # 只有单独执行fibo.py脚本文件时该条件才成立
    PrintFib(10)
    ls = GetFib(10)
    print(ls)