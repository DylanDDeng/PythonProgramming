# -*- coding = utf-8 -*-  
# @Time: 2023/3/28 01:39 
# @Author: Dylan 
# @File: str_util.py 
# @software: PyCharm

def str_reverse(s: str):
    return s[::-1]


def substr(s: str, x: int, y: int):
    return s[x: y]


if __name__ == "__main__":
    print(str_reverse('黑马程序员'))
    print(substr('黑马程序员', 1, 3))
