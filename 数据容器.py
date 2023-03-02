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

# 列表循环
# 演示用while和for遍历列表中的所有元素
def list_while_func(mylist):
    """
    使用while循环遍历列表
    :return: None
    """
    index = 0
    while index < len(mylist):
        print(mylist[index])
        index += 1

mylist = ['传智教育', '黑马程序员', 'Python']

def list_for_func(mylist):
    """
    使用for循环遍历列表
    :param mylist:
    :return: None
    """

    for words in mylist:
        print(words)

# 练习：取出列表内的偶数
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for 循环

mylist1 = []
for num in mylist:
    if num % 2 == 0:
        mylist1.append(num)
print(f"通过for循环，从列表:{mylist}中取出偶数，组成新列表{mylist1}")

# list comprehension
print(f"通过for循环，从列表:{mylist}中取出偶数，组成新列表{[num for num in mylist if num % 2 == 0 ]}")

# while 循环
index = 0
mylist2 = []
while index < len(mylist):
    if mylist[index] % 2 == 0:
        mylist2.append(mylist[index])
    index += 1

print(f"通过while循环，从列表:{mylist}中取出偶数，组成新列表{mylist2}")


# ---------------------------------------------
# tuple 元组
# 不可以修改元素内容， 能存储各种元素

# 定义一个元组
t1 = (1,'Hello', True)
print(f't1的类型是{type(t1)},内容是{t1}')

t2 = ()
t3 = tuple()

print(f't2的类型是{type(t2)}\nt3的类型是{type(t3)}')

# 定义单个元素的元组
t4 = ('Hello') # 不是元组类型
t5 = ('Hello', )  # 是元组
print(f't4的类型是{type(t4)}\nt5的类型是{type(t5)}')

# 元组的嵌套
t6 = ((1, 2, 3), (4, 5, 6))
print(f't6的类型是{type(t6)}')

# 下标索引取出元组t6中的元素6
num = t6[1][2]
print(num)

# index
t7 = ('传智教育', '黑马程序员', 'Python')
print(f'黑马程序员的索引是{t7.index("黑马程序员")}')

# count
t8 = ('传智教育', '黑马程序员', '黑马程序员', '黑马程序员', '黑马程序员', 'Python')
print(f'黑马程序员的出现次数是{t8.count("黑马程序员")}')

# len
t9 = ('传智教育', '黑马程序员', '黑马程序员', '黑马程序员', '黑马程序员', 'Python')
print(f't8元组中的元素共有{len(t9)}个')

# while 遍历所有元组中的元素
index = 0
while index < len(t9):
    print(f'元组中的元素有{t9[index]}')
    index += 1

# for 遍历所有元组中的元素
for i in t9:
    print(i)

# 元组中的元素不可以修改， 元组中的列表中的元素可以修改
t10 = (1, 2, ['itcast','itheima'])
print(f'元组中是:{t10}')

t10[2][1] = '黑马程序员'
print(f'现在的元组是{t10}')

# 元组练习案例
t11 = ('周杰伦', 11, ['football', 'music'])

# 查询1其年龄所在的下标位置
t11.index(11)

# 查询学生姓名
t11[0]

# 删除学生爱好football
t11[2].pop(0)
print(f'现在元组是{t11}')

# 增加爱好coding到list内
t11[2].append('coding')
print(f'现在的元组是{t11}')


# ----------------------------------------------------
# 字符串
mystr = 'itheima and itcast'

# 通过下标索引取值
value = mystr[2]
value2 = mystr[-16]

print(f'从字符串{mystr}中取下标为2的值是{value},取小标为-16的值是{value2}')

# index
value = mystr.index('and')
print(f'字符串{mystr}中and的起始下标是{value}')

# replace(str1,str2)  str1： 为被替换的， str2：为新的
value = mystr.replace('it', '程序')
print(f'原字符串为{mystr}, 新字符串为{value}')

# split() ---返回的是一个列表
mystr = 'hello python itcast itheima'
value = mystr.split(' ')
print(f'原字符串{mystr}, 现在变为{value}, 类型是{type(value)}')

# strip
mystr = '  itheima and itcast  '
new_mystr = mystr.strip()  # 不传入参数，去除首尾空格
print(f'原字符串{mystr}，长度为{len(mystr)},现在变为{new_mystr},长度为{len(new_mystr)}')

mystr = '12itheima and itcast21'
new_mystr = mystr.strip('12')
print(f'原字符串{mystr},现在变为{new_mystr}')

# 统计字符串出现的次数
mystr = 'itheima and itcast'
count = mystr.count('it')
print(f'字符串{mystr}it出现的次数{count}')

# 统计字符串长度
len(mystr)

# 字符串练习，分割字符串
mystr = 'itheima itcast boxuegu'

# 统计有多少个it字符
value = mystr.count('it')
print(f'字符串{mystr}中有{value}个')

# 空格替换为|
value = mystr.replace(' ', '|')
print(f'字符串{mystr}中现在变成{value}')

# 按照|分割，得到列表
value1 = value.split('|')
print(f'字符串{mystr}中现在变成{value1}')

# 数据容器（切片）

# 对list进行切片，从1到4，步长为1
mylist = [0, 1, 2, 3, 4, 5, 6]
result = mylist[1:5]
print(f'结果1：{result}')

# 对tuple进行切片，从头到尾结束，步长为1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result = my_tuple[:]
print(f'结果2:{result}')

# 对str进行切片，从头到尾结束，步长为2
mystr = '01234567'
result = mystr[::2]
print(f'结果3:{result}')

# 对str进行切片，从头到尾结束，步长为-1
mystr = '01234567'
result = mystr[::-1]
print(f'结果4:{result}')

# 对str进行切片，从3到1结束，步长为-1
mystr = '01234567'
result = mystr[3:1:-1]
print(f'结果4:{result}')

# 对tuple进行切片，从头到尾结束，步长为-2
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result = my_tuple[::-2]
print(f'结果2:{result}')

# 序列的切片实践
mystr = "万过薪月, 员序程马黑来, nohtyP学"

# 得到 黑马程序员
result = mystr[::-1][10:15]
print(f'结果是{result}')

# 方法二得到黑马程序员
value = mystr.split(" ")[1][4::-1]
print(f'结果是{value}')

# 集合 无序，去重
my_set = {"传智教育", '黑马程序员', 'itheima', "传智教育", '黑马程序员', 'itheima', "传智教育", '黑马程序员', 'itheima'}
my_set_empty = set()
print(f'my_set的内容是{my_set}, 类型是{type(my_set)}')
print(f'my_set的内容是{my_set_empty}, 类型是{type(my_set_empty)}')

# 添加新元素
my_set.add('Python')
my_set.add('黑马程序员')
print(f'my_set的内容是{my_set}')

# 随机取出一个元素
element = my_set.pop()
print(f'取出的元素是{element}, 取出后的集合是{my_set}')

# 集合被清空了 clear
my_set = my_set.clear()
print(f'集合目前是{my_set}')

# 取差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)  # set1中有，set2中没有的元素
print(set1)
print(set2)
print(set3)

# difference_update()
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)  # 在集合1内删除和集合2内相同的元素, 集合2不变，集合1消除
print(set1)
print(set2)

# 2个集合合并为1个
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(set3)

# 统计集合中的元素数量
set1 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(f'集合内的元素数量为{len(set1)}')

# 集合遍历
# 集合不支持下标， 所以不能用while循环
# 可以用for 循环遍历
set1 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
for num in set1:
    print(num)

# 集合练习，信息去重
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']

my_set = set()
for word in my_list:
    my_set.add(word)
print(f'最终得到的集合为{my_set}')