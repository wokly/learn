#coding:utf-8
import threading
import time
import Queue
import urllib2
import re


startPage=1510
endPage=1560
condition = 200
urls=[]
#爬取页码范围
for page in range(startPage,endPage):

    myUrl ='http://jandan.net/ooxx/page-'+str(page)+'#comments'
    #请求头域
    req = urllib2.Request(myUrl, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
     "User-Agent":'Mozilla/4.1 (compatible; MSIE 5.6; Windows NT)'
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

    print '正在处理第'+str(page)+'页。公有'+str(len(contents))+'个链接'
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
                    urls.append(imgurls)
            num+=1
    print '符合condition的url有'+str(num)+'个'
    time.sleep(1)


def main():
    urlQueue=Queue.Queue()
    print 'urlslen=',len(urls)
    for imgurl in urls:
        print "+++++++++++++++++++++++"
        url = imgurl[0]
        page = imgurl[1]
        num = imgurl[2]
        print url[0]
        if url[0].endswith('gif'):
            filetype = '.gif'
        else:
            filetype = '.jpg'

        littlenum = 1
        savePath = 'g:/temp/'+str(page)+'-'+str(num)+'-'+str(littlenum)+filetype

        for imgurl in url:
                    imgdata = urllib2.urlopen(imgurl).read()
                    imgFile = open(savePath, 'wb')
                    imgFile.write(imgdata)
                    imgFile.close()
                    littlenum+= 1
                    time.sleep(1)



if __name__ == '__main__':
    st = time.time()
    main()
    print '%f'%(time.time()-st)