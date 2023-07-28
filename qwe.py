import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='C:\QAyandex\env\Lib\site-packages\selenium\webdriver\chrome')

driver = webdriver.Chrome(service=service)

driver.get('http://google.com')
time.sleep(5)
driver.quit()