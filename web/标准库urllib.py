import urllib.request

response: object=urllib.request.urlopen("http://www.baidu.com/")
#这里是用http可以返回数据，如果用https则返回不了数据
print(response.status)
print(response.read())
