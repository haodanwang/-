#条件判断

#计算机之所以能做很多的自动化任务，因为它可以自己做条件判断
#比如，输入用户的年龄，根据年龄打印不同的内容，在python中，用if语句实现:
# age=20
# if age>=18:
#     print('you age is',age)
#     print('adult')
#输出结果为:
# you age is 20
# adult
#根据python的缩进规则，如果if语句判断是True,就把缩进的两行print语句执行了，否则什么也不做
#也可以给if添加一个else语句，意思是如果if判断是False，不用执行if的内容，去吧else的执行了:
# age=3
# if age>=18:
#     print('your age is',age)
#     print('Adult')
# else:
#     print('your age is',age)
#     print('Teenager')
# 输出结果为:
# your age is 3
# Teenager
#注意不要少写了冒号:
#当然上面的判断是很粗略的，完全可以用elseif来做更细致的判断
# age=3
# if age>=18:
#     print('Adult')
# elif age>=6:
#     print('teenager')
# else:
#     print('Kid')
# 输出结果为:
# Kid
# elif 是 else if的缩写,完全可以有多个的elif,所以if语句的完整形式是:
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>
#if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，
# 把该判断对应的语句执行后，就忽略掉剩下的elif和else，
# 所以，请测试并解释为什么下面的程序打印的是teenager：
# age=20
# if age>=6:
#     print('Teenager')
# elif age>=18:
#     print('adult')
# else:
#     print('Kid')
#if 判断条件还可以简写，比如写:
#x=1
#x='1'
#x=['1']
#x=(1,)
# if x:
#     print('True')
# 输出结果为:True
# 只要x是非零数值,非空字符串，非空list等，就判断为True,否则为False

#inpu
#最后再看一个有问题的条件判断，使用input()读取用户输入，这样可以自己输入
# birth=input('birth:')
# if birth<2000:
#     print('00前')
# else:
#     print('00后')
# 输入1982,结果报错：
# birth:1982
# Traceback (most recent call last):
#   File "G:/git/-/day01/day04.py", line 67, in <module>
#     if birth<2000:
# TypeError: '<' not supported between instances of 'str' and 'int'
#这是因为input()返回的数据类型是str,str不能直接和整数比较，必须先把str转换成整数
#python提供了int()函数来完成这件事情
# s=input('birth:')
# birth=int(s)
# if birth<2000:
#     print('00前')
# else:
#     print('00后')
# #输出结果为:
# birth:1982
# 00前

#练习题
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# height=1.75
# weight=80.5
# bmi=weight/(height*height)
# if bmi<18.5:
#     print('过轻')
# elif 25>=bmi>=18.5:
#     print('正常')
# elif 28>bmi>25:
#     print('过重')
# elif 32>=bmi>=28:
#     print('肥胖')
# else:
#     print('严重肥胖')
#输出结果为:过重
