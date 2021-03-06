# 输入一个字符串
#   1. 判断您输入的字符串有几个空格
#   2. 将原字符串的左右空白字符去掉，打印出有效字符的长度
#   3. 判断您输入是否是数字

s = input("请输入一个字符串: ")

# 1. 判断您输入的字符串有几个空格
print("您输入的字符串有", s.count(' '), '个空格')

# 2. 将原字符串的左右空白字符去掉，打印出有效字符的长度
s2 = s.strip()  # 去掉空白字符
print("有效字符的个数是: ", len(s2))

# 3. 判断您输入是否是数字
if s2.isdigit():
    print("您输入的是数字")
else:
    print("您输入的不是数字")
