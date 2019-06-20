import scrapy
import bs4
from ..items import DbcommentItem


class DbcommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['book.douban.com']
    start_urls = []
    for i in range(2):
        url = 'https://book.douban.com/top250?start={}'.format(i * 25)
        start_urls.append(url)

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        datas = bs.find_all('tr', class_="item")
        for data in datas:
            url = data.find('div', class_='pl2').find('a')['href']
            yield scrapy.Request(url, callback=self.parse_comment)

    def parse_comment(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        title = str(bs.find('div', id='wrapper').find('h1').text).strip()
        comment_lists = bs.find_all('div', class_='comment')
        for comment in comment_lists:
            comment_info = comment.find('span', class_='comment-info')
            id = str(comment_info.find('a').text).strip()
            short = str(comment.find('span', class_='short').text).strip()
            item = DbcommentItem()
            item['title'] = title
            item['id'] = id
            item['comment'] = short
            yield item
