#!/usr/bin/python3


'''

define

'''


def OutWord():
    print('hello word')


'''

call

'''

OutWord()


'''

param

1. 多参调用
2. 默认值
3. 指定参数赋值
4. 函数返回
'''


def OutWordWithName(name, age=11):
    print('hello', name.title(), int(age))


# 1.
OutWordWithName('liu yue', '22')
# 2.
OutWordWithName(name='li yue')
# 3.
OutWordWithName(age=13, name='liu yue')

# 4.


def SimpleAdd(a, b):
    return (a)+(b)


print(SimpleAdd(1, 2))

'''
1. 通过函数修改列表

将列表传递给函数后，函数就可对其进行修改。
在函数中对这个列表所做的任何修改都是永久性的，
这让你能够高效地处理大量的数据

2. 禁止函数修改列表(通过使用切片)
'''


def ModifyValue(var):
    if var == []:
        var.append(1)
        return
    var = 2


var_1 = 1
var_2 = []
var_3 = [1, 2, 3]

ModifyValue(var_1)
# 1.
ModifyValue(var_2)
# 2.
ModifyValue(var_2[:])

assert(var_1 == 1)
assert(var_2 == [1])
assert(var_3 == [1, 2, 3])
