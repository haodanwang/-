#函数的参数
#定义函数的时候 我们把函数的名字和位置确定下来 函数的接口定义就完成了 对于函数的调用者来说
#只需知道如何传递正确的参数 以及函数将返回什么样的值就够了
#函数的内部的复杂的逻辑被封装起来了 调用者无需了解

#python的函数定义非常的简单 但灵活度却很大 除了正常的必选参数外 还可以使用默认的参数
#可变的参数和关键字参数 使得函数定义出来的接口 不但可以处理复杂的参数 还可以简化调用者的代码

#位置参数
#我们先写一个计算x平方的函数
# def power(x):
#     return x*x

#对于power(X)函数 参数x就是一个位置参数
#当我们调用power()函数的时候 必须有且只有的一个参数x:
# print(power(5))
# print(power(15))
#输出结果为:
#25
#225

#现在如果我们要计算x的三次方怎么办 可以再定义一个power3() 但是如果计算x的四次方 n次方呢？
#其实可以吧power(x) 改成power(x,n) 用来计算x的n次方
# def power(x,n):
#     s=1
#     for y in range(1,n+1):
#         s=s*x
#     return s
#
# print(power(2,10))

#修改后的power(x,n)函数有两个参数 x和n 这两个参数都是位置参数 调用参数的时候 传入的值按照位置的顺序
#依次赋值给参数x和n

#默认参数
#新的power(x，n)函数的定义没有问题 但是 旧的调用代码失败了 原因是我们增加了一个参数 导致旧的代码
#缺少一个参数而无法正常调用
#print(power(5))
#输出结果为:
# Traceback (most recent call last):
#   File "G:/git/-/day01/day09.py", line 38, in <module>
#     print(power(5))
# TypeError: power() missing 1 required positional argument: 'n'
#python的错误信息很明确 调用函数power()缺少了一个参数n
#这个时候 默认参数就派上用场了 由于我们经常计算x的平方 所以完全可以把第二个参数n的默认值设置为2
# def power(x,n=2):
#     s=1
#     for y in range(1,n+1):
#         s=s*x
#     return s
# print(power(5))
#输出结果为:25
#当我们调用power(5)的时候 就相当于调用power(5,2)
#而对于n>2的其他情况 就必须传入n 比如power(5,3)
#从上面的例子可以看出 默认参数开业简化函数的调用 设置默认参数的时候 有几点要注意
#一是必选参数在前 默认参数在后 否则python的解释器会报错
#二是如果设置默认参数
#当函数有多个参数 把变化大的参数放在前面 变化小的参数放在后面 变化小的就可以作为默认参数
#使用默认参数有什么好处 最大的好处就是降低调用函数的难度
#举个例子 我们写个一年级学生注册的函数 需要传入name和gender两个参数:
# def enroll(name, gender):
#     print('name:', name)
#     print('gender:', gender)
#这样 调用enroll()函数只需要传入两个参数
# print(enroll('Sarah', 'F'))
#如果要继续传入年龄 城市等信息怎么办？这样会使得调用函数的复杂度大大增加
#我们可以把年龄和城市设为默认参数
# def enroll(name,gender,age=6,city='Beijing'):
#     print('name:',name)
#     print('gender:',gender)
#     print('age:',age)
#     print('city:',city)
#这样大多数学生注册的时候不需要提供年龄和城市 只提供必需的两个参数
# print(enroll('Sarah','F'))
#只有与默认参数不符合的学生才需要提供额外的信息:
# print(enroll('Bob','M','7'))
# print(enroll('Adam','M',city='Tianjin'))
#可见 默认参数降低了函数调用的难度 而一旦需要更复杂的调用 又可以传递更多的参数来实现
#无论是简单调用函数复杂调用 函数值需要定义一个
#有多个默认参数的时候 调用的时候 既可以按照顺序提供默认参数比如enroll('Bob','M','7')
#意思是除了name gender这两个参数外 最后一个参数应用在age上 由于city的参数没有提供 仍然使用默认值
#也可以不按顺序提供部分默认参数 当不按顺序提供部分默认参数的时候 需要吧参数名写上 比如调用
#enroll('Adam','M',city='Tianjin') 意思是 city参数用传入进去的值 其他默认参数继续使用默认值
#默认参数很有用 但是使用不当 也会掉进坑里面 默认参数有个最大的坑 演示如下
#先定义一个函数 传入一个list 添加一个END再返回

