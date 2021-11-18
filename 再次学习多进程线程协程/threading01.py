#线程
'''
    考虑？创建线程？如何使用线程
    t = threading02.Thread(target=download,name='aa',args=(1,))
    t.start()

    线程：
    新建 就绪 运行 阻塞 结束
'''

import threading
import time


def download(n):
    imanges = ['girl.jpg','boy.jpg','man.jpg']
    for imange in imanges:
        print('正在下载{}'.format(imange))
        time.sleep(n)
        print('完成下载{}'.format(imange))

def listenMusic(n):
    musics = ['东风破','夜曲','彩虹','马德里']
    for music in musics:
        print('正在听{}'.format(music))
        time.sleep(n)
        print('听完了{}'.format(music))

if __name__ == '__main__':
    t1 = threading.Thread(target=download,args=(1,))
    t2 = threading.Thread(target=listenMusic,args=(1.5,))
    t1.start()
    t2.start()
    t2.join()
    print('完成任务')


