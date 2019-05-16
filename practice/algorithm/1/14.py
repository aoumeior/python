# ！/usr/bin/python3
from operator import attrgetter

'''
Sorting Objects Without Native Comparison Support
'''


class User:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return 'User({})'.format(self.id)


users = [User(23), User(3), User(99)]
sorted(users, key=attrgetter('id'))

# [User(3), User(23), User(99)]
