import multiprocessing
class Myclass(multiprocessing.Process):
    def demo1(self):
        print('hello from demo1')
    def run(self) -> None:
        self.demo1()
if __name__=='__main__':
    p=Myclass()
    p.start()