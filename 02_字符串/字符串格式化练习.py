# -*- coding = utf-8 -*-  
# @Time: 2023/2/20 00:37 
# @Author: Dylan 
# @File: 字符串格式化练习.py 
# @software: PyCharm

def cal_stock_price(name, stock_price, stock_code, stock_price_daily_growth_factor,
                    growth_days):
    """
    :param name: 公司名
    :param stock_price: 当前股价
    :param stock_code: 股票代码
    :param stock_price_daily_growth_factor: 股票每日增长系数
    :param growth_days:增长天数
    :return: stock_price_after_days 几天后的股价
    """
    stock_price_after_days = stock_price * (stock_price_daily_growth_factor ** growth_days)

    print(f"公司：{name}, 股票代码:{stock_code},当前股价：{stock_price}")
    print("每日增长系数:%.1f, 经过 %d 天后的增长，股价达到了 %.2f" % (stock_price_daily_growth_factor, growth_days, stock_price_after_days))


cal_stock_price(name = "传智播客",
                stock_price=19.99,
                stock_code="003032",
                stock_price_daily_growth_factor=1.2,
                growth_days=7)
