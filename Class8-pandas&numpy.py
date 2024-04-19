# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

print(np.array([[1,2], [2,2], [3,3]])) # 排列数组
print(np.arange(1,10,0.5)) # 创建数组
print(np.random.randn(5))
print(np.random.randint(1,7,(3,3))) # 创建随机数

import pandas as pd
s1 = pd.Series(['丁一', '王二', '张三'])

# 1. 通过列表创建 dataframe
a = pd.DataFrame([[1,2], [3,4], [5,6]])
print(a)
# 1. 通过列表创建 dataframe
a = pd.DataFrame([[1,2], [3,4], [5,6]], columns=['data', 'score'],index = ['A', 'B','C'])
print(a)

# 1. 通过列表创建 dataframe
a = pd.DataFrame()
date = [1,3,5]
score = [2,4,6]
a['date'] = date
a['score'] = score

# 2. 通过字典创建 dataframe
b = pd.DataFrame({'a':[1,3,5],'b':[2,4,6]},index = ['x','y','z'])
print(b)
b = pd.DataFrame.from_dict({'a':[1,3,5],'b':[2,4,6]},orient = "index")
print(b)

# 3. 通过二位数组创建
d = pd.DataFrame(np.arange(12).reshape(3,4),index=[1,2,3],columns=['A','B','C','D'])
print(d)

# 4. 修改索引
a = pd.DataFrame([[1,2],[3,4],[5,6]], columns=['date','score'], index=['A','B','C'])
a.index.name = '公司'

#a = a.set_index('日期') 
#a.set_index('日期', inplace = True)

a.rename(index={'A':'万科','B':'阿里','C':'百度'}, columns={'date':'日期','score':'分数'}, inplace = True)
a = a.reset_index()


# 6.2.2 Excel 等文件的读取和写入
data1 = pd.read_excel(r'C:\Users\Administrator\Desktop\data.xlsx', sheet_name = 0, encoding = 'utf8')
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\data.csv', delimiter = ',', encoding = 'utf-8')
print(data1)

# 写入
data = pd.DataFrame([[1,2], [3,4],[5,6]], columns = ['A列', 'B列'])
data.to_excel(r'C:\Users\Administrator\Desktop\演示.xlsx', columns=['A列'], index = False)
data.to_csv(r'C:\Users\Administrator\Desktop\演示.csv', index = False, encoding = 'utf_8_sig')

# 6.2.3 数据读取与筛选
data = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], index = ['r1','r2','r3'], columns=['c1','c2','c3'])
data = pd.DataFrame(np.arange(1,10).reshape(3,3), index = ['r1','r2','r3'], columns=['c1','c2','c3'])

# 按照列来选取数据
a = data['c1']
b = data[['c1']] # 返回表头
c = data[['c1', 'c3']] # 选取多列数据

# 按照行来选取数据
a = data[1:3]
b = data.iloc[1:3] 
d = data.loc[['r2', 'r3']]

data.head() # 默认输出表格的前五行
data.head(2) # 提取表格的前两行

# 按照区块来选取
f = data.ix[0:2, ['c1','c3']]
print(f)

# 数据运算
data['c4'] = data['c3'] - data['c1']
data.head()

# 数据筛选
a = data[data['c1'] > 1]
print(a)

# 数据排序
b = data[(data['c1'] > 1) & (data['c2'] < 8)]
a = data.sort_values(by = 'c2', ascending = False)

# 数据排序
a = a.sort_index()

# 数据删除
a = data.drop(columns = 'c1')
b = data.drop(columns = ['c1','c3'])
c = data.drop(index = ['r1','r3'])

# 数据表拼接
import pandas as pd
df1 = pd.DataFrame({'公司':['万科','阿里','百度'], '分数':[90,95,85]})
df2 = pd.DataFrame({'公司':['万科','阿里','百度'], '股价':[20,180,30]})
df3 = pd.merge(df1, df2)
df3 = pd.merge(df1, df2, how = 'outer') # 外连接
df3 = pd.merge(df1, df2, how = 'left') # 左连接
df3 = pd.merge(df1, df2, left_index = True, right_index = True)
df3 = pd.concat([df1,df2],axis = 0) # 按照行方向进行全连接
df3 = pd.concat([df1,df2],axis = 1) # 按照列方向进行全连接
df3 = df1.append(df2) # 简化全连接
df3 = df1.append({'公司':'腾讯','分数':'90'}, ignore_index = True)




