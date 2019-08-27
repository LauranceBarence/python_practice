from gevent import monkey
import requests
import csv
from bs4 import BeautifulSoup
from gevent.queue import Queue
import gevent
import pandas
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

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


# 添加协程任务
def push_work(url_list):
    for url in url_list:
        work.put_nowait(url)


# 分配协程任务
def split_task(count):
    for i in range(count):
        task = gevent.spawn(crawler_data)
        task_list.append(task)


# 启动协程
def run():
    gevent.joinall(task_list)


# 格式化处理数据,存入文件
def format_data(data):
    file_list = []
    header_list = ['city', 'AQI', 'PM2.5/1h', 'PM10/1h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']
    for item in data:
        row = []
        for city in item:
            row.append(city)
            for key in item[city]:
                value = item[city][key]
                row.append(value)
        file_list.append(row)
    # with open('./file/AQI.csv', 'w', encoding='utf-8', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(header_list)
    #     for row in file_list:
    #         writer.writerow(row)
    result = pandas.DataFrame(data=file_list, columns=header_list)
    return result


# 显示图形化结果
def draw_result_array(data):
    # data.to_excel('./file/AQI.xlsx', index=False, sheet_name='2019.0827',encoding='utf-8')
    show_result = data.sort_values(by=['AQI']).tail(10)
    show_result.plot(kind='bar', x='city', y='AQI')
    plt.show()


# 读取文件
def read_csv_file(filepath):
    file_content = filter_data(pandas.read_csv(filepath))
    return file_content


# 数据清洗
def filter_data(data):
    condition = data['AQI'] > 0
    return data[condition]


def main():
    # url_list = crawl_city()
    # if url_list:
    #     push_work(url_list)
    #     split_task(10)
    #     run()
    #     formated_data = format_data(aqi_list)
    formated_data = read_csv_file('./file/AQI.csv')
    draw_result_array(formated_data)


if __name__ == '__main__':
    main()
