#定义函数
#在python中 定义一个函数要使用def语句  依次写入函数名 括号 括号中的参数和冒号:
#然后，在缩进块中编写函数体 函数的返回值用return语句返回

#我们以自定义一个求绝对值的的my_abs函数为例:
# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x

#print(my_abs(-99))

#输出结果为:99

#请注意 函数体内部的语句在执行的时候 一旦执行到return时候 函数就会执行完毕 函数执行完毕后
#并将结果返回 函数内部通过条件判断和循环可以实现非常复杂的逻辑
#如果没有return 语句 函数执行完结束后也会返回结果 只是结果为None return None可以简写为return

#空函数
#如果想定义一个什么也不做的空函数 可以用pass语句
# def nop():
#     pass
#pass语句就是什么也不做 那有什么用 实际上pass可以用来作为占位符 比如现在还没想好怎么写函数的代码
#就可以先放一个pass 让代码可以运行起来
#pass还可以用在其他语句里面 比如:
# age=15
# #bool 0
#
#  if age >=18:
# 0#     pass
# # else:
# #     print('11')
#如果缺少了pass 代码就会报错

#参数检查
#调用函数的时候 如果参数个数不对 Python解释器会自动检查出来 并抛出TypeError:
#print(my_abs(1,2))
#输出结果为:
# Traceback (most recent call last):
#   File "G:/git/-/day01/day08.py", line 38, in <module>
#     print(my_abs(1,2))
# TypeError: my_abs() takes 1 positional argument but 2 were given
#但是如果参数类型不对 python解释器无法帮我们检查。试试my_abs()和内置函数的区别
#print(my_abs('A'))
#输出结果为:
# Traceback (most recent call last):
#   File "G:/git/-/day01/day08.py", line 45, in <module>
#     print(my_abs('A'))
#   File "G:/git/-/day01/day08.py", line 7, in my_abs
#     if x>=0:
# TypeError: '>=' not supported between instances of 'str' and 'int'
#print(abs('A'))
#输出结果为:
# Traceback (most recent call last):
#   File "G:/git/-/day01/day08.py", line 53, in <module>
#     print(abs('A'))
# TypeError: bad operand type for abs(): 'str'

#当传入了不合法的参数的时候 内置函数abs会检查出参数错误 而我们定义的my_abs()没有参数检查
#会导致if语句出错 出错信息当然和abs不一样 所以 这个函数的定义不够完善

#让我们修改下my_abs的定义 对参数类型做检查 只允许整数和浮点数类型的参数 数据类型检查
#可以通过内置函数isinstance()实现
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     else:
#         if x>=0:
#             return x
#         else:
#             return -x
#添加了参数检查以后 如果传入错误的参数类型 函数就可以抛出一个错误

#print(my_abs('A'))
#输出结果为:
# Traceback (most recent call last):
#   File "G:/git/-/day01/day08.py", line 75, in <module>
#     print(my_abs('A'))
#   File "G:/git/-/day01/day08.py", line 67, in my_abs
#     raise TypeError('bad operand type')
# TypeError: bad operand type

#返回多值
#函数可以返回多值？答案是肯定的
#就比如在游戏中经常需要从一个点移动到另一个点 给出坐标 位移和角度 就可以计算出新的坐标
import math

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

# x,y=move(100,100,60,math.pi/6)
# print(x,y)

#输出结果为:
# 151.96152422706632 70.0

#但是其实这只是一个假象 python函数的返回仍然是个单一值
#r=move(100,100,60,math.pi/6)
#print(r)
#输出结果为:
#(151.96152422706632, 70.0)
#原来返回值是一个tuple 但是 在语法上 返回一个tuple可以省略括号 而多个变量接收同一个tuple
#按位置赋值给对应的值 所以 python的函数范湖在多值就是返回一个tuple 但写起来更方便

#小结
#定义函数的时候 需要确定函数名和参数个数 如果有必要 可以先对参数的类型做检查
#函数体内部可以用return 随时返回函数结果 函数执行完毕没有return语句时候 自动返回return None
#函数可以返回多值 但其实就是一个tuple


#练习
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0的两个解
def quadratic(a,b,c):

    if a==0:
        print('此方程不是一元二次方程')
        n=(-c)/b
        return n
    else:
        del1=b*b-4*a*c
        if del1<0:
            print('此方程无解')
        elif del1==0:
            print('此方程一个解')
        else:
            print('此方程有两个不等的实根')
            n3=math.sqrt(del1)
            n1=((-b)+n3)/(2*a)
            n2=((-b)-n3)/(2*a)
            return (n1,n2)


print(quadratic(1,4,3))

#输出结果为:
#此方程有两个不等的实根
#(-1.0, -3.0)
