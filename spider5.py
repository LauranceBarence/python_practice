import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.xiachufang.com/explore/')

html = res.text

obj = BeautifulSoup(html, 'html.parser')

foods = obj.find_all('div', class_='info pure-u')

url_header = 'http://www.xiachufang.com'

result = []
for food in foods:
    r = []
    href = food.find('p', class_='name').find('a')
    name = href.text
    link = href['href']
    eles = food.find('p', class_='ellipsis')
    r.append(str(name).strip())
    r.append((url_header+link))
    r.append(eles.text.strip())
    result.append(r)
print(result)

