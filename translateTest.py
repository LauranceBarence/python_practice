import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

data = {
    'i': input('请输入中文:'),
    'from': 'zh-CHS',
    'to': 'en',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}

res = requests.post('http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule', headers=headers, data=data)

print(res.json()['translateResult'][0][0]['tgt'])
