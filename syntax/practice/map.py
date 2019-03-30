#!/usr/bin/python3


map_e = {'color': 'green', 'points': 5}

'''

access

'''
assert(map_e['color'] == 'green')


'''

addtion

'''

map_e['name'] = 'liu yue'

assert(map_e['name'] == 'liu yue')

'''

modify

'''

map_e['name'] = 'li yue'

assert(map_e['name'] == 'li yue')


'''

delete

!! Python 3.X 里不包含 has_key() 函数，被 __contains__(key) 替代

'''
del map_e['name']

assert(not (map_e.__contains__('name')))


'''

for-each

1. 遍历 key value
2. 遍历 key
3. 遍历 value
'''
# 1.

map_t = {}
for key, value in map_e.items():
    map_t[key] = value

assert(map_t == map_e)

# <class 'dict_items' >
T_ = map_t.items()

# 此处换成 == 会断言失败，
# 因为 items 方法返回的并不是一个列表，而是针对 dict 的一个辅助类
assert(map_t.items() != [('color', 'green'), ('points', 5)])


# 2.

list_a = []
for key in map_e.keys():
    list_a.append(key)

# <class 'dict_keys'>
T_ = map_e.keys()

# 同上仍是辅助类，用于遍历 key 值
assert(list_a != map_e.keys())


# 3.
list_a = []
for value in map_e.values():
    list_a.append(value)

# 同上 <class 'dict_values'>
T_ = map_e.values()


'''

map 的嵌套

'''

map_nest = {'t' : {'a': 1} }

'''

map的辅助工具

'''

res = set([1, 1, 2, 3, 4])


assert({1, 2, 3, 4} == res)
