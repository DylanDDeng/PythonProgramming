# -*- coding = utf-8 -*-  
# @Time: 2023/4/14 16:32 
# @Author: Dylan 
# @File: 03_类和对象.py 
# @software: PyCharm

class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(200, 300)

clock1 = Clock()
clock1.id = '02020'
clock1.price = 30
print(f'闹钟id是{clock1.id}, 价格是:{clock1.price}')
clock1.ring()

