#!/usr/bin/python3

from itertools import compress
'''
Filtering Sequence Elements
'''
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n > 0]
# [1, 4, 10, 2, 3]
[n for n in mylist if n < 0]
# [-5, -7, -1]


'''
if you concern memory using rate , you can use generator expression
'''
pos = (n for n in mylist if n > 0)

for x in pos:  # pos is generator expression
    pass


'''
filter(function, iterable)
return
python3 :  generator express
python2 :  list
'''
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


# Outputs ['1', '2', '-3', '4', '5']
ivals = list(filter(is_int, values))


'''

'''

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
clip_neg = [n if n > 0 else 0 for n in mylist]

'''

'''
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE'
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
list(compress(addresses, more5))
# ['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']
