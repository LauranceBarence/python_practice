import requests
from bs4 import BeautifulSoup

res = requests.get('https://spidermen.cn/')

html = res.text

obj = BeautifulSoup(html, 'html.parser')

articles = obj.find_all('header', class_='entry-header')

for article in articles:
    title = article.find('h2', class_='entry-title').find('a')
    print('文章标题:'+title.text)
    publish_date = article.find('time', class_='published').text
    print('发布日期：'+publish_date)
    print('文章链接:'+title['href'])

