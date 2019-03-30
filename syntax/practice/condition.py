#!/usr/bin/python3

'''

简单例子

'''

if 1 == 1 and 2 == 2:
    assert(True)
else:
    assert(False)

if 1 != 1 and 2 != 2:
    assert(False)

'''

 短路行为

'''

var_assert = []
if 1 == 1 or (var_assert.append(1)) == []:
    assert(var_assert == [])

'''

判断一个元素是否在列表中

'''

var_assert = [1, 2, 3, 4, 5, 6]
if 1 not in var_assert:
    assert(False)

# if-elif-else 结构
if 1 == 1:
    assert(True)
elif 1 == 1:
    assert(True)
else:
    assert(False)

'''

 省略 else 的条件语句

'''
# 从这里就能看出非块状作用域
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
assert(price == 5)
