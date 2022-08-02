# split方法
# 使用字符串中的split方法可以按照指定的分隔符对字符串进行切割，返回由切割结果组成的列表
# 语法格式：
# str.split(sep=None,maxspilt=-1),后者默认-1表示不对最大切割次数做限制


str1 = 'It is a book'
str2 = 'Python##C++##Java##PHP'

ls1 = str1.split()
ls2 = str2.split('##')
ls3 = str2.split('##', 2)  # 对str2进行2次切割

print('ls1:', ls1)
print('ls2:', ls2)
print('ls3:', ls3)


# splitlines方法
# 该方法固定以行结束符('\n','\r','\r\n')作为分隔符对字符串进行切割，返回由切割结果组成的列表
# 语法格式
# str.splitlines([keepends]),keepends表示切割结果中是否保留最后的行结束符，默认为False

str3 = "你好！\n欢迎学习Python语言程序设计！\r\n祝你学习愉快！\r"
ls4 = str3.splitlines()
ls5 = str3.splitlines(True)
print("ls4:", ls4)
print("ls5:", ls5)


str4 = "a**b*c*d"
ls6 = str4.split('*', 2)
print("ls6:", ls6)
ls7 = str4.split('**', 2)
print("ls7:", ls7)