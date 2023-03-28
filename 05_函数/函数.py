# -*- coding = utf-8 -*-  
# @Time: 2023/2/24 11:12 
# @Author: Dylan 
# @File: 函数.py
# @software: PyCharm

# 统计字符串长度，不使用内置函数len()
def cal_len(x: str) -> str:
    cnt = 0
    for letter in x:
        cnt += 1
    return cnt

# 自动查核酸
def show():
    print("欢迎来到黑马程序员 \n请出示您的健康码和72小时核酸证明 " )

show()

# 升级版自动查核酸
def temp_check(x: int) -> str:
    print('欢迎来到黑马程序员！请出示您的健康码及24小时核酸证明， 并配合测量体温')
    if x <= 37.5:
        print(f'体温测量中，您的体温是{x}度，体温正常请进')
    else:
        print(f'体温测量中，您的体温是{x}度，需要隔离')

# 无return语句的返回值
def say_hi():
    print("你好呀")

result = say_hi()

print(f'无返回值的函数，返回内容是{result}')
print(f'无返回值的函数，返回类型是{type(result)}')

# 主动返回None值
def say_hi2():
    print("你好呀")
    return None

result2 = say_hi2()

print(f'无返回值的函数，返回内容是{result2}')
print(f'无返回值的函数，返回类型是{type(result2)}')

# None 的应用场景
def check_age(age: int):
    if age > 18:
        return 'success'
    else:
        return None

result = check_age(16)

if not result:
    print('未成年，不准进入')

# 函数综合案例
money = 5000000
name = input('请输入你的名字：')

# 主菜单函数
def main_menu():
    print('--------------------------主菜单-------------------------')
    print(f'{name} 你好，欢迎来到黑马银行ATM,请选择操作')
    print('查询余额 \t【输入1】')
    print('存款 \t \t【输入2】')
    print('取款 \t \t【输入3】')
    print('退出 \t \t 【输入4】')

    return int(input('请输入您的选择：'))

# 存取款函数
# 取款函数
def get_money(cash):
    global money, name
    money -= cash
    print('--------------------------取款-------------------------')
    print(f'{name}您好，您取款{cash}成功')

    account_balance(show_header=False)


# 存款函数
def deposit(cash):
    global money, name
    money += cash
    print('--------------------------存款-------------------------')
    print(f'{name}您好，您存款{cash}元成功')

    account_balance(show_header=False)

# 查询余额函数
def account_balance(show_header):
    global name, money

    if show_header:
        print('--------------------------查询余额-------------------------')
    print(f'{name}，您好，您的余额剩余{money}元')

while True:
    choice1 = main_menu()
    if choice1 == 1:
        balance = account_balance(show_header=True)
    elif choice1 == 2:
        num = int(input('你想要存多少钱？ 请输入：'))
        deposit_money = deposit(num)
    elif choice1 == 3:
        num = int(input('你想要取走多少钱？ 请输入：'))
        getmoney = get_money(num)
    else:
        print('程序已退出')
        break







