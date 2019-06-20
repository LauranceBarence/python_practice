import scrapy
import bs4
from ..items import DangdangItem


class DangDangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = 'bang.dangdang.com/'
    start_urls = []
    for x in range(1, 4):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + str(x)
        start_urls.append(url)

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        bang_list = bs.find('ul', class_='bang_list')
        book_items = bang_list.findAll('li')
        for book_item in book_items:
            item = DangdangItem()
            item['title'] = str(book_item.find('div', class_='name').find('a').text).strip()
            item['author'] = str(book_item.find('div', class_='publisher_info').find('a').text).strip()
            item['price'] = str(book_item.find('div', class_='price').find('p').find('span', class_='price_n').text)
            print(item['title'])
            yield item
