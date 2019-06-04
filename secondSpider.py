import requests
from bs4 import BeautifulSoup

# 爬虫与BeautifulSoup练习 爬取书籍信息
res = requests.get('http://books.toscrape.com/')

html = res.text

obj = BeautifulSoup(html, 'html.parser')

first_classes = obj.find('div', class_='side_categories').find('ul').find('ul').find_all('li')

for clazz in first_classes:
    print(str(clazz.find('a').text).strip())
