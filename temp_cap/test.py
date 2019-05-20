import base64
import requests

host = 'http://apigateway.jianjiaoshuju.com'
path = '/api/v_1/fzyzm.html'
method = 'POST'
querys = ''
bodys = {}
url = host + path
base64_data = ""
with open('/Users/allmight/PycharmProjects/Aquarius/temp_cap/1558317571244.jpg', 'rb') as fin:
    image_data = fin.read()
    base64_data = base64.b64encode(image_data)
headers = {
            'Connection': 'Keep-Alive',
            'Expect': '100-continue',
            'User-Agent': 'ben',
            'Content - Type':'application / x - www - form - urlencoded;charset = UTF - 8',
            'appCode': '0C55ECFA560A70068F15D9FAEF1C6573',
            'appKey': 'AKID8cc1c12ff10d4a280416bfbbda59e6d0',
            'appSecret': '931573d3c0ad8485735d825d25887e56'
        }
params = {
            'v_pic': base64_data,
            'v_type': 'ne6'
        }
r = requests.post('http://apigateway.jianjiaoshuju.com/api/v_1/fzyzm.html', data=params, headers=headers)
print(r.json())
