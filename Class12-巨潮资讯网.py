from selenium import webdriver
import re
import time
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
url = 'http://www.cninfo.com.cm/new/fulltextSearch?notautosubmit=&keyword=' + '阿里巴巴'
browser.get(url)
time.sleep(3)
data = broswer.page_source
p_count = '<span class="total-box".*?>共(.*?)条'
count = re.findall(p_count, data)[0]

pages = int(int(count)/10)
datas = []
datas.append(data)
for i in range(2):
    broswer.find_element(By.XPATH, '//*[@id="fulltext-search"]/div[2]/div/div/div[3]/div[3]/div[2]/dic/button[2]').click()
    time.sleep(2)
    data = browser.page_source
    print(data)
    datas.append(data)
    time.sleep(1)
alldata = "".join(datas)
browser.quit()

p_title = '<span title="" class="r-title">(.*?)</span></span>'
p_href = '<a target="_blank" href="(.*?)"'
p_date = '<span class="time">(.*?)</span>'
title = re.findall(p_title, alldata, re.S)
href = re.findall(p_href, alldata)
date = re.findall(p_date, alldata, re.S)

for i in range(len(title)):
    title[i] = re.sub('<.*?>', '', title[i])
    href[i] = 'http://www.cninfo.com.cn' + href[i]
    href[i] = re.sub('amp;', '', href[i])
    date[i] = date[i].strip()
    date[i] = date[i].split(' ')[0]
    print(str(i + 1) + '.' + title[i] + ' - ' + date[i])
    print(href[i])
    
