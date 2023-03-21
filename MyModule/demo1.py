# from collections import defaultdict
# dd=defaultdict(float)
# # dd['a']=600
# # dd['a']=200
# # dd['c']
# # dep=[('sales','john doe'),
# #      ('sales','martin smith'),
# #      ('accounting','john'),
# #      ('marketing','elizabeth')]
# incomes=[('books',1250.00),
#          ('books',1300.00),
#          ('books',1420.00),
#          ('tutorials',560.00),
#          ('tutorials',630.00),
#          (',courses',2500.00),
#          ('courses',2430.00),
#          ('courses',2750.00)]
# # for d,e in dep:
# #     dd[d].append(e)
# # print(dd)
# d=defaultdict(float)
# # str1='asdsadsfgfg'
# for p,e in incomes:
#     d[p]+=e
# print(d)
# # named tuple
# from collections import namedtuple
# person=namedtuple('p','name age place')
# x=person('prabha',22,'guntur')#p(name='prabha', age=22, place='guntur')
# hcl=namedtuple('developers','name level language',defaults=['jr','c'])
# dev=hcl('steve','inter')#output: developers(name='steve', level='inter', language='c')
# print(x)
import random
# from collections import deque
# dq=deque()
# dq.append(10)
# dq.append(20)
# dq.appendleft(30)
# dq.append(2)
# dq.popleft()
# print(dq)

# Generators
# import sys
# wgl=[i**2 for i in range(1000000)]#-using comprahension[]
# g=(i**2 for i in range(1000000))#-using generators()
# print(sys.getsizeof(wgl))
# print(sys.getsizeof(g))

# processing
# import multiprocessing as p
# def cal():
#     print("Process 1")
#     for i in range(10):
#         print(i**3)
# def cal2(num):
#     print("Process 2")
#     for i in range(num):
#         print(i**4)
# if __name__=='__main__':
#     print(p.cpu_count())
#     p1=p.Process(target=cal)
#     print(p1.name)
#     p2=p.Process(target=cal2,args=(10,))
#     print(p2.name)
#     p1.start()
#     p1.join()
#     print(p1.pid)
#     p2.start()
#     p2.join()
#     print(p2.pid)

# import multiprocessing
# def square(x):
#     return x*x
# if __name__=='__main__':
#     with multiprocessing.Pool(processes=4) as pool:
#         result=pool.map(square,[1,2,3,4,5])
#     print(result)#[1, 4, 9, 16, 25]

# import multiprocessing
# def cal_square(numbers,q):
#     for i in numbers:
#         q.put(i*i)
# def adding(numbers,q):
#     for i in numbers:
#         q.put(i+i)
# if __name__=='__main__':
#     num=[1,2,3,4,5]
#     q=multiprocessing.Queue()
#     p1=multiprocessing.Process(target=cal_square,args=(num,q))
#     p2=multiprocessing.Process(target=adding,args=(num,q))
#     print(p1.name)
#     p1.start()
#     p1.join()
#     print(p2.name)
#     p2.start()
#     p2.join()
#     while q.empty() is False:
#         print(q.get())

from concurrent.futures import ThreadPoolExecutor
import time
import random
def study():
    for i in range(5):
        print("I am reading book")
        time.sleep(2)
def listening():
    for i in range(5):
        print("listening to music")
        time.sleep(3)
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(study)
        pool.submit(listening)