# /bin/usr/python3

import sys

filename = sys.argv[1]

contacts = []

with open(filename) as file:
    header = file.readline().strip().split(' ')
    for line in file:
        line = line.strip().split(' ')
        contact_map = zip(header, line)
        contacts.append(dict(contact_map))
    for contact in contacts:
        print('email : {email} -- {last}, {first}'.format(**contact))
