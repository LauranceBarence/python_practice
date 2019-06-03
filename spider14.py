import requests
from bs4 import BeautifulSoup
import openpyxl


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


def write_data(data):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = '序号'
    sheet['B1'] = '电影名'
    sheet['C1'] = '评分'
    sheet['D1'] = '推荐语'
    sheet['E1'] = '链接'

    for row in data:
        sheet.append(row)
    wb.save('./file/movie.xlsx')


def main():
    data = spider_data()
    write_data(data)


if __name__ == '__main__':
    main()
