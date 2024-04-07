import requests
import re

str = 'abbaabaabba'


print(re.findall('a.b', str))
print(re.findall('a.*b', str))
print(re.findall('a.*?b', str))
print(re.findall('a(.*?)b', str))


webdict = {}

def baidu(company):
    url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&ie=utf-8&wd=' + company
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    requester = requests.get(url, headers=header).text
    webdict[company]=requester

companys = ['华能信托', '阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
for i in companys:
    baidu(i)
    print(i + '百度新闻爬取成功')

print(webdict['百度集团'])

baidutext = webdict['百度集团']

print(re.findall('<h3 class=".*?</a>.*?</h3>',baidutext))
