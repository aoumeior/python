#!/usr/bin/python3

'''

definde

'''

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

while loop

1. base
2. break
3. continue 

'''

# 1.
list_t = [1, 2, 3, 4]
while list_t:
    list_t.pop()

# 2.

list_t = [1, 2, 3, 4]
while list_t:
    msg = list_t.pop()
    if msg == 4:
        break
    print(msg)

# 3.
list_t = [1, 2, 3, 4]
while list_t:
    msg = list_t.pop()
    if msg == 4:
        continue
    print(msg)
