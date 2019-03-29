#!/usr/bin/python3


animals = ['cat', 'pig', 'dog']

'''
for 语句末尾的冒号告诉Python，下一行是循环的第一行。
'''
for animal in animals:
    print(animal)


'''
range

def range(stop)
range(stop) -> list of integers range(start, stop[, step]) -> list of integers

Return a list containing an arithmetic progression of integers. 
range(i, j) returns [i, i+1, i+2, ..., j-1]; 
start (!) defaults to 0. When step is given, it specifies the increment (or decrement).
For example, range(4) returns [0, 1, 2, 3]. The end point is omitted!
 These are exactly the valid indices for a list of 4 elements.
'''

# [1, 5)
for figure in range(1, 5):
    print(str(figure) + ' is cool')


'''
def range(stop)
range(stop) -> list of integers range(start, stop[, step]) -> list of integers

Return a list containing an arithmetic progression of integers. range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0. When step is given, it specifies the increment (or decrement). For example, range(4) returns [0, 1, 2, 3]. The end point is omitted! These are exactly the valid indices for a list of 4 elements.
'''

'这里不知道怎么了，rt 被编辑器推断为 list 对象 根据 type 返回的却是 range class'
rt = range(0, 1)
# print(type(rt))


'''

min
max

'''

assert(max([1, 2, 3, 4]) == 4)
assert(min([1, 2, 3, 4]) == 1)
