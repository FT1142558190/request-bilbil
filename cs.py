import requests
import json

url = 'http://example.com/api/some-endpoint'  # 请替换为正确的URL
headers = {'Content-Type': 'application/json'}
data = {
    'q': '这个程序的作者是谁？',
    'a': 'Ne-21'
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# 处理响应...