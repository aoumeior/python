#!/usr/bin/python3


'Unpacking'
# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
muduo = ['2019', 'Chen', 'Shuo', (2019, 1, 1)]

_, last_name, first_name, (year, mounth, day) = muduo

'这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。包括字符串，文件对象，迭代器和生成器。'

'如果 参数 不足 则 将会抛出一个 ValueError 异常'

'star expression'

name, email, *phone_number = ('liu yue', '10010@qq.com', '022-68587222', '15022238901')

print(type(phone_number) is list)
