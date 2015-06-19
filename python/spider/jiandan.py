# -*- coding: utf-8 -*-
import urllib2
import os
import re
from threading import Thread
from Queue import Queue

__author__ = 'wwx199990'
outfile = open('d:/test.txt','w')
for page in range(1355,1426):
    print 'page=',page
    myUrl ='http://jandan.net/ooxx1/page-'+str(page)+'#comments'
    req = urllib2.Request(myUrl, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    myResponse = urllib2.urlopen(req)
    myPage = myResponse.read()
    unicodePage = myPage.decode("utf-8")
    reg_content=r'</span><p>.*?<img src=.*?</p>'
    reg_support = r'<span id="cos_support-.*?">(.*?)</span>'
    reg_gifimgs=r'org_src="(.*?.gif)"'
    reg_jpgimgs=r'<img src="(.*?.jpg)"'
    contents = re.findall(reg_content,unicodePage,re.S)
    supports = re.findall(reg_support,unicodePage)
    print len(contents)
    num=1
    for i in range(len(supports)-1):
        if int(supports[i])>300:
            print supports[i]
            gifimgs=re.findall(reg_gifimgs,contents[i])
            if(gifimgs):
                print '================================================='
                littenum=1
                savePath = 'd:/temp/'+str(page)+'-'+str(num)+'-'+str(littenum)
                for gif in gifimgs:
                    gifdata = urllib2.urlopen(gif).read()
                    gifFile = open(savePath+'.gif','wb')
                    gifFile.write(gifdata)
                    gifFile.close()
                    littenum+=1
                num+=1
            else:
                print '#################################################'
                jpgimgs=re.findall(reg_jpgimgs,contents[i])
                if(jpgimgs):
                    littenum=1
                    savePath = 'd:/temp/'+str(page)+'-'+str(num)+'-'+str(littenum)
                    for jpg in jpgimgs:
                        jpgdata = urllib2.urlopen(jpg).read()
                        jpgFile = open(savePath+'.jpg','wb')
                        jpgFile.write(jpgdata)
                        jpgFile.close()
                        littenum+=1
                    num+=1






