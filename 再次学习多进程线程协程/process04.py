#进程：自定义
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        n = 1
        while True:
            n+=1
            print('{}------->自定义进程：{}'.format(n,self.name))

if __name__ == '__main__':
    p = MyProcess('小明')
    p.start()

    p1 = MyProcess('小红')
    p1.start()