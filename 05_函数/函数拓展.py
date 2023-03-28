# -*- coding = utf-8 -*-  
# @Time: 2023/3/9 21:21 
# @Author: Dylan 
# @File: 函数拓展.py 
# @software: PyCharm

# 函数的多返回值
def test_return():
    return 1, 2, 3

# 类型并不受限


x, y, z = test_return()
print(x)
print(y)
print(z)

# 函数的多种参数使用形式

def user_info(name, age, gender):
    print(f'姓名是{name}, 年龄是{age}, 性别是{gender}')

# 位置参数 - 默认的使用形式

user_info('小明', 20, "男")

# 关键字参数
user_info(name='小明', age=20, gender="男")
user_info(age=20, name='小明', gender="男")
user_info('小明', age=20, gender='男')

def user_info(name, age, gender='男'):
    print(f'姓名是{name}, 年龄是{age}, 性别是{gender}')

user_info(name='小明', age=20)
user_info(name='小明', age=20, gender='女')

# 不定长参数
# 位置不定长， * 号

def user_info(*args):
    print(f"args的参数类型是:{type(args)}, 内容是:{args}")

user_info(1, 2, 3, '小明', '男孩')

def user_info(**kwargs):  # 关键字不定长
    print(f"kwargs的参数类型是:{type(kwargs)}, 内容是:{kwargs}")

user_info(name='小王', age=11, gender='男孩', addr='北京')

# 函数作为参数传递
def compute(x, y):
    return x+y

def test_func(compute):
    result = compute(1, 2)
    return result

test_func(compute)

# lambda 函数
def test_func(compute):
    result = compute(1, 2)
    return result

test_func(lambda x, y: x+y)




