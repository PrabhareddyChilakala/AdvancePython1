import multiprocessing
def cal_square(numbers,res):
    for i,n in enumerate(numbers):
        res[i]=n*n
def adding(numbers,res,v):
    v.value=5
    for i,n in enumerate(numbers):
        res[i]=n+n
if __name__=='__main__':
    num=[1,2,3,4,5]
    res=multiprocessing.Array('i',5)
    v=multiprocessing.Value('d',)
    p1=multiprocessing.Process(target=cal_square,args=(num,res))
    p2=multiprocessing.Process(target=adding,args=(num,res,v))
    print(p1.name)
    p1.start()
    p1.join()
    print(res[:])
    print(p2.name)
    p2.start()
    p2.join()
    print(res[:],v.value)