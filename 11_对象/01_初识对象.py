# -*- coding = utf-8 -*-  
# @Time: 2023/4/14 11:47 
# @Author: Dylan 
# @File: 01_初识对象.py 
# @software: PyCharm

# 设计一个类（类比设计一个表）
class Student:
    name = None  # 记录学生姓名
    gender = None  # ... 性别
    nationality = None
    native_place = None
    age = None
# 创建一个对象 （类比 打印一张登记表）
stu_1 = Student()
# 对象属性进行赋值（类比 填写表单）
stu_1 = Student()
stu_1.name = '林军杰'
stu_1.gender = "男"
stu_1.nationality = '中国'
stu_1.native_place = "山东省"
stu_1.age = 31

print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)
