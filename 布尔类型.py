# -*- coding = utf-8 -*-  
# @Time: 2023/2/20 17:04 
# @Author: Dylan 
# @File: 布尔类型.py 
# @software: PyCharm

result = "itma" == 'itca'
print(f"result 的结果是 {result}, 类型是{type(result)}")

# 定义变量，存储bool变量类型数据
bool_1 = True
bool_2 = False
print(f"bool_1 变量的内容是{bool_1}, 类型是{type(bool_1)}")
print(f"bool_1 变量的内容是{bool_2}, 类型是{type(bool_2)}")

# 比较运算符的使用
# ==
num1 = 10
num2 = 10
print(f'10 == 10 的结果是：{num1 ==num2} ')

# !=
num1 = 10
num2 = 15
print(f'10 != 15的结果是：{num1 != num2}')
print(f'10 == 15的结果是：{num1 == num2}')

# 字符串比较
name1 = 'itcast'
name2 = 'itpro'
print(f'itcast != itpro 的结果是：{name1 != name2}')

# 大于 and 大于等于
num1 = 10
num2 = 5
print(f'num1 > num2 的结果是：{num1 > num2}')

num1 = 10
num2 = 10
print(f'num1 >= num2 的结果是：{num1 >= num2}')

num1 = 11
num2 = 4
print(f'num1 <= num2 的结果是:{num1 <= num2}')
print(f'num1 >= num2 的结果是:{num1 >= num2}')