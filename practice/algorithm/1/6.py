'''
You want to make a dictionary that maps keys to more than one value (a so-calle “multidict”).

'''


'you should do like it'

from collections import defaultdict

dic =  defaultdict(list)

dic['a'].append(1)
dic['a'].append(2)

dic['b'].append(3)
dic['b'].append(3)

'defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3, 3]})'

'advantage:'

'1'
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

'2'
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
