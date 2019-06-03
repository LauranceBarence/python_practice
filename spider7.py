import requests
from bs4 import BeautifulSoup
import csv


def set_header():
    file_exist = False
    try:
        with open('./file/movie.csv', 'r') as test:
            liss = []
            for i in test:
                liss.append(i)
            if len(liss) == 0:
                file_exist = True
    except FileNotFoundError:
        file_exist = True
    if file_exist:
        with open('./file/movie.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile, dialect='excel')
            header = ['序号', '电影名', '评分', '推荐语', '链接']
            csv_writer.writerow(header)


def write_data(data):
    with open('./file/movie.csv', 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel')
        for movie in data:
            csv_writer.writerow(movie)


def spider_data():
    result = []
    for i in range(10):
        res = requests.get('https://movie.douban.com/top250?start=' + str(i * 25) + '&filter=')

        html = res.text

        obj = BeautifulSoup(html, 'html.parser')

        movies = obj.find_all('div', class_='item')

        for movie in movies:
            order = str(movie.find('div', class_='pic').find('em').text).encode('utf-8').decode('utf-8')
            title = str(movie.find('div', class_='hd').find('a').text.replace('\xa0', '').replace('\n', '').replace(' ', '')).encode('utf-8').decode('utf-8')
            url = str(movie.find('div', class_='hd').find('a')['href']).encode('utf-8').decode('utf-8')
            rate = str(movie.find('div', class_='bd').find('span', class_='rating_num').text).encode('utf-8').decode('utf-8')
            inq = str(movie.find('div', class_='bd').find('span', class_='inq').text).encode('utf-8').decode('utf-8')
            result.append([order, title, rate, inq, url])
    print(result)
    return result


def main():
    set_header()
    data = spider_data()
    write_data(data)


if __name__ == '__main__':
    main()
