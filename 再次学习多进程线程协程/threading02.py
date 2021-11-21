'''
线程可以共享全局变量
GIL 全局解释器锁
'''

import threading

ticket = 10000000

def task():
    global ticket
    for i in range(1000000):
        ticket-=1
    # print('task1中的ticket的值是:',ticket)

if __name__ == '__main__':
    t1 = threading.Thread(target=task)
    t2 = threading.Thread(target=task)

    t1.start()
    t2.start()
    t2.join()

    print(ticket)
