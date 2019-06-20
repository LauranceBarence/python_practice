from gevent import monkey

monkey.patch_all()

import openpyxl
import requests
from bs4 import BeautifulSoup
import gevent
from gevent.queue import Queue
from openpyxl.utils.exceptions import IllegalCharacterError

base_url = 'http://www.boohee.com/food/group/INDEX?page=PAGE'
special_url = 'http://www.boohee.com/food/view_menu?page=PAGE'
work = Queue()
task_list = []
food_list = []
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 '
                  'Safari/537.36',
}


def get_url_list():
    url_list = []
    for i in range(1, 11):
        for j in range(1, 11):
            url_list.append(base_url.replace('INDEX', str(i)).replace('PAGE', str(j)))
    for i in range(1, 11):
        url_list.append(special_url.replace('PAGE', str(i)))
    return url_list


def push_work(url_list):
    for url in url_list:
        work.put_nowait(url)


def crawler_data():
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        text = res.text
        obj = BeautifulSoup(text, 'html.parser')
        food_objects = obj.find('ul', class_='food-list').findAll('li', class_='item')
        for food_object in food_objects:
            food_text = food_object.find('div', class_='text-box')
            food_name = str(food_text.find('h4').text).strip()
            food_calorie = str(food_text.find('p').text).split('：')[1]
            food_url = 'http://www.boohee.com/'+str(food_text.find('h4').find('a')['href']).strip()
            food_list.append([food_name, food_calorie, food_url])


def save_data(lists):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '食物热量表'
    sheet['A1'] = '食物'
    sheet['B1'] = '热量'
    sheet['C1'] = '链接'
    for row in lists:
        try:
            sheet.append(row)
        except IllegalCharacterError:
            print(row)
            break
    wb.save('./file/food.xlsx')


def split_task(count):
    for i in range(count):
        task = gevent.spawn(crawler_data)
        task_list.append(task)


def run():
    gevent.joinall(task_list)


def main():
    url_list = get_url_list()
    push_work(url_list)
    split_task(10)
    run()
    # print(food_list)
    save_data(food_list)


if __name__ == '__main__':
    main()
