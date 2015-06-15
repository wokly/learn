# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

__author__ = 'wwx199990'
for i in range(1,100):
    myUrl = "http://www.qiushibaike.com/text/page/"+str(i)+"?s=4781171"
    req = urllib2.Request(myUrl, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    myResponse = urllib2.urlopen(req)
    myPage = myResponse.read()
    unicodePage = myPage.decode("utf-8")
    soup = BeautifulSoup(myPage, from_encoding="utf8")
    items = soup.find_all(attrs={"class": "article block untagged mb15"})

    for item in items:
        stats = item.find_all('div',class_="stats")
        vote = stats[0].find_all('span',class_="stats-vote")
        votenums = vote[0].find_all('i',class_="number")
        votenum = votenums[0].string
        if int(votenum)>2000:
            print "voteNumber="+votenum
            contents= item.find_all('div',class_="content")[0].stripped_strings
            for content in contents:
                print content



