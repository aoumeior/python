#!/usr/bin/python3


class Foo:

    def __init__(self, name):
        self._lastname = name

    @property
    def lastname(self):
        'get the last name'
        return self._lastname

    @lastname.setter
    def lastname(self, name):
        if not name:
            raise Exception('invalid last name')
        self._lastname = name

    @lastname.deleter
    def lastname(self):
        del self._lastname


f = Foo('Liu')


print(f.lastname)

f.lastname = ''
