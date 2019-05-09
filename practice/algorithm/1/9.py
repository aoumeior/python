#!/usr/bin/python3

'''
Finding Commonalities in Two Dictionaries
'''

a = {
  'x' : 1,
  'y' : 2,
  'z' : 3
}

b = {
  'w' : 10,
  'x' : 11,
  'y' : 2
}

(a.keys() - b.keys()) # {'z'}

(a.keys() - b.keys()) # {'z'}

(a.items() & b.items()) # {('y', 2)}


# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}