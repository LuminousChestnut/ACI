from selenium import webdriver
import re
import time
from selenium.webdriver.common.by import By
import requests
import os

browser = webdriver.Chrome()
url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=' + '阿里巴巴'
browser.get(url)
time.sleep(3)
data = browser.page_source
p_count = '<span class="total-box".*?>共(.*?)条'
count = re.findall(p_count, data)[0]

pages = int(int(count)/10)
datas = []
datas.append(data)
for i in range(30):
    browser.find_element(By.XPATH, '//*[@id="fulltext-search"]/div[2]/div/div/div[3]/div[3]/div[2]/div/button[2]').click()
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




def setting(index):
    '''
    index params 从 1 到 3
    '''
    if index == 1:
        # 无界面浏览器设置
        for i in range(len(href)):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            browser = webdriver.Chrome(options=chrome_options)
            browser.get(href[i])
            filename = title[i] + ".pdf"
            file_path = "C:\\Arch\\web\\" + filename
            os.rename(file_path, filename)
    if index == 2:
        # 默认下载方法
        for i in range(len(href)):
            headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
            res = requests.get(url=href[i], headers=headers)
            time.sleep(3)
            filename = title[i] + ".pdf"
            filepath = "C://Arch//Web//" + filename
            with open(filepath, 'wb') as f:
                f.write(res.content)
            print('成功')
    if index == 3:
        # 自己设定存储位置
        for i in range(len(title)):
            chrome_options = webdriver.ChromeOptions()
            prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'C:\\Arch\\web'}
            chrome_options.add_experimental_option('prefs', prefs)
            browser = webdriver.Chrome(options=chrome_options)
            browser.get([href[i]])
            try:
                browser.find_element(By.XPATH, '//*[@id="noticeDetail"]/div/div[1]/div[3]/div[3]/div[1]/button').click()
                time.sleep(5)
                print(str(i + 1) + '.' + title[i] + '下载完毕')
                browser.quit()
            except:
                print(title[i] + '不是PDF')
         
        def rename_files_in_directory(directory, old_suffix, new_suffix):
            for filename in os.listdir(directory):
                if filename.endswith(old_suffix):
                    os.rename(
                        os.path.join(directory, filename),
                        os.path.join(directory, filename.replace(old_suffix, new_suffix))
                    )
         
        # 使用示例
        directory_path = 'C:\\Arch\web'  # 替换为你的目录路径
        rename_files_in_directory(directory_path, '.crdownload', '')  # 将所有.txt后缀改为.md后缀
    else:
        raise IndexError
setting(2)
