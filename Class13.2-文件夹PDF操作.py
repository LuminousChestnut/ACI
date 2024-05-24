import os
import pdfplumber

# 1. 遍历文件夹中所有的 PDF 文件
file_dir = r'C:\\演示文件夹'
file_list = []
for files in os.walk(file_dir):
    for file in files[2]:
        if os.path.splitext(file)[1] == '.pdf' or os.path.splitext(file)[1] == '.PDF':
            file_list.append(file_dir + '\\' + file)
print(file_list)

# 2. 文本解析和内容筛选
pdf_all = []
for i in range(len(file_list)):
    pdf = pdfplumber.open(file_list[i])
    pages = pdf.pages
    text_all = []
    for page in pages:
        text = page.extract_text()
        text_all.append(text)
    text_all = ''.join(text_all)
    pdf.close()
    # 通过正文进行筛选
    if ('自有' in text_all) or ('议案' in text_all) or ('现金管理' in text_all):
        pdf_all.append(file_list[i])
print(pdf_all)
# 3. 筛选后文件的移动
for pdf_i in pdf_all:
    newpath = 'C:\\筛选后的文件夹\\' + pdf_i.split('\\')[-1]
    os.rename(pdf_i, newpath)
print('PDF 文本解析及筛选完毕')
