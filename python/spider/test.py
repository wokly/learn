# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

__author__ = 'wwx199990'
myUrl = "http://www.qiushibaike.com/text/page/2?s=4781171"
req = urllib2.Request(myUrl, headers ={
'Connection': 'Keep-Alive',
'Accept': 'text/html, application/xhtml+xml, */*',
'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
myResponse = urllib2.urlopen(req)
myPage = myResponse.read()
unicodePage = myPage.decode("utf-8")
soup = BeautifulSoup(myPage,from_encoding="utf8")
items = soup.find_all(attrs={"class": "article block untagged mb15"})
i=0
for item in items:
    print 'div'+str(i)+'=================================================================='
    for contentItem in item.descendants:
        content = contentItem .find(attrs={"class": "content"})
        for string in content.stripped_strings:
            print (string)
    i+=1
