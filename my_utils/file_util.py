# -*- coding = utf-8 -*-  
# @Time: 2023/3/28 01:46 
# @Author: Dylan 
# @File: file_util.py 
# @software: PyCharm

def print_file_info(file_name: str):
    f = None
    try:
        f = open(file_name, 'r', encoding='UTF-8')
        content = f.read()
        print("文件的内容是:")
        print(content)
    except Exception as e:
        print(f'有问题，文件不存在,原因是:{e}')
    finally:
        if f is not None:
            f.close()


def append_to_file(filename: str,  data: str):
    f1 = open(filename, 'a', encoding='UTF-8')
    f1.write(data)
    f1.write('\n')
    f1.close()




