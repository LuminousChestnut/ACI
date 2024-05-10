from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
service = ChromeService(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)
# driver.quit()
driver.get("https://www.baidu.com/")
driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('阿里巴巴')
# driver.find_element(By.CSS_SELECTOR, 'CSS_SELECTOR')
# driver.find_element(By.XPATH,'//*[@id="su"]').click()
# time.sleep(3)
data = driver.page_source
print(data)
# driver.get("https://finance.sina.com.cn/realstock/company/sh000001/nc.shtml")
# data = driver.get_source
# print(data)
