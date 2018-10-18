#使用list和tuple

#Python内置的一种数据类型是列表:list list是一个有序的集合，可以随时添加和删除其中的元素
# 比如,列出班里所有同学的名字,就可以用一个list表示:
#classmates=['Michael','Bob','Tracy']
# print(classmates)
# 输出结果为:
# ['Michael', 'Bob', 'Tracy']
# 变量classmates就是一个list,用len()函数可以获取list元素的个数
# print(len(classmates))
# 输出结果为:3
#用索引来访问list中的每一个元素,索引下标从0开始
# print(classmates[0],classmates[1],classmates[2])
#输出结果为:Michael Bob Tracy
# print(classmates[3])
# 输出结果为:
# Traceback (most recent call last):
#   File "G:/git/-/day01/day03.py", line 15, in <module>
#     print(classmates[3])
# IndexError: list index out of range
#当索引超出了范围，python会报一个IndexError错误，所以要确保索引不要越界
# 记得最后一个元素的索引是len(classmates)-1
#如果需要取最后一个元素,除了计算索引位置外,还有可以用-1做索引,直接获取最后一个元素
# print(classmates[-1])
# 输出结果为:Tracy
# 以此类推,可以获取到倒数第二个，倒数第三个:
# print(classmates[-2],classmates[-3])
# 输出结果为:Bob Michael
# print(classmates[-4])
# # 当然倒数第四个就越界了
# #输出结果为：
# Traceback (most recent call last):
#   File "G:/git/-/day01/day03.py", line 29, in <module>
#     print(classmates[-4])
# IndexError: list index out of range

#list是一个可变的有序表,所以,可以往list中追加元素到末尾
# classmates.append('Adam')
# print(classmates)
# 输出结果为:['Michael', 'Bob', 'Tracy', 'Adam']
#也可以把元素插入到指定的位置，比如索引号为1的位置：
# classmates.insert(1,'Jack')
# print(classmates)
#输出结果为：['Michael', 'Jack', 'Bob', 'Tracy']
#要删除list末尾的元素,采用pop()方法:
# print(classmates.pop())
# print(classmates)
# 输出结果为:
# Tracy
# ['Michael', 'Bob']
#要删除指定位置的元素，采用pop(i)方法，其中i是索引位置
# print(classmates.pop(1))
# print(classmates)
# 输出结果为:
# Bob
# ['Michael', 'Tracy']
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
# classmates[1]='Spark'
# print(classmates)
# 输出结果为:['Michael', 'Spark', 'Tracy']
#list里面的元素的数据类型也可以不同，比如:
# L=['Apple',12,True]
# print(L)
# 输出结果为:['Apple', 12, True]
#list元素也可以是另外一个list,比如：
# S=['Python','java',['Asp','php'],'scheme']
# print(len(S))
# 输出结果为:4
# p=['Asp','PHP']
# s=['python','java',p,'scheme']
# 要取到"PHP"可以写p[1]或者s[2][1].因此s可以看成一个二维数组,类似的还有三维,四维等
#如果list中一个元素也没有,就是一个空的list,它的长度为0

#tuple
#另外一种有序列表叫做元组:tuple.它和list非常的相似,但是tuple一旦初始化就不能更改
#比如相同的赋值
classmates=('Miachel','Bob','Tracy')
# print(classmates)
# 输出结果为:('Miachel', 'Bob', 'Tracy')
#现在，这classmate这个tuple不能变了,它没有append(),insert()这样的方法。
#获取元素的方法和list一样，你可以正常的使用classmates[0].classmates[1],
#但是不能赋值成另外的元素
# 不可变的tuple有什么意义？因为tuple不可变,所以代码更安全。如果可能
# 能用tuple代替list就尽量使用tuple
# 但是在tuple的使用中存在一个陷阱
#如果定义一个空的tuple
# t=()
# print(t)
# 输出结果为:()
#但是如果只要定义一个元素的tuple,如果你这么定义
# t=(1)
# print(t)
# 输出结果为：1 并不是想象中的(1)
#因为括号既可以表示tuple,又可以表示数学计算公式里面的小括号,这就产生了歧义
# 因此,python规定,在这种情况下,按照小括号进行计算,计算结果自然为1
# 所以,只有一个元素的tuple的定义的时候必须加一个逗号,来消除歧义
# t=(1,)
# print(t)
# 输出结果为:(1,)
#Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。

#最后看一个可变的tuple:
t=('a','b',['A','B'])
print(t)
t[2][0]='X'
t[2][1]='Y'
print(t)
#输出结果为：
# ('a', 'b', ['A', 'B'])
# ('a', 'b', ['X', 'Y'])



