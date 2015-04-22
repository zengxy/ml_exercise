# 一个HTML文件，找出里面的**正文**
__author__ = 'zxy'
from bs4 import BeautifulSoup
from urllib import request

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


def test():
    soup = BeautifulSoup(html_doc)
    for link in soup.find_all('a'):
        print(link.get_text())


def findtext(url):
    req = request.Request(url)
    html = request.urlopen(req).read()
    soup=BeautifulSoup(html)
    article = soup.find("div", class_="show-content")
    for paragraph in article.find_all('p'):
         print(paragraph.get_text())


if __name__ == '__main__':
    url='http://www.jianshu.com/p/19fef9871730'
    findtext(url)
