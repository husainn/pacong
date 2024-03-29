#案例
import requests

import gevent
from gevent import monkey

monkey.patch_all()

def download(url):
    res = requests.get(url)
    content = res.text
    print('下载了{}的数据，长度'.format(url))

if __name__ == '__main__':
    urls = ['http://www.163.com','http://www.qq.com','http://www.baidu.com']
    g1 = gevent.spawn(download,urls[0])
    g2 = gevent.spawn(download,urls[1])
    g3 = gevent.spawn(download,urls[2])

    gevent.joinall(g1,g2,g3)

    print('end')