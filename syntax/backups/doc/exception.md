
''' python

# python 中对于类对象的继承，可以通过 __mro__ 魔术方法进行查看，此方法一般是由于
# except 语句是顺序检查的，第一个匹配的会执行。所以应按照子类到基类的书写方式。

FileNotFoundError.__mro__
'''

`SystemExit` 、 `KeyboardInterrupt` 和 `GeneratorExit` 之外的
所有异常都可以被 `Exception`捕获。 如果你还想捕获这三个异常，将 `Exception` 改成 `BaseException` 即可。

python 除了提供一些内置异常类外，我们还可以继承内置来定义自己的异常类。

关于自定义异常类我们需要关注一下几点：


    自定义异常类应该总是继承自内置的 Exception 类，或者是继承自那些本身就是从 Exception 继承而来的类。尽管所有类同时也继承自 BaseException ，但你不应该使用这个基类来定义新的异常。 BaseException 是为系统退出异常而保留的。
    比如KeyboardInterrupt 或 SystemExit 以及其他那些会给应用发送信号而退出的异常。因此，捕获这些异常本身没什么意义。这样的话，假如你继承 BaseException 可能会导致你的自定义异常不会被捕获而直接发送信号退出程序运行。


```python
# 该语句是try语句执行成功后执行else语句，否则执行except语句.
try...except...else
```

[参考：python: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
