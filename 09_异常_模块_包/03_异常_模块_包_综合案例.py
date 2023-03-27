# -*- coding = utf-8 -*-  
# @Time: 2023/3/28 01:38 
# @Author: Dylan 
# @File: 03_异常_模块_包_综合案例.py 
# @software: PyCharm

"""
这是练习案例
"""

from my_utils import file_util
from my_utils import str_util

print(str_util.str_reverse('abcde'))
str_util.substr('abcdefgh', 1, 4)

file_util.print_file_info('123.txt')
file_util.append_to_file('./123.txt', '不想')

