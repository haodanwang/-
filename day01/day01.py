#打印helloworld
#print('Hello,World')

#输出100+200结果
#print('100+200=',100+200)

#使用input输入控件
#name=input("请输入你的姓名:")
#print(name)

#计算并输出1024*768结果
#print('1024*768=',1024*768)

#缩进有利有弊。好处是强迫你写出格式化的代码，
# 但没有规定缩进是几个空格还是Tab。按照约定俗成的管理，应该始终坚持使用4个空格的缩进。
#if-else 语句练习
# a=100
# if a>=0:
#     print(a)
# else:
#     print(-a)

#数据类型和变量

#print('I\'m ok.') #转义字符\ 输出结果为I'm ok.比如\n表示换行，\t表示制表符
#print('I\'m learning \nPython')#输出结果为
#I'm learning
#Python

#如果字符串里面有很多字符都需要转义，就需要加很多\
# 为了简化，Python还允许用r''表示''内部的字符串默认不转义
#print(r'I\'m learning\n python')
#输出结果为I\'m learning\n python

#如果字符串内部有很多换行，用\n写在一行里不好阅读
# 为了简化，Python允许用'''...'''的格式表示多行内容
# print('''line1
# line2
# line3''')
#输出结果为
# line1
# line2
# line3

#布尔值

#布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True
# 要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写）
# 也可以通过布尔运算计算出来
# print(True)
# print(False)
# print(3>2)
# print(3>5)
# #结果为:
# True
# False
# True
# False

#布尔值可以用and、or和not运算。

#and运算是与运算，只有所有都为True，and运算结果才是True
# print(True and True)
# print(True and False)
# print(False and False)
#print(5>3 and 3>1)
#输出结果为:
# True
# False
# False
#True

#or运算是或运算，只要其中有一个为True，or运算结果就是True
# print(True or True)
# print(True or False)
# print(False or False)
# print(5>3 or 1>3)
# 输出结果为:
# True
# True
# False
# True

#not运算是非运算，它是一个单目运算符，把True变成False，False变成True
# print(not True)
# print(not False)
# print(not 1>2)
# 输出结果为:
# False
# True
# True

#布尔值经常用在条件判断里面 比如：
# age=12
# if age>=18:
#     print('adult')
# else:
#     print('teenager')
#输出结果为：
#teenager

#空值

#空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，
#而None是一个特殊的空值。

#变量

#变量的概念基本上和初中代数的方程变量是一致的，
# 只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
#变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合
# 且不能用数字开头，比如：
#a=1
#此时变量a为一个整数
#print(a)
#a='abc'
#此时a成为一个字符串
#print(a)

#这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
# 静态语言在定义变量时必须指定变量类型如果赋值的时候类型不匹配，就会报错
# a='ABC'
# b=a
# print(a==b)
# print(str(id(a))+'\n'+str(id(b)))
# a='XYZ'
# print(a==b)
# print(str(id(a))+'\n'+str(id(b)))
#输出结果为:
# True
# 1762990981280
# 1762990981280
# False
# 1762991752056
# 1762990981280

#=为赋值符号 当a='ABC' 内存中会创建一个'ABC'的字符串 并让a指向这个字符串 当a=b时候 内存中不会再创建
#一个'ABC'字符串 而是让b也指向之前创建的字符串 所以此时a==b为True 此时查看ID值也是一样的
#当a='XYZ'时候 同样内存中会创建一个'XYZ'的字符串 然后让a指向这个字符串 此时判断a==b为False
#查看ID值 发现a的ID值已经改变

#常量

#所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。
# 在Python中，通常用全部大写的变量名表示常量：
#但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法
# 如果你一定要改变变量PI的值，也没人能拦住你。

#除法

# /除法计算的结果是浮点数 即使两个整数恰好整除也是浮点数
# print(9/3)
# // 称为地板除 两个整数的除法永远是整数 即使除不尽
# print(10//3)
# % 称为求余 等到两个整数相除的余数部分
# print(10%3)
# 以上三个结果为 3.0 / 3 / 1

# 练习题

# n=123
# f=456.789
# s1='Hello,World'
# s2='Hello,\'Adam\''
# s3=r'Hello,"Bart"'
# s4=r'''Hello,Lisa!'''
# print(n)
# print(f)
# print(s1)
# print(s2)
# print(s3)
# print(s4)
#输出结果为
# 123
# 456.789
# Hello,World
# Hello,'Adam'
# Hello,"Bart"
# Hello,Lisa!
# 小结
# Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。
# 对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向。
# 注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）



