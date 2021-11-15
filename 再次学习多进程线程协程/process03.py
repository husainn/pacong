'''
进程用来实现运算类的
显示用来io操作类的
- 实现多任务的方式：
    -多进程模式
    - 多线程模式
    - 协程
    进程 》线程》协程

    进程
    from multiprocessing import Process

    process = Process(target = 函数,name = 进程的名字,args=(给进程传递的参数))
    process 对象
    对象调用方法：
    process.start() 启动进程并执行任务
    process.run()  只是执行了任务，但是没有启动进程
    terminate() 终止进程

'''

from multiprocessing import Process
from time import sleep
import os

m = 1

def task1(s):
    global m
    while True:
        m+=1
        sleep(s)
        print('这是任务1........',m)

def task2(s):
    global m
    while True:
        m += 1
        sleep(s)
        print('这是任务2........',m)

if __name__ == '__main__':
    #子进程
    print(os.getpid())
    p = Process(target=task1,name='任务1',args=(1,))
    p.start()
    p1 = Process(target=task2,name='任务2',args=(2,))
    p1.start()

    while True:
        sleep(1)
        m+=1
        print('--------->main',m)



