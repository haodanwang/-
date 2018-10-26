#函数

#调用函数
#python内置了许多的函数 我们可以直接的调用
#要调用一个函数 需要知道函数的名称和参数 比如求绝对值的函数abs() 只有一个参数
#我们可以从python的官方网站查看文档 也可以在交互式命令行通过help(abs)查看abs函数的帮助信息
#调用abs()函数
# print(abs(100))
# print(abs(-20))
# print(abs(12.34))
# #输出结果为:
# 100
# 20
# 12.34
#调用函数的时候 如果传入的参数数量不对 会报typeError的错误 并且python会明确的告诉你
#abs()有且只有一个参数 但给出了两个
#print(abs(1,2))
#输出结果为:
# Traceback (most recent call last):
#   File "G:/git/-/day01/day07.py", line 17, in <module>
#     print(abs(1,2))
# TypeError: abs() takes exactly one argument (2 given)
#如果传入的参数数量是对的 但是参数类型是不能被函数所接受的 也会报TypeError的错误
#并且给出错误信息:str是错误的参数类型
# print(abs('a'))
# 输出结果为:
# Traceback (most recent call last):
#   File "G:/git/-/day01/day07.py", line 25, in <module>
#     print(abs('a'))
# TypeError: bad operand type for abs(): 'str'
#而max函数max()可接受任意多个函数 并且返回最大的那个
# print(max(1,2,3,4))
# print(max(1,2,3,-5))
# 输出结果为:
# 4
# 3

#数据类型转换
#python内置的常用函数还包括数据类型转换函数 比如int()函数可以把其他数据类型转换为整数
# print(int('123'))
# print(int(12.34))
# print(float('12.34'))
# print(str(1.23))
# print(str(100))
# print(bool(1))
# print(bool(''))
# 输出结果为:
# 123
# 12
# 12.34
# 1.23
# 100
# True
# False
#函数名其实就是一个指向函数对象的引用 完全可一把函数名赋给一个变量 相当于给这个函数取了一个"别名"
# a=abs #变量a()指向abs函数
# print(a(-1)) #所以也可以通过a调用abs函数
#输出结果为:1

#练习
#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
# n1=255
# n2=1000
# print(hex(n1),hex(n2))
# 输出结果为:0xff 0x3e8
#注意 hex()返回的就是字符串类型 所以不需要写成str(hex())