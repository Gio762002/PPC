import sys
import threading
from queue import Queue
import statistics

def worker(queue, ready):
    print("Starting thread:", threading.current_thread().name)
    ready.wait()
    data = queue.get()
    operation = queue.get()

    if operation == 'min':
        print("min:", min(data))
    elif operation == 'max':
        print("max:", max(data))
    elif operation == 'mean':
        print("mean:", statistics.mean(data))
    elif operation == 'median':
        print("median:", statistics.median(data))
    elif operation == 'standard deviation':
        print("standard deviation:", statistics.stdev(data))
    print("Ending thread:", threading.current_thread().name)

if __name__ == "__main__":
    print("Starting thread:", threading.current_thread().name)
    operations = ['min', 'max', 'mean', 'median', 'standard deviation']
    data = [2,34,45,5,2,122,3,4,45,98,57]
    
    queue = Queue()
    ready = threading.Event()
    
    thread1 = threading.Thread(target=worker, args=(queue, ready))
    thread2 = threading.Thread(target=worker, args=(queue, ready))
    thread3 = threading.Thread(target=worker, args=(queue, ready))
    thread4 = threading.Thread(target=worker, args=(queue, ready))
    thread5 = threading.Thread(target=worker, args=(queue, ready))    

    threads = [thread1, thread2, thread3, thread4, thread5]
    for i in range(len(threads)):    
        threads[i].start() 
        queue.put(data)
        queue.put(operations[i])
        ready.set()

        threads[i].join()
    
    print("Ending thread:", threading.current_thread().name)