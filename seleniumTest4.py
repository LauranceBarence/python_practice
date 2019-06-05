from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time

# env_path = './file/chromedriver.exe'

# driver = webdriver.Chrome(executable_path=env_path)

option = Options()
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(1)

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('吴枫')
time.sleep(1)
assistant = driver.find_element_by_id('assistant')
assistant.send_keys('卡西')
time.sleep(1)
button = driver.find_element_by_class_name('sub')
button.click()
time.sleep(1)
content_html = driver.page_source
content_obj = BeautifulSoup(content_html, 'html.parser')
content_list = content_obj.find_all('div', class_='content')
for content in content_list:
    print(content.text)
content_list = driver.find_elements_by_class_name('content')
for content in content_list:
    print(content.text)
driver.close()
