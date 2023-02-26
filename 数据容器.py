# -*- coding = utf-8 -*-  
# @Time: 2023/2/26 00:36 
# @Author: Dylan 
# @File: 数据容器.py 
# @software: PyCharm

# 定义一个列表 list
my_list = ["itheima", "itcast",'python']
print(my_list)
print(type(my_list))

my_list = ['itheima', '666', True]
print(my_list)
print(type(my_list))

# 定义一个嵌套列表
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list)
print(type(my_list))


# 列表中的下标索引
my_list = ['Tom', 'Lily', 'Rose']
print(my_list[0])
print(my_list[1])
print(my_list[2])

print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# 取出嵌套列表中的元素
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[1][1])

# 列表的常用方法
mylist = ['itcast', 'itheima', 'python']

# 查找某元素在列表内部的下表索引
mylist.index('itheima')

# 修改特定下标索引的值
mylist[0] = "传智教育"
print(f'列表修改元素后为：{mylist}')

# insert
mylist.insert(1,'best')
print(f'列表插入元素后为：{mylist}')

# append()
mylist.append("黑马程序员")
print(f'列表追加元素后为：{mylist}')

# extend()
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f"列表追加一批元素后为：{mylist}")

# 删除指定下标索引的元素（2种方式）

# del
mylist = ['itcast', 'itheima', 'python']
del mylist[2]
print(f'列表删除后的元素为：{mylist}')


# pop
mylist = ['itcast', 'itheima', 'python']
element = mylist.pop(2)
print(f'通过pop方式取出元素后列表内容：{mylist}, 取出的元素为{element}')

# 删除某元素在列表中的第一个匹配项
mylist = ['itcast', 'itheima', 'itcast', 'itheima', 'python']
mylist.remove('itheima')
print(f'通过remove方法移除元素后，列表的结果是{mylist}')

# clear() 清空列表
mylist.clear()
print(f'通过clear方法后，列表的结果是{mylist}')

# count() 统计某元素在列表中的数量
mylist = ['itcast', 'itheima', 'itcast', 'itheima', 'python']
num = mylist.count('itheima')
print(f'列表中itheima一共有{num}个')

# len()
len(mylist)

# 列表常用功能练习

# 定义这个列表，并用变量接收他
mylist = [21, 25, 21, 23, 22, 20]

# 追加一个数字31，到列表的尾部
mylist.append(31)
print(f'现在列表为{mylist}')

# 追加一个新列表[29,33,30] 到列表的尾部
mylist.extend([29, 33, 30])
print(f'现在的列表为{mylist}')

# 取出第一个元素
mylist[0]

# 取出最后一个元素
mylist[-1]

# 查找元素31，在列表中的下标位置
mylist.index(31)



#