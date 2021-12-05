#协程：微线程
#进程>线程>协程

#Process Thread 生成器完成
import time


def task1():
    for i in range(3):
        print('A'+str(i))
        yield
        time.sleep(1)

def task2():
    for i in range(3):
        print('B'+str(i))
        yield
        time.sleep(3)

if __name__ == '__main__':
    g1 = task1()
    g2 = task2()
    while True:
        try:
            next(g1)
            next(g2)
        except:
            break
