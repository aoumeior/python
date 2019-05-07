#! /bin/usr/python3

def example():
    try:
        int('N/A')
    except ValueError as e:
        ''' 异常新建再一次抛出、之前的异常被先被抛出 '''
        raise RuntimeError('A parsing error occurred') from e

'error'
example() 


'''
    warning
'''

import warnings

def func(x, y, logfile=None, debug=False):
    '''
    warn()的参数是一个警告消息和一个警告类，警告类有如下几种：
    UserWarning, DeprecationWarning, SyntaxWarning, RuntimeWarning, ResourceWarning, FutureWarning
    '''
    if logfile is not None:
        warnings.warn("logfile argument deprecated", DeprecationWarning)


'''
通常来讲，警告会输出到标准错误上。
python3 -W all example.py
如果你想讲警告转换为异常，可以使用 -W error
python3 -W error example.py
'''
func(1, 2, '1')