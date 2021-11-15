from lxml import etree

html_doc = '''<bookstore>

<book category="COOKING" class="book as time now">
  <title lang="en">Everyday Italian</title>
  <author>Giada De Laurentiis</author>
  <year>2005</year>
  <price>30.00</price>
</book>

<book category="CHILDREN">
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

<book category="WEB">
  <title lang="en">XQuery Kick Start</title>
  <author>James McGovern</author>
  <author>Per Bothner</author>
  <author>Kurt Cagle</author>
  <author>James Linn</author>
  <author>Vaidyanathan Nagarajan</author>
  <year>2003</year>
  <price>49.99</price>
</book>

<book category="WEB">
  <title lang="en">Learning XML</title>
  <author>Erik T. Ray</author>
  <year>2003</year>
  <price>39.95</price>
</book>

</bookstore>'''

se = etree.HTML(html_doc)

print('取出所有书的名称',se.xpath('//book/title/text()'))
print('所有书本的语言',se.xpath('//book/title/@lang'))
print('第一本书的标题',se.xpath('//book[1]/title/text()'))
print('最后一本书的标题',se.xpath('//book[last()]/title/text()'))
print('倒数第二本书的标题',se.xpath('//book[last()-1]/title/text()'))
print('前两本书的标题',se.xpath('//book[position()<3]/title/text()'))
print('所有分类为web的书本',se.xpath('//book[@category="WEB"]/title/text()'))
print('所有价格大于30的书本',se.xpath('//book[price>30]/title/text()'))
print('所有class属性中包含book的书本的class属性',se.xpath('//book[contains(@class,"book")]/@class'))


