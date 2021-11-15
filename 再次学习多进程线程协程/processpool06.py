#阻塞式进程
import time
from random import random
from multiprocessing import Pool
import os

def task(task_name):
    print('开始任务了！{}'.format(task_name))
    start = time.time()
    time.sleep(random()*2)
    end = time.time()
    print('完成任务:{},用时{}，进程id{}'.format(task_name,(start-end),os.getpid()))


if __name__ == '__main__':
    tasks = ['听音乐','吃饭','洗衣服','打游戏','散步','看孩子','做饭']
    pool = Pool(5)
    for task1 in tasks:
        pool.apply(task,args=(task1,))
    pool.close()
    pool.join()

    print('over')