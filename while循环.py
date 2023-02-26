# -*- coding = utf-8 -*-  
# @Time: 2023/2/22 10:47 
# @Author: Dylan 
# @File: while循环.py 
# @software: PyCharm

# while 循环
i = 0
while i < 10:
    print("小美，你好")
    i += 1


# 1+... +100 的和
sum: int = 0
i: int = 1
while i < 101:
    sum += i
    i += 1
print(f'1-100的累加和是:{sum}')

# while 循环猜数字
import random
num = random.randint(1, 100)
i = 1
while 3 < 5:
    guess_num = int(input("请输入你猜的数字："))
    if guess_num == num:
        print("恭喜你，猜对了")
        print(f"猜了{i}次就猜对了，真好")
        break  # 或者可以写 3>5
    elif guess_num > num:
        print("对不起，猜大了")
    else:
        print("对不起，猜小了")

    i += 1

# while 嵌套
i = 1
while i <= 100:
    print(f"今天是第{i}天，准备表白...")

    # 内层循环的控制变量
    j = 1
    while j <= 10:
        print(f"送给小美第{j}只玫瑰花")
        j += 1

    print("小美，喜欢你")
    i += 1

print(f"坚持到第{i-1}天，表白成功")

# 打印九九乘法表
i: int = 1
while i <= 9:  # 控制每一行的输出
    j: int = 1
    while j <=i: # 控制每一行输出的内容
        print(f'{i} * {j} = {i * j}', end='\t')
        j += 1
    i += 1
    print()  # 换行






