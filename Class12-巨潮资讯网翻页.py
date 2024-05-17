 from selenium import webdriver
 import re
 import time
 from selenium.webdriver.common.by import By
 def juchao(keyword):
     browser = webdriver.Chrome()
     url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=' + '阿里巴巴'
     browser.get(url)
     time.sleep(4)
     
     for i in range(2):
         for j in range(1, 21):
             href_1 = browser.find_element(By.XPATH, '//*[@id="fulltext-search"]/div[2]/div/div/div[3]/div[3]/div[1]/div/div[3]/table/tbody/tr[' + str(j) + ']/td[2]/div/a')
             href = href_1.get_attribute('href')
             print(href)
             title = browser.find_element(By.XPATH, '//*[@id="fulltext-search"]/div[2]/div/div/div[3]/div[3]/div[1]/div/div[3]/table/tbody/tr[' + str(j) + ']/td[2]/div/a').text
             print(title)
             date = browser.find_element(By.XPATH, '//*[@id="fulltext-search"]/div[2]/div/div/div[3]/div[3]/div[1]/div/div[3]/table/tbody/tr[' + str(j) + ']/td[3]/div/span').text
             print(date)
         try:
             browser.find_element(By.XPATH, '//*[@id="fulltext-search"]/div[2]/div/div/div[3]/div[3]/div[2]/div/button[2]').click()
             time.sleep(3)
         except:
             print('已经到最后一页')
             break
         
 keywords = ['阿里巴巴']
 for i in keywords:
     juchao(i)

