# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:43:04 2024

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import re
service = ChromeService(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4")
data=driver.page_source

# 1. XPATH 匹配
dictFund = {}
for i in range(1, 21):
    path = driver.find_element(By.XPATH, '//*[@id="fulltext-search"]/div[2]/div/div/div[3]/div[3]/div[1]/div/div[3]/table/tbody/tr[' + str(i) + ']/td[2]/div/a').get_attribute("href")
    title = driver.find_element(By.XPATH, '//*[@id="fulltext-search"]/div[2]/div/div/div[3]/div[3]/div[1]/div/div[3]/table/tbody/tr[' + str(i) + ']/td[2]/div/a/span/span').text
    time = driver.find_element(By.XPATH, '//*[@id="fulltext-search"]/div[2]/div/div/div[3]/div[3]/div[1]/div/div[3]/table/tbody/tr[' + str(i) + ']/td[3]/div/span').text
    dictFund[title + ' ' + time] = path
print(dictFund)




# 2. 正则表达式匹配
p_href='<div class="cell"><a target="_blank" href="(.*?)" data-id.*?</div>'
href=re.findall(p_href,data)
print(href)
p_title='<div class="cell"><a target="_blank" href=.*?<span class="tileSecName-content">(.*?)</span></span>'
title=re.findall(p_title,data)
for i in range(len(title)):
    title[i]=re.sub('<.*?>','',title[i])
    print(title[i])
p_time='<div class="cell"><span class="time".*?>(.*?)</span>'
time=re.findall(p_time,data,re.S)
for i in range(len(time)):
    time[i]=re.sub(' ','',time[i])
    href[i]=href[i].replace('amp;','')
    print(time[i])
    print(str(i+1)+','+title[i]+'--'+time[i])
    print('http://www.cninfo.com.cn'+href[i])







