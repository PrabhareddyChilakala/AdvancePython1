import multiprocessing
def sender(conn):
    conn.send('hello')
    conn.close()
def reciever(conn):
    msg=conn.recv()
    conn.close()
    print(msg)
if __name__=='__main__':
    parent_conn,child_conn=multiprocessing.Pipe()
    p1=multiprocessing.Process(target=sender,args=(child_conn,))
    p2=multiprocessing.Process(target=reciever,args=(parent_conn,))
    print(p1.name)
    p1.start()
    p1.join()
    print(p2.name)
    p2.start()
    p2.join()