from lxml import etree
import requests
import threading
from queue import Queue



def fetch(url):
    '''抓取数据'''
    resp = requests.get(url)
    if resp.status_code !=200:
        return None
    return resp.text

def parse_univerity(url):
    '''解析数据'''
    data = {}
    if fetch(url):
        se = etree.HTML(fetch(url))
        keys = se.xpath("//div[@class='infobox']//table//td[1]//p/text()")
        cols = se.xpath("//div[@class='infobox']//table//td[2]")
        values = []
        for col in cols:
            values.append(' '.join(col.xpath(".//p//text()")))
        data['name'] = se.xpath("//div[@class='wikiContent']/h1/text()")[0].strip()
        if len(keys) == len(values):
            for i in range(len(keys)):
                data[keys[i]] = values[i]
    return data

def process_data(data):
    '''处理数据'''
    if data:
        print(data)


if __name__ == '__main__':
    start_url = "http://www.qianmu.org/ranking/902.htm"
    #1.请求入口页面
    se = etree.HTML(fetch(start_url))
    #2.提取列表页面的链接
    links = se.xpath("//div[@class='rankItem'][2]//tr[position()>1]/td[2]/a/@href")
    for link in links:
        if not link.startswith('http://www.qianmu.org'):
            link = "http://www.qianmu.org/%s" % link
        #提取详情页的信息
        data = parse_univerity(link)
        process_data(data)
