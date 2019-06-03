import requests

type = input('请输入快递公司:\n')
postid = input('请输入单号:\n')

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'www.kuaidi100.com',
    'Referer': 'https://www.kuaidi100.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'}

params = {
    'type': type,
    'postid': postid,
    'temp': '0.8718356580508402',
    'phone': ''
}

res = requests.get('https://www.kuaidi100.com/query', headers=headers, params=params)

infos = res.json()['data']

for info in infos:
    print(info)
    print(info['context'])
