import requests
import openpyxl


def spider_data():
    keyword = input('请输入想搜索的歌手名')
    result = []
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
            result.append([song['name'], song['album']['name'],
                           str(int(song['interval'] / 60)) + ':' + str(song['interval'] % 60),
                           'https://y.qq.com/n/yqq/song/' + song['mid'] + '.html'])
    return result


def save_data(data):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = '歌名'
    sheet['B1'] = '所属专辑'
    sheet['C1'] = '时长'
    sheet['D1'] = '播放链接'

    for row in data:
        sheet.append(row)
    wb.save('./file/test.xlsx')


def main():
    result = spider_data()
    save_data(result)


if __name__ == '__main__':
    main()
