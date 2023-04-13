# -*- coding = utf-8 -*-  
# @Time: 2023/4/13 15:34 
# @Author: Dylan 
# @File: 02_pyecharts使用.py 
# @software: PyCharm
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 折线图使用
line = Line()
line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [20, 30, 10])
# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
# 渲染
line.render()



