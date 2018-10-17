#本节主要练习字符编码
#具体详细的编码历史介绍请查看
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143166410
#6267f12e9bef7ee14cf6a8776a479bdec9b9000
#python的字符串
# print('包含中文的str')
#对于单个字符的编码 python提供了ord()函数获取字符的整数表示，chr()函数吧编码转换为对应的字符
# print(ord('A'))
# print(ord('中'))
# print(chr(66))
# print(chr(25991))
# 输出结果为:
# 65
# 20013
# B
# 文
#如果知道字符的整数编码 还可以采用十六进制这么写str
# print('\u4e2d\u6587')
# 输出结果为:中文
#这两种写法完全是等价的
#由于python的字符串类型是str,在内存中以Unicode表示，一个字符对应若干个字节。如果
#要在网络上传输，或者保存到磁盘上,就需要把str变成以字节为单位的bytes
#python 对bytes类型的数据用带b前缀的单引号或者双引号表示：
# x=b'ABC'
# 虽然'ABC'和b'ABC'显示的内容一样,但是bytes的每个字符都只占用一个字节
# # 以Unicode表示的str通过encode()方法可以编码为指定的bytes,例如:
# print('ABC'.encode('ascii'))
# print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))
# 输出结果为:
# b'ABC'
# b'\xe4\xb8\xad\xe6\x96\x87'
# Traceback (most recent call last):
#   File "G:/git/-/day01/day02.py", line 29, in <module>
#     print('中文'.encode('ascii'))
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
#纯英文的str可以用ASCII编码为bytes,内容是一样的，含有中文的str可以用UTF-8编码为bytes,但是含有中文的
#str无法用ASCII编码,因为中文的编码范围超过了ASCII的编码范围,python会报错。
#反过来，如果我们从网络或者磁盘里面读取了字节流，那就是读到的数据就是bytes.要把bytes变为str,就需要用到decode方法
# print(b'ABC'.decode('ascii'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# #输出结果为：
# ABC
# 中文
# 如果bytes中包含无法解析的字节,decode()方法报错:
# print( b'\xe4\xb8\xad\xff'.decode('utf-8'))
# Traceback (most recent call last):
#   File "G:/git/-/day01/day02.py", line 46, in <module>
#     print( b'\xe4\xb8\xad\xff'.decode('utf-8'))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
#如果bytes中只有一小部分无效的字节,可以传入errors='ingore'忽略错误的字节:
# print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))
#要计算str包含多少个字符,可以用len()函数
# print(len('ABC'))
# print(len('中文'))
# 输出结果为:
# 3
# 2
#len()函数计算的str的字符数，如果换成bytes,len()函数就计算字节数:
# print(len(b'ABC'))
# print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
# print(len('中文'.encode('UTF-8')))
# 输出结果为:
# 3
# 6
# 6
#可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
#在操作字符串的时候,我们经常遇到str和bytes的互相转换。为了避免乱码问题，应该始终坚持使用UTF-8对
#str和bytes进行转换
# 由于python的源码也是一个文本文件,所以,当你的源代码包含中文的时候,在保存源代码的时候,就需要在指定保存为
# UTF-8编码,当python解释器读取源代码的时候,为了让他按UTF-8编码读取,通常在文件开头写上这两行
# #！/usr/bin/env python3
# #-*-coding:utf-8-*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

#格式化
# 输出格式化字符串
# python采用的格式化方法和c语言是一致的,用%实现:
# print('Hello,%s' %'world')
# print('Hi,%s,you have $%d' %('Michael',10000))
# 输出结果为：
# Hello,world
# Hi,Michael,you have $10000

#常见的占位符有：%d 整数 %f 浮点数 %s 字符串 %x 十六进制数
#其中,格式化整数和浮点数还可以指定是否补0和整数与小数的位数
#print('%2d-%0.2d' %(3,1))
# print('%.2f' % 3.1414926)
# 输出结果为：
# 3-01
# 3.14
#如果不确定应该用什么,%s 永远起作用，它会把任何数据类型转换为字符串
# print('Age: %s Gender : %s ' %(25,True))
# 输出结果为：
# Age: 25 Gender : True
#如果字符串里面的%是一个普通字符，这个时候就需要转义，用%%来表示一个%
# print('growth rate :%d %%'% 7)
# 输出结果为：
# growth rate :7 %
#另外一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数
#依次替换字符串内的占位符{0},{1},{2}....,不过这种方法比%要麻烦
# print('Hello,{0},成绩提升了{1:.1f}%'.format('小米',17.125))
# 输出结果为:
# Hello,小米,成绩提升了17.1%
# s1=72
# s2=85
# r=(s2-s1)/s1*100
# print('%s成绩提升了 %.1f %%' % ('小明',r))
#当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8。Python当然也支持其他编码方式，比如把Unicode编码成GB2312：
# print('中文'.encode('gb2312'))
# 输出结果为:
# b'\xd6\xd0\xce\xc4'






