#!/usr/bin/python3

'''

define

'''

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

'''

access

在Python中，第一个列表元素的索引为0，最后一个列表元素的索引可以为 -1

'''
assert(bicycles[0] == 'trek')

assert(bicycles[-1] == 'specialized')

assert(bicycles[-1].title() == 'Specialized')


'''

modify

'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[0] = "python"
assert(bicycles == ['python', 'cannondale', 'redline', 'specialized'])


'''

append

'''

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.append("python")
assert(bicycles == ['trek', 'cannondale', 'redline', 'specialized', 'python'])


'''

insert

'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.insert(0, 'python')
assert(bicycles == ['python', 'trek', 'cannondale', 'redline', 'specialized'])

'''

delete

'''

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
del bicycles[0]
assert(bicycles == ['cannondale', 'redline', 'specialized'])


'''

pop

1. pop() 可删除列表末尾的元素，并让你能够接着使用它。
2. pop(number) 可删除列表任意位置的元素，并让你能够接着使用它。
'''

# 1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
var = bicycles.pop()

assert(bicycles == ['trek', 'cannondale', 'redline'])
assert(var == 'specialized')

# 2
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
var = bicycles.pop(2)

assert(bicycles == ['trek', 'cannondale', 'specialized'])
assert(var == 'redline')


'''

def remove(value)
L.remove(value)
-- remove first occurrence of value.
Raises ValueError if the value is not present.

在容器中我们永远不要在遍历容器中删除/增加元素内容
相反我们应该使用容器内置方法

方法remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，
就需要使用循环来判断是否删除了所有这样的值。
'''

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.remove("trek")
assert(bicycles == ['cannondale', 'redline', 'specialized'])


'''
1.
sort(cmp, key, reverse)
param cmp

L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1

2.
sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
param iterable
'''

# 1
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()

'顺序也是断言相同的一个评判标准 而不是仅仅容器中值相同'
assert(cars == ['audi', 'bmw', 'subaru', 'toyota'])

# 2
cars = ['bmw', 'audi', 'toyota', 'subaru']
assert(sorted(cars) == ['audi', 'bmw', 'subaru', 'toyota'])

'''

L.reverse() -- reverse *IN PLACE*

'''

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()

assert(cars == ['subaru', 'toyota', 'audi', 'bmw'])

'''

def len(object)
len(object) -> integer

Return the number of items of a sequence or collection.

'''

cars = ['bmw', 'audi', 'toyota', 'subaru']
assert(len(cars) == 4)


'''



'''


squares = [value ** 2 for value in range(1, 3)]
assert(squares == [1, 4])


'''

切片

1. 切片的使用
2. 切片的遍历
3. !!!! 切片的应用
    a.复制列表
'''

# 1

# [0 1)
assert([1, 2, 2, 3, ][0:1] == [1])

# 默认开始索引为 0
assert([1, 2, 2, 3, ][:2] == [1, 2])

# 默认结束索引为 list 大小-1
assert([1, 2, 2, 3, ][:] == [1, 2, 2, 3])

# 2

total = []
for value in [1, 2, 3][:]:
    total.append(value)
assert(total == [1, 2, 3])

# !!!! 3

list_r = [1, 2, 3, 4, 5]

list_c = list_r[:]

list_r.remove(1)

assert(list_r != list_c)

# 过下面的断言就知道为什么使用切片来进行复制了

list_r_a = [1, 2, 3, 4]
list_c_a = list_r_a

list_c_a.remove(1)
assert(list_r_a == list_c_a)
