import requests
import hashlib
import json

# 3bb2b801cade4408a1b229db11e56b7c
api_key = input('请输入api秘钥:\n')
headers = {
    'content-type': 'application/json'
}
encrypter = hashlib.md5()
user_name = input('请输入用户名:\n')
encrypter.update(user_name.encode('utf-8'))
userId = encrypter.hexdigest()
print('请输入聊天内容:')
while True:
    message = input()
    req = {
        "perception": {
            "inputText": {
                "text": message
            }
        },
        "userInfo": {
            "apiKey": api_key,
            "userId": userId
        }
    }

    data = json.dumps(req).encode('utf-8')

    res = requests.post('http://openapi.tuling123.com/openapi/api/v2', data=data, headers=headers)
    result = res.json()['results'][0]['values']['text']
    print(result)
    if '再见' in result or '再见' in message:
        break
