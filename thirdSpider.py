import requests
from bs4 import BeautifulSoup

# 爬虫与BeautifulSoup练习 爬取书籍详细信息
res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')

html = res.text

obj = BeautifulSoup(html, 'html.parser')

books = obj.find_all('article', class_='product_pod')

book_storage = []
for book in books:
    title = book.find('h3').find('a')['title']
    price = book.find('p', class_='price_color')
    rank_class = book.find('p', class_='star-rating')['class'][1]
    if rank_class == 'One':
        rank = 1
    elif rank_class == 'Two':
        rank = 2
    elif rank_class == 'Three':
        rank = 3
    elif rank_class == 'Four':
        rank = 4
    else:
        rank = 5
    book_storage.append({'title': title, 'price': price.text, 'rank': rank})

print(book_storage)
