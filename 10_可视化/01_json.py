# -*- coding = utf-8 -*-  
# @Time: 2023/3/28 21:06 
# @Author: Dylan 
# @File: json.py 
# @software: PyCharm

"""
演示json数据和Python字典的相互转化
"""
import json

# 列表转json
data = [{'name': '张大三', "age": 11}, {'name': '李大四', "age": 15}, {'name': '王大锤', "age": 18}]

json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 字典转json
d = {'name': '周杰伦', 'addr': '台北'}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

# json 转字符串
s = '[{"name": "张大三", "age": 11}, {"name": "李大四", "age": 15}, {"name": "王大锤", "age": 18}]'
l = json.loads(s)
print(type(l))
print(l)

# json 转字典
s = '{"name": "周杰伦", "addr": "台北"}'
l = json.loads(s)
print(type(l))
print(l)