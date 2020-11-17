import wechatsogou

ws_api = wechatsogou.WechatSogouAPI(
proxies={
    "http": "192.168.64.117:8089",
})
# data = ws_api.search_gzh('南京航空航天大学')
data = ws_api.search_gzh('南京航空航天大学')
print(next(data))