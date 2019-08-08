from SpiderProject.service.lgCrawler import Crawler
from SpiderProject.controller.view import app


def main():
    app.run(debug=True,host="0.0.0.0",port="8088")
    # crawler = Crawler()
    # crawler.crawl_city()
    # for city in crawler.citys:
    #     print(city)
    #     crawler.crawl_job(city, 'Python')
    #     break


if __name__ == '__main__':
    main()
