import requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/')

text = res.text

html = BeautifulSoup(text, 'html.parser')

comments_bodys = html.find_all('article', class_='comment-body')

comments_list = []

for comment_body in comments_bodys:
    single_data = []
    user_name = comment_body.find('b', class_="fn").text
    content = comment_body.find('div', class_='comment-content').find('p').text
    single_data.append(user_name)
    single_data.append(content)
    comments_list.append(single_data)

print(comments_list)
