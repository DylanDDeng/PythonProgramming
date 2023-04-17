# -*- coding = utf-8 -*-  
# @Time: 2023/4/17 17:19 
# @Author: Dylan 
# @File: 10_类型注解_变量.py 
# @software: PyCharm

"""
演示变量的类型注解
"""
# 基础数据类型注解
var_1: int = 10
var_2: str = 'itheima'
var_3: bool = True

# 类对象类型注解
class Student:
    pass
stu: Student = Student()

# 基础容器类型注释
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {'itheima': 666}

# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, 'itheima', True)
my_dict: dict[str, int] = {'itheima': 666}






