import requests

# 引用requests库
for i in range(1, 6):
    payload = {
        'ct': 24,
        'qqmusic_ver': 1298,
        'new_json': 1,
        'remoteplace': 'txt.yqq.song',
        'searchid': '60997426243444153',
        't': 0,
        'aggr': 1,
        'cr': 1,
        'catZhida': 1,
        'lossless': 0,
        'flag_qc': 0,
        'p': i,
        'n': 20,
        'w': '周杰伦',
        'g_tk': 5381,
        'loginUin': 0,
        'hostUin': 0,
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': 0,
        'platform': 'yqq.json',
        'needNewCode': 0
    }

    headers = {
        "user-agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    res_music = requests.get(
        'https://c.y.qq.com/soso/fcgi-bin/client_search_cp', headers=headers, params=payload)
    # 调用get方法，下载这个字典
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    for song in json_music['data']['song']['list']:
        print(song['name'])
        print('所属专辑:' + song['album']['name'])
        print('播放时长:' + str(int(song['interval'] / 60)) + ':' + str(song['interval'] % 60))
        print('播放链接:https://y.qq.com/n/yqq/song/' + song['mid'] + '.html')
