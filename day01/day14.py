#生成器
#通过列表生成式 我们可以直接创建一个列表 但是 受内存限制 列表容量肯定是有限的 而且创建一个包含100万个元素的的列表
#不仅占用很大的存储空间 如果我们仅仅需要访问前几个元素 那么后面绝大多数元素的占用空间就白白浪费了
#如果列表元素可以按照某种算法推算出来 那我们是否可以在循环的过程中不断推算后续的元素呢 这样不必创建完整
#的list 从而节省大量的空间 在python中 这种一边循环一边计算的机制 我们称为生成器:generator
#要创建一个generator 有很多种方法 第一种方法是 只需要一个列表生成式[] 改成() 就创建了一个generator:
# L=[x*x for  x in range(10)]
# print(L)
# g=(x*x for x in range(10))
# print(g)
#输出结果为：
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# <generator object <genexpr> at 0x000002AA04914C78>
#创建L和g的区别仅在于最外层的[]和（） L是一个list 而g是一个生成器generator
#我们可以直接打印list的每一个元素 但我们怎么去打印generator的元素呢?
#如果要一个个打印出来 可以通过next()函数获取generator的下一个返回值
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#输出结果为:
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# Traceback (most recent call last):
#   File "G:/git/-/day01/day14.py", line 27, in <module>
#     print(next(g))
# StopIteration
#我们讲过 generator保存是算法 每次调用next(g) 就计算下一个元素的值 直到计算到最后一个元素 抛出
#stopIteration的错误
#当然 上面不断的调用next(g)实在是太变态了 正确的方法是使用for循环 因为 generator也是可迭代对象
# g=(x*x for x in range(10))
# for n in g:
#     print(n)
#输出结果为：
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
#所以我们创建一个generator之后 基本上永远不会调用next() 而是通过for循环去代替它 并且不需要管线stopIteration的错误
#generator非常强大 如果推算的算法比较复杂 用类似于for循环无法实现的时候 还可以用函数来实现
#比如 著名的斐波拉契数列 除了第一个和第二个数外 任意一个数都可以由前两个数相加得到:
#1,1,2,3,5,8,13,21,34......
#斐波拉契数列用列表生成式写不出来 但是 用函数把它打印出来却很容易
# def flib(max):
#     n,a,b=0,0,1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         n=n+1
#     return 'done'
# print(flib(6))
#输出结果为：
# 1
# 1
# 2
# 3
# 5
# 8
#仔细查看 可以看出 flib函数实际上是定义了斐波拉契的推算规则 可以从第一个元素开始 推算出后续任意元素
#这种逻辑非常类似于generator
#也就是说 上面的函数 和generator仅一步之遥 要把flib函数变成 generator 只需要把print(b)改成yield b 就行了
def flib(max):
    n,a,b=0,0,1
    while n<max:
        yield  b
        a,b=b,a+b
        n=n+1
    return 'done'
#这就是定义generator的另外一种方法 如果一个函数的定义 包含yield关键字 那么这个函数就不再是一个普通函数 而是一个generator:
# f=flib(6)
# print(f)
#输出结果为:<generator object flib at 0x000002527E154C78>
#这里最难理解的就是generator和函数的执行流程不一样 函数是顺序执行 遇到return 语句或者最后一行的语句就返回
#而变成generator的函数 在每次调用next()的时候执行 遇到yield语句返回 再次执行时从上次返回的yield语句处继续执行
# def odd():
#     print('step 1')
#     yield  1
#     print('step 2')
#     yield 3
#     print('step 3')
#     yield 5
#调用该generator时 首先要生成一个generator对象 然后用next()函数不断获取下一个返回值
# o=odd()
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))
#输出结果为:
# step 1
# 1
# step 2
# 3
# step 3
# 5
#   File "G:/git/-/day01/day14.py", line 108, in <module>
#     print(next(o))
# StopIteration
#可以看到 odd不是普通函数 而是generator 在执行过程中 遇到yield就中断 下次又继续执行 执行三次yield后 已经没有yield可以执行了
#所以第四次调用next(o)就报错
#回到flib的例子 我们在循环过程中不断地调用yield 就会不断中断 当然要给循环设置一个条件来退出循环 不然就会产生一个无限数列出来
#同样的 把函数改成generator后 我们基本上从来不会用next()来获取下一个 而是直接使用for循环来迭代
# for n in flib(6):
#     print(n)
#输出结果为:
# 1
# 1
# 2
# 3
# 5
# 8
#但是用for循环调用generator时 发现拿不到generator的return语句的返回值 如果想要拿到返回值 必须捕获stopIteration错误
#返回值包含在stopIteration的value中
# g=flib(6)
# while True:
#     try:
#         x=next(g)
#         print('g:',x)
#     except StopIteration as  e:
#         print('Generator return value:',e.value)
#         break
#输出结果为:
# g: 1
# g: 1
# g: 2
# g: 3
# g: 5
# g: 8
# Generator return value: done
#关于如果捕捉错误 后面的错误的处理还会详细的讲解

#练习
# 杨辉三角定义如下：
#
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list:
def triangles():
    N=[1]
    while True:
        yield N
        N=N+[0]
        N=[N[i-1]+N[i] for i in  range(len(N))]
g=triangles()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))



