# 字符串提供了4种用于检索的方法，分别是find,index,rfind,rindex,语法格式如下：
# str.find(sub[,start[,end]])
# str.index(sub[,start[,end]])
# str.rfind(sub[,start[,end]])
# str.rindex(sub[,start[,end]])
# 上述语法表示从字符串str中检索字符串sub出现的位置，start和end参数指定了检索范围，即在str[start:end]
# 中检索，默认情况下是str[:]范围中检索
# find方法是在检索范围中按照从左到右的顺序检索，找到字符串sub第一次出现的位置，而rfind是按照从右到左的顺序
# index和find方法相同。rindex和rfind方法相同，只是rfind和find在检索不到字符串时返回-1，index和rindex
# 检索不到会引发ValueError异常


str = 'cat dog cat dog cat dog'
print("str中第一次出现cat的位置：", str.find('cat'))
print("str中最后一次出现cat的位置：", str.rfind('cat'))
print("str中第一次出现mouse的位置：", str.find('mouse'))