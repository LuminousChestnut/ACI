from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import re
service = ChromeService(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://finance.sina.com.cn/realstock/company/sh000001/nc.shtml")
driver.find_element(By.XPATH,'//*[@id="price"]')
data = driver.page_source
texts = re.findall('<div id="price" class=".*?">(.*?)</div>',data, re.S)
print(texts)    
