import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

data = {
    'content': input('请输入关键字')
}

res = requests.post('http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do', data=data, headers=headers)

vjson = json.loads(res.text)['vjson']

vjson_list = []
for key in vjson:
    vjson_list.extend(vjson[key])

result = []
for vjson_item in vjson_list:
    word = str(vjson_item).split(',')[0]
    rel = str(vjson_item).split(',')[1]
    result.append({'联想词': word, '相关度': rel})

print(result)
