import requests
import re

def replacer(stringlist, deletedlist):
    for i in range(len(stringlist)):
        for j in deletedlist:
            stringlist[i] = stringlist[i].replace(j, '')
    return stringlist

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

url = 'https://www.sogou.com/sogou?ie=utf8&interation=1728053249&interV=&&query=阿里巴巴'
res = requests.get(url, headers = headers, timeout = 10).text

p_source = '<p class="news-from text-lightgray">.*?<span>(.*?)</span>'

source = re.findall(p_source, res, re.S)
deletedlist = ['<em>', '</em>', '<!--red_beg-->', '<!--red_end-->']
replacer(source, deletedlist)
print(source)

p_date = '<p class="news-from text-lightgray">.*?</span><span>(.*?)</span>'
date = re.findall(p_date, res, re.S)
print(date)

p_title = '<h3 class="vr-title">.*?>(.*?)</a>'
title = re.findall(p_title, res, re.S)
print(title)

p_href = '<h3 class="vr-title">.*?href="(.*?)"'
href = re.findall(p_title, res, re.S)
print(href)

for i in range(len(title)):
    title[i] = re.sub('<.*?>', '', title[i])
    href[i] = 'https://www.sogou.com' + href[i]
    print(str(i+1) + '.' + title[i] + '-' + date[i] + '-' + source[i])
    print(href[i])

        
    
        
        
