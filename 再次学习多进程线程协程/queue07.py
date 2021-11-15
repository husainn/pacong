#进程间通信,Queue

from multiprocessing import Queue

q = Queue(5)

q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E')
print(q.qsize())

if not q.full():
    q.put('F')  #put() 如果queue满了只能等待，除非有‘空地’则添加成功
else:
    print('队列已满！')

#从队列中取值
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get(timeout=2))


