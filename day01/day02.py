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







