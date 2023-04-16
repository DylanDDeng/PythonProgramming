# -*- coding = utf-8 -*-  
# @Time: 2023/4/16 18:13 
# @Author: Dylan 
# @File: 06_封装_课后练习.py 
# @software: PyCharm

class Phone:
    _is_5g_enable: bool = False

    def _check_5g(self):
        if self._is_5g_enable is True:
            print("5g开启")
        else:
            print("5g关闭，打印4g网络")

    def call_by_5g(self):
        self._check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
