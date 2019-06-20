from gevent import monkey
monkey.patch_all()
import gevent
import requests
import openpyxl
from bs4 import BeautifulSoup
from openpyxl.utils.exceptions import IllegalCharacterError

from gevent.queue import Queue

baseUrl = 'http://www.mtime.com/top/tv/top100/'

url_list = []
for i in range(1, 11):
    if i == 1:
        url_list.append(baseUrl)
    else:
        url_list.append((baseUrl + 'index-' + str(i) + '.html'))
work = Queue()

for url in url_list:
    work.put_nowait(url)

tv_infos = []


def spider():
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url)
        res.encoding = 'utf-8'
        text = res.text
        obj = BeautifulSoup(text, 'html.parser')
        cons = obj.find_all('div', class_='mov_con')
        for con in cons:
            h2 = con.find('h2')
            p0 = h2.find_next_sibling('p')
            title = str(h2.find('a').text).replace('\xa0', ' ')
            if p0:
                if p0.find('a'):
                    director = p0.find('a').text
                else:
                    director = ''
            else:
                director = ''
            main_characters = []
            p2 = p0.find_next_sibling('p')
            if p2:
                characters = p2.find_all('a')
                for character in characters:
                    main_characters.append(character.text)
                character = ' '.join(main_characters)
            else:
                character = ''
            dis = con.find('p', class_='mt3')
            if dis:
                description = str(dis.text).strip()
                description = description.replace('\x12', '·')
            else:
                description = ''
            tv_info = [title, director, character, description]
            tv_infos.append(tv_info)


def save_result(data):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '电视剧'
    sheet['A1'] = '剧名'
    sheet['B1'] = '导演'
    sheet['C1'] = '主演'
    sheet['D1'] = '简介'
    for row in data:
        try:
            sheet.append(row)
        except IllegalCharacterError:
            print(row)
            break
    wb.save('./file/tv.xlsx')


task_list = []

for x in range(10):
    task = gevent.spawn(spider)
    task_list.append(task)

gevent.joinall(task_list)

# print(tv_infos)
save_result(tv_infos)
