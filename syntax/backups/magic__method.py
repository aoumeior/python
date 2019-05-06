#! /usr/bin/python3

from os.path import join

'''
1. __del__

那么 __del__ 就是析构器。它不实现语句 del x (以上代码将不会翻译为 x.__del__())。
它定义的是当一个对象进行垃圾回收时候的行为。
当一个对象在删除的时需要更多的清洁工作的时候此方法会很有用.
比如套接字对象或者是文件对象。

'''


class FileObject:
    ''' file manage '''

    def __init__(self, filepath='./', filename='a.txt'):
        self.file = open(join(filepath, filename))

    def __del__(self):
        self.file.close()
        del self.file


'''
2. __cmp__,__eq__,__lt__,__gt__

个人认为在python动态语言中，比较的魔术方法我认为是坏处是多余好处的，我更加偏爱函数定义

'''


'''
3. 针对数值的魔术方法

我认为对于我是应该知道的。


一元操作符和函数

__pos__(self) 实现正号的特性(比如 +some_object)
__neg__(self) 实现负号的特性(比如 -some_object)
__abs__(self) 实现内置 abs() 函数的特性。
__invert__(self) 实现 ~ 符号的特性。


__add__(self, other)        实现加法。
__sub__(self, other)        实现减法。
__mul__(self, other)        实现乘法。
__floordiv__(self, other)   实现 // 符号实现的整数除法。 
__div__(self, other)        实现 / 符号实现的除法。
__truediv__(self, other)    实现真除法。注意只有只用了 from __future__ import division 的时候才会起作用。
__mod__(self, other)        实现取模算法 % 
__divmod___(self, other)    实现内置 divmod() 算法
__pow__(self, other)        实现使用 ** 的指数运算
__lshift__(self, other)     实现使用 << 的按位左移动
__rshift__(self, other)     实现使用 >> 的按位左移动
__and__(self, other)        实现使用 & 的按位与
__or__(self, other)         实现使用 | 的按位或 
__xor__(self, other)        实现使用 ^ 的按位异或
'''


'''
4. 类型转换

- 只介绍几个支持的挺多的

__int__(self)       实现整形的强制转换
__long__(self)      实现长整形的强制转换
__float__(self)     实现浮点型的强制转换
__complex__(self)   实现复数的强制转换 


'''


'''
5. 类的外在表现

1）

__str__(self) 定义当 str() 调用的时候的返回值
__repr__(self) 定义 repr() 被调用的时候的返回值

***** str() 和 repr() 的主要区别在于 repr() 返回的是机器可读的输出，而 str() 返回的是人类可读的。

***** __unicode__(self) 定义当 unicode() 调用的时候的返回值。

***** unicode() 和 str() 很相似，但是返回的是unicode字符串。

个人认为 __str__ 是一个成熟的 python 类库作者，经常用到的魔术方法。且这个魔术方法对新手十分友好。这并不是空穴来风，这是由于 python 的动态性决定的。

2）

__hash__(self) 定义当 hash() 调用的时候的返回值，它返回一个整形，用来在字典中进行快速比较
__nonzero__(self) 定义当 bool() 调用的时候的返回值。本方法应该返回True或者False，取决于你想让它返回的值。


'''
