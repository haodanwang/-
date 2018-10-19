#循环
#要计算1+2+3,我们可以写表达式
#print(1+2+3)
#输出结果为:6
#要计算1+2+3....+10，勉强也能写的出来
#但是，如果计算1+2+3...+100000,直接写表达式就不可能了
#为了让计算机能计算成百上千万次的重复运算，我们需要循环语句
#python的循环有两种 一种是for..in循环 依次把list或tuple的每个元素迭代出来:
# names=['Michael','Bob','Tracy']
# for name in names:
#     print(name)
#执行这段代码 会依次打印names里面的每一个元素
# #打印结果为:
# Michael
# Bob
# Tracy
#所以for x in..循环就是把每个变量代入变量x 然后执行缩进块语句。
#再比如我们想计算1-10的整数之和，可以用一个sum变量做累加:
# sum=0
# for x in [1,2,3,4,5,6,7,8,9,10]:
#     sum=sum+x
# print(sum)
#输出结果为:55
#如果要计算1-100的整数和，从1写到100有点困难 幸好python提供了一个range()函数
#可以生成一个整数序列，在通过list()函数转换为list.比如range(5)生成的序列就是
#从0开始小于5的整数
#print(list(range(5)))
#输出结果为:[0, 1, 2, 3, 4]
#range(101)就是生成0-100整数序列 计算如下
# sum=0
# for x in range(101):
#     sum=sum+x
# print(sum)
# 输出结果为:5050
#第二种循环就是while循环 只有条件满足 就会不断循环，条件不满足就会退出循环
#比如我们计算100以内的奇数之和 可以用while循环实现
# sum=0
# n=99
# while n>0:
#     sum=sum+n
#     n=n-2
# print(sum)
# 输出结果为:2500
#在循环内部变量n不断自减 直到变为-1的时候 不再满足while条件 循环退出

#练习
#请利用循环依次对list中的每个名字打印出Hello, xxx!：
# L = ['Bart', 'Lisa', 'Adam']
# for name in  L:
#     print('Hello,%s'% name)
#输出结果为:
# Hello,Bart
# Hello,Lisa
# Hello,Adam

#break