# def add_end(L=[]):
#     L.append('END')
#     return L
#正常调用的时候 结果如下:
#print(add_end([1,2,3]))
#输出结果为:[1, 2, 3, 'END']
#print(add_end(['x','y','z']))
#输出结果为:['x', 'y', 'z', 'END']
#这两次的输出结果都正常
#再试试使用默认参数调用
#print(add_end())
#输出结果为:['END'] 输出的结果是正常的
#我们试试再次调用
#print(add_end())
#输出结果为:['END', 'END']
#再试一次
#print(add_end())
#输出结果为:['END', 'END', 'END']
#这一点就产生了疑惑 默认参数是[] 但是函数似乎都记住了上次添加的END之后的list
#原因解释如下:
#python函数在定义的时候 默认参数L的值就被计算出来了 即为[] 因为默认参数L是一个变量 它指向对象L
#每次调用该函数 如果改变了L的内容 则下次调用的时候 默认参数的内容就改了 不再是定义时候的[]了
#定义默认参数要牢记一点:默认参数必须指向不变对象
#要修改上面的例子 我们可以用None这个不变对象来实现
# def add_end(L=None):
#     if L is None:
#         L=[]
#         L.append('END')
#         return L

# print(add_end())
# print(add_end())
#连续调用两次的结果为:
# ['END']
# ['END']
#为什么要设计str，None这样的不变对象呢？因为对象一旦被创建 对象内部的数据就不能修改
#这样就减少了由于修改数据导致的错误 此外 由于对象不变 多任务环境下同时读取对象不需要加锁
#同时读一点问题没有 我们在编程的时候 如果可以设计一个不变对象 那就尽量设计出不变对象

#可变参数
#在python函数中 还可以定义可变参数 顾名思义 可变参数就是传入的参数个数是可变的 可以是1个 2个 到任意个数 还可以是是0个
#我们以数学题为例子 给定一组数字a,b,c....计算 a*a+b*b+c*c....
#要定义这个函数 我们必须确定输入的参数 由于参数个数不确定 我们首先想到的可以把a,b,c..当做一个list或者tuple传进来 这样函数的定义如下:
# def cale(numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum
# print(cale([1,2,3]))
# print(cale((1,2,3,5)))
#输出结果为:
# 14
# 39
#但是这样写 调用调用的时候 需要先组装一个list或者tuple
#如果利用可变参数

# def cale(*numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum
# print(cale(1,2,3))
# print(cale())
# #输出结果为:
# 14
# 0
#定义可变参数和定义一个list或tuple相比 仅仅在参数前面加了一个* 在函数内部 参数numbers接收到的
#是一个tuple 因此 函数的代码完全不变 但是 调用该函数时 可以传入任意个参数 包括0
#如果是已经有了一个list或者tuple 要调用一个可变参数怎么办
# num=[1,2,3]
# print(cale(num[0],num[1],num[2]))
#输出结果为:14

#这种写法当然是可行的 问题是太繁琐 所以python允许你在list或tuple前面加一个* 把list或者tuple的元素变成可变参数传进去
#print(cale(*num))
#*num表示把num这个list的所有元素作为可变参数传进去 这种写法相当有用 而且很常见

#关键字参数
#可变参数允许你传入0个或者任意个参数 这些可变参数在函数调用的时候自动组装为一个tuple
#而关键字参数允许你传入0个或者任意个含参数名的参数 这些关键字参数在函数内部自动组装为一个dict
# def person(name,age,**kw):
#     print('name:',name,'age:',age,'other:',kw)

#函数person除了必选参数name和age外 还接受关键字参数kw 在调用该函数时 可以只传入必选参数:
#print(person('Michale',30))
#输出结果为:name: Michale age: 30 other: {}
#也可以传入任意个数的关键字参数
#extra={'city':'Beijing','Job':'Engineer'}
#print(person('Jack',24,city=extra['city'],job=extra['Job']))
#输出结果为:name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
#当然上面的复杂的调用可以简化的写法:
#print(person('Jcak',24,**extra))
#输出结果为：name: Jcak age: 24 other: {'city': 'Beijing', 'Job': 'Engineer'}
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数到**kw参数
#kw将获得一个dcit 注意kw是获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

#命名关键字参数
#对于关键字参数 函数的调用者可以传入任意不受限制的关键字参数 至于到底传入了哪些 就需要在函数内部通过kw检查
def person(name,age,**kw):
     if 'city' in kw:
         pass
     if 'job' in kw:
         pass
     print('name:',name,'age:',age,'other:',kw)

#但是调用者扔可以传入不受限制的关键字参数
print(person('Jakc',24,city='Beijng',addr='Chaoyang',zipcode='123456'))
