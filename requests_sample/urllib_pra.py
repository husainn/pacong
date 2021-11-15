import urllib
import json
from urllib.request import urlopen

r = urlopen('http://httpbin.org/get')
#读取response的内容,读出来的是二进制文件，需要编码
text = r.read()
content = text.decode('utf-8')
print(type(text),'text',text)
print(type(content),'content',content)
#返回的内容是json格式，直接用loads函数加载成字典
dict1 = json.loads(text)
print(dict1)

#http返回码和msg
print(r.status,r.reason)

#r.headers是一个HTTPMessage对象
print(r.headers)
for k,v in r.headers._headers:
    print(k,v)

ua = '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'''

req = urllib.request.Request('http://httpbin.org/user-agent')
req.add_header('User-Agent',ua)

r = urllib.request.urlopen(req)
print(json.load(r)['user-agent'])

