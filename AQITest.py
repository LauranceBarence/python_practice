from gevent import monkey
import requests
import csv
from bs4 import BeautifulSoup
from gevent.queue import Queue
import gevent

monkey.patch_all()

base_url = 'http://www.pm25.in'
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 '
                  'Safari/537.36',
}
work = Queue()
task_list = []
aqi_list = []
name_dict = {}


# 爬取数据
def crawler_data():
    while not work.empty():
        try:
            url = work.get_nowait()
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                content_text = res.text
                content_object = BeautifulSoup(content_text, 'html.parser')
                data_source = content_object.find('div', class_='span12 data').find_all('div', class_='span1')
                result = {}
                for item in data_source:
                    name = item.find('div', class_='caption')
                    if name:
                        value = item.find('div', class_='value').text
                        result[str(name.text).strip()] = float(str(value).strip())
                city = name_dict[str(url).split('/')[-1]]
                aqi_list.append({city: result})
        except requests.exceptions.ConnectionError:
            print('连接超时')
            continue


# 获取城市
def crawl_city():
    try:
        res = requests.get(base_url, headers=headers, timeout=30)
        if res.status_code == 200:
            content_text = res.text
            content_object = BeautifulSoup(content_text, 'html.parser')
            alphabet_list = content_object.find('div', class_='all') \
                .find('div', class_='bottom').find_all('ul', class_='unstyled')
            url_list = []
            city_list = []
            for alphabet in alphabet_list:
                city_list.extend(alphabet.find_all('li'))
            for city in city_list:
                href = city.find('a')['href']
                province = city.find('a').text
                name_dict[str(href).replace('/', '')] = province
                url_list.append(base_url + href)
            return url_list
    except requests.exceptions.ConnectionError:
        print('连接超时')
        return None


def push_work(url_list):
    for url in url_list:
        work.put_nowait(url)


def split_task(count):
    for i in range(count):
        task = gevent.spawn(crawler_data)
        task_list.append(task)


def run():
    gevent.joinall(task_list)


# 格式化处理数据,存入文件
def format_data(data):
    pass


# 显示图形化结果
def draw_result(data):
    pass


def main():
    url_list = crawl_city()
    if url_list:
        push_work(url_list)
        split_task(10)
        run()
        print(aqi_list)


if __name__ == '__main__':
    main()
