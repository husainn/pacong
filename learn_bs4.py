from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'html.parser')

print(soup.title,type(soup.title))
print(dir(soup.title))
print(soup.a,type(soup.a))
print(soup.a.attrs)
print(soup.a.attrs['href'])
print(soup.a.attrs['class'])
print(soup.p)
print(list(soup.p.children))

print(soup.find_all('a'))
print(soup.find(id='link3').attrs['href'])
print(soup.get_text())

print(soup.select('.story a'))


