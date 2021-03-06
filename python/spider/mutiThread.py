#coding:utf-8
import threading
import time
from Queue import Queue
import urllib2
import re


startPage=1600
endPage=1700
condition = 200

#爬取页码范围
#Producer thread
class Producer(threading.Thread):
    def __init__(self, t_name, queue,pagequeue):
        threading.Thread.__init__(self, name=t_name)
        self.urls=queue
        self.pages=pagequeue
    def run(self):
        while not self.pages.empty():
            page=self.pages.get(1,2)
            headersversion='Mozilla/4.0 (compatible; MSIE 5.'+self.getName()+'; Windows NT) '
            myUrl ='http://jandan.net/aabb/page-'+str(page)+'#comments'
            #请求头域
            req = urllib2.Request(myUrl, headers={
                'Connection': 'Keep-Alive',
                'Accept': 'text/html, application/xhtml+xml, */*',
                'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
             "User-Agent":headersversion
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

            print '正在处理第'+str(page)+'页。共有'+str(len(contents))+'个链接'
            num=0

            for i in range(len(supports)-1):
                if int(supports[i])>condition:
                    gifimgs=re.findall(reg_gifimgs,contents[i])
                    if(gifimgs):
                        imgurls = [gifimgs,page,num]

                    else:
                        jpgimgs=re.findall(reg_jpgimgs,contents[i])
                        if(jpgimgs):
                            imgurls=[jpgimgs,page,num]
                    self.urls.put(imgurls)
                    num+=1
            print '符合condition的url有'+str(num)+'个'
            time.sleep(2)

#Consumer thread


class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.urls = queue

    def run(self):
        num=0
        headersversion='Mozilla/4.1 (compatible; MSIE 5.'+self.getName()+'; Windows NT) '
        while 1:
            imgurl=self.urls.get(1.10)

            url = imgurl[0]
            page = imgurl[1]
            num = imgurl[2]
            if url[0].endswith('gif'):
                filetype = '.gif'
            else:
                filetype = '.jpg'

            littlenum = 1
            savePath = 'g:/temp/'+str(page)+'-'+str(num)+'-'+str(littlenum)+filetype

            for imgurl in url:
                        imgreq = urllib2.Request(imgurl,headers={
                        'Connection': 'Keep-Alive',
                        'Accept': 'text/html, application/xhtml+xml, */*',
                        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                         "User-Agent":headersversion
                        })
                        imgdata=urllib2.urlopen(imgreq).read()
                        imgFile = open(savePath, 'wb')
                        imgFile.write(imgdata)
                        imgFile.close()
                        littlenum+= 1
                        time.sleep(1)

            print "线程"+self.getName()+ str(num)
            print str(page)+'-'+str(num)+'-'+str(littlenum)
            num=num+1

#Main thread
def main():
    pagequeue = Queue()
    queue = Queue()
    for page in range(startPage,endPage):
        pagequeue.put(page)

    producers=[]
    consumers=[]

    for i in range(3):
        producer=Producer(i,queue,pagequeue)
        producer.start()
        producers.append(producer)


    for i in range(6):
        consumer=Consumer(i,queue)
        consumer.start()
        consumers.append(consumer)

    for i in range(3):
        producers[i].join
    for i in range(6):
        consumers[i].join
    print 'All threads terminate!'

if __name__ == '__main__':
    st = time.time()
    main()
    print '%f'%(time.time()-st)