import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
def baidu(company, page):
    num = page * 10
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + company +'&pn=' + str(num)
    data = requests.get(url, headers=headers).text
    p_block = '<div class="result-op c-container xpath-log new-pmd(.*?)</div></div>'
    block = re.findall(p_block, data, re.S)

    title = []
    href = []
    time = []
    source = []

    for i in block:
        p_href = '<h3 class="news-title_1YtI1 "><a href="(.*?)"'
        href1 = re.findall(p_href, i, re.S)
        href.append(href1[0])

        p_title = '<h3 class="news-title_1YtI1 ">.*?aria-label="标题：(.*?)"'
        title.append(re.findall(p_title, i, re.S)[0])

        p_source = '<span class="c-color-gray" aria-label="新闻来源：(.*?)"'
        source.append(re.findall(p_source, data, re.S)[0])

        p_time = '<span class="c-color-gray2 c-font-normal c-gap-right-xsmall" aria-label="发布于：(.*?)"'
        time1 = re.findall(p_time, i, re.S)
        if time1 == []:
            time1 = ['无时间来源']
        time.append(time1[0])

    file1 = open('d:\\数据挖掘报告.txt', 'a', encoding='utf-8')
    file1.write(company + '第' + str(page)+'页'+'数据挖掘 Completed!' + '\n' + '\n')
    for i in range(len(title)):
        print(str(i+1) + '.' + title[i] + '' + source[i])
        file1.write(str(i + 1) + '.' + title[i] + '(' + time[i] + '-' + source[i] + ')' + '\n')

        print(href[i])
        file1.write(href[i] + '\n')
        file1.write('-------------------------' + '\n' + '\n')

companies = ['阿里巴巴', '京东', '拼多多']
for i in companies:
    for page in range(3):
        baidu(i, page)
        print(i + '第' + str(page+1)+'页' + '百度爬虫已完成')


