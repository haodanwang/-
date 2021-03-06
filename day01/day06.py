#使用 dict和set
# python内置了字典 dict全称dictionary 在其他语言中也称为map 使用键-值(key-value)存储
# 具有极快的查找速度
#举个例子，要根据同学的名字查找对应的成绩 如果用list实现 需要两个list：
# names=['Michale','Bob','Tracy']
# score=[95,75,85]
#给定一个名字 要查找对应的成绩 就先要在names中找到对应的位置 再从score取出对应的成绩
#list越长 耗时越长
#如果用dict实现 只需要一个名字-成绩的对照表 直接根据名字查找成绩 无论这个表有多大
#查找速度都不会变慢 用python写一个dict如下:
d={'Michale':95,'Bob':75,'Tracy':85}
# print(d['Michale'])
#输出结果为：95
#这种key-value 存储方式 在放进去的时候 必须根据key算出value的存放位置
#这样 在取的时候才能根据key值直接拿到value
#把数据放进dict的方法 除了初始化指定外 还可以通过key放入
# d['Michale']=67
# print(d['Michale'])
#输出结果为:67
#由于一个key只能放对应的一个value 所以 多次对一个key放入value 后面的值会把前面的冲掉
# d['Tracy']=99
# print(d['Tracy'])
# d['Tracy']=88
# print(d['Tracy'])
#输出结果为:
# 99
#88
#如果key不存在 dict就会报错
#print(d['ABA'])
#输出结果为:
# Traceback (most recent call last):
#   File "G:/git/-/day01/day06.py", line 29, in <module>
#     print(d['ABA'])
# KeyError: 'ABA'
#要避免key不存在的问题 有两种方法 一种是通过in判断key是否存在:
# print('ABA' in d)
# print('Tracy' in d)
#输出结果为:
# False
# True
#二是通过dict提供的get()方法 如果key 不存在 可以返回None 或者自己返回自己指定的值
# print(d.get('ABA'))
# print(d.get('ABA',-1))
#输出结果为:
# None
# -1
#注意:在python的交互环境 返回值为None的时候是不显示结果的
#要删除一个key 用pop(key)方法 对应的value也会从dict中删除
# d.pop('Bob')
# print(d)
# #输出结果为:
# {'Michale': 95, 'Tracy': 85}
#请务必注意 dict内部的存放顺序和key放入的顺序是没有关系的

#list和dict比较 dict有以下的几个特点
# 1.查找和插入的速度极快 不会随着key的增加而变慢
# 2.需要占用大量的内存 内存浪费很多
# 而list相反:
# 1.查找和插入的时间随着元素的增加而增加
# 2.占用空间小 浪费的内存很少
#所以dict是用空间来换取时间的一种方法

#dict可以用在需要高速查找的地方 在python代码中几乎无处不在 正常的使用dict非常的重要 需要牢记的第一条
#就是 dict的key必须是不可变对象
#这是因为dict根据key来计算value的存储位置 如果每次计算相同的key得出的结果不同 那么dict的内部
#直接就混乱了 这个通过key计算位置的算法称为哈希算法
#要保证hash的正确性 作为key的对象就不可变 在python中 字符串 整数等都是不可变的 因此 可以放心的
#作为key 而list是可变的 就不能作为key

#set和dict类似 也是一组key的集合 但不存储key 由于key不能重复 所以 在set里面 没有重复的key
#要创建一个set 需要提供一个list作为输入集合
# s=set([1,2,3])
# print(s)
#注意 传入的参数[1,2,3]是一个list 而显示的{1,2,3}只是告诉你这个set内部有1,2,3这三个元素
# 显示的顺序也不表示set是有序的
#重复的元素在set里面自动被过滤
s=set([1,1,2,3,4,3,2])
#print(s)
#输出结果为:
{1, 2, 3, 4}
#通过add(key)方法可以添加元素到set 可以重复添加 但不会有效果
s.add(4)
#print(s)
#输出结果为:{1, 2, 3, 4}
s.add(5)
#print(s)
#输出结果为:{1, 2, 3, 4, 5}
#可以通过remove(key)方法删除元素
s.remove(4)
#print(s)
#输出结果为i:{1, 2, 3, 5}
#set可以看成数学意义上无序和无重复元素的集合 因此 两个set可以做数学意义上的交集并集等操作:
# s1=set([1,2,3])
# s2=set([2,3,4])
# print(s1&s2)
# print(s1|s2)
#输出结果为:
# {2, 3}
# {1, 2, 3, 4}
#set和dcit的唯一区别仅在于没有存储对应的value 但是 set的原理和dict一样
#所以不可以同样放入可变对象 因为无法判断两个可变对象是否相等 也就无法保证set内部
#"不会有重复元素" 试试把list放入set 看看是否会报错
# a=[1,2,3]
# b=[2,3,4]
# s2=set([a,b])
# print(s2)
# #输出结果为:
# Traceback (most recent call last):
#   File "G:/git/-/day01/day06.py", line 105, in <module>
#     s2=set([a,b])
# TypeError: unhashable type: 'list'

#再议不可变对象
#上面提到了 str是不变对象 list是可变对象
#对于可变对象  比如list 对list进行操作 list内部的内容是会变化的 比如
# a=['a','c','b']
# print(a)
# a.sort()
# print(a)
# #输出结果为:
# ['a', 'c', 'b']
# ['a', 'b', 'c']
#而对于不可变对象呢 比如str 对str进行操作:
# a='Abc'
# print(a.replace('A','a'))
# print(a)
#输出结果为:
# abc
# Abc
#虽然字符串有个replace()方法 也确实变出了'abc' 但是变量啊最后仍然指向’Abc'
#把上面代码改成这样的
# a='Abc'
# b=a.replace('A','a')
# print(b)
# print(a)
#输出结果为:
# abc
# Abc
#要始终牢记的是 a是变量 而'Abc'才是字符串对象 有时候 我们经常说 对象a的内容是'Abc'
#但其实a本身是一个变量，它指向的对象的内容才是'abc'：
#当我们调用a.relace('A','a')的时候 实际上是调用方法replace是作用在字符串对象"Abc"上面的
#而这个方法虽然名字叫replace 但是却没有改变字符串对象"Abc"的内容 相反 replace()方法创建了
#一个新的字符串"abc"并且返回 如果我们用变量b指向该字符串 这样就容易理解了 变量a仍然指向
#原有的字符串"Abc" 但是变量b却指向新的字符串'abc'了
#所以 对于不可变对象来说 调用对象自身的任意方法也不会改变该对象自身的内容 相反 这些方法
#会创建新的对象并返回 这样就保证了不可变对象本身永远是不可变的

#使用key-value存储结构的dict在python中非常有用 选择不可变对象作为key非常重要 最常用的key是字符串
#tuple虽然是不可变对象 但是试试把(1,2,3)和(1,[2,3])放入dict或者set中
# d={(1,2,3):1}
# print(d)
# d1={(1,[2,3])}
#print(d1)
#输出结果为:
# {(1, 2, 3): 1}
# Traceback (most recent call last):
#   File "G:/git/-/day01/day06.py", line 152, in <module>
#     d1={(1,[2,3])}
# TypeError: unhashable type: 'list'








#练习
# address={'北京':1111,'南京':2222,'合肥':3333}
# print('请输入地名')
# add=input()
# while True:
#     if add in address.keys():
#         print('地址为:',add,address.get(add))
#         break
#     else:
#         print('没有这个地址')
#         addUp=input()
#         address.update({add:addUp})
