import requests
from bs4 import BeautifulSoup
import urllib

keyword = input('请输入搜索关键词:')

encoded_keyword = urllib.parse.quote(keyword.encode('gbk'))

result = []

res = requests.get('http://s.ygdy8.com/plus/so.php?typeid=1&keyword=' + encoded_keyword)

res.encoding = 'gbk'

html = res.text

html_header = 'https://www.ygdy8.com'

obj = BeautifulSoup(html, 'html.parser')

movies = obj.find('div', class_='co_content8').find_all('table')

for movie in movies:
    r = []
    a = movie.find('a')
    r.append(a.text)
    url = html_header + a['href']
    sub_res = requests.get(url)
    sub_res.encoding='gbk'
    sub_text = sub_res.text
    sub_obj = BeautifulSoup(sub_text, 'html.parser')
    link = sub_obj.find('div', class_='co_content8').find('table').find('a')
    r.append(link.text)
    result.append(r)

print(result)
