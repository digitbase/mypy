from utile import pr

str1 = 'ni \' \n \n\r  hao'
str2 = "hi \"hao"
str3 = '''
hi 
hao
'''

a='hello world'

pr(a)
pr(a*2)

b =  1
pr(b)
pr(b*2)

print(r'\n') #原样输出
print(f'你好{a}') #格式化输出




# 转换符	描述	示例
# %d	十进制整数	"%d" % 123
# %i	十进制整数（与 %d 相同）	"%i" % 123
# %u	无符号十进制整数	"%u" % 123
# %o	八进制整数	"%o" % 123
# %x	十六进制整数（小写字母）	"%x" % 123
# %X	十六进制整数（大写字母）	"%X" % 123
# %f	浮点数（默认显示 6 位小数）	"%f" % 123.456
# %F	浮点数（与 %f 相同）	"%F" % 123.456
# %e	科学计数法（小写 e）	"%e" % 123.456
# %E	科学计数法（大写 E）	"%E" % 123.456
# %g	自动选择 %f 或 %e 格式输出	"%g" % 123.456
# %G	自动选择 %f 或 %E 格式输出	"%G" % 123.456
# %s	字符串	"%s" % "hello"
# %r	使用 repr() 函数的字符串表示	"%r" % "hello"
# %%	输出百分号 %	"%%" % 100


# 使用示例：01
name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age))  # 输出: Name: Alice, Age: 30

#02
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))  # 输出: Name: Alice, Age: 30

#03
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")  # 输出: Name: Alice, Age: 30

#4
pi = 3.141592653589793
print(f"Pi to 2 decimal places: {pi:.2f}")  # 输出: Pi to 2 decimal places: 3.14
print(f"Pi to 2 decimal places: {pi:.0f}")  # 输出: Pi to 2 decimal places: 3


print('Pi to 2 decimal places: %d' % pi)  # 输出: Pi to 2 decimal places: 3


print(oct(10))
print("%o " % 9) #八进制
print("%X " % 12) #十六进制

print(123, end='') # 取消换行


#   // 取整除
#   % 取余 
pr(9//2)
pr(9%2)


#数据类型： int float str bool compile
#结构类型：  nlist tuple set dict

a = 123.123
pr(type(a))
pr(type(str(a)))
pr(type(float(a)))
pr(a)


# [起始： 结束： 步长]
name = 'abcdefghijklmnopqrstuvwxyzABCDEFGH'
pr(name[6:20:2])


# find 字符串序列.find(str, beg=0, end=len(string)
pr(name.find('a'))

#index count replace split

pr(name.index('a'))
pr(name.count('a'))
pr(name.replace('a', 'b', 1))
