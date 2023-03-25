# -*- coding = utf-8 -*-  
# @Time: 2023/3/19 18:52 
# @Author: Dylan 
# @File: 文件操作.py 
# @software: PyCharm


# open
f = open("./测试.txt", mode='r', encoding="UTF-8")
print(type(f))

# 读取文件 - read()
print(f'读取10个字节的结果是:{f.read(10)}')
print(f'读取全部内容的结果是:{f.read()}, 类型是{type(f)}')

# 读取文件 - readlines() 读取全部内容， 数据类型是list
lines = f.readlines()
print(f'lines对象的类型是{type(lines)}，数据内容是{lines}')

# 读取文件 - readline() 一次读取一行
line = f.readline()
print(f'line对象的类型是{type(line)}, 数据内容是{line}')

# for 循环读取文件
for line in open("./测试.txt", mode='r', encoding="UTF-8"):
    print(f'每一行的数据是{line}')

# close() 关闭文件
f.close()

# with open()
with open("./测试.txt", 'r') as f:
    for line in f:
        print(f'每一行数据是:{line},类型是{type(line)}')


# 单词计数：
## 方法一
with open("./word.txt", mode='r', encoding='utf-8') as f:
    line = f.readlines()
    count = 0
    for sentence in line:
        for word in sentence.split():
            if word == 'itheima':
                count += 1

    print(count)



## 方法二
f = open("./word.txt", mode='r', encoding='utf-8')
content = f.read()
print(content.count('itheima'))

# 文件的写出
f = open('./test.txt', 'w', encoding='utf-8')
f.write('Hello World')  # 将内容写到内存中
f.flush()  # 将内容写到硬盘中
f.close()   # 内置flush功能


# 文件的追加
f = open('./test.txt', mode='a', encoding='utf-8')
f.write('黑马程序员，学python最佳选择')
f.close()

f.write('\n月薪过万')
f.flush()
f.close()






