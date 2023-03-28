# -*- coding = utf-8 -*-
# @Time: 2023/2/15 03:51 
# @Author: Dylan 
# @File: 字符串格式化.py 
# @software: PyCharm
name = "黑马程序员"
message = "学IT来：%s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期，平均工资：%s" % (class_num, avg_salary)
print(message)

#
'Python大数据学科，北京{}期，平均工资：{}'.format(57, 16781)

name = "传智播客"
set_up_year = 2006
stock_price = 19.99
message = "我是：%s， 我成立于：%d, 我今天的估价是：%f" % (name, set_up_year, stock_price)

print(message)

# 控制精度和位置
num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print('数字11.345宽度限制7，小数精度2，结果是：%7.2f' % num2)
print('数字11.345宽度不限制，小数精度2，结果是：%.2f' % num2)

# 另一种快速格式化的方法
name = '传智博客'
set_up_year = 2006
stock_price = 19.99

print(f'我是{name}, 我成立于{set_up_year}, 我今天的股价是{stock_price}')  # 无法对精度做控制

# 表达式格式化
print("1 * 1 的结果是：%d" % (1*1))
print(f"1 * 1 的结果是:{1*1}")
print("字符串在Python中的类型名是：%s" % type('1*1'))




