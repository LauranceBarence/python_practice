from selenium import webdriver
import time

# env_path = './file/chromedriver.exe'

# driver = webdriver.Chrome(executable_path=env_path)

driver = webdriver.Chrome()
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
time.sleep(5)
driver.close()
