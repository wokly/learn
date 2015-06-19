# -*- coding: utf-8 -*-
import urllib2
import re

__author__ = 'wwx199990'
outfile = open('d:/test.txt','w')
for i in range(1,3):
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
    reg_content=r'<div class="content">(.*?)<!--(.*?)-->'
    reg_vote=r'<span class="stats-vote"><i class="number">(.*?)</i>'
    contents = re.findall(reg_content,unicodePage,re.S)
    votes=re.findall(reg_vote,unicodePage)
    print 'contentslen=',len(contents)
    print 'voteslen=',len(votes)
    for j in range(len(votes)-1):
        if (int)(votes[j])>10:
            outfile.write(votes[j])
            outfile.write(contents[j][1].encode('gb18030'))
            content=contents[j][0].replace(r'<br/>','\n')
            outfile.write(content.encode('gb18030'))
            #print votes[j]
            #print contents[j][1]
            #print contents[j]





