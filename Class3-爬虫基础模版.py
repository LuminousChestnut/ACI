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

url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&ie=utf-8&word=阿里巴巴'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

requester = requests.get(url, headers=header).text

# print(requester)
p_block = '<div class="result(.*?)</div></div>'
blocklist = re.findall(p_block, requester, re.S)
print(blocklist)

href = []
title = []
time = []
source = []

for i in blocklist:
    p_href = '<h3 class="news-title_1YtI1 "><a href="(.*?)"'
    href1 = re.findall(p_href, i, re.S)
    href.append(href1[0])
    p_time = '<span class="c-color-gray2">(.*?)'
    time1 = re.findall(p_time, i, re.S)
    if time1 == []:
        time1 = ['无时间来源']
    time.append(time1[0])
    p_title = '<h3 class="news-title_1YtI1 ">.*?aria-label="标题：(.*?)"'
    title1 = re.findall(p_title, i, re.S)
    title.append(title1[0])
    p_source = '<span class="c-color-gray" aria-label="新闻来源：(.*?)"'
    source1 = re.findall(p_source, data, re.S)
    source.append(source1[0])

for i in range(len(href)):
    print(str(i+1)+'.'+title[i]+''+source[i])
    print(href[i])



def replacer(deletelist, stringlist):
    for string in range(len(stringlist)):
        for delete in range(len(deletelist)):
            stringlist[string] = stringlist[string].strip()
            stringlist[string] = re.sub(deletelist[delete], '', stringlist[string])
    return stringlist

# for j in range(len(list)):
#     list[j] = list[j].strip()
#     list[j] = re.sub('<em>', '', list[j])
#     list[j] = re.sub('</em>', '', list[j])

# replacer(['<em>', '</em>'], list)
#
# print(list)

