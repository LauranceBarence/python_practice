import requests

keyword = input('请输入想搜索的歌手名')
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
        'w': keyword,
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
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        "Origin": "https://y.qq.com",
        "Referer": "https://y.qq.com/n/yqq/song/0009BCJK1nRaad.html",
        "Accept": 'application/json, text/javascript, */*; q=0.01'
    }
    res_music = requests.get(
        'https://c.y.qq.com/soso/fcgi-bin/client_search_cp', headers=headers, params=payload)
    # 调用get方法，下载这个字典
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    for song in json_music['data']['song']['list']:
        song_id = song['id']
        print(song['name'])
        params={
        'nobase64': 1,
        'musicid': song_id,
        '-': 'jsonp1',
        'g_tk': '227993575',
        'loginUin': '823271383',
        'hostUin': 0,
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': 0,
        'platform': 'yqq.json',
        'needNewCode': 0
        }
        # res = requests.get("https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg", headers=headers, params=params)
        # print(res.json()['lyric'])