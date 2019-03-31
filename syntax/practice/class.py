
#!/usr/bin/python3

'''
python3

you must like this
'''


'''

in python2.7, you must do like it at the define head.

class Dog(object)

'''


class Dog():
    ''' 一次模拟小狗的简单尝试 '''

    def __init__(self, name, age):
        ''' 初始化 属性'''
        self.name = name
        self.age = age

    def Sit(self):
        ''' 模拟小狗被命令蹲下 '''
        print(self.name.title(), 'is now sitting!')

    def RollOver(self):
        ''' 模拟小狗狗被命令时打滚 '''
        print(self.name.title(), ' rolled over!')


'''

 how create a  instantiated object in programe

'''

mydog = Dog('tom', 11)

assert(mydog.name == 'tom')

assert(mydog.age == int('11'))


'''

how call instantiated object 's function or method

'''


mydog.RollOver()

mydog.Sit()

'''

use inherit

'''

'3.5 version'


class Car():
    ''' 一次模拟汽车的简单尝试 '''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometerreading = 0

    def GetDescriptive(self):
        longname = str(self.year) + ' ' + self.make + ' ' + self.model
        print(longname)


class ElectricCar(Car):
    ''' 电动车的独特之处 '''

    def __init__(self, make, model, year):
        super.__init__(make, model, year)


'2.7 version'


class Animal(object):
    def __init__(self, make, model, year):
        1 + 1

    def Run(self):
        print('Go Go Go')


class Cat(Animal):
    def __init__(self, make, model, year):
        super(Cat, self).__init__(make, model, year)

    def Run(self):
        print('miao ~')
        super(Cat, self).Run()


mycat = Cat('china', 'white', '2019')

mycat.Run()
