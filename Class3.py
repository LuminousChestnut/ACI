'''
1. strip()
清除字符串左右的空格
---

2.re.sub(pattern, repl, string, count=0, flags=0)
参数：

pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''


import requests
import re

url = 'http://www.baidu.com/s?ie=UTF-8&wd=%E5%BE%B7%E5%85%8B%E8%90%A8%E6%96%AF'
header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'

requester = requests.get(url, header).text

list = re.findall('href="(.*?)"', requester)
# print(requester)

list[1] = '<em>' + list[1] + '</em>'
print(list)

def replacer(deletelist, stringlist):
    for string in range(len(stringlist)):
        for delete in range(len(deletelist)):
            stringlist[string] = stringlist[string].strip()
            stringlist[string] = re.sub(deletelist[delete], '', stringlist[string])
    return stringlist

#
# for j in range(len(list)):
#     list[j] = list[j].strip()
#     list[j] = re.sub('<em>', '', list[j])
#     list[j] = re.sub('</em>', '', list[j])

replacer(['<em>', '</em>'], list)

print(list)
