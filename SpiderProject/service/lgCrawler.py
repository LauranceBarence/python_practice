import requests
import re
import time
import multiprocessing
from SpiderProject.dao.jobDao import JobDao


class Crawler(object):
    def __init__(self):
        self.lago_session = requests.session()
        self.header = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.'
                          '3683.86 Safari/537.36'
        }
        self.citys = []
        self.dao = JobDao()

    def crawl_city(self):
        city_search = re.compile(r'www\.lagou\.com\/.*\/">(.*?)</a>')
        city_url = 'https://www.lagou.com/jobs/allCity.html'
        city_text = self.base_crawl(method='Get', url=city_url).text
        self.citys = city_search.findall(city_text)
        self.lago_session.cookies.clear()

    def base_crawl(self, method, url, data=None, info=None):
        # while True:
        # proxy
        # proxyinfo = 'http://{username}:{passowrd}@{host}:{port}'.format(username='',password=''
        # ,host='http-dyn.abuyun.com',port='9020')
        # proxy = {
        #     'http':proxyinfo,
        #     'https':proxyinfo
        # }
        # try:
        if method.lower() == 'get':
            # res = self.lago_session.get(url=url, headers=self.header, proxies=proxy,timeout=6)
            res = self.lago_session.get(url=url, headers=self.header)
        elif method.lower() == 'post':
            # res = self.lago_session.post(url=url, data=data, headers=self.header, proxies=proxy,timeout=6)
            res = self.lago_session.post(url=url, data=data, headers=self.header)
            # except:
            #     self.lago_session.cookies.clear()
            #     cookie_url = 'https://www.lagou.com/jobs/list_{kd}?city={city}&cl=false&fromSearch=true&labelWords=
            # &suginput=' \
            #         .format(kd=info['kd'], city=info['city'])
            #     self.base_crawl(method='get', url=cookie_url)
            #     time.sleep(10)
        res.encoding = 'utf-8'
        # if '频繁' in res.text:
        #     break
        # self.lago_session.cookies.clear()
        # cookie_url = 'https://www.lagou.com/jobs/list_{kd}?city={city}&cl=false&fromSearch=true' \
        #              '&labelWords=&suginput='.format(kd=info['kd'], city=info['city'])
        # self.base_crawl(method='get', url=cookie_url)
        # time.sleep(10)
        # continue
        return res

    def crawl_job(self, city, kd):
        cookie_url = 'https://www.lagou.com/jobs/list_{kd}?city={city}&cl=false&fromSearch=true&labelWords=&suginput=' \
            .format(kd=kd, city=city)
        cookie_text = self.base_crawl(method='get', url=cookie_url).text
        page_re = re.compile(r'class="span\stotalNum">(.*?)</span>')
        try:
            total_num = page_re.search(cookie_text).group(1)
        except Exception:
            return
        else:
            for i in range(1, int(total_num) + 1):
                data = {
                    'pn': i,
                    'kd': kd
                }
                page_url = 'https://www.lagou.com/jobs/positionAjax.json?city={city}&needAddtionalResult=false'.format(
                    city=city)
                referer_url = cookie_url
                self.header['Referer'] = referer_url.encode()
                page_res = self.base_crawl(method='post', url=page_url, data=data, info={'kd': kd, 'city': city})
                if '频繁' in page_res.text:
                    break
                else:
                    job_json = page_res.json()
                    job_list = job_json['content']['positionResult']['result']
                    print(job_list)
                    for job in job_list:
                        self.dao.insert(job)

    def multi_crawl(self, kd):
        pool = multiprocessing.Pool(2)
        for city in self.citys:
            pool.apply_async(self.crawl_job, args=(city, kd))
            pool.close()
            pool.join()
