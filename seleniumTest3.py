from selenium import webdriver
import time

driver = webdriver.Chrome()


def login():
    driver.get('https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php')
    username = 'spiderman'
    password = 'crawler334566'
    time.sleep(1)
    username_slot = driver.find_element_by_id('user_login')
    username_slot.send_keys(username)
    password_slot = driver.find_element_by_id('user_pass')
    password_slot.send_keys(password)
    login_submit = driver.find_element_by_id('wp-submit')
    login_submit.click()
    time.sleep(1)


def to_article(index):
    entry_list = driver.find_elements_by_class_name('entry-title')
    entry_list.reverse()
    entry_list[index - 1].find_element_by_tag_name('a').click()
    time.sleep(1)


def submit_comment(text):
    print(text)
    comment_slot = driver.find_element_by_id('comment')
    comment_slot.send_keys(text)
    comment_submit = driver.find_element_by_id('submit')
    comment_submit.click()
    time.sleep(3)
    driver.close()


def main():
    login()
    to_article(3)
    submit_comment(text='selenium真好玩')


if __name__ == '__main__':
    main()
