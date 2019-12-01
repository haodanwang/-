#map/reduce
#python 内建map()和reduce()函数
#我们先看map() map()j函数接收两个参数 一个是函数 一个是Iteratable map将传入的函数溢出作用到序列的每个元素
#并将结果作为新的的Iterator返回
# 举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
#
#             f(x) = x * x
#
#                   │
#                   │
#   ┌───┬───┬───┬───┼─
#   │   │   │   │   │   │   │   │
#   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
#
# [ 1   2   3   4   5   6   7   8   9 ]
#
#   │   │   │   │   │   │   │   │
#   │   │   │   │   │   │   │   │
#   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
#
# [ 1   4   9  16  25  36  49  64  81 ]
#现在我们用python代码实现
def F(x):
    return x*x
# r=map(F,[1,2,3,4,5,6,7,8,9])
# print(list(r))
#输出结果为:[1, 4, 9, 16, 25, 36, 49, 64, 81]
#实验下同为Iteratable的string
# def f(x):
#     return x+x
# s=map(f,'String')
# print(list(s))
#输出结果为:['SS', 'tt', 'rr', 'ii', 'nn', 'gg']

#map()传入的第一个参数为F 即函数对象本身 由于结果r是一个Iterator Iterator是一个惰性序列 因此通过list()
#让它把整个序列都计算出来并返回一个list
#你可能想 不需要map()函数 写个循环 也可以计算出结果:
# L=[]
# for n in [1,2,3,4,5,6,7,8,9]:
#     L.append(F(n))
# print(L)
#输出结果为:
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
#的确可以 但是 从上面的循环代码 能一眼看明白把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？
#所以 map()作为高阶函数 事实上它把运算规则抽象了 因此 我们不但可以计算简单的f(x)=x*x 还可以计算任意复杂的函数
#比如 把这个list所有数字转换成字符串:
#print(list(map(str,[1,2,3,4,5,6,7,8,9])))
#输出结果为:['1', '2', '3', '4', '5', '6', '7', '8', '9']
#只需要一行代码

#再看看reduce的用法 reduce把一个函数作用在一个序列[x1,x2,x3,....]上 这个函数必须接收两个参数 reduce把结果继续和序列的下一个元素做累积计算
#其效果就是:
#reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2).x3),x4)
#比方说一个序列求和 就可以用reduce实现:
from functools import reduce
#
# def add(x,y):
#     return x+y
#
# print(reduce(add,[1,3,5,7,9]))
#输出结果为:25
#当然求和运算开业直接用python的内建函数sum(), 没必要动用reduce
#但是如果要把序列[1,3,5,7,9]变成整数13579 reduce就可以派上用场了
# def fn(x,y):
#     return  x*10+y
#
# print(reduce(fn,[1,3,5,7,9]))
#输出结果为:13579
#这个例子本身没有多大用处 但是 如果考虑到字符串str也是一个序列 对上面的例子稍加改动 配合map 我们就可以写出把str转换成int的函数
# def fn(x,y):
#     return x*10+y
#
# def char2num(s):
#     digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return digits[s]
#
# print(reduce(fn,map(char2num,'13579')))
#输出结果为:13579
#整理成一个str2int函数就是:
# DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# def str2int(s):
#     def fn(x,y):
#         return x*10+y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn,map(char2num,s))
#
# print(str2int('13579'))
# #输出结果为:13579

#还可以用lambda函数进一步简化成
DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char2num(s):
    return  DIGITS[s]

def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

# print(str2int('1357910'))
#输出结果为:1357910
#也就是说 假设python没有提供int()函数 你完全可以自己写一个把字符串转换成整数的函数  而且只需要几行代码
#lambda函数在后面介绍

#练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    if name==''or not isinstance(name,str):
        return
    newname=name.upper()[0]
    newname+=name.lower()[1:]
    return newname


# L1 = ['adam', 'LISA', 'barT']
# L2=list(map(normalize,L1))
# print(L2)
#输出结果为:
# ['Adam', 'Lisa', 'Bart']

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    if L==[]:
        return 0
    else:
        return  reduce(lambda x,y:x*y,L)
print(prod([1,3,5,7,9]))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456:
def str2float(s):
    pass