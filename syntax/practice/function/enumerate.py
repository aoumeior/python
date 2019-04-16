# ！/binusr/python3

import sys

filename = sys.argv[1]


with open(filename) as file:
    for index, line in enumerate(file):
        print("{0}: {1}".format(index, line))
