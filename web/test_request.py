import requests

r = requests.get("http://www.baidu.com")
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

