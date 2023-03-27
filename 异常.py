# -*- coding = utf-8 -*-  
# @Time: 2023/3/25 20:31 
# @Author: Dylan 
# @File: 异常.py 
# @software: PyCharm

# 异常捕获
try:
    f = open('./abc.txt', 'r', encoding='utf-8')
except:
    print('File Not Found')
    f = open('./abc.txt', 'w', encoding='utf-8')
    f.write('hello')
    f.flush()
    f.close()

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print('出现变量未定义')
    print(e)

# 捕获多个异常
try:
    1/0
except(NameError, ZeroDivisionError) as e:
    print("出现变量未定义 或者 除以0的异常错误")

# 捕获多个异常
try:
    print(name)
except Exception as e:
    print('出现异常了')

# else() 如果没出现异常，需要执行的代码
try:
    f = open('./123.txt', 'r')
except Exception as e:
    print('出现异常')
else:
    print('好高兴，没有出现异常')


try:
    print('Hello')
except Exception as e:
    print('出现异常')
else:
    print('好高兴，没有出现异常')

# finally() 不管出没出现异常，都要执行的代码
try:
    f = open('./123.txt', 'r', encoding='utf-8')
except Exception as e:
    print('出现异常了')
    f = open('./123.txt', 'w', encoding='utf-8')
else:
    print('好高兴，没有异常')
finally:
    print('有没有异常，都要执行')
    f.close()


# 异常传递
def func1():
    print("func1开始执行")
    num = 1 / 0
    print('func1结束执行')

def func2():
    print('func2开始执行')
    func1()
    print('func2结束执行')

def main():
    try:
        func2()

    except Exception as e:
        print(f'出现异常了，异常信息是{e}')

main()



