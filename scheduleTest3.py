import requests
from bs4 import BeautifulSoup
from urllib.request import quote
import time
import csv
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import schedule


def spider_movie():
    csv_file = open('movieTop.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(csv_file)

    for x in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(x * 25) + '&filter='
        res = requests.get(url)
        bs = BeautifulSoup(res.text, 'html.parser')
        bs = bs.find('ol', class_="grid_view")
        for titles in bs.find_all('li'):
            title = titles.find('span', class_="title").text
            list1 = [title]
            writer.writerow(list1)
    csv_file.close()


def get_download_link():
    movie = input('你想看什么电影？')
    gbkmovie = movie.encode('gbk')
    urlsearch = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword=' + quote(gbkmovie)
    res = requests.get(urlsearch)
    res.encoding = 'gbk'
    soup_movie = BeautifulSoup(res.text, 'html.parser')
    urlpart = soup_movie.find(class_="co_content8").find_all('table')
    if urlpart:
        urlpart = urlpart[0].find('a')['href']
        urlmovie = 'https://www.ygdy8.com/' + urlpart
        res1 = requests.get(urlmovie)
        res1.encoding = 'gbk'
        soup_movie1 = BeautifulSoup(res1.text, 'html.parser')
        urldownload = soup_movie1.find('div', id="Zoom").find('span').find('table').find('a')['href']
        print(urldownload)
        return urldownload
    else:
        print('没有' + movie + '的链接')
        return ''


def send_mail(content):
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)

    account = input('请输入你的邮箱：')
    password = input('请输入你的密码：')
    qqmail.login(account, password)

    receiver = input('请输入收件人的邮箱：')

    message = MIMEText(content, 'plain', 'utf-8')
    subject = '电影链接'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print('邮件发送成功')
    except Exception:
        print('邮件发送失败')
    qqmail.quit()


def list_movie():
    with open('./file/movie.csv', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['\ufeff序号'] + '.' + row['电影名'])


def job():
    link = get_download_link()
    if link == '':
        pass
    else:
        send_mail(link)


def main():
    spider_movie()
    list_movie()
    schedule.every().friday.at('21:00').do(job)
    while True:
        schedule.run_pending()
        time.sleep(3600)
