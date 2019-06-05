#  https://y.qq.com/n/yqq/song/000zV1tU1EuUie.html  https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import time
option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(options=option)

driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')

time.sleep(2)

while True:
    comment_content = driver.find_element_by_class_name('js_hot_list')

    comment_list = comment_content.find_elements_by_class_name('js_hot_text')
    try:
        get_more = driver.find_element_by_class_name('comment__show_all').find_element_by_class_name('js_get_more_hot')
        time.sleep(1)
        get_more.click()
    except NoSuchElementException:
        print('所有评论已加载完毕')
        break
    except StaleElementReferenceException:
        print('所有评论已加载完毕')
        break
    if len(comment_list) >= 30:
        break
# print(len(comment_list))
for comment in comment_list:
    print(comment.text)
time.sleep(3)
driver.close()
