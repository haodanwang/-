
#迭代
#如果给定一个list或者tuple 我们可以通过for循环来遍历这个list或tuple 这种遍历我们称为迭代、
#在python中 迭代是通过for...in 来完成的 而很多语言比如C语言,迭代list是通过下标完成的 比如java代码
# for(i=0;i<list.length;i++){
#     n=list[i];
# }
#可以看出 python的for循环抽象程度要高于C的for循环 因为python的for循环不仅仅可以用在list或tuple上
#还可以作用在其他可迭代对象上
#list这种数据类型虽然有下标 但很多其他数据类型是没有下标的 但是只要是可以迭代对象 无论有无下标 都可以迭代
#比如dict就可以迭代:
# d={'a':1,'b':2,'c':3}
# for key in d:
#     print(key)
#输出结果为:
# a
# b
# c
#因为dict的存储不是按照list的方式顺序排序 所以 迭代出的结果顺序很可能不一样
#默认情况下 dict迭代是key 如果需要迭代value 可以用'for value in d.values()'
#如果需要同时迭代key和value 可以使用 for k,v in d.item()
# for value in d.values():
#     print(value)
#输出结果为：
# 1
#  2
#  3
# for k,v in d.items():
#     print(k,':',v)
#输出结果为:
# a : 1
# # b : 2
# # c : 3
#由于字符串是可迭代对象 因此 也可以作用于for循环:
# for ch in 'ABCD':
#     print(ch)
#输出结果为:
# A
# B
# C
# D
#所以 当我们使用for循环时 只要作用于一个可迭代对象 for循环就可以正常运行 而我们不太关心该对象究竟是lsit还是其他的数据类型
#那么 如何判断一个对象是可迭代对象呢  方法是通过collections模块的Iteratable类型判断:
# from collections import Iterable
# print(isinstance('ABC',Iterable))#str是否可以迭代
# print(isinstance([1,2,3],Iterable))#list 是否可以迭代
# print(isinstance(123,Iterable))#整数是否可以迭代
#输出结果为：
# True
# True
# False
#最后一个问题 如果要对list实现类似Java的下标循环怎么办 python内置的enumerate函数可以把一个list变成索引-元素对
#这样就可以在for循环同时迭代索引和元素本身
# for i,value in enumerate(['A','B','C','D']):
#     print(i,value)
#输出结果为:
# 0 A
# 1 B
# 2 C
# 3 D
# 上面的for循环里面 同时引用了两个变量 这个在python里面很常见 比如下面的代码:\
# for x,y in [(1,2),(2,3),(3,4)]:
#     print(x,y)
#输出结果为:
# 1 2
# 2 3
# 3 4

#练习
#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if(len(L)==0):
        return (None,None)
    min=L[0]
    max=L[0]
    for value in L:
        if value<min:
            min=value
        if value>max:
            max=value
    return min,max
print(findMinAndMax([]))
print(findMinAndMax([9,3,4,5,6,7]))
#输出结果为:
# (None, None)
# (3, 9)

