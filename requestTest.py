import requests
from requests import Response

# 爬虫起步，发起请求
res: Response = requests.get("https://static.pandateacher.com/Over%20The%20Rainbow.mp3")

print(res.content)

with open("./file/Rainbow.mp3", "wb") as file:
    file.write(res.content)
