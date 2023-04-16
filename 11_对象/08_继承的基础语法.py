# -*- coding = utf-8 -*-  
# @Time: 2023/4/16 22:02 
# @Author: Dylan 
# @File: 08_继承的基础语法.py 
# @software: PyCharm

"""
演示面向对象，继承的基础语法
"""

# 单继承
class Phone:
    IMEI = None  # 序列号
    producer = "HM"  # 厂商

    def call_by_4g(self):
        print("4g通话")

class Phone2023(Phone):
    face_id = "100001"  # 面部识别

    def call_by_5g(self):
        print("2023年新功能，5g通话")

phone = Phone2023()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

# 多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")
class RemoteControl:
    rc_type = "红外遥控"
    def control(self):
        print("红外遥控开启了")

class MyPhone(Phone, NFCReader, RemoteControl):
     pass

phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()