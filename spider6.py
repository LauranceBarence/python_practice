import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.xiachufang.com/explore/')

html = res.text

obj = BeautifulSoup(html, 'html.parser')

foods = obj.find_all('div', class_='info pure-u')

url_header = 'http://www.xiachufang.com'

result = []

names = []

URLs = []

indent_strips = []

for food in foods:
    href = food.find('p', class_='name').find('a')
    name = href.text
    link = href['href']
    eles = food.find('p', class_='ellipsis')
    names.append(str(name).strip())
    URLs.append((url_header + link))
    indent_strips.append(eles.text.strip())

for i in range(len(names)):
    result.append([names[i], URLs[i], indent_strips[i]])

print(result)
