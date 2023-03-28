# -*- coding = utf-8 -*-  
# @Time: 2023/2/22 18:17 
# @Author: Dylan 
# @File: for 循环.py 
# @software: PyCharm

# 遍历字符串
name = "itheima"
for x in name:
    print(x)

# 案例：数一数有几个a
name = "itheima is a brand of itcast"
count = 0
for x in name:
    if x == 'a':
        count += 1
print(f'itheima is a brand of itcast 中共含有：{count}个字母a')

print(f'itheima is a brand of itcast 中共含有：{name.count("a")}个字母a')

# range

for x in range(5):
    print(x)

# 1- 100 中有几个偶数
count = 0
for x in range(1, 101):
    if x % 2 == 0:
        count += 1
print(f'1-100中有{count}个偶数')

# 坚持表白100天
# 每天送10朵花
i = 0
for i in range(1,101):
    print(f"今天是表白的第{i}天")
    print()
    for j in range(1,11):
        print(f'给小美送{j}花')
        print()

# for 循环打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i} = {i * j}', end='\t')
    print()

# continue
# 中断本次循环，直接进行下一次循环
for i in range(1, 6):
    print('语句1')
    continue
    print('语句2')

# break:整个循环结束
for i in range(1,101):
    print('语句1')
    break
print("语句2")

# 发工资需求

# Method 1
import random
j = 1
salary_balance = 10000
for i in range(1, 21):
    num = random.randint(1, 10)
    if (num >= 5) and (salary_balance - j * 1000) >= 0:
        print(f"员工{i}，发放工资{1000}元，账户余额还剩余{salary_balance - j * 1000}元")
        j += 1
    elif (num < 5) and (salary_balance - j * 1000) >= 0:
        print(f"员工{i}，绩效分{num}，不发工资，下一位")

    else:
        break

print("工资发完了，下个月领取吧")

# Method 2
money = 10000
for i in range(1, 21):
    num = random.randint(1,10)
    if num < 5:
        print(f"员工{i}，绩效分{num}，不发工资，下一位")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}，发放工资{1000}元，账户余额还剩余{money}元")
    else:
        print("工资发完了，下个月领取吧")
        break




