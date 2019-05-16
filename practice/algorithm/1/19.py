#!/usr/bin/python3
'''
Transforming and Reducing Data at the Same Time 
'''

'''
1
'''
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

'''
2
'''
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

'''
3
'''
s = sum((x * x for x in nums))    # Pass generator-expr as argument
s = sum(x * x for x in nums)      # More elegant syntax

'''
4
'''

nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])
