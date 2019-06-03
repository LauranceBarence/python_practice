from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib


def init_server(host, port):

    server = smtplib.SMTP()
    server.connect(host, port)
    return server


def main():
    username = '823271383@qq.com'
    password = 'auyyfbpxtpeybcdd'
    server = init_server('smtp.qq.com', 465)
    server.login(username, password)
    server


if __name__ == '__main__':
    main()
