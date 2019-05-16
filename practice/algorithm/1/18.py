#!/usr/bin/python3
'''
Mapping Names to Sequence Elements
'''

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

print(sub.addr, sub.joined)  # ('jonesy@example.com', '2012-10-19')

print(len(sub))  # 2
addr, joined = sub
print(addr, joined)  # ('jonesy@example.com', '2012-10-19')

'''
1
'''
Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
        return total


s = Stock('ACME', 100, 123.45)
s = s._replace(shares=75)
print(s)  # Stock(name='ACME', shares=75, price=123.45)
