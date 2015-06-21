#coding=utf-8
#调用thread模块中的start_new_thread()函数来产生新线程
__author__ = 'wen'
import time
import thread
def timer(no,interval):
    cnt = 0
    while cnt< 10:
        print 'Thread:(%d) Time:%s\n'%(no,time.ctime())
        time.sleep(interval)
        cnt +=1
    thread.exit_thread()

def test():
    thread.start_new_thread(timer,(1,2))
    thread.start_new_thread(timer,(2,4))

if __name__ =='__main__':
    test()
    time.sleep(100)
