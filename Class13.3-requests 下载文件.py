# 1. 下载 csv 数据文件
import requests
url = ''
res = requests.get(url)
file = open('', 'wb')
file.write(res.content)
file.close()
print('世界银行项目表.csv 下载完毕')

# 2. 通过 requests 库下载图片
import requests
url = ''
res = requests.get(url)
file = open('图片.jpg', 'wb')
file.write(res.content)
file.close()
print('图片.jpg 下载完毕，并保存在代码所在的文件夹')
