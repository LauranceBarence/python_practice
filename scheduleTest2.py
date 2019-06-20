import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random
import time
import schedule


def spider_foods():
    res_foods = requests.get('http://www.xiachufang.com/explore/')
    bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
    list_foods = bs_foods.find_all('div', class_='info pure-u')

    list_all = []

    for food in list_foods:
        tag_a = food.find('a')
        name = tag_a.text[17:-13]
        URL = 'http://www.xiachufang.com' + tag_a['href']
        tag_p = food.find('p', class_='ing ellipsis')
        ingredients = tag_p.text[1:-1]
        list_all.append([name, URL, ingredients])
    return list_all


def send_mail(food_list):
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)

    account = input('请输入你的邮箱：')
    password = input('请输入你的密码：')
    qqmail.login(account, password)

    receiver = input('请输入收件人的邮箱：')

    content = '今天就吃' + random.sample(food_list,1)[0][0] + '吧'
    message = MIMEText(content, 'plain', 'utf-8')
    subject = input('请输入你的邮件主题：')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print('邮件发送成功')
    except Exception:
        print('邮件发送失败')
    qqmail.quit()


def job():
    foods = spider_foods()
    send_mail(foods)


def main():
    schedule.every().friday.at('12:00').do(job)
    while True:
        schedule.run_pending()
        time.sleep(3600)


if __name__ == '__main__':
    main()
