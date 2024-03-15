import requests
import re

url = 'http://www.baidu.com/s?ie=UTF-8&wd=%E5%BE%B7%E5%85%8B%E8%90%A8%E6%96%AF'
header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'

requester = requests.get(url, header).text

list = re.findall('href="(.*?)"', requester)
# print(requester)
print(list)

