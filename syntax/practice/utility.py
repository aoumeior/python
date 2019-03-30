# /usr/bin/python3

'''

int

Convert a number or string to an integer, or return 0 if no arguments are given. 
If x is floating point, the conversion truncates towards zero.
If x is outside the integer range, the function returns a long instead.

'''

age = input('请输入你的年龄')
assert(int(age) == 11)


'''

input

如果你使用的是Python 2.7，应使用函数raw_input() 来提示用户输入。
这个函数与Python 3中的input() 一样，也将输入解读为字符串。 
Python 2.7也包含函数input() ，但它将用户输入解读为Python代码，
并尝试运行它们。因此，最好的结果是出现错误，指出Python不明白输入的代码；
而最糟的结果是，将运行 你原本无意运行的代码。如果你使用的是Python 2.7，
请使用raw_input() 而不是input() 来获取输入。

'''
while 1:
    message = input('你说,我学:\n')
    print(message)


'''

min
max

'''

assert(max([1, 2, 3, 4]) == 4)
assert(min([1, 2, 3, 4]) == 1)
