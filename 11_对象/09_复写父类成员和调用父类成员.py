# -*- coding = utf-8 -*-  
# @Time: 2023/4/17 09:56 
# @Author: Dylan 
# @File: 09_复写父类成员和调用父类成员.py 
# @software: PyCharm

class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("使用5g网络进行通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "ITHEIMA"  # 复写父类的成员属性

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        # 方式1 调用父类成员变量
        # print(f"父类的厂商是:{Phone.producer}")
        # 调用父类的成员方法
        # Phone.call_by_5g(self)
        # 方式2
        print(f'父类的厂商是:{super().producer}')
        super().call_by_5g()
        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)








