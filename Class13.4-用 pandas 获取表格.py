import pandas as pd
import requests

url = ''
response = requests.get(url)
table = pd.read_html(response.content, encoding='gbk')
print(table[0])

table1 = pd.DataFrame(table[0])
print(table)
table.to_excel('大宗交易表.xlsx')
