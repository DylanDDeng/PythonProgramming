# -*- coding = utf-8 -*-  
# @Time: 2023/4/14 17:23 
# @Author: Dylan 
# @File: 04_构造方法.py 
# @software: PyCharm

class Student:
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

        print('Student类创建了一个类对象')
    def say_hi(self):
        print(f'大家好，我是{self.name}, 我的年龄是{self.age}, 我的电话是{self.tel}')

stu = Student('周杰伦', 35, '20930303')
stu.say_hi()