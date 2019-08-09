
'''
Threading vs Multiprocessing

Threading:
- A new thread is spawned within the existing process
- Starting a thread is faster than starting a process
- Memory is shared between all threads
- Mutexes often necessary to control access to shared data
- One GIL (Global Interpreter Lock) for all threads

Multiprocessing:
- A new process is started independent from the first process
- Starting a process is slower than starting a thread
- Memory is not shared between processes
- Mutexes not necessary (unless threading in the new process)
- One GIL (Global Interpreter Lock) for each process

from threading import Thread
import os
import math

def calc():
	for i in range(0, 4000000):
		math.sqrt(i)

threads = []

for i in range(os.cpu_count()):
	print('registering thread %d' % i)
	threads.append(Thread(target=calc))

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()




from multiprocessing import Process
import os
import math
from multiprocessing.dummy import freeze_support


def calc():
    for ix in range(0, 70000000):
        math.sqrt(ix)


processes = []

for i in range(os.cpu_count()):
    print('registering process %d' % i)
    processes.append(Process(target=calc))

for process in processes:
    process.start()

for process in processes:
    process.join()
'''









'''
class Hello:
    def run(self):
        for i in range(5):
            print("Hello")

class Hi:
    def run(self):
        for i in range(5):
            print("Hi")



tsk1 = Hello()
tsk2 = Hi()

#as you will see that tsk2 runs after tsk1 run method, but wa want them to run simultaneously
tsk1.run()
tsk2.run()
'''


'''so we have to define the classes as Thread like below
Hello and Hi are child of Thread Class
IT IS VERY IMPORTANT TO NOTICE THAT run() methods in classes are overriding methods for Thread class
so in order to run run()methods in classes simultaneously  we have to call start() method from class instances
start method calls run methods internally



from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(500):
            print("Hello")
            sleep(0.1)


class Hi(Thread):
    def run(self):
        for i in range(500):
            print("Hi")
            sleep(0.1)


tsk1 = Hello()
tsk2 = Hi()

#
tsk1.start()
sleep(0.5)  # 100msec gap between two tasks to prevent collision(executing both run() at once)
tsk2.start()
# mainthread is responsible for execution of the tsk1.run tsk2.run and print("Bye")
print("Bye")  # so we will see "Bye" somewhere in Hi and Hello in console
'''






'''if we dont wanna execute print("Bye") with tsk1 and tsk2 simultaneously, 
we have to remind mainthread by task.join() method like below
tsk1 = Hello()
tsk2 = Hi()

tsk1.start()
sleep(0.5)  # 100msec gap between two tasks to prevent collision(executing both run() at once)
tsk2.start()

tsk1.join()
tsk2.join()

print("Bye")  # now we will see Bye at the end of the tasks

'''

'''ANOTHER THREAD EXAMPLE
import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
'''


'''ANOTHER EX
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")
'''

'''ANOTHER EX
import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      # Get lock to synchronize threads
      threadLock.acquire()
      print_time(self.name, self.counter, 3)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")
'''

'''ANOTHER EX
import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      process_data(self.name, self.q)
      print ("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = q.get()
         queueLock.release()
         print ("%s processing %s" % (threadName, data))
      else:
         queueLock.release()
         time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")
'''

Sharing Data Between Processes using Array
Implementing Multiprocessing Locks
Sharing Data Between Processes using Value


