import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def get_weather():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url = 'http://www.weather.com.cn/weather/101021200.shtml'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    bsdata = BeautifulSoup(res.text, 'html.parser')
    data1 = bsdata.find(class_='tem')
    data2 = bsdata.find(class_='wea')
    return {'temperature': str(data1.text).strip(), 'weather': data2.text}


def send_mail(weather_info):
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)

    account = input('请输入你的邮箱：')
    password = input('请输入你的密码：')
    qqmail.login(account, password)

    receiver = input('请输入收件人的邮箱：')

    content = '亲爱的，今天的天气是：' + weather_info['temperature'] + weather_info['weather']
    message = MIMEText(content, 'plain', 'utf-8')
    subject = input('请输入你的邮件主题：')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print('邮件发送成功')
    except Exception:
        print('邮件发送失败')
    qqmail.quit()


def main():
    weather_info = get_weather()
    print(weather_info)
    send_mail(weather_info)


if __name__ == '__main__':
    main()
