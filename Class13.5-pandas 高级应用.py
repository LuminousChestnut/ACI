import pandas as pd
data = pd.DataFrame(['c1',2])
# 重复值及缺失值处理
data[data.duplicated()]
# 统计重复行的数量
data.duplicated().sum()
# 按照列去重
data = data.drop_duplicates('c1')
# 缺失值处理
data[data['c1'].isnull()]
print(isinstance(data))
# groupby 数据分组汇总
means = data.groupby('分析师')[['30天收益率']].mean()
# apply 函数进行批处理
def y(x):
    if x > 0:
        return x + 100
    else:
        return x - 100
data['c1'].apply(y)
# 装饰器
def funA(desA):
    print("A")

def funB(desB):
    print("B")

@funB
@funA
def funC(desC):
    print("C")

# Lambda 函数
print(lambda x: x+1)
