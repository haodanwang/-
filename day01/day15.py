#迭代器
#我们已经知道 可以直接作用于for循环的数据类型有以下几种:
#一是集合数据类型 如:list tuple dict set str等
#一类是 generator 包括生成器和带生成器的generator function
#这些可以直接作用于for循环的对象统称为可迭代对象:Iterable
#可以使用isinstance()判断一个对象是否是iterate对象
# from  collections import  Iterable
# print(isinstance([],Iterable))
# print(isinstance({},Iterable))
# print(isinstance('abc',Iterable))
# print(isinstance((x for x in range(10)),Iterable))
# print(isinstance(100,Iterable))
#输出结果为:
# G:/git/-/day01/day15.py:7: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
# True
#   from  collections import  Iterable
# True
# True
# False
#报错的提示是一个警告 是因为版本更新发出的警告。目前可以忽略，不影响后续使用。

#而生成器的作用不但可以作用于for循环 还可以被next()函数不断调用并返回下一个值 直到最后抛出stopIteration错误表示无法继续返回下一个值
#可以被next()函数调用并不断返回下一个值的对象称为迭代器
#可以用isInstance()判断对象是否是Iterator对象
from  collections import  Iterator


# print(isinstance((x for x in range(10)),Iterator))
# print(isinstance([],Iterator))
# print(isinstance({},Iterator))
# print(isinstance('abc',Iterator))
#输出结果为:
# True
# False
# False
# False
#生成器都是Iterator对象 但是list dict str 虽然都是Itertable 却不是Iterator
#把list dict str等Iteratable变成Iterator可以使用iter()函数
# print(isinstance(iter([]),Iterator))
# print(isinstance(iter('abc'),Iterator))
#输出结果为i:
# True
# True
#你可能会问 为什么list dict str等数据类型不是Iterator
#这是因为python的Iterator对象表示的是一个数据流 Iterator对象可以被next()函数调用并不断返回下一个数据
#直到没有数据时抛出StopIteratation错误 可以把这个数据流看成一个有序序列 但我们却不能提前知道序列的长度
#只能不断通过next()函数来按需计算下一个数据 所以Iterator的计算的惰性的 只有在需要返回下一个数据的时候它才会计算
#Iterator甚至可以表示一个无限大的数据流 例如全体自然数 而使用list是永远不可能存储全体自然数的


#小结
#凡是可作用于for循环的对象都是Iteratabel类型
#凡是可以作用于next()函数的对象都是Iterator类型 它们表示一个惰性计算的序列
#集合数据类型如list dict str等Iteratable但不是Iterator 不过可以通过iter()函数获得一个Iterator对象
#python的for循环本质上就是通过不断调用next()函数实现的 例如:
for x in [1,2,3,4,5]:
    pass

#实际上完全等价于:
#首先获取Iterator对象:
it=iter([1,2,3,4,5])
while True:
    try:
        #获得下一个值
        x=next(it)
        print(x)
    except StopIteration:
        #遇到StopIteration就退出循环
        break
#输出结果为:
# 1
# 2
# 3
# 4
# 5



