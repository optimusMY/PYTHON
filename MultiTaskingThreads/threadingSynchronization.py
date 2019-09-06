'''
import threading
import time



def print_epoch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "---------", time.time())

def print_cube(num):
    print("Cube = {}".format(num*num*num))

def print_sqare(num):
    print("Sqare = {}".format(num*num))

if __name__ == "__main__":
    t1 = threading.Thread(target=print_cube, args=(2,))
    t2 = threading.Thread(target=print_sqare, args=(2,))
    t3 = threading.Thread(target=print_epoch, args=("Thread epoch", 1, ))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Done")

'''


'''------------------------------------------------------------------------------
import threading
import time


def print_epoch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "---------", time.time())

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("start thread:", self.name)
        print_epoch(self.name, self.delay)
        print("end thread:", self.name)


if __name__ == "__main__":

    t1 = MyThread("T-1", 1)
    t2 = MyThread("T-2", 2)

    t1.start()
    t2.start()

    print(t1.getName())
    print(t2.getName())
    print(threading.activeCount())
    print(threading.currentThread())
    print(threading.enumerate())

    t1.join()
    t2.join()

    print("Done")

'''




'''
if you dont use lock
t1 and t2 will manipulate x unconciously 
therefore x will be wrong because of simultaneous manipulation
'''
import threading
x = 0

def thread_task(lock):
    global x
    for i in range(100000):
        lock.acquire()
        x += 1
        lock.release()

def main_task():
    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main_task()
    print("{0}".format(x))



