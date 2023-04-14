# -*- coding = utf-8 -*-  
# @Time: 2023/4/14 16:01 
# @Author: Dylan 
# @File: 02_成员方法.py 
# @software: PyCharm

# 定义一个带有成员方法的类
class Student:
    name = None

    def say_hi(self):
        print(f'大家好呀，我是{self.name}, 欢迎大家多多关照')

    def say_hi2(self, msg):
        print(f'大家好，我是{self.name}, {msg}')


stu = Student()
stu.name = "周杰伦"
stu.say_hi2("哎哟 不错哟")

stu1 = Student()
stu1.name = '林俊杰'
stu1.say_hi()
