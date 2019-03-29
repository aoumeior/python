# PRACTICE

## HELLOWROD

FILE: [[ ../helloword.py](./helloword.py)]

1. 第一行那样的特殊形式的注释。它被称作组织行 —— 源文 件的头两个字符是 #! ，后面跟着一个程序。这行告诉你的 Linux/Unix 系统当你执行 你的程序的时候，它应该运行哪个解释器。
2. 跟在注释之后的是一句 Python 语句 —— 它只是打印文本“Hello World”。 print 实际上是一个操作符，而“Hello World”被称为一个字符(注：3版本之前是这样，但是3之后的不太确定 print 是不是一个操作符。)
3. 在linux中 肯能需要 `chmod a+x helloworld.py ` 添加执行标记
4. 有一个更通用的方式用来指示执行的编译程序 `#!/usr/bin/env python`，`env` 用于搜所 操作系统中 python 可能存在的目录并且执行。