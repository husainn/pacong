import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
r = requests.get('http://www.xiachufang.com/',headers=header)
soup =BeautifulSoup(r.text,'lxml')
#提取所有img标签
img_list = []
for i in soup.select('img'):
    if i.has_attr('data-src'):
        img_list.append(i.attrs['data-src'])
    else:
        img_list.append(i.attrs['src'])

#初始化下载文件目录
img_dir = os.path.join(os.path.curdir,'images')
# if not os.path.isdir(img_dir):
#     os.mkdir(img_dir)

for img in img_list:
    pic_name = urlparse(img).path[1:]
    url = img.split('?')[0]
    # print(img_dir)
    file_path = os.path.join(img_dir,pic_name)
    print(file_path)
    # if not os.path.isdir(os.path.dirname(file_path)):
    #     os.mkdir(os.path.dirname(file_path))
    # resp = requests.get(url)
    # with open(file_path,'wb') as stream:
    #     stream.write(resp.content)
    #     print('完成下载：',file_path)

