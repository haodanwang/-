#列表生成式
#列表生成式即List Comprehensions 是python内置的非常简单却强大可以用来创建list的生成式
#举个例子 要生成list(1,2,3,4,5,6,7,8,9,10)可以用list(range(1,11))
#print(list(range(1,11)))
#输出结果为:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#但是如果要生成[1*1,2*2,3*3,4*4.....,10*10]怎么办 方法是循环
# L=[]
# for x in range(1,11):
#     L.append(x*x)
# print(L)
#输出结果为:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#但是循环太繁琐 而列表生成式则可以用一行语句代替循环生成上面的list
#print([x*x for x in range(1,11)])
#输出结果为:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#写列表生成式的时候 把要生成的元素x*x放到前面 后面跟for循环 就可以把list创建出来 十分有用 多写几次 很快就可以熟悉这种语法
#for循环后面还可以附上if判断 这样我们就可以筛选出仅偶数的平方
#print([x*x for x in range(1,11) if x %2==0])
#输出结果为:[4, 16, 36, 64, 100]
#还可以使用两层循环 可以生成全排列
#print([m+n for m in 'ABC' for n in 'XYZ'])
#输出结果为:['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
#三层和三层以上的循环就很少用到了
#运用列表生成式 可以写出非常简洁的代码 例如列出当前目录下的所有文件和目录名 可以通过一行代码实现
#import  os
#print([d for d in os.listdir('.')])#os.listdir()可以列出文件和目录
#输出结果为:
#['.idea', 'day01.py', 'day02.py', 'day03.py', 'day04.py', 'day05.py', 'day06.py', 'day07.py', 'day08.py', 'day09.py', 'day10.py', 'day11.py', 'day12.py', 'day13.py']
#for 循环其实可以同时使用两个甚至多个变量 比如dict的items()可以同时迭代key和value
# d={'x':'A','y':'B','z':'C'}
# for k,v in d.items():
#     print(k,'=',v)
#输出结果为:
# x = A
# y = B
# z = C
#因此列表生成式也可以使用两个变量来生成list:
# d={'x':'A','y':'B','z':'C'}
# print([k+'='+v for k,v in d.items()])
#输出结果为:['x=A', 'y=B', 'z=C']
#最后一个把list中所有的字符串变成小写
# L=['Hello','World','IBM','Apple']
# print([s.lower() for  s in L])
#输出结果为:['hello', 'world', 'ibm', 'apple']

#练习
#如果list中既包含字符串 又包含非字符串 由于非字符串类型没有lower()方法 所以列表生成式会报错
L=['Hello','World',18,'Apple',None]
#print([s.lower() for s in L])
#输出结果为:
# Traceback (most recent call last):
#   File "G:/git/-/day01/day13.py", line 48, in <module>
#     print([s.lower() for s in L])
#   File "G:/git/-/day01/day13.py", line 48, in <listcomp>
#     print([s.lower() for s in L])
# AttributeError: 'int' object has no attribute 'lower'
#使用内建的isinstance函数可以判断一个变量是不是字符串
# x='abc'
# y=123
# print(isinstance(x,str))
# print(isinstance(y,str))
# #输出结果为:
# True
# False
#请修改列表生成式 通过添加if语句保证列表生成式能够正确的的执行
print([s.lower() for s in L if(isinstance(s,str))])
#输出结果为:['hello', 'world', 'apple']
#小结
#运用列表生成器 可以快速的生成list 可以通过一个list去推导出另外一个list 而代码却十分的简洁

