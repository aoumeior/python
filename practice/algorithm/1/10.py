#!/usr/bin/python3

def dedupe_1(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [i for i in range(1,4)]
list(dedup_1(a))

'''
trying to eliminate duplicates in a sequence of unhashable types (such as dicts),
'''
def dedup(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else Key(item)
        if val not in seen:
            yield item
        seen.add(val)
