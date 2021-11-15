import requests

#get请求
r = requests.get('http://httpbin.org/get')
print(r.status_code,r.reason)
print(r.text)

#带参数的get请求
r = requests.get('http://httpbin.org/get',params={'a':'1','b':'2'})
#r.json,将返回对象转换为字典输出
print(r.json())

#post请求
r = requests.post('http://httpbin.org/post',data={'a':'1'})
print(type(r.json()),type(r.text))

#自定义headers请求
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {'User-Agent':ua}
r= requests.get('http://httpbin.org/get',headers=headers)
print(r.json())

#带cookies的请求
cookies=dict(userid='123456',token='xxxxxxxxxxx')
r = requests.get('http://httpbin.org/get',cookies=cookies)
print('带cookies的请求',r.json())

#带auth的请求
r = requests.get('http://httpbin.org/basic-auth/huge/123456',auth=('huge','123456'))
print('basic-auth认证请求',r.json())

#使用session请求
s = requests.Session()
s.get('http://httpbin.org/cookies/set/userid/1234578')
r = s.get('http://httpbin.org/cookies')
print('检查session中的cookies',r.json())

#在requests中使用代理
print('不使用代理：',requests.get('http://httpbin.org/ip').json())
print('使用代理：',requests.get(
    'http://httpbin.org/ip',
    proxies={'http':'http://111.72.25.45:3256'}
).json())

requests.get('http://httpbin.org',timeout=5)