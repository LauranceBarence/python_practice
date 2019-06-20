import scrapy
import bs4
from ..items import JobuiItem


class JobuiSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['www.jobui.com']
    start_urls = ['https://www.jobui.com/rank/company/']

    # 获取详情页url
    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        ul_list = bs.find_all('ul', class_='textList flsty cfix')
        base_url = 'https://www.jobui.com{href}jobs'
        for ul in ul_list:
            link_list = ul.find_all('a')
            for link in link_list:
                company_href = link['href']
                url = base_url.format(href=company_href)
                yield scrapy.Request(url, callback=self.parse_job)

    # 获取详细信息
    def parse_job(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        company = str(bs.find('h1', id='companyH1').find('a').text).strip()
        data_list = bs.find_all('div', class_='job-simple-content')
        for data in data_list:
            item = JobuiItem()
            item['company'] = company
            item['position'] = str(data.find('a').text).strip()
            descs = data.find('div', class_='job-desc').find_all('span')
            item['location'] = str(descs[0].text).strip()
            item['requirement'] = str(descs[1].text).strip()
            yield item
