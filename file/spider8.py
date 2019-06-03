import requests
from bs4 import BeautifulSoup

result = []
for i in range(10):
    res = requests.get('https://movie.douban.com/top250?start=' + str(i * 25) + '&filter=')

    html = res.text

    obj = BeautifulSoup(html, 'html.parser')

    movies = obj.find_all('div', class_='item')

    orders = []

    titles = []

    urls = []

    rates = []

    inqs = []

    for movie in movies:
        orders.append(movie.find('div', class_='pic').find('em').text)
        titles.append(movie.find('div', class_='hd').find('a').text.replace('\xa0', '').replace('\n', '').replace(' ',
                                                                                                                  ''))
        urls.append(movie.find('div', class_='hd').find('a')['href'])
        rates.append(movie.find('div', class_='bd').find('span', class_='rating_num').text)
        inqs.append(movie.find('div', class_='bd').find('span', class_='inq').text)

    for i in range(len(orders)):
        result.append([orders[i], titles[i], rates[i], inqs[i], urls[i]])

print(result)
