#!/usr/bin/python3

'''

串的大小写转换

S.title() -> string

Return a titlecased version of S, i.e.
words start with uppercase characters, 
all remaining cased characters have lowercase.

S.upper() -> string

Return a copy of the string S converted to uppercase.

S.lower() -> string

Return a copy of the string S converted to lowercase.

'''

str_t = 'nEepu neepu' 
assert(str_t.title() == 'Neepu Neepu')


str_u = 'Neepu Neepu'
assert(str_u.upper() == 'NEEPU NEEPU')

str_l = 'NeePu Neepu'
assert(str_l.lower() == 'neepu neepu')


'''

串的拼接

'''


first_name = 'liu'
last_name = 'yue'

total_name = first_name + ' ' + last_name

assert(total_name == 'liu yue')


'''

移除尾部空白/特定字符

def rstrip(chars)
S.rstrip([chars]) -> string or unicode

Return a copy of the string S with trailing whitespace removed.
If chars is given and not None, remove characters in chars instead.
If chars is unicode, S will be converted to unicode before stripping

剔除字符串开头的空白，或同时剔除字符串两端的空白。为此，可分别使用方法lstrip() 和strip() ： 
'''

str_r = 'neepu '
assert( str_r.rstrip() ==  'neepu')

str_r = 'neepue'
assert(str_r.rstrip('e') == 'neepu')

str_r = ''
assert(str_r.rstrip() == '')


'''

使用str解决类型转换问题

str(object='') -> string

Return a nice string representation of the object. 
If the argument is a string, 
the return value is the same object.

'''

name = 'liu yue'
age = 23

message = name + ',\n' + 'happy ' + str(age) + ' birthday'