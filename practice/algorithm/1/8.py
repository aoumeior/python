#!/usr/bin/python3

'''
You want to perform various calculations on a dictionary of data.
'''

prices = {
  'ACME': 45.23,
  'AAPL': 612.78,
  'IBM': 205.55,
  'HPQ': 37.20,
  'FB': 10.75
}

'''
zip

Return a zip object whose .next() method
returns a tuple where the i-th element comes from the i-th iterable argument. 
The .next() method continues 
until the shortest iterable in the argument sequence 
is exhausted and then it raises StopIteration

'''
min_price = min(zip(prices.keys(), prices.values()))
#('AAPL', 612.78)

max_price = max(zip(prices.keys(), prices.values()))
#('IBM', 205.55)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
# (45.23, 'ACME'), (205.55, 'IBM'),
# (612.78, 'AAPL')]

'''!!!
When doing these calculations, be aware that zip() creates an iterator that can only be
consumed once.
'''

'''!!
you need notic, the question the key will be used to determine the result in instances where multiple entries happen to have the same value.
prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
min(zip(prices.values(), prices.keys()))
#(45.23, 'AAA')
max(zip(prices.values(), prices.keys()))
#(45.23, 'ZZZ')
'''

'''
using the zip method , because you may need return a key map

'''