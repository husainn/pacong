#进程间通信
import time
from multiprocessing import Process,Queue

def download(q):
    pics = ['book.jpg','book2.jpg','book3.jpg']
    for pic in pics:
        time.sleep(0.1)
        q.put(pic)
        print('{}下载完成'.format(pic))

def getfile(q):
    while True:
        try:
            file = q.get(timeout=2)
            print('{}保存成功'.format(file))
        except:
            print('保存完成')
            break

if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download,args=(q,))
    p2 = Process(target=getfile,args=(q,))

    p1.start()
    p2.start()
    # p1.join()
    p2.join()

    print('main process done')