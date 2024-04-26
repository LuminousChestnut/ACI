# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

data = pd.read_excel(r'C:\Users\Administrator\Desktop\data.xlsx', sheet_name = 0)

# a = data.drop(columns = 'c1')
# b = data.drop(columns = ['c1', 'c3'])
# c = data.drop(index = ['r1', 'r3'])

df1 = pd.DataFrame({'公司':['万科','阿里','百度'], '分数':[90,95,85]})
df2 = pd.DataFrame({'公司':['万科','阿里','京东'], '股价':[20,180,30]})
df3 = pd.merge(df1, df2)


df1 = pd.DataFrame({'company':['阿里巴巴','阿里巴巴','阿里巴巴'], 'year':[2021,2022,2023], 'score':[100,90,80]})
df2 = pd.DataFrame({'company':['京东','京东','京东'], 'year':[2021,2022,2023], 'score':[70,60,50]})

   
df3 = pd.DataFrame({'year':[2021,2022,2023], 'gdp':[300,200,100]})



data1 = pd.merge(df1, df3, how = 'outer')
data2 = pd.merge(df2, df3, how = 'outer')

data2 = pd.merge(data1, data2, how = 'outer')
print(data2)


data.to_excel('2.xlsx')
df1.to_excel('df1.xlsx')
df2.to_excel('df2.xlsx')
