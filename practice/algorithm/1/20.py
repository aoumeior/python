#!/usr/bin/python3

# python2 don't find ChainMap
from collections import ChainMap
'''
Combining Multiple Mappings into a Single Mapping
'''
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c['x'])      # Outputs 1  (from a)
print(c['y'])      # Outputs 2  (from b)
print(c['z'])      # Outputs 3  (from a)

a['x'] = 13

assert(c['x'] == 13)  # true

'''

'''
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
# new dict subject to uodate dict
merged.update(a)
merged  # {'z': 3, 'x': 1, 'y': 2}

# if any of the original dictionaries mutate,
# the changes don’t get reflected in the merged dictionary.
a['x'] = 13
merged['x']  # 1


'''
1
'''
values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
# ChainMap({'x': 3}, {'x': 2}, {'x': 1})
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])

print(values)
