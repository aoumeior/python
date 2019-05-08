'You want to implement a queue that sorts items by a given priority and always returns the item with the highest priority on each pop operation.'

import heapq

class  PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push (self,item,priority):
        ' warnning : <priority, index> is cmp key '
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'item({!r})'.format(self.name)
    def __str__(self):
        return 'this is a str magic method'



q = PriorityQueue()

q.push(Item('a'), 1)

q.push(Item('z'), 26)

q.push(Item('d'), 4)
