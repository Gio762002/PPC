"""
generate fibonacci series in the child process
using second method : subclassing Process and defining its run() method to implement your algorithm.
"""

from multiprocessing import Process
import sys

class Fibonacci(Process):
    def __init__(self,n):
        super().__init__()
        self.a = 0
        self.b = 1
        self.n = int(n)

    def run(self):
        fib = [self.a, self.b]
        for i in range(self.n-1):
            fib.append(fib[-1] + fib[-2])
        print(fib)

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print("Usage: python fibo_method2.py <index>")
        sys.exit(1)

    try:
        index = int(sys.argv[1])
        if index < 1:
            raise ValueError("Index should be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    f = Fibonacci(index)
    f.start()
    print(f"Fibonacci sequence up to index {index}")
    f.join()
