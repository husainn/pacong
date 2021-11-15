'''
- 实现多任务的方式：
    -多进程模式
    - 多线程模式
    - 协程
    进程 》线程》协程

    进程
'''

from multiprocessing import Process
from time import sleep
import os

def task1():
    while True:
        sleep(1)
        print('这是任务1........',os.getpid(),'-----',os.getppid())

def task2():
    while True:
        sleep(2)
        print('这是任务2........',os.getpid(),'-----',os.getppid())

if __name__ == '__main__':
    #子进程
    print(os.getpid())
    p = Process(target=task1,name='任务1')
    p.start()
    print(p.name)
    p1 = Process(target=task2,name='任务2')
    p1.start()
    print(p1.name)