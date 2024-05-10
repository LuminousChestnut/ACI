# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
x = [1, 2, 3]
y = [1, 2, 3]
# 折线图
plt.plot(x, y, color = 'red', linewidth = 3, linestyle = '--')
# 柱状图
plt.bar([1,2,3,4,5],[1,23,123,3,12312])
# 饼状图
plt.pie([1,2,3])
# 文字说明
plt.title('标题')
plt.xlabel('X轴')
plt.ylabel('Y轴')
# 图例
plt.legend('abcd', loc = 'upper left')
plt.legend('abcd', loc = 'lower right')
# 设置双坐标轴 有点像 hold on
plt.twinx()
# 设置图片大小
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


x1 = np.array([1, 2, 3])
y1 = 2 * x1 + 2 * x1 * x1
plt.plot(x1 ,y1)
plt.twinx()
plt.scatter([1,2],[13,12])
plt.show()
