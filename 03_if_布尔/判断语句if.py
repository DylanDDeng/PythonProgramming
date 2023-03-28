# -*- coding = utf-8 -*-  
# @Time: 2023/2/20 20:49 
# @Author: Dylan 
# @File: 判断语句if.py 
# @software: PyCharm

# if语句的基本使用
age = 30
if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")

print("时间过得真快呀")

# 是否成年人判断小练习
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
age = int(input("请输入你的年龄："))
if age >= 18:
    print("您已成年，游玩需要补票10元")
print("祝您游玩愉快")

# if - else
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
age = int(input("请输入你的年龄："))
if age >= 18:
    print("您已成年，游玩需要补票10元")
else:
    print("您未成年，可以免费游玩")
print("祝您游玩愉快")

# 我要买票吗，小练习
print("欢迎来到黑马动物园")
height = int(input("请输入你的身高（cm): "))
if height > 120:
    print("您的身高超出120cm，游玩需要购票10元")
else:
    print("您的身高未超出120cm,可以免费游玩")

print('祝您游玩愉快')

# if - elif - else 多条件判断
height = int(input("请输入你的身高："))
vip_level = int(input("请输入你的VIP等级（1-5): "))
day = int(input("请告诉我今天是几号："))
if height < 120:
    print("身高小于120，可以免费")
elif vip_level > 3:
    print("vip级别大于3，可以免费")
elif day == 1:
    print("今天是1号，可以免费")
else:
    print("不好意思，条件都不满足，需要买票10元")

# 猜心里数字
num = 5
if int(input("请猜一个数字：")) == num:
    print("恭喜你，猜对了")
elif int(input("请再猜一次：")) == num:
    print('猜对了')
elif int(input("最后一次机会：")) == num:
    print("恭喜，最后一次机会，猜对了")
else:
    print("Sorry, 猜错了")

# if语句的嵌套使用
if int(input("请输入你的身高：")) > 120 :
    print('身高超出限制，不可以免费')
    print('但是vip级别大于3，可以免费')

    if int(input("请输入你的vip等级：")) >3:
        print("恭喜你，vip级别达标，可以免费")
    else:
        print("对不起，不可以免费")

else:
    print("可以免费游玩")

# 领取礼物的条件
if (18 <= int(input("请输入你的年龄：")) < 30) and (int(input('请输入入职时间：')) > 2 or (int(input("请输入你的vip级别")) > 3)):
    print("可以领取礼物")
else:
    print("不可以领取礼物")

# 猜数字练习
import random
num = random.randint(1,10)

guess_num = int(input('请输入你猜测的数字: '))
if num == guess_num:
    print("恭喜你，猜对了")

else:
    if num > guess_num:
        print('不对，猜小了')
    elif num < guess_num:
        print('不对，猜大了')

# 猜数字练习 - 3次
i = 0
num = random.randint(1,10)
while i < 3:
    guess_num = int(input('请输入你猜测的数字: '))
    if num == guess_num:
        print("恭喜你，猜对了")
        break
    else:
        if num > guess_num:
            print('不对，猜小了')
        elif num < guess_num:
            print('不对，猜大了')
    i += 1


num = random.randint(1,10)

for i in range(0,3):
    guess_num = int(input("请输入你猜测的数字："))

    if num == guess_num:
        print("恭喜你，猜对了")
        break
    else:
        if num > guess_num:
            print("不对，猜小了")
        else:
            print("不对，猜大了")
    i += 1







