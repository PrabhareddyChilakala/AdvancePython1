from threading import Thread
from queue import Queue
import time
class Producer():
    def __init__(self):
        self.q=Queue()
    def produce(self):
        for i in range(1,6):
            print('item produced',i)
            self.q.put(i)
            time.sleep(1)
class Consumer():
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        for i in range(1,6):
            print('item received',self.prod.q.get(i))
p=Producer()
c=Consumer(p)
t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
t1.daemon=True
print(t1.daemon)
t1.start()
t2.start()

