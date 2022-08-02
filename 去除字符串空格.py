# 语法格式：
# str.strip()  ,去除str中头部和尾部的空格
# str.rstrip()  ,去除尾部空格
# str.lstrip()  ,去除头部空格

# 如果去除所有的空格，则可以使用replace方法
# str.replace(' ','')  ,去除所有空格


str = ' I like Python! '
str1 = str.strip()  # 去除头部和尾部空格
str2 = str.rstrip()  # 去除尾部空格
str3 = str.lstrip()  # 去除头部空格
str4 = str.replace(' ', '')    # 去除所有空格

print("原字符串:#%s#"%str)
print("去除头部和尾部空格:#%s#"%str1)
print("去除尾部空格:#%s#"%str2)
print("去除头部空格:#%s#"%str3)
print("去除所有空格:#%s#"%str4)