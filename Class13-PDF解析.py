# 1. 解析第一页的文本信息
import pdfplumber
pdf = pdfplumber.open(r'C:\公司A理财公告.PDF')
pages = pdf.pages
page = pages[0]
text = page.extract_text()
print(text)
pdf.close()

# 2. 解析全部页数的文本信息
import pdfplumber
pdf = pdfplumber.open(r'C:\公司A理财公告.PDF')
pages = pdf.pages
text_all = []
for page in pages:
    text = page.extract_text()
    text_all.append(text)
text_all = ''.join(text_all)
print(text_all)
pdf.close()

# 3. 解析表格内容
import pdfplumber
import pandas as pd
pdf = pdfplumber.open(r'C:\公司A理财公告.PDF')
pages = pdf.pages
page = pages[3]
tables = page.extract_tables()
table = tables[0]
for i in range(len(table)):
    for j in range(len(table[i])):
        table[i][j] = table[i][j].replace('\n', '')
pd.set_option('display.max_columns', None)
df = pd.DataFrame(table[1:], columns=table[0])
print(df)
pdf.close()
