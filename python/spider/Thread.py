#coding:utf-8
import threading
import time
import Queue
import urllib2
import re
for page in range(6747,6758):
    print 'page=',page
    myUrl ='http://jandan.net/pic/page-'+str(page)+'#comments'
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
    urls=[]
    for i in range(len(supports)-1):
        if int(supports[i])>100:
            gifimgs=re.findall(reg_gifimgs,contents[i])
            if(gifimgs):
                imgurls = [gifimgs,page,num]

            else:
                jpgimgs=re.findall(reg_jpgimgs,contents[i])
                if(jpgimgs):
                    imgurls=[jpgimgs,page,num]
                    urls.append(imgurls)
            num+=1
class MyThread(threading.Thread):
    def __init__(self,urlQueue):
        threading.Thread.__init__(self)
        self.urlQueue=urlQueue



    def run(self):
        print "+++++++++++++++++++++++"
        imgurl = self.urlQueue.get()
        url = imgurl[0]
        page = imgurl[1]
        num = imgurl[2]
        print url[0]
        if url[0].endswith('gif'):
            filetype = '.gif'
        else:
            filetype = '.jpg'

        littlenum = 1
        savePath = 'd:/temp/'+str(page)+'-'+str(num)+'-'+str(littlenum)+filetype

        for imgurl in url:
                    imgdata = urllib2.urlopen(imgurl).read()
                    imgFile = open(savePath, 'wb')
                    imgFile.write(imgdata)
                    imgFile.close()
                    littlenum+= 1
        self.urlQueue.task_done()
def main():
    urlQueue=Queue.Queue()
    print 'urlslen=',len(urls)
    for url in urls:
        urlQueue.put(url)
    for i in range(len(urls)):
        t = MyThread(urlQueue)
        t.setDaemon(True)
        t.start()



    urlQueue.join()

if __name__ == '__main__':
    st = time.time()
    main()
    print '%f'%(time.time()-st)