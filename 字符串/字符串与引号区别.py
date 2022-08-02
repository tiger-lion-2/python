# 字符串的创建可以使用单引号、双引号、三引号（3个连续的单引号或者双引号）

str1 = 'hello\
 world'
print(str1)
str2 = "hello \nworld"
print(str2)

# 在一对三引号括起来的字符串中，可以直接包含单引号和双引号，不需要使用转义符
str3 = """hello
world
ok
"""
print(str3)