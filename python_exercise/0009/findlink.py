# **一个HTML文件，找出里面的**链接**
__author__ = 'zxy'

from urllib import request
from bs4 import BeautifulSoup


def findtext(url):
    req = request.Request(url)
    html = request.urlopen(req).read()
    soup = BeautifulSoup(html)
    linkHtmls = soup.find_all('a')
    for linkHtml in linkHtmls:
        print(linkHtml.get('href'))


if __name__ == '__main__':
    url = 'http://www.jianshu.com/p/19fef9871730'
    findtext(url)
