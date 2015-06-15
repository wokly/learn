# coding: UTF-8
__author__ = 'wen'

import urllib2
import re
import thread
import time

class Spider_Model:
    def __init__(self):
        self.page =1
        self.pages=[]
        self.enable=False
    def GetPage(self,page):
        myUrl='http://www.qiushibaike.com/text/page/'+page+'?s=4780945'
        req = urllib2.Request(myUrl,headers={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
        myRespons=urllib2.urlopen(req)

        myPage = myRespons.read()
        unicodePage=myPage.decode('utf-8')

        myItems = re.findall('<div class="content".*?</div>',unicodePage,re.S)
        items = []
        for item in myItems:
            item.replace('<div class="content">', '')
            item.replace('/div>','')
            items.append(item)
        return items

    def LoadPage(self):
        while self.enable:
            if len(self.pages)<2:
               try:
                   myPage = self.GetPage(str(self.page))
                   self.page +=1
                   self.pages.append(myPage)
               except:
                   print'无法链接糗事百科'
            else:
                time.sleep(1)

    def ShowPage(self,nowPage,page):
        for items in nowPage:
            print u'第%d页' %page , items
            myInput = raw_input()
            if myInput =="quit":
                self.enable = False
                break

    def Start(self):
        self.enable = True
        page = self.page
        print u'正在加载中请稍候......'

        thread.start_new_thread(self.LoadPage,())

        while self.enable:
            if self.pages:
                nowPage=self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage,page)
                page+=1

print u'请按下回车浏览今日的糗百内容：'
raw_input(' ')
myModel = Spider_Model()
myModel.Start()
