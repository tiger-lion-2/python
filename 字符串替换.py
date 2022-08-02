# 使用字符串的replace方法可以把字符串中指定子串替换成其他内容。语法格式：
# str.replace(old,new[,max])

str = 'cat dog cat dog cat dog'
str1 = str.replace('cat', 'mouse')
str2 = str.replace('cat', 'mouse', 2)
print("str1:", str1)
print("str2:", str2)