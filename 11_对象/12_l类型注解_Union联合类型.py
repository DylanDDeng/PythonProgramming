# -*- coding = utf-8 -*-  
# @Time: 2023/4/26 17:28 
# @Author: Dylan 
# @File: 12_l类型注解_Union联合类型.py 
# @software: PyCharm

"""
通过Union联合类型注释
"""
from typing import Union
my_lsit: list[Union[int, str]] = [1, 2, "itheima", 'itcast']

def func(data: Union[int, str])->Union[int, str]:
    pass
