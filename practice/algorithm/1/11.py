#!/usr/bin/python3
'Naming a Slice'

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:35])

print(cost)

' Instead of doing that, why not name the slices like this?'

SHARES = slice(20,23)
PRICE = slice(31,35)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)


'In addition, '
'you can map a slice onto a sequence of a specific size by using its indices(size) method.'
'This returns a tuple (start, stop, step) where all values have been suitably limited to fit within bounds'

t = slice(5, 50, 2)

s = 'helloword'

'but the indices result isn't indetermination, Reference page:19'
for i in range(*t.indices(len(s))):
    print(s[i])


