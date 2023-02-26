# -*- coding = utf-8 -*-  
# @Time: 2023/2/20 01:10 
# @Author: Dylan 
# @File: input.py 
# @software: PyCharm
print("请告诉我你是谁")
name = input()
print("你是 %s" % name)

# 改进
name = input('请告诉我你是谁：')
print("我知道了，你是：%s" % name)

# 数据类型转换
name = input('请告诉我你的银行卡密码：')
print("我知道了，你的银行卡密码是：%d " % int(name))

# 欢迎登录小程序 练习
user_name = input("请输入你的姓名：")
user_type = input("你的用户类型是：")

print("您好，%s，您是尊贵的 %s" % (user_name, user_type))


