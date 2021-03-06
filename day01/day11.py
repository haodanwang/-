#python的高级特性

#切片
#取一个list或者tuple的部分元素是是非常常见的操作 比如一个list如下
L=['Michael','Sarah','Tracy','Bob','Jack']
#取三个元素 应该怎么做
#笨办法:
#print(L[0],L[1],L[2])
#输出结果为:
#Michael Sarah Tracy
#之所以是笨办法是因为拓展一下 去N个元素就没辙了
#取N个元素 也就是索引为0-（N-1）的元素 可以用循环：
# r=[]
# n=3
# for i in range(n):
#     r.append(L[i])
# print(r)
#输出结果为:['Michael', 'Sarah', 'Tracy']
#对这种经常取值索引范围的操作 用循环十分繁琐 因此 python提供了切片(Slice)操作符 能大大简化这种操作
#对应上面的问题 取前三个元素 用一行代码就能完成切片
#print(L[0:3])
#输出结果为:['Michael', 'Sarah', 'Tracy']
#L[0:3]表示 从索引0开始取 直到索引3为止 但是不包括索引3 即索引0,1,2正好是三个元素
#如果第一个元素为0 还可以省略 L[:3]
#print(L[:3])
#输出结果为:['Michael', 'Sarah', 'Tracy']
#也可以从索引1开始 取出两个元素出来:
#print(L[1:3])
#输出结果为:['Sarah', 'Tracy']
#类似的 既然python支持L[-1]取倒数第一个元素 那么它同样支持倒数切片 试试:
#print(L[-2:])
#print(L[-2:-4])  #为什么不支持倒序切片 这样的输出结果为:[]
#输出结果为:['Bob', 'Jack']
#记住倒数第一个元素的索引为-1
#切片操作十分有用 我们先创建一个0-99的数列
L=list(range(100))
#print(L)
#可以通过切片轻松取出某一段数列 比如前10个
#print(L[:10])
#输出结果为:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#后10个数
#print(L[-10:])
#输出结果为:[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#前11-20个数
#print(L[10:20])
#输出结果为:[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
#前10个数 每两个取一个
#print(L[:10:2])
#输出结果为:[0, 2, 4, 6, 8]
#所有数 每5个取一个:
#print(L[::5])
#输出结果为:
#[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
#tuple也是一种list 唯一的区别是tuple是不可变的 因此 tuple也可以用切片操作 只是操作结果扔是tupele
#print((0,1,2,3,4)[:3])
#输出结果为:(0, 1, 2)
#字符'XXX'也可以看出是一种list 每一个元素就是一个字符 因此 字符串也可以用切片操作 只是操作结果扔是字符串
#print('ABCDEFG'[:3])
#输出结果为:ABC
#print('ABCDEFGHI'[::2])
#输出结果为:ACEGI

#练习
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    L=len(s)
    while L>0:
        L=L-1
        if s[:1]==' ':
            s=s[1:]
        elif s[-1:]==' ':
            s=s[:-2]
        else:
            break
    return s
print(trim('    Hello  '))
print('Hello')