#递归函数
#在函数的内部 我们可以调用其他的函数 如果一个函数在函数内部 这个函数就是个递归函数
#举个例子 我们来计算阶乘n！=1*2*3*4*5*6...*n 用函数fact(n)表示
#fact(n)的递归方式写出来的就是:
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
#print(fact(1))
#print(fact(3))
#递归函数的优点是定义简单 逻辑清楚 理论上 所有的递归函数都可以写成循环的方式 但是循环的逻辑不如递归清楚
#使用递归函数需要注意防止栈溢出 在计算机中 函数调用是通过栈这种数据结构来实现的 每当进入一个函数调用 栈就会
#加一层栈帧 每当函数返回 栈就会减少一个栈帧 由于栈的大小不是无限的 所以 递归调用的次数过多 会导致栈溢出
#print(fact(1000))
#输出结果为:
#Traceback (most recent call last):
#   File "G:/git/-/day01/day10.py", line 14, in <module>
#     print(fact(1000))
#   File "G:/git/-/day01/day10.py", line 8, in fact
#     return n*fact(n-1)
#   File "G:/git/-/day01/day10.py", line 8, in fact
#     return n*fact(n-1)
#   File "G:/git/-/day01/day10.py", line 8, in fact
#     return n*fact(n-1)
#   [Previous line repeated 994 more times]
#   File "G:/git/-/day01/day10.py", line 6, in fact
#     if n==1:
# RecursionError: maximum recursion depth exceeded in comparison

#解决递归调用栈溢出的方法就是尾递归优化 事实上尾递归和循环的效果是一样的 所以 把循环看成是一种特殊的尾递归函数也是可以的
#尾递归是指 在函数返回的时候 调用自身本身 并且 return 语句不能包含表达式 这样编译器或者解释器就可以把尾递归做
#优化 使递归本身无论调用多少次 都会只占用一个栈帧 不会出现栈溢出的情况
#上面的fact(n)函数由于return n*fact(n-1)引入了乘法表达式 所以就不是尾递归了 要改成尾递归方式 需要多一点代码 主要是把每一步的乘积
#传入到递归函数里面:
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
#可以看到 return fact_iter(num-1,num*product)仅返回递归函数本身 num-1和num*product在函数调用前就会就算
#不影响函数调用。
#print(fact(4))
#输出结果为:24
#尾递归调用时，如果做了优化 栈不会增长 因此 无论多少次调用也不会导致栈溢出
#遗憾的是 大多数编程语言没有针对尾递归做优化 python解释器也没有做优化 所以 即使把上面的fact(n)函数
#改成尾递归方式 也会导致栈溢出
#小结
#使用递归函数的优点是逻辑简单清楚 缺点是过深的调用会导致栈溢出
#针对尾递归优化的语言可以通过尾递归防止栈溢出 尾递归实际上是和循环等价的 没有循环语句的编程语言只能通过尾递归实现循环
#python标准的解释器没有针对尾递归做优化 任何递归函数都存在栈溢出的问题

#练习
#汉诺塔的移动可以用递归函数非常简单地实现。
#参考文档:https://blog.csdn.net/hikobe8/article/details/50479669
#请编写move(n, a, b, c)函数，
#它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
# 然后打印出把所有盘子从A借助B移动到C的方法，例如：
# def move(n, a, buffer, c):
#     if(n == 1):
#         print(a,"->",c)
#         return
#     move(n-1, a, c, buffer)
#     move(1, a, buffer, c)
#     move(n-1, buffer, a, c)
# move(4, "a", "b", "c")
#汉诺塔算法待定
