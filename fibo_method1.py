"""
generate fibonacci series in the child process
using first method : passing a function to the constructor

"""

import multiprocessing
import sys


def fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    print(f"Fibonacci sequence up to index {n}: {fib_sequence}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python fib_method1.py <index>")
        sys.exit(1)

    try:
        index = int(sys.argv[1])
        if index < 1:
            raise ValueError("Index should be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    process = multiprocessing.Process(target=fibonacci, args=(index,))
    process.start()
    process.join()
