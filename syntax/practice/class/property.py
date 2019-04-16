#!/usr/bi/python3


class Color:
    ''' a color class '''

    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception('invalid Name')
        self._name = name

    def _get_name(self):
        return self._name

    def _del_name(self):
        del self._name
    name = property(_get_name, _set_name, _del_name, "name operator")


c = Color('#000ff', 'bright red')


c.name = '1'


del c.name

help(Color)
