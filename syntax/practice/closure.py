#!/usr/bin/python3

'''

you must use at python3

1. nonlocal only support python3
2. 
'''


'''

closure

'''


# 1
def SortPriority(value, group):
    res = False

    def Closure(x):
        if x in group:
            # assign
            res = True
            return (0, x)
        return(1, x)
    value.sort(key=Closure)
    return res


number = [8, 3, 2, 5, 4, 7, 4]
group = {2, 3, 5, 7}

res = SortPriority(number, group)

assert(res == False)

# 2


def GetValue():
    res_t = True

    def Closure(x):
        # get
        # 一旦在闭包的作用域内有与‘外界’同名的变量被赋值，
        # 则外部变量的访问被覆盖
        assert(res_t == True)
    Closure(0)
    return res_t


GetValue()


# 3

def SortPriority_1(value, group):
    res = False

    def Closure(x):
        # python3 support nonlocal
        # but not at python2
        nonlocal res
        if x in group:
            # assign
            res = True
            return (0, x)
        return(1, x)
    value.sort(key=Closure)
    return res


res = SortPriority_1(number, group)

assert(res == True)

# 3


def SortPriority_2(value, group):
    res = [False]

    def Closure(x):
        # in python2, you can do the same as in python3
        if x in group:
            # assign
            res[0] = True
            return (0, x)
        return(1, x)
    value.sort(key=Closure)
    return res[0]


res = SortPriority_2(number, group)

assert(res is True)
