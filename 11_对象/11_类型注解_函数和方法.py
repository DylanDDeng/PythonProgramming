# -*- coding = utf-8 -*-  
# @Time: 2023/4/26 17:20 
# @Author: Dylan 
# @File: 11_类型注解_函数和方法.py
# @software: PyCharm

# 对形参进行类型注解
def add(x: int, y: int):
    return x + y

# 对返回值进行类型注解
def func(data: list) -> list:
    return data
